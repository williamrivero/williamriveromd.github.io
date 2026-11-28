# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 06: Bradycardia and Tachycardia With a Pulse. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician-on-duty reading a fast rhythm on the monitor while a nurse places cardioversion pads on a conscious patient.",
    "objectives": [
        "Decide whether a slow or fast rhythm with a pulse is causing cardiopulmonary compromise before choosing treatment.",
        "Manage unstable bradycardia with atropine, then pacing or an epinephrine or dopamine infusion, while treating the cause.",
        "Recognize BRASH syndrome (bradycardia, kidney failure, AV-nodal blockade, shock, hyperkalemia) and treat potassium and the drug effect together.",
        "Sort tachycardia with a pulse by stability, regularity and QRS width, and use adenosine and synchronized cardioversion correctly.",
        "Recognize the moment a peri-arrest rhythm becomes cardiac arrest, and switch algorithms.",
    ],
    "big": """
{{plain:Heart rate is a trade between speed and filling. Too slow, and each beat cannot make up for the missing beats. Too fast, and the heart has no time to fill between beats, so each beat pumps less. In both cases what matters is not the number but whether enough blood reaches the brain, the heart and the kidneys.}}
<p>The picture has a limit. A dialysis patient&rsquo;s heart is often thick and stiff, so it needs more filling time than most, and it may already be underfilled by fluid removal. A heart rate that a healthy person tolerates can tip a dialysis patient into shock. That is why the first question for every rhythm with a pulse is stability, judged at the patient.</p>
<p>Peri-arrest rhythms are common around dialysis: atrial fibrillation after the long gap, slow rhythms from potassium and rate-slowing drugs, and fast rhythms when pressure falls. This module is mainly for nurses and physicians; technicians and assistants learn the first step: bring the defibrillator and monitor to the chair before telephoning (Card 9).</p>
{{cards:Key terms for this module|Bradycardia::A heart rate typically under 50 a minute when it is a bradyarrhythmia.|Tachycardia::A heart rate typically 150 a minute or more when it is a tachyarrhythmia.|Synchronized cardioversion::A shock timed to the R wave of the QRS complex, used for unstable tachycardia with a pulse.|Adenosine::A short-acting drug that briefly blocks the AV node; used for regular narrow-complex tachycardia.|Transcutaneous pacing::Pacing the heart through pads on the skin.|BRASH::Bradycardia, renal failure, AV-nodal blockade, shock and hyperkalemia feeding one another.}}
""",
    "case": {"title": "Slow rhythm, worsening perfusion", "html": """
<p>Mrs. Teresita Morales, 69, dialyzes on Mondays, Wednesdays and Fridays in Cebu City. She takes a beta-blocker for atrial fibrillation and amlodipine. She had diarrhea over the weekend and arrives on Monday weak and dizzy. Before connection her heart rate is 36, blood pressure 82/50 mm Hg; she is pale and slow to answer. The monitor shows a slow, wide-looking rhythm.</p>
<p>The physician-on-duty, Dr. Paolo Lim, has the defibrillator brought to the chair. The pre-dialysis potassium has been sent; the result will take 40 minutes. A nurse asks, &ldquo;Atropine now?&rdquo;</p>
""", "questions": ["Is Mrs. Morales stable or unstable, and why?",
                  "What two problems might be making each other worse?",
                  "What do you do in the next ten minutes, and in what order?"]},
    "sections": [
        ("brady", "Bradycardia", "Bradycardia with a pulse", """
<p>The 2025 adult guideline describes a bradyarrhythmia as a heart rate typically under 50 a minute (lowered from under 60 in earlier guidance), and asks first whether it is causing cardiopulmonary compromise: hypotension, acutely altered mental status, signs of shock, ischemic chest discomfort, or acute heart failure.[[aha2025_als]]</p>
{{fig:rl06_brady}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What to do</th><th>2025 grade</th></tr></thead>
<tbody>
<tr><td>Always</td><td>Airway, oxygen if needed, monitor, IV access, 12-lead ECG if it does not delay treatment; evaluate and treat reversible causes</td><td>Treat causes: COR 1, LOE C-EO</td></tr>
<tr><td>Compromise present</td><td>Atropine: 1 mg IV bolus, repeat every 3 to 5 minutes, maximum 3 mg (algorithm dose)</td><td>COR 2a, LOE B-NR</td></tr>
<tr><td>Atropine ineffective</td><td>Transcutaneous pacing and/or an infusion: epinephrine 2 to 10 mcg a minute, or dopamine 5 to 20 mcg/kg a minute (algorithm doses), titrated</td><td>COR 2b, LOE C-LD</td></tr>
<tr><td>Refractory</td><td>Expert consultation; temporary transvenous pacing</td><td>Transvenous: COR 2a, LOE C-LD</td></tr>
<tr><td>High-degree AV block, unstable, no IV access</td><td>Immediate pacing might be considered</td><td>COR 2b, LOE C-EO</td></tr>
</tbody></table></div>
<p>Atropine works by blocking vagal slowing of the sinus and AV nodes. It helps least when the block is below the AV node (wide escape rhythms) and when the cause is drug or potassium toxicity, which is exactly the situation in many dialysis patients. Do not let atropine doses delay pacing or an infusion in a patient who is getting worse.</p>
{{key:Slow rhythm plus compromise: atropine, then pacing or an epinephrine or dopamine infusion, while you treat the cause. In dialysis, the cause is often potassium, a rate-slowing drug, or both.}}
"""),
        ("brash", "BRASH", "BRASH: when potassium and drugs slow the heart together", """
<p>BRASH syndrome describes a vicious cycle: bradycardia, renal failure, atrioventricular nodal blockade, shock, and hyperkalemia.[[farkas2020]] A moderate rise in potassium and a usual dose of an AV-nodal blocking drug (a beta-blocker, a non-dihydropyridine calcium channel blocker, or digoxin) each slow conduction a little; together they slow it a lot. The slow heart lowers blood pressure, kidney perfusion and potassium excretion fall in patients with residual function, potassium rises further, and the cycle tightens. The usual trigger is hypovolemia, such as diarrhea or poor intake, or a drug that raises potassium.</p>
{{fig:rl06_brash}}
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Isolated drug toxicity</th><th>Isolated hyperkalemia</th><th>BRASH</th></tr></thead>
<tbody>
<tr><td>Potassium</td><td>Normal</td><td>Very high</td><td>Often only moderately high</td></tr>
<tr><td>Drug dose</td><td>Often excessive</td><td>Any</td><td>Usual dose</td></tr>
<tr><td>Trigger</td><td>Overdose</td><td>Missed dialysis, diet</td><td>Hypovolemia, a new potassium-raising drug</td></tr>
<tr><td>Response to treating one part only</td><td>Good</td><td>Good</td><td>Often poor</td></tr>
</tbody></table></div>
<p>The review is a narrative synthesis, not a trial, and the management it describes rests on physiology and case experience: fluid resuscitation where the patient is dry, hyperkalemia treatment (intravenous calcium, insulin with glucose, beta-agonists), and support of the heart rate, which may need an epinephrine infusion.[[farkas2020]] In a dialysis patient, removing potassium means dialysis, and that decision belongs to the attending nephrologist. The practical lesson is recognition: a slow rhythm in a dialysis patient on a rate-slowing drug is potassium until proven otherwise, even when the potassium is &ldquo;only&rdquo; moderately high.</p>
{{key:Slow heart, kidney failure, a rate-slowing drug and a modest potassium rise can be one syndrome. Treat potassium and the bradycardia together, and call the attending nephrologist about dialysis.}}
"""),
        ("tachy", "Tachycardia", "Tachycardia with a pulse", """
<p>For a tachyarrhythmia (heart rate typically 150 a minute or more), the first question is again compromise. A patient with a persistent tachyarrhythmia causing low blood pressure, altered mental status, shock, ischemic chest pain or acute heart failure needs synchronized cardioversion now. A stable patient gives you time for a 12-lead ECG and a more precise diagnosis.[[aha2025_als]]</p>
{{fig:rl06_tachy}}
<div class="table-wrap"><table>
<thead><tr><th>Stable patient</th><th>Narrow QRS</th><th>Wide QRS (0.12 s or more)</th></tr></thead>
<tbody>
<tr><td>Regular</td><td>Vagal maneuvers; adenosine 6 mg rapid IV push with a flush, then 12 mg if needed (COR 1, LOE B-R for adenosine); then rate control with expert advice</td><td>Adenosine only if regular and monomorphic; antiarrhythmic infusion with expert consultation</td></tr>
<tr><td>Irregular</td><td>Usually atrial fibrillation: rate control with expert advice; do not give adenosine</td><td>Expert consultation; polymorphic VT is treated as unstable</td></tr>
</tbody></table></div>
<p>Adenosine is given as a fast push followed immediately by a saline flush, because its effect lasts seconds. The guideline&rsquo;s supportive text notes that 1 mg may be adequate in patients with central lines or after heart transplant.[[aha2025_als]] A dialysis catheter is a central line: give adenosine through it only with the physician&rsquo;s explicit dose decision, after aspirating the lock (Module 7). Tell the patient beforehand that they may feel a brief, frightening pause.</p>
<h3>Synchronized cardioversion</h3>
<p>Synchronized cardioversion delivers the shock on the R wave, avoiding the vulnerable part of the T wave where a shock can trigger VF. For atrial fibrillation, an initial energy of at least 200 J is reasonable, increased if it fails (COR 2a, LOE B-R); for atrial flutter, 200 J may be reasonable (COR 2b, LOE C-LD). For other tachycardias, use the device&rsquo;s recommended energy, or the maximum if unknown.[[aha2025_als]] Sedate whenever feasible. Polymorphic VT in an unstable patient is treated with an unsynchronized, high-energy shock, because the machine cannot reliably find an R wave to time to.</p>
{{fig:rl06_sync}}
{{key:Tachycardia with a pulse: unstable means synchronized cardioversion now. Stable means a 12-lead ECG, then regular or irregular, narrow or wide.}}
"""),
        ("dialysis", "Rhythms and the session", "Peri-arrest rhythms and the dialysis session", """
<p>Arrhythmias in dialysis patients follow the dialysis cycle: atrial fibrillation often begins during or around sessions,[[buiten2014]] and in an implanted-monitor study clinically significant arrhythmias clustered with the long interdialytic gap and the dialytic cycle.[[roychaudhury2018]] Both were observational. That pattern guides both what you look for and what you do with the machine.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Circuit decision</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td>Stable rhythm change during dialysis</td><td>Keep the monitor on; stop fluid removal per protocol; blood pump running</td><td>Physician-on-duty, with the attending nephrologist</td></tr>
<tr><td>Unstable rhythm during dialysis</td><td>Stop treatment per protocol while the team follows the algorithm; return the blood if the circuit is sound and the patient allows (Card 9)</td><td>Physician-on-duty</td></tr>
<tr><td>Slow rhythm with high potassium, patient stable enough</td><td>Dialysis is the treatment: do not stop without the attending nephrologist (Card 10)</td><td>Attending nephrologist</td></tr>
<tr><td>Rhythm lost: no pulse</td><td>Cardiac arrest: Module 7 circuit actions</td><td>Leader and circuit nurse</td></tr>
</tbody></table></div>
<p>The tension in the third row is real. A slow rhythm caused by high potassium is treated by removing potassium, and the patient is already connected to the device that removes it. Stopping dialysis because &ldquo;the patient is unstable&rdquo; may remove the only definitive treatment. Card 10, signed off for this Academy, says plainly: a connected, stable patient stays on the machine, and dialysis is not stopped without the attending nephrologist.</p>
{{key:Before stopping a session for a rhythm problem, ask whether dialysis is the cause or the cure. For potassium-driven bradycardia, it is the cure.}}
{{call:Any unstable rhythm, any new wide or very slow rhythm, or a rhythm change with chest pain: bring the defibrillator, call the physician-on-duty now, and follow your unit protocol. Always ask the attending nephrologist for guidance before stopping dialysis in a patient with high potassium.}}
"""),
    ],
    "debrief": ["""
<p><strong>Stable or unstable.</strong> Unstable. A heart rate of 36 with a pressure of 82/50, pallor and slow answers is bradycardia with cardiopulmonary compromise.</p>
<p><strong>Two problems.</strong> Diarrhea (hypovolemia), a beta-blocker, a missed weekend of potassium removal, and a slow wide rhythm: this pattern fits BRASH, in which a moderate potassium rise and a usual-dose AV-nodal blocker together slow the heart. It may also simply be severe hyperkalemia. Either way, potassium is treated now, without waiting 40 minutes for the result, because the ECG and the story are enough.</p>
<p><strong>The next ten minutes.</strong> Monitor and pads on (pacing ready). Oxygen if saturation is low. Atropine 1 mg is reasonable, but it often works poorly in potassium- and drug-driven block, so it must not delay the next steps. Per the unit order set: intravenous calcium to protect the membrane, insulin with glucose to shift potassium, a cautious saline bolus for the dehydration, and preparation for transcutaneous pacing or an epinephrine infusion if she does not improve. Call the attending nephrologist at once about connecting her for urgent dialysis, which is the definitive treatment, with a low-potassium plan set by the physician. If her pulse is lost, the team moves to cardiac arrest.</p>
"""],
    "skills": {"title": "Peri-arrest rhythm decisions",
               "intro": "In two simulator scenarios (one slow, one fast), make the stability decision and lead the first five minutes while a supervisor observes.",
               "items": [
                   ("Brings the defibrillator and monitor to the chair before telephoning.", True),
                   ("Judges stability by the five signs of compromise before treating the rate.", True),
                   ("For unstable bradycardia, gives atropine per protocol and escalates to pacing or an infusion without delay.", False),
                   ("Names BRASH as a possibility in a dialysis patient on an AV-nodal drug and treats potassium.", False),
                   ("For a regular narrow tachycardia, uses vagal maneuvers and adenosine with a rapid flush, per protocol.", False),
                   ("For unstable tachycardia, sets the defibrillator to synchronized mode, confirms sync markers, and calls clear.", True),
                   ("Does not stop dialysis in potassium-driven bradycardia without the attending nephrologist.", True),
               ],
               "placement": "With the physician-on-duty, review three saved rhythm strips from your unit and classify each by stability, regularity and QRS width."},
    "terms": [("Atrioventricular nodal blocker", "A drug that slows conduction through the AV node, such as a beta-blocker or diltiazem."),
              ("Escape rhythm", "A slow backup rhythm from lower in the heart when higher pacemakers fail."),
              ("Vagal maneuver", "An action such as a modified Valsalva that slows AV-node conduction."),
              ("Sync marker", "A mark the defibrillator places on each R wave to time a synchronized shock."),
              ("Polymorphic VT", "Ventricular tachycardia with changing QRS shapes; treated with an unsynchronized shock if unstable."),
              ("BRASH syndrome", "Bradycardia, renal failure, AV-nodal blockade, shock and hyperkalemia.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "The site guide to potassium and hyperkalemia.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
