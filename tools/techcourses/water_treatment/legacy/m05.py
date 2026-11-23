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
{{plain:Think of the rooftop water tank at home. The water from the main line is clean, yet after a few months the inside walls of the tank feel slippery, and the corners where water sits still are the worst. That slippery layer is not dirt from outside. It is bacteria that settled, stuck, and grew. The same thing happens inside a dialysis water loop.}}
<p>The picture has a limit. You can open a home tank and scrub it. You cannot see inside a loop, and reverse osmosis water is far cleaner than tap water, so the layer grows slowly and without any sign. This layer is called biofilm, and it sheds bacteria and endotoxin into the water that reaches patients. You find it only by sampling. You control it by keeping water moving and by disinfecting on a schedule, before the counts rise.</p>
{{cards:Key terms for this module|Biofilm::A layer of bacteria stuck to a surface and covered by a protective slime.|Culture::Growing bacteria from a water sample on a plate so they can be counted.|Colony-forming unit::The unit for counting bacteria in a culture.|Endotoxin unit::The unit for measuring endotoxin.|Aseptic technique::Working so that your hands, the air, and the container add no germs of their own to the sample.|Dwell time::How long a disinfectant must stay in the system to work.|Residual test::A test that proves the disinfectant has been rinsed out.}}
""",
    "case": {
        "title": "Chills on the Wednesday shift",
        "html": """
<p>It is Wednesday, a little after 08:00. On the morning shift, three patients develop chills and a mild fever about an hour into treatment: Mr. Arnel Ramos, 58, at station 2, Mrs. Teresita Lim, 66, at station 6, and Mr. Jojo Pascual, 49, at station 9. The nurse, Ms. Liza Fernandez, finds no sign of an access infection in any of them, and she calls you to the floor.</p>
<p>You check the file. The last monthly culture, two weeks ago, was 40 colony-forming units per milliliter at the end of the loop, up from 10 the month before. The loop disinfection due last week was postponed because the unit was busy.</p>
""",
        "questions": ["What do these three patients share, and what does that point to?",
                      "Was the last culture result acceptable, and did it already call for action?",
                      "What do you do in the next hour, and what is not your decision?"],
    },
    "sections": [
        ("biofilm", "Biofilm", "Where bacteria live in a water system", """
{{flow:How biofilm forms|Attachment::A few bacteria stick to a pipe wall or a joint.|Growth::They multiply and build a protective slime around themselves.|Maturity::The layer now resists disinfectant and sheds cells and endotoxin.|Spread::The shed bacteria settle farther along the loop and start again.}}
<p>Biofilm forms fastest where the water is warm, where it stands still, or where the surface is rough: storage tanks, dead legs, old flexible hoses, the lines that connect machines to the loop, and bicarbonate concentrate containers. Once the layer is mature it is very hard to remove, because the slime shields the bacteria underneath. The strategy is therefore prevention: continuous flow, sound design, and regular disinfection before counts rise.[[coulliette2013]]</p>
{{fig:wts_isolation|Stagnant branches are where biofilm starts. Short connections and continuous flow are your first defense.}}
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
<p>The limits are those of the international standard. Action levels are typically set at half the limit, and the values written in your facility&rsquo;s own procedure are the ones that apply.[[iso23500_3]][[iso23500_5]] Many units sample monthly, and more often after a high result, a repair, or a new installation.</p>
<p>The method matters as much as the number. Water bacteria are used to living on very little food, so they grow slowly. Laboratories therefore use low-nutrient culture plates incubated at room temperature for about seven days. A hospital blood-culture method is designed for a different purpose and will undercount them.</p>
{{key:A result between the action level and the limit is not a pass. It is the signal to act while there is still a margin.}}
"""),
        ("sampling", "Sampling", "Taking a sample that can be trusted", """
<p>A sample is a small cup of water asked to speak for the whole loop. A dirty sample port or a careless hand can add more bacteria than the water itself contains. A falsely high result leads to wasted disinfections and lost trust in the numbers. A falsely low result is worse, because it tells everyone the water is safe when it is not.</p>
{{flow:Collecting a culture and endotoxin sample|Prepare::Use the sterile, endotoxin-free containers the laboratory supplies. Label them first: point, date, time, and your name.|Clean hands, gloves::Perform hand hygiene and put on clean gloves.|Flush the port::Open it and let water run for the stated time, commonly at least a minute.|Do not wipe with chemicals unless told to::If the procedure calls for alcohol, let it dry fully. Never use bleach on a sample port.|Collect::Fill without touching the inside of the cap or the container. Close it at once.|Keep cold and send::Refrigerate the sample and deliver it within the time the laboratory states.}}
<p>Sample points usually include the start of the loop, the end of the loop (the return, where counts are highest), any storage tank outlet, and a rotating selection of machines for dialysis fluid. Take samples <em>before</em> a scheduled disinfection, when counts are at their highest. The result then shows the worst case that patients were exposed to, which is the number you need to know.</p>
"""),
        ("disinfection", "Disinfection", "Disinfecting the system", """
{{cards:Two ways to disinfect|Heat::Hot water is circulated through the loop for a set time. It leaves no chemical behind, so it can be done often. The system must be built to take the heat.|Chemical::A disinfectant such as peracetic acid or bleach is circulated and left to dwell. It must then be rinsed out completely, and a residual test must be negative.}}
{{flow:A chemical disinfection, in outline|Plan::No patients on dialysis. Post warning signs. Wear the protective equipment listed on the safety data sheet.|Dose::Add the amount the procedure states and circulate it.|Prove it arrived::Test for the disinfectant at the farthest point.|Dwell::Leave it for the stated time.|Rinse::Flush until the residual test is negative at every outlet.|Record and release::Write down concentrations, times, test results, and names.}}
<p>Follow the manufacturer&rsquo;s instructions for your system. The wrong chemical, strength, or temperature can destroy membranes and pipework. Never mix bleach with acid products, because the mixture releases chlorine gas. The lines that connect each machine to the loop, and the machines themselves, are disinfected as part of the same program. A clean loop that feeds a dirty connector hose still delivers contaminated fluid.</p>
{{stop:A positive residual test means disinfectant is still in the water. No patient is connected until every outlet tests negative and the result is recorded.}}
"""),
    ],
    "debrief": ["""
<p><strong>What the three patients share.</strong> They share a shift, and they share the same water and dialysate supply. Reactions in several patients at the same time point to something common to all of them, not to three separate infections. Tell the charge nurse immediately that the water system may be involved and that a disinfection was missed.</p>
<p><strong>Was the last culture acceptable?</strong> The number was, but the trend was not. The result of 40 CFU/mL was under the limit of 100 and under a typical action level of 50. It had also quadrupled in a month. That rise, together with a postponed disinfection, called for action two weeks ago.</p>
<p><strong>What to do now, and what is not yours.</strong> Follow the direction of the nurse and the medical director. Collect water and dialysate samples for culture and endotoxin before any disinfection, so that the evidence of what patients were exposed to is not destroyed. Then disinfect and document the rinse. Whether treatments continue, stop, or move is a clinical decision, not yours. Finally, report the postponed disinfection as a system problem to be reviewed, because a unit that is busy will always find a reason to postpone it again.</p>
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
              ("Pyrogenic reaction", "Fever and chills during dialysis, caused by endotoxin or bacteria in the fluid.")],
    "readings": [("dialysis-water-treatment-systems.html", "Disinfection strategies and microbiological monitoring in full."),
                 ("hemodiafiltration-deep-dive.html", "Why ultrapure fluid is required for hemodiafiltration.")],
}
