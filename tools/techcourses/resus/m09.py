# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 09: Circuit Emergencies That Become Resuscitations. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse pressing gauze on a forearm fistula after a needle dislodgement, blood on the blanket, a second nurse checking the pulse.",
    "objectives": [
        "Recognize venous needle dislodgement and access hemorrhage early, control bleeding, and treat hemorrhagic shock with the team.",
        "Recognize suspected hemolysis, never return the blood, treat the potassium risk, and check for a cluster.",
        "Treat a severe dialyzer reaction or anaphylaxis with intramuscular epinephrine first, and distinguish it from the intravenous epinephrine of cardiac arrest.",
        "Check glucose early in any collapse, and give an opioid antagonist for respiratory arrest from suspected opioid toxicity without interrupting cardiopulmonary resuscitation (CPR).",
        "Move from each circuit emergency to the cardiac arrest algorithm the moment the pulse is lost.",
    ],
    "big": """
{{plain:Most cardiac arrests in a dialysis unit do not come out of nowhere. They are the last step of a problem that started a few minutes earlier: a needle sliding out under a blanket, blood turning the color of wine, a rash in the first minutes of treatment, a patient who becomes confused. Catch the problem in its first minutes and you may never need to compress.}}
<p>The picture has a limit. Some of these emergencies go from first sign to arrest very fast, and some have no obvious first sign at all: a dislodged venous needle may not set off an alarm. So recognition here has two parts. Look actively, because machines miss things. And keep the arrest algorithm one step away, ready the instant the pulse goes.</p>
<p>Each of these emergencies has its own signed-off Quick Card. This module explains the reasoning behind the cards, and the point where each one becomes a resuscitation.</p>
{{cards:Key terms for this module|Venous needle dislodgement::The return needle coming out of the access while the pump keeps running, so blood flows onto the bed instead of back into the patient.|Hemorrhagic shock::Low blood pressure and poor perfusion from blood loss.|Hemolysis::Destruction of red blood cells in the circuit, releasing potassium and hemoglobin.|Anaphylaxis::A severe, rapid allergic reaction affecting breathing, circulation, or both.|Opioid antagonist::A drug such as naloxone that reverses opioid effects.|Cluster::Two or more patients affected by the same problem at the same time.}}
""",
    "case": {"title": "Needle out", "html": """
<p>At 4:15 p.m., in a busy unit in Bacolod City, Mrs. Gloria Santiago, 74, is asleep under a thick blanket in her third hour of dialysis through a left forearm fistula. Two stations away, a patient is vomiting, and both nearby nurses are there. The floor near Station 12 is wet from a mopping that was not finished.</p>
<p>A support aide passing Station 12 notices blood dripping from under the blanket onto the floor. The machine shows no alarm. Mrs. Santiago is pale and does not wake easily.</p>
""", "questions": ["What does the aide do in the first ten seconds?",
                  "Why did the machine not alarm, and what does that teach?",
                  "When does this become a resuscitation, and what changes then?"]},
    "sections": [
        ("bleed", "Needle out, access bleeding", "Needle dislodgement and hemorrhage", """
<p>When the venous needle comes out with the blood pump running, the machine keeps pulling blood from the arterial needle and delivering it onto the bed. The venous pressure alarm is supposed to catch this, but the pressure measured is mostly the resistance of the needle and line itself, so it may fall only a little when the needle is out: the alarm can stay silent.[[frinak2023]] A sleeping patient under a blanket can lose a large volume within minutes.</p>
{{fig:rl09_dislodgement}}
<div class="table-wrap"><table>
<thead><tr><th>Step (Card 4)</th><th>Who</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Lift the blanket; look at both needle sites and line connections</td><td>Anyone</td><td>The machine may not alarm</td></tr>
<tr><td>Stop the blood pump; clamp the line on both sides of the break</td><td>Nurse (any trained staff per policy)</td><td>Stops the loss</td></tr>
<tr><td>Firm pressure on the site with gloved hands and gauze</td><td>Nurse or aide</td><td>Controls bleeding from the access</td></tr>
<tr><td>Lay flat; check consciousness, pulse, pressure; oxygen per protocol</td><td>Second nurse</td><td>Hemorrhagic shock may follow</td></tr>
<tr><td>Call for help and the cart; call the physician-on-duty and the attending</td><td>Charge nurse</td><td>Shock or arrest may need the team</td></tr>
</tbody></table></div>
<p>Never reinsert a dislodged needle, and never return blood through a line end that has been open. If the patient loses the pulse, this is now cardiac arrest with hypovolemia from hemorrhage as the reversible cause: compressions, the arrest algorithm, saline through a working access or a new IV, and early transfer for blood. The wet floor is a hazard for staff during compressions and for the defibrillator; dry it or lay towels.</p>
{{key:A quiet machine proves nothing. Keep the access in view, lift the blanket, stop and clamp, press, and be ready for arrest from blood loss.}}
"""),
        ("hemolysis", "Hemolysis", "Hemolysis: blood that must never go back", """
<p>Hemolysis in the circuit happens when red cells are damaged by overheated or wrongly mixed dialysis fluid, chemical contamination of the water (such as chlorine or chloramine), or kinked or faulty blood tubing. The patient may report chest, back or abdominal pain, nausea, and breathlessness; the blood in the venous line looks translucent, cherry-red or &ldquo;port-wine.&rdquo; Broken red cells release potassium, so the danger is both the hemolysis and the potassium (Card 6).[[greenberg2021]]</p>
{{fig:rl09_hemolysis}}
<div class="table-wrap"><table>
<thead><tr><th>Action</th><th>Reason</th></tr></thead>
<tbody>
<tr><td>Stop the pump, clamp the lines, end the treatment</td><td>Stops further damage</td></tr>
<tr><td>Do not return the blood, ever</td><td>It carries potassium from broken cells</td></tr>
<tr><td>Monitor, urgent potassium and hemoglobin; treat potassium per Card 10</td><td>Arrest from hyperkalemia is the main risk</td></tr>
<tr><td>Check every patient on the same water and concentrate</td><td>Hemolysis is often a cluster</td></tr>
<tr><td>Keep lines, dialyzer, lot numbers, water and fluid samples</td><td>The cause must be found before restarting</td></tr>
</tbody></table></div>
<p>If one patient in a unit has hemolysis, assume others may too until the water and fluid are cleared. In a cluster, the charge nurse may face two deteriorating patients at once: the watcher role and the Medical Director&rsquo;s involvement become essential. If a patient arrests, potassium is the reversible cause to treat during CPR (Module 8), and the circuit blood is not returned.</p>
{{key:Port-wine blood is never returned. Treat the potassium, check every patient on the same supply, and keep the evidence.}}
"""),
        ("reaction", "Dialyzer reaction and anaphylaxis", "Severe reactions: epinephrine first, and the right epinephrine", """
<p>A severe dialyzer reaction or anaphylaxis usually begins within the first minutes of treatment, or soon after a drug such as intravenous iron, an antibiotic or heparin: itching, hives, flushing, throat tightness, wheeze, swelling of the lips or face, low blood pressure, collapse (Card 7). The treatment that saves lives is intramuscular epinephrine into the outer thigh, given early as the protocol directs. Antihistamines and steroids do not replace it. The blood pump is stopped, the lines clamped, and the blood not returned, because the circuit carries the trigger.</p>
{{fig:rl09_anaphylaxis}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Anaphylaxis with a pulse</th><th>Cardiac arrest (any cause, including anaphylaxis)</th></tr></thead>
<tbody>
<tr><td>Route</td><td>Intramuscular, outer thigh</td><td>Intravenous or intraosseous</td></tr>
<tr><td>Usual preparation</td><td>1 mg/mL (1:1,000) ampule or autoinjector</td><td>0.1 mg/mL (1 mg in 10 mL), or the 1 mg/mL ampule diluted to 10 mL per protocol</td></tr>
<tr><td>Adult dose</td><td>As the unit&rsquo;s anaphylaxis protocol directs, repeated at its interval</td><td>1 mg every 3 to 5 minutes</td></tr>
<tr><td>Main danger</td><td>Giving the IM concentration intravenously as a bolus</td><td>Delaying CPR for drugs</td></tr>
</tbody></table></div>
<p>The same drug in two concentrations for two routes is a classic tenfold error. Say the concentration and the route aloud and have the second nurse repeat them. If the patient arrests, the 2025 AHA special-circumstances chapter says it is reasonable to give isotonic intravenous fluids in cardiac arrest from anaphylaxis (COR 2a, LOE C-EO), and that the effectiveness of the standard intramuscular anaphylaxis dose of epinephrine in arrest is uncertain (COR 2b, LOE C-EO).[[aha2025_special]] In arrest, follow the standard arrest algorithm with intravenous epinephrine and give fluids.</p>
{{key:Anaphylaxis with a pulse: intramuscular epinephrine first, blood not returned. Arrest: intravenous epinephrine 1 mg every 3 to 5 minutes and fluids. Say the concentration aloud every time.}}
"""),
        ("other", "Sugar and opioids", "Low glucose and opioid toxicity: the mimics", """
<p>Two treatable causes often hide inside a &ldquo;collapse on dialysis&rdquo;: low blood glucose and opioid toxicity. Both can look like a stroke, a seizure, an arrhythmia or simply a deep sleep.</p>
{{fig:rl09_other}}
<h3>Low glucose</h3>
<p>Dialysis patients with diabetes are at risk of hypoglycemia during and after a session, especially with poor intake, insulin, or glucose-free dialysis fluid. Check capillary glucose early in any confusion, drowsiness, sweating or seizure, and treat per protocol (Card 11). If the patient has no pulse, CPR comes first and glucose is checked during the arrest as a reversible cause.</p>
<h3>Opioid toxicity</h3>
<p>Some opioids and their active metabolites accumulate when the kidneys do not clear them, so a usual dose can cause slow, shallow breathing and pinpoint pupils in a dialysis patient. The 2025 AHA special-circumstances chapter states that an opioid antagonist such as naloxone should be given to people with respiratory arrest from suspected opioid overdose, and that giving it during cardiac arrest from presumed overdose may be reasonable as long as it does not interrupt high-quality CPR.[[aha2025_special]] Ventilation comes first in respiratory arrest; compressions come first if there is no pulse.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Pulse present</th><th>No pulse</th></tr></thead>
<tbody>
<tr><td>Low glucose suspected</td><td>Check glucose; treat per protocol</td><td>CPR; check glucose as a reversible cause</td></tr>
<tr><td>Opioid toxicity suspected, not breathing</td><td>Ventilate with bag-mask; naloxone per protocol</td><td>CPR; naloxone may be considered without interrupting CPR</td></tr>
</tbody></table></div>
{{key:Check glucose early in every collapse. For suspected opioid toxicity, ventilate first and give an antagonist; if there is no pulse, CPR comes first.}}
{{call:Any bleeding access with paleness or low pressure, port-wine blood, signs of anaphylaxis, or a collapse with low glucose or slow breathing: use the matching Quick Card now, call the physician-on-duty and the attending nephrologist, and follow your unit protocol. If the pulse is lost, go to Card 1.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first ten seconds.</strong> The aide lifts the blanket, sees the venous needle out, and shouts for help. If trained and permitted by unit policy, the aide stops the blood pump and clamps; otherwise the aide presses firmly on the site with gloved hands and gauze while the nurse comes. The nurse stops the pump and clamps both sides of the break.</p>
<p><strong>Why no alarm.</strong> The venous pressure measured by the machine is mostly the resistance of the needle and tubing, so it may not fall enough to alarm when the needle comes out. The lesson: keep the access uncovered or check under the blanket, and never trust a quiet machine.</p>
<p><strong>When it becomes a resuscitation.</strong> Mrs. Santiago is pale and hard to wake: check her pulse and pressure now. If she has a pulse with low pressure, lay her flat, give oxygen and saline per protocol through a new IV (not through the open line), and arrange transfer for blood. If she loses her pulse, it is cardiac arrest with hemorrhage as the cause: compressions, the arrest algorithm, fluids, and early transfer. The wet floor is dried or covered before anyone kneels or shocks. The watcher stays with the vomiting patient and the rest of the unit.</p>
"""],
    "skills": {"title": "Circuit emergencies on the edge of arrest",
               "intro": "In three short simulator scenarios (needle out, hemolysis, anaphylaxis), take the first actions and state the point at which the arrest algorithm begins.",
               "items": [
                   ("Lifts the blanket and inspects both needle sites and connections without waiting for an alarm.", True),
                   ("Stops the pump, clamps both sides of a break, and applies firm pressure.", True),
                   ("Never returns blood after hemolysis, a severe reaction, or through an open line end.", True),
                   ("Checks every patient on the same water supply when hemolysis is suspected.", False),
                   ("Gives or prompts intramuscular epinephrine first in anaphylaxis, stating the concentration and route aloud.", True),
                   ("Distinguishes IM anaphylaxis epinephrine from IV arrest epinephrine.", True),
                   ("Checks capillary glucose early in any collapse.", False),
                   ("Moves to the arrest algorithm the moment the pulse is lost.", True),
               ],
               "placement": "Audit one shift for how many accesses are visible versus covered by blankets, and present the result at the staff meeting."},
    "terms": [("Venous needle dislodgement", "The return needle coming out while the pump runs."),
              ("Hemorrhagic shock", "Shock from blood loss."),
              ("Hemolysis", "Red cells destroyed in the circuit, releasing potassium."),
              ("Anaphylaxis", "A severe allergic reaction affecting breathing or circulation."),
              ("Naloxone", "An opioid antagonist that reverses opioid effects."),
              ("Tenfold error", "A dose ten times too high or too low, often from a concentration mix-up.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["09"])
