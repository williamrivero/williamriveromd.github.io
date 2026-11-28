# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 11: Pediatric Arrest and Rhythms During Dialysis. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two pediatric nurses double-checking a syringe label against a weight-based dose card beside a child on a small dialysis bed.",
    "objectives": [
        "Run the pediatric cardiac arrest algorithm, timing epinephrine for shockable and nonshockable rhythms as the 2025 PALS guideline recommends.",
        "Calculate weight-based epinephrine, amiodarone and lidocaine doses and volumes, and defibrillation energies, saying units and concentrations aloud with a second check.",
        "Avoid concentration errors by distinguishing adult arrest, pediatric arrest and anaphylaxis epinephrine preparations.",
        "Manage pediatric supraventricular tachycardia with vagal maneuvers, adenosine and synchronized cardioversion by weight.",
        "Apply the circuit decisions to a child, including extracorporeal volume relative to blood volume and the risks of an uncertain weight.",
    ],
    "big": """
{{plain:In an adult arrest, the drug doses are the same for almost everyone, and the team can say them from memory. In a child, every dose, every volume and every energy is a small calculation. Under stress, small calculations go wrong by a factor of ten. The safest pediatric code is the one where nobody calculates in their head.}}
<p>The picture has a limit. Weight-based dosing is not only about arithmetic. It also depends on knowing the right weight (a dialysis child&rsquo;s weight changes with fluid), the right concentration (the same drug comes in several), and the right maximum (a large child reaches adult doses). So the system matters more than the calculation: a written dose card or a length-based tape, a second person who repeats every dose and volume, and labeled syringes.</p>
<p>This module applies the 2025 AHA and American Academy of Pediatrics pediatric advanced life support guideline to the child on dialysis.[[aha2025_pals]] The numbers below are those printed on the 2025 pediatric algorithms, quoted so you can recognize and check them. Give drugs only within your license and your unit&rsquo;s approved protocol.</p>
{{cards:Key terms for this module|Weight-based dose::A dose calculated per kilogram of body weight, up to a maximum.|Concentration::The amount of drug in each milliliter, such as 0.1 mg/mL.|Length-based tape::A tape laid beside a child that gives an estimated weight and doses by length.|Extracorporeal volume (ECV)::The blood held in the dialyzer and lines.|Synchronized cardioversion::A shock timed to the R wave, used for unstable tachycardia with a pulse.|Expert consultation::Advice from a pediatric cardiologist or intensivist, recommended for complex rhythms.}}
""",
    "case": {"title": "Pediatric arrest during dialysis", "html": """
<p>Mika, 6, has been on hemodialysis for two years through a tunneled catheter. Her dry weight was 19 kg last month; today&rsquo;s pre-dialysis weight was recorded as 21 kg, but the scale reading was later questioned. One hour into the session she becomes unresponsive and pulseless. The monitor shows a slow, wide rhythm, then a flat line confirmed in two leads.</p>
<p>The team starts compressions. The drug nurse asks, &ldquo;Epinephrine, how much?&rdquo; Someone reads the adult ampule label aloud: &ldquo;1 mg per mL.&rdquo;</p>
""", "questions": ["What is the nonshockable plan, and when is epinephrine given?",
                  "What weight do you use, and how do you prevent a tenfold error?",
                  "What happens to the circuit blood, and why does it matter more in a 19 kg child?"]},
    "sections": [
        ("algorithm", "The pediatric arrest algorithm", "Pediatric arrest: two paths again", """
<p>The pediatric cardiac arrest algorithm has the same two-path shape as the adult one: high-quality CPR in two-minute cycles, a rhythm check, shock for VF or pulseless VT, epinephrine and a search for causes for asystole or PEA.[[aha2025_pals]] The differences are the doses, the energies, the ventilation, and how often the arrest is hypoxic.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>2025 PALS recommendation</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Epinephrine, nonshockable</td><td>Initial dose as early as possible</td><td>COR 2a, LOE C-LD</td></tr>
<tr><td>Epinephrine, shockable</td><td>After 2 attempts at defibrillation, or sooner only when rapid defibrillation is not possible</td><td>COR 2b, LOE C-LD</td></tr>
<tr><td>Epinephrine repeat</td><td>Every 3 to 5 minutes until ROSC</td><td>COR 2b, LOE C-LD</td></tr>
<tr><td>First shock</td><td>2 to 4 J/kg; 2 J/kg is reasonable for ease of teaching</td><td>COR 2a, LOE C-LD</td></tr>
<tr><td>Later shocks</td><td>4 J/kg; higher may be considered, not above 10 J/kg or the adult maximum</td><td>COR 2b, LOE C-LD</td></tr>
<tr><td>Antiarrhythmic, shock-refractory VF/pVT</td><td>Amiodarone or lidocaine may be considered</td><td>COR 2b, LOE C-LD</td></tr>
<tr><td>Ventilation with an advanced airway</td><td>20 to 30 breaths a minute</td><td>COR 2b, LOE C-LD</td></tr>
</tbody></table></div>
<p>Reversible causes in a child on dialysis include all the adult dialysis causes (potassium, volume, bleeding from the access, air, low calcium, low glucose) plus the pediatric ones that dominate: hypoxia and acidosis from respiratory failure.</p>
{{fig:rl11_energies}}
{{key:Pediatric arrest: epinephrine as early as possible for asystole and PEA; shocks of 2, then 4 J/kg (up to 10 J/kg or the adult dose) for VF and pulseless VT.}}
"""),
        ("doses", "Doses aloud", "Weight, dose, volume, concentration: said aloud, checked twice", """
<p>The 2025 pediatric cardiac arrest algorithm prints these drug doses: epinephrine 0.01 mg/kg IV or IO (0.1 mL/kg of the 0.1 mg/mL concentration), maximum 1 mg; amiodarone 5 mg/kg bolus (maximum 300 mg), which may be repeated up to 3 doses; or lidocaine 1 mg/kg.</p>
{{fig:rl11_weight_dose}}
<div class="table-wrap"><table>
<thead><tr><th>For a 20 kg child (teaching example)</th><th>Dose</th><th>Volume</th><th>Check</th></tr></thead>
<tbody>
<tr><td>Epinephrine, 0.1 mg/mL</td><td>0.01 &times; 20 = 0.2 mg</td><td>0.2 mg &divide; 0.1 mg/mL = 2 mL</td><td>Below the 1 mg maximum</td></tr>
<tr><td>Amiodarone (concentration per your stock)</td><td>5 &times; 20 = 100 mg</td><td>Depends on the ampule concentration</td><td>Below the 300 mg maximum</td></tr>
<tr><td>Lidocaine</td><td>1 &times; 20 = 20 mg</td><td>Depends on the concentration</td><td>&mdash;</td></tr>
<tr><td>First shock</td><td>2 &times; 20 = 40 J</td><td>&mdash;</td><td>Nearest device setting</td></tr>
<tr><td>Second shock</td><td>4 &times; 20 = 80 J</td><td>&mdash;</td><td>Later shocks up to 10 J/kg or adult dose</td></tr>
</tbody></table></div>
<p>The weight used is the one your unit protocol names. For a dialysis child, that is usually the most recent reliable weight; a questioned scale reading should not be used. A length-based tape gives an estimate when no reliable weight exists. Every dose follows the same spoken pattern: &ldquo;Mika, 20 kilograms. Epinephrine 0.2 milligrams, which is 2 milliliters of 0.1 milligrams per milliliter.&rdquo; The second nurse repeats it and checks the syringe label. The <a href="calc-resuscitation-lab-toolkit.html#tool-3">pediatric dose-and-volume trainer</a> lets your team practice this arithmetic with the steps shown; it is a teaching tool, not a bedside calculator.</p>
{{key:Name the weight, the dose in milligrams, the volume in milliliters and the concentration, aloud; a second person repeats and checks the label.}}
"""),
        ("concentrations", "Concentration traps", "One drug, three concentrations", """
<p>Epinephrine is the drug most often involved in tenfold errors in resuscitation, because the same name covers preparations that differ ten-fold or more, used by different routes for different problems.</p>
{{fig:rl11_concentrations}}
<div class="table-wrap"><table>
<thead><tr><th>Preparation</th><th>Use</th><th>Route</th><th>Danger if confused</th></tr></thead>
<tbody>
<tr><td>1 mg/mL (1:1,000)</td><td>Anaphylaxis with a pulse</td><td>Intramuscular, outer thigh</td><td>Given IV as if 0.1 mg/mL: a tenfold overdose</td></tr>
<tr><td>0.1 mg/mL (1:10,000), or 1 mg/mL diluted to 10 mL</td><td>Cardiac arrest, adult and pediatric</td><td>IV or IO</td><td>Given IM in anaphylaxis: too little</td></tr>
<tr><td>Dilute infusion</td><td>Bradycardia or shock with a pulse</td><td>IV infusion, titrated</td><td>Bolus of infusion concentration</td></tr>
</tbody></table></div>
<p>In the case, someone read the adult ampule label aloud: 1 mg/mL. Drawing 2 mL of that for Mika would give 2 mg, ten times her dose. The safe system is to keep the arrest concentration (0.1 mg/mL, or a prepared dilution) separate and labeled, to dilute ampules only in a standard way set by protocol, and to say the concentration every time.</p>
{{key:Before every pediatric epinephrine dose, say the concentration aloud. For arrest, it is 0.1 mg/mL: 0.1 mL/kg.}}
"""),
        ("rhythms", "Tachycardia and the circuit", "Pediatric tachycardia, and the circuit in a child", """
<p>For pediatric supraventricular tachycardia without compromise, the 2025 PALS guideline recommends vagal stimulation first (COR 1, LOE C-LD), then intravenous or intraosseous adenosine if access is ready (COR 1, LOE C-LD), and expert consultation if both fail. For SVT with cardiopulmonary compromise, synchronized cardioversion starting at 0.5 to 1 J/kg, increased to 2 J/kg if unsuccessful, is reasonable (COR 2a, LOE C-LD); the same energies apply to wide-complex tachycardia with compromise (COR 2a, LOE C-EO).[[aha2025_pals]] The 2025 pediatric tachyarrhythmia algorithm prints adenosine 0.1 mg/kg (maximum 6 mg) as a rapid push with a flush, and a repeat dose of 0.2 mg/kg (maximum 12 mg).</p>
<h3>The circuit in a child</h3>
<p>The circuit decisions of Module 7 apply, with one difference: the blood in the circuit is a larger share of a small child&rsquo;s blood volume. Pediatric dialysis practice estimates blood volume at about 80 mL/kg in children, and European pediatric guidance states that total extracorporeal volume should be approximately less than 10% of blood volume.[[pdn_fischbach2005]] For a 19 kg child, blood volume is about 1,520 mL, and 10% is about 152 mL.</p>
{{fig:rl11_ecv}}
<div class="table-wrap"><table>
<thead><tr><th>Circuit question</th><th>In a small child</th></tr></thead>
<tbody>
<tr><td>Return the blood?</td><td>Returning it matters more for volume, unless air, hemolysis, a reaction or an open line forbids it</td></tr>
<tr><td>Blood-primed circuit?</td><td>The blood is donor blood; the pediatric nephrologist decides whether to return it</td></tr>
<tr><td>Saline bolus</td><td>By weight, per protocol: in septic shock, PALS uses 10 or 20 mL/kg boluses with reassessment (COR 2a, LOE C-LD)</td></tr>
<tr><td>Access for drugs</td><td>Aspirate the catheter lock first; limb volumes are small, so dead space matters</td></tr>
</tbody></table></div>
<p>The <a href="calc-pediatric-dialysis-nurse-toolkit.html#tool-2">extracorporeal volume check</a> in the Pediatric Dialysis Nurse toolkit computes the circuit share for your lines and dialyzer.</p>
{{key:In a small child, the circuit holds a large share of the blood. Return it unless air, hemolysis, a reaction or an open line forbids it, and let the pediatric nephrologist decide about blood-primed circuits.}}
{{call:Any child on dialysis who is pulseless, has a rhythm with compromise, or needs a weight-based resuscitation drug: call for help, the pediatric cart and the dose card, and call the attending pediatric nephrologist. Follow your unit protocol; every dose is checked by a second person.}}
"""),
    ],
    "debrief": ["""
<p><strong>The plan.</strong> A flat line confirmed in two leads in a pulseless child is asystole: the nonshockable path. Compressions at one-third of the chest depth, 15:2 with two rescuers, and epinephrine as early as possible, then every 3 to 5 minutes. Causes: potassium (a slow wide rhythm came first), hypoxia, volume, bleeding at the catheter, air.</p>
<p><strong>The weight and the error.</strong> The questioned 21 kg reading is not used; the unit protocol names the most recent reliable weight, 19 kg (or a length-based tape estimate). Epinephrine is 0.01 mg/kg = 0.19 mg, which many protocols round to 0.2 mg: 2 mL of the 0.1 mg/mL concentration. The person who read &ldquo;1 mg per mL&rdquo; has identified the trap: 2 mL of the ampule would be 2 mg, a tenfold overdose. The drug nurse says the weight, dose, volume and concentration aloud, and a second nurse repeats and checks.</p>
<p><strong>The circuit.</strong> The circuit nurse stops fluid removal and the pump. With no air, hemolysis or reaction, the blood is returned or clamped per protocol; in a 19 kg child (blood volume about 1,520 mL) the circuit blood is a large share of her volume, so returning it matters. The catheter lock is aspirated before the limb is used for drugs. The attending pediatric nephrologist is called.</p>
"""],
    "skills": {"title": "Pediatric megacode with dose checks",
               "intro": "Lead or act as drug nurse in a pediatric megacode on a manikin while a supervisor observes.",
               "items": [
                   ("Uses the protocol weight (reliable recent weight or length-based tape) and states it aloud.", True),
                   ("Calculates and states epinephrine dose in mg and volume in mL of 0.1 mg/mL, below the 1 mg maximum.", True),
                   ("Has every dose repeated and the syringe label checked by a second person.", True),
                   ("Times epinephrine as early as possible for nonshockable rhythms and after two shocks for shockable rhythms.", False),
                   ("Selects 2 J/kg then 4 J/kg, not exceeding 10 J/kg or the adult dose.", True),
                   ("For SVT with compromise, selects synchronized cardioversion at 0.5 to 1 J/kg, then 2 J/kg.", False),
                   ("States the circuit blood decision and the extracorporeal volume share for the child.", False),
               ],
               "placement": "With the pediatric nephrologist, make or review your unit&rsquo;s pediatric dose card for the weights you treat."},
    "terms": [("Weight-based dosing", "Doses calculated per kilogram, up to a maximum."),
              ("Length-based tape", "A tape that estimates weight and doses from a child&rsquo;s length."),
              ("Tenfold error", "A dose ten times too high or low."),
              ("Extracorporeal volume", "The blood held in the dialyzer and lines."),
              ("Blood prime", "Filling the circuit with donor blood before connection in a small child."),
              ("Dead space", "The volume in a line or catheter limb that must be cleared before a drug reaches the patient.")],
    "readings": [("pediatric-dialysis-nurse-15-emergencies-and-resuscitation.html", "Pediatric Dialysis Nurse Module 15: emergencies and resuscitation.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-3", "calc-pediatric-dialysis-nurse-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["11"])
