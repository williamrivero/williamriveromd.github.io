# Emergency Quick Cards: Expansion Review Packet

Renal Care Academy · https://renalcarematters.com/academy/emergency-cards
Prepared November 27, 2026 · For clinical review by the Medical Director / attending nephrologist

**Status at a glance.** Cards 1 and 2 are live and were published on November 27, 2026, with no clinical sign-off recorded yet. Cards 3 to 14 are live on the page as clearly marked **DRAFTS**. A white "DRAFT · Clinical review required" badge sits in each card header and a dashed "draft" tag on the card index, so the status is shown in text and not by color alone. A card becomes "reviewed" only when a reviewer and date are entered in `REVIEW` in `tools/academy/emergency_cards_data.py`. The badge then changes to "Clinically reviewed by … , date".

---

## 1. Topic map

| # | Card (anchor) | Group | Overlaps and how they are kept apart | Academy lessons linked ("Learn it") |
|---|---|---|---|---|
| 1 | Code during hemodialysis (`#code`) | Arrest | Every other card hands off to it when there is no pulse; it links out to 4, 5, 7 and 10 | Charge Nurse 12, Physician-on-Duty 15, Nephrology Nursing 9 |
| 2 | Blood leak alarm (`#leak`) | Circuit | Hemolysis is shown as a separate red step that links to card 6 | Physician-on-Duty 16, Dialysis Technician 9, Biomedical Technician 7 |
| 3 | Severe low blood pressure or collapse (`#hypotension`) | Patient changes | Warning box sends bleeding, rhythm, chest pain, sepsis, reaction, air and hemolysis to their own cards | Physician-on-Duty 13, Nephrology Nursing 9, Charge Nurse 7 |
| 4 | Venous needle dislodgement or access bleeding (`#access-bleeding`) | Circuit | Arterial needle and air go to card 5; low pressure from other causes goes to card 3 | Physician-on-Duty 16 and 19, Head Nurse 4, Nurse Assistant 7 |
| 5 | Suspected air embolism (`#air-embolism`) | Circuit | No pulse goes to card 1 | Physician-on-Duty 16, Dialysis Technician 10, Biomedical Technician 7 |
| 6 | Suspected hemolysis (`#hemolysis`) | Circuit | The warning sets it apart from card 2; potassium goes to card 10; a cluster uses the card 14 branch logic | Physician-on-Duty 16 and 6, Charge Nurse 11 |
| 7 | Severe dialyzer reaction or anaphylaxis (`#anaphylaxis`) | Circuit | A type B reaction, hypotension, air and hemolysis are listed as differentials | Physician-on-Duty 16, Nephrology Nursing 9 |
| 8 | Chest pain during dialysis (`#chest-pain`) | Arrest and heart | The circuit check sends air, hemolysis and reaction to cards 5, 6 and 7; rhythm goes to card 9 | Physician-on-Duty 15, Nephrology Nursing 9 |
| 9 | Symptomatic arrhythmia (`#arrhythmia`) | Arrest and heart | No pulse goes to card 1; a slow or wide rhythm goes to card 10 | Physician-on-Duty 15 and 18 |
| 10 | Suspected severe hyperkalemia (`#hyperkalemia`) | Arrest and heart | Pulse and no pulse are split at step 1; arrest goes to card 1 | Physician-on-Duty 18, Attending Nephrologist 6 |
| 11 | Low blood sugar or sudden confusion (`#hypoglycemia`) | Patient changes | A normal glucose sends the reader to cards 12 and 13 | Physician-on-Duty 18 and 22, Charge Nurse 7 |
| 12 | Seizure during dialysis (`#seizure`) | Patient changes | Glucose goes to card 11; disequilibrium is listed but explicitly not assumed | Physician-on-Duty 18 and 12 |
| 13 | New weakness, facial droop or speech change: suspected stroke (`#stroke`) | Patient changes | Glucose-mimic check links card 11 | Physician-on-Duty 18 |
| 14 | Fever, rigors or suspected sepsis (`#fever-rigors`) | Infection | The cluster branch is in the warning box; hemolysis is a do-not-return condition | Physician-on-Duty 17 and 6, Nephrology Nursing 7, Attending Nephrologist 16 |

**Module link boxes.** The red "Emergency quick cards" box now appears in 26 module pages, before each module's skills checklist or self-assessment. Each box points to the cards that module teaches. The full list is in `MODULE_LINKS` in `tools/academy/apply_emergency_cards.py`.

---

## 2. The twelve draft cards (3 to 14)

The live page is the authoritative rendering. The text below is generated from the same data file (`tools/academy/emergency_cards_data.py`) so a reviewer can mark it up on paper.

### Card 3. Severe low blood pressure or collapse on dialysis  (`#hypotension`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Pressure falls during dialysis with yawning, cramps, nausea, dizziness or sweating, or the patient becomes faint. Unresponsive and not breathing normally: Card 1.

1. *Chair nurse*: **Lay the chair flat, legs raised,** as far as breathing allows; turn to the side if vomiting.
2. *Chair nurse*: **Stop ultrafiltration (UF).** Keep the blood pump running unless you suspect air, hemolysis, a severe reaction or blood loss.
3. *At the same time, Second nurse*: **Check pulse, pressure, oxygen saturation and alertness.** Lift the blanket: look at the access and lines.
4. *Chair nurse*: **Give saline through the circuit** per protocol if the pressure does not recover.
5. *Second nurse*: **Call the physician on duty (POD) and the attending nephrologist** if the pressure stays low, falls again or needs more fluid; at once for chest pain, breathlessness, confusion, fever, bleeding or an abnormal pulse.
6. *At the same time, Charge nurse*: **Assign a watcher** for the other patients while two staff are at this chair.

> **Critical:** Collapse is not always the fluid removal. Chest pain, a new irregular pulse, fever, blood under the blanket, or early itching and wheeze point to another card: check before giving more fluid.

- **Think of these too.** Bleeding from a dislodged needle or the gut (Card 4), arrhythmia (Card 9), acute coronary syndrome (Card 8), sepsis (Card 14), dialyzer reaction or anaphylaxis (Card 7), air (Card 5), hemolysis (Card 6), low blood sugar (Card 11).
- **Reassess and monitor.** Repeat blood pressure, pulse and symptoms after each step, at the interval your protocol sets, until the patient is stable and the POD agrees. The legs-up position rests on expert opinion only, and a breathless patient may not tolerate lying flat.
- **Circuit and access.** Stopping UF stops fluid removal; blood keeps flowing through the dialyzer. The blood pump is stopped only for a circuit cause (air, hemolysis, severe reaction, blood loss). Changes to the UF goal, session time or dialysis fluid are the physician’s decision.
- **Return the blood?.** If the session is ended because the pressure will not recover, return the blood per protocol when the circuit is sound. Do not return it when air, hemolysis or a severe reaction is suspected, or through a clotted circuit.
- **Escalation and transfer.** Emergency transfer when the pressure does not recover after the protocol’s steps, when consciousness stays altered, or when a dangerous cause is likely. The attending nephrologist decides whether to end the session.
- **Restart.** UF resumes only when symptoms settle and the pressure recovers, at the goal and rate the physician sets. Repeated episodes call for a review of the dry weight and prescription, not a habit of giving saline.
- **Document and follow up.** Times, blood pressure series, fluid removed and when UF stopped, fluid given, symptoms, who was called and when, and the outcome. File an incident report for a collapse or a transfer.

**Learn it:** Physician-on-Duty 13, Nephrology Nursing 9, Charge Nurse 7  
**Sources:** EBPG 2007 (Kooman), Reeves & Mc Causland 2018, Kanbay 2020, KDIGO 2020 (Flythe), Greenberg & Choi 2021

### Card 4. Venous needle dislodgement or access bleeding  (`#access-bleeding`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Blood on the bed, chair or floor; a wet dressing or blanket over the access; a needle out or a line apart; or a patient who turns pale, sweaty or drowsy for no clear reason.

1. *Any staff*: **Lift the blanket.** Look at both needle sites and both line connections.
2. *Chair nurse*: **Stop the blood pump.** Clamp the line on both sides of the break.
3. *Chair nurse*: **Press firmly on the site** with gloved hands and gauze, and keep pressing.
4. *At the same time, Second nurse*: **Lay the patient flat.** Check consciousness, pulse and blood pressure. Give oxygen per protocol.
5. *Second nurse*: **Call for help and the emergency cart** if pale, sweaty, drowsy or hypotensive; call the physician on duty (POD) and the attending nephrologist.
6. *Charge nurse*: **Estimate the loss** (bed, chair, blanket, floor) and assign a watcher for the other patients.

> **Critical:** The venous pressure alarm can stay silent when the needle comes out: a quiet machine proves nothing. Keep the access and connections in view all session. Never reinsert a dislodged needle or reconnect a line end that has been open.

- **Think of these too.** Arterial needle out (air may be drawn in: see Card 5), infiltration or hematoma, gastrointestinal bleeding, low blood pressure from other causes (Card 3).
- **Reassess and monitor.** Serial blood pressure, pulse and consciousness. Watch the site after pressure for rebleeding or swelling. Blood tests and fluids are the physician’s decision.
- **Circuit and access.** Blood pump stopped and the line clamped on both sides of the break, so the circuit stays closed. A new needle at a new site is placed only on the physician’s decision, with a sterile needle.
- **Return the blood?.** Blood on the floor is lost. Published reviews give no rule for the blood still in the circuit after a dislodgement, so the unit protocol and the attending nephrologist decide. Blood is never returned through a line end that has been open.
- **Escalation and transfer.** The attending nephrologist for every event. Emergency transfer for shock, ongoing bleeding or a large loss. Fluids and transfusion are decided by the physician.
- **Restart.** Only after bleeding is controlled, the patient is stable and a new needle is placed, on the attending nephrologist’s order. The heparin plan is reviewed before any restart.
- **Document and follow up.** Time found, estimated loss, vital signs over time, actions, who was called. Incident report. Review taping, access visibility and alarm limits; European renal nurses published 12 consensus practice points.

**Learn it:** Physician-on-Duty 16, Physician-on-Duty 19, Head Nurse 4, Nurse Assistant 7  
**Sources:** Saha & Allon 2017, Van Waeleghem 2008, Ribitsch 2014, Frinak 2023, Greenberg & Choi 2021

### Card 5. Suspected air embolism  (`#air-embolism`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Air or foam in the venous line or below the venous chamber, or an air detector alarm, with or without a sudden cough, chest tightness, breathlessness, confusion or collapse.

1. *Chair nurse*: **Stop the blood pump and clamp the venous line.** Never open the clamp or override the air detector.
2. *Chair nurse*: **Do not return the blood.** Rinse-back would push more air into the patient.
3. *At the same time, Second nurse*: **Position the patient per the unit’s protocol:** lying on the left side is the dialysis teaching. Never sit the patient up.
4. *Second nurse*: **Give oxygen** per protocol. Check consciousness, breathing, pulse and oxygen saturation.
5. *Charge nurse*: **Call for help and the emergency cart;** call the physician on duty (POD) and the attending nephrologist; arrange emergency transfer.
6. *Any staff*: **Start CPR flat on the back** if there is no pulse and no normal breathing: go to Card 1.

> **Critical:** Air on the patient side of the detector is an emergency even if the patient feels well at first. Keep the clamp closed until the source is found and a physician decides.

- **Think of these too.** A false air alarm in a well patient (line not seated in the detector, tiny bubbles): the nurse finds the cause before anything is restarted. Also pulmonary embolism, heart attack, anaphylaxis.
- **Reassess and monitor.** Consciousness and focal signs (air can reach the brain in a seated patient), oxygen saturation, blood pressure, heart rhythm.
- **Circuit and access.** Blood pump stopped and venous line clamped. Look for the entry point: a loose connection before the pump, an empty saline bag, an open catheter limb, a cracked line. Keep the circuit for inspection; the machine is held until the biomedical technician checks the air detector and clamp.
- **Return the blood?.** No. The blood in the circuit is not returned.
- **Escalation and transfer.** Emergency transfer for any symptomatic patient. The receiving hospital decides further treatment. **Clinical review required:** sources differ on position. Dialysis texts and reviews teach lying on the left side, some with the head down, and a 2021 review cautions that head-down may worsen brain swelling when air has reached the brain. The AHA 2025 special-circumstances guideline considers lying flat on the back or the recovery position reasonable for gas embolism. No trial compares positions; the unit should choose one.
- **Restart.** No restart on that machine until the cause is found and the detector passes its test. Any further dialysis is the attending nephrologist’s decision.
- **Document and follow up.** Time, what was seen, alarm history, estimated amount of air, entry point, machine number, line and dialyzer lot numbers, actions and calls. Incident report and biomedical check.

**Learn it:** Physician-on-Duty 16, Dialysis Technician 10, Biomedical Technician 7  
**Sources:** Saha & Allon 2017, Greenberg & Choi 2021, AHA 2025 Part 10, Handbook of Dialysis 2015

### Card 6. Suspected hemolysis  (`#hemolysis`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Blood in the venous line looks translucent, cherry-red or “port-wine,” or a sample shows pink plasma, often with chest, back or belly pain, nausea and a rising blood pressure. Several patients may be affected.

1. *Chair nurse*: **Stop the blood pump and clamp the lines.**
2. *Chair nurse*: **Do not return the blood.** It carries potassium released from broken red cells.
3. *At the same time, Second nurse*: **Check airway, breathing and circulation;** give oxygen per protocol; attach the monitor.
4. *POD*: **Order urgent potassium and hemoglobin** and the unit’s hemolysis tests; call the attending nephrologist. Treat high potassium with Card 10.
5. *At the same time, Charge nurse*: **Check every patient on the same water and concentrate supply.** Two or more affected: declare a possible cluster, hold new starts, call the Medical Director.
6. *Technician*: **Keep the lines, dialyzer, packaging and lot numbers,** and take samples of water and dialysis fluid.

> **Critical:** Hemolysis is not a blood leak. A blood leak alarm finds blood in the used dialysis fluid (Card 2); hemolysis shows abnormal blood in the blood lines. With hemolysis, the blood is never returned.

- **Think of these too.** Blood leak (Card 2), very dark blood of a clotting circuit, acute coronary syndrome or aortic dissection when chest or back pain is the main sign.
- **Reassess and monitor.** Continuous ECG (electrocardiogram) for potassium effects, repeat potassium and hemoglobin as the physician orders, and belly pain.
- **Circuit and access.** Blood pump stopped, lines clamped, treatment ended. The machine and the water loop are held until the technician checks dialysis fluid temperature and conductivity and the water for chlorine and chloramine. Kinked or faulty blood tubing has caused outbreaks.
- **Return the blood?.** Never.
- **Escalation and transfer.** The attending nephrologist at once; the Medical Director for any suspected water or dialysis fluid fault or cluster. Emergency transfer for a high potassium, ECG change or unstable patient.
- **Restart.** Not until the cause is found and the water and dialysis fluid are confirmed safe, on a different machine if needed, on the physician’s order.
- **Document and follow up.** Time, blood color, symptoms, machine number, dialyzer and tubing lot numbers, water and fluid test results, other patients checked. Incident report; device faults reported to the supplier and regulator per policy.

**Learn it:** Physician-on-Duty 16, Physician-on-Duty 6, Charge Nurse 11  
**Sources:** Saha & Allon 2017, Duffy 2000, Tipple 1991, Greenberg & Choi 2021

### Card 7. Severe dialyzer reaction or anaphylaxis  (`#anaphylaxis`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Within the first minutes of treatment, or soon after a drug, any of: itching, hives, flushing, throat tightness, hoarseness, wheeze, breathlessness, swelling of the face or lips, low blood pressure or collapse.

1. *Chair nurse*: **Stop the blood pump and clamp the lines.** Do not return the blood.
2. *At the same time, Charge nurse*: **Call for help and the emergency cart;** start the unit’s anaphylaxis protocol.
3. *Authorized nurse or POD*: **Give intramuscular epinephrine (adrenaline) into the outer thigh** as the protocol directs. It is the first-line treatment; do not wait for antihistamines or steroids.
4. *At the same time, Second nurse*: **Protect the airway; give oxygen;** position per protocol (flat with legs raised unless breathing is hard); attach the monitor.
5. *Second nurse*: **Call the physician on duty (POD) and the attending nephrologist;** arrange emergency transfer.
6. *Technician*: **Keep the dialyzer and its packaging;** record the model, lot number and sterilization method.

> **Critical:** When anaphylaxis is possible, treat it now. Epinephrine comes first; antihistamines and steroids do not replace it.

- **Think of these too.** A milder, later (type B) reaction with chest or back pain, diagnosed only after cardiac, embolic and hemolytic causes are excluded; low blood pressure from fluid removal (Card 3); air (Card 5); hemolysis (Card 6). Drugs given during dialysis, such as intravenous iron, antibiotics or heparin, can also cause anaphylaxis.
- **Reassess and monitor.** Airway, breathing, blood pressure and oxygen saturation until handover; further epinephrine doses at the protocol’s interval if symptoms persist; watch for symptoms returning.
- **Circuit and access.** Blood pump stopped, lines clamped, treatment ended. That dialyzer type is not used again for this patient until the physician reviews it.
- **Return the blood?.** No, in a severe reaction: the circuit blood carries the trigger. A mild type B reaction may continue if the nephrologist agrees.
- **Escalation and transfer.** Emergency transfer for anaphylaxis. The attending nephrologist for every reaction. The receiving team decides on blood tests such as tryptase.
- **Restart.** Not on the same dialyzer type or sterilization method until the attending nephrologist decides the next session’s dialyzer and any precautions.
- **Document and follow up.** Onset time relative to the start, symptoms, drugs given with times, dialyzer model, lot and sterilization method, drugs given in the hour before. Update the allergy record. Report the reaction to the supplier and regulator per policy. **Clinical review required:** positioning wording and the unit’s epinephrine protocol (dose, route, repeat interval) to be confirmed against the unit protocol.

**Learn it:** Physician-on-Duty 16, Nephrology Nursing 9  
**Sources:** Anaphylaxis practice parameter 2023, Saha & Allon 2017, Daugirdas & Ing 1988, Greenberg & Choi 2021

### Card 8. Chest pain during dialysis  (`#chest-pain`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** New chest pain, pressure or heaviness during dialysis, or its equivalents: breathlessness, sweating, a fall in pressure or a new abnormal pulse, with or without pain.

1. *POD or chair nurse*: **Go to the patient:** alertness, breathing, color; attach the monitor; pressure, pulse, oxygen saturation.
2. *At the same time, Chair nurse*: **Check the circuit:** air, oddly colored blood, or early itching and wheeze point to Card 5, 6 or 7.
3. *POD*: **Record a 12-lead electrocardiogram (ECG) within 10 minutes** and compare it with the last one on file.
4. *Chair nurse*: **Start the unit’s chest pain protocol,** which usually includes stopping ultrafiltration (UF) and oxygen if saturation is low.
5. *At the same time, Any staff*: **Bring the defibrillator to the chair.** Call the attending nephrologist for pain with ECG change, low pressure, a new rhythm, breathlessness or fainting.
6. *POD*: **Stop per protocol and arrange emergency transfer** for ongoing pain, ECG change, low pressure or an unstable rhythm.

> **Critical:** Not every chest pain in the chair is a fluid-removal problem. Treat it as a heart attack, air, hemolysis or a reaction until the ECG and the circuit check say otherwise.

- **Think of these too.** Acute coronary syndrome, arrhythmia (Card 9), heart muscle strain from low pressure, pericarditis, aortic dissection, pulmonary embolism, air, hemolysis, a type B dialyzer reaction; muscle strain or reflux only after the others are excluded.
- **Reassess and monitor.** Continuous monitor, repeat ECG if pain continues or changes, blood pressure and symptoms. Troponin in kidney failure needs cautious, trend-based interpretation by the receiving team.
- **Circuit and access.** Stop UF per protocol. The blood pump keeps running unless a circuit cause is suspected or the treatment is being ended.
- **Return the blood?.** If the treatment is ended, return the blood per protocol when the circuit is sound, unless air, hemolysis or a severe reaction is suspected.
- **Escalation and transfer.** Where an ECG cannot be obtained or repeated, the chest pain guideline advises referral to an emergency department. Transfer for ongoing pain or ECG change.
- **Restart.** Only when the pain has settled, the ECG is unchanged, the patient is stable and the attending nephrologist agrees, under close observation.
- **Document and follow up.** Times of pain onset, ECGs and their findings, vital signs, fluid removed, actions and calls.

**Learn it:** Physician-on-Duty 15, Nephrology Nursing 9  
**Sources:** AHA/ACC chest pain 2021, KDIGO 2018 (Turakhia), Greenberg & Choi 2021, Saha & Allon 2017

### Card 9. Symptomatic arrhythmia  (`#arrhythmia`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** A new fast, slow or irregular pulse or a monitor rhythm change, with palpitations, dizziness, chest discomfort, breathlessness, low pressure or confusion.

1. *Any staff*: **Check for a pulse.** No pulse and not breathing normally: go to Card 1.
2. *Any staff*: **Bring the defibrillator and monitor to the chair before you telephone;** attach them.
3. *POD*: **Record a 12-lead electrocardiogram (ECG)** and judge stability: low pressure, chest pain, breathlessness or reduced alertness means unstable.
4. *POD*: **Unstable fast rhythm:** follow the advanced cardiac life support (ACLS) tachycardia algorithm; cardioversion only by a trained provider, per protocol.
5. *POD*: **Unstable slow rhythm:** follow the ACLS bradycardia algorithm per protocol, and treat it as high potassium until proven otherwise (Card 10).
6. *POD*: **Stable:** keep the monitor on, check the latest potassium, stop ultrafiltration (UF) per protocol, and call the attending nephrologist. Do not start rhythm drugs from memory.

> **Critical:** A wide-QRS or very slow rhythm is an emergency even when the patient says they feel fine.

- **Think of these too.** Atrial fibrillation or flutter with a fast rate (common around dialysis and after the long gap), ventricular tachycardia, heart block, high or low potassium (a low-potassium dialysis fluid can push potassium too low), drug effects such as beta-blockers or digoxin, ischemia, low pressure.
- **Reassess and monitor.** Continuous rhythm monitoring; save strips; repeat ECG after any change or treatment; potassium, calcium and magnesium as the physician orders.
- **Circuit and access.** Stable: UF stopped per protocol, blood pump running. Unstable: treatment stopped per protocol while the team follows ACLS.
- **Return the blood?.** Return the blood per protocol if the treatment is ended and the circuit is sound. If high potassium is the cause and the patient is stable, dialysis is the treatment: do not stop it without the attending nephrologist.
- **Escalation and transfer.** Emergency transfer for any unstable rhythm and after any shock. A new stable atrial fibrillation is for the attending nephrologist: blood thinners are not started in the chair today.
- **Restart.** Only for a stable patient, on the attending nephrologist’s order, with the dialysis fluid potassium reviewed.
- **Document and follow up.** Rhythm strips with times, ECG findings, electrolytes, dialysis fluid potassium, drugs and shocks with times, calls.

**Learn it:** Physician-on-Duty 15, Physician-on-Duty 18  
**Sources:** AHA 2025 Part 9, KDIGO 2018 (Turakhia), Montague 2008, Greenberg & Choi 2021

### Card 10. Suspected severe hyperkalemia  (`#hyperkalemia`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** A high potassium result, or missed sessions or the long gap with weakness, a slow or irregular pulse, or electrocardiogram (ECG) changes (peaked T waves, wide QRS, absent P waves).

1. *Any staff*: **Check for a pulse.** No pulse: Card 1. With a pulse: continue here.
2. *POD*: **Attach the monitor; record a 12-lead ECG.** Repeat a doubtful (hemolyzed) sample, but never delay treatment for an abnormal ECG.
3. *At the same time, POD*: **Call the attending nephrologist at once** for any ECG change, weakness, slow or irregular pulse, or a value above the unit’s action threshold; start the order set while you call.
4. *POD*: **Protect the heart:** intravenous calcium as the unit’s order set directs when the ECG shows potassium changes. Calcium does not lower potassium.
5. *POD*: **Shift potassium into cells:** insulin with glucose, inhaled salbutamol, or both, per the order set. Arrange glucose checks for several hours after insulin.
6. *Chair nurse*: **Remove potassium with dialysis.** A connected, stable patient stays on the machine; do not stop dialysis without the attending nephrologist.

> **Critical:** Dialysis is the treatment. Stopping the session in a stable patient removes the only real potassium removal; calcium and insulin only buy time.

- **Think of these too.** A falsely high result from a hemolyzed sample; hemolysis in the circuit (Card 6); a slow pulse from drugs. ECG changes are often absent even at high levels, so a normal ECG does not make a high value safe.
- **Reassess and monitor.** Continuous ECG; potassium rechecked when the physician orders, including after dialysis; capillary glucose for several hours after insulin, because hypoglycemia followed in about 13% of treated episodes in one hospital series, at a median of 2 hours.
- **Circuit and access.** Keep dialyzing unless the rhythm is unstable or the patient arrests. The dialysis fluid potassium is the physician’s decision. A patient not yet connected is connected promptly on the physician’s order.
- **Return the blood?.** Only relevant if the session must end (arrest or unstable rhythm): see Card 1.
- **Escalation and transfer.** Emergency transfer when dialysis cannot start promptly, ECG changes persist, or the rhythm is unstable. Cardiac arrest from high potassium: Card 1 (guidelines differ on calcium and bicarbonate during arrest; the unit protocol decides).
- **Restart.** Not applicable: the physician sets the dialysis fluid, duration and recheck after an emergency session.
- **Document and follow up.** Potassium values with times, ECG findings, drugs given as ordered with times, glucose series, dialysis fluid potassium, missed sessions and diet history.

**Learn it:** Physician-on-Duty 18, Attending Nephrologist 6  
**Sources:** KDIGO 2020 (Clase), AHA 2025 Part 10, Cochrane 2005 (Mahoney), Montague 2008, Apel 2014

### Card 11. Low blood sugar or sudden confusion  (`#hypoglycemia`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** New confusion, drowsiness, sweating, odd behavior, slurred speech or a seizure, above all in a patient taking insulin or a sulfonylurea or who ate little.

1. *Chair nurse*: **Check airway, breathing and circulation.** Unresponsive and not breathing normally: Card 1.
2. *Chair nurse*: **Check a capillary glucose now,** in every confused, sweaty, drowsy or seizing dialysis patient.
3. *Chair nurse*: **Low and able to swallow safely:** give fast-acting glucose by mouth as the protocol directs.
4. *Authorized nurse or POD*: **Low and not safe to swallow:** nothing by mouth; give glucose by the route the protocol names.
5. *Chair nurse*: **Recheck the glucose** at the protocol’s interval and treat again if still low; then food once alert.
6. *At the same time, Second nurse*: **Call the physician on duty (POD).** Normal glucose and still confused: think stroke, seizure or drug toxicity (Cards 13, 12).

> **Critical:** A low sugar can look like a stroke, drunkenness or a seizure. Check the glucose before you assume anything else.

- **Think of these too.** Stroke (Card 13), a seizure or the drowsiness after it (Card 12), drug build-up in kidney failure (for example gabapentin, pregabalin, cefepime, acyclovir), low blood pressure, low sodium, uremia, sepsis, low oxygen.
- **Reassess and monitor.** The ADA defines hypoglycemia as glucose below 70 mg/dL, and below 54 mg/dL as clinically significant; treat to the unit’s threshold. The ADA recheck interval after treatment is 15 minutes. Glucose falls during dialysis, and insulin and sulfonylureas act longer in kidney failure, so lows can recur hours later; check again before the patient goes home.
- **Circuit and access.** Dialysis can usually continue once the glucose is treated and the patient is alert, if the physician agrees. Ask whether your dialysis fluid contains glucose.
- **Return the blood?.** Only if the session is ended for another reason; then return per protocol when the circuit is sound.
- **Escalation and transfer.** Emergency transfer if the patient does not recover after treatment, or for low sugar from a sulfonylurea, which can last many hours. The attending nephrologist for every severe episode.
- **Restart.** Continue or resume on the physician’s word once the patient is alert and the glucose is above the protocol’s target.
- **Document and follow up.** Glucose values with times, treatment and route, response, diabetes medicines and timing, last meal, insulin given for potassium. **Clinical review required:** the unit’s treatment amounts and recheck targets.

**Learn it:** Physician-on-Duty 18, Physician-on-Duty 22, Charge Nurse 7  
**Sources:** ADA Standards 2026, Section 6, Abe & Kalantar-Zadeh 2015, Apel 2014, Greenberg & Choi 2021

### Card 12. Seizure during dialysis  (`#seizure`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Jerking of the limbs, stiffening, staring with no response, or a sudden fall in consciousness with twitching, during or soon after dialysis.

1. *Chair nurse*: **Protect the patient and the access:** guard the head, hold the needle arm steady, move hard objects away. Nothing in the mouth.
2. *At the same time, Second nurse*: **Time the seizure.** Call for help and the physician on duty (POD).
3. *Chair nurse*: **Stop the blood pump and clamp the lines** per protocol, so a needle cannot pull out.
4. *Chair nurse*: **When the jerking stops, turn the patient on the side;** airway and oxygen per protocol.
5. *Second nurse*: **Check a capillary glucose** and treat a low value (Card 11).
6. *POD*: **Seizure over 5 minutes, or repeated without recovery:** status epilepticus. Give only the antiseizure drug the protocol names, and arrange emergency transfer.

> **Critical:** Give only the antiseizure drug your unit’s protocol names, by the person it authorizes. Doses differ in kidney failure.

- **Think of these too.** Low sugar, dialysis disequilibrium in early sessions with a very high urea, low sodium, calcium or magnesium, very high blood pressure, stroke or bleeding in the head (heparin), drug toxicity (for example cefepime), low oxygen or low pressure from an arrhythmia, epilepsy. Do not assume disequilibrium explains every seizure.
- **Reassess and monitor.** Breathing, oxygen saturation, blood pressure, glucose, recovery of consciousness, any new one-sided weakness. Seizures in kidney failure can be nonconvulsive and look like drowsy confusion.
- **Circuit and access.** Blood pump stopped and lines clamped to protect the access. After the seizure, check both needle sites for bleeding or displacement.
- **Return the blood?.** Decide with the nurse: return the blood per protocol if the circuit is sound and the patient is safe; do not return it if air or hemolysis is suspected.
- **Escalation and transfer.** The attending nephrologist for every seizure. Emergency transfer for status epilepticus, a first seizure, a focal deficit, head injury, or confusion that does not clear once glucose and pressure are corrected.
- **Restart.** Not the same session unless the attending nephrologist decides. If disequilibrium is suspected, the next prescription (shorter, gentler sessions) is the physician’s decision.
- **Document and follow up.** Start and end times, what was seen, glucose, vital signs, drugs given with times, injuries, needle sites, urea and session number if new to dialysis.

**Learn it:** Physician-on-Duty 18, Physician-on-Duty 12  
**Sources:** AES status epilepticus 2016, Títoff 2019, Greenberg & Choi 2021, Saha & Allon 2017

### Card 13. New weakness, facial droop or speech change: suspected stroke  (`#stroke`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Sudden facial droop, arm or leg weakness, slurred or absent speech, eyes turned to one side, loss of vision or balance, or a sudden severe headache.

1. *Chair nurse*: **Note the last-known-well time:** when the patient was last seen at their usual state, not when you found them.
2. *Chair nurse*: **Check airway, breathing and circulation;** give oxygen only per protocol.
3. *At the same time, Second nurse*: **Check a capillary glucose:** a low sugar can mimic a stroke.
4. *POD*: **Do a face, arm and speech check** and record the findings and the time.
5. *Chair nurse*: **End dialysis per protocol;** return the blood if the circuit is sound. Nothing by mouth.
6. *POD*: **Call the attending nephrologist and arrange emergency transfer to a stroke-capable hospital now.** Do not wait for the session to finish.

> **Critical:** The stroke clock starts at the last-known-well time. Record it, and the time and amount of the last heparin, before the patient leaves.

- **Think of these too.** Low sugar (Card 11), weakness after a seizure, bleeding in the head (heparin), very high blood pressure, disequilibrium, drug toxicity.
- **Reassess and monitor.** Repeat neurologic checks and blood pressure until handover. Blood pressure targets and any treatment are decided by the stroke team, not lowered quickly in the chair.
- **Circuit and access.** Treatment ended per protocol. Keep the access arm free: no blood pressure cuff or drip on the fistula arm.
- **Return the blood?.** Yes, per protocol, when the circuit is sound and no air, hemolysis or severe reaction is suspected.
- **Escalation and transfer.** Emergency transfer. The stroke team decides eligibility for clot-dissolving or clot-retrieval treatment. Hand over: last-known-well time, deficit time, heparin amount and time, other blood thinners, glucose, blood pressures, fluid removed, last potassium, and which arm holds the access.
- **Restart.** No restart that day. Further dialysis is planned with the receiving team.
- **Document and follow up.** Last-known-well time, findings with times, glucose, heparin and blood thinner record, transfer time and destination, calls made.

**Learn it:** Physician-on-Duty 18  
**Sources:** AHA/ASA stroke 2026, Seliger 2003, Greenberg & Choi 2021

### Card 14. Fever, rigors or suspected sepsis during dialysis  (`#fever-rigors`)

**Status:** DRAFT, clinical review required. **Sources checked:** November 27, 2026.

**Recognize:** Shaking chills or fever during dialysis, often with a catheter, with or without low pressure, confusion or fast breathing. Chills in two or more patients: see the warning.

1. *Chair nurse*: **Check airway, breathing, blood pressure and alertness.** Stop ultrafiltration (UF) if the pressure is low.
2. *At the same time, Charge nurse*: **Look around the floor:** is anyone else shivering?
3. *Chair nurse*: **Inspect the catheter exit site or the access** for redness, pus or tenderness.
4. *Chair nurse*: **Draw blood cultures before the first antibiotic,** from the sites your protocol names (usually catheter hub and circuit); protect arm veins.
5. *POD*: **Call the attending nephrologist;** give the first antibiotic as ordered without delay, within the hour if the patient looks septic.
6. *POD*: **Low pressure, confusion or fast breathing:** end the treatment per protocol and prepare emergency transfer.

> **Critical:** **Two or more patients with chills on one shift: possible cluster.** Say it aloud. Charge nurse: stop treatments per the cluster protocol (symptomatic first), hold new starts. Technician: check water and dialysis fluid; keep samples and lot numbers. Call the Medical Director. Do not return blood until the attending advises.

- **Think of these too.** Catheter-related bloodstream infection, a pyrogenic reaction from contaminated water or fluid (blood cultures usually negative, often several patients), access infection, pneumonia or other infections, endocarditis, a transfusion or drug reaction, an overheated dialysis fluid.
- **Reassess and monitor.** Temperature, blood pressure, mentation, breathing rate and lactate if available. Screen for sepsis and repeat.
- **Circuit and access.** Unstable: end the treatment per protocol. Stable: the attending nephrologist decides whether to continue, which allows circuit cultures and the first antibiotic dose, or to end early. Whether to use the catheter is the physician’s decision.
- **Return the blood?.** Yes, per protocol, in an isolated infection with a sound circuit. No if hemolysis, air or a severe reaction is suspected, or the circuit has clotted. In a suspected cluster, clamp and ask the attending nephrologist first.
- **Escalation and transfer.** The attending nephrologist at once; the Medical Director for any cluster; emergency transfer for septic shock, altered mentation or failing oxygenation.
- **Restart.** On the physician’s order. A cluster: no new starts on the affected machines or water loop until they are cleared.
- **Document and follow up.** Onset time and pattern, vital signs over time, other patients checked, exit site and access findings, culture sites and times, antibiotic and time, lactate, calls; machine number and dialyzer lot in a suspected cluster. Incident report for clusters.

**Learn it:** Physician-on-Duty 17, Physician-on-Duty 6, Nephrology Nursing 7, Attending Nephrologist 16  
**Sources:** Surviving Sepsis 2026, KDOQI vascular access 2019, IDSA 2009 (Mermel), Quittnat Pelletier 2016, Kantor 1983, Saha & Allon 2017

---

## 3. Second release: six card briefs (not built)

Each brief follows the same structure as cards 3 to 14. None of these are on the live page yet.

**15. Acute breathlessness or pulmonary edema** (`#breathless`)
- *Recognize:* new or worse breathlessness, unable to lie flat, frothy sputum, falling oxygen saturation, crackles; before, during or after a session.
- *Core actions:* sit the patient up (not flat), give oxygen per protocol, monitor, record a 12-lead ECG. The attending nephrologist decides on urgent fluid removal; diuretics rarely help when there is little urine. Transfer if oxygenation fails.
- *Keep distinct from:* card 3 (low pressure; there the patient lies flat), card 7 (wheeze from anaphylaxis), card 8 (chest pain), card 5 (sudden breathlessness with air).
- *Learn it:* Physician-on-Duty 14; the site guide on dialysis codes has a rebound pulmonary congestion section.
- *Sources to confirm:* Greenberg & Choi 2021; KDIGO 2020 (Flythe) on volume.

**16. Persistent bleeding after needle removal** (`#needle-site-bleeding`)
- *Recognize:* the needle site still bleeds after the usual hold time, or rebleeds after the patient leaves the chair.
- *Core actions:* firm two-finger pressure over the site with gauze, without occluding the access; keep holding for the unit's time; check the thrill or bruit afterward; check pressure and pulse. Escalate prolonged bleeding (heparin dose, platelet problems, outflow stenosis). Never let the patient leave while it is still bleeding.
- *Keep distinct from:* card 4 (needle out during treatment). Card 4 is about the circuit; card 16 is after the treatment.
- *Learn it:* Physician-on-Duty 19, Head Nurse 4.
- *Sources to confirm:* KDOQI vascular access 2019; Kidney Care UK patient guidance, already cited in Physician-on-Duty 19.

**17. Dialysis catheter disconnection or damage** (`#catheter`)
- *Recognize:* an open catheter limb or cap, a cracked hub or limb, the catheter partly pulled out, or bleeding at the exit site.
- *Core actions:* clamp the catheter above the damage at once (air risk); lay the patient flat or left side if air is suspected (card 5); cover with sterile gauze; do not push a partly pulled-out catheter back in; call the attending nephrologist. Do not use the catheter until it is assessed.
- *Keep distinct from:* card 5 (air embolism, which is a consequence), card 14 (catheter infection).
- *Learn it:* Physician-on-Duty 10, Nephrology Nursing 7.
- *Sources to confirm:* KDOQI vascular access 2019; Saha & Allon 2017.

**18. Suspected dialysis disequilibrium syndrome** (`#disequilibrium`)
- *Recognize:* headache, nausea, restlessness, confusion, blurred vision or seizure during or soon after an early session, especially with a very high urea.
- *Core actions:* reduce or stop the session per the physician; check glucose and blood pressure; seizure goes to card 12; transfer if consciousness falls. The prevention prescription for the next session (shorter, gentler) is the physician's decision.
- *Keep distinct from:* cards 11, 12 and 13. Disequilibrium is a diagnosis of exclusion, and the card must say so.
- *Learn it:* Physician-on-Duty 12.
- *Sources to confirm:* Greenberg & Choi 2021. The PubMed reviews found so far (Zepeda-Orozco 2012; Raina 2022) are pediatric, so an adult source is still needed: **clinical review required**.

**19. Suspected water or dialysate contamination affecting several patients** (`#cluster`)
- *Recognize:* two or more patients with chills, fever, hemolysis, nausea or hypotension on one shift, or a water-room alarm or failed test.
- *Core actions:* say "possible cluster" aloud; stop treatments per the cluster protocol, symptomatic patients first; hold new starts; keep water, dialysate, lines and dialyzers with lot numbers; call the Medical Director; check chlorine/chloramine and conductivity; decide blood return per patient (never when hemolysis is possible).
- *Keep distinct from:* cards 6 and 14, which handle one patient; this card handles the unit.
- *Learn it:* Physician-on-Duty 6 and 16, Charge Nurse 11, Water Treatment Technician 12.
- *Sources to confirm:* Tipple 1991; Kantor 1983; Duffy 2000; Saha & Allon 2017; DOH AO 2013-0003 water limits (the unit's reference).

**20. Power failure or machine failure with blood in the circuit** (`#power-failure`)
- *Recognize:* machines go dark or alarm together, or one machine fails mid-treatment.
- *Core actions:* stay at the chair; check each patient; on battery, follow the machine's battery steps; with no power, return the blood by hand crank per the manufacturer's instructions and the unit procedure, or clamp; do not leave a patient connected to a stopped circuit longer than the unit procedure allows; the charge nurse assigns staff chair by chair.
- *Keep distinct from:* card 19 (water). A water-system failure may stop all machines.
- *Learn it:* Physician-on-Duty 30, Charge Nurse 13.
- *Manufacturer instructions required:* the hand-crank method, battery duration and clot-time limits vary by machine model. **Clinical and biomedical review required.** Nothing on this card will be invented.

---

## 4. Evidence matrix

"Verified" means the citation (authors, year, journal, volume, pages, DOI) was confirmed on PubMed. "Section" names the part of the source the claim rests on. Where a claim was checked against the Academy module that already cites the source, rather than against the full guideline text, it says so. Those full-text section checks are listed under "Clinical review required."

| Card | Claim | Source (section) | Basis | Status |
|---|---|---|---|---|
| 1 | Epinephrine 1 mg IV every 3–5 min; amiodarone 300 mg then 150 mg for refractory VF/pVT | AHA 2025 Part 9 (cardiac arrest algorithm, drug therapy) | Guideline; matches site guide | Kept on card 1 |
| 1 | Calcium and bicarbonate in hyperkalemic arrest | ERC 2021 (hyperkalemia; dialysis unit) vs AHA 2025 Part 10 (hyperkalemia) | **Conflict:** ERC recommends; AHA calls effectiveness in arrest uncertain | Doses **removed** from card 1; card states the conflict and defers to protocol |
| 1 | Staff-started CPR and AED use in dialysis clinics | Hofacker 2020 (results) | Registry | Verified |
| 2 | Do not rinse back a confirmed leak by habit; practice differs | Physician-on-Duty 16 citing Handbook of Dialysis | Custom, not trial evidence | Stated as custom on card |
| 3 | Flat, legs up; stop UF; saline if no recovery | EBPG 2007 (Kooman); Reeves 2018; Kanbay 2020 | Expert opinion (legs-up), low-level evidence (stop UF) | Stated as opinion on card |
| 3 | Stop the blood pump only for a circuit cause | Physician-on-Duty 13 (first two moves) | Academy module | Verified against module |
| 4 | Venous pressure alarm may not detect dislodgement | Ribitsch 2014 (29% of fistulas vs 94% of grafts); Frinak 2023; Saha & Allon 2017 | Observational and simulation | Verified |
| 4 | No published rule on returning circuit blood after dislodgement | Physician-on-Duty 16 | Gap in evidence | Unit decision |
| 4 | Never reinsert a dislodged needle; never reconnect an open line end | Physician-on-Duty 16 | Infection-control principle | Verified against module |
| 4 | 12 consensus practice points | Van Waeleghem 2008 | Expert consensus | Verified |
| 5 | Stop pump, clamp venous line, do not return blood | Saha & Allon 2017; Greenberg & Choi 2021 | Review | Verified |
| 5 | Position: left side (dialysis texts) vs supine or recovery (AHA 2025 Part 10, gas embolism) | Handbook of Dialysis; AHA 2025 Part 10 | **Conflict** | **Clinical review required**: unit chooses |
| 6 | Do not return blood (released potassium); keep circuit; check others on the same supply | Saha & Allon 2017; Duffy 2000; Tipple 1991 | Review and outbreak reports | Verified |
| 7 | IM epinephrine first-line; antihistamines and steroids do not replace it | Golden 2023 practice parameter (treatment of anaphylaxis) | Guideline | Citation verified; **full-text section check pending** |
| 7 | Severe reaction: do not return blood; type B may continue if nephrologist agrees | Saha & Allon 2017; Daugirdas & Ing 1988 | Review, classic definition | Verified |
| 7 | Positioning wording (flat, legs up unless breathing is hard) | Golden 2023 | — | **Clinical review required** |
| 8 | 12-lead ECG within 10 minutes; refer if an ECG cannot be obtained | AHA/ACC chest pain guideline 2021 (Gulati), initial evaluation | Guideline | Verified against Physician-on-Duty 15 |
| 8 | Troponin interpretation in kidney failure needs caution | KDIGO 2018 (Turakhia) | Guideline/consensus | Verified |
| 9 | ACLS tachycardia and bradycardia algorithms; cardioversion by a trained provider | AHA 2025 Part 9 (tachycardia, bradycardia) | Guideline | Citation verified; **full-text section check pending** |
| 9 | New AF: no anticoagulation started in the chair | Physician-on-Duty 15; KDIGO 2018 (Turakhia) | Academy module | Verified against module |
| 10 | Calcium stabilizes; insulin with glucose and salbutamol shift; dialysis removes | KDIGO 2020 (Clase); Cochrane 2005 (Mahoney) | Consensus; systematic review | Verified |
| 10 | ECG changes often absent at high potassium | Montague 2008 | Observational | Verified |
| 10 | About 13% hypoglycemia after insulin, median 2 h | Apel 2014 | Observational | Verified |
| 10 | Stable patient stays on dialysis | Physician-on-Duty 18 (stop dialysis? row) | Academy module | Verified against module |
| 11 | Hypoglycemia below 70 mg/dL (level 1), below 54 mg/dL (level 2); recheck 15 min after treatment | ADA Standards 2026, Section 6 | Guideline | Citation verified; **full-text wording check pending** |
| 11 | Glucose falls during dialysis; insulin and sulfonylureas act longer | Abe & Kalantar-Zadeh 2015 | Review | Verified |
| 12 | Seizure over 5 minutes = status epilepticus | AES 2016 (Glauser) | Guideline | Verified |
| 12 | Antiseizure drug only as protocol names; doses differ in kidney failure | Títoff 2019; Physician-on-Duty 18 | Review | Verified |
| 13 | Last-known-well time; glucose check; transfer to a stroke-capable hospital | AHA/ASA 2026 stroke guideline (Prabhakaran), prehospital and emergency evaluation | Guideline | Citation verified; **full-text section check pending** |
| 13 | Higher stroke risk on dialysis | Seliger 2003 | Cohort | Verified |
| 14 | Blood cultures before antibiotics | Surviving Sepsis 2026 (strong recommendation); KDOQI 2019 (statement 25.1); IDSA 2009 | Guideline | Verified against Physician-on-Duty 17 |
| 14 | Circuit and catheter-hub culture sites | Quittnat Pelletier 2016; KDOQI 2019 | Diagnostic study; guideline | Verified |
| 14 | Antibiotic "within the hour if the patient looks septic" | Surviving Sepsis 2026 | Guideline; wording follows Physician-on-Duty 17 | **Clinical review required:** confirm the 2026 timing wording |
| 14 | Pyrogenic reaction clusters with negative cultures | Kantor 1983 | Outbreak report | Verified |

**Doses.** No drug dose appears on cards 3 to 14. Drugs are named with "per the unit's protocol / order set." The only doses on the page are epinephrine and amiodarone on card 1, which are standard AHA 2025 adult cardiac arrest doses. The calcium, insulin and dextrose doses that were on card 1 were removed because they lacked repeat limits and monitoring details and conflict between AHA and ERC.

---

## 5. Decisions needing the unit's input

1. **Air embolism position**: left side (dialysis teaching) or supine/recovery (AHA 2025). Pick one for the card and the unit protocol.
2. **Blood return after a needle dislodgement**: the published reviews give no rule.
3. **Blood return after a confirmed blood leak**: whether the leak size changes the answer, and who decides.
4. **Hypotension protocol**: saline portion, blood pressure trigger, recheck interval, and when UF resumes.
5. **Anaphylaxis protocol**: epinephrine dose, route, repeat interval, and who may give it; positioning wording.
6. **Hyperkalemia order set**: action threshold; calcium salt and amount; insulin amount (a lower insulin dose has been associated with less hypoglycemia); salbutamol; glucose check schedule; calcium and bicarbonate during arrest.
7. **Hypoglycemia**: treatment threshold, oral glucose amount, IV route, and who may give it.
8. **Seizure**: the named antiseizure drug and who is authorized to give it.
9. **Fever**: culture sites, the empiric antibiotic order set, and who owns the cluster protocol.
10. **Stroke**: the designated stroke-capable hospital and transfer route for each unit.
11. **Card 1 doses**: confirm removing the hyperkalemia doses from card 1.
12. **Pediatric link**: Pediatric Dialysis Nurse Module 15 currently links to the adult code card. Keep it with an "adult card" note, or remove it.
13. **Sign-off process**: who signs off each card, and how often cards are re-checked (suggested: at each guideline update, and at least yearly).

---

## 6. Implementation (repository changes)

- `tools/academy/emergency_cards_data.py` (new): card text, review status (`REVIEW`), short source labels, lesson labels, groups.
- `data/academy-emergency-cards-refs.json` (new): 35 APA 7 references, all PubMed-verified. Most were reused from the Academy modules. Golden 2023, ADA 2026 Section 6 and Glauser 2016 were added after checking them on PubMed.
- `tools/academy/apply_emergency_cards.py`:
  - renders cards 3 to 14 from the data;
  - adds a card index of 14 links in four groups, each with a draft tag;
  - adds a "Circuit words used on every card" glossary;
  - adds a status line and Sources line to every card;
  - removes the doses from card 1's hyperkalemia line and states the AHA/ERC conflict;
  - expands the module link boxes from 12 to 26 modules;
  - updates the landing callout;
  - adds print rules: each card starts a page, steps never split, details and the glossary open, light colors even when printed from Dark mode.
- The anchors `#code` and `#leak` and the Save and Print buttons are unchanged.
- `tools/academy/build_schola.py`: **fixes a bug the offline test exposed.** The Schola worker answered every non-page request from the saved cache first. That included the downloads made by Schola's own "Update" and by the cards' "Update saved copy." An update therefore re-saved the old file under the new version tag, and saved copies never actually updated. Requests made with `cache: 'no-cache'`, `'reload'` or `'no-store'` now go to the network first and fall back to the saved copy. This affects every Schola track update, not just the cards.

---

## 7. Validation report

Tested on November 27, 2026 with Chromium (Playwright), against a local server that serves extensionless URLs like Cloudflare does.

| Check | Result |
|---|---|
| Page renders, no script errors (Light, Dim, Dark; phone 390×844 and desktop 1280×900) | Pass |
| 14 cards present; `#code` and `#leak` unchanged | Pass |
| Links in the page body (185, 105 unique): every `#anchor` resolves, every lesson file exists | Pass (0 broken); the build also refuses to run if a lesson or reference key is missing |
| External DOI links | 34 present; not fetched (sandbox has no general internet access) |
| Accessibility (axe-core 4, WCAG 2 A/AA rules) on `main`, Light and Dark | Pass after two contrast fixes (links inside card headers; reference links in Dark) |
| Danger shown by text, not color alone | "Critical" label, "DRAFT" text badge, "draft" tag in the index |
| Without JavaScript | All 14 cards, 86 steps, 12 warnings present; details open with native disclosure |
| Phone fit (390×844, opened by its link so the card starts below the header) | The numbered steps of all 14 cards end within the first screen. The warning box also fits for cards 1, 2, 5, 11 and 12; for the other nine it needs a scroll of about 10–110 px (most: card 3, 111 px; card 10, 109 px) |
| Desktop fit (1280×900) | Every card's core actions fit |
| Print (A4, from Light and from Dark) | 30 pages: each card starts a page, details open, sources and status printed, light background; spot-checked visually |
| Save for offline use → go offline → open `/academy/emergency-cards#seizure` | Pass: page served from the saved copy, all 14 cards present |
| Update saved copy after the page changes | **Failed before the worker fix** (stale copy re-saved); **passes after it** |
| Page in Schola's shared list (saved with any track) | Confirmed in `schola-offline.json`; a full track download was not run end to end |

**Not tested:**
- real iPhone or iPad Safari, and the Home Screen app;
- real Android Chrome;
- screen readers (VoiceOver, TalkBack);
- printing on a physical printer;
- the live Cloudflare deployment and its caching;
- a full Schola "Download all" run.

## References

The full APA list is printed at the end of the live page and kept in `data/academy-emergency-cards-refs.json`. Every in-card "Sources" label links to its entry.
