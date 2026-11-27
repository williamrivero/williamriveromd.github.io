# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 13: The small circuit: blood volume, priming, water and preparation. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Estimate a child&rsquo;s blood volume and express the extracorporeal volume as a share of it.",
        "Explain why the extracorporeal volume should stay below about 10% of blood volume, and what priming options the team may order.",
        "Prevent hypothermia and blood loss in small children during hemodialysis.",
        "Confirm water and dialysate release before treatment, with the Philippine limits and their sources.",
    ],
    "big": """
<p>When a hemodialysis circuit starts, blood leaves the child to fill the lines and dialyzer. In an adult, that volume is a small fraction of the blood in the body. In a small child it can be a large one. If too much blood leaves at once, blood pressure falls before any fluid has been removed.</p>
<p>Your work in this module is to know the size of the circuit compared with the child, to confirm the priming plan before connection, and to make sure the water and dialysate are released for use.</p>
{{plain:Think of the circuit as a detour on a small road. A few cars on a detour do not matter. Send half the traffic onto the detour at once, and the main road empties.}}
<p>The picture has a limit. Cars return when the detour ends; so does blood, at the end of the session, along with the fluid that pushed it back. A very large circuit therefore causes two problems: a fall in blood volume at the start and a fluid load at the end.[[pdn_fischbach2005]]</p>
{{cards:Key terms for this module|Extracorporeal volume (ECV)::The volume of blood outside the body in lines, needles and dialyzer.|Estimated blood volume::Body weight multiplied by an age-based estimate of blood per kilogram.|Prime::The fluid that fills the circuit before blood enters it: saline, albumin or blood.|Water release::Documented confirmation that dialysis water met its limits before use.|Ultrapure dialysate::Dialysate with very low bacteria and endotoxin, needed for high-flux dialyzers and hemodiafiltration.}}
""",
    "case": {"title": "The new baby on the schedule", "html": """
<p>A newborn, <strong>Baby Girl Torres</strong>, 3.5 kilograms, is transferred to the PICU with acute kidney injury and severe fluid overload. PD is not possible after abdominal surgery. The team plans hemodialysis. <strong>Nurse Ben</strong>, who usually dialyzes school-age children, is asked to prepare the circuit. The smallest pediatric lines and dialyzer available hold an illustrative 68 mL together.</p>
""", "questions": ["What is the baby&rsquo;s estimated blood volume, and what share would the circuit take?",
                  "What priming question must be answered before connection, and by whom?",
                  "What else threatens a newborn on a hemodialysis circuit?"]},
    "sections": [
        ("blood-volume-and-the-circuit", "The 10% rule", "Blood volume and the circuit", """
<p>The ESPN practical guidelines state that the total extracorporeal volume (needles, tubing and dialyzer) should be, approximately, less than 10% of the child&rsquo;s total blood volume.[[pdn_fischbach2005]] Estimating blood volume is a teaching approximation: about 80 mL per kilogram in children, and somewhat higher per kilogram in infants and newborns.</p>
{{fig:pdn13_a}}
{{formula:Estimated blood volume (mL) &asymp; weight (kg) &times; 80 (children; higher per kg in infants)<br>ECV share (%) = circuit volume (mL) &divide; estimated blood volume (mL) &times; 100<br>Example: 20 kg child &rarr; about 1,600 mL; a 68 mL circuit = about 4%.<br>10 kg child &rarr; about 800 mL; 68 mL = about 8.5%.<br>3.5 kg newborn at about 85 mL/kg &rarr; about 300 mL; 68 mL = about 23%.}}
<p>Circuit volumes in these examples are illustrative; use the volumes printed for your lines and dialyzer. The share, not the absolute volume, tells you how hard the start will be for the child.</p>
{{key:Know the circuit as a share of the child&rsquo;s blood volume. Under about 10% is the usual aim; above it, the priming plan must be explicit.}}
"""),
        ("priming-decisions", "Priming", "Priming decisions", """
<p>When the circuit would take too large a share, the team primes it with something that keeps blood volume and oxygen-carrying capacity steady. The guidelines describe priming with saline, albumin and sometimes blood in the first sessions with babies and small infants.[[pdn_fischbach2005]] Blood primes bring their own risks: stored blood can carry potassium, acid and citrate, and the team&rsquo;s protocol sets how the prime is prepared and checked.</p>
{{fig:pdn13_b}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Who</th></tr></thead>
<tbody>
<tr><td>Calculate estimated blood volume and ECV share</td><td>Nurse, with independent check</td></tr>
<tr><td>Decide saline, albumin or blood prime, and whether to return the circuit blood at the end</td><td>Pediatric nephrologist (and transfusion service for blood)</td></tr>
<tr><td>Prepare and verify the prime per protocol, including blood-product checks</td><td>Nurse, with a second checker</td></tr>
<tr><td>Monitor blood pressure, heart rate and temperature closely during the first minutes</td><td>Nurse</td></tr>
</tbody></table></div>
<p>Very small infants are also at risk of hypothermia, because dialysate and blood lines exchange heat; machines with temperature control and warming plans help.[[pdn_fischbach2005]] Keep blood sampling to the minimum ordered, and record every milliliter taken: in a newborn, small repeated samples add up to a meaningful blood loss.</p>
{{key:The nurse calculates and confirms; the prescriber decides the prime. No connection until the plan is written and checked.}}
"""),
        ("water-and-release", "Water", "Water and dialysate release", """
<p>A child&rsquo;s blood meets dozens of liters of dialysate across the dialyzer in every session, so water quality matters as much as for adults, and high-flux dialyzers and hemodiafiltration require ultrapure dialysate.[[pdn_fischbach2005]] In the Philippines, Department of Health Administrative Order 2013-0003 sets the water-analysis and monitoring requirements that testing laboratories report against, and the PSN guidelines describe professional expectations.[[doh_ao2013_0003]][[psn2024]]</p>
<ul>
<li>Before the first treatment of the day, confirm that the water system log shows the required daily checks were done and passed, per unit procedure.</li>
<li>Confirm the machine passed its self-test and disinfection is recorded.</li>
<li>Check dialysate composition against the order before connection; conductivity and temperature alarms are not optional.</li>
<li>If a water result fails or a check is missing, do not start: report to the charge nurse and the water treatment technician.</li>
</ul>
{{scene:Preparing for Baby Girl Torres|<p>Ben estimates her blood volume at about 300 mL (3.5 kg &times; 85 mL/kg). The 68 mL circuit is about 23%, more than twice the usual aim. He asks a colleague to recalculate, then calls the pediatric nephrologist: &ldquo;The circuit is about 23% of her blood volume. What prime do you want, and do we return the circuit at the end?&rdquo; The nephrologist orders a blood prime per protocol. Ben arranges a warming plan and a minimum-sample schedule.</p><p class="tc-scene-take">Saying the share out loud turned an abstract volume into a clear decision for the right person.</p>}}
{{key:No treatment starts on water or a machine that has not been released. A missing check is a failed check.}}
"""),
    ],
    "debrief": ["""
<p><strong>The share.</strong> About 3.5 kg &times; 85 mL/kg &asymp; 300 mL; 68 mL is about 23% of her blood volume, far above about 10%.</p>
<p><strong>The priming question.</strong> Saline, albumin or blood prime, and whether to return the circuit blood at the end. The pediatric nephrologist decides, with the transfusion service for blood products. Ben calculates, double-checks and prepares per protocol.</p>
<p><strong>Other threats.</strong> Hypothermia from heat exchange, blood loss from sampling, hypotension at connection, electrolyte loads from a blood prime, and a fluid load at the end. Ben monitors closely in the first minutes and records every milliliter drawn.</p>
"""],
    "skills": {"title": "The small-circuit check", "intro": "Use fictional children and printed circuit volumes.",
               "items": [("Estimates blood volume and calculates the ECV share with an independent check", True),
                         ("States the priming question to the prescriber and documents the order", True),
                         ("Prepares a warming plan and a minimum-sample plan for an infant", False),
                         ("Confirms water log, machine self-test, disinfection and dialysate checks before connection", True),
                         ("Withholds treatment when a water or machine check is missing or failed", True)]},
    "quiz": [
        ('The ESPN guideline aim for total extracorporeal volume is less than about:',
         ['1% of blood volume', '10% of blood volume', '30%', '50%'], 1,
         'Approximately, per the 2005 practical guidelines.'),
        ('Teaching estimate of blood volume in children:',
         ['40 mL/kg', '150 mL/kg', 'About 80 mL/kg', '1 L per year of age'], 2,
         'Higher per kg in infants.'),
        ('A 20-kg child with a 68 mL circuit: ECV share is about:',
         ['1%', '20%', '40%', '4%'], 3,
         '68 &divide; 1,600.'),
        ('A 10-kg child with a 68 mL circuit: about:',
         ['8.5%', '2%', '25%', '50%'], 0,
         '68 &divide; 800.'),
        ('A 3.5-kg newborn at 85 mL/kg with a 68 mL circuit: about:',
         ['5%', '23%', '10%', '60%'], 1,
         '68 &divide; about 300.'),
        ('Who decides whether to prime with blood?',
         ['The nurse', 'The parent', 'The pediatric nephrologist, with the transfusion service', 'The technician'], 2,
         'The nurse calculates and confirms.'),
        ('Why can a very large circuit cause a fluid load at the end?',
         ['It cannot', 'Dialysate leaks', 'Pumps add water', 'Returning the circuit adds blood and rinse fluid'], 3,
         'Return volume loads the child.'),
        ('A risk of blood primes:',
         ['Potassium, acid and citrate loads', 'None', 'Hypothermia only', 'Peritonitis'], 0,
         'Protocols govern preparation.'),
        ('Why are very small infants at risk of hypothermia on hemodialysis?',
         ['They are not', 'Heat exchange through the circuit and dialysate', 'Cold rooms only', 'Fever'], 1,
         'Temperature control helps.'),
        ('Why record every blood sample volume in a newborn?',
         ['Billing', 'Lab rules', 'Small repeated samples add up to meaningful blood loss', 'No reason'], 2,
         'Minimum sampling.'),
        ('High-flux dialyzers and HDF require:',
         ['Tap water', 'No water checks', 'Saline only', 'Ultrapure dialysate'], 3,
         'Per the 2005 guideline.'),
        ('Which issuance sets Philippine dialysis water monitoring requirements?',
         ['DOH AO 2013-0003', 'RA 7610', 'PhilHealth Circular 2024-0036', 'RA 10173'], 0,
         'Testing laboratories report against it.'),
        ('The water log is missing today&rsquo;s check. You:',
         ['Start anyway', 'Do not start; report to the charge nurse and water technician', 'Ask the parent', 'Check tomorrow'], 1,
         'A missing check is a failed check.'),
        ('Before connection you confirm:',
         ['Only the dialyzer', 'Only the blood flow', 'Water release, machine self-test, disinfection and dialysate composition', 'Nothing'], 2,
         'All are release checks.'),
        ('The circuit share matters more than the absolute circuit volume because:',
         ['It does not', 'Machines require it', 'It sets the dialysate', 'It shows how hard the start is for this child'], 3,
         'Same volume, different child, different risk.'),
    ],
    "terms": [("Extracorporeal volume", "Blood outside the body in lines, needles and dialyzer."),
              ("Estimated blood volume", "Weight times an age-based estimate of blood per kilogram."),
              ("Prime", "Fluid that fills the circuit before blood enters."),
              ("Blood prime", "Priming the circuit with blood to protect a small child&rsquo;s blood volume."),
              ("Water release", "Documented confirmation that water met its limits before use."),
              ("Ultrapure dialysate", "Dialysate with very low bacteria and endotoxin.")],
    "readings": [("dialysis-water-treatment-systems.html", "How dialysis water is treated and monitored."),
                 ("crrt-continuous-renal-replacement-therapy.html", "Continuous therapies and small circuits.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html"],
}
