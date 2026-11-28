"""Disaster quick cards 15 to 19 for academy/emergency-cards.html (blueprint section 9; approved in principle by Dr. Rivero on
November 28, 2026, for drafting). Rendered by apply_emergency_cards.py.

These cards are DRAFTS. A card appears on the live quick card page only when REVIEW below records status "reviewed" with a
reviewer and date. Until then it appears only on academy/emergency-cards-disaster-draft.html (noindex), for review.
Content rules (same as emergency_cards_data.py):
  * every step follows the Disaster Preparedness and Response modules and Physician-on-Duty Module 30 named in "learn";
  * no drug doses; every card names who acts, the circuit action, and whether the blood is returned;
  * the blood rule matches Resuscitation Lab Module 7 and Disaster Module 6 word for word in meaning;
  * patients never disconnect themselves (Dr. Rivero's decision, November 28, 2026).
Step tuple: (who, html, same_time)."""

CHECKED = "November 28, 2026"

REVIEW = {  # add {"status": "reviewed", "by": "...", "date": "..."} per card after sign-off; the card then goes live
}

SHORT = {
    "dp_ozen2026": "Ozen 2026", "dp_lurie2015": "Lurie 2015", "dp_anderson2009": "Anderson 2009",
    "dp_fema2025": "FEMA 2025", "dp_ocd_nsed": "OCD NSED 2026", "dp_ra9514": "Fire Code RIRR 2019",
    "dp_lin2021": "Lin 2021", "dp_pagasa_tcws": "PAGASA wind signals", "dch_doh2013": "Department of Health 2013",
}

LESSONS = {
    "disaster-preparedness-03-unit-plan-and-command.html": "Disaster Preparedness 3",
    "disaster-preparedness-05-typhoons-and-floods.html": "Disaster Preparedness 5",
    "disaster-preparedness-06-earthquake-on-the-machine.html": "Disaster Preparedness 6",
    "disaster-preparedness-07-fire-and-evacuation.html": "Disaster Preparedness 7",
    "disaster-preparedness-08-power-water-supplies.html": "Disaster Preparedness 8",
    "physician-on-duty-30-when-the-power-or-water-fails.html": "Physician-on-Duty 30",
    "water-treatment-technician-12-failures-emergencies-capstone.html": "Water Treatment Technician 12",
    "dialysis-head-nurse-12-disaster-and-service-leadership.html": "Head Nurse 12",
    "resuscitation-lab-07-arrest-in-the-dialysis-chair.html": "Resuscitation Lab 7",
}

BLOOD_RULE = ("Blood that may contain air, is hemolyzed, or follows a severe reaction is never returned. Otherwise return it if quick "
              "and safe, or clamp and disconnect. Close a central catheter&rsquo;s own clamps before separating its lines.")

CARDS = [
dict(id="power-failure", num=15, group="disaster", title="Power fails during dialysis",
 index="Power failure mid-session",
 when="The main power fails with patients connected: machines alarm on battery, lights flicker or go out. The generator may or may not start.",
 steps=[
  ("Every nurse", "<b>Stay with your patients.</b> Check airway, alertness and the access; uncover every needle site and look for bleeding.", False),
  ("Technician", "<b>Report the power status:</b> has the generator started, is it stable, and how long will its fuel last?", True),
  ("Charge nurse + POD", "<b>Decide.</b> Continue on the generator only if the technician confirms it is stable. Wait only as long as your protocol allows; otherwise begin the emergency take-off.", False),
  ("Chair nurse", "<b>Without power, return the blood by hand crank,</b> one staff member per patient, watching the venous drip chamber and line until the clamp is closed.", False),
  ("Chair nurse", "<b>Clamp and cut, do not return,</b> after air, hemolysis, a clotted circuit, or when there is no time. Close catheter clamps before separating the lines.", False),
  ("Charge nurse", "<b>Count and record every patient:</b> time off, method, blood returned or not.", False),
  ("POD", "<b>Call the attending nephrologist and the Medical Director</b> (SBAR); emergency transfer for anyone unstable.", False),
 ],
 warn="<b>Without power the air detector and venous clamp may not work:</b> one staff member watches each venous line until the clamp is closed. Never force a clotted circuit back. Patients never disconnect themselves.",
 det=dict(
  diff="A tripped breaker on one circuit (only some machines down); a generator that runs the machines but not the water booster pump (low water pressure alarms minutes later); a water failure rather than a power failure.",
  monitor="Blood pressure, alertness and access sites during and after the return. The generator&rsquo;s fuel and load; the water pressure.",
  circuit="No new connections. On a stable generator, sessions may continue per protocol. With a known end time (fuel running out), end sessions in order while the generator still runs, so the alarms still work.",
  blood="Yes, by hand crank, if the circuit is sound and there is time. No after air, hemolysis, a clotted circuit, or when there is no time. " + BLOOD_RULE,
  escalate="The attending nephrologist and the Medical Director by SBAR (Situation, Background, Assessment, Recommendation); emergency transfer for any unstable patient. The technician calls the fuel supplier and the utility.",
  restart="No new starts until power is stable and the water system has been checked. If the unit closed: only through the five signed restart gates.",
  document="Time of failure, power status reports, each patient&rsquo;s time off, method, blood returned or not and why, and condition; calls made."),
 learn=["physician-on-duty-30-when-the-power-or-water-fails.html", "disaster-preparedness-08-power-water-supplies.html"],
 refs=["handbook", "saha"]),

dict(id="earthquake", num=16, group="disaster", title="Earthquake during dialysis",
 index="Earthquake on the machine",
 when="The ground shakes while patients are connected.",
 steps=[
  ("Everyone", "<b>During shaking, protect in place.</b> Patients stay seated and connected, covering head and neck with the free arm or a pillow. Staff duck, cover and hold beside the nearest patient, shielding the head and steadying the access arm.", False),
  ("Everyone", "<b>Do not disconnect during shaking.</b> Nobody runs.", True),
  ("Chair nurse", "<b>When it stops, check every patient first:</b> needles and lines secure, no blood at the connections. Press and clamp any dislodged needle.", False),
  ("Technician", "<b>Check the machines:</b> upright, running, no water leak; then the water room and the power.", True),
  ("Charge nurse", "<b>Check the room:</b> gas smell, fire, new cracks, exits. Count everyone.", False),
  ("Charge nurse", "<b>Evacuation ordered, or the building unsafe?</b> No: continue or end each session per protocol. Yes: emergency take-off by staff with the blood rule, then out by the stairs (Card 17 for the census).", False),
  ("POD", "<b>Examine anyone hurt or unwell; call the attending nephrologist.</b>", False),
 ],
 warn="<b>Never disconnect during shaking.</b> Never return blood that may contain air, is hemolyzed, or follows a severe reaction. Expect aftershocks: protect in place again each time.",
 det=dict(
  diff="An aftershock; a fall or injury; a dislodged needle hidden under a blanket; a gas or water leak; damage in the water room.",
  monitor="Each patient&rsquo;s pressure and access after the shaking; aftershocks; the building or facilities officer&rsquo;s report.",
  circuit="Stay: sessions continue or end per protocol, patient by patient. Evacuate: emergency take-off by staff.",
  blood=BLOOD_RULE,
  escalate="The attending nephrologist; the building or facilities officer; emergency services for injuries; the local disaster office (LDRRMO) for area-wide damage.",
  restart="After a strong earthquake, a qualified engineer or building official checks the structure before the unit treats patients again; if the unit closed, the five signed restart gates.",
  document="Time and duration, patients connected, injuries, access events, take-off times and blood decisions, building findings, calls."),
 learn=["disaster-preparedness-06-earthquake-on-the-machine.html", "resuscitation-lab-07-arrest-in-the-dialysis-chair.html"],
 refs=["dp_fema2025", "dp_ocd_nsed", "dp_ozen2026"]),

dict(id="fire", num=17, group="disaster", title="Fire or smoke in the unit",
 index="Fire or smoke",
 when="Smoke, flame, a burning smell, or a fire alarm.",
 steps=[
  ("First to see it", "<b>Raise the alarm and close the door</b> to the fire room if it is safe. If you are with a connected patient, call out; do not leave the patient.", False),
  ("Staff without a patient", "<b>Call the Bureau of Fire Protection</b> (and the hospital&rsquo;s emergency number in a hospital-based unit); tell the charge nurse.", True),
  ("Charge nurse", "<b>Decide.</b> A small fire with an exit behind you: trained staff may use an extinguisher (pull, aim, squeeze, sweep). A growing fire or spreading smoke: evacuate. Turn off oxygen not in use; move cylinders if safe.", False),
  ("Chair nurses", "<b>Take-off by staff,</b> patients nearest the fire first: clamp and disconnect; close catheter clamps before separating lines; pressure on fistula sites.", False),
  ("Assigned helpers", "<b>Move patients by mobility category</b> on the evacuation sheet. Stairs, never elevators; stay low in smoke.", False),
  ("Census nurse", "<b>At the assembly point, check every name</b> on the list. Report anyone missing at once to the charge nurse and the firefighters.", False),
 ],
 warn="<b>Never leave a connected patient to fetch an extinguisher.</b> Patients never disconnect themselves. Nobody re-enters a burning building.",
 det=dict(
  diff="An electrical fire in equipment (never use water on it); fumes from reprocessing chemicals; smoke from outside the building. Treat any alarm as real until the charge nurse is told otherwise by the fire service or the building officer.",
  monitor="Breathing and smoke exposure, access sites after the take-off, the census at the assembly point.",
  circuit="Emergency take-off by staff. In a fire, clamp and disconnect is usually right.",
  blood="Usually not returned in a fire (there is no time). " + BLOOD_RULE,
  escalate="The Bureau of Fire Protection; the hospital&rsquo;s emergency number; the attending nephrologist about treatments cut short; the unit manager.",
  restart="Only after the fire service or building officer clears the building and the five restart gates are signed.",
  document="Time of discovery, alarm and calls, each patient&rsquo;s time off and method, the census, anyone missing or injured, the building clearance."),
 learn=["disaster-preparedness-07-fire-and-evacuation.html"],
 refs=["dp_ra9514", "dp_lin2021", "dp_ozen2026"]),

dict(id="typhoon", num=18, group="disaster", title="Typhoon warning raised",
 index="Typhoon warning",
 when="PAGASA raises a Tropical Cyclone Wind Signal for your area, or forecasts one that will arrive before the next sessions.",
 steps=[
  ("Incident lead", "<b>Activate the plan at your unit&rsquo;s trigger;</b> log the time; tell the unit manager and the Dialysis Clinical Head.", False),
  ("Charge nurse", "<b>Call-down:</b> staff first (who can work, who can stay), then patients due in the next 24 hours, then the rest.", False),
  ("Attending nephrologist", "<b>Decide early dialysis:</b> who comes early and when, from the flags the unit gives (recent high potassium, large weight gains, heart failure, missed sessions, flood-prone areas, transport).", False),
  ("Head nurse", "<b>Roster and transport:</b> minimum staffing with a nurse current in Advanced Cardiovascular Life Support (ACLS), staff transport, and a last safe session time.", False),
  ("Technician", "<b>Fuel, water, supplies:</b> generator fuel and test, water storage, supplies above the flood line.", True),
  ("Chair nurses", "<b>Remind every patient:</b> the emergency diet starts after this session; medicines, go-bag, emergency card and backup unit; do not wade in flood water.", False),
 ],
 warn="<b>Nobody travels onto flooded roads to keep a schedule.</b> Any change to a schedule, session length or fluid goal is the attending nephrologist&rsquo;s decision.",
 det=dict(
  diff="Heavy rain without a strong wind signal (floods can come without one); a signal that changes; a storm passing elsewhere that still cuts roads or power.",
  monitor="PAGASA bulletins and local disaster office advisories; staff and patients reached on the call-down.",
  circuit="Normal sessions until the last safe session time; no new connections after it.",
  blood="Normal rinse-back for sessions ended early on the nephrologist&rsquo;s order.",
  escalate="The attending nephrologist for early dialysis; the unit manager for transport and receiving units; the local disaster office (LDRRMO) for evacuation advice.",
  restart="After the storm: find every patient within 24 hours; reopen only through the five signed restart gates.",
  document="Activation time, call-down results, the nephrologist&rsquo;s decisions, early sessions, staff transport, patients not reached."),
 learn=["disaster-preparedness-05-typhoons-and-floods.html", "disaster-preparedness-03-unit-plan-and-command.html", "dialysis-head-nurse-12-disaster-and-service-leadership.html"],
 refs=["dp_pagasa_tcws", "dp_lurie2015", "dp_anderson2009"]),

dict(id="water-failure", num=19, group="disaster", title="Water supply failure or contamination alarm",
 index="Water failure or contamination",
 when="The water supply stops, low water pressure alarms, a water test fails, a contamination alarm sounds, or two or more patients have the same symptoms in one shift (chest or back pain, wine-colored blood in the venous line, itching, nausea, chills).",
 steps=[
  ("Charge nurse", "<b>Stop starting new treatments.</b>", False),
  ("Chair nurses", "<b>End current treatments per protocol.</b> If hemolysis is possible (pain, wine-colored blood): stop the pump, clamp, do not return the blood.", False),
  ("Technician", "<b>Check the water system and hold the water room as it is.</b> Keep circuits, dialyzers and fluid samples if contamination is suspected.", True),
  ("POD", "<b>Examine everyone on the affected loop,</b> not only those with symptoms. Send the sick per protocol, with an electrocardiogram (ECG).", False),
  ("POD", "<b>Call the attending nephrologist and the Medical Director at once.</b>", False),
  ("Charge nurse", "<b>Resume only after a signed water release</b> by the water treatment technician and the medical head.", False),
 ],
 warn="<b>Two patients with the same symptoms in the same shift is a water problem until proven otherwise.</b> Running water is not released water: no restart without a signed release.",
 det=dict(
  diff="A single machine fault or a kinked line (hemolysis in one patient); a pyrogenic reaction cluster (Card 14); a supply interruption without contamination.",
  monitor="Symptoms, blood pressure, ECG and potassium in symptomatic patients; blood counts later if hemolysis is suspected.",
  circuit="No new starts; end current treatments per protocol; keep circuits for investigation.",
  blood="Not returned if hemolysis or contamination is possible. In a pure supply interruption with a sound circuit and no symptoms, return per protocol. " + BLOOD_RULE,
  escalate="The attending nephrologist and the Medical Director at once. The steps of the Department of Health&rsquo;s dialysis water order follow: stop operations until a repeat test complies, disinfect the loop, notify patients.",
  restart="Only after the repeat test complies, the loop is disinfected and the water release is signed.",
  document="Times, symptoms by patient and station, the water loop, actions, samples kept, test results, the release signature."),
 learn=["disaster-preparedness-08-power-water-supplies.html", "physician-on-duty-30-when-the-power-or-water-fails.html", "water-treatment-technician-12-failures-emergencies-capstone.html"],
 refs=["dch_doh2013", "saha", "handbook"]),
]
