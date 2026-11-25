# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 13: Organ Offer Calls and Retrieval Logistics. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator at night at a nurses' station on a phone call, reading back details from a structured form.",
    "objectives": [
        "Run an organ offer call with a structured script and read-back of identifiers, blood group, and times.",
        "Treat any discrepancy on an offer as a safety event and stop the process until it is resolved.",
        "Convene the people who decide acceptance and readiness, quickly and in the right order.",
        "Coordinate transport and timing with the procurement team within DOH transport arrangements.",
        "Log the offer timeline for safety review, logistics, and claims evidence.",
    ],
    "big": """
{{plain:An organ offer call is like air traffic control at night. Several people who cannot see each other must agree, in minutes, on exactly what is arriving, where, and when. Controllers do not trust memory: they use set phrases and read everything back. A single wrong digit, unspoken, can put two planes on one runway.}}
{{fig:rtc13_offer}}
<p>The picture has a limit. Air traffic control has radar to check the words against. On an offer call, the words are often all you have until the organ and its paperwork arrive. That is why the structure of the call, and the read-back, carry so much weight. And unlike a flight, a kidney has a clock: the longer it is stored outside a body, the more its early function tends to suffer, so delays have a real cost.</p>
<p>Your job is to capture the offer exactly, route it to the person who decides acceptance, bring the right people together in the right order, and keep a timeline. You never accept an organ, and you never assume a discrepancy is a typo.</p>
{{cards:Key terms for this module|Organ offer::A call proposing a specific deceased-donor organ for a specific candidate.|Read-back::Repeating critical details to the caller and getting confirmation.|Acceptance::The clinical decision to accept an offer, made by the transplant physician or surgeon on call.|Cold ischemia time::The time a kidney spends cooled and stored between retrieval and transplantation.|Readiness huddle::A short meeting to confirm that the recipient and team are ready to proceed.}}
""",
    "case": {"title": "2:10 a.m.", "html": """
<p>At 2:10 a.m. your mobile rings. The caller from the procurement team says a deceased-donor kidney is available and your candidate, Mr. Nestor Villareal, 49, is first for it. She reads quickly: donor age, cause of death, blood group &ldquo;A,&rdquo; retrieval time, and that the kidney will be on cold storage.</p>
<p>Your waiting-list sheet says Mr. Villareal is blood group O. The caller is in a hurry and says, &ldquo;It&rsquo;s probably fine, they double-checked the matching.&rdquo;</p>
<p>The on-call transplant surgeon, Dr. Paolo Ramirez, is not answering his phone.</p>
""", "questions": ["What do you do about the blood group?",
                  "Whom do you call, in what order, if the surgeon does not answer?",
                  "What goes into the offer log?"]},
    "sections": [
        ("script", "Make urgent communication structured", "A script you can use at 2 a.m.", """
<p>Night calls happen when people are tired. A printed script, kept by the phone and in the on-call bag, protects everyone.</p>
{{flow:A structured offer call|Caller and callback::Name, organization, direct callback number, time of call.|Candidate identity::Full name and two identifiers, read back.|Organ and donor summary::Organ, donor blood group, key donor information the caller provides, read back.|Times::Retrieval or cross-clamp time, expected arrival, storage method, read back.|Logistics::Transport plan, who carries the organ and documents, where it will arrive.|Next contact::When you will call back with the clinical decision, and to whom.}}
<p>Read back each block before moving on: &ldquo;I have blood group A, retrieval at 11:40 p.m., cold storage. Is that correct?&rdquo; Write directly on the form, not on scraps of paper.</p>
{{key:Use the script, write on the form, and read back every critical detail before the call ends.}}
"""),
        ("discrepancy", "A discrepancy is a safety event", "Stop, read back, escalate", """
<p>Some discrepancies are clerical; some are the first sign of a wrong-organ or wrong-patient error. You cannot tell which from the phone. Treat them all as safety events.</p>
<div class="table-wrap"><table>
<thead><tr><th>Discrepancy</th><th>Why it matters</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Blood group differs from your record</td><td>An ABO-incompatible kidney can be rejected within hours in a standard transplant</td><td>Stop; read back; escalate to the transplant physician at once; nothing proceeds until resolved</td></tr>
<tr><td>Candidate identifiers do not match</td><td>Wrong patient</td><td>Stop; verify with the caller and your record; escalate</td></tr>
<tr><td>Times do not add up</td><td>Storage time may be longer than stated</td><td>Clarify and record; escalate</td></tr>
<tr><td>Missing documents expected with the organ</td><td>The team cannot verify on arrival</td><td>Record; escalate before the organ arrives</td></tr>
</tbody></table></div>
<p>&ldquo;It&rsquo;s probably fine&rdquo; is not resolution. Resolution is a verified fact from the source &mdash; for example, the donor blood-group documentation &mdash; reviewed by the transplant physician.</p>
{{key:Never assume a discrepancy is a typo. Stop, read back, escalate, and record the resolution.}}
"""),
        ("convene", "Bring the right people together", "Acceptance, readiness, logistics", """
<p>Acceptance is a clinical decision by the transplant physician or surgeon on call, under program protocol. The coordinator&rsquo;s job is to reach them fast and give them everything from the call. If the first person does not answer, use the escalation list in the role charter (Module 2): the backup surgeon, the transplant nephrologist on call, the program director. Record every attempt with times.</p>
<p>Once the offer is accepted, the work becomes logistics: contacting the candidate with the agreed message, arranging transport to the hospital, alerting the operating room, anesthesia, the HLA laboratory for the final crossmatch, the ward, and the pharmacy, and coordinating organ transport with the procurement team under DOH arrangements for organ transport.[[rtc_doh2025transport]] A short readiness huddle before surgery brings the gates together (Module 14).</p>
<p>When you call the candidate, give a calm, clear message: an organ may be available, the team is reviewing it, please come to the hospital, nothing to eat or drink as instructed, bring your medicines and documents. Do not promise that the transplant will happen; final checks can still stop it.</p>
{{key:Reach the decision maker first. Only after acceptance does the call become logistics, and the candidate hears &ldquo;may,&rdquo; not &ldquo;will.&rdquo;}}
"""),
        ("timeline", "Keep the timeline", "Why the log matters", """
<p>A kidney&rsquo;s storage time is associated with how well it works early after transplant, which is one reason programs move quickly. Record the times as they happen, not from memory afterward.</p>
<div class="table-wrap"><table>
<thead><tr><th>Time to record</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Offer call received; read-back completed</td><td>Shows the call was captured correctly</td></tr>
<tr><td>Each attempt to reach the decision maker</td><td>Shows escalation worked, or where it failed</td></tr>
<tr><td>Acceptance or decline, by whom</td><td>The clinical decision on record</td></tr>
<tr><td>Candidate contacted; arrival</td><td>Readiness and logistics</td></tr>
<tr><td>Organ arrival; documents checked</td><td>Chain of custody</td></tr>
<tr><td>Pre-authorization request for a deceased donor</td><td>Due within two working days after the procedure[[rtc_ph2026]]</td></tr>
</tbody></table></div>
{{scene:The log that explained a delay|<p>After a night offer, a recipient&rsquo;s kidney is slow to work. At the morning review, the coordinator&rsquo;s log shows that the organ arrived 90 minutes later than planned because the transport vehicle was redirected.</p>
<p>The program adds a confirmation call with the transport team at departure to its script.</p>
<p class="tc-scene-take">A log written in real time turned a vague worry into a fixable step.</p>}}
{{key:Write the times as they happen. The log serves safety review, logistics, and the claim.}}
"""),
    ],
    "debrief": ["""
<p><strong>The blood group.</strong> Stop. Read back: &ldquo;You said donor blood group A. Our candidate&rsquo;s record says group O.&rdquo; Ask the caller to verify from the donor documentation and to hold the process. Escalate to the transplant physician at once. A group A kidney is incompatible with a standard transplant into a group O recipient; nothing proceeds until the discrepancy is resolved from source documents and reviewed by the physician.</p>
<p><strong>The surgeon.</strong> Follow the escalation list in the role charter: the backup transplant surgeon, then the transplant nephrologist on call, then the program director. Record each attempt and its time. Do not accept or decline the offer yourself, and tell the caller when you will call back.</p>
<p><strong>The log.</strong> Time of call, caller and callback number, the read-back, the discrepancy and its resolution, every escalation attempt, the decision and who made it, the candidate contact, arrival times, and, if transplanted, the deceased-donor pre-authorization deadline.</p>
"""],
    "skills": {"title": "Offer-call drill",
               "intro": "Take a simulated night offer call with an injected discrepancy while your preceptor observes.",
               "items": [
                   ("Uses the structured script and writes directly on the form.", False),
                   ("Reads back identifiers, blood group, and times before ending the call.", True),
                   ("Stops and escalates a blood-group discrepancy without assuming a typo.", True),
                   ("Follows the escalation list when the first decision maker does not answer, recording each attempt.", True),
                   ("Calls the candidate with a calm message that uses &ldquo;may,&rdquo; not &ldquo;will.&rdquo;", False),
                   ("Completes the offer timeline log in real time.", False),
               ],
               "placement": "Review your program&rsquo;s offer script and on-call escalation list. Run one tabletop drill with the on-call team."},
    "terms": [("Organ offer", "A proposal of a specific organ for a specific candidate."), ("Read-back", "Repeating critical details for confirmation."),
              ("Acceptance", "The clinical decision to accept an offer."), ("Cold ischemia time", "Time a kidney spends cooled and stored."),
              ("Readiness huddle", "A short meeting confirming readiness to proceed.")],
    "readings": [("kidney-transplant.html", "What patients are told about receiving a call for a kidney.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["13"])
