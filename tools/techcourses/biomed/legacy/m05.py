# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician connecting an electrical safety analyzer to a hemodialysis machine.",
    "objectives": [
        "Explain why the inside of a dialysis machine scales and grows bacteria.",
        "Distinguish cleaning, descaling, and disinfection, and match each to its purpose.",
        "Explain why a residual disinfectant test is required before use.",
        "Describe the purpose of protective earth and leakage current tests and when they are performed.",
    ],
    "big": """
{{plain:The fluid path inside a dialysis machine is warm, wet, and fed with bicarbonate, which is close to ideal for bacteria and for a chalky crust called scale. So the machine washes itself with heat or chemicals between uses. The same cabinet holds mains electricity next to water, with a patient connected by a column of blood and saline. So its electrical safety is tested on a schedule. This module covers both kinds of hygiene: chemical and electrical.}}
{{cards:Key terms for this module|Scale::A hard crust of calcium carbonate that forms when bicarbonate dialysate dries or warms.|Descaling::Dissolving scale with an acid. Also called decalcification.|Disinfection::Killing microbes with heat or chemicals.|Residual::Disinfectant left behind after rinsing.|Protective earth::The grounding wire that carries fault current safely away from the metal case.|Leakage current::A small unwanted current that flows from equipment to ground or through a person.|Electrical safety analyzer::The test instrument that measures earth resistance and leakage current.}}
""",
    "case": {
        "title": "Bleach after acid",
        "html": """
<p>At the end of a long day a technician runs an acid descaling program on a machine. Wanting to &ldquo;do a thorough job,&rdquo; the technician then connects a bleach container without waiting for the rinse to finish. A sharp smell fills the room and a colleague begins to cough. The next morning the same machine&rsquo;s residual test is skipped because the strips have run out.</p>
""",
        "questions": ["What caused the smell, and what should happen in the room?",
                      "What is the risk of skipping the residual test?",
                      "What needs to change in the workshop?"],
    },
    "sections": [
        ("why", "Why machines foul", "What builds up inside a machine", """
{{cards:Three kinds of deposit|Scale::Calcium and magnesium from the acid concentrate combine with bicarbonate and form a crust on heaters, sensors, and valves.|Organic film::Proteins and fats from used dialysate coat the lines after the dialyzer.|Biofilm::Bacteria attach to surfaces, especially where bicarbonate concentrate sits, and shed endotoxin.}}
<p>Each deposit causes its own trouble. Scale insulates the heater, coats conductivity sensors so they read wrongly, and makes valves stick. Organic film blinds the blood leak detector. Biofilm contaminates dialysate that started with clean water.[[iso23500_1]]</p>
"""),
        ("programs", "Cleaning programs", "Matching the program to the problem", """
<div class="table-wrap"><table>
<thead><tr><th>Program</th><th>Typical agent</th><th>What it removes</th><th>What it does not do</th></tr></thead>
<tbody>
<tr><td>Descaling</td><td>Citric acid or acetic acid</td><td>Scale</td><td>Does not reliably disinfect by itself unless combined with heat as the manual states</td></tr>
<tr><td>Chemical disinfection and cleaning</td><td>Bleach (sodium hypochlorite) or peracetic acid</td><td>Organic film and microbes</td><td>Bleach does not remove scale</td></tr>
<tr><td>Heat disinfection</td><td>Hot water, often with citric acid</td><td>Microbes; with citric acid, scale as well</td><td>Does not remove heavy organic film</td></tr>
</tbody></table></div>
<p>The manufacturer states which agents, strengths, and frequencies are approved for each model. Using a different chemical can corrode metal parts, harden seals, and void the machine&rsquo;s safety approval. Typically a machine is disinfected after each treatment day and after any service that opens the fluid path, and descaled at a stated interval.</p>
{{flow:A chemical disinfection cycle|Draw in::The machine takes up the agent at a set dilution.|Circulate and dwell::The agent reaches every part of the fluid path for the stated time.|Rinse::Treated water flushes the agent out.|Residual test::A test strip at the stated outlet shows none remains.|Record::Program, agent, time, residual result, name.}}
{{stop:Never run bleach and acid programs back to back without the full rinse between them. Bleach and acid release chlorine gas.}}
{{key:A residual test is required after every chemical disinfection, before the machine is used. No strips means no treatment on that machine.}}
<p>The hoses that connect the machine to the water loop and to the drain are part of the fluid path too. A clean machine on a dirty inlet hose is not clean. Follow your center&rsquo;s program for disinfecting or replacing them, and for the filters at the machine that produce ultrapure dialysate, which have a maximum number of uses or days.</p>
{{fig:wts_pou|Filters at the machine give a final barrier against bacteria and endotoxin. They have a stated life and are replaced on schedule.}}
"""),
        ("electrical", "Electrical safety", "Why electrical safety is tested", """
<p>A dialysis patient is connected to the machine by blood and saline, which conduct electricity, and may have a catheter whose tip lies close to the heart. Currents far too small to feel can be dangerous in that situation. Dialysis machines are therefore designed with a grounded metal case, insulated internal circuits, and strict limits on leakage current.[[iec60601]]</p>
{{cards:Two protections you test|Protective earth::If a live wire touches the case, the earth wire carries the current away and the fuse blows. A broken or corroded earth connection removes that protection silently.|Insulation and leakage::Insulation keeps mains voltage away from the case and the patient. As it ages or gets wet, more current leaks.}}
<p>Periodic testing follows the international standard for recurrent tests, or the national rule that applies to your facility.[[iec62353]] The tests are done with an electrical safety analyzer: at the interval the manufacturer states, after any repair that could affect electrical safety, and after a machine has been dropped, flooded, or opened for major work.</p>
{{flow:An electrical safety test, in outline|Inspect::Plug, cord, strain relief, case, and labels. Many faults are visible.|Protective earth resistance::Measure from the earth pin to exposed metal.|Leakage current::Measure by the method the standard and the manual specify.|Functional check::The machine works normally afterward.|Record::Values, limits, analyzer identity, pass or fail.}}
<p>For a machine with a detachable power cord, the recurrent-test standard gives a limit of 0.3 ohm for protective earth resistance; leakage limits depend on the equipment class and the type of patient connection, so take them from the standard and the service manual, not from memory.[[iec62353]] The socket matters as well: a perfect machine on an ungrounded outlet is not protected. Dialysis stations need correctly grounded outlets on suitably protected circuits, which is a matter for the facility&rsquo;s electrical engineer.</p>
{{stop:A machine that fails an electrical safety test is out of service. So is one with a damaged cord, a cracked plug, or signs that fluid has entered the electronics.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> Bleach met acid still in the machine and released chlorine gas. The room is cleared and ventilated, the coughing colleague is assessed and the exposure reported, and the machine is rinsed fully before anything else is run. The next morning&rsquo;s skipped residual test is a second, separate hazard: bleach or acid remaining in the fluid path can reach a patient&rsquo;s blood. That machine is not used until a residual test is negative. What needs to change: programs are run as the manual sequences them, with rinses completed; chemicals are stored and labeled separately; test strips have a reorder point so they never run out; and &ldquo;doing extra&rdquo; is understood as a deviation from the procedure, not as diligence.</p>
"""],
    "skills": {
        "title": "Disinfection with residual test, and an electrical safety test",
        "intro": "Materials: an out-of-service machine, its manual, approved disinfectant, residual test strips, protective equipment, and an electrical safety analyzer with a valid calibration.",
        "items": [("Selects the program and agent approved in the manual for the stated purpose.", True),
                  ("Wears the protective equipment on the safety data sheet and ventilates the area.", False),
                  ("Allows the complete cycle, including the rinse, to finish.", True),
                  ("Performs the residual test at the stated outlet and reads it at the stated time.", True),
                  ("Records the program, agent, times, and residual result.", False),
                  ("Inspects the plug, cord, and case and reports any damage.", False),
                  ("Measures protective earth resistance and compares with the limit.", True),
                  ("Measures leakage current by the manual&rsquo;s method and compares with the limit.", True),
                  ("Tags the machine out of service if any test fails.", True)],
        "placement": "With a senior technician, check how many power outlets at the treatment stations have been verified as grounded, and when.",
    },
    "quiz": [
        ("What is scale inside a dialysis machine mostly made of?",
         ["Dried blood", "Calcium carbonate from bicarbonate dialysate", "Rust", "Salt from the softener"], 1,
         "Calcium and magnesium combine with bicarbonate to form a hard crust."),
        ("Which agent removes scale?",
         ["Bleach", "An acid such as citric acid", "Plain water", "Alcohol"], 1, "Acid dissolves carbonate scale; bleach does not."),
        ("Why must bleach and acid programs never be run back to back without rinsing?",
         ["They cancel each other", "They release chlorine gas", "They stain the lines", "They cool the heater"], 1,
         "The mixture releases toxic chlorine gas."),
        ("What does a residual test show?",
         ["That the disinfectant was strong enough", "That no disinfectant remains after rinsing", "That the water is soft", "That the heater works"], 1,
         "It protects the patient from chemical remaining in the fluid path."),
        ("Residual test strips have run out. What is correct?",
         ["Rinse twice and use the machine", "Smell the fluid", "Do not use the machine until a residual test is negative", "Use strips for a different chemical"], 2,
         "Without a valid test there is no proof the chemical is gone."),
        ("What is the purpose of the protective earth connection?",
         ["To reduce noise", "To carry fault current safely away from the case", "To power the screen", "To measure conductivity"], 1,
         "It prevents the case from becoming live if insulation fails."),
        ("When is an electrical safety test required apart from the scheduled interval?",
         ["Never", "After repairs affecting electrical safety, or after the machine is dropped or flooded", "Every treatment", "Only when new"], 1,
         "Any event that could affect insulation or earthing calls for a retest."),
        ("Why are dialysis patients especially vulnerable to small electrical currents?",
         ["They sit still", "They are connected to the machine by conductive blood and saline, sometimes through a catheter near the heart", "They wear metal", "The room is cold"], 1,
         "A direct conductive path makes very small currents hazardous."),
    ],
    "terms": [("Sodium hypochlorite", "The chemical name for bleach."),
              ("Peracetic acid", "A disinfectant used for dialysis machines and water systems."),
              ("Insulation", "Material that keeps electricity inside its intended path."),
              ("Ohm", "The unit of electrical resistance.")],
    "readings": [("dialysis-water-treatment-systems.html", "Fluid quality from the loop to the machine."),
                 ("hemodiafiltration-deep-dive.html", "Why ultrapure dialysate and machine filters matter.")],
}
