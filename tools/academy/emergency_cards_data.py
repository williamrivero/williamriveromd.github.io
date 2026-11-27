"""Card data for academy/emergency-cards.html (rendered by apply_emergency_cards.py).

Cards 3 to 14 (Nov 27 2026, Dr. Rivero's expansion brief). Every card here is a DRAFT until a clinical reviewer is
recorded in REVIEW below. Content rules:
  * align with the Academy modules named in "learn" (Physician-on-Duty 13 to 19, Nephrology Nursing 9 and the rest);
  * no drug doses: drugs are named with "per the unit's protocol / order set" (doses live in unit protocols);
  * every card states who acts, which circuit action (stop UF, stop the blood pump, clamp, return the blood,
    disconnect, end the treatment), and whether the blood is returned;
  * sources are keys of data/academy-emergency-cards-refs.json (APA 7, PubMed-verified).
Step tuple: (who, html, same_time). who="" for no role chip. same_time=True prints "At the same time".
"""

CHECKED = "November 27, 2026"
CHECKED_SIGNED = "November 28, 2026"

# Clinical review status per card id. A card is "reviewed" only when a reviewer and date are recorded here.
REVIEW = {  # Dr. Rivero signed off all 14 cards on November 28, 2026
    "code": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "leak": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "hypotension": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "access-bleeding": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "air-embolism": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "hemolysis": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "anaphylaxis": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "chest-pain": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "arrhythmia": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "hyperkalemia": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "hypoglycemia": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "seizure": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "stroke": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
    "fever-rigors": {"status": "reviewed", "by": "Dr. William Gregory Rivero", "date": "November 28, 2026"},
}

SHORT = {   # short labels for the in-card Sources line
    "saha": "Saha &amp; Allon 2017", "greenberg": "Greenberg &amp; Choi 2021", "kooman": "EBPG 2007 (Kooman)",
    "reeves": "Reeves &amp; Mc Causland 2018", "kanbay": "Kanbay 2020", "flythe2020": "KDIGO 2020 (Flythe)",
    "vanwael": "Van Waeleghem 2008", "ribitsch": "Ribitsch 2014", "frinak": "Frinak 2023", "duffy": "Duffy 2000",
    "tipple": "Tipple 1991", "daug1988": "Daugirdas &amp; Ing 1988", "gulati": "AHA/ACC chest pain 2021",
    "aha9": "AHA 2025 Part 9", "aha10": "AHA 2025 Part 10", "turakhia": "KDIGO 2018 (Turakhia)",
    "montague": "Montague 2008", "clase": "KDIGO 2020 (Clase)", "mahoney": "Cochrane 2005 (Mahoney)",
    "apel": "Apel 2014", "abe": "Abe &amp; Kalantar-Zadeh 2015", "titoff": "T&iacute;toff 2019",
    "prabhakaran": "AHA/ASA stroke 2026", "seliger": "Seliger 2003", "mermel": "IDSA 2009 (Mermel)",
    "lok": "KDOQI vascular access 2019", "prescott": "Surviving Sepsis 2026", "kantor": "Kantor 1983",
    "quittnat": "Quittnat Pelletier 2016", "handbook": "Handbook of Dialysis 2015", "lott": "ERC 2021",
    "golden2023": "Anaphylaxis practice parameter 2023", "ada2026": "ADA Standards 2026, Section 6",
    "glauser2016": "AES status epilepticus 2016", "hofacker": "Hofacker 2020",
}

LESSONS = {  # file -> short label for "Learn it" links (files are checked to exist at build time)
    "physician-on-duty-06-water-and-dialysate.html": "Physician-on-Duty 6",
    "physician-on-duty-12-first-sessions-and-unusual-sessions.html": "Physician-on-Duty 12",
    "physician-on-duty-13-when-the-pressure-falls.html": "Physician-on-Duty 13",
    "physician-on-duty-15-heart-emergencies-in-the-chair.html": "Physician-on-Duty 15",
    "physician-on-duty-16-when-the-circuit-fails.html": "Physician-on-Duty 16",
    "physician-on-duty-17-fever-and-bloodstream-infection.html": "Physician-on-Duty 17",
    "physician-on-duty-18-potassium-sugar-and-the-brain.html": "Physician-on-Duty 18",
    "physician-on-duty-19-bleeding-and-heparin.html": "Physician-on-Duty 19",
    "physician-on-duty-22-diabetes-on-dialysis.html": "Physician-on-Duty 22",
    "nephrology-nursing-07-hd-vascular-access-infection-prevention.html": "Nephrology Nursing 7",
    "nephrology-nursing-09-hd-session-complication-response.html": "Nephrology Nursing 9",
    "dialysis-charge-nurse-07-mid-session-surveillance.html": "Charge Nurse 7",
    "dialysis-charge-nurse-11-water-and-machines-hold-release.html": "Charge Nurse 11",
    "dialysis-head-nurse-04-vascular-access-and-bleeding.html": "Head Nurse 4",
    "dialysis-nurse-assistant-07-access-protection-monitoring.html": "Nurse Assistant 7",
    "hemodialysis-technician-10-complications-emergency-response.html": "Dialysis Technician 10",
    "dialysis-biomedical-technician-07-protective-systems-alarm-testing.html": "Biomedical Technician 7",
    "attending-nephrologist-06-electrolyte-emergencies.html": "Attending Nephrologist 6",
    "attending-nephrologist-16-vascular-access-infection.html": "Attending Nephrologist 16",
}

DET_ORDER = [("diff", "Think of these too"), ("monitor", "Reassess and monitor"), ("circuit", "Circuit and access"),
             ("blood", "Return the blood?"), ("escalate", "Escalation and transfer"), ("restart", "Restart"),
             ("document", "Document and follow up")]

W_CALL = "Call the physician on duty (POD) and the attending nephrologist"

CARDS = [
# ───────────────────────────────────────────────────────────────── 3
dict(id="hypotension", num=3, group="deterioration", title="Severe low blood pressure or collapse on dialysis",
 index="Low blood pressure, collapse",
 when="Pressure falls during dialysis with yawning, cramps, nausea, dizziness or sweating, or the patient becomes faint. Unresponsive and not breathing normally: <a href=\"#code\">Card 1</a>.",
 steps=[
  ("Chair nurse", "<b>Lay the chair flat, legs raised,</b> as far as breathing allows; turn to the side if vomiting.", False),
  ("Chair nurse", "<b>Stop ultrafiltration (UF).</b> Keep the blood pump running unless you suspect air, hemolysis, a severe reaction or blood loss.", False),
  ("Second nurse", "<b>Check pulse, pressure, oxygen saturation and alertness.</b> Lift the blanket: look at the access and lines.", True),
  ("Chair nurse", "<b>Give saline through the circuit</b> per protocol if the pressure does not recover.", False),
  ("Second nurse", "<b>Call the physician on duty (POD) and the attending nephrologist</b> if the pressure stays low, falls again or needs more fluid; at once for chest pain, breathlessness, confusion, fever, bleeding or an abnormal pulse.", False),
  ("Charge nurse", "<b>Assign a watcher</b> for the other patients while two staff are at this chair.", True),
 ],
 warn="Collapse is not always the fluid removal. Chest pain, a new irregular pulse, fever, blood under the blanket, or early itching and wheeze point to another card: check before giving more fluid.",
 det=dict(
  diff="Bleeding from a dislodged needle or the gut (<a href=\"#access-bleeding\">Card 4</a>), arrhythmia (<a href=\"#arrhythmia\">Card 9</a>), acute coronary syndrome (<a href=\"#chest-pain\">Card 8</a>), sepsis (<a href=\"#fever-rigors\">Card 14</a>), dialyzer reaction or anaphylaxis (<a href=\"#anaphylaxis\">Card 7</a>), air (<a href=\"#air-embolism\">Card 5</a>), hemolysis (<a href=\"#hemolysis\">Card 6</a>), low blood sugar (<a href=\"#hypoglycemia\">Card 11</a>).",
  monitor="Repeat blood pressure, pulse and symptoms after each step, at the interval your protocol sets, until the patient is stable and the POD agrees. The legs-up position rests on expert opinion only, and a breathless patient may not tolerate lying flat.",
  circuit="Stopping UF stops fluid removal; blood keeps flowing through the dialyzer. The blood pump is stopped only for a circuit cause (air, hemolysis, severe reaction, blood loss). Changes to the UF goal, session time or dialysis fluid are the physician&rsquo;s decision.",
  blood="If the session is ended because the pressure will not recover, return the blood per protocol when the circuit is sound. Do not return it when air, hemolysis or a severe reaction is suspected, or through a clotted circuit.",
  escalate="Emergency transfer when the pressure does not recover after the protocol&rsquo;s steps, when consciousness stays altered, or when a dangerous cause is likely. The attending nephrologist decides whether to end the session.",
  restart="UF resumes only when symptoms settle and the pressure recovers, at the goal and rate the physician sets. Repeated episodes call for a review of the dry weight and prescription, not a habit of giving saline.",
  document="Times, blood pressure series, fluid removed and when UF stopped, fluid given, symptoms, who was called and when, and the outcome. File an incident report for a collapse or a transfer."),
 learn=["physician-on-duty-13-when-the-pressure-falls.html", "nephrology-nursing-09-hd-session-complication-response.html", "dialysis-charge-nurse-07-mid-session-surveillance.html"],
 refs=["kooman", "reeves", "kanbay", "flythe2020", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 4
dict(id="access-bleeding", num=4, group="circuit", title="Venous needle dislodgement or access bleeding",
 index="Needle out, access bleeding",
 when="Blood on the bed, chair or floor; a wet dressing or blanket over the access; a needle out or a line apart; or a patient who turns pale, sweaty or drowsy for no clear reason.",
 steps=[
  ("Any staff", "<b>Lift the blanket.</b> Look at both needle sites and both line connections.", False),
  ("Chair nurse", "<b>Stop the blood pump.</b> Clamp the line on both sides of the break.", False),
  ("Chair nurse", "<b>Press firmly on the site</b> with gloved hands and gauze, and keep pressing.", False),
  ("Second nurse", "<b>Lay the patient flat.</b> Check consciousness, pulse and blood pressure. Give oxygen per protocol.", True),
  ("Second nurse", "<b>Call for help and the emergency cart</b> if pale, sweaty, drowsy or hypotensive; call the physician on duty (POD) and the attending nephrologist.", False),
  ("Charge nurse", "<b>Estimate the loss</b> (bed, chair, blanket, floor) and assign a watcher for the other patients.", False),
 ],
 warn="The venous pressure alarm can stay silent when the needle comes out: a quiet machine proves nothing. Keep the access and connections in view all session. Never reinsert a dislodged needle or reconnect a line end that has been open.",
 det=dict(
  diff="Arterial needle out (air may be drawn in: see <a href=\"#air-embolism\">Card 5</a>), infiltration or hematoma, gastrointestinal bleeding, low blood pressure from other causes (<a href=\"#hypotension\">Card 3</a>).",
  monitor="Serial blood pressure, pulse and consciousness. Watch the site after pressure for rebleeding or swelling. Blood tests and fluids are the physician&rsquo;s decision.",
  circuit="Blood pump stopped and the line clamped on both sides of the break, so the circuit stays closed. A new needle at a new site is placed only on the physician&rsquo;s decision, with a sterile needle.",
  blood="Blood on the floor is lost. Published reviews give no rule for the blood still in the circuit after a dislodgement, so the unit protocol and the attending nephrologist decide. Blood is never returned through a line end that has been open.",
  escalate="The attending nephrologist for every event. Emergency transfer for shock, ongoing bleeding or a large loss. Fluids and transfusion are decided by the physician.",
  restart="Only after bleeding is controlled, the patient is stable and a new needle is placed, on the attending nephrologist&rsquo;s order. The heparin plan is reviewed before any restart.",
  document="Time found, estimated loss, vital signs over time, actions, who was called. Incident report. Review taping, access visibility and alarm limits; European renal nurses published 12 consensus practice points."),
 learn=["physician-on-duty-16-when-the-circuit-fails.html", "physician-on-duty-19-bleeding-and-heparin.html", "dialysis-head-nurse-04-vascular-access-and-bleeding.html", "dialysis-nurse-assistant-07-access-protection-monitoring.html"],
 refs=["saha", "vanwael", "ribitsch", "frinak", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 5
dict(id="air-embolism", num=5, group="circuit", title="Suspected air embolism",
 index="Air in the line",
 when="Air or foam in the venous line or below the venous chamber, or an air detector alarm, with or without a sudden cough, chest tightness, breathlessness, confusion or collapse.",
 steps=[
  ("Chair nurse", "<b>Stop the blood pump and clamp the venous line.</b> Never open the clamp or override the air detector.", False),
  ("Chair nurse", "<b>Do not return the blood.</b> Rinse-back would push more air into the patient.", False),
  ("Second nurse", "<b>Position the patient per the unit&rsquo;s protocol:</b> lying on the left side is the dialysis teaching. Never sit the patient up.", True),
  ("Second nurse", "<b>Give oxygen</b> per protocol. Check consciousness, breathing, pulse and oxygen saturation.", False),
  ("Charge nurse", "<b>Call for help and the emergency cart;</b> call the physician on duty (POD) and the attending nephrologist; arrange emergency transfer.", False),
  ("Any staff", "<b>Start CPR flat on the back</b> if there is no pulse and no normal breathing: go to <a href=\"#code\">Card 1</a>.", False),
 ],
 warn="Air on the patient side of the detector is an emergency even if the patient feels well at first. Keep the clamp closed until the source is found and a physician decides.",
 det=dict(
  diff="A false air alarm in a well patient (line not seated in the detector, tiny bubbles): the nurse finds the cause before anything is restarted. Also pulmonary embolism, heart attack, anaphylaxis.",
  monitor="Consciousness and focal signs (air can reach the brain in a seated patient), oxygen saturation, blood pressure, heart rhythm.",
  circuit="Blood pump stopped and venous line clamped. Look for the entry point: a loose connection before the pump, an empty saline bag, an open catheter limb, a cracked line. Keep the circuit for inspection; the machine is held until the biomedical technician checks the air detector and clamp.",
  blood="No. The blood in the circuit is not returned.",
  escalate="Emergency transfer for any symptomatic patient. The receiving hospital decides further treatment. <b>Clinical review required:</b> sources differ on position. Dialysis texts and reviews teach lying on the left side, some with the head down, and a 2021 review cautions that head-down may worsen brain swelling when air has reached the brain. The AHA 2025 special-circumstances guideline considers lying flat on the back or the recovery position reasonable for gas embolism. No trial compares positions; the unit should choose one.",
  restart="No restart on that machine until the cause is found and the detector passes its test. Any further dialysis is the attending nephrologist&rsquo;s decision.",
  document="Time, what was seen, alarm history, estimated amount of air, entry point, machine number, line and dialyzer lot numbers, actions and calls. Incident report and biomedical check."),
 learn=["physician-on-duty-16-when-the-circuit-fails.html", "hemodialysis-technician-10-complications-emergency-response.html", "dialysis-biomedical-technician-07-protective-systems-alarm-testing.html"],
 refs=["saha", "greenberg", "aha10", "handbook"]),

# ───────────────────────────────────────────────────────────────── 6
dict(id="hemolysis", num=6, group="circuit", title="Suspected hemolysis",
 index="Port-wine blood, hemolysis",
 when="Blood in the venous line looks translucent, cherry-red or &ldquo;port-wine,&rdquo; or a sample shows pink plasma, often with chest, back or belly pain, nausea and a rising blood pressure. Several patients may be affected.",
 steps=[
  ("Chair nurse", "<b>Stop the blood pump and clamp the lines.</b>", False),
  ("Chair nurse", "<b>Do not return the blood.</b> It carries potassium released from broken red cells.", False),
  ("Second nurse", "<b>Check airway, breathing and circulation;</b> give oxygen per protocol; attach the monitor.", True),
  ("POD", "<b>Order urgent potassium and hemoglobin</b> and the unit&rsquo;s hemolysis tests; call the attending nephrologist. Treat high potassium with <a href=\"#hyperkalemia\">Card 10</a>.", False),
  ("Charge nurse", "<b>Check every patient on the same water and concentrate supply.</b> Two or more affected: declare a possible cluster, hold new starts, call the Medical Director.", True),
  ("Technician", "<b>Keep the lines, dialyzer, packaging and lot numbers,</b> and take samples of water and dialysis fluid.", False),
 ],
 warn="Hemolysis is not a blood leak. A blood leak alarm finds blood in the used dialysis fluid (<a href=\"#leak\">Card 2</a>); hemolysis shows abnormal blood in the blood lines. With hemolysis, the blood is never returned.",
 det=dict(
  diff="Blood leak (<a href=\"#leak\">Card 2</a>), very dark blood of a clotting circuit, acute coronary syndrome or aortic dissection when chest or back pain is the main sign.",
  monitor="Continuous ECG (electrocardiogram) for potassium effects, repeat potassium and hemoglobin as the physician orders, and belly pain.",
  circuit="Blood pump stopped, lines clamped, treatment ended. The machine and the water loop are held until the technician checks dialysis fluid temperature and conductivity and the water for chlorine and chloramine. Kinked or faulty blood tubing has caused outbreaks.",
  blood="Never.",
  escalate="The attending nephrologist at once; the Medical Director for any suspected water or dialysis fluid fault or cluster. Emergency transfer for a high potassium, ECG change or unstable patient.",
  restart="Not until the cause is found and the water and dialysis fluid are confirmed safe, on a different machine if needed, on the physician&rsquo;s order.",
  document="Time, blood color, symptoms, machine number, dialyzer and tubing lot numbers, water and fluid test results, other patients checked. Incident report; device faults reported to the supplier and regulator per policy."),
 learn=["physician-on-duty-16-when-the-circuit-fails.html", "physician-on-duty-06-water-and-dialysate.html", "dialysis-charge-nurse-11-water-and-machines-hold-release.html"],
 refs=["saha", "duffy", "tipple", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 7
dict(id="anaphylaxis", num=7, group="circuit", title="Severe dialyzer reaction or anaphylaxis",
 index="Dialyzer reaction, anaphylaxis",
 when="Within the first minutes of treatment, or soon after a drug, any of: itching, hives, flushing, throat tightness, hoarseness, wheeze, breathlessness, swelling of the face or lips, low blood pressure or collapse.",
 steps=[
  ("Chair nurse", "<b>Stop the blood pump and clamp the lines.</b> Do not return the blood.", False),
  ("Charge nurse", "<b>Call for help and the emergency cart;</b> start the unit&rsquo;s anaphylaxis protocol.", True),
  ("Authorized nurse or POD", "<b>Give intramuscular epinephrine (adrenaline) into the outer thigh</b> as the protocol directs. It is the first-line treatment; do not wait for antihistamines or steroids.", False),
  ("Second nurse", "<b>Protect the airway; give oxygen;</b> position per protocol (flat with legs raised unless breathing is hard); attach the monitor.", True),
  ("Second nurse", "<b>Call the physician on duty (POD) and the attending nephrologist;</b> arrange emergency transfer.", False),
  ("Technician", "<b>Keep the dialyzer and its packaging;</b> record the model, lot number and sterilization method.", False),
 ],
 warn="When anaphylaxis is possible, treat it now. Epinephrine comes first; antihistamines and steroids do not replace it.",
 det=dict(
  diff="A milder, later (type B) reaction with chest or back pain, diagnosed only after cardiac, embolic and hemolytic causes are excluded; low blood pressure from fluid removal (<a href=\"#hypotension\">Card 3</a>); air (<a href=\"#air-embolism\">Card 5</a>); hemolysis (<a href=\"#hemolysis\">Card 6</a>). Drugs given during dialysis, such as intravenous iron, antibiotics or heparin, can also cause anaphylaxis.",
  monitor="Airway, breathing, blood pressure and oxygen saturation until handover; further epinephrine doses at the protocol&rsquo;s interval if symptoms persist; watch for symptoms returning.",
  circuit="Blood pump stopped, lines clamped, treatment ended. That dialyzer type is not used again for this patient until the physician reviews it.",
  blood="No, in a severe reaction: the circuit blood carries the trigger. A mild type B reaction may continue if the nephrologist agrees.",
  escalate="Emergency transfer for anaphylaxis. The attending nephrologist for every reaction. The receiving team decides on blood tests such as tryptase.",
  restart="Not on the same dialyzer type or sterilization method until the attending nephrologist decides the next session&rsquo;s dialyzer and any precautions.",
  document="Onset time relative to the start, symptoms, drugs given with times, dialyzer model, lot and sterilization method, drugs given in the hour before. Update the allergy record. Report the reaction to the supplier and regulator per policy. <b>Clinical review required:</b> positioning wording and the unit&rsquo;s epinephrine protocol (dose, route, repeat interval) to be confirmed against the unit protocol."),
 learn=["physician-on-duty-16-when-the-circuit-fails.html", "nephrology-nursing-09-hd-session-complication-response.html"],
 refs=["golden2023", "saha", "daug1988", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 8
dict(id="chest-pain", num=8, group="arrest", title="Chest pain during dialysis",
 index="Chest pain",
 when="New chest pain, pressure or heaviness during dialysis, or its equivalents: breathlessness, sweating, a fall in pressure or a new abnormal pulse, with or without pain.",
 steps=[
  ("POD or chair nurse", "<b>Go to the patient:</b> alertness, breathing, color; attach the monitor; pressure, pulse, oxygen saturation.", False),
  ("Chair nurse", "<b>Check the circuit:</b> air, oddly colored blood, or early itching and wheeze point to <a href=\"#air-embolism\">Card 5</a>, <a href=\"#hemolysis\">6</a> or <a href=\"#anaphylaxis\">7</a>.", True),
  ("POD", "<b>Record a 12-lead electrocardiogram (ECG) within 10 minutes</b> and compare it with the last one on file.", False),
  ("Chair nurse", "<b>Start the unit&rsquo;s chest pain protocol,</b> which usually includes stopping ultrafiltration (UF) and oxygen if saturation is low.", False),
  ("Any staff", "<b>Bring the defibrillator to the chair.</b> Call the attending nephrologist for pain with ECG change, low pressure, a new rhythm, breathlessness or fainting.", True),
  ("POD", "<b>Stop per protocol and arrange emergency transfer</b> for ongoing pain, ECG change, low pressure or an unstable rhythm.", False),
 ],
 warn="Not every chest pain in the chair is a fluid-removal problem. Treat it as a heart attack, air, hemolysis or a reaction until the ECG and the circuit check say otherwise.",
 det=dict(
  diff="Acute coronary syndrome, arrhythmia (<a href=\"#arrhythmia\">Card 9</a>), heart muscle strain from low pressure, pericarditis, aortic dissection, pulmonary embolism, air, hemolysis, a type B dialyzer reaction; muscle strain or reflux only after the others are excluded.",
  monitor="Continuous monitor, repeat ECG if pain continues or changes, blood pressure and symptoms. Troponin in kidney failure needs cautious, trend-based interpretation by the receiving team.",
  circuit="Stop UF per protocol. The blood pump keeps running unless a circuit cause is suspected or the treatment is being ended.",
  blood="If the treatment is ended, return the blood per protocol when the circuit is sound, unless air, hemolysis or a severe reaction is suspected.",
  escalate="Where an ECG cannot be obtained or repeated, the chest pain guideline advises referral to an emergency department. Transfer for ongoing pain or ECG change.",
  restart="Only when the pain has settled, the ECG is unchanged, the patient is stable and the attending nephrologist agrees, under close observation.",
  document="Times of pain onset, ECGs and their findings, vital signs, fluid removed, actions and calls."),
 learn=["physician-on-duty-15-heart-emergencies-in-the-chair.html", "nephrology-nursing-09-hd-session-complication-response.html"],
 refs=["gulati", "turakhia", "greenberg", "saha"]),

# ───────────────────────────────────────────────────────────────── 9
dict(id="arrhythmia", num=9, group="arrest", title="Symptomatic arrhythmia",
 index="Fast, slow or irregular pulse",
 when="A new fast, slow or irregular pulse or a monitor rhythm change, with palpitations, dizziness, chest discomfort, breathlessness, low pressure or confusion.",
 steps=[
  ("Any staff", "<b>Check for a pulse.</b> No pulse and not breathing normally: go to <a href=\"#code\">Card 1</a>.", False),
  ("Any staff", "<b>Bring the defibrillator and monitor to the chair before you telephone;</b> attach them.", False),
  ("POD", "<b>Record a 12-lead electrocardiogram (ECG)</b> and judge stability: low pressure, chest pain, breathlessness or reduced alertness means unstable.", False),
  ("POD", "<b>Unstable fast rhythm:</b> follow the advanced cardiac life support (ACLS) tachycardia algorithm; cardioversion only by a trained provider, per protocol.", False),
  ("POD", "<b>Unstable slow rhythm:</b> follow the ACLS bradycardia algorithm per protocol, and treat it as high potassium until proven otherwise (<a href=\"#hyperkalemia\">Card 10</a>).", False),
  ("POD", "<b>Stable:</b> keep the monitor on, check the latest potassium, stop ultrafiltration (UF) per protocol, and call the attending nephrologist. Do not start rhythm drugs from memory.", False),
 ],
 warn="A wide-QRS or very slow rhythm is an emergency even when the patient says they feel fine.",
 det=dict(
  diff="Atrial fibrillation or flutter with a fast rate (common around dialysis and after the long gap), ventricular tachycardia, heart block, high or low potassium (a low-potassium dialysis fluid can push potassium too low), drug effects such as beta-blockers or digoxin, ischemia, low pressure.",
  monitor="Continuous rhythm monitoring; save strips; repeat ECG after any change or treatment; potassium, calcium and magnesium as the physician orders.",
  circuit="Stable: UF stopped per protocol, blood pump running. Unstable: treatment stopped per protocol while the team follows ACLS.",
  blood="Return the blood per protocol if the treatment is ended and the circuit is sound. If high potassium is the cause and the patient is stable, dialysis is the treatment: do not stop it without the attending nephrologist.",
  escalate="Emergency transfer for any unstable rhythm and after any shock. A new stable atrial fibrillation is for the attending nephrologist: blood thinners are not started in the chair today.",
  restart="Only for a stable patient, on the attending nephrologist&rsquo;s order, with the dialysis fluid potassium reviewed.",
  document="Rhythm strips with times, ECG findings, electrolytes, dialysis fluid potassium, drugs and shocks with times, calls."),
 learn=["physician-on-duty-15-heart-emergencies-in-the-chair.html", "physician-on-duty-18-potassium-sugar-and-the-brain.html"],
 refs=["aha9", "turakhia", "montague", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 10
dict(id="hyperkalemia", num=10, group="arrest", title="Suspected severe hyperkalemia",
 index="High potassium",
 when="A high potassium result, or missed sessions or the long gap with weakness, a slow or irregular pulse, or electrocardiogram (ECG) changes (peaked T waves, wide QRS, absent P waves).",
 steps=[
  ("Any staff", "<b>Check for a pulse.</b> No pulse: <a href=\"#code\">Card 1</a>. With a pulse: continue here.", False),
  ("POD", "<b>Attach the monitor; record a 12-lead ECG.</b> Repeat a doubtful (hemolyzed) sample, but never delay treatment for an abnormal ECG.", False),
  ("POD", "<b>Call the attending nephrologist at once</b> for any ECG change, weakness, slow or irregular pulse, or a value above the unit&rsquo;s action threshold; start the order set while you call.", True),
  ("POD", "<b>Protect the heart:</b> intravenous calcium as the unit&rsquo;s order set directs when the ECG shows potassium changes. Calcium does not lower potassium.", False),
  ("POD", "<b>Shift potassium into cells:</b> insulin with glucose, inhaled salbutamol, or both, per the order set. Arrange glucose checks for several hours after insulin.", False),
  ("Chair nurse", "<b>Remove potassium with dialysis.</b> A connected, stable patient stays on the machine; do not stop dialysis without the attending nephrologist.", False),
 ],
 warn="Dialysis is the treatment. Stopping the session in a stable patient removes the only real potassium removal; calcium and insulin only buy time.",
 det=dict(
  diff="A falsely high result from a hemolyzed sample; hemolysis in the circuit (<a href=\"#hemolysis\">Card 6</a>); a slow pulse from drugs. ECG changes are often absent even at high levels, so a normal ECG does not make a high value safe.",
  monitor="Continuous ECG; potassium rechecked when the physician orders, including after dialysis; capillary glucose for several hours after insulin, because hypoglycemia followed in about 13% of treated episodes in one hospital series, at a median of 2 hours.",
  circuit="Keep dialyzing unless the rhythm is unstable or the patient arrests. The dialysis fluid potassium is the physician&rsquo;s decision. A patient not yet connected is connected promptly on the physician&rsquo;s order.",
  blood="Only relevant if the session must end (arrest or unstable rhythm): see <a href=\"#code\">Card 1</a>.",
  escalate="Emergency transfer when dialysis cannot start promptly, ECG changes persist, or the rhythm is unstable. Cardiac arrest from high potassium: <a href=\"#code\">Card 1</a> (guidelines differ on calcium and bicarbonate during arrest; the unit protocol decides).",
  restart="Not applicable: the physician sets the dialysis fluid, duration and recheck after an emergency session.",
  document="Potassium values with times, ECG findings, drugs given as ordered with times, glucose series, dialysis fluid potassium, missed sessions and diet history."),
 learn=["physician-on-duty-18-potassium-sugar-and-the-brain.html", "attending-nephrologist-06-electrolyte-emergencies.html"],
 refs=["clase", "aha10", "mahoney", "montague", "apel"]),

# ───────────────────────────────────────────────────────────────── 11
dict(id="hypoglycemia", num=11, group="deterioration", title="Low blood sugar or sudden confusion",
 index="Low sugar, sudden confusion",
 when="New confusion, drowsiness, sweating, odd behavior, slurred speech or a seizure, above all in a patient taking insulin or a sulfonylurea or who ate little.",
 steps=[
  ("Chair nurse", "<b>Check airway, breathing and circulation.</b> Unresponsive and not breathing normally: <a href=\"#code\">Card 1</a>.", False),
  ("Chair nurse", "<b>Check a capillary glucose now,</b> in every confused, sweaty, drowsy or seizing dialysis patient.", False),
  ("Chair nurse", "<b>Low and able to swallow safely:</b> give fast-acting glucose by mouth as the protocol directs.", False),
  ("Authorized nurse or POD", "<b>Low and not safe to swallow:</b> nothing by mouth; give glucose by the route the protocol names.", False),
  ("Chair nurse", "<b>Recheck the glucose</b> at the protocol&rsquo;s interval and treat again if still low; then food once alert.", False),
  ("Second nurse", "<b>Call the physician on duty (POD).</b> Normal glucose and still confused: think stroke, seizure or drug toxicity (<a href=\"#stroke\">Cards 13</a>, <a href=\"#seizure\">12</a>).", True),
 ],
 warn="A low sugar can look like a stroke, drunkenness or a seizure. Check the glucose before you assume anything else.",
 det=dict(
  diff="Stroke (<a href=\"#stroke\">Card 13</a>), a seizure or the drowsiness after it (<a href=\"#seizure\">Card 12</a>), drug build-up in kidney failure (for example gabapentin, pregabalin, cefepime, acyclovir), low blood pressure, low sodium, uremia, sepsis, low oxygen.",
  monitor="The ADA defines hypoglycemia as glucose below 70 mg/dL, and below 54 mg/dL as clinically significant; treat to the unit&rsquo;s threshold. The ADA recheck interval after treatment is 15 minutes. Glucose falls during dialysis, and insulin and sulfonylureas act longer in kidney failure, so lows can recur hours later; check again before the patient goes home.",
  circuit="Dialysis can usually continue once the glucose is treated and the patient is alert, if the physician agrees. Ask whether your dialysis fluid contains glucose.",
  blood="Only if the session is ended for another reason; then return per protocol when the circuit is sound.",
  escalate="Emergency transfer if the patient does not recover after treatment, or for low sugar from a sulfonylurea, which can last many hours. The attending nephrologist for every severe episode.",
  restart="Continue or resume on the physician&rsquo;s word once the patient is alert and the glucose is above the protocol&rsquo;s target.",
  document="Glucose values with times, treatment and route, response, diabetes medicines and timing, last meal, insulin given for potassium. <b>Clinical review required:</b> the unit&rsquo;s treatment amounts and recheck targets."),
 learn=["physician-on-duty-18-potassium-sugar-and-the-brain.html", "physician-on-duty-22-diabetes-on-dialysis.html", "dialysis-charge-nurse-07-mid-session-surveillance.html"],
 refs=["ada2026", "abe", "apel", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 12
dict(id="seizure", num=12, group="deterioration", title="Seizure during dialysis",
 index="Seizure",
 when="Jerking of the limbs, stiffening, staring with no response, or a sudden fall in consciousness with twitching, during or soon after dialysis.",
 steps=[
  ("Chair nurse", "<b>Protect the patient and the access:</b> guard the head, hold the needle arm steady, move hard objects away. Nothing in the mouth.", False),
  ("Second nurse", "<b>Time the seizure.</b> Call for help and the physician on duty (POD).", True),
  ("Chair nurse", "<b>Stop the blood pump and clamp the lines</b> per protocol, so a needle cannot pull out.", False),
  ("Chair nurse", "<b>When the jerking stops, turn the patient on the side;</b> airway and oxygen per protocol.", False),
  ("Second nurse", "<b>Check a capillary glucose</b> and treat a low value (<a href=\"#hypoglycemia\">Card 11</a>).", False),
  ("POD", "<b>Seizure over 5 minutes, or repeated without recovery:</b> status epilepticus. Give only the antiseizure drug the protocol names, and arrange emergency transfer.", False),
 ],
 warn="Give only the antiseizure drug your unit&rsquo;s protocol names, by the person it authorizes. Doses differ in kidney failure.",
 det=dict(
  diff="Low sugar, dialysis disequilibrium in early sessions with a very high urea, low sodium, calcium or magnesium, very high blood pressure, stroke or bleeding in the head (heparin), drug toxicity (for example cefepime), low oxygen or low pressure from an arrhythmia, epilepsy. Do not assume disequilibrium explains every seizure.",
  monitor="Breathing, oxygen saturation, blood pressure, glucose, recovery of consciousness, any new one-sided weakness. Seizures in kidney failure can be nonconvulsive and look like drowsy confusion.",
  circuit="Blood pump stopped and lines clamped to protect the access. After the seizure, check both needle sites for bleeding or displacement.",
  blood="Decide with the nurse: return the blood per protocol if the circuit is sound and the patient is safe; do not return it if air or hemolysis is suspected.",
  escalate="The attending nephrologist for every seizure. Emergency transfer for status epilepticus, a first seizure, a focal deficit, head injury, or confusion that does not clear once glucose and pressure are corrected.",
  restart="Not the same session unless the attending nephrologist decides. If disequilibrium is suspected, the next prescription (shorter, gentler sessions) is the physician&rsquo;s decision.",
  document="Start and end times, what was seen, glucose, vital signs, drugs given with times, injuries, needle sites, urea and session number if new to dialysis."),
 learn=["physician-on-duty-18-potassium-sugar-and-the-brain.html", "physician-on-duty-12-first-sessions-and-unusual-sessions.html"],
 refs=["glauser2016", "titoff", "greenberg", "saha"]),

# ───────────────────────────────────────────────────────────────── 13
dict(id="stroke", num=13, group="deterioration", title="New weakness, facial droop or speech change: suspected stroke",
 index="Suspected stroke",
 when="Sudden facial droop, arm or leg weakness, slurred or absent speech, eyes turned to one side, loss of vision or balance, or a sudden severe headache.",
 steps=[
  ("Chair nurse", "<b>Note the last-known-well time:</b> when the patient was last seen at their usual state, not when you found them.", False),
  ("Chair nurse", "<b>Check airway, breathing and circulation;</b> give oxygen only per protocol.", False),
  ("Second nurse", "<b>Check a capillary glucose:</b> a low sugar can mimic a stroke.", True),
  ("POD", "<b>Do a face, arm and speech check</b> and record the findings and the time.", False),
  ("Chair nurse", "<b>End dialysis per protocol;</b> return the blood if the circuit is sound. Nothing by mouth.", False),
  ("POD", "<b>Call the attending nephrologist and arrange emergency transfer to a stroke-capable hospital now.</b> Do not wait for the session to finish.", False),
 ],
 warn="The stroke clock starts at the last-known-well time. Record it, and the time and amount of the last heparin, before the patient leaves.",
 det=dict(
  diff="Low sugar (<a href=\"#hypoglycemia\">Card 11</a>), weakness after a seizure, bleeding in the head (heparin), very high blood pressure, disequilibrium, drug toxicity.",
  monitor="Repeat neurologic checks and blood pressure until handover. Blood pressure targets and any treatment are decided by the stroke team, not lowered quickly in the chair.",
  circuit="Treatment ended per protocol. Keep the access arm free: no blood pressure cuff or drip on the fistula arm.",
  blood="Yes, per protocol, when the circuit is sound and no air, hemolysis or severe reaction is suspected.",
  escalate="Emergency transfer. The stroke team decides eligibility for clot-dissolving or clot-retrieval treatment. Hand over: last-known-well time, deficit time, heparin amount and time, other blood thinners, glucose, blood pressures, fluid removed, last potassium, and which arm holds the access.",
  restart="No restart that day. Further dialysis is planned with the receiving team.",
  document="Last-known-well time, findings with times, glucose, heparin and blood thinner record, transfer time and destination, calls made."),
 learn=["physician-on-duty-18-potassium-sugar-and-the-brain.html"],
 refs=["prabhakaran", "seliger", "greenberg"]),

# ───────────────────────────────────────────────────────────────── 14
dict(id="fever-rigors", num=14, group="infection", title="Fever, rigors or suspected sepsis during dialysis",
 index="Fever, rigors, sepsis",
 when="Shaking chills or fever during dialysis, often with a catheter, with or without low pressure, confusion or fast breathing. Chills in two or more patients: see the warning.",
 steps=[
  ("Chair nurse", "<b>Check airway, breathing, blood pressure and alertness.</b> Stop ultrafiltration (UF) if the pressure is low.", False),
  ("Charge nurse", "<b>Look around the floor:</b> is anyone else shivering?", True),
  ("Chair nurse", "<b>Inspect the catheter exit site or the access</b> for redness, pus or tenderness.", False),
  ("Chair nurse", "<b>Draw blood cultures before the first antibiotic,</b> from the sites your protocol names (usually catheter hub and circuit); protect arm veins.", False),
  ("POD", "<b>Call the attending nephrologist;</b> give the first antibiotic as ordered without delay, within the hour if the patient looks septic.", False),
  ("POD", "<b>Low pressure, confusion or fast breathing:</b> end the treatment per protocol and prepare emergency transfer.", False),
 ],
 warn="<b>Two or more patients with chills on one shift: possible cluster.</b> Say it aloud. Charge nurse: stop treatments per the cluster protocol (symptomatic first), hold new starts. Technician: check water and dialysis fluid; keep samples and lot numbers. Call the Medical Director. Do not return blood until the attending advises.",
 det=dict(
  diff="Catheter-related bloodstream infection, a pyrogenic reaction from contaminated water or fluid (blood cultures usually negative, often several patients), access infection, pneumonia or other infections, endocarditis, a transfusion or drug reaction, an overheated dialysis fluid.",
  monitor="Temperature, blood pressure, mentation, breathing rate and lactate if available. Screen for sepsis and repeat.",
  circuit="Unstable: end the treatment per protocol. Stable: the attending nephrologist decides whether to continue, which allows circuit cultures and the first antibiotic dose, or to end early. Whether to use the catheter is the physician&rsquo;s decision.",
  blood="Yes, per protocol, in an isolated infection with a sound circuit. No if hemolysis, air or a severe reaction is suspected, or the circuit has clotted. In a suspected cluster, clamp and ask the attending nephrologist first.",
  escalate="The attending nephrologist at once; the Medical Director for any cluster; emergency transfer for septic shock, altered mentation or failing oxygenation.",
  restart="On the physician&rsquo;s order. A cluster: no new starts on the affected machines or water loop until they are cleared.",
  document="Onset time and pattern, vital signs over time, other patients checked, exit site and access findings, culture sites and times, antibiotic and time, lactate, calls; machine number and dialyzer lot in a suspected cluster. Incident report for clusters."),
 learn=["physician-on-duty-17-fever-and-bloodstream-infection.html", "physician-on-duty-06-water-and-dialysate.html", "nephrology-nursing-07-hd-vascular-access-infection-prevention.html", "attending-nephrologist-16-vascular-access-infection.html"],
 refs=["prescott", "lok", "mermel", "quittnat", "kantor", "saha"]),
]

GROUPS = [("arrest", "Arrest, rhythm and the heart"), ("circuit", "Circuit and access"),
          ("deterioration", "The patient changes"), ("infection", "Infection")]
FIXED_INDEX = [  # the two original cards, in the same index
    dict(id="code", num=1, group="arrest", index="Code during hemodialysis"),
    dict(id="leak", num=2, group="circuit", index="Blood leak alarm"),
]
