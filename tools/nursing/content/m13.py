# -*- coding: utf-8 -*-
# Module 13 (advanced, after the capstone): convective therapies.
# Base sections: model, physiology (shared convection physiology), evidence (choosing), bedside (shared safety).
# m13_x.py adds the continuous therapy (CRRT) sections after "physiology";
# m13_x2.py adds the hemodiafiltration (HDF) sections after "crrt-transitions".
MODULE = {
    "sub": "The physiology shared by continuous kidney replacement in the intensive care unit and hemodiafiltration in the dialysis unit, and the nursing that keeps each one safe: modes, prescription, anticoagulation, fluid balance, circuits, complications, and quality.",
    "desc": "Advanced Module 13 of the Nephrology Nursing & Hemodialysis self-study series: convection and replacement fluid, continuous renal replacement therapy (CRRT) in the ICU, online hemodiafiltration (HDF) in the dialysis unit, and the nursing checks that keep both safe.",
    "keywords": "CRRT nursing, continuous renal replacement therapy nurse, CVVHDF citrate anticoagulation nursing, hemodiafiltration nursing, online HDF convection volume, CONVINCE trial, replacement fluid safety, filtration fraction",
    "objectives": [
        "Explain how convection differs from diffusion and why it removes larger molecules.",
        "Describe replacement fluid, pre-dilution and post-dilution, and the filtration fraction, and predict how each affects clearance and filter life.",
        "Identify which patients and settings suit continuous therapy and which suit hemodiafiltration.",
        "Apply the safety rules shared by every convective therapy: replacement fluid treated as an intravenous medicine, exact fluid accounting, protected connections, and alarms that are answered, never silenced.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Mental model", "h2": "A sieve as well as a tea bag",
         "html": """
<p>Module 6 pictured standard hemodialysis (HD) as a tea bag. Small solutes such as urea and potassium drift out of the blood and into the dialysate, because there is more of them on the blood side. That is diffusion. It works best for small molecules that move quickly.</p>
<p>Convective therapies add a second picture: a sieve. Pressure pushes plasma water through the membrane. Anything dissolved in that water and small enough to fit the pores is carried along with it, whatever its size up to the pore limit. Larger &ldquo;middle molecules,&rdquo; which diffuse slowly, leave much better this way. The water pushed out is far more than the patient can afford to lose, so sterile <strong>replacement fluid</strong> is given back into the blood line. The net effect is a washing of the plasma, not dehydration.</p>
<p>The picture has a limit. A kitchen sieve holds things back by size alone. A dialysis membrane also carries charge and a coating of protein on its surface. So its real behavior is described by how freely each substance crosses, its sieving coefficient, and not by a simple yes or no.</p>
<p>Two very different treatments use this idea. <strong>Continuous renal replacement therapy (CRRT)</strong> runs around the clock in the intensive care unit (ICU) for a critically ill patient with acute kidney injury (AKI). <strong>Hemodiafiltration (HDF)</strong> adds large-volume convection to high-flux HD in an ordinary chronic session. The machines, settings, and risks differ. The physiology and many of the safety rules are the same, which is why this module teaches them together.</p>
<p>Most of what goes wrong in either therapy is predictable: a wrong bag, a fluid number nobody reconciled, a clotting circuit, an alarm cleared without a cause. Your work is to understand the physiology well enough to see these coming, and to keep the record that lets the prescriber act in time.</p>
"""},
        {"id": "physiology", "nav": "Convection", "tag": "Physiology in depth", "h2": "Convection, replacement fluid, and the filtration fraction",
         "html": """
<p><strong>Three ways to move things across a membrane.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Process</th><th>Driving force</th><th>What it removes best</th><th>Where it is used</th></tr></thead><tbody>
<tr><td>Diffusion</td><td>A concentration difference between blood and dialysate</td><td>Small solutes: urea, creatinine, potassium</td><td>Standard HD; continuous venovenous hemodialysis</td></tr>
<tr><td>Ultrafiltration</td><td>A pressure difference across the membrane</td><td>Water (with whatever is dissolved in it)</td><td>Every treatment that removes fluid</td></tr>
<tr><td>Convection</td><td>Ultrafiltration large enough that solutes are dragged along with the water</td><td>Small and middle molecules alike, up to the pore size</td><td>Hemofiltration, CRRT with replacement fluid, HDF</td></tr>
</tbody></table></div>
<p><strong>Why size matters.</strong> Diffusion slows sharply as molecules get larger. Beta-2 microglobulin, about 11,800 daltons, builds up in long-term dialysis patients, and diffusion alone clears it poorly. Convection works differently. A solute crosses in proportion to the volume of water moved and to its sieving coefficient. That coefficient is close to 1 for urea and potassium, which cross as freely as water. It is lower for larger molecules. It is close to 0 for albumin and blood cells, which a healthy membrane keeps in the blood.</p>
<p><strong>Replacement fluid.</strong> To remove many liters of plasma water without draining the circulation, an almost equal volume of sterile, buffered electrolyte solution goes back into the blood path. In CRRT it comes from prescribed bags. In online HDF the machine makes it from ultrapure dialysate. Either way it enters the bloodstream directly. Over hours, its sodium, potassium, calcium, bicarbonate, and glucose become the patient&rsquo;s plasma composition. Net fluid removal is everything removed minus everything given back.</p>
<p><strong>Where the replacement fluid enters.</strong></p>
<div class="table-wrap"><table><thead><tr><th></th><th>Pre-dilution (before the filter)</th><th>Post-dilution (after the filter)</th></tr></thead><tbody>
<tr><td>What happens to the blood in the filter</td><td>It is diluted before it reaches the fibers, so it stays thinner</td><td>It is concentrated as water leaves, then diluted again after the filter</td></tr>
<tr><td>Clearance per liter exchanged</td><td>Lower, because part of each liter removed is replacement fluid that was just added</td><td>Higher: every liter removed is the patient&rsquo;s own plasma water</td></tr>
<tr><td>Filter life</td><td>Longer</td><td>Shorter if too much water is removed, because the blood thickens and clots</td></tr>
<tr><td>Typical use</td><td>CRRT when clotting limits filter life; HDF when blood flow or hematocrit limits post-dilution</td><td>Usual mode for HDF; common in CRRT when filter life allows</td></tr>
</tbody></table></div>
<p><strong>The filtration fraction.</strong> This is the share of the plasma flowing through the filter that is removed as ultrafiltrate. Plasma flow is the blood flow multiplied by (1 minus the hematocrit). For example, a blood flow of 200 mL/min with a hematocrit of 30% gives a plasma flow of 140 mL/min. Removing 35 mL/min of ultrafiltrate gives a filtration fraction of 35 &divide; 140 = 25%. In post-dilution, the higher the fraction, the thicker the blood leaving the fibers and the faster the filter clots. Units set a ceiling by protocol. When it is reached, the prescriber can raise blood flow, lower the exchange, or move some replacement fluid to pre-dilution.</p>
<p><strong>What each number tells you.</strong> During post-dilution, a rising transmembrane pressure or falling filter performance usually means the blood in the filter is concentrating and clotting. It does not usually mean the machine is faulty. That link between physiology and alarms runs through both halves of this module.</p>
<p><strong>When a pressure climbs, ask first what is happening to the blood inside the fibers.</strong></p>
"""},
        {"id": "evidence", "nav": "Choosing", "tag": "Evidence", "h2": "Where each therapy fits, and what is still unknown",
         "html": """
<p><strong>Continuous therapy in the ICU.</strong> Slow removal over 24 hours causes smaller swings in blood pressure and in brain water than a 4-hour session. On that basis, the Kidney Disease: Improving Global Outcomes (KDIGO) 2012 AKI guideline suggests continuous therapy rather than standard intermittent dialysis for patients who are hemodynamically unstable (graded 2B, a weak suggestion on moderate-quality evidence). It makes the same 2B suggestion for patients with acute brain injury or raised intracranial pressure.[[aki2012]] Randomized comparisons have not shown that any one form of kidney support improves survival. The choice is made for tolerance, availability, and the team&rsquo;s experience.[[aki2012]][[ostermann2020]] Module 4 explains how and when support is started. This module covers how continuous therapy is run.</p>
<p><strong>Hemodiafiltration in the dialysis unit.</strong> HDF is a chronic, outpatient therapy. It aims to clear middle molecules that standard HD removes poorly, and it is often better tolerated hemodynamically, partly because the large exchange cools the blood. Whether it improves survival depends on delivering a high convection volume. The HDF sections below set out the randomized evidence, including the largest trial.</p>
<div class="table-wrap"><table><thead><tr><th></th><th>Continuous therapy (CRRT)</th><th>Hemodiafiltration (HDF)</th></tr></thead><tbody>
<tr><td>Setting</td><td>ICU, around the clock</td><td>Dialysis unit, about 4 hours, three times a week</td></tr>
<tr><td>Patient</td><td>Critically ill, usually with AKI, often in shock</td><td>Stable patient with kidney failure</td></tr>
<tr><td>Access</td><td>Temporary dialysis catheter</td><td>Fistula, graft, or tunneled catheter with good flow</td></tr>
<tr><td>Replacement fluid</td><td>Commercial sterile bags hung by the nurse</td><td>Made online by the machine from ultrapure dialysate</td></tr>
<tr><td>Main nursing risks</td><td>Fluid-balance error, anticoagulation complications, circuit clotting, hypothermia, electrolyte loss</td><td>Water and dialysate contamination, clotting at high filtration fraction, not achieving the prescribed convection volume</td></tr>
</tbody></table></div>
<p><strong>What remains uncertain.</strong> For continuous therapy, the best anticoagulant for each patient, the right moment to stop, and how to adjust medicines that the circuit removes are still debated. For HDF, the convection volume needed for benefit, which patients gain most, and how results from European trials apply in Asian units are open questions. Where evidence is incomplete, the unit protocol and the physician&rsquo;s order decide. Your accurate observations are what make those decisions possible.</p>
"""},
        {"id": "bedside", "nav": "Shared safety", "tag": "Clinical application", "h2": "Safety rules shared by every convective therapy",
         "html": """
<p><strong>Replacement fluid is an intravenous medicine.</strong> Liters of it enter the bloodstream every hour. A wrong bag or a wrong additive acts like a large intravenous error. Before you hang or start it, check the prescription, the product and its concentrations (above all potassium, phosphate, calcium, and bicarbonate), the expiry date, the bag&rsquo;s integrity, and any additive label. Use a second person where the unit requires it. In HDF the machine makes the fluid, so its safety rests on the water system, the ultrafilters, and the disinfection record instead (Module 8).</p>
<p><strong>Three fluid numbers that must agree.</strong> The prescribed net removal, the machine&rsquo;s recorded net removal, and the patient&rsquo;s total balance are different numbers. The total balance counts every infusion, feed, drug, and drain. Record all three as the protocol requires. Report when they drift apart, or when the patient cannot tolerate the removal.</p>
<div class="table-wrap"><table><thead><tr><th>Common error</th><th>What it causes</th><th>How it is prevented</th></tr></thead><tbody>
<tr><td>Wrong replacement or dialysate bag (for example, potassium-free instead of potassium-containing)</td><td>Dangerous potassium, calcium, or acid&ndash;base changes over hours</td><td>Independent check of every bag against the order; labeled additives</td></tr>
<tr><td>Bag or scale disturbed, bag hung but clamp closed</td><td>Fluid removed or given that the machine does not count correctly</td><td>Follow the machine&rsquo;s bag-change steps; never lean on or touch the scales</td></tr>
<tr><td>Alarm silenced and treatment restarted without finding the cause</td><td>Clotting, air entry, blood loss, or unrecorded fluid shifts</td><td>Look at the patient and the circuit first, then the machine; escalate repeated alarms</td></tr>
<tr><td>Open connection or contaminated port</td><td>Bloodstream infection; air entry</td><td>Aseptic technique, locked connections kept visible, catheter care as in Module 7</td></tr>
<tr><td>Heat loss through the circuit unnoticed</td><td>Hypothermia that also hides fever</td><td>Temperature checks and warming as ordered</td></tr>
</tbody></table></div>
<p><strong>Answer alarms; never bypass them.</strong> Pressure, air, blood-leak, and balance alarms protect the patient. Read which alarm it is. Look at the patient and the lines before you touch the machine. Correct the cause, and document it. An air detector or blood-leak detector is never overridden.</p>
<p><strong>Document and hand over.</strong> Each shift&rsquo;s record shows the prescription, the settings, the delivered treatment (effluent dose in CRRT; achieved convection volume in HDF), the fluid balance, anticoagulation monitoring, alarms and actions, circuit changes, and the patient&rsquo;s response. Hand over with SBAR (Situation, Background, Assessment, Recommendation).</p>
<p><strong>Every bag is a medicine, every alarm has a cause, and every hour has a balance. Check all three before you move on.</strong></p>
"""},
    ],
    "case": {
        "title": "Tingling lips at two in the morning",
        "html": """
<p>Mrs. Teresita Reyes, 58, a market vendor from Pampanga, is on day two in the ICU with septic shock and AKI after leptospirosis. She is on continuous venovenous hemodiafiltration with regional citrate anticoagulation and a calcium infusion, both run by the unit protocol. Her noradrenaline dose has come down since yesterday.</p>
<p>It is 2 a.m. You are her nurse. She tells you her lips and fingertips are tingling. The machine shows no alarm. Over the last 3 hours her hourly balance has run 150 mL more negative than prescribed. The calcium infusion bag ran out 40 minutes ago. Nobody replaced it, because the unit was busy with an admission.</p>
""",
        "acte": {
            "Assess": "Tingling around the mouth and fingers, with an empty calcium bag, points to low ionized calcium from citrate. Check her blood pressure, heart rhythm, and QT interval on the monitor. Look for twitching or spasm. Send the ionized calcium sample the protocol requires. Then review the hourly balance and confirm what was actually infused and removed.",
            "Communicate": "Call the physician now with SBAR: patient on citrate CRRT, calcium infusion interrupted for 40 minutes, new perioral and finger tingling, current vital signs and rhythm, ionized calcium sent; request orders for calcium replacement and the citrate and fluid settings. Report the balance running more negative than prescribed.",
            "Teach": "Tell Mrs. Reyes, calmly, that the machine uses a medicine that lowers calcium in the tubing, and that her calcium drip is being restarted. Ask her to tell you at once about tingling, cramps, or a racing heart.",
            "Escalate": "Act immediately per protocol if she develops spasm, seizure, arrhythmia, a long QT interval, or hypotension. Report the interrupted infusion as an incident so that bag changes for protocol-driven infusions are never deferred again.",
        },
        "task": "Write the 2 a.m. progress note: the symptom, what you found (infusion status, vital signs, rhythm, fluid balance), whom you called and when, the orders received, the time the calcium infusion was restarted, the result of the ionized calcium, and the patient&rsquo;s response.",
    },
    "quiz": [
        {"stem": "A patient on standard high-flux HD for many years develops joint pain and carpal tunnel symptoms attributed to the build-up of beta-2 microglobulin. Why would adding large-volume convection be expected to remove more of this molecule?",
         "options": [
             ("Convection drags middle-sized molecules across with the water, while diffusion is slow for larger molecules", True, "This is the core difference: convective removal depends on the water volume moved and the sieving coefficient, not on how fast a molecule diffuses."),
             ("Convection raises the concentration difference between blood and dialysate", False, "That would speed diffusion; convection works by moving water under pressure, not by changing the concentration gradient."),
             ("Convection opens the membrane pores to let albumin pass", False, "A healthy membrane keeps albumin almost entirely in the blood; convection is not meant to remove albumin."),
             ("Convection lowers the blood flow so each molecule stays longer in the dialyzer", False, "Convection does not depend on a lower blood flow; HDF in fact needs a good blood flow."),
         ],
         "objective": "Explain how convection differs from diffusion and why it removes larger molecules.",
         "sources": ["anna7"], "flag": ""},
        {"stem": "During post-dilution continuous hemofiltration, the filter has clotted three times in 24 hours. Blood flow is limited by the catheter, and the filtration fraction is near the unit&rsquo;s ceiling. Which change, if ordered, most directly addresses the cause?",
         "options": [
             ("Increasing the post-dilution exchange rate to clear more solute", False, "More post-dilution removal raises the filtration fraction further and makes clotting more likely."),
             ("Moving part of the replacement fluid to pre-dilution", True, "Pre-dilution thins the blood before it reaches the fibers and lowers hemoconcentration, which extends filter life at the cost of some clearance."),
             ("Switching off the air detector to reduce interruptions", False, "Safety detectors are never bypassed; interruptions are fixed by finding their cause."),
             ("Cooling the replacement fluid", False, "Temperature does not address the concentrated blood that is clotting the filter, and cooling worsens hypothermia."),
         ],
         "objective": "Describe replacement fluid, pre-dilution and post-dilution, and the filtration fraction, and predict how each affects clearance and filter life.",
         "sources": ["anna7"], "flag": "Changes to dilution mode, blood flow, or exchange rate are made by order or protocol."},
        {"stem": "Blood flow is 200 mL/min, the hematocrit is 30%, and the ultrafiltration rate in post-dilution is 35 mL/min. What is the filtration fraction?",
         "options": [
             ("About 18%", False, "This divides 35 by the blood flow (200); the filtration fraction uses plasma flow, not blood flow."),
             ("About 30%", False, "This is the hematocrit, not the filtration fraction."),
             ("About 25%", True, "Plasma flow is 200 &times; (1 &minus; 0.30) = 140 mL/min, and 35 &divide; 140 = 0.25, or 25%."),
             ("About 12%", False, "This understates the fraction; recheck the plasma-flow step."),
         ],
         "objective": "Describe replacement fluid, pre-dilution and post-dilution, and the filtration fraction, and predict how each affects clearance and filter life.",
         "sources": ["anna7"], "flag": ""},
        {"stem": "You are about to hang a new replacement-fluid bag for a patient on continuous therapy. The order specifies a solution containing potassium; the bag on the shelf in the bay is potassium-free and the night is busy. What is the safest action?",
         "options": [
             ("Hang the potassium-free bag and plan to recheck potassium at the next routine blood test", False, "Liters of potassium-free fluid enter the blood every hour; potassium can fall dangerously before the next routine test."),
             ("Add potassium to the bag yourself to match the order", False, "Nurses do not compound additives outside the order and the unit&rsquo;s procedure; that needs an order, a protocol, and a second check."),
             ("Pause the treatment until morning", False, "An unplanned stop risks circuit clotting and delays treatment; the problem is the bag, which can be corrected now."),
             ("Do not hang it; obtain the ordered solution or contact the physician, and check each bag against the order", True, "Replacement fluid is an intravenous medicine: the right product is verified against the order before it is hung, with a second check where required."),
         ],
         "objective": "Apply the safety rules shared by every convective therapy: replacement fluid treated as an intravenous medicine, exact fluid accounting, protected connections, and alarms that are answered, never silenced.",
         "sources": ["aki2012"], "flag": "Bag verification and additive practice follow the unit protocol."},
        {"stem": "Which patient is the most typical candidate for continuous therapy rather than standard intermittent dialysis?",
         "options": [
             ("A stable outpatient on dialysis who wants to clear middle molecules better", False, "This describes a candidate for hemodiafiltration in the dialysis unit, not continuous therapy."),
             ("An ICU patient with AKI who needs kidney support while on a vasopressor for septic shock", True, "Slow, continuous removal is better tolerated when blood pressure is unstable; KDIGO suggests continuous therapy for such patients."),
             ("A ward patient with stable AKI who is walking and eating", False, "A stable patient is usually treated with intermittent dialysis if support is needed."),
             ("A patient on peritoneal dialysis with a single episode of peritonitis", False, "Peritonitis is treated with antibiotics; it is not an indication for continuous therapy."),
         ],
         "objective": "Identify which patients and settings suit continuous therapy and which suit hemodiafiltration.",
         "sources": ["aki2012"], "flag": ""},
    ],
    "reflect": "Think of the last convective treatment you saw or ran. Which of the three fluid numbers (prescribed removal, machine removal, total patient balance) did the team actually reconcile, and who noticed when they disagreed?",
    "practice": {
        "intro": "With a preceptor experienced in continuous therapy or hemodiafiltration, observe and then assist with one treatment from setup to end.",
        "items": [
            "Explains convection, the replacement-fluid site, and the filtration fraction for the running treatment.",
            "Verifies each replacement-fluid or dialysate bag against the order with a second person where required.",
            "Reconciles hourly fluid balance against the prescription and reports a discrepancy.",
            "Responds to a pressure or balance alarm by assessing the patient and circuit before the machine, and documents the cause.",
            "Monitors anticoagulation as ordered (ionized calcium for citrate, clotting tests for heparin) and reports results outside the protocol range.",
            "Records delivered dose (effluent dose or achieved convection volume) and hands over with SBAR.",
        ],
    },
    "readings": [
        ["crrt-continuous-renal-replacement-therapy.html", "Clinician reference for continuous therapy: modes, dose, anticoagulation."],
        ["aki-icu-dialysis-decisions.html", "How starting, continuing, and stopping kidney support in the ICU are decided."],
        ["hemodiafiltration-new-standard.html", "The case for and against hemodiafiltration as a standard treatment."],
        ["hemodiafiltration-deep-dive.html", "Hemodiafiltration in depth: convection volume, machines, and evidence."],
        ["dialysis-water-treatment-systems.html", "Water quality, which online hemodiafiltration depends on."],
    ],
    "calcs": ["calc-crrt-dose.html", "calc-crrt-uf-rate.html", "calc-crrt-flowsheet.html", "calc-hdx-toolkit.html", "calc-plasma-volume.html"],
    "external": [["KDIGO acute kidney injury guideline page (2012 guideline and the status of its update)", "https://kdigo.org/guidelines/acute-kidney-injury/"]],
    "terms": [
        ("Convection", "Removal of solutes carried along with water pushed through a membrane by pressure."),
        ("Sieving coefficient", "How freely a substance crosses a membrane with water: 1 means as freely as water, 0 means not at all."),
        ("Replacement fluid", "Sterile solution infused into the blood path to replace the plasma water removed by convection."),
        ("Pre-dilution", "Giving replacement fluid before the filter, which thins the blood and lengthens filter life."),
        ("Post-dilution", "Giving replacement fluid after the filter, which clears more per liter but concentrates blood in the filter."),
        ("Filtration fraction", "The share of plasma flow through the filter that is removed as ultrafiltrate."),
        ("Middle molecules", "Solutes larger than urea, such as beta-2 microglobulin, that diffusion removes poorly."),
    ],
    "image": {"file": "renal-nursing-13-convective-therapies",
              "alt": "An ICU nurse checks the hanging fluid bags on a continuous kidney replacement machine at a critically ill patient's bedside.",
              "purpose": "Show the two settings of convective therapy, ICU and dialysis unit, as careful bedside work.",
              "scene": "", "focal": "", "setting": "", "details": "", "exclusions": "", "archetype": "", "reviewer": ""},
    "flags": [
        "Advanced module: continuous therapy content needs review by a critical care nephrologist and the ICU's CRRT protocol owner; HDF content by the dialysis unit's medical director and technician.",
        "Post-dilution filtration fraction ceiling, warming, bag-verification and documentation intervals are set by the unit protocol and the machine manufacturer.",
        "Case: citrate and calcium infusion management are protocol-driven; confirm wording against the ICU's citrate protocol.",
    ],
    "crosswalk": {
        "ph": "PSN 2024 nurse training topics: modalities of dialysis, complications; ICU kidney support per hospital protocol",
        "anna": "Acute care kidney replacement therapies (CRRT); hemodiafiltration and convective therapies",
        "edtna": "Acute renal replacement therapy; hemodiafiltration",
        "nncc": "Acute therapies; hemodialysis technologies",
    },
}
