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
{{plain:Look inside an old kettle in a house with hard water and you will find a white, chalky crust on the bottom. Leave a basin of water in a warm corner for a week and its sides turn slimy. The fluid path inside a dialysis machine is warm, wet, and fed with bicarbonate, so it grows both: a crust called scale, and a film of bacteria. That is why the machine washes itself with heat or chemicals between uses. The same cabinet holds mains electricity next to water, with a patient connected by a column of blood and saline, so its electrical safety is tested on a schedule. This module covers both kinds of hygiene: chemical and electrical.}}
<p>The picture has a limit. A kettle with a little scale still boils water, and nobody drinks from the basin. In a machine, scale makes sensors read wrongly, bacteria reach the dialysate, and any cleaning chemical left behind can reach a patient&rsquo;s blood. Every cleaning step, and every test that proves it worked, exists for one of those reasons.</p>
{{cards:Key terms for this module|Scale::A hard crust of calcium carbonate that forms when bicarbonate dialysate dries or warms.|Descaling::Dissolving scale with an acid. Also called decalcification.|Disinfection::Killing microbes with heat or chemicals.|Residual::Disinfectant left behind after rinsing.|Protective earth::The grounding wire that carries fault current safely away from the metal case.|Leakage current::A small unwanted current that flows from equipment to ground or through a person.|Electrical safety analyzer::The test instrument that measures earth resistance and leakage current.}}
""",
    "case": {
        "title": "Bleach after acid",
        "html": """
<p>It is Friday, almost eight in the evening, at the end of a long day. Mr. Paolo Santos, 27, a technician in his first year, runs an acid descaling program on machine 4. He wants to &ldquo;do a thorough job,&rdquo; so he connects a bleach container without waiting for the rinse to finish. Within a minute a sharp smell fills the room. His colleague, Ms. Liza Ramos, begins to cough.</p>
<p>At six the next morning, machine 4 is prepared for the first shift. The residual test is skipped because the box of strips is empty.</p>
""",
        "questions": ["What caused the smell, and what should happen in the room right now?",
                      "What is the risk of using machine 4 without a residual test?",
                      "What needs to change in the workshop so neither event happens again?"],
    },
    "sections": [
        ("why", "Why machines foul", "What builds up inside a machine", """
<p>Think about what flows through the machine in a day: treated water, acid concentrate carrying calcium and magnesium, bicarbonate, and used dialysate carrying what was removed from the patient&rsquo;s blood. Three kinds of deposit follow from that mix.</p>
{{cards:Three kinds of deposit|Scale::Calcium and magnesium from the acid concentrate combine with bicarbonate and form a crust on heaters, sensors, and valves.|Organic film::Proteins and fats from used dialysate coat the lines after the dialyzer.|Biofilm::Bacteria attach to surfaces, especially where bicarbonate concentrate sits, and shed endotoxin.}}
<p>Each deposit causes its own trouble, and the trouble usually looks like a machine fault. Scale insulates the heater, coats conductivity sensors so they read wrongly, and makes valves stick. Organic film blinds the blood leak detector. Biofilm contaminates dialysate that started with clean water.[[iso23500_1]] The practical point is that a drifting sensor or a sticking valve may be a cleaning problem before it is a parts problem.</p>
"""),
        ("programs", "Cleaning programs", "Matching the program to the problem", """
<div class="table-wrap"><table>
<thead><tr><th>Program</th><th>Typical agent</th><th>What it removes</th><th>What it does not do</th></tr></thead>
<tbody>
<tr><td>Descaling</td><td>Citric acid or acetic acid</td><td>Scale</td><td>It does not reliably disinfect by itself, unless it is combined with heat as the manual states</td></tr>
<tr><td>Chemical disinfection and cleaning</td><td>Bleach (sodium hypochlorite) or peracetic acid</td><td>Organic film and microbes</td><td>Bleach leaves scale in place</td></tr>
<tr><td>Heat disinfection</td><td>Hot water, often with citric acid</td><td>Microbes; with citric acid, scale as well</td><td>It does not remove heavy organic film</td></tr>
</tbody></table></div>
<p>Read the table across. Each agent does one job well and leaves another undone, which is why a machine runs more than one kind of program. The manufacturer states which agents, strengths, and frequencies are approved for each model. A different chemical, even a stronger one, can corrode metal parts, harden seals, and void the machine&rsquo;s safety approval. Typically a machine is disinfected after each treatment day and after any service that opens the fluid path, and it is descaled at a stated interval.</p>
{{flow:A chemical disinfection cycle|Draw in::The machine takes up the agent at a set dilution.|Circulate and dwell::The agent reaches every part of the fluid path for the stated time.|Rinse::Treated water flushes the agent out.|Residual test::A test strip at the stated outlet shows none remains.|Record::Program, agent, time, residual result, name.}}
{{stop:Never run a bleach program and an acid program back to back without the full rinse between them. When bleach meets acid, chlorine gas is released.}}
{{key:A residual test is required after every chemical disinfection, before the machine is used. If there are no strips, there is no treatment on that machine.}}
<p>The fluid path does not end at the cabinet. The hoses that connect the machine to the water loop and to the drain belong to it too, and a clean machine on a dirty inlet hose is not clean. Follow your center&rsquo;s program for disinfecting or replacing them. Follow it as well for the filters at the machine that produce ultrapure dialysate; each has a maximum number of uses or days.</p>
{{fig:wts_pou|Filters at the machine give a final barrier against bacteria and endotoxin. They have a stated life and are replaced on schedule.}}
"""),
        ("electrical", "Electrical safety", "Why electrical safety is tested", """
<p>Electric current follows the easiest path to earth. Dry skin is a poor path. A dialysis patient, however, is connected to the machine by blood and saline, which conduct electricity well, and may have a catheter whose tip lies close to the heart. In that situation, currents far too small to feel can be dangerous. Dialysis machines are therefore designed with a grounded metal case, insulated internal circuits, and strict limits on leakage current.[[iec60601]]</p>
{{cards:Two protections you test|Protective earth::If a live wire touches the case, the earth wire carries the current away and the fuse blows. A broken or corroded earth connection removes that protection without any sign.|Insulation and leakage::Insulation keeps mains voltage away from the case and the patient. As it ages or gets wet, more current leaks through it.}}
<p>Both protections can fail while the machine runs perfectly, so you cannot find these faults by watching a treatment. Periodic testing follows the international standard for recurrent tests, or the national rule that applies to your facility.[[iec62353]] You do the tests with an electrical safety analyzer: at the interval the manufacturer states, after any repair that could affect electrical safety, and after a machine has been dropped, flooded, or opened for major work.</p>
{{flow:An electrical safety test, in outline|Inspect::Plug, cord, strain relief, case, and labels. Many faults are visible.|Protective earth resistance::Measure from the earth pin to exposed metal.|Leakage current::Measure by the method the standard and the manual specify.|Functional check::The machine works normally afterward.|Record::Values, limits, analyzer identity, pass or fail.}}
<p>For a machine with a detachable power cord, the recurrent-test standard gives a limit of 0.3 ohm for protective earth resistance. Leakage limits depend on the equipment class and the type of patient connection, so take them from the standard and the service manual, not from memory.[[iec62353]]</p>
<p>The socket matters as well. The earth wire in the cord is only useful if the outlet connects it to earth, so a perfect machine on an ungrounded outlet is not protected. Dialysis stations need correctly grounded outlets on suitably protected circuits. That is a matter for the facility&rsquo;s electrical engineer; your part is to notice and report.</p>
{{stop:A machine that fails an electrical safety test is out of service. So is a machine with a damaged cord, a cracked plug, or signs that fluid has entered the electronics.}}
"""),
    ],
    "debrief": ["""
<p><strong>What caused the smell, and what happens in the room.</strong> Chlorine gas. The bleach met acid that was still in the machine because the rinse had not finished. Clear the room and ventilate it. Ms. Ramos is assessed and the exposure is reported. The machine is rinsed fully before anything else is run on it.</p>
<p><strong>The risk of skipping the residual test.</strong> It is a second, separate hazard, and nobody can smell it. Bleach or acid remaining in the fluid path can reach a patient&rsquo;s blood. Machine 4 is not used until a residual test is negative. An empty box of strips is a reason to wait, not a reason to skip.</p>
<p><strong>What needs to change in the workshop.</strong> Programs are run as the manual sequences them, with every rinse completed. Chemicals are stored and labeled separately. Test strips have a reorder point so they never run out. And &ldquo;doing extra&rdquo; is understood as a deviation from the procedure, not as diligence. Mr. Santos meant well; the procedure is what protects him and the patient.</p>
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
