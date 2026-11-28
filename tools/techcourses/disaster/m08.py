# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 08: Power, Water and Supplies. DRAFT.
Single source for manual blood return and the first ten minutes: Physician-on-Duty Module 30 (repeated here, linked).
Water failure: Water Treatment Technician Module 12. Outage autonomy: Unit Manager Module 12 (CALC-12)."""

MODULE = {
    "image_alt": "A biomedical technician with a headlamp checking a generator's fuel gauge at night, the dialysis unit glowing with emergency lights behind him.",
    "objectives": [
        "Act in the first ten minutes of a power failure: patients first, power status, a decision with the charge nurse, one staff member per patient.",
        "Return blood without power by hand crank, with the operator&rsquo;s eyes doing the air detector&rsquo;s job, and know when to clamp without return.",
        "Check the generator and uninterruptible power supply (UPS), and estimate generator runtime from fuel and fuel use.",
        "Respond to a water failure or contamination alarm: stop starting treatments, end current ones per protocol, call the water technician, and resume only after a signed release.",
        "Keep a supply buffer that survives the event.",
    ],
    "big": """
{{plain:Think of a dialysis machine as four devices in one box: a pump, a heater, a mixer and a set of alarms. When the power fails, all four stop together. The blood in the lines does not know that.}}
<p>The picture has a limit: on many machines a battery keeps the blood pump and some alarms running for a short time, and the time varies by model, so ask your technician and do not assume a figure. When the battery ends, the blood stands still and begins to clot, and the venous air detector and clamp may stop guarding the vein. Water has the same hidden dependence: every treatment uses a large volume of treated water, so a fault in the water room reaches every patient on that loop at once.</p>
<p>Philippine licensing rules require a standby generator appropriate to the facility&rsquo;s size and a plan for emergencies,[[doh2012]] and the Philippine Society of Nephrology (PSN) standard repeats both.[[psn2024]] A generator still takes time to start and can fail. This module repeats the rules taught in <a href="physician-on-duty-30-when-the-power-or-water-fails.html">Physician-on-Duty, Module 30</a> and <a href="water-treatment-technician-12-failures-emergencies-capstone.html">Water Treatment Technician, Module 12</a>, from the whole team&rsquo;s side.</p>
{{cards:Key terms for this module|Standby generator::A fuel generator that takes over when the main power fails.|Transfer switch::The switch that moves the load from the utility line to the generator.|UPS::A battery that keeps selected equipment running without interruption for a short time.|Manual blood return::Returning the circuit&rsquo;s blood by turning the blood pump by hand.|Clamp and cut::Disconnecting without returning the blood.|Signed water release::The water technician&rsquo;s and the medical head&rsquo;s written approval that the water is fit for dialysis again.}}
""",
    "case": {"title": "Brownout at 4:20 p.m.", "html": """
<p>At 4:20 p.m. the utility power fails at a 15-station unit in Ormoc, Leyte. The generator starts. Twelve patients are connected. At 5:10 p.m. the technician reports that the fuel delivery promised for that afternoon has not come; the generator will run out within the hour. The utility says the line will be restored &ldquo;tonight.&rdquo;</p>
<p>At 6:05 p.m. the generator stops. The machines alarm on battery. Two patients, at Stations 3 and 11, are early in their sessions; the others have less than an hour left. The charge nurse assigns staff and opens the take-off kits.</p>
""", "questions": ["What should have happened at 5:10 p.m., when the fuel problem was known?",
                  "At 6:05 p.m., what happens at Stations 3 and 11?",
                  "Who watches the venous line, and what replaces the air detector?"]},
    "sections": [
        ("power", "The first ten minutes", "Power failure: the first ten minutes", """
<p>Most power cuts end when the generator starts, and the shift goes on. A few become real emergencies. The order of the first ten minutes is fixed, so speed comes from not having to think.</p>
{{fig:dp08_power_failure_first_ten_minutes}}
<ol>
<li><strong>Patients first.</strong> Walk the floor. Check every patient&rsquo;s airway, consciousness and access before you look at a machine. Uncover each access and look for bleeding.</li>
<li><strong>Ask for the power status.</strong> The technician reports whether the generator has started, whether it is stable, and how long its fuel will last.</li>
<li><strong>Decide with the charge nurse.</strong> Continue on generator power only if the technician confirms it is stable. Wait only as long as the unit&rsquo;s protocol allows; otherwise begin emergency take-off.</li>
<li><strong>One staff member per patient</strong> whose blood is being returned, watching the venous line.</li>
<li><strong>Watch the patients;</strong> <strong>count and record</strong> each patient&rsquo;s time off, method, and blood returned or not; <strong>call</strong> the attending nephrologist and the medical head.</li>
</ol>
<p><strong>How long will the generator run?</strong> Runtime (hours) = usable fuel (liters) &divide; fuel use at the expected load (liters per hour). For example, 120 liters &divide; 8 liters per hour = 15 hours. The fuel use comes from the generator&rsquo;s data plate and the technician&rsquo;s log. The arithmetic tells you roughly how long fuel supports treatment, not whether the generator will keep running, and a delivery may not arrive. Ask for this number at the start of every storm shift. The <a href="dialysis-unit-manager-12-business-continuity.html#calculator-calc-12-outage-autonomy">outage autonomy calculator (CALC-12)</a> in Unit Manager, Module 12 does the same for the whole unit.</p>
"""),
        ("crank", "Blood return without power", "Returning the blood by hand", """
<p>Without power, a nurse turns the blood pump with the hand crank, and the air detector and venous clamp may not act. <strong>The operator&rsquo;s eyes now do the detector&rsquo;s job.</strong> One staff member stays with each patient whose blood is being returned, watching the venous drip chamber and line until the clamp is closed.</p>
{{fig:dp08_blood_return_without_power}}
<p>The blood rule is the same in every emergency: blood that may contain air, is hemolyzed, or follows a severe reaction is never returned; a clotted circuit is not forced back; when there is no time, clamp and disconnect. Otherwise return it, by hand if needed. A central catheter&rsquo;s own clamps are closed before its lines are separated. The exact steps for your machine model (where the crank sits, how the saline is connected, how the venous clamp is opened by hand) come from the manufacturer and your biomedical technician; practice them on a training circuit twice a year (the power-loss drill).</p>
{{key:Without power, the operator&rsquo;s eyes replace the air detector. One staff member per patient, watching the venous line until the clamp is closed.}}
"""),
        ("gen", "Generator and UPS", "Generator and UPS checks", """
<p>A generator that fails its test in a storm is not a generator. The biomedical technician runs the checks; the head nurse sees the log.</p>
{{fig:dp08_generator_and_ups_checks}}
<ul>
<li><strong>Fuel level</strong> kept at the ready level the unit sets, with a named supplier and a backup supplier.</li>
<li><strong>Test run and log</strong> under real load, including the water system (Module 2&rsquo;s lesson).</li>
<li><strong>Transfer switch test:</strong> power moves to the generator and back.</li>
<li><strong>UPS outlets</strong> labeled and working for the equipment that must not stop.</li>
<li><strong>No extension cords</strong> for dialysis equipment.</li>
<li><strong>Fuel delivery contact</strong> ready, and called early when a long outage is expected.</li>
</ul>
"""),
        ("water", "Water and supplies", "Water failure, contamination and the supply buffer", """
<p>A dry tank, a cut supply, a flooded water room or a failed test stops treated water from the reverse osmosis (RO) system, and treatments stop with it.</p>
{{fig:dp08_water_failure_decision}}
<ol>
<li><strong>Stop starting new treatments.</strong></li>
<li><strong>End current treatments per protocol.</strong> If hemolysis is possible (chest or back pain, wine-colored blood in the venous line), the blood is not returned.</li>
<li><strong>Call the water treatment technician</strong> and the medical head; keep circuits and samples if contamination is suspected.</li>
<li><strong>Resume only after a signed water release.</strong></li>
</ol>
<p>One sick patient is a patient problem. Two patients with the same symptoms in the same shift is a water problem until proven otherwise. When a water test fails, the Department of Health&rsquo;s dialysis water order requires the facility to stop operations until a repeat test complies, disinfect the loop and notify its patients.[[dch_doh2013]] Whether water is fit for dialysis is decided by the water technician and the medical head, never by the shift alone.</p>
{{fig:dp08_supply_buffer}}
<p><strong>The supply buffer.</strong> Keep a written number of days of supply (dialyzers, lines, concentrates, needles, medicines), rotate stock first in, first out, and store it above the past flood line. The number of days is a unit decision, set with the unit manager from the dependency map.</p>
{{call:Generator failure with patients connected, any patient unstable during a power failure, blood that cannot be returned safely, or two patients with similar symptoms on the same water loop: call the attending nephrologist and the medical head at once while following your unit protocol, and always ask the attending nephrologist for guidance.}}
"""),
    ],
    "debrief": ["""
<p><strong>At 5:10 p.m.</strong> The fuel problem was a known end time. The charge nurse and physician-on-duty, told the generator had under an hour, should have decided then: no new connections, end sessions in an orderly way while the generator still ran (normal rinse-back with working alarms), call the backup fuel supplier, and call the attending nephrologist about the patients cut short. Waiting for the utility&rsquo;s &ldquo;tonight&rdquo; turned a planned take-off into a manual one.</p>
<p><strong>At 6:05 p.m.</strong> Patients first, then the decision. At Stations 3 and 11, a nurse at each chair returns the blood by hand crank if the circuit is sound and there is no air, hemolysis or clotting; otherwise clamp and cut. The attending nephrologist decides when those two patients dialyze next.</p>
<p><strong>Who watches.</strong> One staff member per patient being returned, watching the venous drip chamber and line until the clamp is closed, because the air detector may not work without power.</p>
"""],
    "skills": {"title": "Power loss and blood return without power",
               "intro": "With the biomedical technician, at an empty station with a training circuit (no patient), during the power-loss drill.",
               "items": [
                   ("States the first-ten-minutes order: patients first, power status, decision with the charge nurse, one staff per patient, record, call.", True),
                   ("Returns the training circuit by hand crank while watching the venous drip chamber and line until the clamp is closed.", True),
                   ("States when not to return the blood: air, hemolysis, a clotted circuit, or no time.", True),
                   ("Calculates generator runtime from usable fuel and fuel use, and states what the number does not tell you.", False),
                   ("States the four steps of a water failure, including resuming only after a signed release.", True),
                   ("Checks the supply buffer: days of supply, rotation, and storage above the flood line.", False),
               ],
               "placement": "Find the manufacturer&rsquo;s manual blood return steps for each machine model in your unit and post them with the take-off kits."},
    "terms": [("Standby generator", "A fuel generator that takes over when the main power fails."),
              ("Transfer switch", "The switch that moves the load to the generator."),
              ("UPS", "A battery that keeps selected equipment running briefly."),
              ("Manual blood return", "Returning the circuit&rsquo;s blood by turning the pump by hand."),
              ("Clamp and cut", "Disconnecting without returning the blood."),
              ("Signed water release", "Written approval that the water is fit for dialysis again.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "How patients prepare for outages.")],
    "calcs": ["calc-wts-capacity.html", "calc-dialysis-water-reuse.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["08"])
