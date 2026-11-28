# -*- coding: utf-8 -*-
"""Interactive megacodes for the Dialysis Team Resuscitation Lab (16 cases). Writes data/academy-cases/rl-*.json in the
apply_cases.py schema, plus a "lab" block read by the Practice Lab (timed mode and facilitator recorder).
Run from the repo root:  python3 tools/techcourses/resus/cases.py
Every decision node sits on every path (weaker choices show their consequence and rejoin). Clinical content follows the
module text and the signed-off Emergency Quick Cards; deterministic only. Signed off by Dr. Rivero, November 28, 2026.
Every name and identifier is fictional."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "academy-cases"
P = "resuscitation-lab-"
NOTE = ("Fictional patient. Doses and energies are quoted from the 2025 AHA guidelines (and the ERC "
        "where named) for recognition; your unit protocol, crash-cart stock and the attending nephrologist come first. Simulation success "
        "is an educational result, not a prediction of patient survival.")
LBL = {"uf": "Fluid removal", "pump": "Blood pump", "ecg": "Rhythm", "k": "Potassium", "glucose": "Glucose", "line": "Venous line",
       "cpr": "CPR", "etco2": "ETCO2", "access": "Access"}


def ch(grade, text, feedback, nxt, then=None, vitals=None):
    c = {"grade": grade, "text": text, "feedback": f"<p>{feedback}</p>", "next": nxt}
    if then:
        c["then"] = f"<p>{then}</p>"
    if vitals:
        c["vitals"] = vitals
    return c


def node(short, scene, prompt, choices, vitals=None):
    n = {"short": short, "scene": f"<p>{scene}</p>" if scene else "", "prompt": prompt, "choices": choices}
    if vitals:
        n["vitals"] = vitals
    return n


def end(title, text, vitals=None):
    e = {"end": True, "title": title, "text": f"<p>{text}</p>"}
    if vitals:
        e["vitals"] = vitals
    return e


def debrief(points):
    return "<h4>What this case teaches</h4><ul>" + "".join(f"<li><b>{a}</b> {b}</li>" for a, b in points) + "</ul>"


CASES = []


def case(cid, page, title, monitor, intro, nodes, deb, lab, order=None, labels=None):
    d = {"id": cid, "page": P + page + ".html", "title": title,
         "decisions": sum(1 for n in nodes.values() if "choices" in n), "monitorTitle": "Station monitor", "note": NOTE,
         "labels": dict(LBL, **(labels or {})), "monitorOrder": order or ["time", "bp", "hr", "spo2", "ecg", "uf", "pump", "k"],
         "monitor": monitor, "intro": intro, "start": "n1", "nodes": nodes, "debrief": deb, "lab": lab}
    CASES.append(d)


# ─────────────────────────── 01 Readiness ───────────────────────────
case("rl01-five-forty", "01-readiness-before-collapse", "The 5:40 a.m. check",
     {"time": "Mon 5:40 a.m.", "bp": "—", "hr": "—", "spo2": "—", "ecg": "Defibrillator self-test: battery warning", "rhythm": "asystole",
      "rhythmLabel": "Defibrillator screen (no patient)", "alarm": ["ecg"]},
     "<p>You are the charge nurse at an 18-station freestanding unit in Caloocan. The first shift connects at 6:00. Opening the crash cart with the technician, you find a defibrillator battery warning, adult pads that expired last month, and an oxygen cylinder about a quarter full. Today&rsquo;s list includes a patient who missed Friday after a hospital stay. The physician-on-duty arrives at 6:20.</p>",
     {"n1": node("5:40 a.m.", "", "What do you do about the defibrillator and pads?", [
         ch("best", "Treat it as a stop-and-fix item: charge or swap the battery, get in-date pads from stock or a sister unit, and call the Dialysis Clinical Head now.", "A unit without a working defibrillator cannot treat a shockable arrest. Fixing it before connection and escalating the same morning is the readiness standard.", "n2", vitals={"ecg": "Spare battery in; new pads"}),
         ch("poor", "Write it in the logbook for the biomedical technician and start the shift.", "Logging leaves the risk in place all day. Clinic registries show staff applied a defibrillator before EMS in only about half of arrests; a dead one helps nobody.", "n2", then="At 5:50 you reconsider, send the technician for a spare battery and pads, and call the clinical head.", vitals={"ecg": "Spare battery in; new pads"}),
         ch("harmful", "Use the expired pads; they usually work.", "Expired gel can fail to conduct, causing a failed shock or a burn. In-date pads are part of the morning check.", "n2", then="The technician refuses and brings fresh pads from the sister unit.", vitals={"ecg": "Spare battery in; new pads"})]),
      "n2": node("5:52 a.m.", "The defibrillator now passes its self-test with fresh pads. The oxygen cylinder still reads a quarter full.", "What about the oxygen?", [
          ch("best", "Swap it for a full cylinder before 6:00 and check the planner: a quarter cylinder will not last a 30-minute transfer at high flow.", "Oxygen for transfer is part of readiness. The toolkit&rsquo;s oxygen planner turns the gauge reading into minutes.", "n3"),
          ch("ok", "Keep it but put a full cylinder on order for the afternoon.", "Better than nothing, but an arrest before noon would start with too little oxygen.", "n3", then="You decide to swap it now after all."),
          ch("poor", "Oxygen is not needed for dialysis; leave it.", "Resuscitation and transfer depend on oxygen. A low cylinder is a failed check.", "n3", then="The technician swaps the cylinder anyway.")]),
      "n3": node("5:55 a.m.", "Six staff are on the roster: two ACLS-current nurses, two nurses with BLS, a technician and a nurse assistant.", "How do you set up the code roles?", [
          ch("best", "A two-minute huddle: leader until the physician arrives (an ACLS nurse), two compressors, circuit nurse, recorder, runner who calls the ambulance, and a watcher who never joins. Seat the high-risk patient in view of the cart.", "Named roles from the real roster prevent the &ldquo;who does what?&rdquo; delay. The watcher protects the other patients.", "end"),
          ch("ok", "Tell staff to &ldquo;help as needed&rdquo; if anything happens.", "Unnamed roles invite crowding and gaps, and the other patients go unwatched.", "end", then="During the huddle you name the roles after all."),
          ch("poor", "Wait for the physician-on-duty at 6:20 to assign roles.", "The first 20 minutes are the riskiest of the week for the Monday patient; roles must exist before the first connection.", "end", then="You assign roles at 5:58 instead.")]),
      "end": end("6:00 a.m.", "The defibrillator works, the oxygen is full, the roles are named, and the clinical head knows what failed. The Monday patient sits at Station 2, in front of the cart. Nothing happened today; that was the point.")},
     debrief([("Fix before you start.", "A failed defibrillator, pads or oxygen check is a stop-and-fix item, escalated the same morning."),
              ("Read the list for risk.", "Monday, missed sessions, low-potassium baths and recent discharge are arrest flags."),
              ("Name roles from the real roster,", "including a watcher who never joins the arrest.")]),
     {"algorithm": "readiness", "set": ["adult", "dialysis"], "budget": 45})

# ─────────────────────────── 02 Box by box ───────────────────────────
case("rl02-box-by-box", "02-algorithm-foundations", "Box by box: one patient, three algorithms",
     {"time": "10:15 a.m.", "bp": "78/40", "hr": 38, "spo2": 94, "ecg": "Sinus bradycardia", "uf": "On", "pump": "Running",
      "rhythm": "normal", "rhythmLabel": "Slow narrow rhythm", "alarm": ["bp", "hr"]},
     "<p>Mrs. Remedios Aquino, 72, on a beta-blocker, is two hours into dialysis in Iloilo City. She is drowsy but opens her eyes to her name. You are the physician-on-duty, just arrived with the defibrillator.</p>",
     {"n1": node("10:15", "", "Which algorithm is she in, and what is your first move?", [
         ch("best", "Bradycardia with a pulse, unstable (low pressure, drowsy): monitor and pads on, oxygen, IV access, atropine per protocol, and look for causes (potassium, the beta-blocker).", "Five questions: responsive (barely), breathing, definite pulse, not an arrest rhythm, unstable. That places her in unstable bradycardia.", "n2", vitals={"uf": "Off"}),
         ch("poor", "Cardiac arrest: start compressions.", "She has a pulse and responds. Compressions are for absent circulation.", "n2", then="A nurse feels a pulse and stops you. You treat unstable bradycardia.", vitals={"uf": "Off"}),
         ch("poor", "Intradialytic hypotension: saline bolus and observe.", "A heart rate of 38 with drowsiness is a rhythm problem first; fluid alone misses the cause.", "n2", then="You see the rate and treat unstable bradycardia.", vitals={"uf": "Off"})]),
      "n2": node("10:19", "While pads go on and atropine is drawn up, she stops answering. Slow gasps. No definite carotid pulse in 10 seconds.", "What do you say?", [
          ch("best", "&ldquo;No pulse. Cardiac arrest. Compressions now, chair flat.&rdquo; Stop the pacing plan; the recorder notes the time.", "Announcing the transition closes the old plan for everyone at once.", "n3",
             vitals={"time": "10:19", "bp": "—", "hr": "0", "stripRate": 30, "spo2": "—", "ecg": "Slow wide complexes, no pulse", "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, no pulse", "cpr": "Running", "alarm": ["bp", "ecg", "hr"]}),
          ch("harmful", "&ldquo;Increase the pacer current and give another atropine.&rdquo;", "Pacing and atropine belong to bradycardia with a pulse. Without a pulse, only compressions move blood.", "n3", then="Thirty seconds later the recorder says no one has checked a pulse. You call the arrest.",
             vitals={"time": "10:20", "bp": "—", "hr": "0", "stripRate": 30, "spo2": "—", "ecg": "Slow wide complexes, no pulse", "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, no pulse", "cpr": "Running", "alarm": ["bp", "ecg", "hr"]}),
          ch("poor", "Wait for the atropine to work before deciding.", "Gasping without a pulse is cardiac arrest now; waiting withholds compressions.", "n3", then="You start compressions a minute later.",
             vitals={"time": "10:20", "bp": "—", "hr": "0", "stripRate": 30, "spo2": "—", "ecg": "Slow wide complexes, no pulse", "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, no pulse", "cpr": "Running", "alarm": ["bp", "ecg", "hr"]})]),
      "n3": node("10:20", "Compressions are running. The monitor shows organized slow wide complexes.", "Which arrest path, and which cause do you raise first?", [
          ch("best", "Nonshockable (PEA): epinephrine as soon as feasible, two-minute cycles, and treat potassium and the beta-blocker as likely causes (BRASH), per protocol.", "Organized electricity without a pulse is PEA. In a dialysis patient on a beta-blocker, potassium and the drug together top the cause list.", "n4", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("poor", "Shock it.", "PEA is not shockable; a shock wastes time and pauses compressions.", "n4", then="The leader corrects the path to nonshockable.", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("ok", "Nonshockable path, but look for causes later once the physician has time.", "The path is right, but in PEA finding the cause is the treatment; ask now.", "n4", then="You raise potassium at the next cycle.", vitals={"pump": "Stopped", "line": "Blood returned"})]),
      "n4": node("10:31", "After epinephrine and potassium treatment per protocol, the rhythm check shows a narrow rhythm at 72. A nurse feels a strong carotid pulse; pressure 96/60.",
                 "Which algorithm now?", [
          ch("best", "Post-ROSC care: keep pads on, oxygen titrated, MAP target, 12-lead ECG, glucose and potassium, call the attending nephrologist and the transfer.", "A definite pulse and pressure is ROSC: the third algorithm in ten minutes. Pads stay on because re-arrest is common.", "end",
             vitals={"time": "10:31", "bp": "96/60", "hr": 72, "spo2": 95, "ecg": "Sinus rhythm", "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "cpr": "Stopped", "alarm": []}),
          ch("poor", "Keep compressing until the ambulance arrives.", "Compressing over a strong pulse is unnecessary; reassessment exists to catch this change.", "end", then="The recorder points out the pulse; compressions stop.",
             vitals={"time": "10:32", "bp": "96/60", "hr": 72, "spo2": 95, "ecg": "Sinus rhythm", "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "cpr": "Stopped", "alarm": []})]),
      "end": end("10:45", "Mrs. Aquino is transferred with a pulse after passing through three algorithms: unstable bradycardia, PEA arrest, and post-ROSC care. Each transition was announced aloud.")},
     debrief([("Five questions place the patient;", "ask them again at every reassessment."),
              ("Announce transitions aloud.", "&ldquo;No pulse, cardiac arrest&rdquo; closes the previous plan."),
              ("Slow rhythm plus a rate-slowing drug in a dialysis patient", "means potassium and BRASH until proven otherwise.")]),
     {"algorithm": "transitions", "set": ["adult", "dialysis"], "budget": 30})

# ─────────────────────────── 03 Another low BP ───────────────────────────
case("rl03-another-low-bp", "03-algorithm-recognition", "&ldquo;It looks like another low BP&rdquo;",
     {"time": "3:20 p.m.", "bp": "72/40", "hr": 64, "spo2": "—", "ecg": "Regular narrow rhythm", "uf": "On", "pump": "Running",
      "rhythm": "normal", "rhythmLabel": "Regular narrow rhythm, 64/min", "alarm": ["bp"]},
     "<p>Mr. Danilo Reyes, 59, often has low pressure in his last hour of dialysis in Davao City. The pressure alarm sounds. He is slumped, eyes half open, with a snoring breath every few seconds. A colleague says, &ldquo;Another low BP. Legs up, saline bolus?&rdquo;</p>",
     {"n1": node("3:20", "", "What do you check first?", [
         ch("best", "Breathing and a definite pulse together, within 10 seconds.", "Slumped and snoring every few seconds may be agonal breathing. Breathing and pulse separate arrest from hypotension.", "n2", vitals={"hr": "No pulse", "alarm": ["bp", "hr"]}),
         ch("poor", "Give a saline bolus through the circuit first.", "Treating the pressure first can waste the critical minute of an arrest.", "n2", then="As the saline runs, you check: no definite pulse.", vitals={"hr": "No pulse", "alarm": ["bp", "hr"]}),
         ch("poor", "Look at the monitor: the rhythm is regular, so he has a circulation.", "A regular rhythm on the monitor cannot prove a pulse.", "n2", then="You feel the neck anyway: no pulse.", vitals={"hr": "No pulse", "alarm": ["bp", "hr"]})]),
      "n2": node("3:21", "No definite pulse. The snoring breaths are irregular gasps. The monitor still shows a regular narrow rhythm at 64.", "What is this, and what do you say?", [
          ch("best", "&ldquo;Not breathing normally, no pulse: code! Chair flat, compressions.&rdquo; Pulseless electrical activity.", "Gasping without a pulse is cardiac arrest; organized rhythm without a pulse is PEA.", "n3", vitals={"bp": "—", "cpr": "Running", "uf": "Off", "rhythmLabel": "Organized rhythm, no pulse (PEA)"}),
          ch("harmful", "Respiratory arrest: give breaths only.", "There is no pulse, so this is cardiac arrest. Breaths alone do not circulate blood.", "n3", then="A second nurse confirms no pulse and starts compressions.", vitals={"bp": "—", "cpr": "Running", "uf": "Off", "rhythmLabel": "Organized rhythm, no pulse (PEA)"}),
          ch("poor", "Recheck the blood pressure cuff first.", "A cuff reading does not change a pulseless patient&rsquo;s algorithm.", "n3", then="Compressions start 30 seconds later.", vitals={"bp": "—", "cpr": "Running", "uf": "Off", "rhythmLabel": "Organized rhythm, no pulse (PEA)"})]),
      "n3": node("3:22", "Compressions are running. The circuit nurse has stopped fluid removal. There is no air, no abnormal blood color, and the lines are intact.", "Which causes do you raise for this late-session PEA?", [
          ch("best", "Hypovolemia from fluid removal, bleeding at the access (lift the blanket), low potassium or calcium from the bath, then the rest; saline through the circuit per protocol.", "Late-session arrest points to volume and falling electrolytes; PEA is treated by finding the cause.", "n4", vitals={"pump": "Stopped", "line": "Blood returned + saline"}),
          ch("ok", "High potassium first, as in every dialysis arrest.", "Potassium is always on the list, but late in the session volume and low electrolytes are more likely.", "n4", then="The leader adds volume and the access check.", vitals={"pump": "Stopped", "line": "Blood returned + saline"}),
          ch("poor", "None: give drugs and wait.", "In PEA the cause is often the only way back.", "n4", then="You lift the blanket: the access is dry. You give saline per protocol.", vitals={"pump": "Stopped", "line": "Blood returned + saline"})]),
      "n4": node("3:30", "After epinephrine and saline through the circuit, the next rhythm check shows a narrow rhythm at 98 with a palpable pulse; pressure 88/52.", "What next?", [
          ch("best", "ROSC: pads stay on, oxygen, pressure support per physician, ECG, glucose and potassium, call the attending and arrange transfer; dialysis not restarted.", "ROSC is a pulse and a pressure. Dialysis restarts only on the attending&rsquo;s decision.", "end",
             vitals={"time": "3:30 p.m.", "bp": "88/52", "hr": 98, "spo2": 93, "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "cpr": "Stopped", "alarm": ["bp"]}),
          ch("harmful", "Reconnect and finish the last 40 minutes of dialysis.", "Restarting a circuit in an unstable patient after arrest risks re-arrest and is the attending&rsquo;s decision.", "end", then="The physician-on-duty stops the restart and calls the attending.",
             vitals={"time": "3:31 p.m.", "bp": "88/52", "hr": 98, "spo2": 93, "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "cpr": "Stopped", "alarm": ["bp"]})]),
      "end": end("3:50 p.m.", "Mr. Reyes leaves by ambulance with a pulse. The debrief records one habit: in every slumped patient, breathing and pulse come before blood pressure.")},
     debrief([("Breathing and pulse first.", "A familiar pattern (&ldquo;another low BP&rdquo;) can hide an arrest."),
              ("The rhythm does not prove a pulse.", "Regular narrow rhythm without a pulse is PEA."),
              ("Late-session arrest:", "volume, the access, and low electrolytes lead the cause list.")]),
     {"algorithm": "recognition", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 04 Chair would not recline ───────────────────────────
case("rl04-chair", "04-bls-at-the-chair", "The chair that would not recline",
     {"time": "7:05 a.m.", "bp": "—", "hr": "No pulse", "stripRate": 200, "spo2": "—", "ecg": "Not yet attached", "uf": "On", "pump": "Running",
      "rhythm": "vf", "rhythmLabel": "Monitor not yet attached", "alarm": ["hr"]},
     "<p>You are a nurse assistant passing Station 4 in Quezon City at 7:05 a.m. Mrs. Lorna Castillo, 64, about 85 kg, has slumped forward ten minutes after connection. She does not answer, she is gasping, and you feel no pulse. You shout for help and pull the recliner lever; the backrest goes only halfway down and sticks.</p>",
     {"n1": node("7:05", "", "What do you do now?", [
         ch("best", "Start compressions where she is, as flat as the chair goes, while help comes.", "Compressions start where the patient is. A better surface is worth it only if it costs no time.", "n2", vitals={"cpr": "Running"}),
         ch("poor", "Keep working the lever until the chair is flat.", "Every second fighting the chair is a second without blood flow.", "n2", then="After 30 seconds you give up on the lever and compress.", vitals={"cpr": "Running"}),
         ch("harmful", "Pull her onto the floor by yourself while she is still connected.", "Moving a connected patient without clamping can pull out the needles; a single rescuer cannot lift 85 kg safely.", "n2", then="A nurse stops you; you compress in the chair.", vitals={"cpr": "Running"})]),
      "n2": node("7:06", "Two nurses arrive with the cart. One says, &ldquo;Let us move her to the floor.&rdquo;", "What is the best plan?", [
          ch("best", "Keep compressing; one nurse tries the CPR release or slides a backboard; the circuit nurse stops the pump and clamps before any move; move only with four people on a count.", "A firm surface helps only if it does not delay compressions, and the circuit must be safe before moving.", "n3", vitals={"uf": "Off", "pump": "Stopped", "line": "Clamped"}),
          ch("poor", "Stop compressions and move her now.", "Stopping for an unplanned move costs a minute of no flow and risks the access.", "n3", then="The move takes 50 seconds without compressions; the leader restarts CPR on the floor.", vitals={"uf": "Off", "pump": "Stopped", "line": "Clamped"})]),
      "n3": node("7:07", "Pads go on. The AED analyzes and advises a shock.", "What happens around the shock?", [
          ch("best", "&ldquo;Everyone clear: patient, chair, lines, machine.&rdquo; Shock, then compressions immediately, no pulse check.", "Resume compressions immediately after a shock (COR 2a, LOE B-R); clear the lines and machine in a dialysis unit.", "n4",
             vitals={"ecg": "AED: shock delivered", "rhythmLabel": "Shockable rhythm", "time": "7:07 a.m."}),
          ch("poor", "Shock, then check the pulse for 10 seconds.", "A post-shock pulse check adds a pause when the heart is stunned; compress first.", "n4", then="The leader calls for compressions after the pause.", vitals={"ecg": "AED: shock delivered", "time": "7:07 a.m."}),
          ch("harmful", "Shock while the circuit nurse keeps holding the blood lines.", "Anything touching the patient during a shock can carry current to staff.", "n4", then="The AED pauses; the nurse lets go; the shock is delivered.", vitals={"ecg": "AED: shock delivered", "time": "7:08 a.m."})]),
      "n4": node("7:09", "Compressions continue. Your arms are burning after two minutes.", "What now?", [
          ch("best", "Swap with the next compressor at the rhythm check, standing ready beside the chair.", "Depth falls with fatigue before you feel it; swap every two minutes.", "end"),
          ch("ok", "Keep going until you cannot continue.", "Quality drops before you notice.", "end", then="The leader swaps you at the next check.")]),
      "end": end("7:20 a.m.", "The physician-on-duty arrives and leads the rest of the arrest. The stuck recliner is tagged out, and every chair&rsquo;s CPR position is added to tomorrow&rsquo;s morning check.")},
     debrief([("Compress where the patient is.", "Improve the surface only if it costs no time."),
              ("Clamp before any move.", "The circuit nurse makes the lines safe first."),
              ("Clear patient, chair, lines and machine;", "compress immediately after the shock.")]),
     {"algorithm": "adult-bls", "set": ["adult", "dialysis"], "budget": 15})

# ─────────────────────────── 05 Collapse at Station 7 ───────────────────────────
VF = {"rhythm": "vf", "rhythmLabel": "Ventricular fibrillation", "hr": "No pulse", "stripRate": 220, "bp": "—", "spo2": "—", "ecg": "VF"}
case("rl05-station-7", "05-adult-cardiac-arrest", "Collapse at Station 7",
     dict(VF, time="9:40 a.m.", uf="On", pump="Running", cpr="Starting", alarm=["hr", "ecg"]),
     "<p>Tuesday, 9:40 a.m., freestanding unit in Pasig. Mr. Arnel Gutierrez, 61, two hours into dialysis, collapses: unresponsive, not breathing, no pulse. The physician-on-duty stepped out to the pharmacy next door. You are the ACLS-current nurse leading until she returns. Compressions start within 15 seconds; pads go on at 40 seconds. The screen shows a chaotic trace.</p>",
     {"n1": node("9:41", "", "First rhythm check. What do you do?", [
         ch("best", "VF: &ldquo;Charging, continue compressions. Everyone clear: patient, chair, lines, machine. Shock.&rdquo; Compressions immediately.", "VF is shockable; shock early and resume compressions at once.", "n2", vitals={"time": "9:41 a.m.", "uf": "Off"}),
         ch("poor", "Wait for the physician-on-duty before shocking.", "A trained nurse defibrillates per protocol; waiting lowers the chance of success with each minute.", "n2", then="You shock 90 seconds later.", vitals={"time": "9:43 a.m.", "uf": "Off"}),
         ch("harmful", "Give epinephrine first, then shock.", "On the shockable path, the shock comes first; epinephrine follows failed initial shocks.", "n2", then="You shock after the drug.", vitals={"time": "9:42 a.m.", "uf": "Off"})]),
      "n2": node("9:43", "Second rhythm check: still VF. Second shock delivered; compressions resume.", "What about epinephrine now?", [
          ch("best", "Epinephrine 1 mg IV through the secured venous needle (circuit nurse confirms), then every 3 to 5 minutes; the recorder calls the time.", "After initial shocks fail, epinephrine 1 mg every 3 to 5 minutes is reasonable (COR 2a).", "n3", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("poor", "Give epinephrine at every two-minute check.", "Every 2 minutes is too often; every other cycle keeps 3 to 5 minutes.", "n3", then="The recorder corrects the interval.", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("harmful", "Give 5 mg of epinephrine to make up for lost time.", "High-dose epinephrine is not recommended (COR 3: No Benefit).", "n3", then="The drug nurse reads back and the leader corrects to 1 mg.", vitals={"pump": "Stopped", "line": "Blood returned"})]),
      "n3": node("9:47", "Third check: VF persists after three shocks and one epinephrine. The physician-on-duty returns.", "What happens now?", [
          ch("best", "15-second summary and &ldquo;You have the lead.&rdquo; Shock again; consider amiodarone 300 mg (or lidocaine) per protocol; review causes aloud.", "Shock-refractory VF: amiodarone or lidocaine may be considered (COR 2b). A clean leadership handover keeps one voice.", "n4", vitals={"time": "9:47 a.m."}),
          ch("poor", "Both of you give orders until it settles.", "Two leaders cause duplicated and missed actions.", "n4", then="The physician asks for a summary and takes the lead.", vitals={"time": "9:48 a.m."}),
          ch("poor", "Routine calcium and bicarbonate for every dialysis arrest.", "Routine calcium and bicarbonate are not recommended; give them only for a specific cause per protocol.", "n4", then="The physician asks for the last potassium first.", vitals={"time": "9:48 a.m."})]),
      "n4": node("9:51", "After the fourth shock and amiodarone, the rhythm check shows organized narrow complexes at 88.", "What do you do?", [
          ch("best", "Feel for a definite pulse within 10 seconds; a pulse and pressure mean ROSC; no pulse means PEA and compressions resume.", "An organized rhythm needs a pulse check; the rhythm alone does not mean circulation.", "end",
             vitals={"time": "9:51 a.m.", "hr": 88, "bp": "92/58", "spo2": 94, "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "ecg": "Sinus", "cpr": "Stopped", "alarm": []}),
          ch("poor", "Stop CPR: the rhythm is back.", "Stopping without a pulse check risks leaving PEA untreated.", "end", then="A nurse feels for a pulse: present, pressure 92/58.",
             vitals={"time": "9:52 a.m.", "hr": 88, "bp": "92/58", "spo2": 94, "rhythm": "normal", "rhythmLabel": "Sinus rhythm with a pulse", "ecg": "Sinus", "cpr": "Stopped", "alarm": []})]),
      "end": end("10:05 a.m.", "Mr. Gutierrez has ROSC and is handed over to the ambulance with the recorder&rsquo;s sheet, a 12-lead ECG, and the dialysis facts.")},
     debrief([("Shock VF early;", "compress immediately after."), ("Epinephrine after the initial shocks fail,", "then every 3 to 5 minutes, 1 mg."),
              ("Refractory VF:", "amiodarone or lidocaine may be considered; no routine calcium or bicarbonate."),
              ("ROSC is a pulse and a pressure.", "")]),
     {"algorithm": "adult-arrest", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 06a Slow rhythm ───────────────────────────
case("rl06-slow", "06-peri-arrest-rhythms", "Slow rhythm, worsening perfusion",
     {"time": "Mon 6:20 a.m.", "bp": "82/50", "hr": 36, "spo2": 95, "ecg": "Slow wide-looking rhythm", "k": "Pending (40 min)", "uf": "Not started", "pump": "Not connected",
      "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, 36/min", "alarm": ["bp", "hr"]},
     "<p>Mrs. Teresita Morales, 69, takes a beta-blocker and amlodipine, had diarrhea over the weekend, and arrives on Monday weak and dizzy in Cebu City. Heart rate 36, pressure 82/50, pale and slow to answer. You are the physician-on-duty. The potassium result will take 40 minutes.</p>",
     {"n1": node("6:20", "", "Is she stable, and what do you suspect?", [
         ch("best", "Unstable bradycardia (low pressure, slow responses); suspect hyperkalemia plus the beta-blocker together (BRASH), triggered by dehydration.", "Stability is judged by signs; a slow rhythm in a dialysis patient on an AV-nodal drug is potassium until proven otherwise.", "n2"),
         ch("poor", "Stable: the rate is slow but she is talking.", "Low pressure and slow responses are signs of compromise.", "n2", then="Her pressure falls to 78/44; you treat her as unstable."),
         ch("poor", "Beta-blocker overdose only: hold the drug and observe.", "The dose is usual; potassium and the drug together are the likely mechanism.", "n2", then="You add potassium to the plan.")]),
      "n2": node("6:22", "Pads are on; pacing is ready.", "What is your treatment plan now?", [
          ch("best", "Atropine 1 mg per protocol (without delaying the rest), IV calcium and insulin with glucose per order set, cautious saline, pacing or an epinephrine infusion if no response; call the attending about urgent dialysis.", "Treat the rate and the potassium together; atropine often works poorly in potassium- and drug-driven block.", "n3",
             vitals={"time": "6:30 a.m.", "hr": 44, "bp": "88/54", "rhythmLabel": "Slow rhythm, improving"}),
          ch("poor", "Atropine every 3 minutes until the rate rises, nothing else yet.", "Atropine alone may fail and delays potassium treatment; the maximum is 3 mg.", "n3", then="After 3 mg with no change, you give calcium and insulin and prepare to pace.",
             vitals={"time": "6:35 a.m.", "hr": 40, "bp": "84/50"}),
          ch("harmful", "Adenosine to &ldquo;reset&rdquo; the rhythm.", "Adenosine slows AV conduction further and is for regular narrow tachycardia.", "n3", then="The nurse questions the order; you switch to atropine, calcium and insulin.",
             vitals={"time": "6:32 a.m.", "hr": 38, "bp": "80/48"})]),
      "n3": node("6:40", "The potassium returns at 6.9 mmol/L. Her rate is 46, pressure 90/56, more alert.", "What happens to dialysis?", [
          ch("best", "With the attending nephrologist&rsquo;s plan, connect her now for urgent dialysis on the potassium bath the physician orders, monitored, with glucose checks after insulin.", "Dialysis is the definitive treatment; calcium and insulin only buy time.", "end",
             vitals={"time": "6:50 a.m.", "uf": "Low per order", "pump": "Running", "k": "6.9 mmol/L", "hr": 58, "bp": "102/60", "rhythm": "normal", "rhythmLabel": "Narrow rhythm, 58/min", "alarm": ["k"]}),
          ch("poor", "Delay dialysis until tomorrow since she is better.", "Shifting treatments wear off and potassium rebounds.", "end", then="The attending asks for urgent connection.",
             vitals={"time": "7:10 a.m.", "uf": "Low per order", "pump": "Running", "k": "6.9 mmol/L", "hr": 52, "bp": "96/58", "alarm": ["k"]})]),
      "end": end("9:30 a.m.", "After dialysis her rate is 70 and her pressure 118/68. The attending reviews her beta-blocker and the reason she became dehydrated.")},
     debrief([("Stability by signs, not the number.", ""), ("BRASH:", "potassium and an AV-nodal drug slow the heart together; treat both."),
              ("Dialysis is the cure for potassium-driven bradycardia;", "connect with the attending&rsquo;s plan.")]),
     {"algorithm": "adult-brady", "set": ["adult", "dialysis"], "budget": 30})

# ─────────────────────────── 06b Fast rhythm ───────────────────────────
case("rl06-fast", "06-peri-arrest-rhythms", "Fast rhythm with a pulse",
     {"time": "11:10 a.m.", "bp": "118/72", "hr": 176, "spo2": 96, "ecg": "Regular narrow tachycardia", "uf": "On", "pump": "Running",
      "rhythm": "svt", "rhythmLabel": "Regular narrow tachycardia, 176/min", "alarm": ["hr"]},
     "<p>Mr. Felix Domingo, 52, dialyzes through a tunneled catheter. Halfway through his session he reports palpitations. He is alert, talking, pressure 118/72. You are the physician-on-duty.</p>",
     {"n1": node("11:10", "", "Is he stable, and what first?", [
         ch("best", "Stable: 12-lead ECG, stop fluid removal per protocol, vagal maneuver, then adenosine per protocol if it persists.", "Stable regular narrow tachycardia: vagal maneuvers, then adenosine (COR 1).", "n2", vitals={"uf": "Off"}),
         ch("poor", "Unstable: synchronized cardioversion now.", "No signs of compromise; cardioversion is for instability.", "n2", then="You pause and treat him as stable.", vitals={"uf": "Off"})]),
      "n2": node("11:14", "Vagal maneuvers fail. He has only the dialysis catheter for access.", "How do you give adenosine?", [
          ch("best", "Aspirate the catheter lock, flush; give the dose the physician decides for a central line (the guideline notes 1 mg may be adequate), as a rapid push with a flush; warn him about a brief pause.", "A dialysis catheter is a central line: lock first, and the dose decision changes.", "n3"),
          ch("harmful", "Push 12 mg straight into the catheter limb with the lock still in it.", "This pushes heparin or citrate lock into him and gives a large central dose.", "n3", then="The circuit nurse stops you, aspirates the lock, and you choose a central-line dose.")]),
      "n3": node("11:16", "After adenosine, the rhythm briefly slows, then returns at 180. Now his pressure is 76/40 and he is confused.", "What now?", [
          ch("best", "Unstable: synchronized cardioversion per protocol (sedate if feasible), sync markers confirmed on each R wave, everyone clear.", "Persistent tachyarrhythmia with hypotension and confusion needs synchronized cardioversion.", "n4",
             vitals={"time": "11:20 a.m.", "hr": 82, "bp": "112/70", "rhythm": "normal", "rhythmLabel": "Sinus rhythm", "alarm": []}),
          ch("poor", "Another adenosine and wait.", "He is now unstable; drugs must not delay cardioversion.", "n4", then="His pressure falls further; you cardiovert.",
             vitals={"time": "11:23 a.m.", "hr": 84, "bp": "108/68", "rhythm": "normal", "rhythmLabel": "Sinus rhythm", "alarm": []}),
          ch("harmful", "Unsynchronized shock at low energy.", "An unsynchronized shock can land on the T wave and cause VF; use sync for a tachycardia with a pulse.", "n4", then="You switch the device to sync before the shock.",
             vitals={"time": "11:22 a.m.", "hr": 84, "bp": "108/68", "rhythm": "normal", "rhythmLabel": "Sinus rhythm", "alarm": []})]),
      "n4": node("11:25", "He is in sinus rhythm, alert, pressure 112/70.", "What about the session?", [
          ch("best", "Keep him monitored; the physician-on-duty and attending decide whether to resume, return the blood or end; check potassium, magnesium, and the catheter tip position if suspected.", "Rhythm changes around dialysis need a cause review before restarting.", "end"),
          ch("ok", "Restart fluid removal at the original rate.", "Restarting without review may trigger it again; the attending decides.", "end", then="The attending lowers the fluid goal and asks for electrolytes.")]),
      "end": end("12:30 p.m.", "Mr. Domingo finishes a shortened session with a reduced fluid goal and is referred for cardiology review.")},
     debrief([("Stable or unstable decides the path.", ""), ("Adenosine through a dialysis catheter:", "aspirate the lock; central-line dose decided by the physician."),
              ("Synchronized for tachycardia with a pulse;", "unsynchronized only for pulseless or polymorphic VT.")]),
     {"algorithm": "adult-tachy", "set": ["adult", "dialysis"], "budget": 25})

# ─────────────────────────── 07a Air in the system ───────────────────────────
case("rl07-air", "07-arrest-in-the-dialysis-chair", "Air in the system",
     {"time": "1:40 p.m.", "bp": "138/80", "hr": 92, "spo2": 97, "ecg": "Sinus", "line": "Foam below venous chamber", "uf": "On", "pump": "Stopped (air alarm)",
      "rhythm": "normal", "rhythmLabel": "Sinus rhythm", "alarm": ["line", "pump"]},
     "<p>At 1:40 p.m., the air detector alarms on Mrs. Nora Valdez&rsquo;s machine. You see foam below the venous chamber. She is sitting up and suddenly coughs and says her chest feels tight. You are her nurse.</p>",
     {"n1": node("1:40", "", "What do you do first?", [
         ch("best", "Keep the pump stopped, clamp the venous line, never override the detector; do not return the blood.", "Air on the patient side is an emergency; returning the blood pushes more air in.", "n2", vitals={"line": "Venous line clamped", "uf": "Off"}),
         ch("harmful", "Clear the alarm and complete rinse-back.", "Overriding the detector and rinsing back drives air into the patient.", "n2", then="The charge nurse stops the rinse-back and clamps.", vitals={"line": "Venous line clamped", "uf": "Off", "spo2": 90}),
         ch("poor", "Tap the chamber to move the bubbles and restart.", "Air below the venous chamber is not removed by tapping; restarting risks embolism.", "n2", then="You clamp the line instead.", vitals={"line": "Venous line clamped", "uf": "Off"})]),
      "n2": node("1:41", "She is breathless, saturation 89%.", "How do you position and support her?", [
          ch("best", "100% oxygen; lay her flat per the unit protocol (supine or left side; never sitting up); call for help, the cart, the physician-on-duty and the attending; arrange emergency transfer.", "AHA 2025: 100% oxygen (COR 1) and supine or recovery position on a level surface (COR 2a); dialysis teaching uses the left side. Never sitting up.", "n3", vitals={"spo2": 93}),
          ch("harmful", "Sit her upright to ease the breathing.", "Sitting up can send air to the brain; every source says never sit up.", "n3", then="The physician lays her flat.", vitals={"spo2": 88})]),
      "n3": node("1:45", "She becomes unresponsive with gasping. No pulse.", "What now?", [
          ch("best", "Cardiac arrest: CPR flat on her back, pads, arrest algorithm; the circuit stays clamped, blood not returned.", "Every source agrees CPR is done flat on the back. The blood decision stays &ldquo;not returned.&rdquo;", "n4",
             vitals={"time": "1:45 p.m.", "bp": "—", "hr": "0", "stripRate": 50, "spo2": "—", "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]}),
          ch("harmful", "Keep her on her left side while compressing.", "Effective compressions need her flat on her back.", "n4", then="The team turns her supine and compresses.",
             vitals={"time": "1:46 p.m.", "bp": "—", "hr": "0", "stripRate": 50, "spo2": "—", "rhythm": "wide", "rhythmLabel": "Slow wide rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]})]),
      "n4": node("1:48", "The technician wants to inspect the circuit.", "What happens to the machine?", [
          ch("best", "Keep the circuit clamped and intact for inspection; the machine is held until the biomedical technician checks the detector and clamp.", "Finding the air entry point prevents the next event.", "end"),
          ch("poor", "Discard the lines to tidy the station.", "The evidence of the entry point is lost.", "end", then="The charge nurse retrieves the lines.")]),
      "end": end("2:10 p.m.", "Mrs. Valdez regains a pulse and is transferred for oxygen therapy and assessment for hyperbaric treatment. The entry point is found: a loose connection before the blood pump.")},
     debrief([("Air: clamp, do not return,", "100% oxygen, flat, never sitting up."), ("Position differs between sources;", "follow the unit protocol. CPR is always flat on the back."),
              ("Keep the circuit", "for inspection.")]),
     {"algorithm": "dialysis-air", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 07b Station 7, the circuit ───────────────────────────
case("rl07-circuit", "07-arrest-in-the-dialysis-chair", "Station 7, the circuit",
     dict(VF, time="9:40 a.m.", uf="On (2.1 L of 3.2 L)", pump="Running", cpr="Running", alarm=["hr", "ecg"]),
     "<p>Same arrest as Module 5: Mr. Arnel Gutierrez, 61, forearm fistula, 2.1 L removed of a 3.2 L goal. Compressions have started. You are his assigned nurse, now the circuit nurse. A saline bag dripped earlier and the chair is wet near his arm.</p>",
     {"n1": node("9:40", "", "Your first action?", [
         ch("best", "Stop fluid removal and say it aloud.", "Fluid removal empties a circulation that has none to spare.", "n2", vitals={"uf": "Off"}),
         ch("poor", "Run to help with compressions.", "The circuit needs one owner; leaving it unmanaged keeps removing fluid.", "n2", then="The leader sends you back to the machine.", vitals={"uf": "Off"})]),
      "n2": node("9:40", "No air, no abnormal blood color, lines intact, no reaction signs.", "The blood decision?", [
          ch("best", "Return the blood quickly with saline (or clamp and disconnect if that would take you away from something more urgent), and announce it.", "With no circuit cause, return the blood volume (ERC) or clamp and disconnect (Card 1).", "n3", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("harmful", "Leave the pump running and keep dialyzing during CPR.", "A running circuit during arrest is unmanaged and may keep removing volume.", "n3", then="The leader asks you to stop and return.", vitals={"pump": "Stopped", "line": "Blood returned"}),
          ch("poor", "Spend four minutes on a full rinse-back program.", "The decision should take seconds; a long rinse-back pulls you from the team.", "n3", then="You switch to clamp and disconnect.", vitals={"pump": "Stopped", "line": "Clamped, disconnected"})]),
      "n3": node("9:41", "The defibrillator is charging for VF.", "What must be true before the shock?", [
          ch("best", "Wet drapes wiped or moved, pads on dry skin away from the fistula arm, the machine disconnected unless rated defibrillation-proof, your hands off the lines at &ldquo;clear.&rdquo;", "ERC: disconnect unless defibrillation-proof, beware wet surfaces.", "n4"),
          ch("harmful", "Hold the lines steady during the shock so the needles do not move.", "The lines touch the patient and can carry current to you.", "n4", then="You let go when the leader repeats &ldquo;clear.&rdquo;")]),
      "n4": node("9:43", "The leader asks for epinephrine.", "Which access, and how?", [
          ch("best", "The secured venous needle with a saline-primed line, flush before and after; tell the leader it is ready.", "ERC: leave the access open (working, secured) and use it for drugs.", "end"),
          ch("poor", "Start a new IV in the fistula arm.", "Avoid the fistula arm; the existing venous needle is ready and safer.", "end", then="You use the venous needle instead.")]),
      "end": end("10:05 a.m.", "Handover: two hours on the machine, 2.1 L removed, blood returned at the start, last potassium, fistula needles secured. Dialysis is not restarted without the attending nephrologist.")},
     debrief([("Stop fluid removal first.", ""), ("Decide and announce the blood:", "return or clamp; never return after air, hemolysis or reaction."),
              ("Before the shock:", "dry, pads clear, disconnected unless rated, hands off."), ("Use the access safely", "for drugs.")]),
     {"algorithm": "dialysis-arrest", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 08 Missed session ───────────────────────────
case("rl08-missed-session", "08-hyperkalemia-with-pulse-and-in-arrest", "The missed session",
     {"time": "Mon 6:10 a.m.", "bp": "130/80", "hr": 58, "spo2": 97, "ecg": "Peaked T waves, QRS slightly wide", "k": "Pending (45 min)", "uf": "Not started", "pump": "Not connected",
      "rhythm": "peaked", "rhythmLabel": "Peaked T waves", "alarm": ["ecg"]},
     "<p>Mr. Eduardo Panganiban, 55, missed Saturday for a family wake in Batangas. At 6:10 a.m. he is weak with heavy legs. His ECG shows peaked T waves and a slightly wide QRS. The potassium result will take 45 minutes. You are the physician-on-duty.</p>",
     {"n1": node("6:10", "", "What do you do before the result?", [
         ch("best", "Start the order set now: IV calcium for the ECG changes, insulin with glucose (and salbutamol if prescribed), monitor and pads on, connect promptly for dialysis; call the attending.", "ECG changes do not wait for the laboratory: protect, shift, remove.", "n2", vitals={"time": "6:30 a.m.", "uf": "Per order", "pump": "Running", "glucose": "Checks ordered"}),
         ch("poor", "Wait for the result before treating.", "The ECG already shows potassium effects; waiting risks arrest.", "n2", then="At 6:40 you start calcium and insulin and connect him.", vitals={"time": "6:40 a.m.", "uf": "Per order", "pump": "Running"}),
         ch("poor", "Connect without drugs; dialysis will fix it.", "Dialysis is definitive but takes time; calcium protects the heart now.", "n2", then="You add calcium and insulin after connection.", vitals={"time": "6:35 a.m.", "uf": "Per order", "pump": "Running"})]),
      "n2": node("6:55", "His rhythm slows to 40 and widens; then he is unresponsive and pulseless. Slow wide organized complexes on the monitor.", "Which algorithm, and first moves?", [
          ch("best", "Cardiac arrest, nonshockable (PEA): compressions, circuit nurse stops fluid removal and makes the blood decision, epinephrine as soon as feasible; potassium is the leading cause.", "Arrest comes first; potassium is the reversible cause.", "n3",
             vitals={"time": "6:55 a.m.", "bp": "—", "hr": "0", "stripRate": 34, "spo2": "—", "rhythm": "sine", "rhythmLabel": "Sine-wave pattern, no pulse", "ecg": "Sine wave, no pulse", "cpr": "Running", "uf": "Off", "alarm": ["hr", "ecg"]}),
          ch("harmful", "Give more calcium and wait for the potassium result.", "Without a pulse, only compressions move blood.", "n3", then="Compressions start 40 seconds later.",
             vitals={"time": "6:56 a.m.", "bp": "—", "hr": "0", "stripRate": 34, "spo2": "—", "rhythm": "sine", "rhythmLabel": "Sine-wave pattern, no pulse", "ecg": "Sine wave, no pulse", "cpr": "Running", "uf": "Off", "alarm": ["hr", "ecg"]})]),
      "n3": node("6:57", "The team asks about potassium drugs during the arrest.", "What guides the choice?", [
          ch("best", "The unit protocol, decided in advance: AHA 2025 rates calcium, bicarbonate and insulin as of uncertain effectiveness and advises against inhaled beta-agonists; ERC 2025 gives 10 mL of 10% calcium chloride with 50 mmol bicarbonate through separate lines. No pause in compressions.", "Guidelines differ; the protocol chooses, written beforehand.", "n4"),
          ch("harmful", "Calcium and bicarbonate in the same line, back to back, quickly.", "They precipitate in the line; use separate lines or flush between.", "n4", then="The drug nurse flushes the line between them."),
          ch("poor", "Inhaled salbutamol through the bag-mask.", "AHA 2025: inhaled beta-agonists are not recommended in hyperkalemic arrest.", "n4", then="The leader stops the nebulizer.")]),
      "n4": node("7:06", "After epinephrine and protocol treatment, he has a pulse at 72 with a pressure of 100/60. Potassium returns at 8.1 mmol/L.", "What now?", [
          ch("best", "Post-ROSC care, repeat potassium and glucose, keep pads on, and let the attending nephrologist decide where dialysis continues (usually monitored, possibly after transfer).", "Potassium rebounds; dialysis restarts only on the attending&rsquo;s decision.", "end",
             vitals={"time": "7:06 a.m.", "bp": "100/60", "hr": 72, "spo2": 95, "k": "8.1 mmol/L", "rhythm": "peaked", "rhythmLabel": "Narrow rhythm, peaked T", "cpr": "Stopped", "alarm": ["k"]}),
          ch("poor", "Reconnect immediately at high blood flow without calling anyone.", "Restarting in an unstable patient is the attending&rsquo;s decision.", "end", then="The attending is called and plans monitored dialysis.",
             vitals={"time": "7:08 a.m.", "bp": "100/60", "hr": 72, "spo2": 95, "k": "8.1 mmol/L", "rhythm": "peaked", "rhythmLabel": "Narrow rhythm, peaked T", "cpr": "Stopped", "alarm": ["k"]})]),
      "end": end("9:00 a.m.", "Mr. Panganiban is dialyzed under monitoring after transfer. The social worker and attending review why he missed his session and plan for the next family event.")},
     debrief([("Treat ECG changes without waiting for the laboratory.", ""), ("In arrest, CPR first;", "AHA and ERC differ on potassium drugs; the protocol decides."),
              ("Calcium and bicarbonate never share a line", "without a flush."), ("After ROSC,", "potassium rebounds; the attending decides on dialysis.")]),
     {"algorithm": "hyperkalemia", "set": ["adult", "dialysis"], "budget": 25})

# ─────────────────────────── 09a Needle out ───────────────────────────
case("rl09-needle-out", "09-circuit-emergencies", "Needle out",
     {"time": "4:15 p.m.", "bp": "84/50", "hr": 118, "spo2": 95, "ecg": "Sinus tachycardia", "uf": "On", "pump": "Running", "line": "No alarm",
      "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": ["bp"]},
     "<p>Bacolod City, 4:15 p.m. Mrs. Gloria Santiago, 74, asleep under a thick blanket in her third hour. Blood is dripping from under the blanket onto a wet floor. The machine shows no alarm. She is pale and hard to wake.</p>",
     {"n1": node("4:15", "", "What do you do in the first ten seconds?", [
         ch("best", "Lift the blanket; venous needle out: stop the blood pump, clamp both sides, press firmly with gloved hands and gauze, shout for help.", "A quiet machine proves nothing; stop the loss first.", "n2", vitals={"pump": "Stopped", "line": "Clamped; pressure on site", "uf": "Off"}),
         ch("harmful", "Reinsert the needle and continue.", "Never reinsert a dislodged needle.", "n2", then="The charge nurse stops you; pump off, clamp, pressure.", vitals={"pump": "Stopped", "line": "Clamped; pressure on site", "uf": "Off"}),
         ch("poor", "Check the machine first; it shows no alarm, so it must be minor.", "The venous pressure alarm can stay silent when a needle is out.", "n2", then="You lift the blanket and see the needle out.", vitals={"pump": "Stopped", "line": "Clamped; pressure on site", "uf": "Off"})]),
      "n2": node("4:16", "Pressure 76/42, heart rate 128. Large pool of blood.", "Next?", [
          ch("best", "Lay her flat, oxygen, call the physician-on-duty and attending, new IV (not the open line) for saline per physician, estimate the loss, assign a watcher, dry the floor.", "Hemorrhagic shock: volume, help, and a safe floor.", "n3", vitals={"bp": "80/46", "hr": 124}),
          ch("harmful", "Return the circuit blood through the open line end.", "Blood is never returned through an open line end.", "n3", then="You use a new IV instead.", vitals={"bp": "78/44", "hr": 126})]),
      "n3": node("4:22", "She becomes unresponsive; no pulse.", "What now?", [
          ch("best", "Cardiac arrest with hemorrhage as the cause: compressions, pads, arrest algorithm, fluids, early transfer for blood; floor dried before kneeling or shocking.", "The cause guides treatment during CPR.", "end",
             vitals={"time": "4:22 p.m.", "bp": "—", "hr": "0", "stripRate": 110, "spo2": "—", "rhythm": "normal", "rhythmLabel": "Organized rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]}),
          ch("poor", "Keep pressing the site and wait for the physician.", "Without a pulse, compressions come first.", "end", then="A nurse starts compressions.",
             vitals={"time": "4:23 p.m.", "bp": "—", "hr": "0", "stripRate": 110, "spo2": "—", "rhythm": "normal", "rhythmLabel": "Organized rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]})]),
      "end": end("4:45 p.m.", "With fluids and CPR she regains a pulse and is transferred for blood. The unit changes its blanket rule: access arms stay visible.")},
     debrief([("Lift the blanket;", "machines can miss dislodgement."), ("Stop, clamp, press;", "never reinsert or return through an open end."),
              ("Arrest from hemorrhage:", "CPR plus volume and early blood.")]),
     {"algorithm": "dialysis-hemorrhage", "set": ["adult", "dialysis"], "budget": 15})

# ─────────────────────────── 09b Reaction after connection ───────────────────────────
case("rl09-reaction", "09-circuit-emergencies", "Reaction after connection",
     {"time": "6:08 a.m.", "bp": "86/48", "hr": 124, "spo2": 91, "ecg": "Sinus tachycardia", "uf": "On", "pump": "Running",
      "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": ["bp", "spo2"]},
     "<p>Eight minutes after connection with a new dialyzer type, Mr. Romeo Castro, 66, develops hives, wheeze, lip swelling and a pressure of 86/48.</p>",
     {"n1": node("6:08", "", "First actions?", [
         ch("best", "Stop the pump, clamp, do not return the blood; call for help; IM epinephrine into the outer thigh per protocol.", "Anaphylaxis: epinephrine first; the circuit carries the trigger.", "n2", vitals={"pump": "Stopped", "line": "Clamped, not returned", "uf": "Off"}),
         ch("poor", "Give an antihistamine and observe.", "Antihistamines do not replace epinephrine.", "n2", then="He worsens; IM epinephrine is given.", vitals={"pump": "Stopped", "line": "Clamped, not returned", "uf": "Off", "bp": "80/44"}),
         ch("harmful", "Return the blood quickly to treat the low pressure.", "Returning the blood gives back the trigger.", "n2", then="The charge nurse clamps; IM epinephrine is given.", vitals={"pump": "Stopped", "line": "Clamped", "uf": "Off", "bp": "78/42"})]),
      "n2": node("6:10", "The drug nurse holds a 1 mg/mL ampule and asks, &ldquo;IV push?&rdquo;", "What do you say?", [
          ch("best", "&ldquo;No. Intramuscular, outer thigh, the protocol dose of 1 mg per mL. IV epinephrine is for arrest, at 0.1 mg per mL.&rdquo;", "Route and concentration differ; an IV bolus of the IM concentration is a tenfold error.", "n3", vitals={"bp": "98/58", "spo2": 94}),
          ch("harmful", "&ldquo;Yes, push it IV quickly.&rdquo;", "A bolus of 1 mg/mL IV in a patient with a pulse can cause dangerous arrhythmias.", "n3", then="A second nurse reads back the route and corrects to IM.", vitals={"bp": "96/56", "spo2": 93})]),
      "n3": node("6:16", "Despite a second IM dose per protocol, he becomes unresponsive with no pulse.", "What now?", [
          ch("best", "Cardiac arrest algorithm: compressions, IV epinephrine 1 mg every 3 to 5 minutes, isotonic IV fluids (reasonable in anaphylactic arrest), transfer.", "AHA 2025: IV fluids reasonable (COR 2a); the standard IM dose in arrest is of uncertain effectiveness.", "end",
             vitals={"time": "6:16 a.m.", "bp": "—", "hr": "0", "stripRate": 120, "spo2": "—", "rhythm": "normal", "rhythmLabel": "Organized rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]}),
          ch("poor", "Another IM dose and wait.", "In arrest, IV epinephrine within the arrest algorithm and CPR come first.", "end", then="The leader starts the arrest algorithm.",
             vitals={"time": "6:17 a.m.", "bp": "—", "hr": "0", "stripRate": 120, "spo2": "—", "rhythm": "normal", "rhythmLabel": "Organized rhythm, no pulse (PEA)", "cpr": "Running", "alarm": ["hr"]})]),
      "end": end("6:40 a.m.", "He regains a pulse and is transferred. The dialyzer, packaging and lot number are kept; that dialyzer type is not used again for him until the physician reviews it.")},
     debrief([("Anaphylaxis: IM epinephrine first;", "blood not returned."), ("Say route and concentration aloud.", "IM 1 mg/mL vs IV 0.1 mg/mL."),
              ("Arrest:", "the standard algorithm with IV epinephrine and fluids.")]),
     {"algorithm": "dialysis-anaphylaxis", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 09c Dark blood ───────────────────────────
case("rl09-hemolysis", "09-circuit-emergencies", "Dark blood, chest pain, rising potassium",
     {"time": "8:30 a.m.", "bp": "168/94", "hr": 104, "spo2": 96, "ecg": "Sinus tachycardia", "line": "Translucent, port-wine blood", "uf": "On", "pump": "Running",
      "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": ["line"]},
     "<p>At 8:30 a.m., Mrs. Linda Ocampo, 61, at Station 9 reports back and chest pain and nausea. The blood in her venous line looks translucent, like red wine. Two minutes later, the patient at Station 10 says his back hurts.</p>",
     {"n1": node("8:30", "", "What do you do at Station 9?", [
         ch("best", "Stop the pump, clamp the lines, do not return the blood; monitor; urgent potassium and hemoglobin; call the physician-on-duty.", "Hemolyzed blood carries potassium and is never returned.", "n2", vitals={"pump": "Stopped", "line": "Clamped, not returned", "uf": "Off"}),
         ch("harmful", "Return the blood and end the session.", "Returning hemolyzed blood adds potassium.", "n2", then="The charge nurse clamps the lines.", vitals={"pump": "Stopped", "line": "Clamped", "uf": "Off", "k": "Rising"})]),
      "n2": node("8:33", "Station 10 has the same symptoms; his venous line also looks abnormal.", "What does the charge nurse do?", [
          ch("best", "Declare a possible cluster: stop and clamp at Station 10, check every patient on the same water and concentrate, hold new starts, call the Medical Director; technician keeps lines and samples water and fluid.", "Hemolysis is often a shared supply fault.", "n3"),
          ch("poor", "Treat Station 10 separately later.", "A cluster needs immediate action across the unit.", "n3", then="You declare the cluster five minutes later.")]),
      "n3": node("8:50", "Mrs. Ocampo&rsquo;s potassium is 7.4 mmol/L; the ECG shows peaked T waves. At 8:55 she becomes unresponsive and pulseless.", "What now?", [
          ch("best", "Cardiac arrest: CPR, arrest algorithm, potassium treatment per protocol; blood still not returned; the watcher covers Station 10 and the rest.", "Potassium is the reversible cause; the circuit decision stays.", "end",
             vitals={"time": "8:55 a.m.", "bp": "—", "hr": "0", "stripRate": 40, "spo2": "—", "rhythm": "sine", "rhythmLabel": "Sine-wave pattern, no pulse", "cpr": "Running", "k": "7.4 mmol/L", "alarm": ["hr", "k"]}),
          ch("poor", "Everyone goes to Station 9.", "Station 10 is also affected and needs a watcher.", "end", then="The charge nurse sends one nurse back to Station 10.",
             vitals={"time": "8:56 a.m.", "bp": "—", "hr": "0", "stripRate": 40, "spo2": "—", "rhythm": "sine", "rhythmLabel": "Sine-wave pattern, no pulse", "cpr": "Running", "k": "7.4 mmol/L", "alarm": ["hr", "k"]})]),
      "end": end("10:00 a.m.", "Mrs. Ocampo has ROSC and is transferred; the patient at Station 10 is stable. The water team finds a carbon tank breakthrough. No treatment restarts until the water and fluid are cleared.")},
     debrief([("Port-wine blood is never returned.", ""), ("One hemolysis can be a cluster:", "check everyone on the same supply."),
              ("Potassium drives the arrest risk;", "keep a watcher for the other patients.")]),
     {"algorithm": "dialysis-hemolysis", "set": ["adult", "dialysis"], "budget": 20})

# ─────────────────────────── 10 Child becoming quiet ───────────────────────────
case("rl10-child-quiet", "10-pediatric-bls-and-deterioration", "The child becoming quiet",
     {"time": "2:40 p.m.", "bp": "104/66", "hr": 54, "spo2": 82, "rr": 8, "ecg": "Sinus bradycardia", "uf": "On", "pump": "Running",
      "rhythm": "normal", "rhythmLabel": "Slow sinus rhythm, 54/min", "alarm": ["hr", "spo2"]},
     "<p>Jun-Jun, 8, 22 kg, arrived coughing and breathing fast after gaining 1.8 kg. Forty minutes into dialysis he is drowsy and pale, with slow shallow breaths. Saturation 82%; heart rate 54 (it was 120). You are the pediatric dialysis nurse.</p>",
     {"n1": node("2:40", "", "What is happening, and what is first?", [
         ch("best", "Respiratory failure with hypoxic bradycardia: call for help and the pediatric cart; open the airway; bag-mask ventilation with oxygen using the right mask size.", "In children, breathing usually fails first; ventilation breaks the chain.", "n2", vitals={"spo2": 90, "hr": 88, "rr": "Bagging 20/min"}),
         ch("poor", "Atropine for the slow heart rate.", "Hypoxic bradycardia needs oxygen and ventilation, not atropine.", "n2", then="You ventilate; the rate rises.", vitals={"spo2": 88, "hr": 80, "rr": "Bagging"}),
         ch("poor", "Start compressions at once.", "With a pulse and a rate over 60 for now, effective ventilation comes first.", "n2", then="A colleague takes the airway and ventilates; the rate rises.", vitals={"spo2": 88, "hr": 82, "rr": "Bagging"})]),
      "n2": node("2:43", "With bagging, saturation 90%, heart rate 88. The physician-on-duty and attending pediatric nephrologist are called.", "What about the circuit?", [
          ch("best", "Report the fluid status and pressure; the physicians decide whether fluid removal continues for the edema or stops for pressure.", "In pulmonary edema, fluid removal may be treatment; it is a physician decision.", "n3"),
          ch("ok", "Stop fluid removal automatically because he is unwell.", "Stopping may remove part of the treatment for edema; ask the physician.", "n3", then="The attending restarts gentle fluid removal.")]),
      "n3": node("2:50", "Despite good bag-mask ventilation with oxygen, his heart rate falls to 50 and he is mottled with weak pulses.", "What now?", [
          ch("best", "Start pediatric CPR: one-third chest depth, 100 to 120 a minute, 15:2 with two rescuers; epinephrine by weight if compromise persists after hypoxia is corrected.", "PALS 2025: CPR for HR under 60 with compromise despite effective oxygenated ventilation (COR 1).", "end",
             vitals={"time": "2:50 p.m.", "hr": 50, "bp": "62/34", "spo2": 88, "cpr": "Running", "alarm": ["hr", "bp", "spo2"]}),
          ch("poor", "Wait until the heart rate is under 40.", "The threshold is under 60 with poor perfusion despite ventilation.", "end", then="You start CPR a minute later.",
             vitals={"time": "2:51 p.m.", "hr": 44, "bp": "58/30", "spo2": 86, "cpr": "Running", "alarm": ["hr", "bp", "spo2"]})]),
      "end": end("3:15 p.m.", "Jun-Jun&rsquo;s heart rate recovers with ventilation and brief CPR; he is moved to the pediatric intensive care unit with a plan for gentle fluid removal there.")},
     debrief([("Breathing fails first in children;", "ventilate with the right mask."), ("Under 60 with poor perfusion despite ventilation:", "compressions."),
              ("The circuit decision", "belongs to the physicians.")]),
     {"algorithm": "peds-deterioration", "set": ["pediatric", "dialysis"], "budget": 20}, order=["time", "bp", "hr", "spo2", "rr", "ecg", "uf", "pump"])

# ─────────────────────────── 11 Pediatric arrest ───────────────────────────
case("rl11-peds-arrest", "11-pediatric-arrest-and-dialysis", "Pediatric arrest during dialysis",
     {"time": "10:05 a.m.", "bp": "—", "hr": "0", "spo2": "—", "ecg": "Flat line in two leads", "uf": "On", "pump": "Running", "access": "Tunneled catheter",
      "rhythm": "asystole", "rhythmLabel": "Asystole (confirmed in two leads)", "alarm": ["hr", "ecg"]},
     "<p>Mika, 6, last reliable dry weight 19 kg (today&rsquo;s 21 kg reading is questioned), dialyzes through a tunneled catheter. One hour in she is unresponsive and pulseless; a slow wide rhythm became a flat line confirmed in two leads. Compressions have started. The drug nurse asks, &ldquo;Epinephrine, how much?&rdquo; Someone reads the ampule: &ldquo;1 mg per mL.&rdquo;</p>",
     {"n1": node("10:05", "", "Which path, and when is epinephrine given?", [
         ch("best", "Nonshockable (asystole): epinephrine as early as possible, then every 3 to 5 minutes; 15:2 with two rescuers.", "PALS 2025: initial epinephrine as early as possible in nonshockable arrest (COR 2a).", "n2", vitals={"cpr": "Running 15:2", "uf": "Off"}),
         ch("poor", "Shock first.", "Asystole is not shockable.", "n2", then="The leader moves to the nonshockable path.", vitals={"cpr": "Running 15:2", "uf": "Off"})]),
      "n2": node("10:06", "", "What weight and dose?", [
          ch("best", "Protocol weight 19 kg: 0.01 mg/kg = 0.19 mg (about 0.2 mg per protocol) = about 2 mL of 0.1 mg/mL; said aloud and checked by a second nurse.", "Weight, dose, volume and concentration said aloud prevent tenfold errors.", "n3"),
          ch("harmful", "2 mL from the 1 mg/mL ampule.", "That is 2 mg, ten times her dose.", "n3", then="The second nurse catches it: 0.1 mg/mL is used."),
          ch("poor", "Use the questioned 21 kg reading.", "Use the protocol&rsquo;s reliable weight or a length-based tape.", "n3", then="The leader switches to 19 kg.")]),
      "n3": node("10:07", "The circuit nurse is at the machine. No air, no hemolysis, no reaction signs.", "The circuit decision?", [
          ch("best", "Stop fluid removal and the pump; return the blood per protocol (in a 19 kg child, about 1,520 mL blood volume, the circuit blood matters); aspirate the catheter lock before using a limb for drugs.", "Small children: the circuit is a large share of blood volume; lock first.", "n4", vitals={"pump": "Stopped", "access": "Lock aspirated; limb flushed"}),
          ch("harmful", "Push epinephrine straight into the catheter limb.", "The lock (heparin or citrate) would go in first.", "n4", then="The circuit nurse aspirates the lock first.", vitals={"pump": "Stopped", "access": "Lock aspirated"})]),
      "n4": node("10:11", "At the next check: VF.", "Energy?", [
          ch("best", "2 J/kg (about 40 J; nearest setting), then 4 J/kg for the next shock; compressions immediately after each.", "PALS 2025: 2 to 4 J/kg first (2 J/kg for teaching), then 4 J/kg.", "end",
             vitals={"time": "10:11 a.m.", "rhythm": "vf", "stripRate": 240, "rhythmLabel": "Ventricular fibrillation", "ecg": "VF"}),
          ch("harmful", "200 J, the adult setting.", "Pediatric energies are weight-based; 200 J is 10 J/kg for her, the maximum, not the first shock.", "end", then="The leader resets to 40 J.",
             vitals={"time": "10:11 a.m.", "rhythm": "vf", "stripRate": 240, "rhythmLabel": "Ventricular fibrillation", "ecg": "VF"})]),
      "end": end("10:25 a.m.", "After a shock at 2 J/kg and continued CPR, Mika regains a pulse and is transferred to the pediatric intensive care unit. The dose card and syringe labels are reviewed at the debrief.")},
     debrief([("Weight, dose, volume, concentration aloud,", "with a second check."), ("Arrest epinephrine is 0.1 mg/mL:", "0.1 mL/kg."),
              ("Energies by weight:", "2, then 4, up to 10 J/kg or the adult dose."), ("In small children", "the circuit blood matters; lock before drugs.")]),
     {"algorithm": "peds-arrest", "set": ["pediatric", "dialysis"], "budget": 25}, order=["time", "bp", "hr", "spo2", "ecg", "uf", "pump", "access"])

# ─────────────────────────── 12 Pulse restored ───────────────────────────
case("rl12-rosc", "12-rosc-and-transfer", "Pulse restored, now what?",
     {"time": "2:35 p.m.", "bp": "84/50", "hr": 112, "spo2": 89, "ecg": "Sinus tachycardia", "uf": "Off (2.6 L removed)", "pump": "Stopped; blood returned", "k": "5.1 (this morning)",
      "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": ["bp", "spo2"]},
     "<p>After 11 minutes of CPR, Mr. Leonardo Ramos, 70, has a carotid pulse at a freestanding unit in Taytay. Pressure 84/50, saturation 89% on a mask, irregular breathing, not following commands. The ambulance is 20 minutes away. A nurse asks, &ldquo;Should we put him back on dialysis while we wait?&rdquo;</p>",
     {"n1": node("2:35", "", "First priorities?", [
         ch("best", "Keep pads on; support breathing with the bag-mask and oxygen to 90 to 98%; saline per physician toward a MAP of at least 65; 12-lead ECG; glucose and potassium.", "AHA 2025 post-ROSC targets for oxygen and pressure, plus dialysis-specific checks.", "n2", vitals={"spo2": 94, "bp": "96/58"}),
         ch("poor", "Remove the pads to make him comfortable.", "Re-arrest is common; pads stay on.", "n2", then="You reattach the pads.", vitals={"spo2": 92, "bp": "90/54"})]),
      "n2": node("2:40", "", "Restart dialysis?", [
          ch("best", "No, not without the attending nephrologist; he is unstable and needs monitored care. Call the attending and the receiving hospital.", "Card 1: do not restart dialysis unless the attending says so.", "n3"),
          ch("harmful", "Yes, reconnect to finish the session.", "Starting a circuit in an unstable patient can drop the pressure and cause re-arrest.", "n3", then="The physician-on-duty stops the restart.")]),
      "n3": node("2:48", "His pulse is lost again.", "What do you do?", [
          ch("best", "Re-arrest: compressions within seconds, arrest algorithm from the recorder&rsquo;s last rhythm and drug times.", "Pads on and a running timeline make re-arrest fast to treat.", "n4",
             vitals={"time": "2:48 p.m.", "bp": "—", "hr": "No pulse", "stripRate": 220, "spo2": "—", "rhythm": "vf", "rhythmLabel": "Ventricular fibrillation", "alarm": ["hr"]}),
          ch("poor", "Check the blood pressure cuff again.", "No pulse means compressions now.", "n4", then="Compressions start 20 seconds later.",
             vitals={"time": "2:49 p.m.", "bp": "—", "hr": "No pulse", "stripRate": 220, "spo2": "—", "rhythm": "vf", "rhythmLabel": "Ventricular fibrillation", "alarm": ["hr"]})]),
      "n4": node("2:58", "After one shock, ROSC again; pressure 98/60. The ambulance arrives.", "What goes in the handover?", [
          ch("best", "Identity, time of collapse, rhythms, shocks, drugs and times, ROSC times; hours on machine, 2.6 L removed, blood returned, last potassium; current vitals; ECG and sheets.", "The arrest and dialysis facts travel together.", "end",
             vitals={"time": "2:58 p.m.", "bp": "98/60", "hr": 104, "spo2": 95, "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": []}),
          ch("poor", "&ldquo;He arrested and we got him back.&rdquo;", "Without the dialysis facts and times, the receiving team starts over.", "end", then="The recorder hands over the full sheet.",
             vitals={"time": "2:59 p.m.", "bp": "98/60", "hr": 104, "spo2": 95, "rhythm": "normal", "rhythmLabel": "Sinus tachycardia", "alarm": []})]),
      "end": end("3:05 p.m.", "Mr. Ramos leaves with a full handover. The debrief adds a one-page post-ROSC handover sheet to the crash cart.")},
     debrief([("After ROSC:", "oxygen 90 to 98%, MAP at least 65, ECG, glucose, potassium, pads on."), ("No dialysis restart", "without the attending nephrologist."),
              ("Hand over the arrest and the dialysis facts together.", "")]),
     {"algorithm": "post-rosc", "set": ["adult", "dialysis"], "budget": 25})

# ─────────────────────────── 13 Debrief ───────────────────────────
case("rl13-debrief", "13-team-code-status-and-debrief", "The debrief nobody wanted",
     {"time": "11:05 a.m.", "bp": "—", "hr": "—", "spo2": "—", "ecg": "Event over", "rhythm": "asystole", "rhythmLabel": "Monitor idle"},
     "<p>After a 25-minute resuscitation ending in transfer with ROSC, the team in Pampanga is exhausted. During the event: two physicians gave conflicting orders for a minute; one epinephrine dose was given twice; the watcher joined compressions and another patient&rsquo;s pressure fell unnoticed; the patient&rsquo;s daughter waited alone. A senior nurse says, &ldquo;Let us just go back to work.&rdquo; You are the charge nurse.</p>",
     {"n1": node("11:05", "", "Do you debrief?", [
         ch("best", "Yes, ten minutes now, systems not people, using the five questions and the recorder&rsquo;s sheet.", "A structured debrief is associated with better learning; fear of blame is why it needs structure.", "n2"),
         ch("poor", "Skip it; everyone is tired.", "The lessons are lost and the same failures recur.", "n2", then="You hold a short debrief at shift end instead.")]),
      "n2": node("11:10", "", "The conflicting orders. What is the fix?", [
          ch("best", "A leadership handover script (&ldquo;summary, I am taking the lead, you have the lead&rdquo;) owned by the Dialysis Clinical Head and rehearsed in the next drill.", "System fix with an owner and a date.", "n3"),
          ch("poor", "Tell the junior physician to stay quiet next time.", "Blaming a person leaves the system unchanged.", "n3", then="The team agrees on a handover script instead.")]),
      "n3": node("11:13", "", "The doubled epinephrine?", [
          ch("best", "Closed-loop orders to named people and a recorder who calls doses due; owned by the head nurse and practiced in every drill.", "Orders to the room cause doubled and missed doses.", "n4"),
          ch("ok", "A sign on the cart saying &ldquo;check before giving.&rdquo;", "Signs help little without closed-loop habits.", "n4", then="You add closed-loop practice to drills.")]),
      "n4": node("11:16", "", "The watcher and the daughter?", [
          ch("best", "&ldquo;The watcher never joins&rdquo; added to the shift huddle (charge nurse); a staff member or social worker assigned to families during any code, with supported presence if policy allows.", "Other patients and families need named people.", "end"),
          ch("poor", "Nothing to change; it was a busy day.", "Both failures will recur without owners.", "end", then="You assign owners after all.")]),
      "end": end("11:20 a.m.", "Three changes, three owners, three dates, and a drill booked for next month. The action list goes on the notice board.")},
     debrief([("Debrief every event,", "about systems, not people."), ("Fix with owners and dates:", "leadership script, closed-loop orders, watcher rule, family support.")]),
     {"algorithm": "team", "set": ["adult", "dialysis"], "budget": 45})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("rl*.json"):
        old.unlink()
    for c in CASES:
        (OUT / f"{c['id']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(CASES)} Resuscitation Lab cases")


if __name__ == "__main__":
    main()
