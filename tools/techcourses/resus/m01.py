# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 01: Ready Before the Collapse. Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A charge nurse and a technician checking a defibrillator and crash cart at dawn in an empty dialysis unit.",
    "objectives": [
        "Explain why cardiac arrest clusters in dialysis units, including the Monday session, low-potassium dialysis fluid, and large fluid removal.",
        "Describe the single chain of survival and name the person who owns each link on your shift.",
        "Complete a daily defibrillator, oxygen, suction and crash-cart check, and act on a failed item before the first patient connects.",
        "Compare what a freestanding and a hospital-based dialysis unit can do in the first ten minutes, and plan the ambulance call and transfer.",
        "Assign resuscitation roles at the start of the shift from the real roster, including a watcher for the other patients.",
    ],
    "big": """
{{plain:Think of a fire drill in a building that already has smoke detectors. The detectors are your monitors and your trained staff. The drill is not about the fire; it is about whether the extinguisher is where everyone thinks it is, whether the door opens, and whether each person knows their job. Most deaths in a fire come from the minutes lost before anyone acts.}}
<p>The picture has a limit. A fire does not stay connected to a machine that holds a few hundred milliliters of the patient&rsquo;s blood. In a dialysis unit, the &ldquo;building&rdquo; is also part of the emergency: the circuit, the chair, the water on the floor, and twelve other patients still dialyzing. Readiness here means the equipment works, the roles are named, and the team has already decided what happens to the machine before anyone needs to.</p>
<p>Your work in this module is simple to state. Know why arrests happen in your unit. Check the equipment every morning as if today were the day. Name the roles before the first patient connects. And know exactly how help arrives and how long it takes.</p>
{{cards:Key terms for this module|Cardiac arrest::The heart stops pumping effectively; the person is unresponsive, not breathing normally (gasping counts as not normal), and has no pulse.|Chain of survival::The linked actions that together give the best chance of survival, from recognition to recovery.|Automated external defibrillator (AED)::A device that analyzes the rhythm and tells the rescuer whether to shock.|Manual defibrillator::A defibrillator with a screen on which a trained clinician reads the rhythm and chooses the energy.|Crash cart::The mobile cart holding the defibrillator, airway equipment, suction and resuscitation drugs.|Watcher::The staff member who keeps every other connected patient safe while the team works on the arrest.}}
""",
    "case": {"title": "The 5:40 a.m. check", "html": """
<p>It is Monday, 5:40 a.m., at a freestanding 18-station hemodialysis unit in Caloocan. The first shift connects at 6:00. Charge nurse Ms. Rowena Dizon opens the crash cart with technician Mr. Paolo Ramos. The defibrillator&rsquo;s self-test screen shows a battery warning. The adult pads in the cart expired last month. The oxygen cylinder gauge reads about a quarter full. The suction unit works.</p>
<p>The physician-on-duty, Dr. Kim Salonga, is on her way and will arrive at 6:20. Today&rsquo;s list includes Mr. Ernesto Bautista, 67, who missed Friday&rsquo;s session after a hospital stay, and two patients dialyzing on a 1.0 mEq/L potassium bath. The nearest hospital emergency room is 15 minutes away in normal traffic; the unit relies on the city ambulance or a private ambulance on call.</p>
""", "questions": ["Which failed item matters most, and can the first shift start?",
                  "What does today&rsquo;s patient list add to your readiness plan?",
                  "Whom do you assign to each code role before 6:00, and who watches the other patients?"]},
    "sections": [
        ("why", "Why dialysis units", "Why arrests happen on the dialysis floor", """
<p>Cardiac arrest is the most feared complication of hemodialysis, and its pattern is predictable. In a review of 400 arrests across more than 5.7 million hemodialysis sessions in the United States, the rate was 7 per 100,000 sessions. Arrests were more frequent on Mondays. Patients who arrested were nearly twice as likely to have been dialyzed against a potassium bath of 0 or 1.0 mEq/L on that day (17.1% compared with 8.8%), and 37% had been in hospital in the previous 30 days. Sixty percent died within 48 hours.[[karnik2001]] A later case-control study of 502 arrests in clinics caring for 43,200 patients found arrest associated with dialysis fluid potassium below 2 mEq/L, larger fluid removal volumes, and low-calcium dialysis fluid, whatever the pre-dialysis potassium.[[pun2011]]</p>
<p>The physiology explains the pattern. Over the long weekend gap, potassium, fluid and acid build up. The first session then removes them fastest. A heart thickened by years of high blood pressure and kidney disease is electrically unstable when potassium swings from high to low within hours and when fluid removal lowers the pressure that feeds the coronary arteries. The long two-day gap itself is associated with more deaths and cardiac events on the day after it.[[foley2011]] All of these studies are observational, so they identify risk, not proof of cause; but they tell you which patients deserve a second look on a Monday morning.</p>
{{fig:rl01_unit_types}}
<div class="table-wrap"><table>
<thead><tr><th>Risk signal</th><th>Why it matters</th><th>What readiness looks like</th></tr></thead>
<tbody>
<tr><td>Monday or the first session after a missed one</td><td>Highest potassium and fluid load of the week</td><td>Monitor attached early; potassium checked per protocol; seat near the station with the best view</td></tr>
<tr><td>Potassium bath of 0 to 1 mEq/L</td><td>Rapid fall in potassium during the session</td><td>Prescription reviewed by the physician; extra rhythm watch late in the session</td></tr>
<tr><td>Recent hospital discharge</td><td>Sicker patient; prescription may no longer fit</td><td>Fresh review of the dialysis order before connection</td></tr>
<tr><td>Large fluid removal goal</td><td>Low pressure and coronary underfilling</td><td>Blood pressure trend watched; fluid removal reduced per order if pressure falls</td></tr>
<tr><td>Drop in systolic pressure of 30 mm Hg or more</td><td>Seen before 16% of arrests in one series</td><td>Treat as a warning sign, not a routine low pressure (Card 3)</td></tr>
</tbody></table></div>
{{key:Monday, missed sessions, low-potassium baths, recent discharge and big fluid removal are the arrest-risk flags. Read the list at 5:40 a.m. with those flags in mind.}}
"""),
        ("chain", "Chain of survival", "One chain, drawn for the dialysis floor", """
<p>The 2025 AHA guidelines use a single chain of survival for adults and children, in and out of hospital.[[aha2025_systems]] In a dialysis unit, every link happens in one room within minutes, which is both the advantage and the danger: everyone is close, so everyone assumes someone else is doing the next step.</p>
{{fig:rl01_chain}}
<div class="table-wrap"><table>
<thead><tr><th>Link</th><th>On the dialysis floor</th><th>Owner on your shift</th></tr></thead>
<tbody>
<tr><td>Recognize and call</td><td>Unresponsive, not breathing normally, no pulse in 10 seconds: shout, call the code</td><td>The first person at the chair</td></tr>
<tr><td>Compressions now</td><td>Recliner flat, compressions within seconds</td><td>The nearest trained staff; swap every 2 minutes</td></tr>
<tr><td>Defibrillator at the chair</td><td>Pads on as soon as it arrives; rhythm decides</td><td>The defibrillator and drugs person</td></tr>
<tr><td>Circuit managed</td><td>Fluid removal stopped, blood decision made and announced</td><td>The circuit nurse</td></tr>
<tr><td>Advanced care and transfer</td><td>Drugs, airway, reversible causes, ambulance called early</td><td>The leader (usually the physician-on-duty)</td></tr>
<tr><td>Recovery and debrief</td><td>Handover, family, documentation, team debrief</td><td>The leader and the charge nurse</td></tr>
</tbody></table></div>
<p>The chain has one link the general guidelines do not draw: the other patients. When five staff gather around Station 7, the circuits at Stations 1 to 18 are still running. A named watcher stays outside the arrest and keeps every other patient safe. That person never joins compressions.</p>
{{key:Every link has one named owner before the shift starts, and the watcher is never pulled into the arrest.}}
"""),
        ("check", "Morning check", "The morning check: equipment that works today", """
<p>The defibrillator and the crash cart are only as good as their last check. In one cohort of 729 in-clinic arrests, simply having a defibrillator on site was not associated with better survival after adjustment for patient differences.[[hn_lehrich2007]] The device matters when it works, is brought to the chair at once, and is used by someone who is ready. In a later registry, staff applied a defibrillator before the ambulance arrived in only 52.3% of clinic arrests.[[pun2019]]</p>
{{fig:rl01_cart_check}}
{{flow:A five-minute morning check|Defibrillator::Self-test passed; battery charged; adult pads (and pediatric pads where children dialyze) in date and sealed; spare pads; paper or memory working.|Airway and oxygen::Bag-valve-mask with adult masks in sizes; oxygen cylinder with enough pressure for transfer; tubing and masks; oral and nasal airways.|Suction::Unit switched on and tested; tubing and a rigid tip present.|Drugs and fluids::Sealed tray with the unit&rsquo;s list; expiry dates; saline bags and flushes; glucose meter with strips.|Paper and phones::Code record sheet, a working clock, and the ambulance and receiving hospital numbers posted where the runner will look.}}
<p>A failed item is not a note in the log; it is a decision. In the case, the defibrillator battery warning and expired pads mean the unit has no reliable defibrillator. The first shift should not connect high-risk patients until a charged device and in-date pads are at hand, from a charging dock, a spare battery, or a sister unit, and the Medical Director or Dialysis Clinical Head should hear it before 6:00. The low oxygen cylinder must be swapped before it is needed for a transfer. The exact rule for what blocks a shift is your unit&rsquo;s policy; write it down before the morning you need it.</p>
{{key:A failed defibrillator, pads or oxygen check is a stop-and-fix item before the first high-risk patient connects, and the clinical head hears about it the same morning.}}
{{call:Defibrillator fails its self-test, pads are missing or expired, or oxygen will not last a transfer: tell the charge nurse and the Dialysis Clinical Head before the first connection, and follow your unit protocol for which patients may start. Always ask the attending nephrologist for guidance on any high-risk patient whose session is delayed.}}
"""),
        ("roles", "Roles and transfer", "Roles on the roster, and how help arrives", """
<p>Philippine rules set the minimum: dialysis nurses hold a current BLS certificate; the physician-on-duty holds current ACLS from a DOH-accredited provider; and at least one nurse on every shift holds an updated ACLS certificate.[[doh2012]][[psn2024]] A roster can have enough nurses and still leave a shift without a current ACLS holder, so the charge nurse checks names, not headcount.</p>
{{fig:rl01_roster}}
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>Who usually holds it</th><th>Combine with (small team)</th></tr></thead>
<tbody>
<tr><td>Leader</td><td>Physician-on-duty; the ACLS-current nurse until the physician arrives</td><td>Defibrillator and drugs, if only three staff</td></tr>
<tr><td>Compressor 1 and 2</td><td>Any BLS-trained staff, including technicians and assistants</td><td>Airway (swap every 2 minutes)</td></tr>
<tr><td>Airway</td><td>Nurse or physician</td><td>Compressor 2</td></tr>
<tr><td>Defibrillator and drugs</td><td>ACLS-current nurse</td><td>Leader</td></tr>
<tr><td>Circuit nurse</td><td>The patient&rsquo;s dialysis nurse</td><td>Recorder, once the circuit is safe</td></tr>
<tr><td>Recorder and timer</td><td>Any staff who can write and keep time</td><td>Runner</td></tr>
<tr><td>Watcher</td><td>A nurse who stays with the other patients</td><td>Never combined with the arrest</td></tr>
<tr><td>Runner</td><td>Technician, assistant or clerk</td><td>Recorder</td></tr>
</tbody></table></div>
<h3>Freestanding and hospital-based units</h3>
<p>A hospital-based unit can call a code team that arrives in minutes. A freestanding unit is, for practical purposes, an out-of-hospital arrest site: registries count clinic arrests as out-of-hospital events.[[pun2019]] Help means an ambulance, and the minutes until it arrives belong to your team. Post the ambulance numbers, know the realistic travel time at 6:00 a.m. and at 5:00 p.m., and agree with the receiving emergency room in advance what you will send with the patient. Call the ambulance early: the runner calls as soon as the code is called, not after the first rhythm check.</p>
{{key:Name the code roles at the start of every shift from the real roster, confirm an ACLS-current nurse is present, and call the ambulance at the moment the code is called.}}
{{scene:Two-minute huddle|<p>At 5:55 a.m., charge nurse Ms. Dizon reads the roles aloud: &ldquo;Leader until Dr. Salonga arrives: Joy. Compressors: Paolo and Ben. Circuit: the patient&rsquo;s own nurse. Recorder: Liza. Watcher: Grace. Runner and ambulance: Mang Tony.&rdquo; She adds, &ldquo;Mr. Bautista is at Station 2, right in front of the cart.&rdquo;</p>
<p class="tc-scene-take">The huddle took two minutes. Nobody will have to ask &ldquo;who does what?&rdquo; during an arrest today.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>What matters most.</strong> The defibrillator. A battery warning plus expired pads means the unit cannot reliably shock a shockable rhythm today. Ms. Dizon puts the device on charge, sends Mr. Ramos for a spare battery or a loaned device and fresh pads, and calls the Dialysis Clinical Head before 6:00. The oxygen cylinder is swapped for a full one. Suction works.</p>
<p><strong>Can the shift start?</strong> That is a unit policy decision made in advance, not improvised at 5:45. A sensible policy delays the highest-risk patients until a working defibrillator is at hand and records who decided. Mr. Bautista (missed session, recent discharge) should not connect before then, and the physician-on-duty should review his order and potassium when she arrives. The two patients on a 1.0 mEq/L bath are flagged for the physician to review.</p>
<p><strong>Roles.</strong> A leader until the physician arrives (the ACLS-current nurse), two compressors, a circuit nurse, a recorder, a runner who also calls the ambulance, and a watcher who never joins the arrest. Mr. Bautista sits in the station with the clearest view and closest to the cart.</p>
<p>None of this needed a guideline grade. It needed a check done as if today were the day.</p>
"""],
    "skills": {"title": "A morning readiness check and a role huddle",
               "intro": "Using your own unit&rsquo;s cart and defibrillator (in training mode), complete the check and run a two-minute role huddle while a supervisor observes.",
               "items": [
                   ("Confirms the defibrillator self-test, battery and pad expiry, and names the action for any failure.", True),
                   ("Checks the bag-valve-mask, masks, oxygen pressure, tubing, airways and suction, and tests the suction.", True),
                   ("Checks the drug tray seal and expiry dates against the unit list, and the glucose meter.", False),
                   ("Escalates a failed defibrillator or oxygen check to the charge nurse and clinical head before the first connection.", True),
                   ("Reads the day&rsquo;s list for risk flags (Monday, missed session, low-potassium bath, recent discharge, large fluid goal).", False),
                   ("Assigns every code role from the real roster, including a watcher who will not join the arrest.", True),
                   ("States the ambulance number, the realistic travel time, and when the runner calls it.", False),
               ],
               "placement": "For one week, do the morning check with the charge nurse and record every item that was missing or failed. Present the list at the next staff meeting."},
    "terms": [("Chain of survival", "The linked actions that give the best chance of survival, from recognition to recovery."),
              ("Watcher", "The staff member who keeps every other connected patient safe during an arrest."),
              ("Freestanding unit", "A dialysis unit outside a hospital, where help arrives by ambulance."),
              ("Self-test", "The defibrillator&rsquo;s automatic daily check of battery and circuits."),
              ("Potassium bath", "The potassium concentration of the dialysis fluid, in mEq/L."),
              ("Long interdialytic gap", "The two-day gap between sessions over the weekend.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit, for the whole team.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-4", "calc-resuscitation-lab-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["01"])
