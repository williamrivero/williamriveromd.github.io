# -*- coding: utf-8 -*-
"""Algorithm recognition item bank for the Resuscitation Lab Practice Lab. Writes data/academy-resus/recognition.json.
Item: id, type (pick | strip | missing | order | unsafe | evolve), set (adult | pediatric | dialysis tags), algo, stem,
optional strip {rhythm, rate}, findings, options, answer (index; for "order" the correct order of option indexes),
why (one explanation per option, or one string for "order"), tag (misconception), mod (module number that teaches it).
Every strip item carries clinical findings: a trace alone never establishes a pulse, perfusion or stability.
Run from the repo root:  python3 tools/techcourses/resus/recognition.py     DRAFT pending clinical sign-off."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "academy-resus" / "recognition.json"

TAGS = {
    "rhythm-equals-pulse": "Treating the monitor rhythm as proof of a pulse",
    "gasping-is-breathing": "Mistaking gasping for breathing",
    "stable-by-numbers": "Judging stability by heart rate instead of signs",
    "shock-nonshockable": "Shocking a nonshockable rhythm",
    "wrong-algorithm-after-change": "Staying in the old algorithm after the patient changes",
    "hyperk-normal-ecg": "Trusting a normal ECG in hyperkalemia",
    "hyperk-pulse-vs-arrest": "Confusing hyperkalemia with a pulse and hyperkalemic arrest",
    "return-contaminated-blood": "Returning blood after air, hemolysis or a reaction",
    "pause-for-machine": "Pausing CPR for the machine",
    "peds-adult-dose": "Adult doses, energies or ratios in a child",
    "epi-concentration": "Confusing epinephrine concentrations or routes",
    "peds-breathing-first": "Missing respiratory failure as the cause in a child",
    "rosc-check": "Confirming ROSC without a pulse and pressure",
    "artifact": "Mistaking artifact for a lethal rhythm",
    "stop-dialysis-hyperk": "Stopping dialysis in stable hyperkalemia",
    "sync-unsync": "Confusing synchronized and unsynchronized shocks",
}

I = []


def item(t, sets, algo, stem, options, answer, why, tag, mod, strip=None, findings=None):
    d = {"id": f"r{len(I) + 1:02d}", "type": t, "set": sets, "algo": algo, "stem": stem, "options": options, "answer": answer,
         "why": why, "tag": tag, "mod": mod}
    if strip:
        d["strip"] = strip
    if findings:
        d["findings"] = findings
    I.append(d)


A, D, PD = ["adult"], ["adult", "dialysis"], ["pediatric", "dialysis"]

# ── vignette -> algorithm + first action ──
item("pick", D, "adult-arrest", "A patient slumps in the chair: unresponsive, gasping every 10 seconds, no definite pulse in 10 seconds.",
     ["Adult cardiac arrest: compressions now", "Respiratory arrest: ventilate only", "Intradialytic hypotension: saline", "Vasovagal faint: legs up and observe"], 0,
     ["Gasping with no definite pulse is cardiac arrest.", "There is no pulse, so ventilation alone does not circulate blood.", "Treating pressure first wastes the critical minute.", "A faint has a pulse."], "gasping-is-breathing", 3)
item("pick", A, "resp-arrest", "An adult is not breathing but has a strong carotid pulse.",
     ["Respiratory arrest: open the airway and give about one breath every 6 seconds", "Cardiac arrest: compressions", "Shock", "Observe"], 0,
     ["Respiratory arrest with a pulse: ventilate (AHA suggests 10 breaths a minute) and recheck the pulse often.", "There is a pulse.", "No rhythm indication.", "Without breathing, arrest follows within minutes."], "gasping-is-breathing", 3)
item("pick", D, "deterioration", "A patient is pale and sweaty with a pressure of 76/40, responsive, breathing normally, pulse 104, an hour before the end of the session.",
     ["Deterioration with a pulse: lay flat, stop fluid removal, check the access and causes (Card 3)", "Cardiac arrest", "Respiratory arrest", "Tachycardia algorithm: cardiovert"], 0,
     ["Responsive with a pulse and breathing: deterioration, treated by cause.", "There is a pulse.", "He is breathing.", "Sinus tachycardia from low pressure is not treated with cardioversion."], "rhythm-equals-pulse", 3)
item("pick", A, "adult-brady", "Heart rate 34, pressure 80/46, new confusion; the patient has a pulse.",
     ["Unstable bradycardia: atropine per protocol, then pacing or an infusion; treat causes", "Stable bradycardia: observe", "Cardiac arrest: compressions", "Adenosine"], 0,
     ["Low pressure and confusion are compromise.", "Signs of compromise make it unstable.", "There is a pulse.", "Adenosine slows the heart further."], "stable-by-numbers", 6)
item("pick", A, "adult-tachy", "Heart rate 168, regular and narrow, pressure 124/78, alert, palpitations only.",
     ["Stable tachycardia: 12-lead ECG, vagal maneuvers, adenosine per protocol", "Synchronized cardioversion now", "Defibrillation", "Atropine"], 0,
     ["No compromise: stable path.", "Cardioversion is for instability.", "Defibrillation is for pulseless or polymorphic VT.", "Atropine speeds the heart."], "stable-by-numbers", 6)
item("pick", D, "hyperkalemia", "Monday, missed session, potassium 7.6 mmol/L, peaked T waves, alert with a pulse, connected.",
     ["Hyperkalemia with a pulse: calcium for ECG changes, shift, keep dialyzing", "Hyperkalemic arrest algorithm", "Stop dialysis and observe", "Wait for a repeat sample"], 0,
     ["Pulse present: protect, shift, remove.", "She is not in arrest.", "Dialysis is the cure.", "ECG changes mean treat now."], "hyperk-pulse-vs-arrest", 8)
item("pick", PD, "peds-deterioration", "A 7-year-old on dialysis is drowsy, breathing slowly, saturation 80%, heart rate falling from 120 to 70.",
     ["Respiratory failure: open the airway and bag-mask ventilate with oxygen", "Atropine", "Synchronized cardioversion", "Wait for the heart rate to fall below 60"], 0,
     ["Children usually arrest from respiratory failure; ventilation breaks the chain.", "Hypoxic bradycardia needs oxygen.", "No tachycardia.", "Act before arrest."], "peds-breathing-first", 10)
item("pick", PD, "peds-arrest", "Which pathway for a 15-year-old with signs of puberty in cardiac arrest?",
     ["Adult BLS (30:2), with doses checked against weight and adult maximums", "Infant BLS", "Child BLS with 15:2 always", "No CPR until weight is known"], 0,
     ["After puberty, adult guidance applies.", "Not an infant.", "15:2 applies before puberty.", "Never delay CPR."], "peds-adult-dose", 10)
item("pick", D, "dialysis-air", "Foam below the venous chamber, air alarm, the patient coughs and is breathless.",
     ["Stop the pump, clamp the venous line, do not return the blood, oxygen, lay flat", "Rinse back the blood", "Sit the patient up", "Override the alarm and continue"], 0,
     ["Card 5 actions.", "Rinse-back pushes air in.", "Sitting up may send air to the brain.", "Never override the detector."], "return-contaminated-blood", 7)
item("pick", D, "dialysis-anaphylaxis", "Five minutes after connection: hives, wheeze, lip swelling, pressure 82/46.",
     ["Stop the pump, clamp, do not return; IM epinephrine per protocol", "Antihistamine and continue", "Return the blood and finish", "IV epinephrine 1 mg bolus"], 0,
     ["Epinephrine first; blood not returned.", "Antihistamines do not replace epinephrine.", "The circuit carries the trigger.", "IV bolus of 1 mg is the arrest dose, dangerous with a pulse."], "epi-concentration", 9)

# ── strip + findings ──
item("strip", D, "adult-arrest", "Unresponsive, gasping, no pulse.", ["PEA: compressions and epinephrine as soon as feasible", "ROSC: post-arrest care", "Shock", "Observe"], 0,
     ["Organized rhythm without a pulse is PEA.", "ROSC needs a pulse.", "PEA is not shockable.", "No pulse means CPR."], "rhythm-equals-pulse", 3, strip={"rhythm": "normal", "rate": 70}, findings="No pulse, gasping")
item("strip", D, "post-rosc", "After CPR: strong carotid pulse, pressure 102/64.", ["ROSC: post-arrest care, pads stay on", "PEA: continue CPR", "Shock", "Asystole"], 0,
     ["A pulse and pressure confirm ROSC.", "There is a pulse.", "Not shockable.", "There is organized activity."], "rosc-check", 12, strip={"rhythm": "normal", "rate": 70}, findings="Pulse 70, BP 102/64")
item("strip", D, "adult-arrest", "Unresponsive, no pulse.", ["VF: shock, then compressions", "Asystole: epinephrine", "Atrial fibrillation: rate control", "Artifact: reattach leads"], 0,
     ["Chaotic trace with no pulse is VF.", "There is electrical activity.", "AF has a pulse.", "Artifact does not cause pulselessness."], "shock-nonshockable", 5, strip={"rhythm": "vf"}, findings="No pulse")
item("strip", A, "adult-arrest", "Talking, shivering under a blanket, pressure 130/80.", ["Artifact: check the patient and leads", "VF: shock", "Asystole", "Pulseless VT"], 0,
     ["A talking patient cannot be in VF.", "Shocking a conscious patient is dangerous.", "Not flat.", "He has a pulse."], "artifact", 3, strip={"rhythm": "vf"}, findings="Alert and talking")
item("strip", D, "adult-arrest", "Unresponsive, no pulse; flat line confirmed in two leads, gain up.", ["Asystole: CPR and epinephrine as soon as feasible", "Shock", "Pacing", "Stop resuscitation"], 0,
     ["Confirmed asystole is nonshockable.", "Nothing to defibrillate.", "Routine pacing in arrest is not recommended.", "Not a reason to stop."], "shock-nonshockable", 5, strip={"rhythm": "asystole"}, findings="No pulse; confirmed in two leads")
item("strip", A, "adult-tachy", "Pulse present, pressure 70/40, confused.", ["Unstable VT with a pulse: synchronized cardioversion", "Pulseless VT: defibrillate", "Stable: amiodarone infusion", "Adenosine for any wide rhythm"], 0,
     ["Wide regular tachycardia with a pulse and compromise.", "He has a pulse.", "Not stable.", "Adenosine only if regular, monomorphic and stable."], "stable-by-numbers", 6, strip={"rhythm": "wide", "rate": 180}, findings="Pulse present, BP 70/40, confused")
item("strip", A, "adult-arrest", "Unresponsive, no pulse.", ["Pulseless VT: defibrillate", "VT with a pulse: synchronized cardioversion", "Sinus tachycardia", "Adenosine"], 0,
     ["Pulseless VT is treated like VF.", "There is no pulse.", "Wide fast complexes are not sinus.", "Never adenosine in arrest."], "sync-unsync", 5, strip={"rhythm": "wide", "rate": 190}, findings="No pulse")
item("strip", D, "hyperkalemia", "Alert, pulse 62, missed Friday session.", ["Hyperkalemia with a pulse: protect, shift, dialyze", "Hyperkalemic arrest", "Normal ECG", "Ischemia only"], 0,
     ["Peaked T waves in a missed-session patient with a pulse.", "There is a pulse.", "Tall narrow T waves are abnormal.", "Potassium first in this story."], "hyperk-pulse-vs-arrest", 8, strip={"rhythm": "peaked", "rate": 62}, findings="Pulse present; missed session")
item("strip", D, "hyperkalemia", "Unresponsive, no pulse, missed two sessions.", ["Hyperkalemic arrest: CPR first; potassium treatment per unit protocol", "Hyperkalemia with a pulse", "VF: shock", "Asystole only"], 0,
     ["A sine-wave pattern without a pulse is hyperkalemic arrest.", "No pulse.", "Not VF.", "There is activity; cause is potassium."], "hyperk-pulse-vs-arrest", 8, strip={"rhythm": "sine", "rate": 40}, findings="No pulse")
item("strip", A, "adult-tachy", "Pulse present, irregular, 150, pressure 84/50, chest discomfort.", ["Unstable AF: synchronized cardioversion (initial energy at least 200 J reasonable)", "Adenosine", "Observe", "Defibrillation unsynchronized"], 0,
     ["Irregular, no P waves, unstable.", "Adenosine does not treat AF.", "Unstable needs treatment now.", "Use sync with a pulse."], "sync-unsync", 6, strip={"rhythm": "irregular", "rate": 150}, findings="Pulse present, BP 84/50, chest discomfort")
item("strip", A, "adult-brady", "Pulse 38, pressure 128/76, alert, no symptoms.", ["Stable bradycardia: monitor and find the cause", "Unstable: pace now", "Cardiac arrest", "Atropine 3 mg at once"], 0,
     ["No compromise: monitor and look for causes such as potassium and drugs.", "Not unstable.", "There is a pulse.", "Not indicated, and not as a single 3 mg dose."], "stable-by-numbers", 6, strip={"rhythm": "normal", "rate": 38}, findings="Pulse 38, BP 128/76, alert")
item("strip", A, "adult-tachy", "Pulse present, alert, pressure 120/70.", ["Stable regular narrow tachycardia (SVT): vagal maneuver, adenosine per protocol", "Unstable: cardiovert", "VT", "Sinus rhythm"], 0,
     ["Stable regular narrow tachycardia.", "No compromise.", "Narrow complexes.", "Too fast and no P waves."], "stable-by-numbers", 6, strip={"rhythm": "svt", "rate": 176}, findings="Pulse present, BP 120/70, alert")
item("strip", PD, "peds-brady", "8-year-old, pulse 52, mottled, weak pulses, despite good bag-mask ventilation with oxygen.", ["Start pediatric CPR", "Atropine only", "Observe", "Synchronized cardioversion"], 0,
     ["Under 60 with compromise despite effective oxygenated ventilation: CPR (PALS COR 1).", "Hypoxic bradycardia does not respond to atropine alone.", "Arrest is near.", "Not a tachycardia."], "peds-breathing-first", 10, strip={"rhythm": "normal", "rate": 52}, findings="Pulse 52, mottled, despite effective ventilation")

# ── missing assessment ──
item("missing", A, "adult-tachy", "The monitor shows a wide, fast, regular rhythm. Before choosing treatment, what must you check?",
     ["Whether there is a pulse", "The potassium result", "The dry weight", "The dialysis fluid temperature"], 0,
     ["Pulse decides arrest vs tachycardia algorithm.", "Later.", "Irrelevant now.", "Irrelevant now."], "rhythm-equals-pulse", 3)
item("missing", A, "adult-arrest", "A patient is slumped and the monitor shows sinus rhythm at 80. What do you check first?",
     ["Breathing and a definite pulse together", "The blood pressure cuff", "Glucose", "The machine alarms"], 0,
     ["Breathing and pulse place the patient.", "Cuffs can wait.", "Later.", "Later."], "rhythm-equals-pulse", 3)
item("missing", A, "post-rosc", "After an organized rhythm appears at a rhythm check, what confirms ROSC?",
     ["A definite pulse and a measurable blood pressure", "The rhythm alone", "The patient&rsquo;s color", "Time elapsed"], 0,
     ["ROSC is clinical.", "May be PEA.", "Unreliable.", "Irrelevant."], "rosc-check", 12)
item("missing", A, "adult-tachy", "A tachycardia with a pulse at 160. Which assessment decides between cardioversion and drugs?",
     ["Signs of instability: low pressure, altered mental status, shock, chest pain, heart failure", "The heart rate number", "The patient&rsquo;s age", "The time of day"], 0,
     ["Stability decides.", "Rate alone does not.", "Not decisive.", "Irrelevant."], "stable-by-numbers", 6)
item("missing", D, "dialysis-arrest", "Before deciding to return the circuit blood in an arrest, what must the circuit nurse check?",
     ["Air, hemolysis, a severe reaction, or an open line end", "The dialyzer brand", "The patient&rsquo;s billing status", "The water room logbook"], 0,
     ["These forbid returning the blood.", "Irrelevant.", "Irrelevant.", "Not at this moment."], "return-contaminated-blood", 7)
item("missing", PD, "peds-arrest", "Before giving a pediatric epinephrine dose, what must be read aloud and confirmed?",
     ["Weight, dose in mg, volume in mL, and concentration", "Only the volume", "Only the drug name", "The parents&rsquo; names"], 0,
     ["All four prevent tenfold errors.", "Volume without concentration is unsafe.", "Not enough.", "Irrelevant."], "epi-concentration", 11)

# ── order the steps ──
item("order", D, "adult-arrest", "Put the first actions of an arrest on the machine in order.",
     ["Shock if shockable", "Recognize and call the code", "Compressions with the chair flat", "Pads on", "Epinephrine when due"], [1, 2, 3, 0, 4],
     "Recognize and call; compress; pads; shock a shockable rhythm; drugs when due. The circuit nurse stops fluid removal in parallel.", "pause-for-machine", 4)
item("order", D, "dialysis-arrest", "Order the circuit nurse&rsquo;s actions in an arrest with no circuit cause.",
     ["Make the access safe for drugs", "Stop fluid removal", "Announce the blood decision", "Check for air, hemolysis, reaction, open line", "Return the blood or clamp and disconnect"], [1, 3, 4, 2, 0],
     "Stop fluid removal; check for a circuit cause; return or clamp; announce; prepare the access.", "return-contaminated-blood", 7)
item("order", D, "hyperkalemia", "Order the treatment of hyperkalemia with a pulse and ECG changes.",
     ["Remove (dialysis)", "Protect (IV calcium)", "Shift (insulin with glucose, salbutamol)", "Glucose checks for hours"], [1, 2, 0, 3],
     "Protect, shift, remove, then monitor glucose after insulin.", "hyperk-pulse-vs-arrest", 8)
item("order", PD, "peds-deterioration", "Order the steps for a child whose breathing is failing.",
     ["Compressions if HR stays under 60 with poor perfusion", "Open the airway and bag-mask with oxygen", "Call for help and the pediatric cart", "Epinephrine if compromise persists after hypoxia is corrected"], [2, 1, 0, 3],
     "Call; ventilate; compress if needed; epinephrine if compromise persists.", "peds-breathing-first", 10)
item("order", D, "post-rosc", "Order the first actions after ROSC.",
     ["Hand over with dialysis facts", "Confirm pulse and pressure, pads on", "Oxygen to 90 to 98% and MAP at least 65", "12-lead ECG, glucose, potassium"], [1, 2, 3, 0],
     "Confirm; stabilize; test; hand over.", "rosc-check", 12)

# ── unsafe action ──
item("unsafe", D, "dialysis-arrest", "Which action is unsafe during an arrest on the machine?",
     ["Returning the blood after foam is seen in the venous line", "Stopping fluid removal", "Securing the venous needle for drugs", "Clamping and disconnecting"], 0,
     ["Returning blood after air pushes air in.", "Correct.", "Correct.", "Acceptable."], "return-contaminated-blood", 7)
item("unsafe", D, "dialysis-arrest", "Which is unsafe before a shock?",
     ["The circuit nurse holding the blood lines during the shock", "Wiping a wet chair", "Pads on dry skin away from the access arm", "Disconnecting a machine not rated defibrillation-proof"], 0,
     ["Lines touch the patient and can carry current.", "Safe.", "Safe.", "Safe."], "pause-for-machine", 7)
item("unsafe", PD, "peds-arrest", "Which is unsafe for a 20 kg child in arrest?",
     ["2 mL of 1 mg/mL epinephrine IV", "2 mL of 0.1 mg/mL epinephrine IV", "First shock 40 J", "Compressions one-third of chest depth"], 0,
     ["That is 2 mg, ten times the dose.", "Correct dose (0.2 mg).", "2 J/kg.", "Correct."], "epi-concentration", 11)
item("unsafe", D, "hyperkalemia", "Which is unsafe in a stable, connected patient with potassium 7.0 and peaked T waves?",
     ["Stopping dialysis and sending him home to return tomorrow", "IV calcium per order set", "Insulin with glucose and glucose checks", "Calling the attending nephrologist"], 0,
     ["Removes the definitive treatment.", "Appropriate.", "Appropriate.", "Appropriate."], "stop-dialysis-hyperk", 8)
item("unsafe", A, "adult-tachy", "Which is unsafe for unstable polymorphic VT with a pulse?",
     ["Synchronized cardioversion at low energy", "Unsynchronized high-energy shock", "Calling for help", "Preparing for arrest"], 0,
     ["The device may not synchronize to changing QRS shapes; use defibrillation.", "Correct.", "Correct.", "Correct."], "sync-unsync", 6)
item("unsafe", D, "dialysis-anaphylaxis", "Which is unsafe in severe anaphylaxis on dialysis?",
     ["Pushing the 1 mg/mL ampule IV as a bolus", "IM epinephrine into the outer thigh", "Stopping the pump and clamping", "Keeping the dialyzer for review"], 0,
     ["A tenfold-concentration IV bolus with a pulse is dangerous.", "Correct.", "Correct.", "Correct."], "epi-concentration", 9)

# ── evolving cases ──
item("evolve", D, "transitions", "A patient with unstable bradycardia (HR 34, BP 78/40) becomes unresponsive and gasping; no pulse. Which algorithm now?",
     ["Cardiac arrest: compressions now", "Keep pacing", "More atropine", "Synchronized cardioversion"], 0,
     ["Pulse lost: arrest.", "Pacing belongs to bradycardia with a pulse; routine pacing in arrest is not recommended.", "Not without a pulse.", "No tachycardia."], "wrong-algorithm-after-change", 2)
item("evolve", D, "transitions", "During PEA arrest, the next rhythm check shows VF.", ["Shockable path: shock", "Continue nonshockable path", "Stop CPR", "Synchronized cardioversion"], 0,
     ["Rhythm changed: shock.", "The rhythm now is shockable.", "No.", "No pulse: unsynchronized."], "wrong-algorithm-after-change", 5)
item("evolve", D, "transitions", "Ten minutes after ROSC the patient loses the pulse again.", ["Re-arrest: compressions within seconds", "Recheck the pressure cuff", "Restart dialysis", "Give fluids and wait"], 0,
     ["Re-arrest: arrest algorithm.", "Delay.", "Never.", "CPR first."], "wrong-algorithm-after-change", 12)
item("evolve", D, "transitions", "A stable SVT (BP 120/70) becomes BP 74/40 with confusion after adenosine.", ["Now unstable: synchronized cardioversion", "Repeat adenosine and wait", "Observe", "Unsynchronized shock"], 0,
     ["Instability changes the path.", "Do not delay.", "Unsafe.", "Use sync with a pulse."], "wrong-algorithm-after-change", 6)
item("evolve", PD, "transitions", "A child&rsquo;s heart rate rose with ventilation, then falls to 48 with poor perfusion despite good ventilation.", ["Pediatric CPR", "Continue ventilation only", "Synchronized cardioversion", "Wait for 40"], 0,
     ["Under 60 with compromise despite ventilation: CPR.", "Not enough now.", "No.", "Threshold is 60."], "wrong-algorithm-after-change", 10)
item("evolve", D, "transitions", "Hyperkalemia with a pulse (connected, dialyzing) progresses to a sine wave and no pulse.", ["Hyperkalemic arrest: CPR first, then potassium per protocol", "Continue the shift treatments only", "Increase blood flow", "Wait for the result"], 0,
     ["Arrest comes first.", "Not without a pulse.", "No.", "No."], "hyperk-pulse-vs-arrest", 8)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for it in I:
        if it["type"] == "order":
            assert sorted(it["answer"]) == list(range(len(it["options"]))), it["id"]
        else:
            assert 0 <= it["answer"] < len(it["options"]) and len(it["why"]) == len(it["options"]), it["id"]
        assert it["tag"] in TAGS, it["id"]
        if it["type"] == "strip":
            assert it.get("findings"), it["id"] + ": strip items need clinical findings"
    OUT.write_text(json.dumps({"tags": TAGS, "items": I}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(I)} recognition items")


if __name__ == "__main__":
    main()
