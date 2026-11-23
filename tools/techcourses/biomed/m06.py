# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician and a charge nurse signing a return-to-service form beside a hemodialysis machine.",
    "objectives": [
        "Apply a step-by-step method to find the cause of a fault instead of replacing parts by guesswork.",
        "Decide which tests are needed after a repair before the machine is released.",
        "Maintain the records every machine should have across its life.",
        "Use equipment data to support the unit&rsquo;s quality program and replacement planning.",
    ],
    "big": """
{{plain:Fault-finding is detective work. You collect the facts, form an idea of the cause, test that idea, fix what you proved, and then prove the machine is safe again. The last step is the one most often skipped, and it is the one that protects the patient.}}
{{flow:A method for any fault|Gather::Exact alarm text or code, what the machine was doing, what the operator saw.|Reproduce::Can you make it happen again safely, with no patient?|Simple things first::Supplies, connections, water, power, concentrate, settings.|Divide::Use the flow diagram and the manual&rsquo;s fault tables to narrow the area.|Test one idea at a time::Change one thing and observe.|Repair::With approved parts, by the manual.|Verify and release::Run the tests the repair calls for, record, and hand over.}}
{{cards:Key terms for this module|Fault code::The number or message the machine gives when it detects a problem.|Intermittent fault::A fault that comes and goes.|Root cause::The underlying reason, not just the part that failed.|Verification::Tests that prove the repair worked and nothing else was disturbed.|Asset register::The list of all equipment with its identity and history.|Downtime::Time a machine is unavailable for treatment.}}
""",
    "case": {
        "title": "Three machines, one alarm",
        "html": """
<p>On a Tuesday morning three machines on the same side of the unit give low conductivity alarms within ten minutes of each other. Machines on the other side are running normally. A colleague is already opening the first machine to change its conductivity sensor. All three machines draw acid concentrate from the same central supply line.</p>
""",
        "questions": ["What do the three machines have in common?",
                      "Is replacing a sensor a sound first step?",
                      "What would you check first, and whom would you tell?"],
    },
    "sections": [
        ("method", "Method", "Think before you open the cabinet", """
<p>Most alarms in daily use are not machine faults. An empty or wrong concentrate container, a kinked inlet hose, low water pressure, or a poorly seated connector accounts for many of them. Starting with the simple, shared causes saves time and avoids creating new faults by disturbing a healthy machine.</p>
{{cards:Questions that narrow a fault quickly|One machine or several?::Several at once points to something shared: water, concentrate, power.|Always or sometimes?::Intermittent faults suggest loose connections, air, or temperature.|Since when?::What changed just before? A service visit, new supplies, a different operator.|Which phase?::Start-up, priming, treatment, or disinfection.}}
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Check first</th><th>Then consider</th></tr></thead>
<tbody>
<tr><td>Low or unstable conductivity</td><td>Concentrate containers, pick-up tubes, central supply, correct concentrate type</td><td>Air in the lines, proportioning pump, scaled or drifted sensor</td></tr>
<tr><td>Temperature alarm</td><td>Inlet water temperature and flow</td><td>Heater, sensor, scale</td></tr>
<tr><td>Fluid balance or ultrafiltration error</td><td>Dialyzer connectors, leaks at couplings, air</td><td>Balancing valves, ultrafiltration pump</td></tr>
<tr><td>Repeated blood leak alarms with no blood seen</td><td>Air bubbles, dirty sensor window</td><td>Detector calibration</td></tr>
<tr><td>Machine fails disinfection</td><td>Disinfectant container and pick-up</td><td>Intake valve, heater</td></tr>
</tbody></table></div>
{{key:Replacing parts until the alarm stops is not diagnosis. If you cannot explain why the part failed, you have not finished.}}
"""),
        ("verify", "After repair", "What to test after a repair", """
<p>Any repair disturbs the machine. The service manual states which tests must follow which work; the more of the fluid path or the electrical system you opened, the more you verify.</p>
{{cards:Verification after repair|Function::The fault is gone under the conditions that produced it.|Affected parameters::Recalibrate anything the repair could have changed.|Protective systems::Re-prove alarms and automatic actions in the area you worked on.|Leaks::Run the machine and inspect every connection you touched.|Electrical safety::Retest if the repair involved mains wiring or the earth path.|Disinfection::If the fluid path was opened, disinfect and pass a residual test.}}
{{fig:code_readiness|Readiness is built in advance. The same holds for equipment: a machine is ready because its checks were done, not because it switched on.}}
{{flow:Release|Complete the record::Findings, work, parts, tests, instruments.|Remove your tag::Only when every required test has passed.|Hand over in person::Tell the charge nurse what was wrong, what was done, and anything to watch.|Acceptance::The nurse accepts the machine for clinical use; operators run normal pre-use checks.}}
{{stop:If a required test cannot be completed, the machine stays out of service, however busy the unit is. Say so plainly and offer the date it will be ready.}}
"""),
        ("records", "Lifetime records", "The records behind every machine", """
{{cards:The machine file|Identity::Model, serial number, asset number, purchase and installation dates, software version.|Acceptance::Tests at installation.|Preventive maintenance::Every scheduled visit, with readings.|Repairs::Every fault, cause, and action.|Safety tests::Electrical safety and protective system tests.|Disinfection and filters::Programs run and filter changes, where kept per machine.|Retirement::The decision and date the machine left service.}}
<p>Keep the manufacturer&rsquo;s safety notices and software updates in the same system, with a note of which machines were affected and when the action was completed. Report serious equipment incidents through the facility&rsquo;s process and to the supplier.</p>
"""),
        ("quality", "Quality", "Equipment data in the quality program", """
{{fig:dashboard|An illustrative dashboard. A few equipment indicators, tracked monthly, show whether maintenance is keeping up.}}
{{cards:Indicators worth tracking|Maintenance on time::The share of scheduled visits completed by their due date.|Repeat faults::The same fault on the same machine within a set period.|Downtime::Days each machine was unavailable.|Treatment interruptions::Sessions stopped or moved because of equipment.|Overdue test instruments::Should always be zero.}}
{{fig:fishbone}}
<p>When a machine has frequent faults, parts that can no longer be obtained, or repair costs approaching the price of replacement, the technician&rsquo;s records are the evidence that supports retiring it. A good service history is also what makes a medical director confident in the machines on the floor.</p>
{{fig:pdsa}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> The three machines share a side of the unit and a central acid concentrate line. Three sensors do not fail in the same ten minutes; a shared supply does. Replacing a sensor is not a sound first step and risks disturbing a healthy machine. Check the central concentrate supply first: tank level, the correct concentrate connected, the valve to that side of the unit, and air in the line. Tell the charge nurse immediately that the alarms point to the concentrate supply on that side and that the machines are in bypass, so the clinical team can decide about connected patients. The colleague stops, closes the first machine, and it is checked before reuse because it was opened. Afterward, record the event and review why the supply ran low or was interrupted.</p>
"""],
    "skills": {
        "title": "Fault-finding and return to service",
        "intro": "Materials: an out-of-service machine with a simulated fault set by the preceptor, the service manual, test instruments, and blank service and release forms.",
        "items": [("Collects the exact alarm text and the circumstances before touching the machine.", False),
                  ("Checks simple and shared causes before opening the cabinet.", True),
                  ("Uses the flow diagram and fault table to narrow the fault area.", False),
                  ("Tests one idea at a time and states the reasoning.", False),
                  ("Repairs by the manual with approved parts.", True),
                  ("Lists and performs the verification tests the repair requires.", True),
                  ("Disinfects and passes a residual test if the fluid path was opened.", True),
                  ("Completes the service record and hands over in person to the charge nurse before removing the tag.", True)],
        "placement": "Review one machine&rsquo;s complete file with a senior technician and present its history, in five minutes, as you would to the unit&rsquo;s quality meeting.",
    },
    "quiz": [
        ("Three machines fed by the same concentrate line alarm for low conductivity within minutes. What is the most likely cause?",
         ["Three failed sensors", "A problem with the shared concentrate supply", "A software fault", "The blood pumps"], 1,
         "Simultaneous faults on several machines point to something they share."),
        ("What is the first step in fault-finding?",
         ["Replace the most expensive part", "Gather the exact alarm text and the circumstances", "Restart repeatedly", "Open the cabinet"], 1,
         "Facts first; they often identify the cause without opening the machine."),
        ("Why check simple causes first?",
         ["They are commonly the cause, and it avoids disturbing a healthy machine", "It looks busy", "Manuals forbid opening machines", "Parts are expensive"], 0,
         "Supplies, connections, water, and settings account for many alarms."),
        ("A part was replaced and the alarm stopped, but the reason the part failed is unknown. What is true?",
         ["The job is complete", "The diagnosis is incomplete and the fault may return", "The machine needs no tests", "The part was defective from the factory"], 1,
         "Without a cause, the same failure may recur."),
        ("The fluid path was opened during a repair. What is required before release?",
         ["Nothing extra", "Disinfection and a negative residual test, plus the manual&rsquo;s verification tests", "Only a wipe of the outside", "A new power cord"], 1,
         "Opening the fluid path can introduce contamination."),
        ("A required post-repair test cannot be completed before the next shift. What is correct?",
         ["Release the machine and test later", "Keep it out of service and state when it will be ready", "Ask the operator to watch it", "Remove the tag quietly"], 1,
         "A machine is released only when every required test has passed."),
        ("Who accepts a repaired machine for clinical use?",
         ["The technician alone", "The charge nurse, after the technician&rsquo;s handover", "The supplier", "The next patient"], 1,
         "The technician certifies technical fitness; the clinical lead accepts it for use."),
        ("Which indicator should always be zero?",
         ["Machines in the unit", "Test instruments in use past their calibration due date", "Treatments per day", "Spare parts in stock"], 1,
         "An overdue instrument undermines every measurement made with it."),
    ],
    "terms": [("Flow diagram", "The drawing in the service manual that shows every component of the fluid path in order."),
              ("Safety notice", "A manufacturer&rsquo;s formal warning about a problem with a device, with the action required."),
              ("Retirement", "Formally removing a machine from service at the end of its life.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality management in a dialysis center."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Equipment and utilities in disaster planning.")],
    "calcs": ["calc-dialysis-qapi-scorecard.html", "calc-dialysis-continuity-planner.html"],
}
