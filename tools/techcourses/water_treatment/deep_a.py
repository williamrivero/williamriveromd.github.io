# -*- coding: utf-8 -*-
"""Water Treatment track, 12-module edition: new content for Modules 1 to 6.
compose.py combines this with sections reused from legacy/ (the original six modules).
Entry keys: objectives, big, case (dict or ("L", legacy_id)), sections (list of ("L", legacy_id, section_id) or
(id, nav, h2, html)), debrief, skills, quiz_keep [(legacy_id, [indexes])], quiz (new items), terms, readings, calcs, image_alt."""

NEW = {}

NEW["01"] = {
    "image_alt": "A technician comparing a glass of tap water with a dialyzer on a bench.",
    "keep": "01",   # objectives, big, case, debrief, skills, terms, readings from legacy module 01
    "sections": [("L", "01", "exposure"), ("L", "01", "contaminants"),
        ("units", "Units", "Reading the units on a water report", """
<p>Water results come in several units. An independent technician reads them without stopping to think.</p>
<div class="table-wrap"><table>
<thead><tr><th>Unit</th><th>Say it as</th><th>Used for</th><th>Worth knowing</th></tr></thead>
<tbody>
<tr><td>mg/L</td><td>milligrams per liter</td><td>Chlorine, metals, minerals</td><td>The same as parts per million (ppm) in water</td></tr>
<tr><td>&micro;g/L</td><td>micrograms per liter</td><td>Trace metals such as lead</td><td>One thousandth of a mg/L; also called parts per billion</td></tr>
<tr><td>&micro;S/cm</td><td>microsiemens per centimeter</td><td>Conductivity of feed and product water</td><td>Rises with dissolved salts; product water is far lower than feed</td></tr>
<tr><td>CFU/mL</td><td>colony-forming units per milliliter</td><td>Bacteria</td><td>Counts live bacteria that grew on the plate</td></tr>
<tr><td>EU/mL</td><td>endotoxin units per milliliter</td><td>Endotoxin</td><td>Measures bacterial fragments, live or dead</td></tr>
<tr><td>gpg</td><td>grains per gallon</td><td>Hardness, on many test kits</td><td>1 grain per gallon is about 17 mg/L as calcium carbonate</td></tr>
<tr><td>psi or bar</td><td>pounds per square inch, or bar</td><td>Pressure gauges</td><td>1 bar is about 14.5 psi; never mix the two in one log</td></tr>
</tbody></table></div>
{{key:Always write the unit beside the number. &ldquo;0.1&rdquo; means nothing; &ldquo;0.1 mg/L total chlorine&rdquo; is a result.}}
"""),
        ("L", "01", "tiers"),
        ("history", "Why the rules exist", "Four kinds of harm that shaped today&rsquo;s rules", """
<p>Every limit in the standard exists because patients were once injured. Knowing the pattern helps you recognize it early.[[ward2011]][[coulliette2013]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What went wrong</th><th>How it showed in patients</th><th>What the unit had missed</th><th>The safeguard today</th></tr></thead>
<tbody>
<tr><td>Chloramine reached the dialysate</td><td>Falling hemoglobin across many patients, rising need for anemia treatment, sometimes sudden hemolysis</td><td>Exhausted carbon; a utility that switched disinfectant; a free chlorine test used where total chlorine was needed</td><td>Two carbon tanks in series, total chlorine testing every shift</td></tr>
<tr><td>Aluminum in the water</td><td>Bone pain, fractures, confusion and speech problems developing over months</td><td>No reverse osmosis, or a failing membrane</td><td>Reverse osmosis, rejection monitoring, periodic chemical analysis</td></tr>
<tr><td>Excess fluoride</td><td>Itching, nausea, chest pain, dangerous heart rhythms within one session</td><td>Utility overfeed with an exhausted or absent treatment stage</td><td>Reverse osmosis and chemical analysis; attention to utility notices</td></tr>
<tr><td>Bacteria and endotoxin</td><td>Chills, fever, and low blood pressure in several patients on one shift</td><td>Dead legs, a neglected tank, skipped disinfection, contaminated bicarbonate</td><td>Loop design, scheduled disinfection, monthly cultures and endotoxin tests</td></tr>
</tbody></table></div>
<p>Notice the common thread: in nearly every case the equipment existed, and a routine check had lapsed. That is why this track spends as much time on logs as on tanks.</p>
"""),
        ("L", "01", "roles")],
    "quiz_keep": [("01", [0, 1, 2, 3, 4, 5, 6, 7])],
    "quiz": [
        ("A test kit reports hardness as 2 grains per gallon. About how many mg/L as calcium carbonate is that?",
         ["2", "17", "34", "170"], 2, "One grain per gallon is about 17 mg/L, so two is about 34 mg/L."),
        ("Several patients&rsquo; hemoglobin levels fall over two months with no other explanation. Which water problem should a technician think of first?",
         ["Hard water", "Low-level chloramine breakthrough", "Cold feed water", "High product flow"], 1,
         "Chloramine damages red blood cells and can show first as a pattern of worsening anemia."),
    ],
}

NEW["02"] = {
    "image_alt": "A technician and an engineer looking at a system drawing in a water room.",
    "objectives": [
        "Describe how city, deep-well, and delivered water differ and what each demands of the system.",
        "Read a feed water analysis and say what each line means for treatment.",
        "Follow a system drawing, identify valves and bypasses, and state their normal positions.",
        "Explain how a system is sized and why it is validated before first use and after major change.",
    ],
    "big": """
{{plain:A water system is designed for one particular water supply and one particular workload. Change either, a new well, a tanker delivery, four more stations, and the system that was safe last month may no longer be. An independent technician knows what the system was designed for, so that he or she can tell when reality has moved away from the design.}}
{{cards:Key terms for this module|Feed water analysis::A laboratory report on the water entering the system.|Total dissolved solids::The total amount of dissolved minerals and salts.|Turbidity::Cloudiness from fine particles.|Bypass valve::A valve that lets water go around a treatment stage.|Normally closed::A valve that stays shut in routine operation.|Peak demand::The most water the unit needs at one moment.|Validation::Documented proof that the system produces water within limits, before patients use it.}}
""",
    "case": {"title": "A new well replaces the city supply", "html": """
<p>To cut costs and avoid supply interruptions, the building owner switches the clinic from city water to a newly drilled deep well. Nobody tells the water room. Over three weeks the softener needs regenerating twice as often, the sediment filter loads quickly with reddish deposits, and the morning chlorine test reads zero at the feed tap as well as after the carbon tanks.</p>
""", "questions": ["What do the reddish deposits and the faster softener exhaustion tell you?",
                  "The feed chlorine is zero. Is that good news?",
                  "What should have happened before the source was changed?"]},
    "sections": [
        ("sources", "Source water", "Three sources, three sets of problems", """
{{fig:wts_source}}
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Typical character</th><th>Main demands on the system</th><th>What to watch</th></tr></thead>
<tbody>
<tr><td>City (municipal) water</td><td>Disinfected with chlorine or chloramine; quality fairly steady but changes after pipe work, floods, or a change of disinfectant</td><td>Carbon capacity for the highest disinfectant dose expected</td><td>Utility notices; total chlorine in the feed; sediment after main breaks</td></tr>
<tr><td>Deep well</td><td>Usually no disinfectant; often hard; may carry iron, manganese, and more dissolved minerals; bacteria possible</td><td>Larger softener; iron removal if needed; attention to microbial growth because nothing in the feed suppresses it</td><td>Hardness, iron staining, softener frequency, seasonal change</td></tr>
<tr><td>Delivered (tanker) water</td><td>Unknown and variable from load to load</td><td>Testing each delivery as a new source</td><td>Chlorine, hardness, turbidity, the tanker&rsquo;s previous cargo</td></tr>
</tbody></table></div>
<p>Many Philippine units use more than one source over a year: city water with a deep well as backup, or tankers during shortages. Each switch is a change of source. It is reported to the charge nurse and the medical director, and the unit&rsquo;s procedure for a source change is followed before patients are dialyzed on it.[[iso23500_1]]</p>
"""),
        ("report", "Feed water report", "Reading a feed water analysis", """
<p>A feed water analysis is done when the system is designed, then periodically and whenever the source changes. You do not need to be a chemist to use it. Read each line as a message about one part of the system.</p>
<div class="table-wrap"><table>
<thead><tr><th>Line on the report</th><th>What it means</th><th>Which part of the system it affects</th></tr></thead>
<tbody>
<tr><td>Total chlorine, and whether chloramine is used</td><td>How much disinfectant the carbon must remove</td><td>Carbon tank size and replacement interval</td></tr>
<tr><td>Hardness (calcium and magnesium)</td><td>How fast the softener resin is used up</td><td>Softener size and regeneration frequency</td></tr>
<tr><td>Iron and manganese</td><td>Metals that foul softener resin and membranes and stain equipment reddish or black</td><td>May need a dedicated iron filter ahead of the softener</td></tr>
<tr><td>Total dissolved solids, or conductivity</td><td>The overall mineral load</td><td>Reverse osmosis workload and the product conductivity you can expect</td></tr>
<tr><td>Turbidity or silt density index</td><td>Fine particles that plug filters and membranes</td><td>Sediment filtration and cartridge life</td></tr>
<tr><td>pH</td><td>Acidity or alkalinity</td><td>Carbon removes chloramine less efficiently at high pH; membrane performance also shifts</td></tr>
<tr><td>Temperature range</td><td>Cold water lowers membrane output</td><td>System capacity on the coldest day</td></tr>
<tr><td>Aluminum, fluoride, nitrate, sulfate, and metals</td><td>Toxic contaminants that must be reduced below dialysis limits</td><td>Reverse osmosis performance; how much margin the membrane has</td></tr>
<tr><td>Bacteria</td><td>Microbial load entering the system</td><td>Disinfection strategy</td></tr>
</tbody></table></div>
{{key:Keep the design-stage feed water report in the water room file. When something changes, compare the new report line by line with the old one.}}
"""),
        ("drawing", "Drawing and valves", "The system drawing and its valves", """
<p>Every system should have a current drawing showing each component in order, with every valve, gauge, and sample port numbered to match a tag on the equipment. If your system has no drawing or no tags, making them with your preceptor is the best first project you can take on.</p>
{{cards:Valves you must be able to find|Isolation valves::One before and one after each tank or filter, so it can be serviced.|Bypass valves::Let water go around a stage. Useful for service; dangerous if left open.|Sample ports::Small taps at defined points. Keep them clean and capped.|Drain valves::For backwash, rinse, and emptying tanks.|Check valves::Let water flow one way only, protecting against backflow.|Pressure relief valve::Opens if pressure is too high.}}
<div class="table-wrap"><table>
<thead><tr><th>Valve</th><th>Normal position during treatment</th><th>What happens if it is wrong</th></tr></thead>
<tbody>
<tr><td>Carbon tank bypass</td><td>Closed, and locked or tagged</td><td>Chlorine and chloramine go straight to the reverse osmosis unit and the patients</td></tr>
<tr><td>Softener bypass</td><td>Closed</td><td>Hard water scales the membrane</td></tr>
<tr><td>Reverse osmosis bypass, if fitted</td><td>Closed, and locked or tagged</td><td>Untreated or partly treated water enters the loop</td></tr>
<tr><td>Loop return valve</td><td>Open</td><td>Water stops circulating; pressure and bacterial risk rise</td></tr>
<tr><td>Sample ports</td><td>Closed and capped</td><td>Leaks and contamination</td></tr>
</tbody></table></div>
{{stop:After any service visit, walk the system with the drawing and confirm every valve is back in its normal position before the system is released. A carbon bypass left open is one of the most dangerous errors in a water room.}}
"""),
        ("sizing", "Sizing", "How a system is sized: a worked example", """
{{fig:wts_sizing}}
<p>Sizing is the designer&rsquo;s job, but a technician who understands it can tell when the unit has outgrown its system. The steps, with illustrative numbers only:</p>
{{flow:Sizing in five steps|Count the users::Machines, reprocessing sinks, bicarbonate mixing, rinse and disinfection cycles.|Find peak demand::The moment the most water is drawn, usually shift start.|Add a margin::Room for growth and for a membrane that has aged.|Correct for cold water::Check output at the coldest feed temperature expected.|Check each stage::Carbon contact time and softener capacity at that same flow.}}
{{formula:<strong>Illustration.</strong> Twelve machines each drawing about 0.8 liters per minute while running gives about 10 liters per minute. Add 4 liters per minute for reprocessing and mixing: 14 liters per minute at peak. With a 20 percent margin the system should deliver about 17 liters per minute, at the coldest feed water of the year. Your own figures come from the machine manuals and the designer.}}
<p>Two consequences follow. First, adding stations, a reprocessing machine, or hemodiafiltration raises peak demand and can push the carbon tanks below their contact time even if the reverse osmosis unit keeps up. Second, low water pressure alarms at shift start are often a sizing signal, not a fault.</p>
"""),
        ("validation", "Validation", "Validation: proving the system before patients rely on it", """
<p>A new or substantially changed system is not used on patients until it has been shown, with documented test results, to produce water within limits. This is validation. The medical director approves it.[[iso23500_1]]</p>
{{cards:What validation usually includes|Installation check::The system matches the drawing; materials and connections are correct.|Operational check::Flows, pressures, alarms, and automatic valves work as designed.|Chemical analysis::Product water meets the chemical limits.|Microbiology::Cultures and endotoxin within limits, typically repeated over several weeks.|Disinfection proof::Disinfectant reaches every point and rinses out completely.|Records::Results, dates, and signatures filed in the system file.}}
<p>The same thinking applies on a smaller scale after any major change: a new membrane, new carbon, pipe work, or a change of source. Module 11 covers what to re-test after each kind of change.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> Reddish deposits point to iron in the well water, and a softener that exhausts twice as fast means the water is much harder than before. Zero chlorine in the feed is not good news: it means there is no disinfectant suppressing bacterial growth in the pretreatment, and it confirms the source has changed. Report all three findings to the charge nurse and medical director the day you put them together. A source change should have been preceded by a feed water analysis of the well, a review of whether the softener, filters, and membrane can cope, a decision about iron removal and microbial control, and re-validation with chemical and microbiological tests. Until that is done, the medical director decides whether treatment continues on this water.</p>
"""],
    "skills": {"title": "Reading the system drawing and the feed water report",
        "intro": "Materials: the system drawing, valve tags, the most recent feed water analysis, and the design-stage analysis.",
        "items": [("Names the unit&rsquo;s water source or sources and how the unit is told of a change.", True),
                  ("Traces the drawing from feed to drain and matches each numbered valve to its tag.", False),
                  ("States the normal position of every bypass valve and shows how each is locked or tagged.", True),
                  ("Reads five lines of the feed water report and says which component each affects.", False),
                  ("Compares the current report with the design-stage report and points out any change.", False),
                  ("Explains what would raise the unit&rsquo;s peak demand.", False),
                  ("States who approves use of the system after a major change.", True)],
        "placement": "With your preceptor, update or create the valve list for your system: number, location, purpose, normal position."},
    "quiz": [
        ("A unit switches from city water to a deep well. What is true of the well water?",
         ["It is the same water", "It usually has no disinfectant and is often harder", "It needs no treatment", "It is always sterile"], 1,
         "Well water is typically undisinfected and mineral-rich, so the softener works harder and microbial control needs attention."),
        ("Which valve must be closed and locked or tagged during treatment?",
         ["Loop return valve", "Carbon tank bypass valve", "Feed isolation valve", "Sample port on the feed line"], 1,
         "An open carbon bypass sends chlorine and chloramine directly downstream."),
        ("Iron in the feed water mainly threatens which components?",
         ["The softener resin and the membrane", "The gauges", "The dialysis chairs", "The drain"], 0,
         "Iron fouls resin and membranes and leaves reddish deposits."),
        ("Why does adding stations threaten the carbon tanks even if the reverse osmosis unit keeps up?",
         ["Carbon dislikes noise", "Higher flow shortens contact time in the carbon bed", "Stations use carbon", "It does not"], 1,
         "Contact time is bed volume divided by flow; more flow means less time."),
        ("What is validation?",
         ["A daily chlorine test", "Documented proof that the system produces water within limits before patients use it", "A supplier&rsquo;s invoice", "A backwash"], 1,
         "Validation is the evidence that a new or changed system is fit for use."),
        ("A tanker delivers water during a shortage. How is it handled?",
         ["Used immediately", "Tested and treated as a new source", "Mixed with product water", "Rejected always"], 1,
         "Each delivery can differ, so it is tested before use."),
        ("After a service visit, what is checked before release?",
         ["That every valve is back in its normal position", "The paint", "The invoice total", "Nothing"], 0,
         "Valves left in service positions are a common and dangerous error."),
        ("On a feed water report, which line most directly tells you how hard the softener must work?",
         ["pH", "Hardness", "Temperature", "Turbidity"], 1, "Hardness is the calcium and magnesium the softener must remove."),
    ],
    "terms": [("Municipal water", "Water supplied by a city or district utility."),
              ("Silt density index", "A test of how quickly fine particles plug a filter; it predicts membrane fouling."),
              ("Check valve", "A valve that allows flow in one direction only."),
              ("Re-validation", "Repeating the proof of water quality after a major change.")],
    "readings": [("dialysis-water-treatment-systems.html", "Design by source water and capacity sizing in full.")],
    "calcs": ["calc-dialysis-water-reuse.html"],
}

NEW["03"] = {
    "image_alt": "A technician checking the salt level in a softener brine tank.",
    "objectives": [
        "Explain how sediment filters work and use the pressure drop to decide on backwash or replacement.",
        "Describe the softener cycle and set and verify the regeneration timer.",
        "Perform a hardness test and interpret the result.",
        "Troubleshoot common filter and softener problems.",
    ],
    "big": """
{{plain:The first two stages are the humble ones: a filter that catches dirt and a softener that removes the minerals that form scale. Neither protects the patient directly. They protect the carbon and the membrane, and when they are neglected, everything downstream fails sooner.}}
{{cards:Key terms for this module|Multimedia filter::A tank with layers of sand and gravel that trap particles.|Cartridge filter::A replaceable filter element in a housing.|Pressure drop::Pressure before the filter minus pressure after it.|Backwash::Reverse flow that lifts and rinses the bed.|Resin::Beads that swap sodium for calcium and magnesium.|Regeneration::Recharging the resin with brine.|Hardness::Dissolved calcium and magnesium.}}
""",
    "case": ("L", "02"),
    "sections": [("L", "02", "filters"),
        ("backwash", "Backwash", "Backwashing a media filter", """
<p>Most media filters and carbon tanks backwash automatically on a timer or when the pressure drop reaches a set point. You still need to know what the valve is doing, because you are the one who notices when it does not.</p>
{{flow:An automatic backwash cycle|Service ends::The control valve takes the tank off line.|Backwash::Water flows upward, lifts the bed, and carries trapped dirt to drain.|Settle::Flow stops; the layers resettle, heaviest at the bottom.|Rinse::Downward flow to drain clears loosened particles.|Return to service::Water goes forward again.}}
<div class="table-wrap"><table>
<thead><tr><th>Check during or after a backwash</th><th>What you want to see</th><th>If not</th></tr></thead>
<tbody>
<tr><td>Timer setting</td><td>Outside treatment hours</td><td>Reset and report; a backwash in treatment hours starves the system of water</td></tr>
<tr><td>Drain flow</td><td>Strong flow, dirty at first, clearing by the end</td><td>Weak flow suggests a blocked drain line or failing valve</td></tr>
<tr><td>Media in the drain</td><td>None</td><td>Sand or carbon in the drain means the flow is too high or an internal part has broken</td></tr>
<tr><td>Pressure drop afterward</td><td>Back near the clean value</td><td>If it stays high, the bed is fouled or channeled and needs service</td></tr>
</tbody></table></div>
"""),
        ("L", "02", "softener"),
        ("hardness", "Hardness test", "The hardness test and what the result means", """
<p>Hardness is tested on water leaving the softener, usually at the end of the treatment day when the resin has done the most work. Most kits are either drop-count titrations (count the drops until the color changes) or dip strips.</p>
{{flow:Performing a drop-count hardness test|Flush the port::Run water so you are testing the softener&rsquo;s current output.|Measure the sample::Fill the vial exactly to the mark.|Add the indicator::The sample turns one color if hardness is present.|Add reagent drop by drop::Swirl after each drop and count.|Read the end point::The color change marks the end; the drop count gives the hardness by the kit&rsquo;s table.|Record::Value, unit, port, time, name.}}
<div class="table-wrap"><table>
<thead><tr><th>Result</th><th>Meaning</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Within the unit&rsquo;s limit</td><td>Softener has capacity</td><td>Record</td></tr>
<tr><td>Rising over several days but within the limit</td><td>Capacity is being used up sooner than before</td><td>Report the trend; check salt, regeneration frequency, and whether the feed water has become harder</td></tr>
<tr><td>Above the limit</td><td>Resin exhausted or regeneration failed</td><td>Report; check salt, bridge, clock, and brine draw; regenerate outside treatment hours; retest before the next shift</td></tr>
</tbody></table></div>
<p>A softener regenerates either by the clock (every so many days) or by a meter (after so many liters). A meter-based softener adapts when water use rises; a clock-based one does not, so it can run out early during a busy week.</p>
"""),
        ("trouble", "Troubleshooting", "Troubleshooting filters and softeners", """
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Likely causes</th><th>What to check, in order</th></tr></thead>
<tbody>
<tr><td>Pressure drop rises within days of a backwash</td><td>Dirtier feed water; backwash not completing; bed fouled</td><td>Feed water appearance, backwash drain flow, timer, then call for service</td></tr>
<tr><td>Low pressure everywhere downstream</td><td>Clogged filter; booster pump fault; low feed pressure from the street</td><td>Feed gauge first, then each gauge in turn to find where pressure is lost</td></tr>
<tr><td>Hard water after the softener</td><td>No salt; salt bridge; clock wrong; brine line blocked; resin exhausted or fouled with iron</td><td>Salt level, bridge, clock, brine draw during a regeneration, then resin</td></tr>
<tr><td>Salty water downstream, high conductivity alarms</td><td>Regeneration during treatment; rinse too short; control valve stuck</td><td>Stop or bypass by procedure, report, complete the rinse, test hardness and conductivity</td></tr>
<tr><td>Brine tank overflowing or not refilling</td><td>Float or refill valve fault</td><td>Report for service; do not leave the softener unregenerated</td></tr>
<tr><td>Resin beads in the downstream filter</td><td>Broken internal screen</td><td>Report; the softener needs repair before it damages the membrane</td></tr>
</tbody></table></div>
{{key:To find where pressure is being lost, read the gauges in order from the feed line. The fault lies between the last good gauge and the first bad one.}}
"""),
    ],
    "debrief": ("L", "02"),
    "skills": {"title": "Filter and softener round with a hardness test",
        "intro": "Materials: the log, a hardness test kit, the softener manual, and the system drawing.",
        "items": [("Reads both gauges on each filter, calculates the pressure drop, and compares it with the clean value.", False),
                  ("States the pressure drop at which the unit backwashes or changes each filter.", False),
                  ("Checks the backwash and regeneration timers against the real time.", True),
                  ("Checks the salt level and tests for a salt bridge.", False),
                  ("Performs a hardness test at the correct port and records the value with its unit.", True),
                  ("States the action for a hardness result above the unit&rsquo;s limit.", True),
                  ("Finds the point of pressure loss in a simulated low-pressure problem by reading gauges in order.", False)],
        "placement": "Observe one full softener regeneration from start to finish with your preceptor and note what the drain flow looks like at each stage."},
    "quiz_keep": [("02", [0, 1, 2, 7])],
    "quiz": [
        ("During a backwash, in which direction does water flow through the bed?",
         ["Downward", "Upward, lifting the bed", "Sideways", "It does not flow"], 1, "Upward flow lifts the media and carries trapped dirt to drain."),
        ("Sand appears in the drain during backwash. What does this suggest?",
         ["Normal operation", "Flow is too high or an internal part is broken", "The softener needs salt", "The carbon is new"], 1,
         "Media should stay in the tank; losing it means a fault."),
        ("A clock-based softener runs out early during an unusually busy week. Why?",
         ["The clock is fast", "It regenerates by time, not by the amount of water used", "Salt is too pure", "The carbon is exhausted"], 1,
         "More water used means the resin is exhausted before the scheduled regeneration."),
        ("Pressure is normal at the feed gauge and after the sediment filter, but low after the softener. Where is the problem?",
         ["In the street supply", "In the sediment filter", "In or around the softener", "In the reverse osmosis unit"], 2,
         "The fault lies between the last good gauge and the first bad one."),
    ],
    "terms": [("Titration", "Adding a reagent drop by drop until a color change shows the end point."),
              ("Control valve", "The automatic valve on top of a tank that directs service, backwash, and rinse flows."),
              ("Channeling", "Water cutting a path through a bed so most of the bed is bypassed.")],
    "readings": [("dialysis-water-treatment-systems.html", "Pretreatment design and troubleshooting.")],
}

NEW["04"] = {
    "image_alt": "Gloved hands holding a chlorine test vial against a color comparator beside a sample port.",
    "objectives": [
        "Distinguish free chlorine, chloramine, and total chlorine.",
        "Explain empty-bed contact time and why two carbon tanks are used in series.",
        "Perform a total chlorine test correctly and act on the result at each sample port.",
        "Describe carbon replacement and the checks required before release.",
    ],
    "big": """
{{plain:Of everything in the water room, the carbon tanks stand most directly between a poison and the patient. Chlorine and chloramine cross the dialyzer membrane and destroy red blood cells, and nothing after the carbon removes them reliably. This module is about one tank arrangement and one test, done properly, several times a day, for as long as the unit runs.}}
{{cards:Key terms for this module|Free chlorine::Chlorine not combined with anything.|Chloramine::Chlorine combined with ammonia. Also called combined chlorine.|Total chlorine::Free chlorine plus chloramine.|Empty-bed contact time::Minutes of contact between water and carbon.|Worker and polisher::First and second carbon tanks in series.|Breakthrough::Chlorine passing through a tank.|Reagent::The chemical in the test that produces color.}}
""",
    "case": ("L", "04"),
    "sections": [
        ("chemistry", "Chlorine basics", "Free, combined, and total chlorine", """
<p>Utilities disinfect water in one of two ways. Some add chlorine alone. Others add chlorine and then ammonia, which forms chloramine: a weaker but longer-lasting disinfectant that survives the journey through long pipe networks.</p>
{{formula:<strong>Total chlorine = free chlorine + chloramine (combined chlorine)</strong>}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Free chlorine</th><th>Chloramine</th></tr></thead>
<tbody>
<tr><td>Removed by carbon</td><td>Quickly</td><td>More slowly; needs the full contact time</td></tr>
<tr><td>Detected by a free chlorine test</td><td>Yes</td><td>No</td></tr>
<tr><td>Detected by a total chlorine test</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Harm in dialysis</td><td>Damages red blood cells</td><td>Damages red blood cells; the commoner cause of patient injury</td></tr>
</tbody></table></div>
<p>A utility can change from chlorine to chloramine, or raise the dose, without telling you. A unit that tests only free chlorine would see nothing. This is why the test is always total chlorine, and why its limit of 0.1 mg/L applies to the total.[[iso23500_3]]</p>
"""),
        ("L", "02", "carbon"),
        ("L", "04", "chlorine"),
        ("technique", "Test technique", "Getting the test right every time", """
<div class="table-wrap"><table>
<thead><tr><th>Error</th><th>Effect on the result</th><th>How to avoid it</th></tr></thead>
<tbody>
<tr><td>Sampling before the system has run</td><td>Falsely low: the water sat in the carbon for hours</td><td>Run for the time your procedure states</td></tr>
<tr><td>Not flushing the port</td><td>Unrepresentative</td><td>Flush for the stated time</td></tr>
<tr><td>Free chlorine reagent or strip used</td><td>Misses chloramine entirely</td><td>Check the kit says total chlorine</td></tr>
<tr><td>Expired or badly stored reagent</td><td>Falsely low or no color</td><td>Check dates; store cool, dry, and closed</td></tr>
<tr><td>Wrong sample volume</td><td>Too strong or too weak a color</td><td>Fill exactly to the mark</td></tr>
<tr><td>Reading too early or too late</td><td>Wrong value</td><td>Use a timer, not a guess</td></tr>
<tr><td>Dirty vial or fingers on the glass</td><td>False color or cloudiness</td><td>Rinse the vial with sample water; hold by the top</td></tr>
<tr><td>Reading color in poor light</td><td>Misjudged shade</td><td>Read against white in good light, or use a meter</td></tr>
</tbody></table></div>
{{key:Once a week, test the feed water with the same kit. It should read clearly positive. If it does not, the kit cannot be trusted for any of the week&rsquo;s results.}}
<p>Two kinds of test are common. Color-comparison kits and strips are quick and cheap but depend on your eyes. A handheld meter (colorimeter) reads the color electronically and gives a number; it needs its own zero check and periodic verification against a standard. Either is acceptable if it can read reliably at 0.1 mg/L.</p>
"""),
        ("replace", "Carbon replacement", "Replacing carbon and returning to service", """
<p>Carbon cannot be recharged in place. When the worker tank shows breakthrough, or at the interval the unit has set, the carbon is replaced. A common practice is to move the polisher into the worker position and put the fresh carbon in the polisher position, so the freshest carbon is always the last barrier.</p>
{{flow:From exhausted carbon to release|Plan::No patients on dialysis. Tell the charge nurse.|Replace::New, virgin carbon of the specified grade. Regenerated carbon is not used for dialysis.|Rinse::To drain until the water runs clear of black fines, by the supplier&rsquo;s method.|Check downstream::Inspect or change the fine filter.|Test::Total chlorine after each tank with the system running at working flow.|Record and release::Date, carbon type and batch, test results, name.}}
<p>Carbon is specified by grade. Dialysis systems commonly call for granular carbon with a high adsorption rating (an iodine number of 900 or more is a usual specification) and, where the feed contains chloramine, a type made for chloramine removal. Use what the system designer specified; cheaper substitutes can exhaust in weeks.[[iso23500_2]][[coulliette2013]]</p>
{{stop:If chlorine is above the limit after the second tank, no dialysis starts on this water. There is no workaround in the water room. The medical director decides what happens next.}}
"""),
        ("L", "02", "fine")],
    "debrief": ("L", "04"),
    "skills": ("L", "04"),
    "quiz_keep": [("02", [3, 4, 5, 6]), ("04", [0, 1, 2, 3])],
    "quiz": [
        ("A unit uses a free chlorine test. The utility switches to chloramine. What will the test show?",
         ["A high reading", "Little or nothing, even though chloramine is present", "The exact chloramine level", "Hardness"], 1,
         "A free chlorine test does not detect chloramine."),
        ("Why test the feed water with the same kit once a week?",
         ["To waste reagent", "To prove the kit can show a positive result", "To check hardness", "To cool the port"], 1,
         "A kit that cannot read positive on chlorinated feed water cannot be trusted."),
        ("After carbon replacement, what must be done before release?",
         ["Nothing", "Rinse until clear and test total chlorine after each tank at working flow", "Add salt", "Lower the pump pressure"], 1,
         "New carbon sheds fines and must be proven to remove chlorine."),
        ("Which carbon is not used for dialysis water treatment?",
         ["Virgin granular carbon", "Regenerated (reactivated) carbon", "Carbon of the specified grade", "Carbon made for chloramine removal"], 1,
         "Regenerated carbon may carry contaminants from its previous use."),
    ],
    "terms": [("Colorimeter", "A handheld meter that reads the color of a test sample and displays a number."),
              ("Iodine number", "A rating of how much a carbon can adsorb; higher means more capacity."),
              ("Carbon fines", "Fine black dust shed by new carbon.")],
    "readings": [("dialysis-water-treatment-systems.html", "Carbon sizing and the response to breakthrough.")],
}

NEW["05"] = {
    "image_alt": "A technician reading flow meters on a reverse osmosis unit.",
    "objectives": [
        "Explain how a reverse osmosis membrane separates product from reject water.",
        "Record the operating readings and calculate percent rejection and percent recovery.",
        "Interpret changes in readings and name the likely cause.",
        "Start up, shut down, and respond to alarms on the unit by procedure.",
    ],
    "big": """
{{plain:The reverse osmosis unit removes most of what is still dissolved in the water: salts, metals, and nearly all bacteria and endotoxin. It is a pump pushing water against a very fine membrane. You judge its health with a handful of readings, and its health changes slowly, so the skill is in comparing today with last month.}}
{{cards:Key terms for this module|Membrane::A rolled sheet with pores too small for most dissolved substances.|Product water::The clean water that passes through. Also called permeate.|Reject water::The concentrated stream carried away. Also called concentrate.|Percent rejection::How much of the dissolved salt the membrane stopped.|Percent recovery::How much of the feed became product.|Fouling::Dirt, organic matter, or bacteria coating the membrane.|Scaling::Mineral crust on the membrane.}}
""",
    "case": ("L", "03"),
    "sections": [("L", "03", "ro"),
        ("readings", "The readings", "The readings that matter and what moves them", """
<p>A typical unit shows these readings. Record all of them at the same time each day, with the system at steady running.</p>
<div class="table-wrap"><table>
<thead><tr><th>Reading</th><th>What it tells you</th><th>If it rises</th><th>If it falls</th></tr></thead>
<tbody>
<tr><td>Feed pressure (before the pump)</td><td>Whether pretreatment is supplying enough water</td><td>Rarely a problem</td><td>Clogged prefilter, low supply, or a tank in backwash</td></tr>
<tr><td>Pump (membrane) pressure</td><td>The push against the membrane</td><td>Membrane fouling or scaling, colder water, or a closed-down reject valve</td><td>Pump wear, a leak, or low feed</td></tr>
<tr><td>Product flow</td><td>How much clean water is made</td><td>Warmer water; or a damaged membrane letting too much through</td><td>Fouling, scaling, colder water, low pressure</td></tr>
<tr><td>Reject flow</td><td>How much water carries salts away</td><td>Less recovery; wastes water</td><td>Risk of scaling; check the reject valve setting</td></tr>
<tr><td>Feed conductivity</td><td>Mineral load coming in</td><td>Source change, softener passing brine</td><td>Source change</td></tr>
<tr><td>Product conductivity</td><td>Mineral load getting through</td><td>Membrane damage, a leaking seal, higher feed load, warmer water</td><td>Usually good; confirm the sensor is working</td></tr>
<tr><td>Feed temperature</td><td>Explains changes in flow</td><td>More flow, slightly lower rejection</td><td>Less flow</td></tr>
</tbody></table></div>
{{key:Always look at temperature before blaming the membrane. A cold morning lowers product flow on a perfectly healthy unit.}}
"""),
        ("L", "03", "numbers"),
        ("patterns", "Patterns", "Recognizing the pattern", """
<p>Single readings mislead. Patterns across readings point to the cause.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Most likely cause</th><th>What usually follows</th></tr></thead>
<tbody>
<tr><td>Product flow falling slowly, pump pressure rising, rejection steady</td><td>Fouling by particles or biological growth</td><td>Check prefilters and pretreatment; membrane cleaning by the supplier</td></tr>
<tr><td>Product flow falling, rejection falling</td><td>Scaling from hardness</td><td>Check softener performance; cleaning with a descaling agent by the supplier</td></tr>
<tr><td>Product flow rising, rejection falling</td><td>Membrane damage, classically from chlorine</td><td>Check chlorine logs; membrane replacement</td></tr>
<tr><td>Sudden jump in product conductivity after service</td><td>Seal or connector not seated</td><td>Call the service provider back</td></tr>
<tr><td>Everything changes together on one day</td><td>Feed water changed</td><td>Check the source; compare feed conductivity and temperature</td></tr>
</tbody></table></div>
<p>Membranes are cleaned or replaced by trained service staff using chemicals and procedures specific to the membrane. Your part is to notice early, report with figures, and make sure the cause upstream is fixed so the new membrane does not go the same way.</p>
"""),
        ("operate", "Operating the unit", "Start-up, shutdown, and alarms", """
{{flow:A routine start-up|Check pretreatment::Tanks in service, timers correct, valves in normal position.|Open the feed::Confirm feed pressure is adequate.|Start the unit::Many units flush to drain first; product is diverted until quality is acceptable.|Wait for steady readings::Do not test or record during the first minutes.|Record and compare::Readings against yesterday and last month.}}
<p>Many units flush themselves periodically when idle, to stop water stagnating against the membrane. A unit that sits switched off for days grows bacteria and may need disinfection before use: follow your procedure after any long shutdown.</p>
<div class="table-wrap"><table>
<thead><tr><th>Alarm</th><th>What the unit usually does</th><th>First checks</th></tr></thead>
<tbody>
<tr><td>Low feed pressure</td><td>Stops the pump to protect it</td><td>Supply, prefilter pressure drop, a tank in backwash or regeneration, closed valve</td></tr>
<tr><td>High product conductivity</td><td>Diverts product to drain or alarms</td><td>Feed conductivity, softener status, recent service, rejection trend</td></tr>
<tr><td>High temperature</td><td>Stops to protect the membrane</td><td>Feed temperature; a pump running against a closed valve</td></tr>
<tr><td>Low product flow or pressure in the loop</td><td>Machines alarm for low water</td><td>Demand at that moment, temperature, product flow trend</td></tr>
<tr><td>Motor overload</td><td>Pump trips</td><td>Do not reset repeatedly; report for electrical check</td></tr>
</tbody></table></div>
{{stop:Any alarm that affects water quality or supply is reported to the charge nurse at once, with which stations are running. Resetting an alarm is not a response.}}
{{fig:wts_dualpass|In a dual-pass system each pass has its own readings. Record both, and calculate rejection for each.}}
"""),
    ],
    "debrief": ("L", "03"),
    "skills": {"title": "Reverse osmosis readings, calculations, and alarm response",
        "intro": "Materials: the unit&rsquo;s display and gauges, the log with at least one month of readings, a calculator, and the alarm list from the manual.",
        "items": [("Confirms pretreatment status and valve positions before start-up.", False),
                  ("Waits for steady running before recording.", False),
                  ("Records all pressures, flows, conductivities, and temperature with units.", False),
                  ("Calculates percent rejection and percent recovery correctly.", True),
                  ("Compares with last month and describes any pattern and its likely cause.", False),
                  ("States the action for each alarm on the unit&rsquo;s alarm list.", True),
                  ("Reports a simulated high product conductivity alarm to the charge nurse with stations affected.", True),
                  ("Explains why conductivity does not replace chlorine testing or cultures.", True)],
        "placement": "Plot one month of product flow, pump pressure, product conductivity, and temperature and present the pattern to your preceptor."},
    "quiz_keep": [("03", [0, 1, 2, 3, 4, 7])],
    "quiz": [
        ("Product flow is rising and rejection is falling. What is the most likely cause?",
         ["Fouling", "Membrane damage, classically from chlorine", "Cold water", "A clogged prefilter"], 1,
         "A damaged membrane lets more water and more salt through."),
        ("The low feed pressure alarm stops the pump. What is checked first?",
         ["The membrane", "Supply, prefilter, and whether a tank is in backwash or regeneration", "The loop return", "The storage tank lid"], 1,
         "Low feed pressure originates upstream of the pump."),
    ],
    "terms": [("Permeate", "Another word for product water."), ("Concentrate", "Another word for reject water."),
              ("Dual pass", "Two sets of membranes in series; product from the first feeds the second."),
              ("Microsiemens per centimeter", "The unit of conductivity for very pure water.")],
    "readings": [("dialysis-water-treatment-systems.html", "Single- and dual-pass design and capacity.")],
    "calcs": ["calc-ro-recovery-dualpass.html", "calc-dialysis-water-reuse.html"],
}

NEW["06"] = {
    "image_alt": "A technician tracing loop pipework to a wall outlet at a dialysis station.",
    "objectives": [
        "Describe direct-feed and tank-fed distribution and the features that discourage bacterial growth.",
        "Identify dead legs, unsuitable materials, and stagnant points.",
        "Explain the role, monitoring, and replacement of ultraviolet lamps and ultrafilters.",
        "Include machine connection hoses and outlets in monitoring and disinfection.",
    ],
    "big": """
{{plain:After the reverse osmosis unit the water is at its cleanest. Everything from that point to the machine can only make it dirtier. The loop&rsquo;s job is to deliver that water to every station without giving bacteria a place to settle: keep it moving, keep the pipe smooth, keep branches short, and clean it before counts rise.}}
{{cards:Key terms for this module|Distribution loop::Pipework that carries product water past every station and back.|Direct feed::The reverse osmosis unit feeds the loop with no storage tank.|Dead leg::A branch where water does not circulate.|Biofilm::Bacteria attached to a surface inside a protective slime.|Ultraviolet lamp::A lamp that kills bacteria in passing water.|Ultrafilter::A filter fine enough to hold back bacteria and endotoxin.|Point of use::At the machine.}}
""",
    "case": {"title": "The station nobody uses", "html": """
<p>Station 9 has been out of use for five months since its machine was sent for repair. Its wall outlet is still connected to the loop by a meter of hose. Monthly cultures at the loop return have risen from under 5 to 38 CFU/mL, while the sample at the loop start remains under 5.</p>
""", "questions": ["What does a clean loop start and a rising loop return tell you?",
                  "Why is station 9 a suspect?",
                  "What would you report, and what might be done?"]},
    "sections": [("L", "03", "loop"),
        ("designs", "Two designs", "Direct feed and tank-fed systems", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Direct feed</th><th>Tank-fed</th></tr></thead>
<tbody>
<tr><td>How it works</td><td>The reverse osmosis unit supplies the loop directly; unused water returns to the unit&rsquo;s inlet</td><td>Product water fills a storage tank; a pump circulates it around the loop and back to the tank</td></tr>
<tr><td>Strength</td><td>No tank for bacteria to grow in</td><td>A reserve of water for peak demand and short outages</td></tr>
<tr><td>Weakness</td><td>No reserve; the unit must meet peak demand by itself</td><td>The tank is the commonest site of contamination</td></tr>
<tr><td>Extra equipment</td><td>Usually none</td><td>Ultraviolet lamp and ultrafilter after the tank; filtered air vent</td></tr>
</tbody></table></div>
{{cards:A storage tank that stays clean|Sized modestly::Large tanks let water sit.|Sloped or conical base::Drains completely from the lowest point.|Tight lid::Nothing falls in.|Filtered air vent::Air entering as the level drops passes a fine filter.|Spray device::Disinfectant reaches every internal surface.|No sight tubes or dead pockets::Nowhere for water to stand.}}
<p>Pipe material matters too. Loops are built from materials that do not shed chemicals into very pure water and have smooth joints. Copper, brass, galvanized steel, and aluminum are never used in contact with product water, because pure water dissolves them.[[iso23500_2]]</p>
"""),
        ("flow", "Keeping water moving", "Keeping water moving", """
<p>Bacteria attach where water is slow. Designers therefore aim for a minimum speed in the loop at all times, including at peak demand when the stations are drawing water off. Commonly quoted design guidance is about 0.9 meters per second in a tank-fed loop and about 0.5 meters per second in a direct-feed loop at the end of the loop; use your designer&rsquo;s figures.[[iso23500_1]]</p>
<p>You cannot see velocity, but you can watch its signs:</p>
<div class="table-wrap"><table>
<thead><tr><th>What to record</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Loop supply pressure and loop return pressure</td><td>A falling return pressure means more water is being drawn off, or the pump is weakening</td></tr>
<tr><td>Return flow, if a meter is fitted</td><td>Shows water is actually coming back</td></tr>
<tr><td>Whether the loop runs overnight and on days off</td><td>A loop that is switched off is a loop that is growing biofilm</td></tr>
<tr><td>Any closed valve or unused outlet</td><td>Each one is a possible dead leg</td></tr>
</tbody></table></div>
{{fig:wts_isolation}}
"""),
        ("uvuf", "Lamps and filters", "Ultraviolet lamps and ultrafilters", """
<p>An ultraviolet lamp shines light at a wavelength of 254 nanometers through the passing water. It damages bacteria so they cannot multiply. It does not remove them, and killing bacteria releases endotoxin, so a lamp is followed by an ultrafilter.</p>
<div class="table-wrap"><table>
<thead><tr><th>Component</th><th>How it fails quietly</th><th>How you catch it</th></tr></thead>
<tbody>
<tr><td>Ultraviolet lamp</td><td>The lamp still glows but its output has fallen with age; the quartz sleeve is coated so light is blocked</td><td>Intensity meter reading if fitted; lamp hours against the maker&rsquo;s replacement interval; sleeve cleaning on schedule</td></tr>
<tr><td>Ultrafilter</td><td>Plugs gradually; or is damaged and passes bacteria</td><td>Pressure drop across it; cultures and endotoxin after it; replacement on schedule</td></tr>
<tr><td>Tank vent filter</td><td>Becomes wet or blocked</td><td>Scheduled replacement; inspect when the tank is serviced</td></tr>
</tbody></table></div>
{{fig:wts_pou}}
<p>Many machines also carry their own filter for dialysis fluid. Those belong to the machine and are covered in the Biomedical Technician track, but the principle is the same: a filter has a life, and the date is written on it.</p>
"""),
        ("hoses", "Outlets and hoses", "The last meter: outlets and machine hoses", """
<p>The hose from the wall outlet to the machine is the part of the water path most often forgotten. It is flexible, it is warm from the machine, and it may sit full of still water all night.</p>
{{cards:Rules for outlets and hoses|Short::As short as the station allows.|Included in disinfection::Loop disinfection runs with machines connected, or hoses are disinfected with the machine, by your procedure.|Replaced on schedule::Old hoses grow biofilm that disinfection cannot remove.|No spare coils::Extra hose is extra stagnant volume.|Unused stations::Disconnected at the outlet, and the outlet flushed and included in disinfection.|Sampled::Dialysis fluid from machines is cultured in rotation.}}
{{key:If loop cultures are clean but machine cultures are not, look at the hoses and the machines.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> A clean loop start with a rising loop return means bacteria are being added along the loop, not arriving from the reverse osmosis unit. Station 9 is a dead leg: a meter of hose and an outlet holding still water for five months, shedding into the passing flow. Report the trend and the suspect to the chief technician and medical director now, while the count is under the action level. Likely actions are to disconnect the hose, flush and disinfect the outlet, bring forward the loop disinfection, and resample. Then walk the whole loop for other unused branches. The lesson is the one from Module 1: the count had not crossed any limit, and that is exactly when acting is cheap.</p>
"""],
    "skills": {"title": "Loop walk-down and dead-leg hunt",
        "intro": "Materials: the loop drawing, a flashlight, the log, and the lamp and filter records.",
        "items": [("States whether the system is direct feed or tank-fed and traces the loop from supply to return.", False),
                  ("Records loop supply and return pressures and compares with previous readings.", False),
                  ("Confirms the loop runs continuously, including overnight.", True),
                  ("Identifies every unused outlet, capped branch, and spare hose coil and reports them.", True),
                  ("Checks ultraviolet lamp hours or intensity and the date of the last sleeve cleaning.", False),
                  ("Reads the pressure drop across the ultrafilter and its replacement date.", False),
                  ("Inspects the storage tank lid and vent filter, if a tank is fitted.", False),
                  ("Explains how machine hoses are disinfected and when they are replaced in this unit.", True)],
        "placement": "Walk the full loop with the drawing and mark on it every difference between the drawing and what is installed."},
    "quiz_keep": [("03", [5, 6])],
    "quiz": [
        ("Cultures are under 5 CFU/mL at the loop start and 38 CFU/mL at the loop return. What does this suggest?",
         ["The reverse osmosis unit is failing", "Bacteria are being added along the loop", "The laboratory mixed up samples", "The softener needs salt"], 1,
         "A clean start and a dirty return point to a source within the loop, such as a dead leg."),
        ("What is the main weakness of a tank-fed system?",
         ["No reserve of water", "The tank is a common site of contamination", "It cannot be disinfected", "It needs no pump"], 1,
         "Stored water gives bacteria time and surfaces to grow on."),
        ("Why is an ultrafilter placed after an ultraviolet lamp?",
         ["To warm the water", "To remove dead bacteria and the endotoxin they release", "To add chlorine", "To soften the water"], 1,
         "The lamp kills bacteria but does not remove them or their fragments."),
        ("An ultraviolet lamp is glowing. Does that prove it is working?",
         ["Yes", "No; output falls with age and a coated sleeve blocks light", "Only at night", "Only in direct-feed systems"], 1,
         "Lamp hours, intensity readings, and sleeve cleaning show whether it is effective."),
        ("Which material must not contact product water?",
         ["The loop material specified by the designer", "Copper or brass", "Approved flexible hose", "Stainless steel of the specified grade"], 1,
         "Very pure water dissolves copper, brass, zinc, and aluminum into the water."),
        ("Loop cultures are clean, but dialysis fluid from two machines is above the action level. Where do you look?",
         ["The feed water", "The connection hoses, the machines, and the bicarbonate", "The softener", "The carbon tanks"], 1,
         "The contamination is entering after the loop."),
    ],
    "terms": [("Quartz sleeve", "The clear tube around an ultraviolet lamp; it must be clean for light to pass."),
              ("Nanometer", "One billionth of a meter; used for wavelengths of light."),
              ("Loop return", "The end of the loop, where water comes back to the tank or the reverse osmosis unit.")],
    "readings": [("dialysis-water-treatment-systems.html", "Loop layouts, isolation bays, and point-of-use filtration.")],
}
