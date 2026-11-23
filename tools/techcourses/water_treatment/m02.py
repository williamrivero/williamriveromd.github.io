# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "Filter housings, a softener, and carbon tanks in a dialysis water room.",
    "objectives": [
        "Describe the job of each pretreatment stage and the order in which water passes through them.",
        "Use the pressure drop across a filter to decide when it needs attention.",
        "Explain how a softener works and why regeneration must not happen during treatment hours.",
        "Explain how carbon tanks remove chlorine, what empty-bed contact time means, and why two tanks are used in series.",
    ],
    "big": """
{{plain:Pretreatment is everything before the reverse osmosis unit. Think of it as a set of bodyguards for the membrane. The sediment filter stops dirt, the softener stops scale, and the carbon tanks stop chlorine. The carbon tanks have a second job that matters even more: they are the only reliable barrier between chloramine and the patient.}}
{{flow:Water through pretreatment (a common order; yours may differ)|Feed water::From the city, a well, or a tanker. A booster pump keeps pressure steady.|Sediment filter::Traps sand, rust, and silt.|Softener::Swaps calcium and magnesium for sodium.|Carbon tanks::Two in series remove chlorine and chloramine.|Fine filter::Catches carbon dust before the membrane.|To reverse osmosis::Clean, soft, chlorine-free water.}}
{{cards:Key terms for this module|Pressure drop::The difference between the pressure before and after a filter. Also called delta P. It rises as the filter clogs.|Backwash::Running water backward through a tank to lift and rinse the bed.|Regeneration::Recharging a softener with salt water (brine).|Empty-bed contact time::How many minutes water spends in the carbon tank. More time removes more chlorine.|Worker and polisher::The first and second carbon tanks. The worker does most of the removal; the polisher is the backup.}}
""",
    "case": {
        "title": "The softener that regenerated at noon",
        "html": """
<p>After a power interruption overnight, the softener&rsquo;s timer is several hours wrong. At 12:10, in the middle of the second shift, the softener starts to regenerate. A few minutes later two machines alarm for high conductivity, and the reverse osmosis unit shows a rising product conductivity.</p>
""",
        "questions": ["What is the softener sending downstream during regeneration?",
                      "What do you do at the softener, and whom do you tell?",
                      "What daily check would have prevented this?"],
    },
    "sections": [
        ("filters", "Filters", "Sediment filters and the pressure drop", """
{{fig:wts_train|Find the pretreatment stages on the left of the treatment train. The order of softener and carbon tanks differs between installations; follow your own system drawing.}}
<p>A sediment filter is a tank of layered sand and gravel, or a cartridge, that traps particles. As it fills with dirt, water has a harder time getting through, and the pressure after the filter falls. Every filter therefore has a gauge before it and a gauge after it.</p>
{{formula:<strong>Pressure drop</strong> = pressure before the filter &minus; pressure after the filter.<br>Example: 60 psi before and 52 psi after gives a drop of 8 psi. If the drop was 3 psi when the filter was new, it is clogging.}}
<p>Your unit&rsquo;s procedure states the pressure drop at which a tank is backwashed or a cartridge is changed. Record both gauges every day: one reading tells you little, but a row of readings shows the filter loading up.</p>
"""),
        ("softener", "Softener", "The softener and its brine tank", """
<p>Hard water contains calcium and magnesium. On a reverse osmosis membrane these form scale, like the crust inside a kettle, and block it. A softener is a tank of resin beads that hold sodium. As hard water passes, the beads grab calcium and magnesium and release sodium in exchange.</p>
{{flow:The softener cycle|Service::Hard water in, soft water out. The resin slowly fills with calcium and magnesium.|Backwash::Water runs upward to loosen and rinse the bed.|Brine draw::Strong salt water from the brine tank pushes calcium and magnesium off the resin.|Rinse::Excess salt is flushed to drain.|Back in service::The resin is recharged with sodium.}}
<p>During regeneration the softener is off line and salty water is flowing to drain. If the valve fails or the timer is wrong, that brine can go downstream. For this reason softeners are set to regenerate when no patient is on dialysis, and the timer is checked every day.</p>
<p>Softener performance is checked with a hardness test on water leaving the softener, usually at the end of the treatment day when the resin is most used up. Many units use a limit of about 1 grain per gallon (17 mg/L as calcium carbonate); work to the limit in your procedure. Check also that the brine tank holds enough salt and that the salt has not formed a hard bridge above the water.</p>
{{key:Check the softener clock every morning, and after every power interruption.}}
"""),
        ("carbon", "Carbon tanks", "Carbon tanks: the chlorine barrier", """
<p>Activated carbon is charcoal processed to have an enormous internal surface. Chlorine and chloramine are removed as water passes over that surface. Removal takes time, so the water must stay in contact with the carbon long enough.</p>
{{formula:<strong>Empty-bed contact time (minutes)</strong> = volume of the carbon bed &divide; water flow rate.<br>Example: a tank holding 300 liters of carbon with water flowing at 30 liters per minute gives 300 &divide; 30 = 10 minutes.}}
<p>Guidance commonly calls for two carbon tanks in series with a total contact time of at least 10 minutes at the highest flow, about 5 minutes in each.[[iso23500_1]][[coulliette2013]] Chloramine is harder to remove than free chlorine and needs the full contact time.</p>
{{cards:Why two tanks in series|The worker::The first tank removes nearly all the chlorine and is used up first.|The sample port between them::Testing here shows when the worker is becoming exhausted.|The polisher::The second tank protects patients while the worker is replaced.|Breakthrough::Chlorine passing through a tank. After the worker it is a warning; after the polisher it is a stop.}}
<p>Carbon tanks are backwashed to keep water from cutting channels through the bed, but backwashing does not restore exhausted carbon. Exhausted carbon is replaced. Carbon is also a good home for bacteria, which is one reason stages after it must control microbes.</p>
{{stop:Total chlorine above the limit after the second carbon tank means dialysis on that water stops until it is corrected and an authorized person releases the system.}}
"""),
        ("fine", "After carbon", "The fine filter and the handover to reverse osmosis", """
<p>A cartridge filter of about 5 micrometers usually sits after the carbon tanks. It catches carbon dust and resin fragments that would otherwise plug the membrane. Record its pressure drop and change it on schedule or when the drop reaches the stated value. A new cartridge that clogs within days is a message: something upstream is shedding.</p>
{{fig:wts_source}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> A softener that regenerates during treatment can send brine downstream, which raises the salt load on the reverse osmosis membrane and the conductivity of the product water. Follow the unit&rsquo;s procedure to stop the regeneration or bypass the softener, tell the charge nurse immediately which machines alarmed and why, and do not return the softener to service until it has completed a full rinse and the hardness and conductivity results are acceptable. The nurse decides what happens with connected patients. The check that prevents this is simple: compare the softener clock with the real time every morning and after every power interruption, and record it.</p>
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
