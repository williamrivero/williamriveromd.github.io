# Guide Blueprint — BLS/ACLS Code Blue Protocol for Dialysis Units

**Working filename:** `guides/bls-acls-code-blue-dialysis.html`
**Slug:** `bls-acls-code-blue-dialysis`
**Type:** Dual-mode guide (Patient/Family tab + Clinician tab), 4-language (EN/TL/CEB/KAP)
**Status:** Plan / blueprint — not yet built
**Author:** W. G. M. Rivero, MD, FPCP, DPSN
**Target review tag:** 2026 · AHA 2020 ACLS Guidelines · ANNA Standards · DOH PH · PRC BLS 2023

---

## 1. Purpose & positioning

A comprehensive, practical guide on **Code Blue (cardiac arrest) recognition, response, and
resuscitation** tailored specifically to the **dialysis unit environment** — both free-standing
outpatient dialysis centers and in-hospital hemodialysis units. Dialysis patients face a cardiac
arrest risk 10–20× higher than the general population; the dialysis unit itself presents unique
rescue challenges (ESRD physiology, active vascular access, anticoagulated circuits, limited
respiratory support) that standard ACLS courses do not fully address.

**Dual audience rationale:**
- **Patient/Family tab:** demystifies what a "code blue" looks like, what the team is doing, why
  it happens more often in dialysis patients, what families can do, and the concept of advance
  directives (DNR/DNI) in the ESRD context.
- **Clinician tab:** step-by-step operational protocol — team roles, ACLS algorithm with
  dialysis-specific modifications, ESRD drug dosing, AV access pitfalls, post-ROSC care,
  documentation with the Code Blue Recording Flowsheet, and mock-code drill design.

**Scope decision:**

| Topic | Covered here | Defer to |
|---|---|---|
| General cardiac arrest (community) | Brief intro + context | AHA / Red Cross ACLS/BLS courses |
| Dialysis-specific arrest triggers | Yes — core | — |
| ACLS algorithm (modified for ESRD) | Yes — full clinician section | — |
| Drug dosing in ESRD/dialysis | Yes — reference table | `dialysis-prescription.html` |
| AV fistula/graft/catheter emergencies | Yes — bleeding, disconnection | `avf-aneurysm-and-changes.html`, `dialysis-access-infection.html` |
| Post-cardiac arrest care | Yes — TTM, cath lab timing, ICU handoff | — |
| Advance directives in ESRD (DNR/DNI) | Yes — patient tab | — |
| Code Blue Recording Flowsheet | Yes — embedded fillable reference + explained | — |
| Hyperkalemia (trigger, not full guide) | Yes — ESRD-specific arrest cause | links to `metabolic-acidosis-ckd.html` |
| Anemia & cardiac risk | Brief + link | `anemia-management.html` |
| Cardiovascular risk in ESRD | Brief + link | `cardiovascular-death-dialysis.html`, `heart-kidney-connection.html` |

---

## 2. Title, meta & SEO

**Patient hero `<h1>` (EN):** "Code Blue in the Dialysis Center — *What Happens When Someone
Collapses During Treatment*"

**Clinician hero `<h1>` (EN):** "BLS/ACLS Code Blue Protocol for Dialysis Units — *Operational
Guide & ESRD-Specific Modifications*"

**`<title>`:** `Code Blue & Cardiac Arrest Protocol for Dialysis Units · W. G. M. Rivero, MD`

**Meta description (EN):** "What to do when a patient collapses in the dialysis center — the
Code Blue protocol, ACLS algorithm with ESRD-specific modifications, drug dosing, Code Blue
Recording Flowsheet guide, and advance directives in dialysis. For patients, families, and
dialysis care teams."

**Keywords:** code blue dialysis, cardiac arrest dialysis center, ACLS ESRD, hemodialysis
cardiac arrest protocol, code blue recording sheet, dialysis CPR, ROSC dialysis, BLS dialysis
unit Philippines, dialysis emergency protocol, hyperkalemia cardiac arrest, DNR dialysis.

**Hero subtitle (EN):** "Cardiac arrest happens at a much higher rate in dialysis patients.
This guide explains what the dialysis team does during a code blue — and helps clinicians run
an evidence-based, ESRD-adapted resuscitation with clear team roles, drug dosing, and
documentation."

**JSON-LD:** `MedicalWebPage`, `audienceType: "patient"`, `dateModified`/`datePublished` filled
by `patch_last_reviewed.py`. (Do not hand-write; the patch script owns this.)

---

## 3. Page architecture (matches house dual-mode skeleton)

```
<header class="site-header">           HOME · ← All Guides
<div class="guide-lang-bar">           EN / TL / CEB / KAP  (ids glb-en…glb-kap)
<div class="guide-toggle-bar">         Dark · Desktop
<div class="audience-tabs">            🧑‍⚕️ For Patients & Families | 🩺 For Clinicians
                                       (tab-pt active by default, tab-md)

<div class="mode-patient">             ← TEAL hero gradient
   <section class="hero">  +  hero <figure>/<picture> (fetchpriority high)
   <nav class="nav-strip"> patient pills
   <main class="container"> … patient sections …
</div>

<div class="mode-physician">           ← NAVY hero gradient (#0f1e2e→#1a2e4a), gold accent #d4af4f
   <section class="hero"> + clin-badges
   <nav class="nav-strip"> clinician pills
   <main class="container"> … clinician sections …
</div>

<!-- DR CARD -->  <div class="dr-card-wrap"> … </div>
<!-- RELATED-GUIDES-START --> <div class="related-guides"> … <!-- RELATED-GUIDES-END -->
<footer class="guide-footer"> … references …
```

**Critical conventions (from CLAUDE.md):**
- Start in **patient mode** (default CSS state). **Never** add a restore-on-load IIFE —
  `patch_mode_cls.py` strips it (CLS fix). `setMode()` may still write to `localStorage`.
- `dr-card-wrap` → `related-guides` → `footer` must be the last blocks, **outside** `<main>`,
  nothing between them. Enforced by `patch_signature_position.py`.
- Do **not** write CSS into the guide's master `<style>` — master CSS is owned by
  `patch_master_css.py`. Per-guide tweaks go in a second `<style>` block only.
- Every translatable string needs all four sibling `data-lang` spans (en/tl/ceb/kap).

---

## 4. PATIENT TAB — section outline

Nav pills: **What is a Code Blue · Why it happens in dialysis · What the team does · The family's role · Advance directives (DNR/DNI) · Questions to ask your doctor**

### 4.1 What is a "Code Blue"?
Plain-language explanation: the phrase used in hospitals and clinics when someone's heart stops
or they stop breathing and the team needs to rush to help. Acknowledge it can be frightening to
witness as a fellow patient or family member. Reassure that the team prepares and drills for this.

### 4.2 Why does this happen more in dialysis patients?
Framed honestly, without alarm:
- Dialysis patients have hearts that work harder — high blood pressure, enlarged hearts, weakened
  heart muscles are common.
- Fluid changes during dialysis (taking off too much fluid too fast) can stress the heart.
- Potassium build-up between dialysis sessions (if diet is not followed) can trigger dangerous
  heart rhythms. Cross-link `eating-on-dialysis.html`.
- Calcium and other electrolytes also shift during treatment.
- Not everyone who collapses dies — many recover, especially when the team responds fast.

**Statistics (patient-appropriate framing):** "Studies show dialysis patients are more likely to
have a cardiac event during or shortly after treatment — which is exactly why dialysis centers are
required to have trained staff and emergency equipment on site at all times."

### 4.3 What does the dialysis team do during a Code Blue?
Step-by-step, plain language, calming tone:
1. **Recognize** — a staff member notices the patient is unresponsive, not breathing normally.
2. **Call for help** — the Code Blue alarm is activated; the on-call physician or nephrologist is
   called immediately.
3. **Start CPR** — chest compressions begin right away while the dialysis machine is put on hold.
4. **Use the defibrillator (AED/shock machine)** — if the heart is in a dangerous rhythm, a
   controlled electrical shock may restore it.
5. **Give medicines** — medicines like epinephrine help the heart restart.
6. **Record everything** — a designated team member writes down every action and time on the
   Code Blue Recording Sheet (so doctors can review exactly what happened).
7. **Notify family** — a staff member contacts the family as soon as possible.
8. **Transfer if needed** — if the patient regains a pulse (ROSC), they are transferred to the
   hospital emergency room or ICU for further care.

### 4.4 The family's role
- **Stay calm and step back** — the team needs space to work.
- **Tell staff your contact number when you sign in** — they will call as soon as it is safe to do so.
- **Provide advance directive information** — if your loved one has a Do Not Resuscitate (DNR)
  order, bring a copy every session. Verbal instructions cannot always be honored in a crisis.
- **Ask questions afterward** — you have a right to know what happened and what comes next.

### 4.5 Advance Directives — DNR & DNI in Dialysis
Sensitive, respectful section:
- What a DNR (Do Not Resuscitate) and DNI (Do Not Intubate) order means.
- Why some dialysis patients — especially those with very advanced illness or poor quality of life
  on dialysis — choose to document these wishes.
- How to talk to your nephrologist about advance directives. The conversation is not giving up;
  it is making sure your values guide your care.
- Philippine law context: reference RA 11223 (UHC Act) patient rights provisions; note that formal
  advance directive legislation is still evolving in PH — document preferences in writing and
  discuss with family and care team. (Verify legal status at build time.)
- Cross-link: `dialysis-coming-pre-eskd.html` (preparation for dialysis section on goals of care).

### 4.6 Questions to ask your nephrologist
Printable checklist style:
- "Do you have a Code Blue team trained and ready at this dialysis center?"
- "What emergency equipment do you have here — a defibrillator, oxygen, crash cart?"
- "If something happens to me during dialysis, who will you call first?"
- "Can I prepare an advance directive? How do I do that in the Philippines?"
- "What are the warning signs before cardiac arrest I should tell my family about?"

---

## 5. CLINICIAN TAB — section outline

Clin badges: `AHA 2020 ACLS` · `ESRD-Modified` · `Free-standing & In-hospital` · `ANNA Standards`
· `Code Blue Documentation` · `Mock Code Protocol`

Nav pills: **Why dialysis arrests are different · ESRD arrest triggers · Code Blue activation ·
Team roles · ACLS algorithm (ESRD-modified) · Defibrillation · Drug dosing · Access & circuit ·
Post-ROSC care · Recording flowsheet · Mock code drills · Algorithms · Evidence**

### 5.1 Why Dialysis Cardiac Arrest Is Clinically Distinct
Epidemiology + framing for the clinician:
- SCA incidence in dialysis patients: ~7× general population; ~25% of ESRD deaths are sudden
  cardiac death.
- >80% of in-dialysis arrests occur during the **last hour of treatment** or **within 1 hr post-
  session** — fluid and electrolyte shifts are the dominant trigger.
- Shockable rhythms (VF/pVT) are less common in ESRD than in the general SCA population
  (~25–30% vs ~50%) — non-shockable PEA and asystole dominate, driven by electrolyte causes.
- This shifts the resuscitation priority: **treat the reversible cause (the 5 Hs + 5 Ts,
  especially hyperkalemia, hypovolemia, hypoxia, and acidosis) simultaneously with CPR**.

### 5.2 ESRD-Specific Arrest Triggers — The Modified "5H + 5T + 3D" Framework

**Standard 5Hs:**
- Hypovolemia (ultrafiltration excess, bleeding)
- Hypoxia
- Hydrogen ion (acidosis — metabolic acidosis common in ESRD)
- Hypo/Hyperkalemia (**hyperkalemia is the dominant ESRD-specific H**)
- Hypothermia

**Standard 5Ts:**
- Tension pneumothorax
- Tamponade (uremic pericarditis with effusion)
- Toxins (drug errors, dialysate contamination)
- Thrombosis – pulmonary (PE is underdiagnosed in ESRD)
- Thrombosis – coronary

**3D additions (dialysis-specific):**
- **Dialysate error** (wrong potassium/calcium bath — low-K dialysate causing hypokalemia arrest)
- **Disconnection** (air embolism from circuit disconnection; massive hemorrhage from needle
  dislodgement)
- **Drug error** (heparin overdose, EPO hypersensitivity, IV iron reaction)

### 5.3 Code Blue Activation — Dialysis Unit Protocol

**Recognition triggers (call for help if ANY present):**
- Unresponsive to voice or sternal rub
- Absent or agonal respirations
- No palpable pulse (carotid or femoral — **avoid brachial/radial on AVF side**)
- Sudden hypotension + unresponsiveness on the dialysis chair

**Activation sequence:**
1. Call out "CODE BLUE, [BED/CHAIR NUMBER]" — designate one person to activate the unit alarm
   and call the on-call physician/ROD/on-call nephrologist simultaneously.
2. Start the **Code Blue Recording Clock** — note CPR Start Time, Time Code Called, Team,
   Time Team Arrived on the Recording Flowsheet.
3. Put the dialysis machine on **bypass/rinse-back** if ROSC is anticipated; otherwise leave
   circuit connected unless it is a hemorrhage emergency.
4. Lower the dialysis chair flat; firm surface under the patient (dialysis chair ≠ hard surface —
   use a backboard if available).

### 5.4 Team Roles (ESRD Unit — Adapted from AHA Team Dynamics)

| Role | Primary duty during code | Who fills it |
|---|---|---|
| **Compressor #1** | High-quality CPR, 2-min cycles, rate 100–120/min, depth 5–6 cm | Nurse #1 / Technician |
| **Compressor #2** | Relieves Compressor #1 every 2 minutes | Nurse #2 / Technician |
| **Airway** | BVM ventilation (30:2 or asynchronous post-intubation); manages O₂ | Nurse / Resp Therapist |
| **Defibrillator / AED** | Pads on, charge, analyze rhythm every 2 min; shock if indicated | Nurse #3 / Charge Nurse |
| **Medications** | Prepares and gives IV/IO drugs per algorithm; accesses IV/CVC — NOT AVF/AVG | Charge Nurse / Pharmacist |
| **Recorder** | Logs time, interventions, drugs on Code Blue Recording Flowsheet | Dedicated nurse/tech |
| **Team Leader** | Directs resuscitation; closes loop communications; decides ROSC/termination | Physician / On-call Nephrologist |
| **Family liaison** | Removes other patients from area; contacts family; completes notification section of flowsheet | Unit Secretary / Nurse |
| **Circuit manager** | Manages dialysis machine (bypass, saline prime, blood return if ROSC, or circuit disconnect as ordered) | Technician |

### 5.5 ACLS Algorithm — ESRD-Modified (BLS → ACLS Sequence)

> **Foundational rule:** All standard AHA 2020 ACLS steps apply. ESRD modifications are
> additive — they do not replace the algorithm.

**Phase 1 — BLS Foundation (0–2 min)**
1. Confirm unresponsiveness; call for help + AED.
2. Start **high-quality CPR** immediately. Minimize interruptions (<10 sec for rhythm check).
3. Apply pads (avoid AVF arm if possible — place pad below clavicle and left lateral as usual;
   note AVF does not contraindicate defibrillation).
4. Open airway; BVM ventilation at 30:2.

**Phase 2 — Rhythm Analysis & Defibrillation (every 2 min)**
- **VF / pulseless VT (shockable):**
  - Biphasic: 120–200 J (device-specific); Monophasic: 360 J
  - Resume CPR immediately after shock — do not pause to check pulse.
  - → Epinephrine 1 mg IV/IO every 3–5 min.
  - → Amiodarone: 1st dose 300 mg IV; 2nd dose 150 mg IV.
  - → Lidocaine (if amiodarone unavailable): 1–1.5 mg/kg IV; 2nd dose 0.5–0.75 mg/kg.
- **Asystole / PEA (non-shockable — ESRD dominant rhythm):**
  - Continue high-quality CPR. No shock.
  - → Epinephrine 1 mg IV/IO every 3–5 min.
  - → **Prioritize reversible cause treatment** (see Phase 3).

**Phase 3 — Treat ESRD Reversible Causes (concurrent with CPR)**

| Suspected cause | Bedside clue | Intervention |
|---|---|---|
| **Hyperkalemia** | Pre-arrest K > 6 mEq/L, peaked T waves, last session missed | **Calcium chloride 1 g IV** (10 mL of 10% — cardiac membrane stabilization); Sodium bicarb 50 mEq IV; consider dextrose + insulin push; emergent dialysis if ROSC |
| **Hypovolemia (UF excess)** | Excessive weight removed, relative hypotension pre-arrest | Stop dialysis UF; NS 500 mL bolus IV |
| **Hypoxia** | Low pre-arrest SpO₂ | 100% O₂ via BVM; airway; intubation if needed |
| **Metabolic acidosis** | Known severe acidosis, bicarb < 15 | **Sodium bicarbonate 50 mEq (50 mL of 8.4%) IV** — use cautiously; causes hyperosmolarity |
| **Air embolism** | Circuit disconnection noted; sudden arrest | Left lateral decubitus + Trendelenburg; 100% O₂; aspirate via central line if available |
| **Dialysate error (hypokalemia arrest)** | Low-K bath used; ECG shows U waves / flat T pre-arrest | Potassium chloride IV per protocol; dialysate corrected |
| **Cardiac tamponade** | Uremic patient, JVD, muffled sounds | Emergent bedside US; pericardiocentesis |
| **PE** | Immobile, DVT risk, CVC patient | Empiric thrombolytics if high suspicion and no ROSC with standard ACLS |

**Phase 4 — ROSC / Termination**
- **ROSC achieved:** → Post-cardiac arrest care (Section 5.7). Transfer to ER/ICU.
- **Termination criteria:** Team leader decision. Document time and reason on Recording Flowsheet.
  Standard criteria apply: ≥ 20 min of resuscitation with no shockable rhythm, no reversible
  cause found, no ROSC. **Special consideration in ESRD:** hyperkalemia-driven PEA may respond
  after longer resuscitation if calcium/bicarb/dialysis is applied — extend effort if cause is
  clearly treated mid-code.

### 5.6 Vascular Access Considerations During Code Blue

- **Never use AVF/AVG for drug/fluid delivery during arrest** — high-pressure flow, risk of
  hematoma, rupture, and failed delivery. Use peripheral IV or CVC (tunneled catheter lumen is
  acceptable for emergencies if patent and the nurse is trained).
- **IO access** (tibial or humeral) is the fastest fallback if no IV is available.
- **Needles in AVF at arrest onset:** leave needles in place if patient needs to go to CPR; clamp
  tubing and cover. Do not attempt removal during active chest compressions — risk of needle
  dislodgement, hemorrhage. Remove after ROSC or circuit secured.
- **Catheter bleeding arrest:** clamp both lumens immediately; apply pressure at exit site; maintain
  CPR uninterrupted.
- **AED pad placement:** standard placement (right infraclavicular + left lateral) is safe with
  AVF. If pacemaker/ICD present, keep pad ≥ 8 cm from device.

### 5.7 Post-ROSC Care (Pre-Transfer Stabilization)

| Priority | Action |
|---|---|
| Airway | Secure airway if not already intubated; confirm ETT position |
| Hemodynamics | Target MAP > 65 mmHg; titrate vasopressors if available |
| 12-lead ECG | Immediately; evaluate for STEMI → emergent cath lab consideration |
| Temperature management | Target normothermia (36–37.5°C); avoid hyperthermia post-ROSC |
| Glucose | Target 7.8–10 mmol/L (140–180 mg/dL); avoid hypoglycemia |
| Electrolytes | Repeat K⁺, Ca²⁺, bicarb; correct as needed; arrange emergent dialysis if hyperK persists |
| Dialysis circuit | Complete rinse-back if ROSC and patient stable; document UF volume removed |
| Transport | Notify receiving ER/ICU; transmit Code Blue Recording Flowsheet with patient |
| Family | Complete notification section of flowsheet; provide status update |

### 5.8 Code Blue Recording Flowsheet — Field-by-Field Guide

The **Code Blue Recording Flowsheet** is a two-sided, time-stamped document completed by the
designated Recorder during every resuscitation event. Each field:

**Header fields (fill at code activation):**
- **DATE** / **ROOM #** / **PATIENT LABEL** (NAME, AGE, MRN)
- **CPR START TIME** — the exact time chest compressions began (military/24h format)
- **TIME CODE CALLED** — when the alarm/overhead page was activated
- **TEAM** — name or role of team leader
- **TIME TEAM ARRIVED** — when the responding team reached bedside

**Main tracking table (one row per 2-minute CPR cycle):**

| Column | What to record |
|---|---|
| TIME (military) | 24-hour time at each rhythm check (every 2 min) |
| BP | If measured during a brief pulse check; leave blank if no check performed |
| HR | Heart rate from monitor during pulse check |
| RHYTHM | VF / VT / PEA / Asystole / Sinus / etc. |
| O₂ Sat | SpO₂ if waveform is reliable during CPR |
| PULSE (0 = absent, + = present) | Result of pulse check |
| CPR (x2 min rounds) | Tick/checkmark each 2-min cycle; note who compressed |
| SHOCK | Record joule setting and number of shocks delivered |
| EPINEPHRINE | 1 mg — tick each dose; note time |
| AMIODARONE | 300 mg (1st) / 150 mg (2nd) — tick and note dose |
| LIDOCAINE | 1–1.5 mg/kg (1st) / 0.5–0.75 mg/kg (2nd) — tick and note |
| ADENOSINE | 6 mg (1st) / 12 mg (2nd) — rapid IV push; for SVT with pulse, not PEA/VF |
| ATROPINE | 1 mg q3–5 min, max 3 mg — **note: atropine is no longer first-line in asystole per 2020 AHA; included for bradycardia or pulseless rhythms in specific settings** |
| CALCIUM CHLORIDE | 1 g / 10 mL — tick and note time; essential in hyperK arrest |
| SODIUM BICARBONATE | 50 mEq / 50 mL — tick and note; reserved for confirmed severe acidosis or hyperK |
| COMMENTS | BVM, intubation, IV/IO access, fluid boluses, pacing, cardioversion, line placement, labs drawn, circuit status, any unusual events |

**Conclusion section (fill at code end):**
- **TIME EVENT ENDED**
- **PATIENT OUTCOME:** ROSC achieved / Expired — efforts terminated
- **REASON RESUSCITATION ENDED:** ROSC / No benefit to continue
- **FAMILY NOTIFICATION:** At bedside / By phone / Unable to reach / No family / Pending
  - Name of person notified; relationship to patient
- **PERSONNEL ON DUTY:** Primary Nurse, Charge Nurse, Recorder, CPR Staff, Medication Staff,
  Respiratory Therapist, Resident on Duty (ROD), Physician, On-Call Nephrologist

**Recorder best practices:**
- Use military (24-hour) time for every entry.
- Write legibly; if time is uncertain, bracket it (e.g., "~14:03").
- Do not leave the Recorder role to help with CPR — documentation cannot be recreated afterward.
- After the code, retain the original flowsheet in the patient's chart; a copy goes to the
  Quality Assurance review.

### 5.9 Mock Code Drill Design for Dialysis Units

**Recommended frequency:** quarterly at minimum; at least one unannounced drill per year.

**Drill scenarios to rotate:**
1. Hyperkalemic PEA arrest (most realistic ESRD scenario) — no shockable rhythm; requires calcium +
   bicarb + cause identification.
2. VF arrest mid-dialysis with defibrillation — tests AED competency and pad placement with AVF.
3. Air embolism from circuit disconnection — tests recognition and positioning response.
4. Cardiac arrest + access bleeding simultaneously — tests team role differentiation under stress.
5. Pediatric/young ESRD patient (if pediatric patients are seen in the unit).

**Drill checklist:**
- [ ] Code Blue alarm activates in < 30 seconds of recognition
- [ ] First compression in < 1 minute of collapse recognition
- [ ] AED applied and rhythm analyzed in < 2 minutes
- [ ] Team roles assigned without confusion; closed-loop communication used
- [ ] Recorder starts flowsheet at CPR start time
- [ ] Reversible causes verbalized and addressed
- [ ] Family liaison role filled
- [ ] Debriefing conducted within 30 minutes of drill

**Documentation:** record drill date, participants, scenarios, deficiencies, and corrective actions
in the unit's QA log. Required for PHIC accreditation and DOH licensing.

### 5.10 Algorithms

Three embedded flowchart candidates (generate with `williamriveromd-infographic-skill`):

1. **ESRD Code Blue Activation & Team Assembly** — from recognition to first compression.
2. **ACLS Algorithm — Dialysis Unit ESRD Modification** — shockable vs. non-shockable branches
   with ESRD-specific drug doses and concurrent reversible cause treatment.
3. **Post-ROSC Stabilization & Transfer Protocol** — from return of pulse to ICU handoff.

### 5.11 Case Snapshots

1. **Hyperkalemic PEA arrest** — patient missed 2 dialysis sessions; found unresponsive post
   session with K⁺ 7.8 mEq/L. PEA; calcium chloride + bicarb given during CPR; ROSC at 18 min.
2. **VF arrest from dialysate bath error** — low-K bath (0.0 mEq/L) administered; patient
   developed VF 90 min into treatment. Defibrillated × 2; amiodarone; ROSC.
3. **Air embolism from needle dislodgement** — patient unresponsive; noted AVF needle dislodged
   with air sucked into venous return. Left lateral decubitus positioning; 100% O₂; ROSC.
4. **Pulseless VT — uremic cardiomyopathy** — patient with ESRD + severe LV dysfunction; VT
   arrest during routine HD. Defibrillated × 1; amiodarone; ROSC; transferred for ICD evaluation.

### 5.12 Evidence & Guidelines

- AHA 2020 Guidelines for CPR and ECC — primary ACLS algorithm source
- AHA Scientific Statement on Sudden Cardiac Death in ESRD (Circulation 2020)
- KDIGO 2024 CKD Update — cardiovascular risk in CKD/ESRD
- ANNA (American Nephrology Nurses Association) Standards of Practice for Hemodialysis
- DOH Philippines — Hospital Licensure Standards for Dialysis Units
- Philippine Heart Association ACLS/BLS 2023 update
- Philippine Renal Disease Registry (NKTI) — ESRD epidemiology data

---

## 6. Images / visual assets

Use the `williamriveromd-infographic-skill` to generate prompts. Candidate assets:

1. **Hero (patient):** editorial, calm — a patient on a dialysis chair with a supportive nurse
   nearby; teal house palette. 1024×1024, capped at 600px by `patch_hero_maxwidth.py`. Non-alarming.
2. **Code Blue Team Roles Diagram** (patient tab) — color-coded roles around a dialysis chair,
   simplified. Shows who does what without being frightening.
3. **ESRD Code Blue Activation Flowchart** (clinician) — recognition → activation → roles → CPR
   start. Clean algorithm style.
4. **ACLS Algorithm — Dialysis Unit ESRD-Modified** (clinician) — shockable vs. non-shockable
   with ESRD drug dosing inset boxes. Landmark reference-card style.
5. **ESRD Reversible Causes (5H + 5T + 3D) Reference Card** (clinician) — matrix infographic,
   one row per cause with bedside clue and intervention.
6. **Code Blue Recording Flowsheet — Annotated Sample** (clinician) — labeled reproduction of
   the completed flowsheet showing which field goes where. Not a fillable form (guide is static
   HTML) — a visual annotation/teaching tool.

Hero needs `fetchpriority="high" loading="eager"`, full-width `<figure>`, `<img>` capped at
`max-width:600px` centered. Each `<figure>` gets a `<figcaption>` with `<p class="fig-desc">`.
Add og:image tags via `williamriveromd-local-image-generator` once images exist.

---

## 7. Cross-linking — `related_guides.json`

Add the new entry:

```json
"bls-acls-code-blue-dialysis.html": [
  "cardiovascular-death-dialysis.html",
  "heart-kidney-connection.html",
  "dialysis-access-infection.html",
  "avf-aneurysm-and-changes.html",
  "metabolic-acidosis-ckd.html",
  "eating-on-dialysis.html",
  "dialysis-prescription.html",
  "dialysis-adequacy.html",
  "post-dialysis-fatigue.html",
  "dialysis-coming-pre-eskd.html"
]
```

Add `bls-acls-code-blue-dialysis.html` into the arrays of reverse-linked guides so the
relationship is bidirectional: `cardiovascular-death-dialysis.html`, `heart-kidney-connection.html`,
`dialysis-access-infection.html`, `avf-aneurysm-and-changes.html`, `metabolic-acidosis-ckd.html`.

---

## 8. Build / patch workflow (after authoring the HTML)

Author the file by copying the dual-mode skeleton from a recent guide (e.g. `dialysis-adequacy.html`),
then run, in order (or just run `/setup-guide bls-acls-code-blue-dialysis.html`):

```bash
python3 patch_master_css.py         --guide bls-acls-code-blue-dialysis.html
python3 patch_hero_fetchpriority.py --guide bls-acls-code-blue-dialysis.html
python3 patch_hero_fullwidth.py     --guide bls-acls-code-blue-dialysis.html
python3 patch_hero_maxwidth.py      --guide bls-acls-code-blue-dialysis.html
python3 patch_mode_cls.py           --guide bls-acls-code-blue-dialysis.html
python3 patch_mode_restore.py       --guide bls-acls-code-blue-dialysis.html
python3 patch_signature_position.py --guide bls-acls-code-blue-dialysis.html
python3 patch_last_reviewed.py      --guide bls-acls-code-blue-dialysis.html
python3 generate_sitemap.py
# then edit related_guides.json (section 7)
```

Each script is idempotent and supports `--dry-run`. Commit the guide + `sitemap.xml` +
`related_guides.json` to `main`.

---

## 9. Authoring checklist

- [ ] Dual-mode skeleton copied; `mode-patient` default, navy `mode-physician`.
- [ ] All translatable strings have en/tl/ceb/kap sibling spans.
- [ ] No restore-on-load IIFE; page paints in patient mode.
- [ ] `dr-card-wrap` → `related-guides` → `footer` last, outside `<main>`.
- [ ] Hero patched (fetchpriority/fullwidth/maxwidth).
- [ ] Figures have figcaption + fig-desc; image-lightbox script before `</body>`.
- [ ] Code Blue Recording Flowsheet annotated image included in clinician tab (Section 5.8).
- [ ] All ACLS drug doses cross-checked against AHA 2020 guidelines at build time.
- [ ] AHA 2020 note on atropine in asystole preserved (no longer first-line).
- [ ] Advance directives section verified against current Philippine legal framework.
- [ ] Mock code drill checklist included and verifiable.
- [ ] `related_guides.json` updated both directions.
- [ ] `sitemap.xml` regenerated.

---

## 10. Editorial guardrails

- **This is an educational guide, not a substitute for certified BLS/ACLS training.** Every
  clinician section must include the note: "This guide supplements, not replaces, certified
  AHA/PHA BLS-ACLS training. All dialysis unit staff should maintain current BLS certification."
- Drug doses must match AHA 2020 at build time — flag any that change with future guideline updates.
- Patient tab must never be alarming; lead with "the team is trained and prepared."
- Advance directives section is sensitive — use compassionate, non-coercive language.
- Code Blue Recording Flowsheet content reproduced educationally (not as a fillable clinical form
  — the HTML guide is static; link to downloadable PDF version if one is created separately).
- All Filipino context (DOH, PHIC dialysis accreditation, PHA ACLS) verified at build time.
