# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A water treatment technician checking gauges in a dialysis water room.",
    "objectives": [
        "Explain why drinking water is not safe for dialysis without further treatment.",
        "Name the main groups of contaminants and the harm each can cause.",
        "Distinguish dialysis water, standard dialysis fluid, and ultrapure dialysis fluid.",
        "State who is responsible for water quality and what the technician must report.",
    ],
    "big": """
{{plain:Your stomach and gut protect you from most of what is in a glass of tap water. A dialysis patient has no such protection: the water goes into dialysate, and dialysate is separated from the blood only by a thin membrane with tiny pores. Small chemicals pass straight through. So dialysis water must be far cleaner than drinking water.}}
{{cards:The numbers that explain this job|About 14 liters::What a person drinks in a week.|More than 300 liters::The water a dialysis patient&rsquo;s blood is exposed to in a week, through the dialyzer.|One loop::Every station on the shift is fed from the same pipe.|Zero warning::Most contaminants have no taste, color, or smell.}}
{{cards:Key terms for this module|Contaminant::Anything in water that should not reach the patient.|Chloramine::Chlorine combined with ammonia, added to city water to kill germs. It destroys red blood cells in dialysis.|Endotoxin::A fragment of the wall of dead bacteria. It causes fever and chills.|Dialysis water::Treated water used to make dialysate and to rinse and reprocess equipment.|Dialysis fluid::Another name for dialysate: dialysis water mixed with concentrates.|Action level::A result below the maximum limit at which the unit must already investigate.}}
""",
    "case": {
        "title": "The city flushes its pipes",
        "html": """
<p>On a Monday morning the water utility announces that it has been flushing the mains over the weekend and has temporarily raised the disinfectant dose. The feed water looks slightly cloudy. The first shift is due to start in forty minutes. A nurse asks whether the water room needs anything, and a colleague says, &ldquo;The reverse osmosis unit is running normally, so we are fine.&rdquo;</p>
""",
        "questions": ["Which contaminant is most likely to have increased, and which stage removes it?",
                      "Does a normal reverse osmosis reading answer the question?",
                      "What would you test, and whom would you tell, before the first patient is connected?"],
    },
    "sections": [
        ("exposure", "Why it matters", "Drinking water and dialysis water are different products", """
<p>Water utilities treat water so that it is safe to drink. They add chlorine or chloramine to kill germs, and sometimes fluoride for teeth or aluminum salts to clear cloudiness. These are helpful in drinking water. In dialysis they are poisons, because they cross the dialyzer membrane directly into the blood.[[ward2011]][[cdc_water]]</p>
{{fig:kidney_vs_dialyzer|Healthy kidneys and the gut filter what we drink. On dialysis, water in the dialysate is separated from blood only by the dialyzer membrane.}}
<p>The quality of feed water also changes without notice. Utilities raise disinfectant doses after pipe repairs or floods. Wells change with the season. Tanker deliveries vary from load to load. A water system that was adequate last month can be overwhelmed this month, which is why testing is done every day and not once.</p>
"""),
        ("contaminants", "Contaminants", "Three groups of contaminants", """
{{cards:What can be in the water, and what it does|Chemicals added on purpose::Chlorine and chloramine destroy red blood cells (hemolysis). Fluoride in excess can cause itching, chest pain, and dangerous heart rhythms.|Chemicals from the ground and pipes::Aluminum harms the brain and bones over time. Calcium and magnesium (&ldquo;hardness&rdquo;) cause nausea, headache, and weakness. Copper, zinc, lead, and nitrate have each caused patient injuries.|Living contaminants::Bacteria grow in tanks and pipes. Their fragments, called endotoxin, cause fever, chills, and low blood pressure during treatment.}}
<p>The international standard sets a maximum for each chemical in dialysis water. A few examples show how strict the limits are: total chlorine 0.1 milligram per liter (mg/L), aluminum 0.01 mg/L, fluoride 0.2 mg/L, calcium 2 mg/L, and magnesium 4 mg/L.[[iso23500_3]] These are far below what is allowed in drinking water.</p>
<div class="table-wrap"><table>
<thead><tr><th>Contaminant</th><th>Where it comes from</th><th>What it can do to a patient</th><th>Main barrier</th></tr></thead>
<tbody>
<tr><td>Chlorine and chloramine</td><td>Added by the water utility</td><td>Breaks red blood cells; anemia</td><td>Carbon tanks</td></tr>
<tr><td>Calcium and magnesium</td><td>Natural minerals in ground water</td><td>Nausea, vomiting, weakness; also scales the membrane</td><td>Softener, then reverse osmosis</td></tr>
<tr><td>Aluminum, fluoride, nitrate, metals</td><td>Utility treatment, soil, pipes</td><td>Bone and brain disease, heart rhythm problems, anemia</td><td>Reverse osmosis</td></tr>
<tr><td>Bacteria and endotoxin</td><td>Growth inside tanks, filters, and pipes</td><td>Fever, chills, low blood pressure, long-term inflammation</td><td>Reverse osmosis, ultrafilters, disinfection</td></tr>
</tbody></table></div>
{{key:Carbon removes chlorine and chloramine. Reverse osmosis does not do this job reliably, and chlorine damages many reverse osmosis membranes. The carbon tanks must work, and they must be tested.}}
"""),
        ("tiers", "Purity levels", "Three levels of purity", """
{{fig:wts_tiers}}
<div class="table-wrap"><table>
<thead><tr><th>Fluid</th><th>What it is</th><th>Bacteria limit</th><th>Endotoxin limit</th></tr></thead>
<tbody>
<tr><td>Dialysis water</td><td>Water leaving the treatment system</td><td>Less than 100 colony-forming units per milliliter (CFU/mL)</td><td>Less than 0.25 endotoxin units per milliliter (EU/mL)</td></tr>
<tr><td>Standard dialysis fluid</td><td>Dialysis water mixed with concentrates</td><td>Less than 100 CFU/mL</td><td>Less than 0.5 EU/mL</td></tr>
<tr><td>Ultrapure dialysis fluid</td><td>Dialysis fluid passed through an extra filter at the machine</td><td>Less than 0.1 CFU/mL</td><td>Less than 0.03 EU/mL</td></tr>
</tbody></table></div>
<p>These are the limits of the international standard.[[iso23500_3]][[iso23500_5]] Units set an action level below each limit, commonly at half of it, so that a rising count is dealt with before the limit is reached. Ultrapure fluid is required for hemodiafiltration (HDF), in which fluid made from dialysate is infused into the blood.</p>
"""),
        ("roles", "Who is responsible", "Who is responsible for the water", """
{{cards:Roles in water quality|Medical director::Carries overall responsibility for water quality, approves limits and procedures, and reviews results.|Water treatment technician::Operates the system, performs and records tests, takes samples, and stops and reports when a limit is crossed.|Dialysis nurse::Is told at once of any hold, decides what happens to patients, and watches for symptoms.|Biomedical technician and suppliers::Maintain and repair equipment and confirm it is fit to return to service.}}
<p>Philippine dialysis facilities are licensed by the Department of Health, and water quality is part of what is inspected.[[doh2012]][[doh_water]] As a technician you do not decide whether patients are dialyzed. You make sure the people who decide have the facts in time.</p>
{{stop:If you think the water may be unsafe, say so before patients are connected. A delayed shift is an inconvenience. Contaminated water reaches every chair at once.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> A higher disinfectant dose means more chlorine and chloramine in the feed water, and the carbon tanks are the stage that removes them. A normal reverse osmosis reading says nothing about chlorine. Before the first patient is connected, test total chlorine after the carbon tanks, check the sediment filter pressures because the water is cloudy, and tell the charge nurse what the utility announced and what you found. If the result is above the unit&rsquo;s limit, treatments do not start until an authorized person releases the water. Record the announcement, the result, the time, and who was told.</p>
"""],
    "skills": {
        "title": "Tracing the system and explaining the risks",
        "intro": "Materials: the system drawing, the unit&rsquo;s list of limits, and the water room itself.",
        "items": [("Traces the water path from the feed line to the loop return on the drawing and in the room.", False),
                  ("Names what each stage removes.", False),
                  ("States the unit&rsquo;s limit and action level for total chlorine, bacteria, and endotoxin.", True),
                  ("Explains why a normal reverse osmosis reading does not prove the absence of chlorine.", True),
                  ("Identifies who must be told when water quality is in doubt, and how to reach them.", True),
                  ("Locates the written procedures and the log for the water system.", False)],
        "placement": "With your preceptor, find out where your unit&rsquo;s feed water comes from and how the unit learns about changes made by the supplier.",
    },
    "quiz": [
        ("Why must dialysis water be cleaner than drinking water?",
         ["Dialysis patients drink more water", "Contaminants cross the dialyzer membrane directly into the blood, in very large weekly volumes", "Dialysis machines rust easily", "Drinking water is not disinfected"], 1,
         "The gut protects a person who drinks water. In dialysis, hundreds of liters a week are separated from blood only by a membrane."),
        ("Which contaminant destroys red blood cells and is removed mainly by carbon tanks?",
         ["Calcium", "Endotoxin", "Chloramine", "Sodium"], 2,
         "Chloramine and chlorine cause hemolysis. Activated carbon is the barrier against them."),
        ("What is endotoxin?",
         ["A live bacterium", "A fragment of dead bacteria that can cause fever and chills", "A disinfectant", "A mineral that causes scale"], 1,
         "Endotoxin comes from the cell wall of certain bacteria and can cause reactions even when no live bacteria are found."),
        ("In the international standard, what is the maximum total chlorine in dialysis water?",
         ["0.1 mg/L", "1 mg/L", "4 mg/L", "10 mg/L"], 0,
         "The limit is 0.1 mg/L, far below the level in tap water."),
        ("Which fluid has the strictest limits for bacteria and endotoxin?",
         ["Feed water", "Dialysis water", "Standard dialysis fluid", "Ultrapure dialysis fluid"], 3,
         "Ultrapure fluid has limits of less than 0.1 CFU/mL and less than 0.03 EU/mL."),
        ("What is an action level?",
         ["The maximum allowed result", "A result below the maximum at which the unit must already act", "The result at which patients are sent home", "A target set by the water utility"], 1,
         "Acting at the action level keeps results from ever reaching the limit."),
        ("The utility announces a higher disinfectant dose. The reverse osmosis display is normal. What should you do first?",
         ["Nothing; the display is normal", "Test total chlorine after the carbon tanks and inform the nurse", "Add more salt to the softener", "Switch off the carbon tanks"], 1,
         "The reverse osmosis display does not measure chlorine. Test where chlorine is removed and tell the nurse before patients are connected."),
        ("Who carries overall responsibility for dialysis water quality in a facility?",
         ["The water utility", "The equipment supplier", "The medical director", "The newest technician"], 2,
         "The medical director is responsible. The technician&rsquo;s duty is to test, record, stop, and report."),
    ],
    "terms": [("Feed water", "Water entering the treatment system from the city supply, a well, or a tanker."),
              ("Hemolysis", "Red blood cells breaking apart."),
              ("Colony-forming unit", "One bacterium, or clump of bacteria, that grows into a visible colony on a culture plate."),
              ("Hardness", "Dissolved calcium and magnesium in water.")],
    "readings": [("dialysis-water-treatment-systems.html", "The full reference, including the chemical limits table."),
                 ("hemodiafiltration-deep-dive.html", "Why newer therapies need ultrapure fluid.")],
}
