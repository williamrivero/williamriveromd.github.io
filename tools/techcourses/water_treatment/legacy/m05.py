# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician collecting a water sample from a port on a dialysis water loop.",
    "objectives": [
        "Explain what biofilm is and why it is easier to prevent than to remove.",
        "State the limits and action levels for bacteria and endotoxin in dialysis water and dialysis fluid.",
        "Collect a water sample for culture and endotoxin testing using clean technique.",
        "Describe heat and chemical disinfection and the checks that prove the system is safe to use afterward.",
    ],
    "big": """
{{plain:Reverse osmosis water is very clean, but bacteria still find places to live: in tanks, in pipe joints, in connectors. They form a slippery layer called biofilm, which sheds bacteria and endotoxin into the water. You cannot see it. You find it by sampling, and you control it by keeping water moving and by disinfecting on a schedule, before counts rise.}}
{{cards:Key terms for this module|Biofilm::A layer of bacteria stuck to a surface inside a protective slime.|Culture::Growing bacteria from a water sample on a plate so they can be counted.|Colony-forming unit::The unit for counting bacteria in a culture.|Endotoxin unit::The unit for measuring endotoxin.|Aseptic technique::Working so that your hands, the air, and the container add no germs to the sample.|Dwell time::How long a disinfectant must stay in the system to work.|Residual test::A test proving the disinfectant has been rinsed out.}}
""",
    "case": {
        "title": "Chills on the Wednesday shift",
        "html": """
<p>Three patients on the same shift develop chills and a mild fever about an hour into treatment. None has signs of an access infection. The last monthly culture, two weeks ago, was 40 colony-forming units per milliliter at the end of the loop, up from 10 the month before. The loop disinfection due last week was postponed because the unit was busy.</p>
""",
        "questions": ["What do these three patients have in common?",
                      "Was the last culture result acceptable, and did it call for action?",
                      "What do you do now, and what is not your decision?"],
    },
    "sections": [
        ("biofilm", "Biofilm", "Where bacteria live in a water system", """
{{flow:How biofilm forms|Attachment::A few bacteria stick to a pipe wall or joint.|Growth::They multiply and build a protective slime.|Maturity::The layer resists disinfectant and sheds cells and endotoxin.|Spread::Shed bacteria settle further along the loop.}}
<p>Biofilm forms fastest where water is warm, still, or rough-surfaced: storage tanks, dead legs, old flexible hoses, the lines that connect machines to the loop, and bicarbonate concentrate containers. Once mature it is very hard to remove, so the strategy is prevention: continuous flow, sound design, and regular disinfection before counts rise.[[coulliette2013]]</p>
{{fig:wts_isolation|Stagnant branches are where biofilm starts. Short connections and continuous flow are the first defense.}}
"""),
        ("limits", "Limits", "Limits and action levels", """
{{fig:wts_tiers}}
<div class="table-wrap"><table>
<thead><tr><th>Fluid</th><th>Bacteria: limit</th><th>Bacteria: typical action level</th><th>Endotoxin: limit</th><th>Endotoxin: typical action level</th></tr></thead>
<tbody>
<tr><td>Dialysis water</td><td>Less than 100 CFU/mL</td><td>50 CFU/mL</td><td>Less than 0.25 EU/mL</td><td>0.125 EU/mL</td></tr>
<tr><td>Standard dialysis fluid</td><td>Less than 100 CFU/mL</td><td>50 CFU/mL</td><td>Less than 0.5 EU/mL</td><td>0.25 EU/mL</td></tr>
<tr><td>Ultrapure dialysis fluid</td><td>Less than 0.1 CFU/mL</td><td>&mdash;</td><td>Less than 0.03 EU/mL</td><td>&mdash;</td></tr>
</tbody></table></div>
<p>The limits are those of the international standard; action levels are typically set at half the limit, and your facility&rsquo;s written values are the ones that apply.[[iso23500_3]][[iso23500_5]] Many units sample monthly, and more often after a high result, a repair, or a new installation. Laboratories use low-nutrient culture plates incubated at room temperature for about seven days, because water bacteria grow slowly; a hospital blood-culture method will undercount them.</p>
{{key:A result between the action level and the limit is not a pass. It is the signal to act while there is still a margin.}}
"""),
        ("sampling", "Sampling", "Taking a sample that can be trusted", """
<p>A dirty sample port or a careless hand can add more bacteria than the water contains, and a falsely high result leads to wasted disinfections and lost trust in the numbers. A falsely low result is worse.</p>
{{flow:Collecting a culture and endotoxin sample|Prepare::Use the sterile, endotoxin-free containers the laboratory supplies. Label them first: point, date, time, your name.|Clean hands, gloves::Perform hand hygiene and wear clean gloves.|Flush the port::Open it and let water run for the stated time, commonly at least a minute.|Do not wipe with chemicals unless told to::If the procedure calls for alcohol, let it dry fully; never use bleach on a sample port.|Collect::Fill without touching the inside of the cap or container. Close at once.|Keep cold and send::Refrigerate and deliver within the time the laboratory states.}}
<p>Sample points usually include the start of the loop, the end of the loop (the return, where counts are highest), any storage tank outlet, and a rotating selection of machines for dialysis fluid. Samples are taken <em>before</em> a scheduled disinfection, when counts are at their highest, so the result reflects the worst case patients were exposed to.</p>
"""),
        ("disinfection", "Disinfection", "Disinfecting the system", """
{{cards:Two ways to disinfect|Heat::Hot water is circulated through the loop for a set time. It leaves no chemical behind, so it can be done often. The system must be built for it.|Chemical::A disinfectant such as peracetic acid or bleach is circulated and left to dwell. It must then be rinsed out completely and a residual test must be negative.}}
{{flow:A chemical disinfection, in outline|Plan::No patients on dialysis. Post warning signs. Wear the protective equipment on the safety data sheet.|Dose::Add the amount the procedure states and circulate.|Prove it arrived::Test for the disinfectant at the farthest point.|Dwell::Leave for the stated time.|Rinse::Flush until the residual test is negative at every outlet.|Record and release::Write down concentrations, times, test results, and names.}}
<p>Follow the manufacturer&rsquo;s instructions for your system: the wrong chemical, strength, or temperature can destroy membranes and pipework. Never mix bleach with acid products, which releases chlorine gas. The lines that connect each machine to the loop and the machines themselves are disinfected as part of the same program, because a clean loop feeding a dirty connector hose is still contaminated.</p>
{{stop:A positive residual test means disinfectant is still in the water. No patient is connected until every outlet tests negative and the result is recorded.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> The three patients share a shift and the same water and dialysate supply. Reactions in several patients at once point to something they share: tell the charge nurse immediately that the water system may be involved and that a disinfection was missed. The last culture of 40 CFU/mL was under the limit of 100 and under a typical action level of 50, but it had quadrupled in a month. That trend, with a postponed disinfection, called for action two weeks ago. Now: follow the nurse&rsquo;s and medical director&rsquo;s direction, collect water and dialysate samples for culture and endotoxin before any disinfection so the evidence is not destroyed, then disinfect and document the rinse. Whether treatments continue, stop, or move is a clinical decision. Postponing disinfection because the unit is busy should be reported as a system problem and reviewed.</p>
"""],
    "skills": {
        "title": "Aseptic sampling and a documented disinfection",
        "intro": "Materials: laboratory sample containers, gloves, the sampling plan, the disinfection procedure, the safety data sheet, and residual test strips.",
        "items": [("Labels containers before sampling with point, date, time, and name.", False),
                  ("Performs hand hygiene and wears clean gloves.", False),
                  ("Flushes the sample port for the stated time.", True),
                  ("Collects the sample without touching the inside of the cap or container.", True),
                  ("Stores and sends the sample as the laboratory requires.", False),
                  ("Confirms no patient is on dialysis and posts warning signs before a chemical disinfection.", True),
                  ("Wears the protective equipment listed on the safety data sheet.", True),
                  ("Verifies disinfectant at the farthest point and observes the full dwell time.", False),
                  ("Rinses and obtains a negative residual test at every outlet before release.", True),
                  ("Records concentrations, times, results, and names.", False)],
        "placement": "Take part in one full sampling round and one full loop disinfection under observation, and file the laboratory report when it returns.",
    },
    "quiz": [
        ("What is biofilm?",
         ["A plastic lining in pipes", "A layer of bacteria attached to a surface inside a protective slime", "A type of filter", "Scale from hard water"], 1,
         "Biofilm sheds bacteria and endotoxin and resists disinfectant."),
        ("In the international standard, what is the bacteria limit for dialysis water?",
         ["Less than 1 CFU/mL", "Less than 100 CFU/mL", "Less than 500 CFU/mL", "Less than 1,000 CFU/mL"], 1,
         "The limit is less than 100 CFU/mL, with an action level typically at 50."),
        ("A culture result lies between the action level and the limit. What does this mean?",
         ["Pass; no action", "Act now, while there is still a margin", "The laboratory made an error", "Stop all dialysis permanently"], 1,
         "Action levels exist so that the limit is never reached."),
        ("When are routine culture samples best taken?",
         ["Just after disinfection", "Just before a scheduled disinfection", "Only when patients have fever", "Once a year"], 1,
         "Sampling before disinfection shows the highest level patients were exposed to."),
        ("Why is the sample port flushed before collecting?",
         ["To cool the water", "To clear water and bacteria that sat in the port, so the sample represents the loop", "To add chlorine", "To fill the drain"], 1,
         "Stagnant water in the tap does not represent the system."),
        ("After a chemical disinfection, what must be shown before any patient is connected?",
         ["A negative residual test at every outlet", "A warm loop", "A full brine tank", "A new filter"], 0,
         "Residual disinfectant reaching a patient causes harm."),
        ("Why must bleach never be mixed with acid products?",
         ["The mixture is too weak", "It releases chlorine gas", "It stains the pipes", "It makes foam"], 1,
         "Chlorine gas is toxic. Use and store these products separately."),
        ("Several patients on one shift develop chills at about the same time. What is the technician&rsquo;s first step?",
         ["Start a disinfection immediately", "Tell the charge nurse at once that the water or dialysate may be involved", "Wait for the monthly culture", "Change the sediment filter"], 1,
         "Report first. The clinical team decides about patients, and samples should be taken before disinfection."),
    ],
    "terms": [("Peracetic acid", "A chemical disinfectant widely used for dialysis water systems and machines."),
              ("Safety data sheet", "The document that lists a chemical&rsquo;s hazards, protective equipment, and first aid."),
              ("Pyrogenic reaction", "Fever and chills during dialysis caused by endotoxin or bacteria in the fluid.")],
    "readings": [("dialysis-water-treatment-systems.html", "Disinfection strategies and microbiological monitoring in full."),
                 ("hemodiafiltration-deep-dive.html", "Why ultrapure fluid is required for hemodiafiltration.")],
}
