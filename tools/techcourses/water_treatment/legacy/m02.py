# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "Filter housings, a softener, and carbon tanks in a dialysis water room.",
    "objectives": [
        "Describe what each pretreatment stage does and the order in which water passes through them.",
        "Use the pressure drop across a filter to decide when it needs attention.",
        "Explain how a softener works, and why it must never regenerate during treatment hours.",
        "Explain how carbon tanks remove chlorine, what empty-bed contact time means, and why two tanks are placed in series.",
    ],
    "big": """
{{plain:Think of a security detail walking a VIP through a crowded mall. One guard clears the path of obstacles, one keeps the crowd from pressing in, and one checks every hand that reaches out. Pretreatment is that detail for the reverse osmosis membrane. The sediment filter stops dirt, the softener stops scale, and the carbon tanks stop chlorine.}}
<p>The picture has a limit. A bodyguard protects only the VIP. The carbon tanks protect the membrane, but they also do a second job that matters even more: they are the only reliable barrier between chloramine and the patient. Nothing downstream will catch what the carbon lets through.</p>
{{flow:Water through pretreatment (a common order; yours may differ)|Feed water::Comes from the city, a well, or a tanker. A booster pump keeps the pressure steady.|Sediment filter::Traps sand, rust, and silt.|Softener::Exchanges calcium and magnesium for sodium.|Carbon tanks::Two in series remove chlorine and chloramine.|Fine filter::Catches carbon dust before it reaches the membrane.|To reverse osmosis::Clean, soft water with no chlorine.}}
{{cards:Key terms for this module|Pressure drop::The pressure before a filter minus the pressure after it. Also called delta P. It rises as the filter clogs.|Backwash::Running water backward, upward through a tank, to lift and rinse the bed.|Regeneration::Recharging a softener with strong salt water (brine).|Empty-bed contact time::The number of minutes water spends in the carbon tank. More time removes more chlorine.|Worker and polisher::The first and second carbon tanks. The worker does most of the removal; the polisher is the backup.}}
""",
    "case": {
        "title": "The softener that regenerated at noon",
        "html": """
<p>A brownout cut the power to the clinic for about two hours on Monday night. Nobody reset the softener&rsquo;s timer, and it is now several hours wrong. On Tuesday at 12:10, in the middle of the second shift, the softener starts to regenerate.</p>
<p>A few minutes later the machines at stations 4 and 7 alarm for high conductivity. The charge nurse, Mr. Paolo Aquino, calls the water room. The technician, Ms. Rhea Domingo, 27, finds the reverse osmosis display showing product conductivity rising with each reading, and she can hear the softener valve cycling.</p>
""",
        "questions": ["What is the softener sending downstream during regeneration?",
                      "What do you do at the softener, and whom do you tell?",
                      "What daily check would have prevented this?"],
    },
    "sections": [
        ("filters", "Filters", "Sediment filters and the pressure drop", """
{{fig:wts_train|Find the pretreatment stages on the left of the treatment train. The order of the softener and the carbon tanks differs between installations; follow your own system drawing.}}
<p>A sediment filter is a tank of layered sand and gravel, or a cartridge in a housing, that traps particles. As it fills with dirt, water has a harder time getting through, so the pressure after the filter falls below the pressure before it. That is why every filter has two gauges, one before and one after.</p>
{{formula:<strong>Pressure drop</strong> = pressure before the filter &minus; pressure after the filter.<br>Example: 60 psi before and 52 psi after gives a drop of 8 psi. If the drop was 3 psi when the filter was new, it is clogging.}}
<p>Your unit&rsquo;s procedure states the pressure drop at which a tank is backwashed or a cartridge is changed. Record both gauges every day. One reading tells you little. A row of readings shows you the filter loading up, day by day, before it starves the system of water.</p>
"""),
        ("softener", "Softener", "The softener and its brine tank", """
<p>Hard water carries calcium and magnesium. On a reverse osmosis membrane they form scale, like the white crust inside an old kettle, and the scale blocks the membrane. A softener is a tank of resin beads loaded with sodium. As hard water flows past, the beads take up calcium and magnesium and release sodium in their place.</p>
{{flow:The softener cycle|Service::Hard water in, soft water out. The resin slowly fills with calcium and magnesium.|Backwash::Water runs upward to loosen and rinse the bed.|Brine draw::Strong salt water from the brine tank pushes calcium and magnesium off the resin.|Rinse::The extra salt is flushed to drain.|Back in service::The resin is recharged with sodium.}}
<p>During regeneration the softener is off line and salty water is flowing to drain. If the valve fails or the timer is wrong, that brine can travel downstream instead. For this reason a softener is set to regenerate only when no patient is on dialysis, and its timer is checked every day.</p>
<p>You check the softener&rsquo;s work with a hardness test on the water leaving it, usually at the end of the treatment day, when the resin is most used up. Many units use a limit of about 1 grain per gallon (17 mg/L as calcium carbonate); work to the limit in your own procedure. Check also that the brine tank holds enough salt, and that the salt has not formed a hard crust, a bridge, above the water.</p>
{{key:Check the softener clock every morning, and after every power interruption.}}
"""),
        ("carbon", "Carbon tanks", "Carbon tanks: the chlorine barrier", """
<p>Activated carbon is charcoal processed so that each grain has an enormous internal surface. Chlorine and chloramine are taken out of the water as it passes over that surface. The removal takes time, so the water must stay in contact with the carbon long enough for it to finish.</p>
{{formula:<strong>Empty-bed contact time (minutes)</strong> = volume of the carbon bed &divide; water flow rate.<br>Example: a tank holding 300 liters of carbon with water flowing at 30 liters per minute gives 300 &divide; 30 = 10 minutes.}}
<p>Guidance commonly calls for two carbon tanks in series with a total contact time of at least 10 minutes at the highest flow, about 5 minutes in each.[[iso23500_1]][[coulliette2013]] Chloramine is harder to remove than free chlorine and needs the full contact time. The practical point is that contact time is set by the busiest moment of the day, not the average one.</p>
{{cards:Why two tanks in series|The worker::The first tank removes nearly all the chlorine, and it is used up first.|The sample port between them::Testing here tells you when the worker is becoming exhausted.|The polisher::The second tank protects patients while the worker is replaced.|Breakthrough::Chlorine passing through a tank. After the worker it is a warning; after the polisher it is a stop.}}
<p>Carbon tanks are backwashed so that water does not cut channels through the bed. Backwashing does not restore exhausted carbon; exhausted carbon is replaced. Carbon is also a comfortable home for bacteria, because it has removed the chlorine that would have kept them down. That is one reason the stages after it must control microbes.</p>
{{stop:Total chlorine above the limit after the second carbon tank means dialysis on that water stops until it is corrected and an authorized person releases the system.}}
"""),
        ("fine", "After carbon", "The fine filter and the handover to reverse osmosis", """
<p>A cartridge filter of about 5 micrometers usually sits after the carbon tanks. It catches carbon dust and resin fragments that would otherwise plug the membrane. Record its pressure drop, and change it on schedule or when the drop reaches the stated value. A new cartridge that clogs within days is telling you something: a stage upstream is shedding, and that stage needs to be found.</p>
{{fig:wts_source}}
"""),
    ],
    "debrief": ["""
<p><strong>What the softener is sending downstream.</strong> Brine. During regeneration the softener flushes strong salt water to drain, and with the timer wrong it is doing so while the system is supplying patients. Salt that slips downstream raises the load on the reverse osmosis membrane and the conductivity of the product water, which is what the machines at stations 4 and 7 detected.</p>
<p><strong>What to do at the softener, and whom to tell.</strong> Follow the unit&rsquo;s procedure to stop the regeneration or bypass the softener. Tell Mr. Aquino at once which machines alarmed and why. He decides what happens with the connected patients; that decision is not yours. Do not return the softener to service until it has finished a full rinse and the hardness and conductivity results are acceptable. Record the times, the readings, and whom you told.</p>
<p><strong>The check that prevents it.</strong> Compare the softener clock with the real time every morning and after every power interruption, and write it in the log. A two-minute check would have kept this regeneration in the night where it belongs.</p>
"""],
    "skills": {
        "title": "Pretreatment daily round",
        "intro": "Materials: the water room log, a hardness test kit, and the system drawing.",
        "items": [("Reads and records the pressure before and after each filter and calculates the pressure drop.", False),
                  ("Compares each pressure drop with the unit&rsquo;s stated limit and with the previous days.", False),
                  ("Checks the softener clock against the real time and corrects or reports a difference.", True),
                  ("Checks the salt level in the brine tank and looks for a salt bridge.", False),
                  ("Performs a hardness test at the correct port and records the result with units.", False),
                  ("Identifies the worker tank, the polisher tank, and the sample port for each.", True),
                  ("States what to do if chlorine is found after the second carbon tank.", True)],
        "placement": "Calculate the empty-bed contact time of your unit&rsquo;s carbon tanks from the bed volume and the highest flow, with your preceptor checking the figures.",
    },
    "quiz": [
        ("A filter reads 58 psi before and 46 psi after. What is the pressure drop?",
         ["4 psi", "12 psi", "46 psi", "104 psi"], 1, "58 minus 46 is 12 psi. Compare it with the unit&rsquo;s limit and with earlier readings."),
        ("What does a softener remove?",
         ["Chlorine", "Bacteria", "Calcium and magnesium", "Sodium"], 2, "The resin exchanges calcium and magnesium for sodium, protecting the membrane from scale."),
        ("Why are softeners set to regenerate outside treatment hours?",
         ["Regeneration is noisy", "Brine could reach the machines and the softener is off line during the cycle", "Salt is cheaper at night", "Carbon tanks need the water"], 1,
         "A valve or timer fault during regeneration can send salt water downstream."),
        ("A carbon bed of 240 liters receives 40 liters per minute. What is the empty-bed contact time?",
         ["4 minutes", "6 minutes", "10 minutes", "16 minutes"], 1, "240 divided by 40 is 6 minutes."),
        ("Chlorine is detected after the first carbon tank but not after the second. What does this mean?",
         ["The system has failed and all treatment stops", "The worker tank is becoming exhausted; the polisher is protecting patients, and the unit&rsquo;s response plan starts", "The test kit is faulty", "The softener needs salt"], 1,
         "Breakthrough after the worker is a warning to increase testing and arrange replacement as the procedure states."),
        ("Does backwashing restore exhausted carbon?",
         ["Yes, completely", "Yes, if done twice", "No; exhausted carbon must be replaced", "Only with hot water"], 2,
         "Backwashing prevents channeling but does not renew the carbon&rsquo;s capacity."),
        ("A new 5-micrometer cartridge clogs in three days. What is the best interpretation?",
         ["Cartridges are low quality", "Something upstream, such as the carbon or the softener, is shedding particles", "The reverse osmosis unit is too strong", "Nothing; this is normal"], 1,
         "Rapid clogging points to a problem upstream that needs to be found."),
        ("After a power interruption, which softener check comes first?",
         ["Salt color", "The clock and regeneration setting", "Tank paint", "Resin age"], 1, "A wrong clock moves regeneration into treatment hours."),
    ],
    "terms": [("Resin", "Small plastic beads in a softener that hold sodium and exchange it for calcium and magnesium."),
              ("Brine", "Strong salt water used to recharge the softener."),
              ("Channeling", "Water cutting a path through a bed so that most of the bed is bypassed."),
              ("Micrometer", "One thousandth of a millimeter. Also called a micron.")],
    "readings": [("dialysis-water-treatment-systems.html", "Pretreatment design for city, well, and delivered water.")],
}
