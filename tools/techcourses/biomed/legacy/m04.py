# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician comparing a reference meter with a dialysis machine display during maintenance.",
    "objectives": [
        "Distinguish preventive maintenance, corrective maintenance, and performance verification.",
        "Explain what calibration is and why the reference instrument must itself be calibrated.",
        "Plan a maintenance schedule from the manufacturer&rsquo;s requirements and the unit&rsquo;s workload.",
        "Write a service record that is complete and traceable.",
    ],
    "big": """
{{plain:Picture a fish vendor at the palengke. The spring in her old scale has slowly tired, and every kilo she weighs is now a little light. Nobody notices, because the needle still swings. Then a buyer carries his fish to the market&rsquo;s public scale, and the difference shows at once. A dialysis machine ages the same way: sensors drift, pumps wear, and seals harden, slowly and without any alarm. Preventive maintenance is replacing and checking parts on a schedule, before they fail. Calibration is the trip to the public scale: you compare what the machine says with an instrument you trust, and you correct the difference.}}
<p>The picture has a limit. A light kilo costs a buyer a few pesos. A machine that reads wrong changes what reaches every patient connected to it, at every session, until someone checks. And the public scale must itself be checked, or it misleads everyone who trusts it. Maintenance and calibration are only as good as the schedule you keep and the record you leave.</p>
{{cards:Three kinds of work|Preventive maintenance::Scheduled replacement of wearing parts, cleaning, and checks, done whether or not there is a fault.|Corrective maintenance::Repair after a fault.|Performance verification::Measuring what the machine does against known values, and calibrating if it is outside tolerance.}}
{{cards:Key terms for this module|Calibration::Comparing a reading with a trusted reference and adjusting to match.|Tolerance::The allowed difference between the reading and the true value.|Reference instrument::A meter of known accuracy used to check the machine.|Traceable::Linked by documented calibrations back to a national or international standard.|As found, as left::The reading before adjustment and the reading after.|Operating hours::The machine&rsquo;s running-time counter, often used to schedule maintenance.}}
""",
    "case": {
        "title": "The meter nobody checked",
        "html": """
<p>It is Wednesday, just after one in the afternoon. Your center calibrates dialysate conductivity on all twelve machines every six months, using one handheld reference meter. The chief technician, Mr. Ramon Cruz, finished the last round two weeks ago.</p>
<p>A visiting service engineer, Mr. Danilo Reyes, 46, borrows the meter and shows you its label. The meter&rsquo;s own calibration certificate expired fourteen months ago. He checks it in fresh standard solution. The meter reads 3 percent low. On the floor, the nurses are connecting the afternoon shift.</p>
""",
        "questions": ["What does a meter that reads low mean for the twelve machines?",
                      "What do you do first, and whom do you tell today?",
                      "What control would have stopped the expired meter from being used?"],
    },
    "sections": [
        ("program", "The program", "Building a maintenance program", """
<p>The World Health Organization describes a maintenance program as three linked parts: an inventory of every device, a schedule of inspection and preventive maintenance, and a system for corrective maintenance, all supported by records.[[who_maint]] The inventory tells you what you are responsible for, the schedule tells you when each item is due, and the records tie them together. For a dialysis machine, the content of each visit comes from the manufacturer: which parts are replaced at which interval, which checks are done, and which tests follow.</p>
{{flow:From manual to calendar|List every machine::Model, serial number, location, and assignment.|Read the schedule::Intervals by months or operating hours, whichever comes first.|Spread the work::Stagger visits so that only a few machines are out at a time.|Stock the kits::Order maintenance kits and common spares ahead.|Do and record::Complete each visit by the checklist.|Review::Track what is overdue, and why.}}
<p>Do the arithmetic. A center with twelve machines on a six-month interval has twenty-four visits a year, about one every two weeks. Planned that way, maintenance never competes with a full treatment schedule. Left until inspection month, it competes with every shift.</p>
{{key:An overdue preventive maintenance visit is a reportable risk, not an administrative detail. When one is overdue, tell the chief technician and the charge nurse, and record the reason.}}
"""),
        ("calibration", "Calibration", "What calibration is", """
<p>A drifting sensor gives no warning. The number on the screen looks just as confident when it is wrong. Calibration brings that number back to the truth, one parameter at a time, in a fixed order.</p>
{{flow:Calibrating one parameter|Stabilize::Let the machine reach steady operation.|Measure as found::Read the machine and the reference at the same point and time.|Compare::Is the difference within the manual&rsquo;s tolerance?|Adjust::If not, adjust by the manual&rsquo;s procedure.|Measure as left::Read both again and confirm.|Record::Both sets of readings and the reference meter&rsquo;s identity.}}
<div class="table-wrap"><table>
<thead><tr><th>Parameter</th><th>Typical reference</th><th>Why it matters to the patient</th></tr></thead>
<tbody>
<tr><td>Dialysate conductivity</td><td>Calibrated conductivity meter</td><td>The patient receives the wrong amount of sodium and other salts</td></tr>
<tr><td>Dialysate temperature</td><td>Calibrated thermometer</td><td>Chilling if too cold, or damage to red cells if too hot</td></tr>
<tr><td>Arterial and venous pressure</td><td>Calibrated pressure meter</td><td>Alarms that are missed, or alarms that sound for nothing</td></tr>
<tr><td>Dialysate flow and blood pump speed</td><td>Measuring cylinder and timer, or flow meter</td><td>Less blood cleaning than prescribed</td></tr>
<tr><td>Ultrafiltration volume</td><td>Measuring cylinder or calibrated scale</td><td>Too much or too little fluid removed</td></tr>
</tbody></table></div>
<p>Notice the order: you read the machine before you touch it. The &ldquo;as found&rdquo; value is not paperwork for its own sake. If a machine was far out of tolerance when you found it, patients treated since the last visit may have been affected, and the clinical team needs to know. Once you adjust, that evidence is gone.</p>
{{fig:hd_params|Each prescribed setting is only delivered if the machine&rsquo;s sensors and pumps are accurate. Calibration connects the prescription to what the patient actually receives.}}
"""),
        ("reference", "Reference instruments", "Who checks the checker?", """
<p>Calibration moves the machine toward the reference. If the reference is wrong, you move every machine toward the same wrong value, and they then agree with each other perfectly. Nothing in the unit will reveal it.</p>
<p>Reference instruments therefore have their own calibration, done by an accredited laboratory or the manufacturer at a stated interval, with a certificate that links them to national standards. This chain is called traceability.</p>
{{cards:Rules for test equipment|Label::Each instrument carries its identity and its calibration due date.|Check before use::Never use an instrument past its due date.|Verify between calibrations::For example, check a conductivity meter in standard solution.|Record which instrument::Write it on every service record.|If one is found wrong::Review every machine it was used on since it was last known to be good.}}
"""),
        ("records", "Service records", "A service record that stands up", """
{{cards:What every service record contains|The machine::Model, serial number, asset number, location, operating hours.|The reason::Scheduled visit or reported fault, with the exact message.|The findings::As-found readings and what was observed.|The work::Steps performed, parts replaced with part numbers, software version.|The tests::As-left readings, alarm and safety tests, with pass or fail.|The instruments::Identity and calibration due date of each.|The people::Technician&rsquo;s name and signature, date, and who accepted the machine back.}}
<p>A service record answers the question someone will ask months from now: what was done to this machine, by whom, and with what?</p>
<p>Keep records for the life of the machine, organized per machine so that its whole history can be read in order. Patterns show up only in a history: the same pump replaced three times, or conductivity drifting the same way at every visit.</p>
{{fig:dashboard|Simple counts from the service records, such as visits done on time, repeat faults, and days out of service, can be charted for the unit&rsquo;s quality meeting.}}
"""),
    ],
    "debrief": ["""
<p><strong>What a meter that reads low means for the twelve machines.</strong> All twelve are wrong in the same direction. A meter that reads low makes a correct machine look high, so each was adjusted to match. If the meter reads 3 percent low, each machine adjusted to agree with it now delivers dialysate with conductivity about 3 percent higher than it displays. That means more sodium than prescribed, on all twelve machines, possibly for many months, because nobody knows when the meter began to drift.</p>
<p><strong>What you do first, and whom you tell.</strong> Tell the chief technician, the charge nurse, and the medical director today. The clinical team decides what the error means for patients; that decision is theirs, not yours. Your work is the equipment. Obtain a reference meter with a valid certificate, verify every machine, record the as-found and as-left values, and correct those out of tolerance. The as-found values tell the clinical team how far off each machine was.</p>
<p><strong>The control that would have stopped it.</strong> A register of test instruments with calibration due dates, a label on each instrument, and a rule that an overdue instrument is not used. It is simple and cheap. The due date was on the meter all along; nobody was required to read it.</p>
"""],
    "skills": {
        "title": "A calibration with a traceable record",
        "intro": "Materials: an out-of-service machine, its service manual, a reference conductivity and temperature meter with a valid certificate, standard solution, and a blank service record.",
        "items": [("Checks the reference instrument&rsquo;s identity and calibration due date before use.", True),
                  ("Verifies the reference meter against standard solution.", False),
                  ("Allows the machine to reach steady operation before measuring.", False),
                  ("Measures and records as-found conductivity and temperature.", True),
                  ("States the tolerance from the service manual and decides correctly whether adjustment is needed.", True),
                  ("Adjusts by the manual&rsquo;s procedure, if needed, and records as-left values.", False),
                  ("Completes the service record with machine identity, readings, instrument identity, and signature.", True),
                  ("Reports any as-found value far outside tolerance to the chief technician and charge nurse.", True)],
        "placement": "Build or review your center&rsquo;s test instrument register and maintenance calendar with a senior technician.",
    },
    "quiz": [
        ("What is preventive maintenance?",
         ["Repair after a breakdown", "Scheduled work done before failure occurs", "Cleaning the screen", "Buying a new machine"], 1,
         "It replaces wearing parts and checks performance on a schedule."),
        ("What does calibration mean?",
         ["Cleaning a sensor", "Comparing a reading with a trusted reference and adjusting to match", "Restarting the machine", "Replacing the battery"], 1,
         "Calibration ties the machine&rsquo;s reading to a known value."),
        ("Why record the as-found value before adjusting?",
         ["It is not necessary", "It shows how far out the machine was, which may matter for patients already treated", "To make the form longer", "For the supplier&rsquo;s invoice"], 1,
         "A large as-found error is clinical information."),
        ("A reference meter is past its calibration due date. What is correct?",
         ["Use it carefully", "Do not use it until it is calibrated", "Use it for pressure only", "Add a correction by guesswork"], 1,
         "An unverified reference can make every machine wrong in the same direction."),
        ("What does traceable mean for a reference instrument?",
         ["It has a tracking device", "Its accuracy is linked by documented calibrations to a national or international standard", "It was bought recently", "It is stored in a locked drawer"], 1,
         "Traceability is the documented chain behind the instrument&rsquo;s accuracy."),
        ("A reference meter is discovered to have been reading wrong. What must be reviewed?",
         ["Nothing", "Every machine it was used on since it was last known to be correct", "Only the last machine", "Only machines with alarms"], 1,
         "All work done with a faulty reference is in doubt."),
        ("A center has ten machines with a six-month maintenance interval. About how many visits are needed per year?",
         ["5", "10", "20", "60"], 2, "Ten machines, twice a year each, is twenty visits."),
        ("Which item belongs in every service record?",
         ["The technician&rsquo;s opinion of the brand", "The identity and calibration due date of the test instruments used", "The patient&rsquo;s diagnosis", "The price of the machine"], 1,
         "Without the instrument&rsquo;s identity, the measurements cannot be traced."),
    ],
    "terms": [("Asset number", "The facility&rsquo;s own identification number for a piece of equipment."),
              ("Standard solution", "A liquid of precisely known conductivity used to check a meter."),
              ("Accredited laboratory", "A laboratory formally recognized as competent to calibrate instruments.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Using equipment data in the quality program."),
                 ("dialysis-prescription.html", "The settings your calibrations support.")],
    "calcs": ["calc-dialysis-qapi-scorecard.html"],
}
