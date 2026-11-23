# -*- coding: utf-8 -*-
"""Water Treatment track, 12-module edition: new content for Modules 7 to 12. See deep_a.py for the format."""

NEW = {}

NEW["07"] = {
    "image_alt": "A technician reading a concentrate container label against an order sheet.",
    "objectives": [
        "Explain what acid and bicarbonate concentrates contribute to dialysate and why they must match the machine.",
        "Mix, label, verify, and discard bicarbonate concentrate by procedure.",
        "Describe a central concentrate delivery system and the safeguards against mix-ups.",
        "Keep the bicarbonate system clean and recognize contamination.",
    ],
    "big": """
{{plain:Think of a carinderia that makes its own iced tea. The water comes from a clean filter, but the drink the customer tastes depends on which powder was scooped in, and how much. If two powders sit in identical tubs, the cook can pick up the wrong one and the drink will still look the same in the glass.}}
<p>The picture has a limit. A wrong iced tea only tastes wrong. Clean water is only half of dialysate. The other half is two concentrates that the machine dilutes with water: an acid concentrate carrying most of the salts, and a bicarbonate concentrate carrying the buffer. The patient&rsquo;s blood moves toward whatever the dialysate contains, so a mistake here is a medication error. In many units the water technician mixes and distributes these concentrates, and that is why the work belongs in this track.</p>
{{cards:Key terms for this module|Acid concentrate::The concentrate holding sodium, potassium, calcium, magnesium, chloride, a small amount of acid, and usually glucose.|Bicarbonate concentrate::The concentrate holding sodium bicarbonate, the buffer that corrects acid in the blood.|Proportioning ratio::The fixed proportions in which a machine mixes acid concentrate, bicarbonate concentrate, and water.|Batch::One mixed quantity, with its own label and record.|Central delivery::Tanks and pipes that carry concentrate to wall outlets at each station.|Use time::How long a mixed concentrate may be kept before it is discarded.}}
""",
    "case": {"title": "Two acid formulas on one shelf", "html": """
<p>The unit stocks two acid concentrates from the same supplier, in identical white containers. They differ only in one number on the label: one gives a dialysate potassium of 2, the other 3. On a busy Tuesday morning a new aide, Mr. Kevin Manalo, 22, restocks the store, and containers of both kinds end up in one row.</p>
<p>At 09:30 the nurse, Ms. Aileen Torres, checks the container at station 5 against the order for her patient, Mrs. Felicidad Ocampo, 70. It does not match. The machine&rsquo;s conductivity has been normal the whole time, and no alarm has sounded. She calls you to the station.</p>
""", "questions": ["Why did the machine not alarm?",
                  "What should happen at station 5, and whose decision is it?",
                  "What would make this mistake harder to repeat, and what do you report?"]},
    "sections": [
        ("two", "Two concentrates", "What each concentrate does", """
<p>Why two concentrates instead of one? If all the salts were put into one concentrate with bicarbonate, calcium and magnesium would react with the bicarbonate and form a solid, like the white scale inside a kettle. So the ingredients are kept apart until the last moment, when the machine mixes them into a large volume of water.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Acid concentrate</th><th>Bicarbonate concentrate</th></tr></thead>
<tbody>
<tr><td>Contains</td><td>Sodium, potassium, calcium, magnesium, chloride, a small amount of acetic or citric acid, usually glucose</td><td>Sodium bicarbonate, sometimes with sodium chloride</td></tr>
<tr><td>Varies between patients</td><td>Yes: potassium and calcium come in several formulas</td><td>Usually one formula; the machine can vary the amount delivered</td></tr>
<tr><td>Supports bacterial growth</td><td>No; it is too acidic and salty</td><td>Yes, readily, once mixed with water</td></tr>
<tr><td>Supplied as</td><td>Ready-made liquid in containers or bulk; or powder mixed on site</td><td>Powder cartridges on the machine; or powder mixed with dialysis water on site; or ready-made liquid</td></tr>
<tr><td>Main risk</td><td>Wrong formula connected</td><td>Contamination; loss of strength if kept too long or mixed too hard</td></tr>
</tbody></table></div>
<p>Machines mix the two concentrates and water in a fixed proportion, and several different proportioning systems are in use worldwide. Each concentrate is made for one system only, and that system is stated on the label. A concentrate made for a different system will give the wrong dialysate, even though each container is correct on its own. The biomedical technician configures the machine. Your part is to make sure that only matching concentrates reach it.[[iso23500_5]]</p>
{{key:Conductivity measures the total amount of salt. Two acid formulas with different potassium give almost the same conductivity, so the machine cannot tell them apart. The label is the only safeguard.}}
"""),
        ("labels", "Labels and storage", "Reading labels and organizing the store", """
<div class="table-wrap"><table>
<thead><tr><th>On the label</th><th>Why you check it</th></tr></thead>
<tbody>
<tr><td>Product type: acid or bicarbonate</td><td>The two connect to different ports</td></tr>
<tr><td>Formula: potassium and calcium levels</td><td>It must match the physician&rsquo;s order for that patient</td></tr>
<tr><td>Proportioning system</td><td>It must match the machines in your unit</td></tr>
<tr><td>Lot number and expiry date</td><td>So a recalled batch can be traced; expired product is never used</td></tr>
<tr><td>Seal and container condition</td><td>A broken seal or a damaged container is rejected</td></tr>
</tbody></table></div>
{{cards:A store that prevents mix-ups|One formula per shelf::With a large shelf label showing the potassium and calcium.|Color or tag coding::A unit-wide code for each formula, applied on receipt.|Look-alikes apart::Never side by side.|First in, first out::Oldest stock at the front.|Trained restocking::Only staff who know the formulas put stock away.|Quarantine area::For damaged, expired, or unidentified containers.}}
<p>Mix-ups happen in the store long before they happen at the station, so the store is where you prevent them. By international convention, acid concentrate connectors and containers are marked red and bicarbonate blue, and the connectors are shaped so that one will not fit the other&rsquo;s port. Treat any connector that has been forced or modified as a hazard, and report it.</p>
"""),
        ("bicarb", "Mixing bicarbonate", "Mixing bicarbonate from powder", """
{{flow:Preparing a batch|Prepare::Clean hands and clean gloves. Use a container or mixer that has been cleaned and disinfected by procedure.|Water::Add dialysis water to the mark. Never tap water.|Powder::Add the whole contents of the stated number of bags. Check the lot and expiry first.|Mix::Mix gently until fully dissolved. Do not whip air into it.|Verify::Test the batch by the unit&rsquo;s method.|Label::Write the contents, date and time mixed, discard time, lot numbers, and your name.|Record::Enter the batch in the log.}}
<div class="table-wrap"><table>
<thead><tr><th>Mistake</th><th>What it causes</th></tr></thead>
<tbody>
<tr><td>Mixing too hard or for too long</td><td>Carbon dioxide escapes, the solution becomes more alkaline, and it may behave wrongly in the machine</td></tr>
<tr><td>Wrong amount of water or powder</td><td>A concentrate that is too strong or too weak; conductivity alarms at every machine</td></tr>
<tr><td>Powder not fully dissolved</td><td>A weak concentrate at first and a strong one later; blocked pick-up filters</td></tr>
<tr><td>Topping up an old batch with new</td><td>Bacteria from the old batch seed the new one</td></tr>
<tr><td>Keeping a batch past its use time</td><td>Bacteria grow and the concentrate loses strength</td></tr>
<tr><td>A dirty container, or the lid left off</td><td>Contamination</td></tr>
</tbody></table></div>
<p>Bicarbonate in water behaves differently from the acid concentrate. Once it is mixed with water, bacteria grow in it readily, and it gives up carbon dioxide if it is mixed too hard. Both facts shape the rules below.</p>
<p>Verify each batch before you release it. Units use conductivity, a density check, or pH, as the concentrate manufacturer advises. The acceptable range is in the manufacturer&rsquo;s instructions and in your procedure. A batch outside the range is discarded. It is not corrected by adding a bit more powder or water, because you no longer know what is in the container.</p>
<p>The use time for mixed bicarbonate is set by the manufacturer and is short, commonly within a day. Write the discard time on the label when you mix. Empty, rinse, and disinfect the container at the frequency your procedure states.</p>
{{stop:Never add fresh bicarbonate to a container that still holds old solution, and never use a batch with no label.}}
"""),
        ("central", "Central delivery", "Central concentrate systems", """
<p>Larger units pipe concentrates from tanks to wall outlets at each station. This removes heavy lifting and the handling of single containers. It also means that one error in the tank reaches every station at the same moment, so the safeguards move from the station to the tank room.</p>
{{cards:Safeguards in a central system|Separate tanks and lines::Acid and bicarbonate never share pipework.|One formula per acid line::Each line and each outlet is labeled with its formula.|Different connectors::Acid and bicarbonate outlets do not accept each other&rsquo;s hoses.|Filling controls::Trained staff fill the tanks, with a second person checking the product against the tank label.|Level and low alarms::So that a tank does not run dry in the middle of a shift.|Scheduled disinfection::The bicarbonate tank and loop are disinfected and rinsed on a schedule; acid lines are not disinfected with bleach.}}
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>How it shows</th><th>First response</th></tr></thead>
<tbody>
<tr><td>Acid tank filled with the wrong formula</td><td>Usually nothing at all on the machines</td><td>Stop use of that line and tell the charge nurse immediately; the clinical team reviews the patients</td></tr>
<tr><td>Bicarbonate tank running low or drawing air</td><td>Low conductivity alarms on several machines at once</td><td>Check the tank level and the pick-up; tell the nurse the cause</td></tr>
<tr><td>Bicarbonate batch too weak or too strong</td><td>Conductivity alarms across the unit soon after a new batch goes on line</td><td>Take the batch off line, verify it, and discard it if out of range</td></tr>
<tr><td>Contaminated bicarbonate system</td><td>High cultures in dialysis fluid from several machines; slime or cloudiness in the tank; possibly reactions in patients</td><td>Report; disinfect the tank and lines; review the cleaning frequency</td></tr>
<tr><td>White crystals at outlets and connectors</td><td>Dried bicarbonate</td><td>Clean them off; check for leaks; crystals can block connectors</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Why the machine did not alarm.</strong> Conductivity reflects the total salt content, and the two formulas differ by a very small amount of potassium. The machine read both as normal. Only the label tells them apart.</p>
<p><strong>What should happen at station 5, and whose decision it is.</strong> Ms. Torres and the physician decide what to do for Mrs. Ocampo. Your part is to state exactly which product was connected and from what time, and to keep the container so it can be checked. Then check every other station and the store, because the same row supplied them.</p>
<p><strong>What makes a repeat harder, and what to report.</strong> Separate shelves with large formula labels; a color tag applied to each container on receipt; restocking only by trained staff; look-alike products never in the same row; and a second check of the container against the order at setup. Report the event as an incident even if Mrs. Ocampo is well. The cause is in the store, not in the person at station 5, and only a report will change the store.</p>
"""],
    "skills": {"title": "Mixing, labeling, and verifying a bicarbonate batch",
        "intro": "Materials: bicarbonate powder, a cleaned mixing container, dialysis water, the unit&rsquo;s verification instrument, labels, and the batch log.",
        "items": [("Confirms the container has been cleaned and disinfected by procedure and holds no old solution.", True),
                  ("Uses dialysis water and fills to the correct mark.", True),
                  ("Checks powder type, lot, and expiry and adds the stated quantity.", False),
                  ("Mixes gently until dissolved without over-mixing.", False),
                  ("Verifies the batch by the unit&rsquo;s method and states the acceptable range.", True),
                  ("Labels with contents, time mixed, discard time, lot numbers, and name.", True),
                  ("Records the batch in the log.", False),
                  ("Reads an acid concentrate label and states formula, proportioning system, lot, and expiry.", False),
                  ("States the action for a batch that fails verification.", True)],
        "placement": "Audit the concentrate store with your preceptor: look for look-alike products stored together, expired stock, and unlabeled containers."},
    "quiz": [
        ("Why are acid and bicarbonate supplied as two separate concentrates?",
         ["To save money", "Calcium and magnesium would react with bicarbonate and form a solid if stored together", "To make mixing harder", "They have different colors"], 1,
         "Keeping them apart until dilution prevents precipitation."),
        ("Two acid concentrates differ only in potassium. Will the machine&rsquo;s conductivity alarm tell them apart?",
         ["Yes, always", "No; conductivity is nearly the same", "Only at night", "Only with bicarbonate off"], 1,
         "Conductivity measures total salts; the label is the safeguard."),
        ("Which water is used to mix bicarbonate concentrate?",
         ["Tap water", "Dialysis water", "Softened water only", "Drinking water from a dispenser"], 1,
         "Only treated dialysis water is used."),
        ("Why should bicarbonate not be mixed vigorously for a long time?",
         ["It foams over", "Carbon dioxide is lost and the solution changes", "It becomes acidic", "It hardens"], 1,
         "Over-mixing drives off carbon dioxide and makes the solution more alkaline."),
        ("A bicarbonate container is half full of yesterday&rsquo;s batch. What is correct?",
         ["Top it up with fresh solution", "Discard, clean and disinfect the container, then prepare a fresh batch", "Use it first", "Add more powder"], 1,
         "Old solution seeds bacteria into the new batch and is past its use time."),
        ("Low conductivity alarms occur on six machines at once shortly after a new bicarbonate batch goes on line. What is the likely cause?",
         ["Six faulty machines", "The batch, or the supply running low or drawing air", "Hard water", "Cold weather"], 1,
         "Simultaneous alarms point to the shared supply."),
        ("By convention, which color marks acid concentrate connectors?",
         ["Blue", "Red", "Green", "Yellow"], 1, "Acid is red and bicarbonate is blue."),
        ("A mixed batch fails verification. What do you do?",
         ["Adjust it with more powder", "Discard it and prepare a new batch", "Use it on one machine", "Dilute it at the station"], 1,
         "An out-of-range batch is discarded, not corrected."),
    ],
    "terms": [("Buffer", "A substance that neutralizes acid. In dialysate the buffer is bicarbonate."),
              ("Precipitate", "A solid that forms and settles out of a liquid."),
              ("Lot number", "The manufacturer&rsquo;s code identifying one production batch."),
              ("Density check", "Measuring how heavy a liquid is for its volume, as a check on how strong it is.")],
    "readings": [("dialysis-prescription.html", "Why dialysate potassium, calcium, and bicarbonate are prescribed individually."),
                 ("dialysis-water-treatment-systems.html", "Fluid quality from water to dialysate.")],
}

NEW["08"] = {
    "image_alt": "A technician writing readings on a water room log sheet beside a gauge panel.",
    "objectives": [
        "Carry out the start-of-day round in order and release the system to the charge nurse.",
        "State what each daily check proves and what it cannot prove.",
        "Keep records that another person can rely on.",
        "Establish each reading&rsquo;s normal range for your system and report drift before a limit is reached.",
    ],
    "big": """
{{plain:Think of the vital signs a ward nurse takes every morning. One blood pressure, read alone, says little. Written on the same chart day after day, beside yesterday&rsquo;s value, it shows whether the patient is getting better or worse long before anyone is in danger.}}
<p>The picture has a limit. A ward patient has a doctor who reads the chart on rounds. A water log has no one unless the unit decides who that will be. The earlier modules explained each stage. This one ties them into a single daily routine, the records that prove it was done, and the review that makes the records useful. The round takes about twenty minutes. Done properly, it is the cheapest safety measure in the unit.</p>
{{flow:The start-of-day round|System on and stable::Let it run for the time your procedure states.|Chlorine::Test total chlorine after the carbon tanks before the first patient.|Pretreatment::Read the filter pressures, the softener and backwash clocks, and the salt.|Reverse osmosis::Record pressures, flows, conductivities, temperature, and rejection.|Loop::Record supply and return pressures; check the lamp and filter status.|Concentrates::Confirm the batches are in date and the tanks are at level.|Sign and release::Record every number, sign, and tell the nurse the water is released.}}
{{cards:Key terms for this module|Baseline::The usual value of a reading on your system when it is healthy.|Normal range::The band around the baseline that needs no action.|Trend::The direction readings are moving over days or weeks.|Release::The recorded statement that today&rsquo;s checks passed.|Second review::A weekly look at the log by someone other than the person who filled it in.}}
""",
    "case": {"title": "The log nobody reviewed", "html": """
<p>Mr. Romeo Garcia, 45, has been the unit&rsquo;s only water technician for three years. His log is complete and neatly signed. For six weeks it shows the pressure drop across the fine filter rising from 3 to 14 psi, and the reverse osmosis product flow falling by a fifth. Every entry is a real number, correctly recorded. Nobody acted on any of them.</p>
<p>On the seventh Monday, at 06:00, the machines alarm for low water pressure as the first shift begins. The charge nurse, Ms. Nenita Bautista, holds the patients in the waiting area. The first shift starts two hours late.</p>
""", "questions": ["Was the recording at fault?",
                  "What was missing from the routine, and what would have shown the problem early?",
                  "What would you add so this cannot happen again?"]},
    "sections": [("L", "04", "checks"),
        ("baseline", "Your normal ranges", "Finding your system&rsquo;s normal ranges", """
<p>A reading means something only when you know what is normal for your own system. The manual gives the design values. Your log gives the real ones, because every system sits on its own feed water, its own pipe lengths, and its own temperature. For each reading, the unit should have a written baseline, a normal range, and an action point, approved by the person responsible for the system.</p>
<div class="table-wrap"><table>
<thead><tr><th>Reading</th><th>Where the baseline comes from</th><th>A sensible action point</th></tr></thead>
<tbody>
<tr><td>Pressure drop across each filter</td><td>The value just after a new cartridge or a good backwash</td><td>The manufacturer&rsquo;s change-out figure, or an agreed rise above the clean value</td></tr>
<tr><td>Hardness after the softener</td><td>The result just after a good regeneration</td><td>The unit&rsquo;s hardness limit</td></tr>
<tr><td>Total chlorine after each tank</td><td>Undetectable when the carbon is healthy</td><td>Any detectable result after the worker is reported; the limit applies after the polisher</td></tr>
<tr><td>Percent rejection</td><td>The value with a new or freshly cleaned membrane</td><td>An agreed fall below baseline, well before the alarm</td></tr>
<tr><td>Product flow</td><td>The value at a stated temperature</td><td>An agreed fall at a similar temperature</td></tr>
<tr><td>Loop return pressure</td><td>The typical value at shift start and at idle</td><td>A fall that does not recover</td></tr>
</tbody></table></div>
{{key:Print the baseline, normal range, and action point at the top of each column of the log sheet. A number is far easier to judge when its reference sits beside it.}}
"""),
        ("L", "04", "records"),
        ("L", "04", "trends"),
        ("review", "Review", "Weekly and monthly review", """
<p>Recording is half of monitoring. The other half is someone looking at the record with fresh eyes. The person who writes the same column every morning stops seeing a slow change, because each day looks almost like the one before. A second reader sees the whole week at once.</p>
{{cards:A review routine that works|Daily::The technician compares today with yesterday before signing.|Weekly::A second person reads the week&rsquo;s log and looks for drift, gaps, and identical numbers.|Monthly::The main readings are charted and taken to the unit&rsquo;s quality meeting with the culture and endotoxin results.|After any incident::The log from before the event is reviewed for warnings that were missed.}}
<div class="table-wrap"><table>
<thead><tr><th>What the reviewer looks for</th><th>What it suggests</th></tr></thead>
<tbody>
<tr><td>A reading moving the same way for a week or more</td><td>A problem is developing</td></tr>
<tr><td>Identical readings day after day</td><td>Entries were copied, or a gauge is stuck</td></tr>
<tr><td>Blanks, ticks, or &ldquo;OK&rdquo;</td><td>Checks were not done, or not recorded</td></tr>
<tr><td>Out-of-range entries with no note of action</td><td>Reporting broke down</td></tr>
<tr><td>Tests done at odd times</td><td>Shifts started before the checks were complete</td></tr>
</tbody></table></div>
{{fig:pdsa}}
<p>Release is the last step of the round. Say it in words to the charge nurse, &ldquo;water checks complete and within limits; system released,&rdquo; and sign it. If something is outside limits, say that instead, and say exactly what is on hold. The nurse should never have to guess whether the water is ready.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Was the recording at fault?</strong> No. Mr. Garcia&rsquo;s recording was excellent. Every number was real, and every number was written down.</p>
<p><strong>What was missing.</strong> Review and a defined action point. He wrote each number without a baseline beside it to compare against, and nobody else read the log. A rise from 3 to 14 psi, seen one day at a time, never looked like an event. Seen as a column, it was obvious.</p>
<p><strong>What to add.</strong> Three things: baselines and action points printed on the sheet, a weekly second review that is itself signed, and a monthly chart for the quality meeting. With those in place, the rising pressure drop would have triggered a cartridge change in week two, and the falling product flow would have prompted a look upstream. Good records that nobody reads protect no one.</p>
"""],
    "skills": {"title": "Start-of-day round and release",
        "intro": "Materials: the log sheet with baselines and action points, test kits, and the system itself.",
        "items": [("Allows the system to reach steady running before testing.", False),
                  ("Performs the total chlorine test correctly at the correct port.", True),
                  ("Records pretreatment readings and checks timers and salt.", False),
                  ("Records reverse osmosis readings and calculates rejection.", False),
                  ("Records loop readings and checks lamp and filter status.", False),
                  ("Checks concentrate batches and tank levels.", False),
                  ("Compares each reading with its baseline and action point and reports any drift.", True),
                  ("Enters numbers with units, time, and name, with no blanks.", True),
                  ("States the release to the charge nurse in words and signs it.", True)],
        "placement": "Carry out the weekly second review of another technician&rsquo;s log under supervision and list what you found."},
    "quiz_keep": [("04", [4, 5, 6, 7])],
    "quiz": [
        ("What is a baseline?",
         ["The legal limit", "The usual value of a reading when the system is healthy", "The alarm setting", "Yesterday&rsquo;s reading"], 1,
         "Baselines come from your own system in good condition."),
        ("A log shows the same pressure reading to the decimal for three weeks. What does this most likely indicate?",
         ["A very stable system", "Copied entries or a stuck gauge", "A new filter", "Cold weather"], 1,
         "Real systems vary slightly day to day."),
        ("Who should carry out the weekly log review?",
         ["The same technician who filled it in", "A second person", "Nobody", "The patient"], 1,
         "Fresh eyes catch drift the daily recorder has stopped seeing."),
        ("What is the last step of the start-of-day round?",
         ["Backwashing the filter", "Telling the charge nurse the system is released, and signing", "Changing the carbon", "Calling the supplier"], 1,
         "Release is a stated, recorded handover."),
    ],
    "terms": [("Action point", "A value agreed in advance at which something must be done."),
              ("Run chart", "A simple graph of one reading over time."),
              ("Steady running", "The state after start-up, once the readings have stopped changing.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Run charts and quality review."),
                 ("dialysis-water-treatment-systems.html", "Monitoring schedules.")],
    "calcs": ["calc-dialysis-qapi-scorecard.html"],
}

NEW["09"] = {
    "image_alt": "Gloved hands collecting water from a sample port into a sterile container.",
    "objectives": [
        "Explain what chemical analysis, culture, and endotoxin testing each measure and when each is done.",
        "State the limits and action levels your unit works to.",
        "Collect, label, store, and send samples so that results can be trusted.",
        "Read a laboratory report and respond correctly to each kind of result.",
    ],
    "big": """
{{plain:Think of a blood test at a clinic. The nurse draws one tube, and the doctor may make decisions on that result for months. If the tube is mislabeled, left in a hot car, or sent to a laboratory that runs the wrong test, the patient has given blood for nothing, and nobody may notice that the answer is wrong.}}
<p>The picture has a limit. A patient can come back tomorrow for a repeat. A water sample is usually taken once a month, so a careless sample wastes a whole month of protection. Some contaminants cannot be tested for in the water room at all. Metals and other chemicals need a laboratory, and bacteria need days to grow on a plate. Your work in this module is to get a true answer from the laboratory and to know what to do with it.</p>
{{cards:Key terms for this module|Chemical analysis::A laboratory test for a list of metals and other chemicals.|Culture::Growing bacteria from a sample so they can be counted.|Endotoxin test::A laboratory test for fragments of bacterial cell walls.|Action level::A result below the limit at which the unit must already take action.|Aseptic technique::Working so that you add no germs to the sample.|Chain of custody::The record of who handled a sample and when.}}
""",
    "case": {"title": "A high count from one port", "html": """
<p>It is Friday afternoon. The water technician, Ms. Jessa Mendoza, 31, opens the monthly laboratory report. It shows 280 CFU/mL at the mid-loop sample port. The loop start and the loop return, collected by her on the same morning, are both under 10. Last month all three points were under 10.</p>
<p>She walks to the mid-loop port. Its cap is cracked, and it sits behind a treatment chair where it is often bumped when the chair is moved.</p>
""", "questions": ["Is a true loop count of 280 likely, given the other two results?",
                  "Can you set the result aside?",
                  "What do you do and report this week?"]},
    "sections": [
        ("three", "Three kinds of test", "Three kinds of laboratory test", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Chemical analysis</th><th>Bacterial culture</th><th>Endotoxin test</th></tr></thead>
<tbody>
<tr><td>Looks for</td><td>Aluminum, fluoride, nitrate, sulfate, calcium, magnesium, sodium, potassium, heavy metals, and others on the standard&rsquo;s list</td><td>Live bacteria that can grow on a plate</td><td>Fragments of bacterial cell walls, from live or dead bacteria</td></tr>
<tr><td>Usual frequency</td><td>At validation, then at least yearly, and after a change of source or membrane</td><td>Commonly monthly; more often after a high result or a system change</td><td>Commonly monthly, with the cultures</td></tr>
<tr><td>Sample taken from</td><td>Product water, after the reverse osmosis unit</td><td>Loop start, loop return, tank outlet, and machines in rotation</td><td>The same points as cultures</td></tr>
<tr><td>Result arrives in</td><td>Days to weeks</td><td>About a week</td><td>Hours to days</td></tr>
<tr><td>Container</td><td>As the laboratory supplies; metals need special bottles</td><td>Sterile</td><td>Sterile and endotoxin-free</td></tr>
</tbody></table></div>
<p>Each test answers a different question, which is why none can replace another. A clean culture does not rule out endotoxin, because endotoxin comes from dead bacteria as well as live ones. A clean chemical analysis says nothing about bacteria.</p>
<p>Frequencies are set by the unit&rsquo;s monitoring plan and the regulations it follows.[[iso23500_1]][[doh_water]] The plan lists every sample point, how often each is sampled, and who reviews the results. If your unit has no written plan, raise it with the medical director.</p>
"""),
        ("L", "05", "limits"),
        ("L", "05", "sampling"),
        ("points", "Where and when", "Choosing sample points and timing", """
{{cards:Where to sample, and why|Loop start::Shows what the reverse osmosis unit and any tank deliver.|Loop return::Shows the worst the loop does; it usually has the highest count.|Storage tank outlet::If there is a tank, sample it directly.|Machines in rotation::Dialysis fluid from a different set of machines each month, so that every machine is covered over time.|Bicarbonate system::Where concentrate is mixed or distributed centrally.|After any repair::The repaired section, before release.}}
<p>Timing matters as much as place. Collect samples before a scheduled disinfection, not after it, and at a time when the system is running normally. A sample taken the morning after disinfection will look excellent. It will tell you nothing about what patients were exposed to the day before.</p>
<div class="table-wrap"><table>
<thead><tr><th>Handling step</th><th>Rule</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Labeling</td><td>Before filling: point, date, time, and name</td><td>Unlabeled samples get mixed up</td></tr>
<tr><td>Storage</td><td>Refrigerated, not frozen</td><td>Warmth lets bacteria multiply; freezing kills them</td></tr>
<tr><td>Transport time</td><td>Within the laboratory&rsquo;s stated window, commonly 24 hours</td><td>The longer a sample waits, the further its result drifts</td></tr>
<tr><td>Request form</td><td>States that the sample is dialysis water, and names the method required</td><td>A general hospital method undercounts water bacteria</td></tr>
<tr><td>Record</td><td>Who collected it, who received it, and when</td><td>So that a strange result can be traced</td></tr>
</tbody></table></div>
<p>Water bacteria grow slowly and prefer poor conditions, because they live in water with almost no food in it. The standard therefore calls for low-nutrient culture media incubated at room temperature for about seven days. A laboratory that uses a blood-culture method at body temperature for two days will report falsely low counts. Ask your laboratory which method it uses.[[iso23500_3]]</p>
"""),
        ("results", "Reading results", "Reading the report and responding", """
<div class="table-wrap"><table>
<thead><tr><th>Result</th><th>What it means</th><th>Response</th></tr></thead>
<tbody>
<tr><td>Below the action level at all points</td><td>The system is under control</td><td>File it, chart it, and continue the schedule</td></tr>
<tr><td>Rising month to month but below the action level</td><td>Biofilm is developing</td><td>Report the trend; consider bringing disinfection forward; look for dead legs</td></tr>
<tr><td>At or above the action level, below the limit</td><td>Act now, while there is a margin</td><td>Report to the medical director; disinfect; resample; investigate the cause</td></tr>
<tr><td>Above the limit</td><td>The water or fluid is out of specification</td><td>Report immediately; the medical director decides about treatment; disinfect, find the cause, and resample until the results are acceptable</td></tr>
<tr><td>One point high, its neighbors low</td><td>Possibly a contaminated sample or port</td><td>Report; resample that point promptly with careful technique; inspect the port; do not dismiss it without a repeat</td></tr>
<tr><td>Endotoxin high, culture low</td><td>Dead bacteria or their fragments; biofilm upstream, or a recent disinfection</td><td>Treat it as a real finding; check the ultrafilters and the upstream stages</td></tr>
<tr><td>A chemical above its limit</td><td>The membrane or a pretreatment stage is not removing it, or the source has changed</td><td>Report immediately; review rejection, the feed water, and recent changes</td></tr>
</tbody></table></div>
{{key:Every laboratory report is read, signed, and dated by a named person on the day it arrives. A report filed unread is the same as no test at all.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is a true loop count of 280 likely?</strong> No. Water that reads under 10 at the start of the loop and under 10 at the return, on the same morning, is unlikely to carry 280 in between. A cracked cap on a port that is often bumped makes contamination of the sample, or of the port itself, the probable explanation.</p>
<p><strong>Can you set the result aside?</strong> No. A dirty port is still part of the loop, and it can seed the water that flows past it. A probable explanation is not yet a proven one.</p>
<p><strong>What to do and report this week.</strong> Report the result and your reasoning to the chief technician and the medical director. Replace the cap, and clean and disinfect the port by procedure. Resample all three points with careful technique. Move or guard the port so it is not bumped again. If the repeat is clean, Ms. Mendoza records the investigation and closes it. If it is high again, treat it as a real loop problem and disinfect.</p>
"""],
    "skills": ("L", "05"),
    "quiz_keep": [("05", [1, 2, 3, 4])],
    "quiz": [
        ("How often is chemical analysis of product water done, at a minimum, in most monitoring plans?",
         ["Daily", "At least yearly, and after a change of source or membrane", "Never", "Every shift"], 1,
         "Chemical contaminants change slowly, but any change of source or membrane calls for a new analysis."),
        ("A laboratory cultures dialysis water at body temperature for 48 hours. What is the likely effect?",
         ["Falsely high counts", "Falsely low counts", "No effect", "Faster endotoxin results"], 1,
         "Water bacteria grow slowly and need low-nutrient media at room temperature for about a week."),
        ("Endotoxin is high but the culture is low. How should this be treated?",
         ["As a laboratory error", "As a real finding needing investigation", "As good news", "As a reason to stop endotoxin testing"], 1,
         "Endotoxin comes from dead as well as live bacteria."),
        ("How should culture samples be stored before transport?",
         ["Frozen", "Refrigerated", "In a warm car", "In direct sunlight"], 1,
         "Refrigeration holds the count steady; warmth raises it and freezing lowers it."),
    ],
    "terms": [("Monitoring plan", "The unit&rsquo;s written list of what is tested, where, how often, and who reviews it."),
              ("Low-nutrient medium", "A culture plate with little food, suited to slow-growing water bacteria."),
              ("Out of specification", "Outside the limits your unit works to.")],
    "readings": [("dialysis-water-treatment-systems.html", "Chemical limits and microbiological monitoring.")],
}

NEW["10"] = {
    "image_alt": "A technician in protective equipment hanging a disinfection sign at an empty treatment station.",
    "objectives": [
        "Explain how biofilm forms and why disinfection is scheduled before counts rise.",
        "Compare heat and chemical disinfection and prepare a correct dilution.",
        "Carry out a chemical disinfection with proof of reach, dwell, and rinse.",
        "Handle disinfectants safely and respond to a spill or exposure.",
    ],
    "big": """
{{plain:Think of the inner pot of a rice cooker. Washed after every meal, it comes clean in a minute with soap and water. Left for a week, the rice at the bottom dries into a crust that soaking and scrubbing barely move, and sometimes the pot is ruined.}}
<p>The picture has a limit. You can see the crust in a pot. You cannot see biofilm in a loop; you learn about it only from culture results, weeks after it started. Disinfection is therefore not a cure for a contaminated system. It is routine housekeeping that keeps a clean system clean. Done on schedule, it is quick and uneventful. Done late, after biofilm has matured, it may not work at all, and parts of the system may have to be replaced.</p>
{{cards:Key terms for this module|Biofilm::Bacteria attached to a surface in a protective slime.|Disinfectant::A chemical or heat treatment that kills microbes.|Dilution::Mixing a strong stock chemical with water to the working strength.|Dwell time::How long the disinfectant stays in the system.|Residual::Disinfectant remaining after the rinse.|Safety data sheet::The document listing a chemical&rsquo;s hazards and first aid.}}
""",
    "case": ("L", "05"),
    "sections": [("L", "05", "biofilm"),
        ("methods", "Methods", "Choosing and scheduling the method", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Heat</th><th>Chemical</th></tr></thead>
<tbody>
<tr><td>How it works</td><td>Hot water is circulated through the loop for a set time</td><td>A disinfectant is circulated and then left to dwell</td></tr>
<tr><td>Residue</td><td>None</td><td>It must be rinsed out and proven absent</td></tr>
<tr><td>How often it can be done</td><td>Frequently, even daily or weekly, often automatically overnight</td><td>Less often; each cycle takes the system out of use for hours</td></tr>
<tr><td>Requirements</td><td>Pipework, pumps, and fittings rated for the temperature</td><td>Compatible materials; protective equipment; test strips</td></tr>
<tr><td>Typical agents</td><td>Hot water</td><td>Peracetic acid products; bleach (sodium hypochlorite); others as the manufacturer approves</td></tr>
<tr><td>Watch out for</td><td>Scalds; sections that do not reach temperature</td><td>Membrane and metal damage from the wrong agent; residual; fumes</td></tr>
</tbody></table></div>
<p>The manufacturer&rsquo;s instructions state which method and which agents each part of the system tolerates. Bleach destroys many reverse osmosis membranes, so the membrane and the loop often have different procedures.[[iso23500_2]]</p>
<p>Set the frequency from your unit&rsquo;s own culture results: often enough that counts never approach the action level. Many units disinfect the loop monthly and adjust from there. Your culture results are the test of the schedule. If counts are rising between disinfections, either the interval is too long or something is seeding the loop.</p>
"""),
        ("dilution", "Dilution", "Working out a dilution", """
<p>Chemical disinfectants arrive as a concentrated stock. You dilute the stock to the working strength stated in the procedure. Too weak, and the disinfection fails without any sign. Too strong, and you risk damage to the system and a longer rinse. The arithmetic below is the same every time.</p>
{{formula:<strong>Stock volume needed = (working strength &times; total volume) &divide; stock strength</strong><br>Illustration: a procedure calls for 200 liters at 1 percent, and the stock is 5 percent. Stock needed = (1 &times; 200) &divide; 5 = 40 liters, made up to 200 liters with dialysis water. Use the strengths in your own procedure and on your own product label.}}
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Why</th></tr></thead>
<tbody>
<tr><td>The strength printed on the stock container</td><td>Products with the same name come in different strengths</td></tr>
<tr><td>The expiry date and storage</td><td>Disinfectants lose strength with age, heat, and light</td></tr>
<tr><td>The system volume</td><td>The loop, tank, and hoses together; this figure should be written in the procedure</td></tr>
<tr><td>A test strip for concentration</td><td>It confirms the working strength was reached at the farthest point</td></tr>
<tr><td>A separate test strip for residual</td><td>A concentration strip is not sensitive enough to prove the rinse</td></tr>
</tbody></table></div>
{{key:Use two different strips: a high-range strip to prove the disinfectant arrived at full strength, and a low-range strip to prove it has gone.}}
"""),
        ("L", "05", "disinfection"),
        ("problems", "When it goes wrong", "Troubleshooting a disinfection", """
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Likely cause</th><th>Action</th></tr></thead>
<tbody>
<tr><td>No disinfectant at the farthest point</td><td>A closed valve, an air lock, too small a dose, or a pump not running</td><td>Do not start the dwell clock; find and correct the cause; confirm at every point</td></tr>
<tr><td>Concentration low everywhere</td><td>A dilution error, expired stock, or a system volume larger than assumed</td><td>Recalculate; check the stock; add more by procedure and retest</td></tr>
<tr><td>Residual will not clear at one outlet</td><td>A dead leg or a long hose holding disinfectant</td><td>Flush that outlet longer; report the dead leg</td></tr>
<tr><td>Residual clears, then reappears</td><td>Disinfectant trapped in a tank, a filter housing, or a branch is washing out slowly</td><td>Keep rinsing; drain and rinse the tank or housing; retest every outlet</td></tr>
<tr><td>Counts back up within two weeks</td><td>Mature biofilm, or a source such as a dead leg, a tank, old hoses, or the bicarbonate system</td><td>Report; investigate the source; a different agent, repeated cycles, or replacement of parts may be needed</td></tr>
<tr><td>Strong smell, coughing, sore eyes</td><td>Poor ventilation or a spill</td><td>Leave the area, ventilate, follow the safety data sheet, and report</td></tr>
</tbody></table></div>
<p>Notice that the first row stops the clock. Dwell time counts only from the moment the disinfectant is proven at full strength at the farthest point. Time spent before that does not count, however long it was.</p>
"""),
        ("L", "06", "chemicals")],
    "debrief": ("L", "05"),
    "skills": {"title": "A documented loop disinfection",
        "intro": "Materials: the disinfection procedure, the approved disinfectant and its safety data sheet, protective equipment, concentration and residual test strips, warning signs, and the disinfection record.",
        "items": [("Confirms no patient is on dialysis, tells the charge nurse, and posts warning signs.", True),
                  ("Reads the safety data sheet and wears the stated protective equipment.", True),
                  ("Checks stock strength and expiry and calculates the dilution correctly.", True),
                  ("Doses and circulates by procedure.", False),
                  ("Proves working concentration at the farthest point before starting the dwell time.", True),
                  ("Observes the full dwell time.", False),
                  ("Rinses and obtains a negative residual test at every outlet, including unused ones.", True),
                  ("Records concentrations, times, results, and names, and releases the system in writing.", False),
                  ("States the first aid for skin and eye contact with the disinfectant in use.", True)],
        "placement": "Take part in one complete disinfection, then check the next month&rsquo;s culture results and discuss with your preceptor whether the interval is right."},
    "quiz_keep": [("05", [0, 5, 6, 7])],
    "quiz": [
        ("A procedure calls for 100 liters at 2 percent. The stock is 10 percent. How much stock is needed?",
         ["2 liters", "10 liters", "20 liters", "50 liters"], 2, "(2 &times; 100) &divide; 10 = 20 liters, made up to 100 liters."),
        ("Why are two different test strips used during chemical disinfection?",
         ["To use up stock", "One proves full strength arrived; a more sensitive one proves it has been rinsed out", "For different colors", "They are the same"], 1,
         "High-range and residual strips answer different questions."),
        ("Counts return to their old level two weeks after disinfection. What does this suggest?",
         ["Normal variation", "Mature biofilm or a source seeding the loop", "The laboratory is wrong", "The softener is exhausted"], 1,
         "Rapid regrowth means something survived or keeps reseeding."),
        ("Why might the reverse osmosis membrane and the loop have different disinfection procedures?",
         ["Tradition", "Some agents that suit the loop, such as bleach, damage many membranes", "The membrane needs no disinfection", "The loop cannot be disinfected"], 1,
         "Agent compatibility differs between components."),
    ],
    "terms": [("Stock solution", "The concentrated chemical as supplied."), ("Working strength", "The diluted strength used in the system."),
              ("Air lock", "Trapped air that stops liquid from reaching part of a pipe or branch."),
              ("Peracetic acid", "A widely used disinfectant for dialysis water systems.")],
    "readings": [("dialysis-water-treatment-systems.html", "Disinfection strategies in full.")],
}

NEW["11"] = {
    "image_alt": "A technician fitting a new filter cartridge into a housing.",
    "objectives": [
        "Describe the scheduled maintenance of each component and what triggers unscheduled replacement.",
        "State the checks required after each kind of component change before the system is released.",
        "Supervise and document a supplier service visit.",
        "Maintain the system file and the instruments used to test the water.",
    ],
    "big": """
{{plain:Think of a car fresh from the vulcanizing shop with a new tire. The tire itself is fine. The risk is in what the mechanic touched: a lug nut left loose, a jack still under the frame. A careful driver walks around the car and checks before he takes it onto the highway.}}
<p>The picture has a limit. A loose lug nut can be seen. A carbon tank still shedding fines, or a bypass valve left half open, looks normal from the outside. Every part of the water system wears out: cartridges plug, carbon is exhausted, resin tires, membranes foul, lamps dim. Replacing them on time is ordinary work. The risk lies in the hours afterward, when something new has been fitted, valves have been moved, and the system has not yet been proven. This module is about changing things safely.</p>
{{cards:Key terms for this module|Scheduled maintenance::Work done at set intervals whether or not there is a fault.|Trigger::A reading that calls for replacement before the scheduled date.|Post-change check::A test that proves the system is safe after a component was changed.|System file::The complete record of the system: drawings, manuals, results, service reports.|Calibration::Checking an instrument against a known standard.|Spare parts list::The items the unit keeps in stock so a failure does not stop treatment.}}
""",
    "case": {"title": "New carbon, cloudy water", "html": """
<p>A supplier&rsquo;s engineer replaces both carbon tanks on a Sunday, when the unit is closed. He leaves a one-line report: &ldquo;Carbon changed. OK.&rdquo;</p>
<p>On Monday at 05:15, the water technician, Mr. Rodel Castillo, 38, starts the round. He finds gray water at the sample port after the second tank. The fine filter&rsquo;s pressure drop is three times its usual value. The carbon bypass valve handle is in a different position from where he left it on Friday. The first patients are due at 06:30.</p>
""", "questions": ["What three problems are in front of you, and what does each one mean?",
                  "May the first shift start, and what must happen first?",
                  "What should the supplier&rsquo;s report have contained?"]},
    "sections": [
        ("schedule", "Schedule", "A maintenance schedule by component", """
<div class="table-wrap"><table>
<thead><tr><th>Component</th><th>Routine attention</th><th>Replace when</th><th>Typical life</th></tr></thead>
<tbody>
<tr><td>Sediment media filter</td><td>Backwash; check timer</td><td>Pressure drop stays high after backwash; media lost or fouled</td><td>Years</td></tr>
<tr><td>Cartridge filters</td><td>Record pressure drop</td><td>Pressure drop reaches the change-out value, or at the scheduled interval</td><td>Weeks to months</td></tr>
<tr><td>Softener resin</td><td>Regeneration; salt; hardness test</td><td>Hardness cannot be controlled despite correct regeneration; resin fouled with iron</td><td>Several years</td></tr>
<tr><td>Carbon</td><td>Backwash; total chlorine tests</td><td>Breakthrough after the worker, or at the unit&rsquo;s set interval</td><td>Months to a year or more, depending on chlorine load</td></tr>
<tr><td>Reverse osmosis membrane</td><td>Daily readings; periodic cleaning by the supplier</td><td>Rejection or flow cannot be restored by cleaning</td><td>A few years</td></tr>
<tr><td>Ultraviolet lamp</td><td>Lamp hours; sleeve cleaning</td><td>At the maker&rsquo;s hour limit, or when intensity falls</td><td>About a year of continuous use</td></tr>
<tr><td>Ultrafilters</td><td>Pressure drop; cultures after the filter</td><td>Scheduled interval, pressure drop, or failed cultures</td><td>Months to a year</td></tr>
<tr><td>Tank vent filter</td><td>Inspection</td><td>Scheduled interval, or if wet or blocked</td><td>Months</td></tr>
<tr><td>Pumps and motors</td><td>Listen and feel for noise, heat, vibration, leaks</td><td>On failure or at planned overhaul</td><td>Years</td></tr>
<tr><td>Gauges and sensors</td><td>Compare with a reference</td><td>When they cannot be calibrated</td><td>Years</td></tr>
<tr><td>Flexible hoses</td><td>Inspection; included in disinfection</td><td>Scheduled interval; discoloration, stiffness, or slime</td><td>A year or so</td></tr>
</tbody></table></div>
<p>The lives shown are rough guides only. Your manufacturer&rsquo;s manual and your own records set the real intervals, because the same part lasts longer on clean feed water than on poor feed water. Write the installation date on every replaceable part, with a permanent marker or a tag, so that anyone can see its age at a glance.</p>
"""),
        ("after", "After a change", "After every change, prove the system", """
{{flow:The same four steps after any change|Flush or rinse::Send air, dust, preservative, or debris to drain.|Restore::Return every valve to its normal position and set the timers.|Test::Run the checks specific to what was changed.|Record and release::Write what was done, the results, and who released the system.}}
<div class="table-wrap"><table>
<thead><tr><th>What was changed</th><th>Checks before release</th></tr></thead>
<tbody>
<tr><td>Cartridge filter</td><td>Flush; no leaks at the housing; pressure drop at the clean value</td></tr>
<tr><td>Sediment media</td><td>Backwash and rinse until the water runs clear; pressure drop; the downstream filter</td></tr>
<tr><td>Softener resin or control valve</td><td>Regeneration and a full rinse; hardness within limit; product conductivity normal; clock correct</td></tr>
<tr><td>Carbon</td><td>Rinse until clear of fines; downstream filter checked or changed; total chlorine within limit after each tank at working flow; bypass closed and tagged</td></tr>
<tr><td>Reverse osmosis membrane</td><td>Flush out preservative by the supplier&rsquo;s method; rejection, flows, and pressures recorded as the new baseline; product conductivity normal; chemical analysis if the plan requires</td></tr>
<tr><td>Ultraviolet lamp or sleeve</td><td>Lamp lit; intensity reading; hours reset</td></tr>
<tr><td>Ultrafilter</td><td>Flush; integrity or pressure check by the maker&rsquo;s method; disinfect if the plan requires</td></tr>
<tr><td>Pipe work, a new outlet, or any opening of the loop</td><td>Disinfect; rinse; negative residual; culture and endotoxin before or soon after release, as the plan states</td></tr>
<tr><td>Pump or motor</td><td>Rotation, pressure, flow, no leaks, no abnormal heat or noise</td></tr>
</tbody></table></div>
{{stop:A system that has been opened, or has had a component changed, stays on hold until its post-change checks are recorded. &ldquo;The supplier said it is fine&rdquo; is not a record.}}
"""),
        ("service", "Service visits", "Managing a service visit", """
<p>An outside engineer knows the equipment. You know the unit, the patients&rsquo; schedule, and what the system looked like yesterday. A good visit uses both kinds of knowledge, and a poor one uses only the first.</p>
{{flow:Before, during, and after a visit|Before::Agree the time with the charge nurse. Note every valve position and the last readings.|During::Stay with the engineer where you can. Ask what is being done, and why.|Before they leave::Walk the system together against the drawing. Run it and take readings.|Paperwork::Get a signed report listing the work done, parts and lot numbers, and tests and results.|After::Complete the post-change checks. File the report. Tell the nurse the system is released, or that it is on hold.}}
<div class="table-wrap"><table>
<thead><tr><th>A service report should state</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Date, time, and the engineer&rsquo;s name</td><td>So the work can be traced</td></tr>
<tr><td>What was found and what was done</td><td>The next person needs the history</td></tr>
<tr><td>Parts and materials fitted, with type and lot</td><td>So a substitute or a recalled batch can be traced</td></tr>
<tr><td>Tests performed, with the actual results</td><td>Evidence, not opinion</td></tr>
<tr><td>Valves and settings changed, and their final positions</td><td>It prevents a bypass being left open</td></tr>
<tr><td>Anything left outstanding</td><td>So that it is followed up</td></tr>
</tbody></table></div>
"""),
        ("file", "System file", "The system file, instruments, and spares", """
{{cards:What the system file holds|Drawings and valve list::Kept up to date.|Manuals::For every component.|Validation records::From installation and from each major change.|Daily logs::In date order.|Laboratory reports::Chemical, culture, and endotoxin, each signed as reviewed.|Disinfection records::With concentrations and residual results.|Maintenance and service reports::Scheduled and unscheduled.|Incident records::With the review and the actions taken.}}
<p>The instruments you test with need looking after too. Every number in the log is only as good as the tool that produced it. A chlorine meter that has never been checked, a conductivity meter with a dirty probe, or a gauge stuck at one reading all produce confident, wrong numbers.</p>
<div class="table-wrap"><table>
<thead><tr><th>Instrument or supply</th><th>Care</th></tr></thead>
<tbody>
<tr><td>Chlorine and hardness kits and strips</td><td>In date; stored cool, dry, and closed; a reorder point set</td></tr>
<tr><td>Handheld chlorine meter</td><td>A zero check at each use; verified against a standard on schedule</td></tr>
<tr><td>Conductivity meter</td><td>Probe rinsed; verified against a standard solution on schedule</td></tr>
<tr><td>Pressure gauges</td><td>Compared with a reference gauge on schedule; replaced if stuck or fogged</td></tr>
<tr><td>Thermometers</td><td>Compared with a reference on schedule</td></tr>
</tbody></table></div>
<p>Finally, keep a short list of spares on site, so that a predictable failure does not cancel a shift: cartridges, salt, in-date test kits, a spare ultraviolet lamp, fuses, hose and clamps, and warning tags. Review the list after every incident, and add whatever you wished you had.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The three problems.</strong> Gray water means the new carbon was not rinsed until clear, and fines are passing downstream. The high pressure drop means those fines are plugging the fine filter, and they may have reached the membrane. The moved bypass handle means the carbon may be partly bypassed, so chlorine removal is unproven.</p>
<p><strong>May the first shift start?</strong> No. Tell the charge nurse that the system is on hold, and why, well before the 06:30 patients arrive. Then work in order. Confirm the bypass is fully closed and tag it. Rinse the carbon to drain until the water runs clear. Change the fine filter. Test total chlorine after each tank at working flow, and take a full set of reverse osmosis readings. Release the system only when those results are recorded and acceptable.</p>
<p><strong>What the report should have contained.</strong> The carbon type and lot, the rinse performed, chlorine results at both ports, the final valve positions, and a signature. Arrange for future visits to be attended, and for the walk-down to happen before the engineer leaves, not the morning after.</p>
"""],
    "skills": {"title": "Cartridge change with post-change checks",
        "intro": "Materials: a replacement cartridge of the correct type, the housing tool, the drawing and valve list, the log, and a service report form.",
        "items": [("Agrees the timing with the charge nurse and confirms no patient is on dialysis.", True),
                  ("Records valve positions and pressure readings before starting.", False),
                  ("Isolates and depressurizes the housing safely.", True),
                  ("Fits the correct cartridge and seals the housing without contaminating it.", False),
                  ("Flushes to drain and checks for leaks.", False),
                  ("Returns every valve to its normal position and confirms against the valve list.", True),
                  ("Records the new clean pressure drop and writes the installation date on the housing.", False),
                  ("States the post-change checks for carbon, membrane, and pipe work.", True),
                  ("Completes the record and releases the system in writing.", True)],
        "placement": "Review the last three supplier service reports in your system file against the list in this module and note what is missing."},
    "quiz": [
        ("What triggers carbon replacement before its scheduled date?",
         ["A full brine tank", "Chlorine breakthrough after the worker tank", "Cold weather", "A new cartridge"], 1,
         "Breakthrough shows the carbon is exhausted."),
        ("After carbon is replaced, which check is essential before release?",
         ["Hardness", "Total chlorine within limit after each tank at working flow", "Lamp hours", "Tank level"], 1,
         "New carbon must be proven to remove chlorine, and the bypass must be closed."),
        ("A new reverse osmosis membrane has been fitted. What should be recorded?",
         ["Nothing new", "Rejection, flows, and pressures as the new baseline", "Only the invoice", "The softener clock"], 1,
         "Future readings are judged against the new baseline."),
        ("A section of loop pipe was opened for repair. What is required?",
         ["A wipe of the outside", "Disinfection, rinse with negative residual, and cultures as the plan states", "A hardness test", "Nothing"], 1,
         "Opening the loop can introduce bacteria."),
        ("An engineer leaves a report saying only &ldquo;Serviced. OK.&rdquo; What is correct?",
         ["Accept it", "Ask for work done, parts, test results, and final valve positions", "Throw it away", "Sign it yourself"], 1,
         "A report must give evidence that can be checked later."),
        ("Why write the installation date on each replaceable part?",
         ["Decoration", "So anyone can see when it is due for replacement", "For the supplier&rsquo;s warranty only", "It is not useful"], 1,
         "Visible dates prevent overdue parts."),
        ("A pressure gauge has read exactly the same value for a month. What should you suspect?",
         ["A perfect system", "A stuck gauge", "High chlorine", "A new filter"], 1,
         "Gauges fail too; compare with a reference."),
        ("What is the first step before any maintenance that takes a stage out of service?",
         ["Start immediately", "Agree the timing with the charge nurse and confirm no patient is on dialysis", "Open the bypass", "Call the laboratory"], 1,
         "Maintenance is planned around patient treatment."),
    ],
    "terms": [("Preservative", "A chemical in which new membranes are shipped; it must be flushed out before use."),
              ("Integrity test", "A test that shows a filter has no holes or leaks."),
              ("Reorder point", "The stock level at which more is ordered."),
              ("Walk-down", "Checking the system, component by component, against the drawing.")],
    "readings": [("dialysis-water-treatment-systems.html", "Component functions and failure modes."),
                 ("dialysis-qapi-vs-cqi.html", "Using maintenance data in quality review.")],
}

NEW["12"] = {
    "image_alt": "A technician placing a hold tag on a water system control panel while speaking to a nurse.",
    "keep": "06",
    "sections": [("L", "06", "pattern"), ("L", "06", "failures"),
        ("report", "Reporting", "What to say, in thirty seconds", """
<p>When a limit is crossed, the charge nurse is usually busy with patients, and has perhaps thirty seconds to listen. In that time she needs five facts, in the same order every time, so that she can decide without asking you a single question.</p>
{{flow:An urgent water report|What::The result or the alarm, with its number and unit.|Where::Which port, tank, or unit.|When::The time you found it.|Who is affected::Which stations are running, and whether patients are connected.|What you have done::The hold you have placed, and what you need from her.}}
{{formula:<strong>Example.</strong> &ldquo;Total chlorine is 0.18 mg/L after tank one and 0.14 after tank two, at 10:45. Our limit is 0.1. Six patients are still on. I have put the system on hold for new starts. I need the medical director informed.&rdquo;}}
<p>Notice what the example leaves out: no guesses about the cause, no apology, no story. Then write down the time you reported and the name of the person you told. If you cannot reach the charge nurse within a minute, go up the unit&rsquo;s escalation list. Do not wait.</p>
"""),
        ("L", "06", "disaster"), ("L", "06", "quality"),
        ("capstone", "Capstone", "Capstone: four practical stations", """
<p>To finish the track, a preceptor observes you at four stations on your own unit&rsquo;s system. Each station uses a simulated problem, set up so that it looks like a real one. All critical steps must be satisfactory. The stations test what you do, not what you can recite.</p>
<div class="table-wrap"><table>
<thead><tr><th>Station</th><th>Task</th><th>Critical steps</th></tr></thead>
<tbody>
<tr><td>1. Start-of-day round</td><td>Complete the round, including a total chlorine test, and release the system</td><td>Correct port and correct test; numbers with units; release stated in words</td></tr>
<tr><td>2. Out-of-range result</td><td>Respond to a simulated chlorine result above the limit after both tanks</td><td>Hold; report within two minutes with the five facts; no repeat result substituted for the first</td></tr>
<tr><td>3. Sampling and disinfection</td><td>Collect a culture sample; then talk through a chemical disinfection, covering dilution, reach, dwell, rinse, and residual</td><td>Aseptic collection; correct dilution; negative residual at every outlet before release</td></tr>
<tr><td>4. After a change</td><td>A simulated service visit has replaced the carbon and left a valve out of position; find the problems and state the post-change checks</td><td>Finds the valve; holds the system; states chlorine testing at both ports before release</td></tr>
</tbody></table></div>
{{cards:To complete the track|All twelve self-assessments::Attempted, with every missed item reviewed.|Every critical checklist step::Demonstrated on your own system.|One full disinfection and one sampling round::Performed under observation.|Four capstone stations::All critical steps satisfactory.|Sign-off::Recorded by the preceptor on the unit&rsquo;s own form.}}
"""),
    ],
    "quiz_keep": [("06", [0, 1, 2, 3, 4, 5, 6, 7])],
    "quiz": [
        ("In an urgent water report, which fact tells the nurse how many patients are at risk right now?",
         ["The supplier&rsquo;s name", "Which stations are running and whether patients are connected", "The softener setting", "The date of the last culture"], 1,
         "The clinical team&rsquo;s first decision concerns patients already on dialysis."),
        ("You cannot reach the charge nurse within a minute during a breakthrough. What do you do?",
         ["Wait", "Go up the unit&rsquo;s escalation list", "Release the system", "Go home"], 1,
         "A hold must be communicated; use the next contact."),
    ],
}
