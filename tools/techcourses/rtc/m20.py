# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 20: Integrated Capstone and International Practice. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator presenting a case timeline to a small group of colleagues in a training room.",
    "objectives": [
        "Coordinate one recipient and one donor from referral to follow-up, applying the four gates at every step.",
        "Handle simultaneous problems in the right order: safety first, then deadlines, then routine.",
        "Recognize and avoid the critical failures that cannot be averaged away in assessment.",
        "Compare Philippine practice with United States, United Kingdom, and Australian practice, and decide what to borrow and what needs local legal review.",
    ],
    "big": """
{{plain:Up to now each module has been one stretch of road. The capstone drives the whole route in one go, at night, in the rain, with two passengers who each need something different. The skill being tested is not knowing each stretch; it is knowing which problem to handle first when three arrive at once.}}
{{fig:rtc20_journey}}
<p>The picture has a limit. A real case is never driven in one sitting; it unfolds over months, with weeks of quiet between bursts of urgency. The capstone compresses that into a two-hour simulation so that a preceptor can see how you sort, route, and close. It also asks you to look outward: other countries have built coordinator roles, donor advocates, and independent checks that are worth learning from &mdash; and rules that do not apply here.</p>
<p>Use the same sorting rule as on any busy shift. First, anything that could harm a person now: a safety signal, a sensitizing event before an offer, a discrepancy, a donor in distress. Second, anything with a deadline that cannot be recovered: a pre-authorization about to lapse, a claim window closing, a courier leaving. Third, everything else, in the register with an owner and a date.</p>
{{cards:Key terms for this module|Capstone::A simulated integrated case scored by a preceptor.|Critical failure::An action so unsafe that it fails the capstone regardless of the total score.|Independent living donor advocate (ILDA)::A US role that represents only the donor; a comparison, not Philippine law.|Independent assessment::A UK process in which an independent assessor checks a living donation for consent and reward; a comparison.|Jurisdiction::The legal system a rule belongs to.}}
""",
    "case": {"title": "The capstone: four problems, one evening", "html": """
<p>You are the on-call coordinator from 5 p.m. to 8 a.m. Your caseload includes this pair: Mr. Ruben Garcia, 48, wait-listed and also awaiting a living donation from his friend of twenty years, Mr. Alvin Torres, 46, who is in evaluation.</p>
<p>5:20 p.m. Mr. Torres calls privately: he wants to withdraw, and he does not want Mr. Garcia to know why.</p>
<p>6:05 p.m. The Z Benefits lead emails that Mr. Garcia&rsquo;s pre-authorization, approved for the planned living-donor transplant, expires in nine days.</p>
<p>9:30 p.m. Mr. Garcia&rsquo;s wife messages that he received two units of blood at a local hospital yesterday after a fall.</p>
<p>1:45 a.m. The procurement team calls with a deceased-donor kidney offer for Mr. Garcia.</p>
""", "questions": ["In what order do you handle the four events, and why?",
                  "What exactly do you say to Mr. Garcia about the living donation?",
                  "What does the offer call require, given yesterday&rsquo;s transfusion?"]},
    "sections": [
        ("sort", "Sort, route, close", "The capstone method", """
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Category</th><th>Action</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Donor withdraws privately</td><td>Safety and rights</td><td>Thank him; confirm he may stop; record in his restricted record; inform his advocate and donor team; agree neutral wording</td><td>Donor advocate and donor team</td></tr>
<tr><td>Transfusion yesterday</td><td>Safety (sensitizing event)</td><td>Report tonight to the transplant physician and HLA laboratory; request the transfusion record</td><td>Transplant physician</td></tr>
<tr><td>Night offer</td><td>Safety and time</td><td>Structured call with read-back; tell the decision maker about the transfusion before any decision</td><td>Transplant surgeon or physician on call</td></tr>
<tr><td>Pre-authorization expiring</td><td>Deadline</td><td>Flag to the Z Benefits lead; the living-donor plan has closed, and a deceased-donor transplant follows its own pre-authorization rule (within two working days after the procedure)</td><td>Z Benefits lead</td></tr>
</tbody></table></div>
<p>The scoring has five dimensions, each 0 to 4: separation and privacy; routing to decision owners; timeliness; communication with each person; and documentation and loop closure. A pass needs 16 of 20, every dimension at least 2, and no critical failure.</p>
{{key:Safety first, unrecoverable deadlines second, everything else into the register. Every action names its owner.}}
"""),
        ("critical", "Critical failures", "What cannot be averaged away", """
<p>Some actions fail the capstone regardless of the score, because in real life they can cause harm that no amount of good work elsewhere undoes.</p>
<ul>
<li>Disclosing a donor&rsquo;s private reasons to the recipient or family.</li>
<li>Presenting a payment approval or a test result as clinical or ethical clearance.</li>
<li>Advancing a case with an unresolved coercion, identity, or document concern.</li>
<li>Letting a pre-authorization lapse without flagging it.</li>
<li>Accepting offer details without read-back, or passing over a discrepancy.</li>
<li>Failing to report a sensitizing event before a compatibility decision.</li>
<li>Giving medicine advice outside protocol.</li>
<li>Treating a sent message as a closed loop on an urgent matter.</li>
</ul>
{{key:A critical failure fails the capstone, because in practice it can cause harm no total score can repair.}}
"""),
        ("compare", "International practice", "Borrow principles, not laws", """
<p>Other countries have built transplant coordination over decades. Their experience is useful; their rules are theirs.</p>
<div class="table-wrap"><table>
<thead><tr><th>Country or body</th><th>What it does</th><th>What to borrow</th><th>What needs Philippine legal review</th></tr></thead>
<tbody>
<tr><td>United States: OPTN</td><td>Requires an independent living donor advocate (ILDA) and sets donor follow-up reporting points[[rtc_optn]]</td><td>A person who represents only the donor; structured follow-up</td><td>US advocate qualifications, reporting deadlines, and allocation scores</td></tr>
<tr><td>United States: ABTC</td><td>Separate certification paths for clinical and procurement coordinators, with experience requirements[[rtc_abtc]]</td><td>Clear separation of clinical and procurement roles</td><td>A US credential is not a Philippine qualification</td></tr>
<tr><td>United Kingdom: Human Tissue Authority</td><td>Independent assessment of living donations for consent and absence of reward[[rtc_hta]]</td><td>An independent check outside the transplant team</td><td>UK law and processes; the Philippine safeguard is the DOH order and the HTEC</td></tr>
<tr><td>Australia: state health services</td><td>Advanced nursing coordinator roles that include education, case conferences, and quality work</td><td>Coordinators who lead improvement, not only tasks</td><td>One employer&rsquo;s grade is not a national qualification</td></tr>
<tr><td>KDIGO and WHO</td><td>Global frameworks for candidates, donors, recipients, and ethical donation[[rtc_kdigo2020]][[rtc_kdigo2017]][[rtc_who2010]]</td><td>Evidence-based pathways; voluntariness and financial neutrality</td><td>Guidelines do not override Philippine law or authorize independent clinical acts</td></tr>
</tbody></table></div>
{{key:Borrow principles that fit Philippine safeguards; never apply a foreign deadline, credential, or allocation rule as if it were local law.}}
"""),
        ("next", "After the course", "Keeping it current", """
<p>The rules in this course will change. PhilHealth Circular 2026-0019 was published days before this course was written;[[rtc_ph2026]] DOH orders are revised; KDIGO updates its guidelines. Keep your source register current (Module 2), read every new circular for its effective date and legacy rule, and ask your program to review its role charter yearly.</p>
<p>Completing the course is an Academy learning record. It is not certification, CPD units, or a DOH or PhilHealth qualification. Competence is shown in practice, signed off by your preceptor, on your program&rsquo;s own procedures.</p>
{{key:Keep the source register current, read every rule for its effective date, and let practice, not paperwork, show competence.}}
"""),
    ],
    "debrief": ["""
<p><strong>Order.</strong> At 5:20 p.m., the donor&rsquo;s withdrawal (his rights and safety) and, as soon as you learn of it at 9:30 p.m., the transfusion (a sensitizing event) come first; both are routed the same evening. At 1:45 a.m., the offer call follows the script, and the transfusion is told to the decision maker before any decision. The pre-authorization flag goes to the Z Benefits lead the same evening; the living-donor plan has closed, so the team and lead decide what applies next.</p>
<p><strong>What Mr. Garcia hears.</strong> Only the neutral wording agreed with Mr. Torres and his team: &ldquo;The team is not able to proceed with this donor.&rdquo; Then support Mr. Garcia: he remains on the waiting list, and the team will talk with him about other options.</p>
<p><strong>The offer.</strong> Structured call with read-back of identifiers, blood group, and times; immediate escalation to the on-call surgeon or physician with the transfusion information; the HLA laboratory informed so it can advise on the crossmatch. If the transplant proceeds, the deceased-donor pre-authorization is due within two working days after the procedure, and two separate journeys continue: his, and Mr. Torres&rsquo;s, who still deserves the program&rsquo;s support and respect.</p>
"""],
    "skills": {"title": "Capstone simulation",
               "intro": "Complete the 120-minute capstone with injected events while your preceptor scores five dimensions.",
               "items": [
                   ("Sorts simultaneous events by safety, unrecoverable deadline, and routine, and explains the order.", True),
                   ("Handles a private donor withdrawal without disclosure, using agreed neutral wording.", True),
                   ("Reports a sensitizing event to the physician and HLA laboratory before a compatibility decision.", True),
                   ("Runs an offer call with read-back and escalation.", True),
                   ("Flags an expiring pre-authorization to the correct owner.", True),
                   ("Documents every action with time, owner, and closure evidence.", False),
                   ("Compares one foreign practice with Philippine safeguards and states what to borrow and what needs legal review.", False),
               ],
               "placement": "Present one real (de-identified) case from your program as a journey map, marking each gate and who closed it."},
    "terms": [("Capstone", "A simulated integrated case scored by a preceptor."), ("Critical failure", "An action that fails the capstone regardless of score."),
              ("ILDA", "Independent living donor advocate (US)."), ("Independent assessment", "A UK independent check of a living donation."),
              ("Jurisdiction", "The legal system a rule belongs to.")],
    "readings": [("kidney-transplant.html", "The patient guide, to revisit the whole journey from the patient&rsquo;s side."),
                 ("organ-donation-philippines.html", "Organ donation in the Philippines, for the public.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["20"])
