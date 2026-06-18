# Resuscitation Algorithm Figures — 2025 AHA (Prompt Pack)

Clinical-algorithm flowcharts for the williamriveromd.com visual atlas + the
Code Blue / ACLS-in-the-dialysis-unit guide. Content verified against the
**2025 AHA Guidelines for CPR & ECC (released Oct 22, 2025)** and, for the
dialysis-specific figure, ERC Special Circumstances + AJKD Hemodialysis
Emergencies (see "Accuracy flags" at the end).

> **Style = "Clinical Algorithm" archetype, NOT the Mechanism style.**
> These are decision flowcharts, so they get a `2D` render badge in the atlas
> (flat flowchart), not the purple `Mechanism` badge.

**Shared style (applies to every prompt):**
Clean 2D clinical decision flowchart on a **white background**. Rounded
rectangular action boxes, **diamond decision nodes** (yes/no branches clearly
labeled), thin navy (#0f1e2e) connector arrows, strong top-to-bottom flow, no
spaghetti lines. Restrained palette: navy text/borders, teal (#1a6b72) headers,
amber (#b8860b) caution, clinical red (#b91c1c) for shock/emergency steps, renal
green (#1f7a4d) for "go/route" steps. Bold condensed sans-serif title, short
high-legibility labels, generous whitespace, mobile-readable. A small "dose box"
panel where noted. **No 3D, no photorealism, no icons-as-clutter.** Do **not**
render any organization branding, logos, journal names, or guideline-body
acronyms (no "AHA", "American Heart Association", "©AHA", "2025 Guidelines"
text). Bottom-right corner: small semi-transparent navy **"© williamriveromd.com"**,
not obscuring content. 4:3 or portrait (tall algorithms) as noted.

**Destination & suggested filenames** (atlas section "Resuscitation &
emergencies" + Code Blue guide; ids assigned at wiring time):
| # | Figure | File | Ratio |
|---|--------|------|-------|
| 1 | Adult BLS / CPR + AED | `acls-adult-bls-aed-algorithm` | portrait |
| 2 | Adult Cardiac Arrest (ACLS) | `acls-adult-cardiac-arrest-algorithm` | portrait |
| 3 | Adult Bradycardia | `acls-adult-bradycardia-algorithm` | portrait |
| 4 | Adult Tachycardia | `acls-adult-tachycardia-algorithm` | portrait |
| 5 | Adult Post-Cardiac-Arrest | `acls-adult-post-rosc-algorithm` | 4:3 |
| 6 | Pediatric BLS (PBLS) | `pals-pediatric-bls-algorithm` | portrait |
| 7 | PALS Cardiac Arrest | `pals-cardiac-arrest-algorithm` | portrait |
| 8 | PALS Bradycardia | `pals-bradycardia-algorithm` | portrait |
| 9 | PALS Tachycardia | `pals-tachycardia-algorithm` | portrait |
| 10 | PALS Post-Cardiac-Arrest | `pals-post-rosc-algorithm` | 4:3 |
| 11 | Dialysis-Unit Code Blue | `dialysis-code-blue-acls-algorithm` | portrait |
| 12 | Difficult / Failed Intubation | `airway-difficult-failed-intubation-algorithm` | portrait |

---

## 1. Adult BLS / High-Quality CPR + AED

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamond
decision nodes, navy connectors, restrained navy/teal/amber/red/green palette,
bold sans-serif, mobile-readable, no 3D, no org branding/logos/acronyms.
Bottom-right: small semi-transparent navy "© williamriveromd.com". Portrait.

TITLE: "Adult BLS — High-Quality CPR & AED (Healthcare Provider)"

TOP-TO-BOTTOM FLOW:
1. Box: "Verify scene safety."
2. Box: "Check responsiveness (tap & shout). Shout for help / activate
   emergency response; get AED + emergency equipment."
3. Box: "Assess breathing AND pulse simultaneously — no more than 10 seconds."
4. Decision diamond: "Normal breathing? Definite pulse?"
   - Branch "Breathing + pulse" → Box (green): "Monitor until help arrives."
   - Branch "No normal breathing, pulse PRESENT" → Box (amber): "Rescue breaths:
     1 breath every 6 sec (~10/min). Check pulse every 2 min. Suspected opioid:
     give naloxone."
   - Branch "No breathing/gasping AND no pulse" → Box (red): "CARDIAC ARREST —
     START CPR."
5. Box: "High-quality CPR (C-A-B): start compressions."
6. DOSE/QUALITY PANEL (side): "Rate 100-120/min · Depth ≥2 in (5 cm), not >2.4 in
   · Full recoil · Ratio 30:2 (1 or 2 rescuers, adult) · With advanced airway:
   continuous compressions + 1 breath/6 sec · Compression fraction ≥60% ·
   minimize pauses (<10 sec)."
7. Box: "Apply AED as soon as it arrives. Power on, attach pads (upper-right
   sternum + lower-left apex), clear & analyze."
8. Decision diamond: "Shockable rhythm / shock advised?"
   - YES → Box (red): "Deliver 1 shock → immediately resume CPR ~2 min."
   - NO → Box: "Resume CPR ~2 min (pads on)."
9. Loop arrow: "Re-analyze every 2 min; switch compressors."
```

---

## 2. Adult Cardiac Arrest (ACLS)

```
Clean 2D clinical decision flowchart, white background, two-column shockable vs
non-shockable layout, rounded boxes + diamonds, navy connectors, navy/teal/amber/
red palette, bold sans-serif, mobile-readable, no 3D, no org branding/acronyms.
Bottom-right: small semi-transparent navy "© williamriveromd.com". Portrait.

TITLE: "Adult Cardiac Arrest Algorithm"

TOP:
- Box (red): "Start CPR — give oxygen, attach monitor/defibrillator."
- Decision diamond: "Rhythm shockable?"  → splits into two columns.

LEFT COLUMN — SHOCKABLE (VF / pulseless VT):
- "Shock" → "CPR 2 min; obtain IV access (IV preferred over IO); treat causes."
- "Rhythm check → shockable? → Shock (#2)"
- "CPR 2 min. Epinephrine 1 mg after the 2nd shock, then every 3-5 min.
   Consider advanced airway + waveform capnography."
- "Rhythm check → shockable? → Shock (#3)"
- "CPR 2 min. Amiodarone 300 mg (then 150 mg) OR lidocaine 1-1.5 mg/kg
   (then 0.5-0.75 mg/kg) for refractory VF/pVT."
- Loop: "Continue 2-min cycles."

RIGHT COLUMN — NON-SHOCKABLE (Asystole / PEA):
- "CPR 2 min; obtain IV access (IV preferred over IO)."
- "Epinephrine 1 mg ASAP, then every 3-5 min. Consider advanced airway +
   capnography."
- "Rhythm check every 2 min → if shockable, cross to left column."

BOTTOM SHARED:
- Diamond: "ROSC?" → green box: "Post-Cardiac-Arrest Care."
- DOSE PANEL: "Epinephrine 1 mg IV every 3-5 min · Amiodarone 300→150 mg ·
   Lidocaine 1-1.5→0.5-0.75 mg/kg · Defibrillation: biphasic = manufacturer
   dose (or max if unknown); monophasic 360 J · CPR cycle 2 min · PETCO2 <10
   mmHg = improve compressions; abrupt rise = ROSC."
- REVERSIBLE CAUSES box (H's & T's): "Hypovolemia · Hypoxia · Hydrogen ion
   (acidosis) · Hypo-/Hyperkalemia · Hypothermia · Tension pneumothorax ·
   Tamponade · Toxins · Thrombosis (pulmonary) · Thrombosis (coronary)."
```

---

## 3. Adult Bradycardia (with a Pulse)

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Adult Bradycardia With a Pulse"

FLOW:
1. Box: "Bradyarrhythmia (typically HR <50/min) with symptoms. Identify & treat
   underlying cause."
2. Box: "Maintain airway, assist breathing; oxygen if hypoxemic; monitor rhythm,
   BP, oximetry; IV access; 12-lead ECG (don't delay therapy)."
3. Decision diamond: "Persistent bradyarrhythmia causing hypotension, acutely
   altered mental status, signs of shock, ischemic chest discomfort, or acute
   heart failure?"
   - NO → green box: "Monitor and observe."
   - YES → treatment ladder:
4. Box: "Atropine 1 mg IV bolus; repeat every 3-5 min; max total 3 mg."
5. Box (if atropine ineffective): "Transcutaneous pacing AND/OR Dopamine
   infusion 5-20 mcg/kg/min AND/OR Epinephrine infusion 2-10 mcg/min."
6. Box: "Consider expert consultation; transvenous pacing."

DOSE PANEL: "Atropine 1 mg q3-5 min (max 3 mg) · Dopamine 5-20 mcg/kg/min ·
Epinephrine 2-10 mcg/min."
```

---

## 4. Adult Tachycardia (with a Pulse)

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Adult Tachycardia With a Pulse"

FLOW:
1. Box: "Tachyarrhythmia (usually HR ≥150/min). Identify & treat underlying
   cause. Airway/oxygen; monitor rhythm, BP, oximetry; IV; 12-lead ECG."
2. Decision diamond #1: "Persistent tachyarrhythmia causing hypotension, acutely
   altered mental status, signs of shock, ischemic chest discomfort, or acute
   heart failure?"
   - YES (UNSTABLE) → red box: "Synchronized cardioversion (consider sedation).
     If regular narrow-complex, consider adenosine first — do not delay
     cardioversion."
   - NO (STABLE) → "12-lead ECG; assess QRS width" → Decision diamond #2.
3. Decision diamond #2: "Wide QRS ≥0.12 sec?"
   - YES (WIDE) → box: "Adenosine only if regular & monomorphic; consider
     antiarrhythmic infusion; expert consultation."
   - NO (NARROW) → box: "Vagal maneuvers; adenosine (if regular); beta-blocker
     or calcium-channel blocker; expert consultation."

DOSE PANEL: "Synchronized cardioversion: use device-specific recommended energy;
if unknown, use maximum energy. · Adenosine 6 mg rapid IV push → 12 mg if needed.
· Stable wide-QRS antiarrhythmics: Procainamide 20-50 mg/min (max 17 mg/kg) then
1-4 mg/min; Amiodarone 150 mg over 10 min then 1 mg/min; Sotalol 100 mg
(1.5 mg/kg) over 5 min (avoid if prolonged QT)."
NOTE on figure: do NOT print fixed joule values for cardioversion (2025 uses
device-specific / max energy).
```

---

## 5. Adult Post-Cardiac-Arrest (Post-ROSC) Care

```
Clean 2D clinical flowchart + targets panel, white background, rounded boxes +
diamonds, navy connectors, navy/teal/amber/green palette, bold sans-serif,
mobile-readable, no 3D, no org branding/acronyms. Bottom-right: small
semi-transparent navy "© williamriveromd.com". 4:3.

TITLE: "Adult Post-Cardiac-Arrest Care (after ROSC)"

FLOW:
1. Box: "Manage airway; early advanced airway + waveform capnography."
2. Box: "Oxygenation: 100% O2 until stable, then titrate SpO2 90-98%
   (PaO2 60-105 mmHg). Avoid hypoxemia AND hyperoxia."
3. Box: "Ventilation: start ~10 breaths/min; target normocapnia PaCO2
   35-45 mmHg. Avoid hyperventilation."
4. Box: "Hemodynamics: treat hypotension; target MAP ≥65 mmHg with fluids +
   vasopressors."
5. Box: "Obtain 12-lead ECG."
6. Decision diamond: "STEMI or unstable cardiogenic shock / suspected cardiac
   cause?"
   - YES → red box: "Emergent coronary angiography / PCI."
   - NO → box: "Admit ICU; critical-care management."
7. Decision diamond: "Follows commands?"
   - YES → box: "Other critical care; monitor."
   - NO (comatose) → box: "Temperature control + continuous EEG / seizure
     monitoring + delayed multimodal neuroprognostication."

TARGETS PANEL: "SpO2 90-98% · PaCO2 35-45 mmHg · MAP ≥65 mmHg · Temperature
control: choose one target 32-37.5°C, actively prevent fever (≥24 h) · Glucose
140-180 mg/dL · Neuroprognostication: multimodal, delayed (exam, EEG, imaging,
biomarkers NSE/NfL at ~72 h); never one test alone · Treat reversible causes."
```

---

## 6. Pediatric Basic Life Support (PBLS)

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red/green palette, bold sans-serif,
mobile-readable, no 3D, no org branding/acronyms. Bottom-right: small
semi-transparent navy "© williamriveromd.com". Portrait.

TITLE: "Pediatric BLS — Infant & Child"

FLOW:
1. Box: "Verify scene safety. Check responsiveness; shout for help / activate
   emergency response; get AED + equipment."
2. Box: "Assess breathing AND pulse ≤10 sec. Pulse: infant = brachial; child =
   carotid or femoral."
3. Decision diamond: "Normal breathing? Pulse present?"
   - "Breathing + pulse" → green: "Monitor until help arrives."
   - "Not breathing, pulse present" → amber: "Rescue breaths 1 every 2-3 sec
     (~20-30/min). Recheck pulse every 2 min."
   - "No pulse, OR HR <60/min with poor perfusion" → red: "START CPR."
4. Box: "High-quality CPR. Ratio 30:2 single rescuer / 15:2 with ≥2 rescuers.
   Rate 100-120/min. Depth ≥1/3 AP diameter (~1.5 in/4 cm infant; ~2 in/5 cm
   child). Full recoil."
5. Box (technique, amber): "Infant compressions: two-thumb encircling-hands
   (preferred) OR one-hand heel technique. (Two-finger technique no longer
   recommended.)"
6. Decision diamond: "Single rescuer?"
   - "Witnessed sudden collapse" → "Activate EMS + get AED first, then CPR."
   - "Unwitnessed/asphyxial" → "~2 min CPR first, then activate EMS/get AED."
   - "≥2 rescuers" → "One does CPR (15:2) while other activates EMS + gets AED."
7. Box: "AED as soon as available. Child <8 y / infant: use pediatric dose
   attenuator + pads if available (manual defibrillator preferred for infants);
   if only AED without attenuator, use it. Resume CPR immediately after shock."
```

---

## 7. PALS Cardiac Arrest

```
Clean 2D clinical decision flowchart, white background, two-column shockable vs
non-shockable layout, rounded boxes + diamonds, navy connectors,
navy/teal/amber/red palette, bold sans-serif, mobile-readable, no 3D, no org
branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Pediatric Cardiac Arrest Algorithm"

TOP:
- Box (red): "Start CPR (15:2 with 2 rescuers); give oxygen; attach
  monitor/defibrillator."
- Decision diamond: "Rhythm shockable?" → two columns.

LEFT — SHOCKABLE (VF / pulseless VT):
- "Shock 2 J/kg → CPR 2 min; obtain IV/IO access."
- "Rhythm check → shockable? → Shock 4 J/kg → CPR 2 min. Epinephrine
   0.01 mg/kg after the 2nd shock, then every 3-5 min."
- "Rhythm check → shockable? → Shock ≥4 J/kg (max 10 J/kg or adult dose) →
   CPR 2 min. Amiodarone 5 mg/kg OR lidocaine 1 mg/kg."
- Loop: "Continue cycles; subsequent shocks ≥4 J/kg (max 10 J/kg/adult)."

RIGHT — NON-SHOCKABLE (Asystole / PEA):
- "Epinephrine 0.01 mg/kg ASAP, then every 3-5 min."
- "CPR 2 min; obtain IV/IO access."
- "Rhythm check every 2 min → if shockable, cross to left."

BOTTOM SHARED:
- Diamond "ROSC?" → green: "Post-Cardiac-Arrest Care."
- DOSE PANEL: "Epinephrine 0.01 mg/kg (0.1 mL/kg of 0.1 mg/mL) IV/IO q3-5 min,
  max single 1 mg · Amiodarone 5 mg/kg (max single 300 mg) · Lidocaine 1 mg/kg ·
  Defibrillation 2 → 4 → ≥4 J/kg (max 10 J/kg or adult dose) · CPR cycle 2 min."
- PHYSIOLOGY-DIRECTED panel (amber, 2025): "If arterial line: target diastolic
  BP ≥25 mmHg (infant) / ≥30 mmHg (child ≥1 y). ETCO2 may monitor CPR quality —
  do NOT use a single ETCO2 value alone to stop resuscitation."
- REVERSIBLE CAUSES (H's & T's): "Hypovolemia · Hypoxia · Hydrogen ion ·
  Hypoglycemia · Hypo-/Hyperkalemia · Hypothermia · Tension pneumothorax ·
  Tamponade · Toxins · Thrombosis (pulmonary/coronary)."
```

---

## 8. PALS Bradycardia (with a Pulse & Poor Perfusion)

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Pediatric Bradycardia With a Pulse & Poor Perfusion"

FLOW:
1. Box: "Bradycardia with cardiopulmonary compromise. Support ABCs; airway;
   oxygen; monitor/defibrillator; IV/IO access."
2. Decision diamond: "HR <60/min with poor perfusion despite adequate
   oxygenation & ventilation?"
   - NO → green: "Support ABCs, observe, oxygen, monitor; treat cause."
   - YES → red: "START CPR (compress even if pulse present)."
3. Decision diamond: "Bradycardia persists after CPR?"
   - NO → green: "Stop CPR; continue support & monitoring; treat cause."
   - YES → drug box: "Epinephrine 0.01 mg/kg IV/IO (0.1 mL/kg of 0.1 mg/mL),
     max single 1 mg, repeat q3-5 min (preferred drug). Atropine 0.02 mg/kg
     (min 0.1 mg, max single 0.5 mg, may repeat once) for increased vagal tone
     or primary AV block."
4. Box: "Consider transthoracic/transvenous pacing. Identify & treat reversible
   causes (H's & T's)."
```

---

## 9. PALS Tachycardia (with a Pulse & Poor Perfusion)

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Pediatric Tachycardia With a Pulse & Poor Perfusion"

FLOW:
1. Box: "Tachycardia with cardiopulmonary compromise. Support ABCs; oxygen;
   monitor/defibrillator; IV/IO; evaluate 12-lead ECG / QRS width."
2. Decision diamond: "QRS width?"
   - NARROW (≤0.09 sec) → "Sinus tach vs SVT":
       • Sinus tach (P waves present, variable R-R, infant <220 / child <180) →
         "Search for & treat cause."
       • SVT (P waves absent/abnormal, constant R-R, infant ≥220 / child ≥180) →
         next diamond.
   - WIDE (>0.09 sec) → "Probable VT" → unstable path.
3. Decision diamond (SVT): "Hemodynamically stable?"
   - STABLE → box: "Vagal maneuvers (ice to face/Valsalva) — don't delay.
     Adenosine 0.1 mg/kg rapid IV/IO push (max 6 mg) → 0.2 mg/kg (max 12 mg)."
   - UNSTABLE (or adenosine ineffective) → red: "Synchronized cardioversion
     0.5-1 J/kg → increase to 2 J/kg if ineffective (consider sedation)."
4. WIDE/VT box: "If unstable: synchronized cardioversion 0.5-1 → 2 J/kg. May
   consider adenosine only if regular & monomorphic. Antiarrhythmic with expert
   consult: Amiodarone 5 mg/kg over 20-60 min OR Procainamide 15 mg/kg over
   30-60 min — do NOT give together. Obtain expert consultation."
```

---

## 10. PALS Post-Cardiac-Arrest (Post-ROSC) Care

```
Clean 2D clinical flowchart + targets panel, white background, rounded boxes +
diamonds, navy connectors, navy/teal/amber/green palette, bold sans-serif,
mobile-readable, no 3D, no org branding/acronyms. Bottom-right: small
semi-transparent navy "© williamriveromd.com". 4:3.

TITLE: "Pediatric Post-Cardiac-Arrest Care (after ROSC)"

FLOW (care bundle boxes):
1. "Oxygenation: titrate SpO2 94-99%; avoid hyperoxia & hypoxemia."
2. "Ventilation: target normocapnia PaCO2 ~35-45 mmHg (or patient baseline);
   avoid routine hyperventilation."
3. "Blood pressure: fluids/vasoactives to avoid hypotension; maintain
   age-appropriate BP (≥5th percentile for age; checklist target >10th
   percentile)."
4. "Temperature: actively prevent fever — keep core ≤37.5°C in comatose
   patients; continuous temperature monitoring."
5. "Glucose: avoid hypo- and hyperglycemia."
6. "Continuous EEG; detect & treat seizures promptly; standardize
   sedation/analgesia."
7. "Continuous monitoring; treat underlying causes; consider transfer to
   pediatric center of excellence."

NEUROPROGNOSTICATION PANEL (teal, NEW 2025): "Multimodal & multi-timepoint —
never a single test. Modalities: neuro exam, EEG (incl. quantitative),
neuroimaging (DWI-MRI, cerebral blood flow), serum biomarkers (incl.
neurofilament light, NfL). Assess predictors of favorable AND unfavorable
outcome across the post-arrest period."
```

---

## 11. Dialysis-Unit Code Blue — ACLS Modifications

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Code Blue in the Dialysis Unit — What Changes vs Standard ACLS"

TOP BANNER (navy): "Run the universal ACLS algorithm. Never delay compressions
or defibrillation for the machine — a trained nurse manages the machine in
parallel."

LEFT FLOW (machine actions, in parallel):
1. "Call code / start CPR / get defibrillator."
2. "Stop ultrafiltration (UF) and stop dialysis (bypass)."
3. "Stop the blood pump."
4. Decision diamond: "Air embolism or circuit contamination suspected?"
   - NO → green: "RETURN the patient's blood (~150-250 mL) + give fluid bolus
     (recovers volume)."
   - YES → red: "Do NOT return blood. Clamp both lines, disconnect. (See air
     embolism box.)"
5. Decision diamond: "Machine certified defibrillation-proof (IEC)?"
   - YES → "May defibrillate while connected (no one touching machine; beware
     wet floor)."
   - NO → "Disconnect from machine before defibrillating."
6. Box: "Leave vascular access (fistula/graft needles or catheter) open — use it
   for drugs & fluids."

RIGHT FLOW (treat the top reversible cause):
- Box (amber): "HYPERKALEMIA = leading reversible cause. In a coding dialysis
  patient, give empiric calcium before labs return."
- DOSE PANEL: "Calcium gluconate 10% 10 mL (1 g) IV over 2-3 min (repeat PRN) —
  membrane stabilization, does not lower K · OR Calcium chloride 10% 10 mL via
  central/large-bore · Regular insulin 10 units IV + 25 g dextrose (D50 50 mL),
  monitor glucose · Nebulized salbutamol 10-20 mg · Sodium bicarbonate role
  limited (esp. anuric) · EMERGENCY HEMODIALYSIS = definitive (removes K)."

AIR EMBOLISM box (red, bottom-left): "Clamp lines, stop pump, do NOT return.
Position LEFT lateral decubitus + Trendelenburg (Durant maneuver). 100% oxygen.
If central catheter, aspirate air from distal port. Standard ACLS."

REVERSIBLE CAUSES (dialysis-weighted H's & T's): "Hyperkalemia (#1) ·
Hypovolemia (aggressive UF) · Hydrogen ion (acidosis) · Hypocalcemia · Hypoxia ·
Tamponade (uremic pericarditis) · Thrombosis (coronary/PE) · Toxins · Tension
pneumothorax."
```

---

## 12. Difficult / Failed Tracheal Intubation

```
Clean 2D clinical decision flowchart, white background, rounded boxes + diamonds,
navy connectors, navy/teal/amber/red palette, bold sans-serif, mobile-readable,
no 3D, no org branding/acronyms. Bottom-right: small semi-transparent navy
"© williamriveromd.com". Portrait.

TITLE: "Unanticipated Difficult / Failed Intubation (Adult)"

TOP BANNER (navy): "Throughout: call for help early · declare the problem to the
team · maintain oxygenation · ensure full neuromuscular blockade · limit attempts."

TOP-TO-BOTTOM FLOW (Plan A → B → C → D):

PLAN A — Mask ventilation & tracheal intubation (green header):
- Box: "Optimise: head/neck position (ramped/sniffing), preoxygenation,
  neuromuscular blockade. Laryngoscopy — videolaryngoscope, external laryngeal
  manipulation, bougie."
- Box: "Maximum 3 + 1 attempts (3 by intubator + 1 by a more experienced
  colleague). Confirm with waveform capnography."
- Decision diamond: "Tracheal intubation successful (capnography confirms)?"
  - YES → green box: "Proceed. Confirm tube; ongoing care."
  - NO → red box: "DECLARE FAILED INTUBATION → Plan B."

PLAN B — Maintain oxygenation via supraglottic airway (amber header):
- Box: "Insert 2nd-generation supraglottic airway device (SAD). Maximum 3
  attempts."
- Decision diamond: "Oxygenation via SAD adequate?"
  - YES → box (amber): "STOP AND THINK — choose: (1) wake the patient,
    (2) intubate via the SAD (e.g., fibreoptic-guided), (3) proceed without
    intubating, or (4) front-of-neck access. (Best option depends on urgency
    and skills.)"
  - NO → red box: "→ Plan C."

PLAN C — Final facemask ventilation (amber/red header):
- Box: "Final attempt at facemask ventilation — 2-person technique, oral +
  nasal airway adjuncts, ensure full paralysis."
- Decision diamond: "Facemask oxygenation adequate?"
  - YES → green box: "WAKE THE PATIENT (then reschedule / awake technique)."
  - NO → red box: "DECLARE 'Can't Intubate, Can't Oxygenate' (CICO) → Plan D."

PLAN D — Emergency front-of-neck access / eFONA (red header):
- Box (red): "CICO — life-threatening emergency. Give 100% oxygen; continue
  attempts to oxygenate."
- Box (red): "Scalpel cricothyroidotomy — scalpel–bougie–tube technique
  (transverse stab through cricothyroid membrane, rotate, bougie, railroad a
  size-6.0 cuffed tube). Confirm with capnography."
- Box: "Post-procedure: confirm placement, secure airway, ICU / definitive
  airway, debrief & document."

SIDE NOTE PANEL (teal): "Anticipated difficulty → choose AWAKE intubation
before induction (awake videolaryngoscopy/flexible scope) rather than entering
this emergency pathway. In a declared CICO emergency, 'wake the patient' is NOT
an option — proceed to front-of-neck access."
```

---

## Accuracy flags (verified content; confirm verbatim before print)

- **Adult ACLS:** IV access is **preferred over IO** in 2025 (reverses the 2020
  equivalence) — based on the 2025 ILCOR review incl. PARAMEDIC-3/IVIO. In
  shockable rhythm, **epinephrine is given after the 2nd shock** (after initial
  defibrillation fails); in non-shockable, **ASAP**. Energy: biphasic =
  manufacturer (or max if unknown), monophasic 360 J.
- **Adult Tachycardia:** the 2025 algorithm **does not print fixed cardioversion
  joules** — use device-specific / maximum energy. Do not draw the old
  50-100/120-200/100 J ladder.
- **Adult Post-ROSC:** TTM is now **"temperature control," target 32-37.5°C**,
  fever prevention. Duration "≥24 h" (some sources state ≥36 h total) — label
  with the range, not a single asserted number.
- **PBLS:** infant **two-finger technique dropped** for two-thumb-encircling /
  one-hand (2025). PBLS and PALS are now separate guideline Parts.
- **PALS arrest:** **physiology-directed resuscitation** is the headline 2025
  addition (DBP ≥25 infant/≥30 child; ETCO2 for quality, not a sole stop rule).
  Drug/energy doses unchanged from 2020.
- **PALS post-ROSC:** **pediatric neuroprognostication is NEW in 2025**
  (multimodal/multi-timepoint, adds NfL). BP target: Part 8 says **>5th
  percentile**; the PALS checklist says **>10th percentile** — sources differ.
- **Dialysis figure:** the stop-UF / return-blood / disconnect-unless-defib-proof
  checklist is **ERC Special Circumstances + AJKD Hemodialysis Emergencies**, not
  a named AHA dialysis statement (none confirmed to exist). Hyperkalemia
  treatment hierarchy is AHA/ILCOR; **empiric calcium in the coding dialysis
  patient is standard practice**, while ILCOR found insufficient evidence to
  formally recommend for/against calcium and **suggests insulin+glucose**.
- **Difficult / failed intubation figure:** built on the **Difficult Airway
  Society (DAS) 2015** unanticipated-difficult-intubation algorithm (Plans A–D,
  ending in scalpel cricothyroidotomy for CICO) — the standard teaching
  algorithm; this is an **airway/anaesthesia guideline, not part of the AHA CPR
  guidelines**. The **ASA 2022** difficult-airway update is reflected in the side
  note (awake-intubation decision before induction; "wake the patient" removed
  from the CICO emergency). Confirm the scalpel–bougie–tube wording against the
  DAS/ASA source before print. Sources: DAS 2015 (Br J Anaesth 2015;115:827) ·
  ASA 2022 Practice Guidelines for Management of the Difficult Airway.
- Because automated full-text fetch of ahajournals.org / cpr.heart.org was
  blocked, all figures were corroborated across ≥2 sources; **open the official
  2025 algorithm PDFs to confirm exact box wording before finalizing print art.**

### After images are generated
1. Save each `<name>.png` to `images/`; build matching `.webp` (Pillow q82).
2. Add a **"Resuscitation & emergencies"** section to `guides/nephrology-atlas.html`
   (algorithms category) with each as a `render:'2D'` item; bump the Algorithms
   stat-pill; run the `node --check` TABS validation.
3. Wire the dialysis figure (and any others desired) into
   `guides/code-blue-acls-dialysis-unit.html` as `<figure class="illus-panel">`
   with WebP+PNG and 4-language `<figcaption>`.
