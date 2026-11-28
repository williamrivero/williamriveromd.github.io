# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 06: Earthquake on the Machine. DRAFT.
Consistency lock (blueprint section 4): the emergency take-off rule here and the circuit decision in Resuscitation Lab Module 7
are one rule. Any edit to either changes both."""

MODULE = {
    "image_alt": "A nurse crouching beside a patient who stays seated and connected in a dialysis recliner, shielding the patient's head and steadying the access arm.",
    "objectives": [
        "Protect patients in place during shaking: patients stay connected and covered; staff duck, cover and hold without leaving a patient.",
        "Check every patient, line, needle and machine after the shaking, in a set order.",
        "Decide when patients stay and when they come off, and perform the emergency take-off with the blood rule.",
        "Explain why the building is checked before anyone stays, and how aftershocks change the plan.",
        "Secure equipment before an earthquake, and join the quarterly Nationwide Simultaneous Earthquake Drill.",
    ],
    "big": """
{{plain:When the ground shakes, a connected patient is like a passenger strapped into a seat on a bumpy flight. Unbuckling and walking the aisle is far more dangerous than staying put and holding on. The crew does not open the doors mid-air; they wait until it is safe, then help everyone off in order.}}
<p>The picture has a limit. A seatbelt keeps a passenger safe; a dialysis circuit does not. Shaking can pull a needle, kink or separate a line, tip a machine or a pole, and send equipment sliding. That is why staff stay close during the shaking, and why the checks afterward start with the needles and lines.</p>
<p>The national advice is &ldquo;duck, cover and hold,&rdquo; practiced each quarter in the Nationwide Simultaneous Earthquake Drill (NSED).[[dp_ocd_nsed]] For a person who cannot drop to the floor, such as a patient in a recliner, the advice is to stay put, cover the head and neck with the arms or a pillow, and hold on until the shaking stops.[[dp_fema2025]] PHIVOLCS reports the magnitude and location after the event.</p>
{{cards:Key terms for this module|Protect in place::Staying where you are during shaking and protecting the head, neck and access, instead of moving.|Duck, cover and hold::The Philippine earthquake drill action: get low, cover the head, hold on until the shaking stops.|Emergency take-off::Ending treatments quickly, by staff, because the unit must be evacuated or cannot continue.|Blood rule::The one rule for returning circuit blood in any emergency, shared with the Resuscitation Lab.|Aftershock::A smaller earthquake after the main one, which can come minutes to days later.|Structural check::An inspection of the building by a qualified engineer or building official.}}
""",
    "case": {"title": "Magnitude 6.8 at 9:40 a.m.", "html": """
<p>At 9:40 a.m. a strong earthquake shakes a second-floor unit in Lipa, Batangas, for about 40 seconds. Sixteen patients are connected. Five staff are on the floor: the charge nurse, three nurses and a technician. Ceiling panels fall near Station 4; a saline pole tips over at Station 9; the lights flicker but stay on.</p>
<p>When the shaking stops, a patient at Station 12 is pulling at his lines and shouting, &ldquo;Take me off, I want to go down!&rdquo; Another nurse says, &ldquo;Let us disconnect everyone and go down to the street.&rdquo; PHIVOLCS later reports a magnitude 6.8 event.</p>
""", "questions": ["What should staff and patients have done during the 40 seconds of shaking?",
                  "In what order do you check after the shaking?",
                  "Who decides whether the unit evacuates, and what has to be true before patients stay?"]},
    "sections": [
        ("during", "During the shaking", "Protect in place", """
<p><strong>Patients stay connected.</strong> Disconnecting during shaking is more dangerous than staying: hands are unsteady, the patient may fall, and an open line or catheter can bleed or draw in air. The patient stays seated, covers the head and neck with the free arm or a pillow, and keeps the access arm still.</p>
{{fig:dp06_protect_in_place}}
<p><strong>Staff duck, cover and hold, without leaving a patient.</strong> A nurse within reach of a patient crouches beside the recliner, shields the patient&rsquo;s head and steadies the access arm if it is safe to do so, and holds on. Staff do not run across the floor during shaking, and nobody runs for the stairs.</p>
<p>Shaking usually lasts seconds to about a minute. Count, stay low, and wait until it stops.</p>
{{key:During shaking: patients stay connected and covered; staff stay low beside the patients; nobody disconnects and nobody runs.}}
"""),
        ("after", "After the shaking", "The checks after the shaking", """
<p>When the shaking stops, the charge nurse calls for the checks in a set order. The patients come first, the building second.</p>
{{fig:dp06_after_the_shaking}}
<ol>
<li><strong>Every patient:</strong> conscious, breathing, not injured; needles and lines secure; no blood at the connections. A dislodged needle is pressed and clamped at once (the same first aid as any needle dislodgement).</li>
<li><strong>Every machine:</strong> upright, running, no alarm that stops treatment; no water leak.</li>
<li><strong>The room:</strong> no gas smell, no fire, no new cracks in walls or columns, exits clear.</li>
<li><strong>Everyone accounted for:</strong> patients, staff, companions and visitors.</li>
</ol>
<p>The technician checks the water room and the power; the physician-on-duty examines any patient who was hurt or became unwell. Expect aftershocks: repeat the protect-in-place step with each one.</p>
"""),
        ("decide", "Take off or stay", "Stay, end the session, or take everyone off", """
<p>Most strong earthquakes do not end the shift. The decision has one main question: <strong>has evacuation been ordered, or is the building unsafe?</strong></p>
{{fig:dp06_take_off_or_stay}}
<ul>
<li><strong>No:</strong> continue or end each session per protocol, patient by patient, as the physician and charge nurse decide. Patients who are frightened, hurt or unwell may end early.</li>
<li><strong>Yes:</strong> emergency take-off by staff, then evacuate (Module 7).</li>
</ul>
<p><strong>The blood rule (the same rule as the Resuscitation Lab).</strong> Blood that may contain air, is hemolyzed, or follows a severe reaction is never returned. Otherwise, return the blood if it is quick and safe, or clamp and disconnect. A central venous catheter&rsquo;s own clamps are closed before its lines are separated. This is the circuit decision taught in <a href="resuscitation-lab-07-arrest-in-the-dialysis-chair.html">Resuscitation Lab, Module 7</a>; the two modules give one rule.</p>
<p><strong>Who decides about the building.</strong> Visible damage (cracks in columns or beams, a leaning structure, a gas smell, fire) means evacuate; the incident lead decides with the building or facilities officer. Before the unit treats patients again after a strong quake, a qualified engineer or building official checks the structure; for a hospital-based unit, the hospital&rsquo;s plan decides. The unit does not stay in a damaged building to finish a schedule.</p>
{{call:Evacuation ordered, visible structural damage, gas smell or fire: emergency take-off by staff with the blood rule, then evacuate (Module 7). Follow your unit protocol, and always ask the attending nephrologist for guidance on ending or resuming treatment.}}
"""),
        ("secure", "Before the next one", "Securing the unit, and the quarterly drill", """
<p>Most earthquake injuries indoors come from falling and sliding objects. Secure them before the next quake.</p>
{{fig:dp06_secure_equipment}}
<ul>
<li>Lock machine and recliner wheels during treatment.</li>
<li>Strap tall equipment and water treatment components to the wall, as the manufacturer and the engineer advise.</li>
<li>Use shelves with lips or restraints for supplies; keep heavy items low.</li>
<li>Chain oxygen cylinders upright.</li>
</ul>
<p><strong>Join the NSED.</strong> The Office of Civil Defense holds the Nationwide Simultaneous Earthquake Drill each quarter (in 2026, on March 12, June 18, September 10 and November 5).[[dp_ocd_nsed]] A dialysis unit can join it with the whole shift. Patients take part only in the protect-in-place step, and only if they agree; nobody is disconnected or moved for a drill, and a named watcher stays with the patients.</p>
<div class="alert alert-amber"><div class="alert-icon">🧒</div><div class="alert-body"><h4>Units that dialyze children</h4><p>A small child may not stay still. The caregiver or nurse holds and shields the child in the bed or chair, keeping the access steady. A child&rsquo;s circuit holds a larger share of the blood volume, so the blood rule and the pediatric nephrologist&rsquo;s instructions matter even more in a take-off.</p></div></div>
"""),
    ],
    "debrief": ["""
<p><strong>During the shaking.</strong> Patients stay connected, covering head and neck and keeping the access arm still. The five staff stay low beside patients, shielding heads and access arms where they can; nobody crosses the floor or disconnects anyone.</p>
<p><strong>After.</strong> The charge nurse calls the checks: every patient and every access first (Station 12&rsquo;s lines, the patients near the fallen panels at Station 4 and the pole at Station 9), then the machines, the room (gas, fire, cracks, exits), then a count of everyone. The technician checks water and power. The man at Station 12 is calmed by a nurse who checks his needles and explains that staff will take him off if the unit leaves.</p>
<p><strong>Stay or go.</strong> The incident lead decides with the building or facilities officer. Visible structural damage means emergency take-off with the blood rule and evacuation down the stairs, never the elevator. Without damage, sessions continue or end per protocol, patient by patient, with protect-in-place repeated in aftershocks, and the building is checked before the next shift.</p>
"""],
    "skills": {"title": "Protect in place and the emergency take-off",
               "intro": "At an empty station with a manikin in a recliner connected to a training circuit, during a facilitated earthquake drill.",
               "items": [
                   ("During the simulated shaking, stays low beside the patient, shields the head and steadies the access arm.", True),
                   ("Does not disconnect during shaking.", True),
                   ("After the shaking, checks the patient, needles and lines, then the machine, then the room, in order.", False),
                   ("States the stay-or-go question and who decides it.", False),
                   ("Performs the emergency take-off with the blood rule: never returns blood after air, hemolysis or a severe reaction.", True),
                   ("Closes a central catheter&rsquo;s own clamps before separating the lines.", True),
                   ("Confirms everyone is accounted for before leaving the floor.", False),
               ],
               "placement": "Join the next quarterly NSED with your shift, with a named watcher for the patients."},
    "terms": [("Protect in place", "Staying where you are during shaking and protecting the head, neck and access."),
              ("Duck, cover and hold", "Get low, cover the head, hold on until the shaking stops."),
              ("Emergency take-off", "Ending treatments quickly, by staff, because the unit must be evacuated."),
              ("Blood rule", "Never return blood after air, hemolysis or a severe reaction; otherwise return if quick and safe, or clamp and disconnect."),
              ("Aftershock", "A smaller earthquake after the main one."),
],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient guide to disaster preparation, including earthquakes.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
