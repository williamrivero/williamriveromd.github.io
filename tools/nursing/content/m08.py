# -*- coding: utf-8 -*-
MODULE = {
    "sub": "A patient meets more than 100 liters of water in a single session. How that water is made safe, what the machine checks and what it cannot check, and why the nurse&rsquo;s signature on the log is a clinical act.",
    "desc": "Module 8 of the Nephrology Nursing & Hemodialysis self-study series: extracorporeal circuit and machine safety checks, carbon treatment and reverse osmosis, chemical and microbial water hazards, total chlorine testing, conductivity and temperature, documentation and release criteria for registered nurses.",
    "keywords": "dialysis water treatment nursing, chloramine hemolysis, carbon tank total chlorine test, reverse osmosis dialysis, dialysate conductivity, ISO 23500, DOH AO 2013-0003, hemodialysis machine safety checks",
    "objectives": [
        "Trace water from the municipal or deep-well supply to the dialyzer and state what each treatment stage removes.",
        "Explain why chlorine and chloramine are dangerous in dialysis water and how carbon treatment is verified.",
        "Distinguish chemical from microbial hazards and state how each is monitored.",
        "Explain what dialysate conductivity and temperature monitoring detect, and what they do not.",
        "Apply release criteria: hold treatment when a required test fails or is missing, and escalate.",
        "Perform and document pre-treatment machine and circuit safety checks.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "Water as a medicine given by the liter",
         "html": """
<p>Picture a pharmacy that compounds one medicine in very large doses, on site, every morning. The medicine has ingredients, specifications, quality tests, and a release step before anyone receives it. Dialysis water is that medicine. A healthy person drinks about two liters of water a day, and the gut wall and kidneys stand between that water and the blood. A person on hemodialysis (HD) meets well over 100 liters of water per session, as dialysis fluid, with only a thin synthetic membrane in between and no kidney to clear what crosses.</p>
<p>The picture has a limit. A compounded medicine is tested batch by batch before it leaves the pharmacy. Dialysis water is made continuously, and some of its hazards change by the hour: carbon runs out without warning, and bacteria grow inside the pipes between monthly samples. The machine at the chair cannot see most of these hazards. So release is not a single test. It is a set of checks, each at its own interval, and someone must confirm they were done before the first patient is connected.</p>
<p>Most mornings every check passes. Rarely, one fails or is missing, and contaminants that are harmless in drinking water can then injure every patient on the floor at once. Your work is to know which checks stand between the supply and your patient, to confirm they were done, and to hold treatment when one is missing.</p>
"""},
        {"id": "physiology", "nav": "Treatment stages", "tag": "Physiology", "h2": "From supply to dialyzer",
         "html": """
<p>Follow the water from the tap to the dialyzer. Each stage removes something, and each has its own way of failing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Purpose</th><th>What goes wrong if it fails</th></tr></thead>
<tbody>
<tr><td>Sediment filter</td><td>Removes particles</td><td>Downstream components clog</td></tr>
<tr><td>Softener</td><td>Exchanges calcium and magnesium for sodium</td><td>Hard water scales and damages the membrane downstream</td></tr>
<tr><td>Carbon tanks (two in series)</td><td>Adsorb chlorine and chloramine</td><td>Hemolysis in patients; damage to the membrane downstream</td></tr>
<tr><td>Reverse osmosis</td><td>Rejects dissolved salts, metals, bacteria, and endotoxin</td><td>Chemical contaminants and microbes reach the dialysate</td></tr>
<tr><td>Distribution loop</td><td>Delivers treated water to each station</td><td>Stagnant sections grow biofilm</td></tr>
<tr><td>Dialysis machine</td><td>Mixes water with acid and bicarbonate concentrates; warms, degasses, and monitors the dialysate</td><td>Wrong composition or temperature reaches the blood</td></tr>
</tbody></table></div>
<p><strong>Why chlorine matters.</strong> Water utilities add chlorine or chloramine to keep drinking water free of bacteria. In dialysis the chain runs like this. Chloramine crosses the dialyzer membrane. It oxidizes hemoglobin inside red cells. The damaged cells break apart. Hemolysis releases potassium, and it can be fatal. Reverse osmosis (RO) does not remove chloramine reliably, and chlorine damages the RO membrane itself. So the carbon tanks are the only barrier. Carbon has a finite capacity and gives no warning when it is used up. That is why the test after the carbon tanks is repeated every treatment day, and not assumed from yesterday.</p>
<p><strong>Chemical and microbial hazards are different problems.</strong> Chemical contaminants such as aluminum, fluoride, copper, and nitrate come from the source water or the plumbing. Their toxicity may be sudden or may build over months. Bacteria grow inside the system itself, on tank and pipe surfaces. Even when the dialyzer membrane holds the organisms back, fragments of their cell walls, called endotoxin, can cross or stimulate inflammation. The patient then has fever and chills during treatment.</p>
<p><strong>What the machine watches.</strong> Dialysate conductivity reflects the total concentration of dissolved ions, mostly sodium. It tells the machine whether water and concentrates were mixed in the right proportion. Temperature is watched because overheated dialysate causes hemolysis and cold dialysate causes shivering. If either goes out of range, the machine diverts dialysate away from the dialyzer. Neither sensor can detect chloramine, bacteria, endotoxin, or trace chemicals.</p>
<p><strong>A machine in full &ldquo;green&rdquo; status can be running on unsafe water. The machine checks the mix and the warmth. Only the water tests check the water.</strong></p>
"""},
        {"id": "evidence", "nav": "Standards", "tag": "Evidence", "h2": "Which standard applies, and what it says",
         "html": """
<p>The international reference is the International Organization for Standardization (ISO) 23500 series, whose second edition was published in 2024. Part 3 sets the requirements for dialysis water.[[iso23500_3]] In the Philippines, the Department of Health (DOH) licensing order and its 2013 implementing guidelines on dialysis water refer to the standards of the Association for the Advancement of Medical Instrumentation. Those standards have since been harmonized with the ISO series. The Philippine Society of Nephrology (PSN) 2024 guidance repeats the local testing schedule.[[doh2012]][[doh2013]][[psn2024]] Each facility should state in its water policy which standard and edition it follows. The figures below are the commonly cited values. They are for orientation and do not replace that policy.</p>
<div class="table-wrap"><table>
<thead><tr><th>Parameter</th><th>Commonly cited limit for dialysis water</th><th>Local schedule in DOH and PSN guidance</th></tr></thead>
<tbody>
<tr><td>Total chlorine after the carbon tanks</td><td>No more than 0.1 mg/L</td><td>Before treatment begins each day, and through the day as the unit policy states</td></tr>
<tr><td>Bacteria</td><td>Below 100 colony-forming units (CFU) per mL; act at 50</td><td>At least monthly</td></tr>
<tr><td>Endotoxin</td><td>Below 0.25 endotoxin units (EU) per mL; act at half that level</td><td>As the facility&rsquo;s adopted standard requires</td></tr>
<tr><td>Chemical contaminants</td><td>Individual limits for each contaminant</td><td>At least every six months</td></tr>
</tbody></table></div>
<p>These limits do not come from randomized trials, and none could ethically be run. They come from outbreak investigations, toxicology, and engineering consensus. Each includes an &ldquo;action level&rdquo; set below the maximum, so that a unit intervenes while the water is still within specification. The evidence that failure causes harm is nonetheless strong, because the harm has been seen directly in outbreaks of hemolysis, aluminum poisoning, and fever reactions. What that evidence does not tell you is the exact safe threshold. The numbers are consensus values with a safety margin built in.</p>
<p><strong>The limits are consensus values, but the harm they guard against has been seen directly. Treat a failed or missing test as a real hazard, not a paperwork gap.</strong></p>
"""},
        {"id": "bedside", "nav": "Checks and release", "tag": "Clinical application", "h2": "Release criteria, machine checks, documentation",
         "html": """
<p><strong>Release before first use.</strong> At the start of each treatment day, someone confirms two things. The water system is running within its normal pressures and readings. The total chlorine test after the carbon tanks has been done, read at the correct time with in-date reagent, and recorded. In many Philippine units a technician performs the test. As the nurse in charge, you remain responsible for knowing it was done before any patient is connected. If the result is above the unit&rsquo;s action threshold, if the test was not done, or if the log is blank, <strong>treatment does not start on that supply</strong>. Inform the charge nurse, technician, and nephrologist. Follow the unit&rsquo;s procedure for retesting and finding the failure, and document the hold. If patients are already dialyzing when a failure is found, stop their treatments as the procedure directs and assess them for hemolysis.</p>
<p><strong>Machine and circuit checks before each patient.</strong> The exact sequence belongs to the manufacturer&rsquo;s manual and the unit procedure. The checks answer a fixed set of questions:</p>
<ul>
<li>Has the machine passed its self-test, and is it free of residual disinfectant?</li>
<li>Are the correct acid and bicarbonate concentrates connected, and do conductivity and temperature read within range? Does an independent check agree, where the unit requires one?</li>
<li>Is the dialyzer the one prescribed? If reprocessed, does it carry this patient&rsquo;s name, has it passed its checks, and has residual germicide been tested as absent?</li>
<li>Is the circuit primed without air, are all connections tight, and are clamps and caps in place?</li>
<li>Are the air detector, blood-leak detector, and pressure alarms armed, with limits set close to the working pressures and never bypassed?</li>
</ul>
<p><strong>Documentation is the release.</strong> A log entry records that a named person verified a safety barrier at a stated time. An entry made from memory at the end of the shift, or copied from the day before, removes the barrier while appearing to keep it.</p>
<p><strong>If you did not see the result, do not sign for it. If there is no result, no patient is connected.</strong></p>
"""},
    ],
    "case": {
        "title": "A blank line in the log",
        "html": """
<p>It is Monday, 6:15 a.m. You are the opening nurse. Six patients are waiting, some after a three-day gap. Among them is Mr. Danilo Cruz, 58, who arrived breathless and 4 kilograms above his dry weight. The water-room log shows Saturday&rsquo;s total chlorine result but nothing for today. The technician, Mr. Jun Villanueva, tells you, &ldquo;It is always fine, the carbon was changed last month. I will test it after we start.&rdquo; Every machine shows normal conductivity and temperature.</p>
""",
        "acte": {
            "Assess": "Whether today&rsquo;s test has been done at the correct sampling point; reagent expiry; water-system readings; which patients are most at risk from delay (breathlessness, high potassium risk).",
            "Communicate": "State clearly to the technician and charge nurse that no patient will be connected until the test is done and recorded; inform the nephrologist if the result fails or delay is prolonged.",
            "Teach": "Explain to waiting patients, plainly, that a safety check on the water is being completed.",
            "Escalate": "A failed result: hold the supply, follow the unit procedure, notify the medical director; assess any patient with symptoms of fluid overload or hyperkalemia for urgent alternatives.",
        },
        "task": "Write the log entry and the handoff note you would leave for the next shift, assuming the test was done at 6:40 a.m. and passed.",
    },
    "quiz": [
        {"stem": "Which component of a dialysis water system is responsible for removing chlorine and chloramine?",
         "options": [
             ("The water softener", False, "The softener exchanges calcium and magnesium for sodium. It does not remove chlorine."),
             ("The reverse osmosis membrane", False, "Reverse osmosis does not reliably remove chloramine and is damaged by chlorine."),
             ("The carbon tanks", True, "Activated carbon adsorbs chlorine and chloramine. Because carbon is exhausted without warning, total chlorine is tested after the tanks each treatment day."),
             ("The sediment filter", False, "The sediment filter removes particles only."),
         ],
         "objective": "Trace water from the municipal or deep-well supply to the dialyzer and state what each treatment stage removes.", "sources": ["iso23500_3", "doh2013"], "flag": ""},
        {"stem": "At the start of the day, the total chlorine test after the carbon tanks reads above the unit&rsquo;s action threshold. Six patients are waiting. What do you do?",
         "options": [
             ("Begin treatments and repeat the test in one hour", False, "Patients would be exposed to chloramine, which can cause hemolysis."),
             ("Begin treatments on the patients who waited longest and hold the rest", False, "No patient should be exposed to a supply that has failed the test."),
             ("Hold initiation of all treatments on that supply, notify the responsible staff, and follow the unit procedure", True, "A supply that fails the facility&rsquo;s action threshold is not released. The hold, notification, retest, and corrective steps follow the unit&rsquo;s procedure and are documented."),
             ("Increase the dialysate flow rate to dilute the chlorine", False, "Dialysate flow does not change the chlorine concentration of the water."),
         ],
         "objective": "Apply release criteria: hold treatment when a required test fails or is missing, and escalate.", "sources": ["iso23500_3", "doh2013", "psn2024"], "flag": "The action threshold and corrective steps are those of the facility&rsquo;s adopted standard and water policy."},
        {"stem": "All machines display normal dialysate conductivity and temperature. What can you conclude about the safety of the water?",
         "options": [
             ("The water is free of chloramine", False, "Conductivity does not detect chloramine."),
             ("The water meets bacterial and endotoxin limits", False, "Neither sensor detects microbes or endotoxin."),
             ("No further water testing is needed today", False, "Required water tests are independent of machine monitoring."),
             ("The dialysate is correctly proportioned and warmed, but other water hazards have not been verified", True, "Conductivity confirms the ionic mix and temperature confirms warming. Chloramine, microbes, endotoxin, and trace chemicals require separate tests."),
         ],
         "objective": "Explain what dialysate conductivity and temperature monitoring detect, and what they do not.", "sources": ["iso23500_3"], "flag": ""},
    ],
    "reflect": "Who performs the total chlorine test in your unit, where is the sample taken, and how would you know if it had not been done? If you cannot answer all three, find out before your next shift.",
    "practice": {
        "intro": "With the unit technician and your preceptor, in the water room and on an unconnected machine.",
        "items": [
            "Traces the water path and names each component and its purpose.",
            "Observes, then performs, a total chlorine test at the correct sampling point with correct timing.",
            "Reads and interprets the water-system log, and identifies a missing or out-of-range entry.",
            "States the unit&rsquo;s action threshold, hold procedure, and whom to notify.",
            "Completes the pre-treatment machine and circuit checks per the manufacturer&rsquo;s manual without prompting.",
            "Demonstrates the residual-disinfectant or germicide test used in the unit.",
        ],
    },
    "readings": [
        ("dialysis-water-treatment-systems.html", "The site&rsquo;s clinical and engineering reference on hemodialysis water treatment. Assigned reading for this module."),
        ("dialyzer-reprocessing-reuse.html", "Reprocessing, germicide testing, and reuse safety."),
        ("dialysis-qapi-vs-cqi.html", "Where water monitoring sits in the unit&rsquo;s quality program."),
        ("typhoon-disaster-preparedness-dialysis.html", "Water and power interruptions during disasters."),
    ],
    "calcs": ["calc-dialysis-water-reuse.html"],
    "external": [
        ("ISO 23500-3:2024 (standard summary page)", "https://www.iso.org/standard/84370.html"),
        ("Department of Health order 2013-0003 on dialysis water", "https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036"),
    ],
    "terms": [
        ("Chloramine", "A disinfectant formed from chlorine and ammonia, added to municipal water; causes hemolysis if it reaches the blood."),
        ("Hemolysis", "Destruction of red blood cells."),
        ("Endotoxin", "Fragments of bacterial cell wall that provoke fever and inflammation."),
        ("Biofilm", "A layer of bacteria attached to the inner surface of pipes and tanks."),
        ("Conductivity", "The ability of a solution to carry electric current; used to check the ionic concentration of dialysate."),
        ("Action level", "A result below the maximum limit at which corrective steps begin."),
    ],
    "image": {
        "file": "renal-nursing-08-water-room-log",
        "alt": "Dialysis staff member reviews the water-system monitoring log before treatment.",
        "purpose": "Show the release step: a person reading the log before the day begins.",
        "scene": "A Filipino dialysis technician or nurse in scrubs stands in a compact water-treatment room holding an open logbook, pen poised, looking from the page toward a row of tall cylindrical tanks and a wall-mounted panel of gauges.",
        "focal": "The person and the open logbook; tanks behind.",
        "setting": "Tiled water room in a Philippine dialysis center, pipes along the wall, a small sampling tap.",
        "details": "Two matching tall tanks side by side suggesting carbon tanks in series; a small test kit on a shelf.",
        "exclusions": "No readable log entries, gauge numbers, or labels; no brand names; do not attempt to depict a technically complete treatment train.",
        "archetype": "J (Environmental storytelling)", "reviewer": "Dialysis water technician or biomedical engineer, and nephrologist",
        "diagram_note": "A treatment-train diagram must be built as reviewed site-native markup or a verified vector graphic; topology and sampling points require technical review.",
    },
    "flags": [
        "Numeric water limits are commonly cited ISO 23500-3 values shown for orientation; the facility&rsquo;s adopted standard and edition govern.",
        "Endotoxin testing frequency is not specified in the Philippine sources reviewed.",
        "Machine check sequence is manufacturer-specific and intentionally generic.",
    ],
    "crosswalk": {
        "ph": "DOH AO 2012-0001 and AO 2013-0003 water requirements; PSN 2024 water testing schedule",
        "anna": "Hemodialysis: water treatment, dialysate, equipment",
        "edtna": "Dialysis technology: water treatment and machine safety",
        "nncc": "Hemodialysis",
    },
}
