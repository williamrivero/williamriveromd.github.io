# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 17: Transfers, Disasters, and Continuity of Care. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker on the phone at a dialysis unit desk during heavy rain, a printed transfer checklist in hand.",
    "objectives": [
        "Treat every transfer between units, hospitals, or home as a handoff that closes only when the receiving service confirms the person arrived and was treated.",
        "Arrange temporary dialysis away from home (travel, family emergencies, work) with the information the receiving unit needs.",
        "Prepare patients and families for typhoons, floods, and earthquakes with a personal dialysis emergency plan.",
        "Coordinate during a disaster: contact lists, alternative units, transport, and tracing patients who did not arrive.",
        "Protect privacy while sharing only what the receiving service needs for safe care.",
    ],
    "big": """
{{plain:Moving a person on dialysis from one unit to another is like passing a lit candle from hand to hand in the wind. The flame does not care how carefully the first person held it. What matters is whether the second hand was ready, and whether anyone checked that the flame was still burning on the other side.}}
{{fig:sw17_continuity}}
<p>The picture has a limit. A candle that goes out can be relit in a second. A person on hemodialysis who misses sessions while a transfer is &ldquo;being arranged&rdquo; builds up fluid and potassium every day, and after two or three missed sessions the danger is real (Module 2). That is why continuity is not paperwork. It is the difference between a person who is dialyzed on time in a new place and one who ends up in an emergency room.</p>
<p>Your job in this module is to make transfers and disasters into handoffs that close on evidence. Disasters show what happens when continuity fails. After Hurricane Katrina in 2005, 94 dialysis facilities on the United States Gulf Coast closed for at least a week and existing plans were inadequate.[[kopp2007]] In interviews with 386 patients from nine New Orleans units, 44% missed at least one session and almost 17% missed three or more; missing three or more was associated with hospitalization, and patients unaware of their unit&rsquo;s emergency plan were more likely to miss.[[anderson2009]] The Philippines faces typhoons and floods every year.</p>
{{cards:Key terms for this module|Transfer::A permanent move of a patient&rsquo;s dialysis care to another unit.|Transient dialysis::Temporary dialysis at another unit while traveling or during an emergency.|Handoff packet::The information the receiving unit needs: dialysis order, access, serologies, medicines, allergies, contacts, benefit status.|Arrival confirmation::The receiving unit&rsquo;s confirmation that the patient arrived and was treated.|Personal emergency plan::A patient&rsquo;s written plan for disasters: where to go, whom to call, what to bring, what to eat.|Patient tracing::Contacting every patient after a disaster to find who missed treatment and why.}}
""",
    "case": {"title": "Typhoon signal 3 on a Monday", "html": """
<p>Sunday, 6:00 p.m. The national weather agency raises a Signal No. 3 tropical cyclone wind signal over your province. Your unit in a coastal town expects flooding on its access road by Monday morning. The unit head decides to run an extra early shift Monday before the roads close, then close until the water recedes.</p>
<p>You are asked to help reach 60 patients. Among them: Mrs. Lourdes Cabrera, 70, who lives alone on an island barangay reachable only by boat; Mr. Ariel Domingo, 36, whose phone has been off for two days; and Mr. Victor Lim, 55, who is visiting his daughter in Cebu and asked last week to dialyze there, but whose papers were never sent.</p>
<p>By Wednesday the unit is still closed. The nearest open unit is in the provincial capital, 40 kilometers away.</p>
""", "questions": ["How do you organize contacting 60 patients before Monday?",
                  "What do you do for Mrs. Cabrera, Mr. Domingo, and Mr. Lim?",
                  "How do you know, by Thursday, that every patient has been dialyzed somewhere?"]},
    "sections": [
        ("handoff", "Transfer as a handoff", "Closed only on arrival", """
<p>A transfer begins with a request and ends with a confirmation. In between, the person is at risk of falling through the gap: the receiving unit has no slot, the papers are incomplete, the serology results are too old, the PhilHealth session count is unclear, or the person cannot afford the travel.</p>
{{flow:A transfer that closes|Request::The patient asks, or the team recommends; agree the reason and date.|Find a slot::Call the receiving unit; get a named contact and a confirmed start date.|Send the packet::Dialysis order, access type, recent serologies, medicines, allergies, contacts, benefit status, social notes needed for care.|Plan the journey::Transport, cost, companion, timing relative to the last session.|Confirm arrival::Call the receiving unit after the first session; record who confirmed.}}
<p>Send only what the receiving unit needs for safe care and benefit processing. A full psychosocial assessment rarely needs to travel; a short summary of what affects care (language, caregiver, safety concerns the person agreed to share) usually does. Under the Data Privacy Act, health information is sensitive personal information; share it for a clear purpose with a lawful basis (Module 18).[[ra10173]]</p>
{{key:A transfer is not done when the papers leave. It is done when the receiving unit confirms the person was dialyzed.}}
"""),
        ("travel", "Temporary dialysis away from home", "Travel, family emergencies, work", """
<p>People on dialysis travel for funerals, weddings, graduations, work, and family emergencies. With planning, most can dialyze at another unit for a few sessions. Without planning, many skip sessions instead.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Detail</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Ask early</td><td>Ask every patient at review whether they plan to travel</td><td>Social worker, nurse</td></tr>
<tr><td>Medical clearance</td><td>Whether travel is safe; schedule around it</td><td>Attending nephrologist</td></tr>
<tr><td>Find a unit</td><td>Units near the destination with a slot; their requirements</td><td>Social worker, patient</td></tr>
<tr><td>Send the packet</td><td>Order, serologies within the receiving unit&rsquo;s required period, medicines, contacts</td><td>Nurse, social worker</td></tr>
<tr><td>Costs and benefits</td><td>How PhilHealth sessions and charges apply at the receiving unit</td><td>Claims officer, receiving unit</td></tr>
<tr><td>Confirm</td><td>The first session at the receiving unit happened</td><td>Social worker</td></tr>
</tbody></table></div>
<p>Serology results (for hepatitis B, hepatitis C, and HIV) are the most common reason a receiving unit refuses a patient on arrival. Check how recent the receiving unit requires them to be, before the person travels.</p>
{{key:Ask about travel at every review. Plan the receiving unit, the packet, the cost, and the confirmation before the trip.}}
"""),
        ("prepare", "Preparing for typhoons and floods", "The personal emergency plan", """
<p>The best time to plan for a disaster is a calm week. Every patient and family should have a written personal emergency plan, reviewed at the start of the rainy season.</p>
{{fig:sw17b_plan}}
<div class="table-wrap"><table>
<thead><tr><th>The plan covers</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Where to go if our unit closes</td><td>Two alternative units, with addresses and numbers</td></tr>
<tr><td>How to reach us and how we reach you</td><td>Two phone numbers, a relative&rsquo;s number, a neighbor&rsquo;s number</td></tr>
<tr><td>What to bring</td><td>A copy of the dialysis order, serologies, medicine list, PhilHealth details, ID</td></tr>
<tr><td>What to eat and drink if dialysis is delayed</td><td>The unit&rsquo;s emergency diet advice from the dietitian (stricter fluid, salt, and potassium limits)</td></tr>
<tr><td>Medicines</td><td>A few days&rsquo; supply kept dry</td></tr>
<tr><td>Who needs extra help</td><td>Those living alone, on islands, in flood-prone areas, or without phones</td></tr>
</tbody></table></div>
<p>Keep a unit-level list of the patients who will need extra help: those who live alone, far away, on islands, in flood zones, or who depend on others for transport. Those are the people you call first when a signal is raised. In the Katrina interviews, patients who did not know their unit&rsquo;s plan were more likely to miss three or more sessions,[[anderson2009]] which suggests that the plan only helps if patients know it.</p>
{{key:Every patient has a written emergency plan before the rainy season, and the unit knows who needs help first.}}
"""),
        ("during", "During and after a disaster", "Find every patient", """
<p>When a disaster hits, the work is to get every patient dialyzed somewhere and to find those who were not. Divide the patient list among staff, call in order of risk, and record each call.</p>
{{flow:Coordinating during a disaster|Before landfall::Call the high-risk list first; move sessions earlier if the unit decides; confirm each person&rsquo;s plan.|Unit closed::Arrange sessions at open units; share a list with them; organize transport where possible.|Track::One sheet: every patient, where they will dialyze, when, confirmed or not.|Trace::Anyone not confirmed in 48 hours: call relatives and neighbors; ask the barangay; alert the nephrologist.|After::Review who missed sessions and why; update the plans.}}
<p>Disasters also bring social emergencies: homes lost, income gone, documents destroyed. After the immediate danger, your usual work (assistance, documents, caregiver plans) resumes at higher intensity. The site&rsquo;s patient guide on typhoon preparedness is a good handout for families.</p>
{{call:A patient on hemodialysis who cannot be reached or confirmed dialyzed within two days of a disaster: alert the attending nephrologist and start tracing through relatives, neighbors, and the barangay.}}
{{scene:The boat|<p>Before a typhoon, social worker Mr. Noel Pascua calls the barangay captain of an island community where two dialysis patients live.</p>
<p>The captain arranges a boat to bring both patients to the mainland the day before landfall. They stay with relatives near an open unit and miss no sessions.</p>
<p class="tc-scene-take">The plan worked because the list of who needed help first existed before the signal was raised.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Contacting 60 patients.</strong> Divide the list among available staff. Start with the high-risk list (living alone, islands, flood zones, no phone, dependent on others). For each: the time of the extra Monday shift, what to eat and drink if dialysis is delayed, where to go if the unit stays closed, and a confirmed callback number. Record every call on one tracking sheet.</p>
<p><strong>The three patients.</strong> Mrs. Cabrera: call the barangay captain today about bringing her to the mainland before the roads and seas close, and a place to stay near an open unit. Mr. Domingo: call his listed relatives and neighbors; ask the barangay; tell the nephrologist that he is unreachable. Mr. Lim: send his packet to the Cebu unit today, confirm a slot, check his serologies are recent enough, and confirm after his first session there.</p>
<p><strong>Knowing by Thursday.</strong> The tracking sheet shows every patient, where and when they will dialyze, and whether the receiving unit confirmed it. Anyone unconfirmed after 48 hours is traced and reported to the nephrologist. Afterward, review who missed sessions and why, and update every plan.</p>
"""],
    "skills": {"title": "A transfer packet and an emergency plan",
               "intro": "For a fictional patient, prepare a transfer and a personal emergency plan, and run a disaster call list, while your supervisor observes.",
               "items": [
                   ("Arranges a transfer with a named receiving contact and confirmed start date.", False),
                   ("Sends a packet limited to what the receiving unit needs for safe care and benefits.", False),
                   ("Checks serology dates against the receiving unit&rsquo;s requirement before travel.", False),
                   ("Confirms the first session at the receiving unit before closing the transfer.", True),
                   ("Writes a personal emergency plan with alternative units, contacts, documents, and diet advice.", False),
                   ("Prioritizes a disaster call list by risk and keeps one tracking sheet.", False),
                   ("Alerts the nephrologist and starts tracing for any patient unconfirmed within two days.", True),
               ],
               "placement": "Review your unit&rsquo;s disaster plan with the head nurse. Build or update the list of patients who need help first, and check their contact numbers."},
    "terms": [("Transfer", "A permanent move of dialysis care to another unit."),
              ("Transient dialysis", "Temporary dialysis at another unit."),
              ("Handoff packet", "The information the receiving unit needs for safe care."),
              ("Arrival confirmation", "The receiving unit&rsquo;s confirmation that the patient was treated."),
              ("Personal emergency plan", "A patient&rsquo;s written disaster plan."),
              ("Patient tracing", "Finding every patient after a disaster.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient guide to typhoon and disaster preparedness on dialysis."),
                 ("travel-dialysis-ckd.html", "The patient guide to traveling on dialysis.")],
    "calcs": ["calc-social-worker-toolkit.html#tool-4"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["17"])
