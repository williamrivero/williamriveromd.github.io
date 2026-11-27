# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 08: Mechanical, volume and urgent problems.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain the mechanisms of outflow failure, dialysate leaks, hernias and pleural leaks from the pressure physiology of a fluid-filled abdomen.",
        "Triage poor drainage, leaks, swelling, pain on inflow or outflow, and fluid overload by urgency.",
        "Recognize the emergencies that override routine troubleshooting.",
        "Prepare patients for power interruptions, typhoons, floods and supply disruption.",
        "Escalate with the data the team needs and avoid unsafe manipulation.",
    ],
    "big": """
<p>Most mechanical problems in peritoneal dialysis (PD) are fixable if found early and handled gently. A constipated bowel pushing the catheter out of the pelvis, a leak tracking into the abdominal wall, a slowly growing hernia: none of these is an emergency on day one. Each can become one if it is missed, or if someone forces fluid through a blocked catheter at midnight.</p>
<p>Your work is to sort the urgent from the routine, to protect the catheter, and to keep the patient safe when the power or the supply chain fails. Most of the skill lies in asking the right questions in the right order before anyone touches anything.</p>
{{plain:Think of the abdomen filled with dialysate as a water balloon inside a box. Pressure rises with every liter, and it rises more when the patient sits, strains, coughs or lifts. That pressure pushes fluid toward any weak point: the catheter tunnel, an old incision, the groin, a small gap in the diaphragm.}}
<p>The picture has a limit. A balloon has uniform walls. The abdomen has known weak points, and a bowel that moves and can displace the catheter. Pressure also affects breathing and the return of blood to the heart, which is why large fills can cause breathlessness or discomfort in some patients.</p>
{{cards:Key terms for this module|Outflow failure::Fill is normal but drain is slow or incomplete.|Pericatheter leak::Dialysate escaping along the catheter tunnel to the exit site.|Hernia::A bulge of abdominal contents through a weak point in the wall.|Hydrothorax::Dialysate leaking into the chest through a gap in the diaphragm.|Strangulation::Loss of blood supply to bowel trapped in a hernia; an emergency.}}
""",
    "case": {"title": "Three pillows at 9 PM", "html": """
<p><strong>Mr. Dante Ramos, 60</strong>, a retired security guard on CAPD for two years, lives with his wife in Valenzuela. He calls the PD hotline at 9 PM. Nurse <strong>Liezl</strong> answers.</p>
<p><strong>9:00 PM.</strong> Over three days his drain volumes have fallen from about 2,300 to 1,500 mL per exchange. He has not moved his bowels in five days. Tonight he felt breathless lying down and needed three pillows. He asks whether he should do an extra exchange with the strongest bag to &ldquo;pull the water out.&rdquo;</p>
""", "questions": ["Which detail changes this from a drain problem to an emergency?",
                  "Should you try position changes over the phone?",
                  "What goes into the handoff?"]},
    "sections": [
        ("mechanisms-and-what", "Mechanisms", "Mechanisms and what you see", """
<p>Each problem in this module follows from two facts: a full abdomen is under pressure, and the catheter sits among organs that move.</p>
{{fig:pd08_weak}}
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Mechanism</th><th>What you see</th><th>Urgency</th></tr></thead>
<tbody>
<tr><td>Outflow failure</td><td>Constipated bowel displaces the catheter; tip migrates out of the pelvis; kinked tubing; fibrin plug; omentum wraps the catheter</td><td>Fill normal, drain slow or incomplete; drain alarms; UF falls</td><td>Same-day call if persistent; urgent if pain, fever or cloudy effluent</td></tr>
<tr><td>Pericatheter leak</td><td>Fluid tracks along the tunnel, especially early after insertion or with large fills</td><td>Wet dressing, clear fluid at the exit site (glucose-positive on testing per protocol)</td><td>Same day; the team decides whether to hold or reduce PD</td></tr>
<tr><td>Abdominal wall or genital leak</td><td>Fluid dissects into tissue planes</td><td>Uneven abdominal wall swelling, scrotal or labial swelling, falling UF</td><td>Same day</td></tr>
<tr><td>Hernia</td><td>Raised pressure enlarges a weakness</td><td>Painless bulge that grows with fill</td><td>Routine to same day; <strong>urgent if painful, firm, red or with vomiting (possible strangulation)</strong></td></tr>
<tr><td>Pleural leak (hydrothorax)</td><td>Dialysate crosses a gap in the diaphragm, more often on the right</td><td>New breathlessness, especially after fills; falling UF</td><td><strong>Urgent; stop fills and call</strong></td></tr>
<tr><td>Pain on inflow</td><td>Solution temperature, acidity, rapid inflow, catheter jet</td><td>Pain at the start of fill</td><td>Routine review; urgent if persistent or with cloudy effluent</td></tr>
<tr><td>Pain at end of drain</td><td>Catheter tip against bowel or bladder as fluid empties</td><td>Pain in the last minutes of drain</td><td>Routine review; the team often considers tidal APD</td></tr>
<tr><td>Hemoperitoneum</td><td>Menstruation, ovulation, minor trauma, rarely serious bleeding inside the abdomen</td><td>Blood-tinged effluent</td><td>Report; urgent if heavy, persistent, or with pain or low blood pressure</td></tr>
<tr><td>Fluid overload</td><td>Falling UF, falling urine, missed therapy, intake</td><td>Weight gain, edema, high blood pressure, breathlessness</td><td>Same day; <strong>emergency if breathless at rest, chest pain or low oxygen</strong></td></tr>
</tbody></table></div>
<h3>Example: four calls, four mechanisms</h3>
<p><strong>Mrs. Linda</strong>, nine days after an urgent-start catheter, finds her gauze soaked with clear fluid after each fill. A pericatheter leak is likely; the tunnel has not sealed. You arrange same-day review, and the team decides on smaller fills, lying down, or a pause.</p>
<p><strong>Mang Pedring</strong> carries sacks of rice for his store. A soft bulge in his right groin has grown over two months and is bigger after each fill. It is painless and goes back when he lies down. You report it for review and teach him the signs that would make it an emergency.</p>
<p><strong>Ms. Weng</strong> notices that her right side feels heavy and she is breathless after every fill, but fine after draining. Her UF has dropped. A pleural leak is possible. She stops fills and you call the team urgently.</p>
<p><strong>Mr. Celso</strong> says his belly looks lopsided, the left side swollen and doughy, and his UF has fallen. He may have a leak into the abdominal wall. Same-day review.</p>
<h3>A rare late complication</h3>
<p>Encapsulating peritoneal sclerosis is a rare, serious late complication in which the peritoneum thickens and encases the bowel. Symptoms include recurrent bowel obstruction, weight loss and falling UF, sometimes after PD has stopped. Report persistent obstructive symptoms in long-term or former PD patients.</p>
{{key:Ask which phase the problem happens in and where the fluid is going. The answer usually names the mechanism.}}
"""),
        ("assess-first", "Assess first", "Assess first", """
<p>Before any troubleshooting, ask:</p>
<ul>
<li>When did it start?</li>
<li>Which phase: fill, dwell or drain?</li>
<li>How much therapy was completed?</li>
<li>Pain? Where?</li>
<li>Effluent clarity?</li>
<li>Bowel pattern?</li>
<li>Recent surgery, lifting or trauma?</li>
<li>Swelling anywhere: abdomen, groin, genitals, legs?</li>
<li>Breathing: at rest, lying flat, after fills?</li>
</ul>
<p><strong>Screen for emergencies:</strong> severe abdominal pain, breathlessness at rest or respiratory distress, fainting, altered thinking, unstable vital signs, signs of sepsis, a painful hernia that will not go back, heavy bleeding. These go to the emergency pathway. Any cloudy effluent or abdominal pain also activates the peritonitis pathway (Module 7).</p>
<h3>Why the order matters</h3>
<p>The question about breathing comes before the question about position. A patient with a slow drain who is comfortable can safely try walking or changing sides. A patient with a slow drain who is breathless at rest may be fluid overloaded or have fluid in the chest, and asking them to keep trying exchanges wastes time they do not have.</p>
{{call:Send the patient through the emergency pathway, and call the nephrologist, for breathlessness at rest, chest pain, fainting, confusion, a painful irreducible hernia or heavy bleeding. Do not troubleshoot the catheter first.}}
"""),
        ("safe-troubleshooting", "Safe troubleshooting", "Safe troubleshooting", """
<p>Permitted, if the patient is stable and the unit protocol allows: check the clamps; look for kinks along the line; change position (stand, walk, lean, lie on the other side); confirm the cycler or bag height; ask about bowel movements.</p>
{{fig:pd08_triage}}
<p><strong>Not permitted unless specifically ordered and trained:</strong> forceful flushing with a syringe, aspiration, inserting anything into the catheter, unapproved cycler overrides, or continuing fills when a leak or breathlessness is present. Treatments such as intraperitoneal heparin for fibrin, laxatives, imaging and catheter repositioning are prescriber decisions.[[pd_crabtree2019]]</p>
<h3>Example: a slow drain, handled well</h3>
<p>Mrs. Tess calls at 7 PM. Her drain has been running 40 minutes and only 900 mL has come out. Nurse Liezl asks about pain (none), breathing (normal), effluent (clear) and bowels (two days without). She asks Mrs. Tess to check that both clamps are open and to trace the line for kinks. One clamp is half closed. The drain resumes.</p>
<p>Liezl still documents the call and asks about bowels, because two days without a movement in a patient who usually goes daily is the kind of detail that explains next week&rsquo;s drain problem. She teaches the bowel plan the team has ordered.</p>
<h3>Example: what not to do</h3>
<p>A relative who is a nursing student tries to &ldquo;unblock&rdquo; a slow catheter with a syringe of saline at home. The catheter now drains even less and the patient has pain. Force can push a fibrin plug deeper, tear tissue or introduce bacteria. A fixable problem has become a procedure.</p>
{{key:Gentleness protects the catheter. Force can make a fixable problem permanent.}}
"""),
        ("anticipate-disruption", "Disruption", "Anticipate disruption", """
<p>The Philippines sees typhoons, floods, earthquakes, brownouts and heat waves. PD can continue through many of these if the patient has planned. The plan is made in the dry season and checked before the rains, not invented during the storm.</p>
<p>At training, and every few months after, review:</p>
<div class="table-wrap"><table>
<thead><tr><th>Plan element</th><th>What the patient should know or have</th></tr></thead>
<tbody>
<tr><td>Contacts</td><td>PD unit hours, after-hours number, backup contact, nearest emergency department</td></tr>
<tr><td>Supplies</td><td>At least the reserve the program recommends; storage off the floor and away from floodwater</td></tr>
<tr><td>Power</td><td>For APD: a prescribed backup CAPD regimen, supplies for it and validated competence; whom to tell about planned outages</td></tr>
<tr><td>Evacuation</td><td>A go-bag with solutions, connection supplies, caps, medicines, records and the current order</td></tr>
<tr><td>Missed therapy</td><td>How to report it; which symptoms mean urgent care</td></tr>
<tr><td>Heat</td><td>Storage temperature limits for solutions; recognizing dehydration versus overload</td></tr>
</tbody></table></div>
<h3>Example: a family in an evacuation center</h3>
<p>Typhoon floodwater forces Mrs. Aurora&rsquo;s family into the barangay covered court. She brings her go-bag: two days of solutions, caps, masks, her medicines, her prescription card and the PD unit&rsquo;s number. The court has no clean private space. Her son hangs a blanket across a corner near the barangay health station, and she does her exchanges there with sanitizer and a clean towel laid on a folding table, as she was taught for emergencies.</p>
<p>She calls the PD unit on the second day. The nurse checks how many exchanges she has done, her weight if a scale is available, the clarity of her effluent and how many bags remain. The supplier is contacted to deliver to the evacuation center. Without the go-bag, she would have missed two days of dialysis.</p>
<h3>Example: heat and the wrong conclusion</h3>
<p>During a heat wave, Mr. Joel feels dizzy and his weight is down 1.5 kg. His wife suggests he drink more and &ldquo;use the weaker bag.&rdquo; Dizziness and weight loss in heat may mean he is too dry. Changing solution strength is the prescriber&rsquo;s decision. You assess blood pressure, intake, sweating and urine, and call the team the same day.</p>
<p>The site&rsquo;s guides on typhoon and disaster preparedness and on heat and dialysis give patient-facing language you can reuse.</p>
{{key:A disaster plan works only if it exists before the disaster. Check it before every rainy season.}}
{{fig:pd08_fig_08_typhoon_go_bag_plan}}
"""),
    ],
    "debrief": ["""
<p><strong>9:03 PM.</strong> Liezl asks: Is he breathless at rest now? &ldquo;A bit, even sitting.&rdquo; Chest pain? No. Confusion? No. Swelling? Legs up to the knees. Effluent? Clear. Abdominal pain? Bloated, not severe.</p>
<p><strong>Which detail changes everything.</strong> Breathlessness at rest. Falling drains and constipation alone are a same-day problem. Breathlessness at rest suggests acute fluid overload, or possibly a pleural leak, and makes this an emergency.</p>
<p><strong>Position changes over the phone?</strong> No. Liezl does not try position changes, and she tells him not to do an extra exchange with the strongest bag on his own. Changing the solution is a prescription decision, and more troubleshooting would only delay care.</p>
<p><strong>9:05 PM, the handoff.</strong> She directs urgent emergency evaluation through the local pathway and tells his wife to call an ambulance if he worsens. She calls the nephrologist on duty with SBAR: last completed exchange, drain volumes over three days, weight if known, bowel history, breathlessness at rest, clear effluent, and his question about the strong bag.</p>
<p><strong>Next day.</strong> After he is stabilized, the team addresses constipation and catheter function. Liezl arranges a bowel-care teaching session and a follow-up drain check.</p>
<p><strong>Take-home.</strong> Breathlessness at rest turns a drain problem into an emergency. Troubleshoot later.</p>
"""],
    "skills": {"title": "After-hours outage call",
               "intro": "Simulate an after-hours power-failure call for an APD patient. Confirm stability, whether the patient is connected, how much therapy was delivered, whether a prescribed backup plan exists, supplies on hand, and when power is expected back. Document and close the loop.",
               "items": [("Confirms the patient is stable before troubleshooting.", True),
                         ("Confirms connection status and therapy delivered.", False),
                         ("Confirms a prescribed backup plan, supplies and validated competence before backup CAPD.", True),
                         ("Uses only permitted external checks.", True),
                         ("Documents and closes the loop with a named clinician.", False)]},
    "quiz": [
        ("Which finding changes low-drain troubleshooting into an emergency response?",
         ["New breathlessness at rest", "Mild bloating", "One drain 100 mL lower than usual", "A request for diet advice"], 0,
         "Breathlessness at rest may mean acute fluid overload or a pleural leak. The others are routine to same-day concerns."),
        ("What is a common reversible cause of outflow failure in many programs?",
         ["Wrong solution brand", "High blood pressure", "Constipation displacing the catheter", "Exit-site crust"], 2,
         "A loaded bowel can push the catheter tip out of the pelvis. Bowel care often restores drainage."),
        ("Which action is unsafe without a specific order and training?",
         ["Checking clamps", "Changing position", "Checking for kinks", "Forceful syringe flushing of the catheter"], 3,
         "Force can push a plug deeper, tear tissue or introduce bacteria. The other checks are permitted when the patient is stable."),
        ("Ms. Weng has new right-sided heaviness and breathlessness after every fill, with falling UF. This suggests:",
         ["Hernia", "Pleural leak (hydrothorax); stop fills and call urgently", "Constipation", "Exit-site infection"], 1,
         "Dialysate may be crossing into the chest. Stop fills and call."),
        ("Mang Pedring has a painless groin bulge that grows with fills and goes back when he lies down. This is most likely:",
         ["Peritonitis", "A hernia; report for review and teach the warning signs", "Normal", "A pleural leak"], 1,
         "It becomes urgent if painful, firm, red or accompanied by vomiting."),
        ("A painful, firm, red hernia with vomiting requires:",
         ["A routine clinic visit", "Larger fills", "Exit-site care", "Emergency evaluation for possible strangulation"], 3,
         "Bowel trapped in a hernia can lose its blood supply."),
        ("Mrs. Linda&rsquo;s gauze soaks with clear fluid after each fill, nine days after an urgent-start catheter. This suggests:",
         ["A pericatheter leak; same-day report", "Peritonitis", "Normal sweat", "Hydrothorax"], 0,
         "The tunnel has not sealed. The team decides on smaller fills, position or a pause."),
        ("Uneven, doughy abdominal wall swelling with falling UF suggests:",
         ["Exit-site infection", "Low potassium", "An abdominal wall leak", "A normal fill"], 2,
         "Fluid may be dissecting into the tissue planes of the abdominal wall."),
        ("Which three details matter most after a power outage during APD?",
         ["Favorite food, address, age", "Only the time", "Connection status, therapy delivered or missed, and symptoms, plus power status and the backup plan", "The cycler brand only"], 2,
         "These tell the team what was lost and whether the backup plan is safe to use."),
        ("Pain in the last minutes of drain is usually due to:",
         ["The catheter tip against bowel or bladder as fluid empties", "Peritonitis, always", "A hernia", "Fluid overload"], 0,
         "Report it; the team may consider tidal APD."),
        ("When may backup CAPD be used after an outage?",
         ["Whenever convenient", "Only with a written backup plan, supplies and validated competence", "Never", "Only in hospital"], 1,
         "Backup is planned and validated in advance."),
        ("Blood-tinged effluent with dizziness and falling blood pressure requires:",
         ["Waiting until the next exchange", "Routine review", "An exit-site swab", "Emergency evaluation"], 3,
         "Bleeding with signs of low blood volume is an emergency."),
        ("Why does a full abdomen raise the risk of leaks and hernias?",
         ["Glucose weakens skin", "Antibiotics thin tissue", "It does not", "Pressure inside the abdomen pushes fluid toward weak points, more so when sitting, straining or lifting"], 3,
         "That is why lifting heavy loads, such as rice sacks, matters."),
        ("A long-term former PD patient has recurrent bowel obstruction symptoms and weight loss. What should be considered and reported?",
         ["Exit-site infection", "Encapsulating peritoneal sclerosis", "Normal aging", "Low potassium only"], 1,
         "This rare late complication can appear even after PD has stopped."),
        ("Which item belongs in a typhoon go-bag for a PD patient?",
         ["Only clothing", "Only food", "Solutions, connection supplies, caps, medicines, records and the current order", "Nothing; PD stops during typhoons"], 2,
         "With a go-bag, PD can continue in an evacuation center."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Tunnel", "The path of the catheter under the skin between the cuffs."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Outflow failure", "Normal fill with slow or incomplete drain."),
              ("Pericatheter leak", "Dialysate escaping along the catheter tunnel to the exit site."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("Hydrothorax", "Dialysate leaking into the chest through a gap in the diaphragm."),
              ("Hernia", "Bulging of abdominal contents through a weak point in the wall."),
              ("Hemoperitoneum", "Blood in the peritoneal cavity, seen as blood-tinged effluent."),
              ("Encapsulating peritoneal sclerosis", "A rare late complication in which a thickened peritoneum encases the bowel.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "Disaster preparedness for dialysis patients."),
                 ("el-nino-heat-dialysis.html", "Heat and dialysis.")],
    "calcs": ["calc-dialysis-continuity-planner.html", "calc-fluid-overload.html"],
}
