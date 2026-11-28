# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 04: Ready Patients: Card, Diet, Medicines, Contacts. DRAFT.
The Academy three-day emergency kidney diet sheet (downloads/three-day-emergency-kidney-diet.*) was approved by Dr. Rivero on
November 28, 2026; this module teaches it and links it. The team writes in each patient's fluid allowance."""

MODULE = {
    "image_alt": "An older man on hemodialysis and his adult daughter packing a waterproof go-bag on a wooden table at home.",
    "objectives": [
        "Help a patient fill in an emergency card that another unit could use to dialyze them safely.",
        "Teach a patient the Academy three-day emergency kidney diet sheet and fill in its personal fields, including the team&rsquo;s fluid allowance.",
        "Help a patient plan a medicine supply, two phone numbers and a family contact before typhoon season.",
        "Teach the rule on the machine: stay calm, stay connected, protect the access arm, wait for staff; patients are not taught to self-disconnect.",
        "Adapt the preparation for patients on peritoneal dialysis (PD) and for children.",
    ],
    "big": """
{{plain:A patient&rsquo;s go-bag is like a passport for treatment. If the patient arrives at a strange unit after a flood, the card in that bag tells the nurse who they are, how they dialyze and what they take. Without it, the nurse has to guess.}}
<p>The passport has a limit: it does not keep potassium down or fluid off during the days before the patient reaches another unit. That is the diet&rsquo;s job, and it is the part patients find hardest, because relief food is often salty, potassium-rich, or both. And the go-bag does nothing for a patient who is on the machine when the ground shakes. For that moment, the patient needs one simple rule, practiced in advance.</p>
<p>After Hurricane Katrina, patients who did not know their unit&rsquo;s emergency plan were among the more likely to miss three or more sessions.[[dp_anderson2009]] Preparing patients is not a leaflet handed out once; it is a short conversation, repeated before every typhoon season. The social worker&rsquo;s role in this is taught in <a href="social-worker-17-transfers-disasters-and-continuity.html">Social Worker, Module 17</a>.</p>
{{cards:Key terms for this module|Emergency card::A wallet card with the facts another unit needs to dialyze the patient safely.|Go-bag::A packed, waterproof bag with the card, medicines, diet sheet, water, a power bank and a flashlight.|Three-day emergency kidney diet::A short-term eating plan that limits potassium, salt and fluid more tightly than usual, to buy time until the next session.|Medicine list::The patient&rsquo;s current medicines, doses and times, kept with the card.|Self-disconnection::A patient separating themselves from the machine; not taught in this course.|Backup unit::The receiving unit the patient goes to if their own unit cannot open.}}
""",
    "case": {"title": "Mang Ernesto's go-bag", "html": """
<p>Mr. Ernesto Villanueva, 67, has been on hemodialysis for three years through a left forearm fistula. He lives with his daughter, Liza, in a flood-prone part of Valenzuela. Before typhoon season the unit&rsquo;s social worker asks them to bring his go-bag to the next session.</p>
<p>The bag holds: a photocopy of a prescription from two years ago, a plastic bag of mixed pills, a packet of instant noodles &ldquo;for emergencies,&rdquo; two bananas, a phone with a cracked screen and no power bank, and a note with the unit&rsquo;s landline. Liza asks, &ldquo;If the power goes out while he is on the machine, should he pull the needles out himself? My neighbor said patients are taught to do that abroad.&rdquo;</p>
""", "questions": ["What is missing from Mang Ernesto&rsquo;s card and bag?",
                  "Which items in the bag work against him in a three-day emergency?",
                  "How do you answer Liza&rsquo;s question about self-disconnection?"]},
    "sections": [
        ("card", "The emergency card", "A card another unit can use", """
<p>The card carries what a stranger needs to dialyze the patient safely, and nothing more. Keep it in a waterproof sleeve in the go-bag and a photo of it on the patient&rsquo;s and a family member&rsquo;s phone.</p>
{{fig:dp04_emergency_card}}
<div class="table-wrap"><table>
<thead><tr><th>Front</th><th>Back</th></tr></thead>
<tbody>
<tr><td>Name; kidney diagnosis</td><td>Current medicines and doses</td></tr>
<tr><td>Dialysis days and session length</td><td>Allergies</td></tr>
<tr><td>Access type and side (fistula, graft, catheter)</td><td>PhilHealth number</td></tr>
<tr><td>Target (dry) weight</td><td>My unit, with two phone numbers</td></tr>
<tr><td>Last potassium, with its date</td><td>Backup unit; family contact</td></tr>
</tbody></table></div>
<p>The site&rsquo;s <a href="../guides/climate-extremes-kidney-care.html">climate extremes guide</a> has a printable Kidney Emergency Card. The nurse updates the card when the prescription, access or dry weight changes, and checks it at the start of each typhoon season. The card is the patient&rsquo;s own document; the unit keeps no copy outside the patient&rsquo;s record.</p>
"""),
        ("diet", "The emergency diet", "The three-day emergency kidney diet", """
<p>When sessions are missed, food decides how fast potassium and fluid build up. The Academy&rsquo;s <strong>Three-Day Emergency Kidney Diet</strong> sheet, approved by Dr. Rivero on November 28, 2026, gives adults on hemodialysis the amounts: a no-cook, no-refrigerator menu in measured household portions, swaps for when it is safe to cook, a &ldquo;hold for now&rdquo; list of local foods, food and water safety when the power is out, advice for diabetes, the warning signs that mean go to a hospital now, and a kit list. The patient starts it as soon as the emergency is announced, before a session is missed.</p>
<p class="dp-dl"><a href="../downloads/three-day-emergency-kidney-diet.pdf"><strong>Download the Three-Day Emergency Kidney Diet</strong> (PDF, 4 pages, A4)</a> &middot; <a href="../downloads/three-day-emergency-kidney-diet.html">open it in the browser</a></p>
<p>Before typhoon season, the team fills in the sheet&rsquo;s &ldquo;My information&rdquo; page with the patient: the daily fluid allowance (the team sets it; if no number is written, the sheet shows the national plan&rsquo;s 2 cups, about 480 mL, a day), the unit and backup unit numbers, the diabetes plan, and any low-salt brands the unit recommends. The patient&rsquo;s own dietitian may adjust the plan.</p>
{{fig:dp04_emergency_diet_principles}}
<ul>
<li><strong>Choose</strong> foods that are lower in potassium and salt and keep without a refrigerator: white rice, unsalted crackers, canned fruit with the syrup drained, eggs, and fresh chicken or fish only while it can be kept cold.</li>
<li><strong>Limit</strong> the foods that relief packs and stores are full of: dried and salted fish, instant noodles (and their seasoning packet), canned sardines and processed meat, and high-potassium foods such as bananas and coconut water.</li>
<li><strong>Measure fluid.</strong> Use one marked cup for all drinks. Salty food drives thirst, so less salt makes the fluid limit easier.</li>
<li><strong>Amounts come from the sheet; the fluid number comes from the team.</strong> The plan has less protein than the usual dialysis diet and lasts only until the next session; it is not a reason to skip dialysis.</li>
</ul>
<p>For patients with diabetes, the sheet drops the candy and added sugar except to treat a low blood sugar, and tells them not to change insulin or diabetes pills on their own. The sheet is for adults on hemodialysis only: patients on PD, children, pregnant patients and transplant recipients need their own plan from the team. For children, the pediatric nephrologist orders a weight-based plan.</p>
{{key:Limit potassium, salt and fluid until the next session, with the sheet&rsquo;s measured portions and the team&rsquo;s fluid number. No one should skip dialysis because they are &ldquo;on the emergency diet.&rdquo;}}
"""),
        ("supply", "Medicines and contacts", "Medicines, phones and family", """
<p><strong>Medicines.</strong> A written list (name, dose, time), kept with the card, and an extra supply agreed with the patient&rsquo;s doctor and pharmacist, rotated so it does not expire. Pharmacies may close after a disaster. The list lets a receiving unit or a hospital continue treatment without guessing.</p>
<p><strong>Two phone numbers and a family contact.</strong> One number is rarely enough: phones are lost, batteries die, and numbers change. The unit records two numbers and a family contact, and checks them before typhoon season (the call-down drill, Module 12).</p>
<p><strong>The go-bag.</strong> Card, medicine list and supply, the diet sheet, bottled water, a power bank, a flashlight, copies of recent records, and a clean dressing for the access.</p>
{{fig:dp04_go_bag}}
<p><strong>Patients on PD and home dialysis.</strong> They need a supply of solution bags and a clean place for exchanges, and a way to reach their PD unit when phone lines are down. A Japanese hospital reported on its communication with PD patients after the 2016 Kumamoto earthquake.[[dp_kawabata2017]] PD units keep a list of patients&rsquo; addresses and supply levels, protected under the Data Privacy Act.</p>
"""),
        ("machine", "On the machine", "What a patient does on the machine when disaster strikes", """
<p>This is the rule every patient learns: <strong>stay calm, stay connected, protect the access arm, and wait for staff. Staff take patients off.</strong></p>
{{fig:dp04_on_the_machine_when_disaster_strikes}}
<p>Some countries teach patients to disconnect themselves in an emergency. The Academy does not (Dr. Rivero&rsquo;s decision), for a clear reason. In 626 hemodialysis patients in 10 centers across six countries, only 20.0% had been trained in self-disconnection, and on a checklist only 40.3% identified the first stage of the procedure correctly and 38.3% the second.[[dp_ozen2026]] A patient who pulls a needle, opens a catheter or separates lines under stress risks bleeding, air entering a central vein, or a lost access. Staff are trained to do this with the blood rule (Module 6) and the right clamps.</p>
<p>During shaking, a patient in a recliner stays seated and covers the head and neck with the free arm or a pillow, keeping the access arm still.[[dp_fema2025]] In a fire or an evacuation, staff come to each patient and take them off in turn (Module 7).</p>
{{call:A patient on the machine who is bleeding from the access, feels faint, or tries to disconnect during an event is attended at once by the nearest staff member. Follow your unit protocol, and always ask the attending nephrologist for guidance.}}
<div class="alert alert-amber"><div class="alert-icon">🧒</div><div class="alert-body"><h4>Units that dialyze children</h4><p>A child&rsquo;s go-bag also holds what the caregiver needs: a car seat or stroller plan for evacuation, the child&rsquo;s weight on the card, pediatric supplies, and comfort items. The diet is weight-based and ordered by the pediatric nephrologist. A caregiver stays with the child during the session when the unit allows it, and knows the same rule: stay connected and wait for staff.</p></div></div>
"""),
    ],
    "debrief": ["""
<p><strong>What is missing.</strong> A current emergency card (access type and side, dry weight, last potassium, medicines, allergies, PhilHealth number, backup unit, family contact); a written medicine list with an agreed extra supply instead of mixed loose pills; two phone numbers; a power bank; the diet sheet; bottled water; a flashlight; a clean dressing.</p>
<p><strong>What works against him.</strong> Instant noodles (and their seasoning) are very salty, and bananas are high in potassium; both make the days before the next session more dangerous. Swap them for the &ldquo;choose&rdquo; foods, give him the three-day diet sheet, and fill in his fluid allowance with him.</p>
<p><strong>Liza&rsquo;s question.</strong> &ldquo;No. At this unit patients are not taught to disconnect themselves. If the power goes out, he stays calm and connected, keeps his fistula arm still, and waits; a nurse will come to him and take him off safely.&rdquo; Explain why: pulling needles under stress can cause bleeding and lose the fistula, and the nurses are trained to do it with the right clamps.</p>
"""],
    "skills": {"title": "Preparing a patient for typhoon season",
               "intro": "With a patient (and a family member where possible), complete the preparation conversation before typhoon season.",
               "items": [
                   ("Fills in or updates the emergency card with access type and side, dry weight, last potassium with date, medicines, allergies, units and contacts.", True),
                   ("Checks two phone numbers and a family contact, and updates the unit record.", True),
                   ("Teaches the three-day diet sheet and fills in its personal fields: the team&rsquo;s fluid allowance, the unit and backup numbers, and the diabetes plan.", False),
                   ("Reviews the go-bag and the medicine supply plan.", False),
                   ("Teaches the rule on the machine and confirms the patient can say it back: stay calm, stay connected, protect the access arm, wait for staff.", True),
                   ("Does not teach or encourage self-disconnection.", True),
               ],
               "placement": "Complete the conversation with five patients, including one on PD or one child where the unit treats them."},
    "terms": [("Emergency card", "A wallet card with the facts another unit needs to dialyze the patient safely."),
              ("Go-bag", "A packed, waterproof bag with the card, medicines, diet sheet, water, power bank and flashlight."),
              ("Emergency kidney diet", "A short-term plan with less protein, potassium, salt and fluid, kept only until the next session."),
              ("Backup unit", "The receiving unit the patient goes to if their own unit cannot open."),
              ("Self-disconnection", "A patient separating themselves from the machine; not taught in this course.")],
    "readings": [("climate-extremes-kidney-care.html", "The printable Kidney Emergency Card and climate advice for patients."),
                 ("typhoon-disaster-preparedness-dialysis.html", "The patient guide to typhoon preparation.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["04"])
