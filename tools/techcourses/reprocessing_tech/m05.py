# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 05: Water for Reprocessing. v0.1 RT05."""

MODULE = {
    "image_alt": "A reprocessing technician filling a sterile sample bottle from a labeled water outlet in the reuse room, with the water treatment loop visible through a window.",
    "objectives": [
        "Explain why reprocessing water touches the blood side of the dialyzer and must meet dialysis water quality.",
        "Trace water from the treatment plant to the reprocessing outlet and name the sampling points.",
        "State the DOH monitoring schedule and the meaning of a limit and an action level.",
        "Collect a water sample without contaminating it, and record it correctly.",
        "Escalate an abnormal result and hold reprocessing when the program requires it.",
    ],
    "big": """
{{plain:When you wash a baby&rsquo;s bottle, you rinse it with clean water, not with water from a puddle. The bottle can be spotless and still make the baby sick if the last rinse was dirty.}}
<p>The picture has a limit. A bottle&rsquo;s rinse water touches the outside of what the baby swallows. Reprocessing water fills the blood compartment of the dialyzer, the inside of the fibers where the patient&rsquo;s blood will flow next treatment. Bacteria and their toxins left there meet the blood directly. So the reuse outlet is treated as a point of use, sampled and protected like a dialysis station.</p>
{{cards:Key terms for this module|Product water::Water leaving the treatment system, usually after reverse osmosis.|Point of use::An outlet where water enters a process that touches patients, such as a dialysis machine or the reprocessor.|Endotoxin::A toxin from the walls of certain bacteria. It can cause fever and chills even when the bacteria are dead.|Colony-forming units (CFU)::A count of live bacteria grown from a water sample.|Total dissolved solids (TDS)::A measure of how much dissolved mineral and salt remains in the water.|Action level::A value below the limit at which you must investigate and correct.}}
<p>Your role is not to run the water plant. It is to know where the reuse outlet sits in the system, to sample and record correctly when assigned, to read the logs before you start, and to stop when the evidence says the water is not fit.</p>
""",
    "case": {"title": "Monday morning", "html": """
<p>At 6:00 on a Monday, Mr. Arnold Mendoza opens the reuse room at a unit in Laguna. Before starting the reprocessor, he checks the water log. The weekly product-water TDS reading taken on Saturday is 14 mg/L. The action limit written on the log is 10 mg/L. Nobody has signed the corrective-action box.</p>
<p>Twenty used dialyzers from Saturday&rsquo;s last shift are in the refrigerator waiting to be processed. The water technician starts work at 8:00.</p>
""", "questions": ["What does a TDS of 14 mg/L tell you, and what does it not tell you?",
                  "May Mr. Mendoza start processing the twenty dialyzers?",
                  "Who must know, and what record should he make?"]},
    "sections": [
        ("why", "Why water matters here", "Why reprocessing water matters", """
<p>Water is used to rinse the blood compartment, to clean by reverse ultrafiltration, to dilute germicide, and to rinse germicide out before treatment. Each time, it fills the inside of the fibers. The reprocessing standard of the Association for the Advancement of Medical Instrumentation (AAMI) expects reprocessing water to meet the quality required for dialysis water.[[aami_reuse]]</p>
<p>Outbreak investigations show what happens when it does not. In a CDC investigation of one United States center, water used to prepare dialysis fluid and to reprocess dialyzers exceeded the allowed bacteria and endotoxin levels; 13 episodes of bacteremia or pyrogenic reaction followed. They were traced to the water and to one machine type that was not heat-disinfected as its maker advised, not to reuse itself, but the same water was filling reprocessed dialyzers.[[rt_jackson1994]] In Hanoi, 303 dialysis patients had pyrogenic reactions over nine months; the bacteria found were largely waterborne, and investigators named suboptimal water or reprocessing as the likely cause.[[rt_archibald2006]] Most dialysis outbreaks in a CDC review were preventable by adequate water treatment, disinfection and adherence to reprocessing protocols.[[rt_roth2000]]</p>
<p>The most severe case was in Caruaru, Brazil, in 1996. Water from a reservoir reached a dialysis center without proper treatment. It carried microcystins, toxins made by blue-green algae. Of 130 patients, 101 developed acute liver failure, and 50 died.[[rt_jochimsen1998]] That center did not reuse dialyzers; the lesson is that water reaches the blood, and anything in it reaches the patient.</p>
{{key:Water that fills the fibers reaches the next patient&rsquo;s blood. The reuse outlet is a point of use.}}
"""),
        ("path", "The water path", "From the plant to the reuse outlet", """
{{fig:rt05_water}}
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What it does</th><th>What can go wrong for the reuse room</th></tr></thead>
<tbody>
<tr><td>Pretreatment (filters, softener, carbon)</td><td>Removes particles, hardness and chlorine or chloramine</td><td>Exhausted carbon lets chlorine through, which can damage membranes and patients</td></tr>
<tr><td>Reverse osmosis</td><td>Removes most dissolved solids and bacteria</td><td>A failing membrane raises TDS and conductivity</td></tr>
<tr><td>Storage and distribution loop</td><td>Delivers product water to points of use</td><td>Biofilm grows in dead legs and stagnant pipes</td></tr>
<tr><td>Reprocessing outlet and hose</td><td>Feeds the reprocessor or the manual rinse</td><td>Unlabeled outlet, old hose, outlet left running into a sink, contamination at the tip</td></tr>
</tbody></table></div>
<p>The Malaysian 2026 standards, a current regional comparison, require labeled water outlets in the reprocessing area.[[rt_my2026]] Biofilm, a slimy layer of bacteria on pipe walls, is the usual source of persistent contamination. It shelters bacteria from disinfectant and sheds endotoxin into the water.</p>
{{key:Know which loop feeds your outlet, and report anything that changes it: a new hose, a dead leg, a leak.}}
"""),
        ("schedule", "Monitoring and limits", "The monitoring schedule, limits and action levels", """
<p>The DOH water order sets the minimum monitoring for licensed facilities.[[doh_water]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>Where</th><th>How often (DOH minimum)</th></tr></thead>
<tbody>
<tr><td>Microbiology</td><td>Raw water, product water and point of use</td><td>Before operation, then at least monthly</td></tr>
<tr><td>Chemical analysis</td><td>Point of use</td><td>Before operation, then at least every six months</td></tr>
<tr><td>Total dissolved solids</td><td>Product water</td><td>Weekly; corrective action above 10 mg/L</td></tr>
</tbody></table></div>
<p>The order requires stopping and compliant repeat testing when water fails, and makes the medical director accountable for water quality.[[doh_water]] Sampling and transport follow the accredited laboratory&rsquo;s instructions.</p>
{{fig:rt05_limits}}
<p>The international standard for dialysis water, ISO 23500-3, sets a maximum total viable microbial count of 100 CFU/mL and endotoxin of 0.25 endotoxin units (EU) per mL, with action levels usually set at half those values.[[iso23500_3]] Check these figures against the edition your facility follows. An action level is a warning: the water still meets the limit, but something is changing, and the time to find it is now.</p>
{{key:Act at the action level, not at the limit. A limit broken means patients may already have been exposed.}}
"""),
        ("sampling", "Sampling", "Collecting a sample that tells the truth", """
<p>A sample is only as good as its collection. A contaminated bottle reports a false failure; a sample taken after flushing a heavily used outlet for a long time may report a false pass. Follow the laboratory&rsquo;s instructions for flushing, disinfecting the outlet and bottle handling, because they differ between laboratories and the DOH order allows some local variation.[[doh_water]]</p>
{{flow:Sampling the reuse outlet|Prepare::Sterile bottle from the laboratory, label filled in before sampling, hand hygiene, clean gloves.|Outlet::Follow the laboratory&rsquo;s instructions for disinfecting and flushing the outlet.|Collect::Open the bottle only at the moment of filling. Do not touch the inside of the cap or the outlet tip.|Close and label::Outlet name, date, time, collector.|Send::Cold chain and timing as the laboratory requires.|Record::Log the sample and later the result, and who reviewed it.}}
{{key:Label the bottle before you open it. A result without a location and time is useless.}}
"""),
        ("escalate", "When a result fails", "When a result fails", """
{{cards:What you do with an abnormal water result|At or above an action level::Report the same day to the water technician and the head nurse. Increase monitoring as the program directs.|Above a limit::Stop reprocessing if the program requires, report to the medical director&rsquo;s designate, and follow the corrective-action plan.|A result you cannot read or is missing::Treat it as not proven. Ask before you start.|Patients with fever or chills during treatment::Report at once; it may be water, the dialyzer or the machine (Module 11).}}
{{stop:If the water log shows an unsigned failure, do not start the reprocessor. Ask the person responsible for water before any dialyzer is processed.}}
"""),
    ],
    "debrief": ["""
<p><strong>What does 14 mg/L tell you?</strong> The reverse osmosis system is passing more dissolved solids than it should. A membrane may be failing, or pretreatment may be exhausted. It does not tell you whether bacteria or endotoxin have risen, and it does not by itself say the water is dangerous today. It does say that the corrective action required above 10 mg/L has not been documented.[[doh_water]]</p>
<p><strong>May he start?</strong> Not until the person responsible for water confirms what was done and whether the water is fit for use. The twenty dialyzers can stay refrigerated within the time your procedure allows; if that time will run out, they follow the procedure for overdue dialyzers (Module 8), and patients receive new dialyzers.</p>
<p><strong>Who must know?</strong> The water technician, the head nurse, and the medical director&rsquo;s designate. He records the time he found the unsigned result, who he told, and the decision. That record protects the patients and him.</p>
"""],
    "skills": {"title": "Water sampling and log review",
               "intro": "Practice with a sterile bottle on a training outlet, then review a set of synthetic water logs.",
               "items": [
                   ("Labels the bottle with outlet, date, time and collector before opening it.", True),
                   ("Follows the laboratory&rsquo;s outlet preparation steps.", False),
                   ("Fills the bottle without touching the inside of the cap or the outlet tip.", True),
                   ("Reviews the water log before starting the reprocessor.", True),
                   ("Identifies a result at an action level and one above a limit.", True),
                   ("Stops and asks when the log shows an unsigned failure.", True),
                   ("Records who was told and when.", False),
               ],
               "placement": "Collect one water sample from the reuse outlet under supervision, and follow it to its result and the review signature."},
    "quiz": [
        ("Why must reprocessing water meet dialysis water quality?",
         ["It is used to wash the floor", "It fills the blood compartment that the next patient&rsquo;s blood will flow through", "It is drunk by patients", "It is only used outside the dialyzer"], 1,
         "Anything left in the fibers meets the blood."),
        ("What can cause fever and chills even when bacteria are dead?",
         ["Endotoxin", "Chlorine", "Calcium", "Sodium"], 0,
         "Endotoxin from bacterial walls triggers fever and chills."),
        ("What happened at Caruaru, Brazil, in 1996?",
         ["A germicide error", "Untreated reservoir water with algal toxins caused liver failure in 101 patients, 50 of whom died", "A power failure", "A dialyzer recall"], 1,
         "Water reaches the blood, and anything in it reaches the patient."),
        ("Under the DOH order, how often is product-water TDS measured?",
         ["Daily", "Weekly", "Monthly", "Yearly"], 1,
         "Weekly, with corrective action above 10 mg/L."),
        ("Under the DOH order, how often at minimum is microbiology tested at the point of use?",
         ["Weekly", "Monthly", "Every six months", "Yearly"], 1,
         "Before operation, then at least monthly."),
        ("What is an action level?",
         ["The maximum allowed value", "A lower value at which you investigate and correct before the limit is broken", "The value at which the lab stops counting", "A target to aim for"], 1,
         "It warns while the water still meets the limit."),
        ("A water sample bottle was opened before it was labeled, and the outlet name was forgotten. What is the result worth?",
         ["Full value", "Little; a result without location and time cannot guide action", "It is valid if the result is good", "It can be labeled later from memory"], 1,
         "Label before opening."),
        ("Where does persistent bacterial contamination of a water loop usually come from?",
         ["The sun", "Biofilm on pipe walls and in dead legs", "The patient", "The germicide"], 1,
         "Biofilm shelters bacteria and sheds endotoxin."),
        ("You find an unsigned failed result in the water log at the start of a shift. What do you do?",
         ["Start processing and report later", "Do not start; ask the person responsible for water first", "Process only the urgent dialyzers", "Sign the box yourself"], 1,
         "An unresolved failure must be addressed before any processing."),
        ("In the Hanoi report, what were the bacteria found in patients mostly like?",
         ["Skin bacteria", "Waterborne organisms", "Food-borne organisms", "Airborne viruses"], 1,
         "Waterborne organisms point to water or reprocessing."),
        ("According to a CDC review of dialysis outbreaks, most were:",
         ["Unavoidable", "Preventable with adequate water treatment, disinfection and adherence to reprocessing protocols", "Caused by patients", "Caused by new dialyzers"], 1,
         "Execution, again, is the lesson."),
        ("Who is accountable for water quality under the DOH order?",
         ["The reprocessing technician", "The medical director", "The patient", "The supplier"], 1,
         "The medical director is accountable; the technician samples, reads and reports."),
    ],
    "terms": [("Product water", "Water leaving the treatment system, usually after reverse osmosis."),
              ("Point of use", "An outlet where water enters a process that touches patients."),
              ("Endotoxin", "A toxin from bacterial walls that causes fever and chills."),
              ("Biofilm", "A slimy layer of bacteria on pipe walls that resists disinfection."),
              ("Action level", "A value below the limit that triggers investigation and correction."),
              ("Dead leg", "A pipe section where water does not flow, so bacteria can grow."),
              ("Reverse osmosis", "Purification by forcing water through a membrane that holds back dissolved solids.")],
    "readings": [("dialysis-water-treatment-systems.html", "How dialysis water is made and monitored.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c5"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
