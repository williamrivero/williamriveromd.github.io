# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 01: The Coordinator as Navigator for Two People. Written for this series from published sources."""

MODULE = {
    "image_alt": "A transplant coordinator at a whiteboard with two separate colored pathway columns, explaining next steps to a calm adult recipient.",
    "objectives": [
        "Map the recipient&rsquo;s and the living donor&rsquo;s journeys as two separate pathways with separate decision rights.",
        "Apply the four-gate question (medical, legal, ethical, insurance) at every step of both pathways.",
        "Build a barrier register row that names an owner, a due date, and the evidence that will close it.",
        "Tell clinical coordination apart from procurement coordination, donor advocacy, and Z Benefits work.",
        "Write an SBAR request that asks a named decision maker for a specific decision by a specific time.",
    ],
    "big": """
{{plain:Picture an airport with two travelers who are going to the same city. One is a patient flying home for treatment; the other is a volunteer flying with them to help. Each has their own passport, their own ticket, their own baggage, and their own right to turn back at the gate. Both must clear the same four checkpoints &mdash; health, immigration, security, and the ticket counter &mdash; and no checkpoint will wave anyone through because another checkpoint already did. The transplant coordinator is the airline&rsquo;s escort for both travelers.}}
{{fig:rtc00_two_paths}}
<p>The picture has a limit. At an airport the volunteer is there for a short trip and comes home unchanged. A living kidney donor accepts a surgical risk and a small, lifelong change in kidney function, and gets no medical benefit from the operation. That is why the donor&rsquo;s checkpoints are not a copy of the recipient&rsquo;s. They are designed to protect someone who is healthy, and their gates include one the recipient does not face: the question of whether the gift is truly free.</p>
<p>Your job in this module is to learn the map. Most failures in a transplant program are not dramatic. A referral that nobody acknowledged. A test that expired the week before the case conference. A donor who wanted to stop but did not know how to say so in private. A family that believed a signed insurance form meant the surgery was approved. Each of these is a coordination failure, and each is preventable by the same habit: keep the two journeys separate, ask the four questions at every gate, and close each step with evidence from the person who owns it.</p>
{{cards:Key terms for this module|Recipient::The person with kidney failure who may receive the kidney.|Living donor::A healthy person who may give a kidney. The donor has their own team, record, rights, and choices.|Gate::A point where a decision must be made before the journey continues.|Four systems::Medical, legal, ethical, and insurance. Each gate asks all four questions.|Barrier register::A table of every open problem: who it affects, the owner, the next action, the due date, and what will prove it is closed.|SBAR::Situation, background, assessment, request: a short structure for asking someone to decide.}}
""",
    "case": {"title": "One family, two journeys, one folder", "html": """
<p>You have been the clinical transplant coordinator at a Quezon City transplant center for two weeks. Mrs. Lorna Bautista, 47, has been on hemodialysis for three years. Her younger brother, Mr. Ramon Castillo, 41, has started donor testing.</p>
<p>At 10:15 a.m. Mrs. Bautista calls, delighted. &ldquo;The PhilHealth form was signed this morning. So the operation is approved, right? Can we book it for next month?&rdquo;</p>
<p>At 11:40 a.m. Mr. Castillo stops you in the corridor and asks, very quietly, whether he is allowed to stop the tests. He does not say why. He asks you not to tell his sister.</p>
<p>At 2:00 p.m. the unit manager suggests a timesaver: &ldquo;Put the brother&rsquo;s papers in the sister&rsquo;s folder. One family, one folder. Easier for everyone.&rdquo;</p>
""", "questions": ["What is the next safe action for Mrs. Bautista, and what will you tell her about the PhilHealth form?",
                  "What is the next safe action for Mr. Castillo, and what may you not disclose?",
                  "How do you answer the unit manager, and what will you put in the barrier register today?"]},
    "sections": [
        ("two", "Two protected journeys", "One relationship, two people", """
<p>Start with the idea every later module rests on. A transplant links two people. It does not merge them.</p>
<p>The recipient seeks treatment for their own illness. The donor accepts a risk for someone else&rsquo;s benefit. Their interests overlap, but they are not the same, and sometimes they pull in opposite directions. A recipient may hope the donor never hesitates. A donor may need, at any point, to stop. The program serves both by keeping them apart where it matters: separate records, separate conversations, separate consent, separate contact preferences, and a separate team member who looks out for the donor alone.</p>
<div class="table-wrap"><table>
<thead><tr><th>Kept separate</th><th>Why</th><th>What may be shared</th></tr></thead>
<tbody>
<tr><td>Medical record and test results</td><td>Each person&rsquo;s health information belongs to them</td><td>Only what each person authorizes</td></tr>
<tr><td>Private conversations</td><td>A donor cannot speak freely with the recipient or family listening</td><td>Nothing, unless the person chooses</td></tr>
<tr><td>Reasons for stopping</td><td>A donor&rsquo;s reasons can expose them to pressure or blame</td><td>A neutral, agreed statement only</td></tr>
<tr><td>Insurance and funding plans</td><td>Different packages, different responsibilities</td><td>The shared timeline, when both agree</td></tr>
<tr><td>Next-step plans</td><td>Each person has different gates and deadlines</td><td>Milestones both have agreed to share</td></tr>
</tbody></table></div>
<p>The shared view &mdash; what a family sees on a joint update &mdash; shows only the milestones both people have agreed to share. Everything else lives in each person&rsquo;s own record. This is not secrecy for its own sake. The Department of Health (DOH) order on living donation builds the same separation into its safeguards: an advocate for the donor, separate psychosocial review, and the donor&rsquo;s right to withdraw.[[rtc_doh2021]]</p>
{{key:Two people, two records, two sets of rights. The shared view shows only what both have agreed to share.}}
{{scene:The joint update|<p>Coordinator Ms. Arlene Ramos gives a weekly phone update to a recipient and his wife. The wife asks whether the donor, a cousin, &ldquo;finished his blood tests.&rdquo;</p>
<p>Ms. Ramos answers: &ldquo;I can tell you everything about your husband&rsquo;s next steps. Your cousin&rsquo;s information is his to share; I&rsquo;ll let him know you asked.&rdquo; She then calls the cousin, who says he would rather update them himself.</p>
<p class="tc-scene-take">The update stayed useful, and the donor kept control of his own story.</p>}}
"""),
        ("gates", "Four systems at every gate", "Ask all four questions, every time", """
<p>At every step &mdash; referral, workup, approval, scheduling, discharge, transfer &mdash; ask four questions for each person.</p>
<ul>
<li><strong>Medical.</strong> Has the authorized clinician made the decision this step needs, on current results?</li>
<li><strong>Legal.</strong> Are the documents authentic, current, and complete, and is consent valid?</li>
<li><strong>Ethical.</strong> Are the protections complete: voluntariness, no reward, the advocate, the ethics committee review?</li>
<li><strong>Insurance.</strong> Is the funding route confirmed in writing, for this person, under the right version of the rule?</li>
</ul>
<p>The four systems do not answer for each other. A completed laboratory request is not a medical clearance. An insurance pre-authorization is not consent. A signed consent is not ethics approval. A free operating slot is not readiness. When a family hears &ldquo;the form was signed,&rdquo; they naturally hear &ldquo;it is approved.&rdquo; Part of your job is to say, gently and precisely, which approval that was and which ones are still open.</p>
{{fig:rtc01_register}}
<h3>The barrier register</h3>
<p>Every open problem gets one row. A row has ten fields: the person (by case pseudonym in any shared list), the system, the barrier, the risk if it stays open, the owner, the next action, the due date, the escalation contact, the status, and the closure evidence with its date. The last field is the one people skip, and it is the one that matters most. A row closes only when the service that owns it confirms the work is done &mdash; an appointment that happened, a result reviewed, a decision written. An email that left your outbox closes nothing.</p>
<p>The <a href="calc-transplant-coordinator-toolkit.html#tool-2">barrier register aging tool</a> in the toolkit turns a row&rsquo;s open date and due date into days open, days overdue, and an escalation tier.</p>
{{key:A sent message is not a closed loop. A row closes on evidence from the service that owns it.}}
{{scene:The cardiology referral|<p>On March 3 coordinator Mr. Paolo Navarro sends a cardiology referral for a recipient. On March 20 the register shows it as &ldquo;sent.&rdquo; He calls cardiology: no appointment exists; the fax went to a retired number.</p>
<p>He resends to the current number, gets a verbal acknowledgment with a name, books the slot himself through the clinic secretary, and updates the row: &ldquo;Appointment confirmed for March 27 by Ms. Ocampo, cardiology clinic.&rdquo; He closes it only after the visit note arrives.</p>
<p class="tc-scene-take">Seventeen days were lost to a status that described an action, not an outcome.</p>}}
"""),
        ("authority", "Coordinate within authority", "Who decides what", """
<p>The coordinator is the person who keeps the next step clear and follows it to completion. The coordinator is not the person who decides whether it happens. Learn the owners now; every later module uses this table.</p>
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Owner</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Recipient medical suitability</td><td>The transplant multidisciplinary team</td><td>Assemble the evidence, prepare the case conference, record the decision</td></tr>
<tr><td>Donor medical suitability</td><td>The donor&rsquo;s evaluating clinicians</td><td>Coordinate the workup on the donor&rsquo;s own pathway</td></tr>
<tr><td>Donor surgical consent</td><td>The surgeon, with independent witnessing under the DOH order</td><td>Arrange the meeting, interpreter, and witnesses</td></tr>
<tr><td>Ethics of a living donation</td><td>The Hospital Transplant Ethics Committee (HTEC)</td><td>Prepare a complete submission; track conditions</td></tr>
<tr><td>Benefits</td><td>PhilHealth and other payers, under the applicable circular</td><td>Assemble the request; track validity and deadlines</td></tr>
<tr><td>Organ acceptance</td><td>The transplant physician or surgeon on call</td><td>Capture the offer with read-back; convene the team</td></tr>
</tbody></table></div>
<p>Four job titles get confused. A <strong>clinical transplant coordinator</strong> guides recipients and donors through the program within a facility-assigned clinical scope. A <strong>procurement coordinator</strong> manages deceased donors and organ retrieval, a separate role the DOH defines for deceased donation.[[rtc_doh2010b]] A <strong>donor advocate</strong> is designated under the DOH living-donor order to protect the donor&rsquo;s interests; a job title or this course does not make anyone one.[[rtc_doh2021]] A <strong>Z Benefits Coordinator</strong> handles PhilHealth package navigation and evidence; each contracted facility must have at least one, and one coordinator may handle at most three Z packages.[[rtc_ph2026]] One person may hold more than one of these roles only if the hospital assigns them in writing and the conflicts are managed &mdash; and the recipient&rsquo;s coordinator should never quietly stand in for the donor&rsquo;s advocate.</p>
<h3>Asking for a decision: SBAR</h3>
<p>When you need a decision, ask in four parts. <strong>Situation:</strong> what needs deciding. <strong>Background:</strong> the facts the decision maker needs. <strong>Assessment:</strong> your view of the coordination problem &mdash; not a clinical judgment. <strong>Request:</strong> the specific decision, from whom, by when. &ldquo;FYI, some tests are old&rdquo; asks for nothing. &ldquo;Please decide by Friday whether the 14-month-old stress test must be repeated before Tuesday&rsquo;s conference&rdquo; asks for exactly one thing.</p>
{{key:You coordinate decisions; you do not make them. Every SBAR ends with a named person, one decision, and a time.}}
"""),
        ("why", "Why navigation matters", "What the evidence shows, and what it does not", """
<p>Why invest in a coordinator at all? Because transplantation is, for most people with kidney failure who can have one, the better long-term treatment &mdash; and because many people who could benefit never finish the steps to get there.</p>
<p>Start with the benefit. A systematic review of 110 cohort studies, covering about 1.9 million people, found that kidney transplantation was associated with lower mortality, fewer cardiovascular events, and substantially better quality of life than chronic dialysis.[[rtc_tonelli2011]] These were observational studies: healthier people are more likely to be transplanted, and no trial has randomized people to transplant or dialysis. A large United States registry study tried to reduce that bias by comparing transplant recipients only with people already on the waiting list. Death risk was higher in the first two weeks after transplant (relative risk 2.8, reflecting the operation itself) and then fell well below the wait-listed group, to a relative risk of 0.32 by 18 months.[[rtc_wolfe1999]] That early dip in safety is one reason readiness matters so much (Module 14).</p>
<p>Now the gap. People stall at different steps: interest, referral, the first visit, the workup, finding a donor. In a cluster randomized trial in 23 hemodialysis units in Ohio, 167 patients were assigned to monthly meetings with trained transplant-recipient navigators or to usual care. Navigated patients completed 3.5 transplant-process steps against 1.6 in the control group (difference 1.9 steps; 95% confidence interval 1.3 to 2.5), with similar effects across race and sex.[[rtc_sullivan2012]] The trial measured steps completed, a process outcome. It did not show that navigation increased the number of transplants or improved survival, and its navigators were peers, not hospital coordinators. Still, the mechanism is the one this course teaches: someone who knows the next step, removes the barrier, and follows up.</p>
<div class="table-wrap"><table>
<thead><tr><th>Claim</th><th>Strength</th><th>Say it as</th></tr></thead>
<tbody>
<tr><td>Transplant is associated with longer life than dialysis</td><td>Many consistent cohorts; no randomized trial</td><td>&ldquo;is associated with&rdquo;</td></tr>
<tr><td>Navigation increases steps completed</td><td>One randomized trial, 167 patients</td><td>&ldquo;a trial showed more steps completed&rdquo;</td></tr>
<tr><td>Navigation increases transplants</td><td>Not shown by that trial</td><td>&ldquo;has not been shown&rdquo;</td></tr>
</tbody></table></div>
{{key:Match your words to the evidence. &ldquo;Associated with&rdquo; for cohorts, &ldquo;showed&rdquo; for trials, and say what a study did not measure.}}
"""),
    ],
    "debrief": ["""
<p><strong>Mrs. Bautista.</strong> Thank her for the good news and name the approval precisely: &ldquo;That form is PhilHealth&rsquo;s pre-authorization. It tells us how the operation can be paid for. The transplant team still has to finish your medical review, your brother has his own separate evaluation, and the ethics committee has its review. I&rsquo;ll call you on Friday with your next step.&rdquo; Record the pre-authorization date in the register; its 180-day validity clock has started (Module 10).</p>
<p><strong>Mr. Castillo.</strong> Thank him for asking. Tell him that yes, he may pause or stop at any time, and that this conversation stays private. Offer a confidential meeting with his designated donor advocate and the donor team, today if he wishes. Do not ask him to explain himself to you, and do not tell his sister anything except what he later agrees to. Record the fact of the request, factually and briefly, in his restricted record.</p>
<p><strong>The unit manager.</strong> Decline the shared folder kindly and explain: &ldquo;Their records have to stay separate under our donor safeguards and privacy rules. I can give you one shared timeline that shows only the milestones both have agreed to share.&rdquo; Open two register rows: the donor&rsquo;s request for a confidential meeting (owner: donor advocate; due today) and the recipient&rsquo;s open gates (owner: transplant team; next review Friday).</p>
<p>None of these actions decided anything clinical. Each one made sure the right person would decide, and that each person knew exactly where they stood.</p>
"""],
    "skills": {"title": "Two pathway maps and an SBAR",
               "intro": "Using a fictional recipient and donor, build both pathway maps and a barrier register while your preceptor observes.",
               "items": [
                   ("Draws separate recipient and donor pathways, each with medical, legal, ethical, and insurance gates.", False),
                   ("Explains which information may appear in the shared view and which stays in each person&rsquo;s record.", True),
                   ("Writes three barrier register rows with owner, due date, escalation contact, and closure evidence.", True),
                   ("Distinguishes clinical coordination, procurement coordination, donor advocacy, and Z Benefits roles.", False),
                   ("Explains to a simulated recipient which approval a signed payer form represents, and which remain open.", True),
                   ("Writes and delivers one SBAR that names a decision maker, one decision, and a time.", False),
                   ("Responds to a simulated donor&rsquo;s private request to stop without disclosing it.", True),
               ],
               "placement": "Shadow a coordinator for one clinic day. List every handoff you see and mark which ones were closed with evidence from the receiving service."},
    "terms": [("Recipient", "The person with kidney failure who may receive the kidney."),
              ("Living donor", "A healthy person who may give a kidney; has their own team, record, and rights."),
              ("Gate", "A point where a decision must be made before the journey continues."),
              ("Barrier register", "A table of open problems with owner, due date, escalation contact, status, and closure evidence."),
              ("SBAR", "Situation, background, assessment, request."),
              ("Procurement coordinator", "A role that manages deceased donors and organ retrieval."),
              ("Z Benefits Coordinator", "The facility staff member who navigates PhilHealth Z Benefits packages.")],
    "readings": [("kidney-transplant.html", "The patient guide to kidney transplantation, to see the journey from the patient&rsquo;s side.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["01"])
