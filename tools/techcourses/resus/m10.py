# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 10: Pediatric BLS and the Child Who Is Getting Worse. Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A pediatric dialysis nurse supporting the airway of a drowsy school-age child while a colleague brings a pediatric bag-mask.",
    "objectives": [
        "Apply the pediatric definitions (infant under about 1 year, child up to puberty) and choose the pediatric pathway early.",
        "Perform infant and child compressions using the 2025 techniques, depths and ratios, without the two-finger technique.",
        "Recognize respiratory failure as the usual road to pediatric arrest, and ventilate effectively with a correctly sized bag-mask.",
        "Start compressions for a heart rate under 60 with poor perfusion despite effective oxygenated ventilation, and escalate as the 2025 guideline recommends.",
        "Relieve severe choking in infants and children with the 2025 sequences, and use an AED with a pediatric attenuator when available.",
    ],
    "big": """
{{plain:In adults, the heart usually fails first and breathing stops because the heart stopped. In children it is usually the other way around. The lungs fail first; oxygen falls; the heart slows; and only then does it stop. That means you can often see a child&rsquo;s arrest coming, and the treatment that turns it around is usually air, not electricity.}}
<p>The picture has a limit. Children on dialysis are not typical children. Many have heart strain from high blood pressure and fluid overload, electrolyte swings like adults on dialysis, and access through a central catheter. A child on dialysis can also have a primary cardiac arrest, from potassium or a rhythm problem. So the pediatric rule &ldquo;think breathing first&rdquo; sits beside the dialysis rule &ldquo;think potassium and the circuit.&rdquo;</p>
<p>This module is essential for pediatric dialysis teams and recommended for every unit that ever treats an adolescent or a small adult. It follows the 2025 AHA and American Academy of Pediatrics (AAP) pediatric basic and advanced life support guidelines.[[aha2025_pbls]][[aha2025_pals]]</p>
{{cards:Key terms for this module|Infant::Younger than about 1 year (newborns follow neonatal guidance).|Child::From about 1 year to puberty; after puberty, adult guidance applies.|Respiratory failure::Breathing that can no longer keep oxygen and carbon dioxide safe.|Two-thumb encircling technique::Both hands around an infant&rsquo;s chest, thumbs compressing the sternum.|Pediatric attenuator::A pad or setting that reduces AED energy for small children.|Cardiopulmonary compromise::Signs that the heart and lungs are failing: poor perfusion, low blood pressure, altered mental status.}}
""",
    "case": {"title": "The child becoming quiet", "html": """
<p>Jun-Jun, 8, weighs 22 kg and has been on hemodialysis for six months through a tunneled catheter at a hospital pediatric dialysis unit in Manila. He gained 1.8 kg since his last session and arrives coughing, breathing fast at 40 a minute, with an oxygen saturation of 91% in room air. His mother says he slept sitting up.</p>
<p>Forty minutes into the session he becomes quiet. Pediatric dialysis nurse Ms. Aileen Cruz finds him drowsy and pale; his breathing is slow and shallow; saturation is 82%; his heart rate, 120 at the start, is now 54.</p>
""", "questions": ["What is happening to Jun-Jun, in physiological order?",
                  "What is the first treatment, and who does it?",
                  "At what point would you start compressions?"]},
    "sections": [
        ("definitions", "Who counts as a child", "Infant, child, adult: choose the pathway early", """
<p>The 2025 pediatric guidelines apply to infants younger than about 1 year (excluding newborns) and to children up to puberty; after the onset of puberty, adult guidance applies.[[aha2025_pbls]] In a pediatric dialysis unit, most patients are children; an adolescent with signs of puberty is treated with adult BLS, while weight-based drug dosing may still apply until adult doses are reached.</p>
{{fig:rl10_age_bands}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Infant</th><th>Child (to puberty)</th><th>After puberty</th></tr></thead>
<tbody>
<tr><td>Compression depth</td><td>At least one-third of the chest depth, about 4 cm</td><td>At least one-third of the chest depth, about 5 cm</td><td>5 to 6 cm</td></tr>
<tr><td>Technique</td><td>Two thumbs encircling, or heel of one hand</td><td>One or two hands</td><td>Two hands</td></tr>
<tr><td>Rate</td><td>100 to 120 a minute</td><td>100 to 120 a minute</td><td>100 to 120 a minute</td></tr>
<tr><td>Ratio, one rescuer</td><td>30:2</td><td>30:2</td><td>30:2</td></tr>
<tr><td>Ratio, two rescuers</td><td>15:2</td><td>15:2</td><td>30:2</td></tr>
<tr><td>With an advanced airway</td><td>Continuous compressions; a breath every 2 to 3 seconds</td><td>Same</td><td>Adult guidance</td></tr>
</tbody></table></div>
<p>The ratios and the advanced-airway rate come from the 2025 pediatric cardiac arrest algorithm; the 2025 PALS guideline suggests targeting 20 to 30 breaths a minute with an advanced airway (COR 2b, LOE C-LD).[[aha2025_pals]]</p>
{{key:Choose the pediatric pathway early: before puberty, use pediatric depth, technique and ratios (15:2 with two rescuers).}}
"""),
        ("technique", "Compressions and the AED", "Infant and child compressions in 2025", """
<p>The 2025 pediatric BLS guideline eliminated the two-finger technique for infant chest compressions, because it often fails to reach the needed depth. For infants, the recommended techniques are the two-thumb encircling hands technique or the heel of one hand; if the rescuer cannot encircle the chest, compress with the heel of one hand.[[aha2025_pbls]]</p>
{{fig:rl10_infant_technique}}
<p>For cardiac arrest in a child, the guideline recommends immediate application and use of an automated external defibrillator, with a pediatric attenuator if available.[[aha2025_pbls]] If no attenuator or pediatric pads are available, an adult AED is still used: a shock for VF matters more than the energy setting. Pediatric pads go anteroposterior on small children when they would otherwise touch.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Why it matters</th><th>Correction</th></tr></thead>
<tbody>
<tr><td>Two fingers on an infant&rsquo;s sternum</td><td>Too shallow</td><td>Two thumbs encircling, or the heel of one hand</td></tr>
<tr><td>Adult depth on a small child</td><td>Injury, no extra flow</td><td>One-third of the chest depth</td></tr>
<tr><td>30:2 with two rescuers before puberty</td><td>Too few breaths for a breathing-driven arrest</td><td>15:2</td></tr>
<tr><td>No AED because the child is small</td><td>VF untreated</td><td>Use an AED; attenuator if available</td></tr>
</tbody></table></div>
{{key:No more two-finger compressions: two thumbs encircling or the heel of one hand for infants. Use an AED in children, with an attenuator if you have one.}}
"""),
        ("breathing", "Breathing first", "Respiratory failure: the usual road to pediatric arrest", """
<p>Most pediatric cardiac arrests are hypoxic: the lungs fail, oxygen falls, the heart muscle and the conduction system become starved, and the heart slows before it stops. The slowing is a late sign and an urgent one. In a child on dialysis, the commonest reason is fluid overload causing pulmonary edema; others are pneumonia, aspiration, sedative or opioid effects, and seizures.</p>
{{fig:rl10_resp_failure}}
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you see</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Respiratory distress</td><td>Fast breathing, retractions, nasal flaring, prefers to sit up</td><td>Oxygen, sit up if possible, call the physician; review fluid status</td></tr>
<tr><td>Respiratory failure</td><td>Tiring, slowing or shallow breaths, falling saturation, drowsiness</td><td>Open the airway; bag-mask ventilation with oxygen; call for help</td></tr>
<tr><td>Bradycardia with poor perfusion</td><td>Heart rate falling, pale or mottled, weak pulses</td><td>Effective oxygenated ventilation first; compressions if rate stays under 60 with compromise</td></tr>
<tr><td>Arrest</td><td>No pulse, not breathing normally</td><td>Pediatric cardiopulmonary resuscitation (CPR)</td></tr>
</tbody></table></div>
<p>Bag-mask ventilation in a child needs the right mask size (from the bridge of the nose to the cleft of the chin, sparing the eyes), a smaller bag, and gentle breaths, just enough for chest rise. Effective ventilation alone often brings a slowing heart rate back up within seconds. For the dialysis circuit during respiratory distress, stop fluid removal only if the pressure is falling; in pulmonary edema, fluid removal may be part of the treatment, and that is the physician&rsquo;s decision.</p>
{{key:In children, the heart usually stops because breathing failed first. Effective bag-mask ventilation with oxygen is the treatment that breaks the chain.}}
"""),
        ("brady", "Bradycardia and choking", "Pediatric bradycardia, and choking", """
<p>For a child with bradycardia and cardiopulmonary compromise, the 2025 PALS guideline recommends starting CPR if the heart rate is under 60 a minute despite effective oxygenated ventilation (COR 1, LOE C-EO). If compromise persists after hypoxia and other causes are corrected, give intravenous or intraosseous epinephrine (COR 1, LOE C-EO). Atropine is recommended when bradycardia with compromise is caused by increased vagal tone or primary AV block, not by hypoxia (COR 1, LOE C-LD). Emergency transcutaneous pacing may be considered for complete heart block or sinus node dysfunction that does not respond to CPR (COR 2b, LOE C-EO).[[aha2025_pals]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Child&rsquo;s state</th><th>Action (PALS 2025)</th></tr></thead>
<tbody>
<tr><td>Slow heart rate, perfusing well</td><td>Oxygen, monitor, find the cause (potassium, drugs, hypoxia)</td></tr>
<tr><td>Slow rate with compromise</td><td>Effective oxygenated ventilation first</td></tr>
<tr><td>Still under 60 with compromise despite ventilation</td><td>Start CPR</td></tr>
<tr><td>Compromise persists after correcting hypoxia</td><td>IV or IO epinephrine</td></tr>
<tr><td>Vagal cause or primary AV block</td><td>Atropine</td></tr>
</tbody></table></div>
<h3>Choking</h3>
<p>The 2025 pediatric BLS guideline separates infants and children. For an infant with severe foreign-body airway obstruction: repeated cycles of 5 back blows alternating with 5 chest thrusts, and no abdominal thrusts. For a child: repeated cycles of 5 back blows alternating with 5 abdominal thrusts.[[aha2025_pbls]] If the child becomes unresponsive, start CPR.</p>
{{fig:rl10_ratios}}
{{key:Heart rate under 60 with poor perfusion despite good ventilation: start compressions. Infant choking: back blows and chest thrusts; child choking: back blows and abdominal thrusts.}}
{{call:A child on dialysis who is tiring, desaturating, drowsy or slowing: call for help and the pediatric cart, ventilate, and call the physician-on-duty and the attending pediatric nephrologist now. Follow your unit protocol.}}
"""),
    ],
    "debrief": ["""
<p><strong>The physiology.</strong> Fluid gain of 1.8 kg in a 22 kg child, cough, orthopnea and fast breathing point to pulmonary edema. Over 40 minutes he moved from respiratory distress to respiratory failure: slow, shallow breaths, a saturation of 82%, drowsiness. The falling heart rate (120 to 54) is hypoxic bradycardia, a sign that arrest is close.</p>
<p><strong>The first treatment.</strong> Ms. Cruz calls for help and the pediatric cart, opens the airway, and starts bag-mask ventilation with oxygen using a correctly sized mask, while a second nurse attaches the monitor and pads. Effective ventilation is the treatment most likely to bring his heart rate up. The physician-on-duty and the attending pediatric nephrologist are called; the circuit decision (whether fluid removal continues for the edema or stops for low pressure) is theirs.</p>
<p><strong>Compressions.</strong> If, despite effective oxygenated ventilation, his heart rate stays under 60 a minute with poor perfusion, the team starts pediatric CPR: one-third of the chest depth, 100 to 120 a minute, 15:2 with two rescuers. If compromise persists after hypoxia is corrected, intravenous epinephrine is given by weight (Module 11). If he loses his pulse, the pediatric cardiac arrest algorithm begins.</p>
"""],
    "skills": {"title": "Pediatric BLS and early recognition",
               "intro": "On infant and child manikins, perform compressions, bag-mask ventilation and a choking sequence while a supervisor observes.",
               "items": [
                   ("Chooses the pediatric pathway correctly by age and signs of puberty.", False),
                   ("Compresses an infant with two thumbs encircling or the heel of one hand, never two fingers.", True),
                   ("Compresses one-third of the chest depth at 100 to 120 a minute with full recoil.", True),
                   ("Uses 15:2 with two rescuers before puberty.", True),
                   ("Selects the correct mask size and ventilates with visible chest rise.", True),
                   ("Starts compressions for a heart rate under 60 with poor perfusion despite effective ventilation.", True),
                   ("Demonstrates infant (back blows and chest thrusts) and child (back blows and abdominal thrusts) choking sequences.", False),
                   ("Uses an AED with a pediatric attenuator when available, or an adult AED when not.", False),
               ],
               "placement": "Check the pediatric cart in your unit for mask and bag sizes, pediatric pads and attenuator, and list anything missing."},
    "terms": [("Infant", "Younger than about 1 year, excluding newborns."),
              ("Puberty", "The point after which adult resuscitation guidance applies."),
              ("Hypoxic bradycardia", "Slowing of the heart caused by low oxygen."),
              ("Pediatric attenuator", "A device that lowers AED energy for small children."),
              ("Retractions", "Skin pulling in between or under the ribs with each breath, a sign of distress."),
              ("Orthopnea", "Breathlessness lying flat, eased by sitting up.")],
    "readings": [("pediatric-dialysis-nurse-15-emergencies-and-resuscitation.html", "Pediatric Dialysis Nurse Module 15: emergencies and resuscitation.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
