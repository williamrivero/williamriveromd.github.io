# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Turnover has a clinical phase and an environmental phase, and yours begins only after clinical clearance and the patient has left. The four station statuses, the surfaces and sequence, keeping surfaces wet, what a &ldquo;clean&rdquo; tag does and does not mean, and what the trials of better cleaning actually show.",
    "desc": "Housekeeping & Support Staff Module 7: safe environmental turnover of a dialysis station after clinical clearance, four station statuses, surface sequence and wet contact time, a worked turnover time budget, fluorescent-marker audit evidence, and the REACH and multicenter cleaning trials.",
    "keywords": "dialysis station turnover cleaning, dialysis chair disinfection between patients, clinical clearance before cleaning, environmental cleaning trial REACH, fluorescent marker cleaning audit",
    "image_alt": "An environmental service aide wiping the armrest of an empty dialysis chair, the dialysis machine beside it switched to standby, a small status card reading nothing visible clipped to the table.",
    "objectives": [
        "Explain the two phases of turnover and confirm clinical clearance and patient departure before starting.",
        "Use the four station statuses to stop anyone using a station that is not ready.",
        "Clean and disinfect every assigned surface in sequence and keep each wet for the label contact time.",
        "Explain why environmental completion is not technical or clinical readiness.",
        "Interpret what fluorescent-marker audits and cleaning trials show about thoroughness and infections.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A pit stop with two crews",
         "html": """
<p>In a motor race, a pit stop looks like chaos but runs in strict order. One crew changes the tires; another refuels. Nobody refuels while the driver is still braking, and the car does not leave until the chief says so. A station turnover is a pit stop with two crews. The clinical crew (nurse or technician) ends the treatment, returns the blood, removes needles, takes down the bloodlines and dialyzer, and starts the machine&rsquo;s own disinfection. Only then does the environmental crew, you if you are assigned, clean and disinfect the surfaces. Then the unit releases the station for the next patient.</p>
<p>The picture has a limit. In a race, speed wins. In a dialysis unit, a fast turnover that skipped a surface or wiped before the contact time is a losing turnover, even if the next patient sat down on time.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Clinical first, patient out, then you. Every surface, fully wet, every time. Then hand it over; do not declare it ready.</div>
"""},
        {"id": "statuses", "nav": "Four statuses", "tag": "Workflow", "h2": "Four station statuses",
         "html": """
<p>This track uses four status labels so that everyone can see where a station is in the pit stop. Your unit may use different words, colored cards or a whiteboard; the idea is the same.</p>
<ol class="tc-flow">
<li><b>Occupied</b>A patient is at the station, connected or not. Environmental disinfection does not start.</li>
<li><b>Awaiting cleaning</b>The nurse has cleared it clinically and the patient has left. Mark it unavailable.</li>
<li><b>Cleaning in progress</b>You are working. Nobody sits, sets supplies down or brings the next patient.</li>
<li><b>Environmental work complete, awaiting release</b>Your part is done and recorded. The unit releases it for clinical use.</li>
</ol>
<p>A &ldquo;clean&rdquo; tag or card means only that the assigned environmental work is complete. It does not mean the machine&rsquo;s internal disinfection is finished, that the machine has passed its checks, or that the next patient&rsquo;s prescription is ready. Those belong to clinical and technical staff.</p>
<div class="tc-stop"><span class="tc-lab">Stop and call</span>If a patient is still at the station, if bloodlines, a dialyzer, needles or sharps are still present, or if there is liquid you cannot explain under or around the machine, do not start. Tell the nurse.</div>
"""},
        {"id": "sequence", "nav": "The sequence", "tag": "Practice", "h2": "The environmental sequence",
         "html": """
<p>CDC&rsquo;s station disinfection checklist begins with steps that are not yours (ending treatment, removing the circuit) and then sets out the environmental part: remove used items, clean visible soil, disinfect all surfaces, and let them stay wet for the contact time.[[cdc_station]] The CDC dialysis assessment tool asks units to define in writing who cleans which surfaces, because in many units this responsibility is split between clinical staff and environmental staff.[[cdc_dart]] Here is the environmental sequence as an EVS aide or orderly would do it, once assigned and signed off.</p>
<ol>
<li><strong>Confirm.</strong> The nurse has cleared the station and the patient has left. Mark it &ldquo;awaiting cleaning,&rdquo; then &ldquo;cleaning in progress.&rdquo;</li>
<li><strong>Prepare.</strong> Hand hygiene, PPE for the task, fresh wipes or pre-wet cloths, waste bags. Bring only what you need.</li>
<li><strong>Remove.</strong> Bag used linen at the station without shaking it (Module 8). Discard used disposable items into the right waste stream. Follow the unit list for unused supplies (Module 5). Leave patient belongings and papers for the nurse.</li>
<li><strong>Clean visible soil.</strong> Blood or body fluid first, per your spill card if needed (Module 9).</li>
<li><strong>Disinfect, clean to dirty, high to low.</strong> Side table and tray, call button and remote, lamp switch, chair arms and their undersides, chair controls, the seat and back, the leg rest, the chair base and wheels as assigned. External machine surfaces only if assigned for that machine and product: housing, handles and pole, never screens, buttons, connectors, ports or hoses unless your written procedure includes them.</li>
<li><strong>Keep wet.</strong> Each surface stays visibly wet for the full label time; re-wet if needed.</li>
<li><strong>Inspect.</strong> Look for missed spots, damage, residue, and anything left behind.</li>
<li><strong>Finish.</strong> Remove PPE, hand hygiene, record the work, mark &ldquo;environmental work complete,&rdquo; and tell the nurse.</li>
</ol>
<p>Wall boxes (the water and drain connections in the wall) and drains are not part of this sequence unless your unit has a separate written procedure and you have been trained for it. They can harbor bacteria, and CDC advises defined responsibility and separate supplies for them.[[cdc_wallbox]]</p>
"""},
        {"id": "budget", "nav": "Time budget", "tag": "Worked example", "h2": "A turnover time budget",
         "html": """
<p>Most turnovers fail not because staff do not know the steps but because the schedule leaves no time to do them. Doing the arithmetic in advance helps supervisors set realistic schedules.</p>
<div class="tc-formula"><strong>Worked example (illustrative times).</strong> Shift one ends at 10:00 a.m.; the next patient is booked to start at 10:30 a.m. That is a 30-minute gap.<br>Clinical phase (rinse-back, needle removal, circuit removal, patient leaves): about 12 minutes.<br>Environmental phase: removing items and soil, 4 minutes; disinfecting surfaces, 6 minutes; the product&rsquo;s wet contact time after the last surface is wetted, 3 minutes; inspection and handoff, 2 minutes. Total 15 minutes.<br>Clinical setup of the next treatment after release: the remaining 3 minutes.<br><strong>Result:</strong> 12 + 15 + 3 = 30. There is no slack at all. One late patient pickup or a small spill and the contact time will be cut. The unit should either stagger start times or choose a product whose contact time fits, and never ask staff to shorten the contact time.</div>
<p>The <a href="calc-dialysis-support-staff-toolkit.html">Support Staff Toolkit</a> has a turnover time budget that does this with your unit&rsquo;s own numbers and shows where the time runs out.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>A turnover that is short of time is a scheduling problem to report, not a contact time to cut.</div>
"""},
        {"id": "evidence", "nav": "What the trials show", "tag": "Evidence", "h2": "Does better cleaning prevent infections?",
         "html": """
<p><strong>Thoroughness is often poor, and it can be improved.</strong> When researchers marked high-touch surfaces in hospital rooms with an invisible fluorescent gel and checked after cleaning, only 47 percent of marked targets had been cleaned; education and feedback produced sustained improvement.[[carling2006]] Fluorescent marking is now a common audit method (Module 15).</p>
<p><strong>Better cleaning does not automatically prevent every infection.</strong> In a randomized trial in 16 hospitals in Ohio, a program that monitored cleaning and gave feedback made cleaning more thorough and reduced <em>Clostridioides difficile</em> spores on surfaces, but did not reduce hospital-acquired <em>C. difficile</em> infection.[[ray2017]] In the REACH trial in 11 Australian hospitals, a cleaning bundle of product use, technique, training, audit with feedback and communication was followed by fewer vancomycin-resistant enterococcal infections, from 0.35 to 0.22 per 10,000 occupied bed-days (relative risk 0.63), but no significant change in <em>Staphylococcus aureus</em> bloodstream infection or <em>C. difficile</em> infection.[[mitchell2019]] A review of the earlier evidence concluded that improving environmental disinfection can contribute to reducing infections, with the strongest data for some organisms.[[donskey2013]]</p>
<p>What this means for you: thorough cleaning is necessary but not sufficient. Hand hygiene, nurses&rsquo; aseptic technique, vaccination, isolation and the environment work together; the environment is the part you own. None of these trials were in dialysis units, where blood on surfaces makes the environment matter even more for hepatitis viruses (Module 3); that is an evidence-supported inference, not a trial result.</p>
"""},
    ],
    "case": {
        "title": "Ten minutes left at Station 7",
        "html": """
<p><strong>Thursday, 10:05 a.m., shift change.</strong> The second-shift patient for Station 7, Aling Nora, is standing beside the chair with her bag. The first-shift patient, Mang Delfin, is still connected; his machine shows about ten minutes left. A nurse from the other side of the unit, busy and kind, says to Ramon, an orderly who is signed off for station cleaning, &ldquo;Start on the table and the chair arm on the free side, para mabilis.&rdquo;</p>
""",
        "acte": {
            "Notice": "The station is occupied: a patient is connected. Environmental disinfection must not start. The next patient standing at the station adds risk.",
            "Communicate": "&ldquo;Ma&rsquo;am, he&rsquo;s still connected, so I&rsquo;ll wait for clearance. Shall I bring Aling Nora a chair in the waiting area?&rdquo; Tell Mang Delfin&rsquo;s nurse that the next patient is waiting at the station.",
            "Do": "Keep the next patient and clean supplies away from the occupied station; prepare your supplies nearby; start only when the nurse clears it and Mang Delfin has left.",
            "Escalate": "If shift gaps are routinely too short for full turnover and contact time, report it to the supervisor with times from your log.",
        },
        "task": "Write the log entry for this turnover with the time of clearance, start, last surface wetted, and handoff.",
        "outcome": """
<p>Ramon brought Aling Nora to a chair in the waiting area. Mang Delfin finished nine minutes later. After the nurse cleared the station and he walked out, Ramon did the full sequence and timed the contact. The station was released at 10:31, six minutes late. The supervisor, reviewing a week of such logs, staggered two start times by fifteen minutes.</p>
""",
    },
    "second_round": ("You find a small pool of clear liquid under the machine during turnover, and the nurse has already left the area.",
                     "What you do before continuing, whom you tell, and why you do not mop it up as ordinary water."),
    "evidence_out": "Two satisfactory observed station turnovers on separate occasions (if assigned), each with fluorescent-marker check and timed contact.",
    "critical": "Starting station disinfection while a patient is at the station, touching the circuit or machine controls, or releasing an incomplete station.",
    "reflect": "If you were the next patient, which surface at the station would you most want to be sure was disinfected? Is it on your task card?",
    "practice": {"intro": "Practice on a training station with fluorescent marker before any live station.", "items": [
        "Confirm clinical clearance with the nurse using the unit&rsquo;s words, and set the status card.",
        "Perform a full environmental turnover on a training station; your preceptor marks 10 high-touch spots with fluorescent gel beforehand.",
        "Time the wet contact on each surface type and re-wet as needed.",
        "Explain to your preceptor what &ldquo;environmental work complete&rdquo; does and does not mean.",
        "Calculate one turnover time budget for your unit&rsquo;s real shift gap in the toolkit.",
    ]},
    "readings": [("dialysis-machine-assignment.html", "How stations and machines are assigned to patients."),
                 ("dialysis-qapi-vs-cqi.html", "How units measure and improve quality, including cleaning audits.")],
    "calcs": ["calc-dialysis-support-staff-toolkit.html"],
    "terms": [("Clinical clearance", "The nurse&rsquo;s or authorized staff member&rsquo;s confirmation that the clinical phase of turnover is complete."),
              ("Environmental work complete", "Status meaning the assigned cleaning is done; not a declaration that the station is clinically or technically ready."),
              ("Fluorescent marker", "An invisible gel placed on surfaces before cleaning and checked under ultraviolet light afterward to audit thoroughness.")],
    "quiz": [
        {"stem": "When may environmental disinfection of a station start?", "options": [
            ("After clinical clearance and after the patient has left.", True, "Both are prerequisites."),
            ("In the last ten minutes of treatment, on the free side.", False, "The station is still occupied."),
            ("As soon as the next patient arrives.", False, "Arrival does not clear the station."),
            ("Whenever the aide is free.", False, "Clearance and departure come first.")], "sources": ["cdc_station"]},
        {"stem": "What does &ldquo;environmental work complete&rdquo; mean?", "options": [
            ("Your assigned cleaning is done; the unit still releases the station.", True, "It is not technical or clinical readiness."),
            ("The machine has passed its checks.", False, "That is technical."),
            ("The next patient can be connected.", False, "Release is a unit decision."),
            ("The station is sterile.", False, "Disinfection is not sterilization.")], "sources": []},
        {"stem": "You find bloodlines still on the machine. What do you do?", "options": [
            ("Stop and ask the nurse to complete the clinical phase.", True, "Circuit handling is excluded."),
            ("Remove them carefully with gloves.", False, "Excluded task."),
            ("Clean around them.", False, "The clinical phase is incomplete."),
            ("Cut them to fit the bin.", False, "Dangerous and excluded.")], "sources": ["cdc_station"]},
        {"stem": "Which surfaces of the dialysis machine may you clean?", "options": [
            ("Only those in your written, machine-specific assignment, never controls, connectors or hoses unless included.", True, "Machine surfaces are conditional."),
            ("All of it, including the screen buttons.", False, "Controls are excluded by default."),
            ("The inside, by opening panels.", False, "Never."),
            ("None, under any circumstances.", False, "Exterior surfaces can be assigned.")], "sources": ["cdc_dart"]},
        {"stem": "In the fluorescent-marker study, what share of marked targets had been cleaned at baseline?", "options": [
            ("About 47 percent.", True, "Less than half."),
            ("About 99 percent.", False, "Much lower."),
            ("None.", False, "Some were cleaned."),
            ("Exactly 75 percent.", False, "It was about 47 percent.")], "sources": ["carling2006"]},
        {"stem": "In the Ohio randomized trial, better cleaning:", "options": [
            ("Improved thoroughness and spores on surfaces but did not reduce C. difficile infection.", True, "Cleaning alone was not sufficient for that outcome."),
            ("Eliminated all infections.", False, "It did not."),
            ("Made cleaning worse.", False, "It improved."),
            ("Was not tested.", False, "It was a randomized trial.")], "sources": ["ray2017"]},
        {"stem": "In the REACH trial, which infection fell significantly after the cleaning bundle?", "options": [
            ("Vancomycin-resistant enterococcal infection.", True, "Relative risk 0.63."),
            ("All three measured infections.", False, "Only VRE fell significantly."),
            ("None.", False, "VRE infections fell."),
            ("Hepatitis B.", False, "Not measured.")], "sources": ["mitchell2019"]},
        {"stem": "What is the fair conclusion from the cleaning trials?", "options": [
            ("Thorough cleaning is necessary but works together with hand hygiene and other measures.", True, "Mixed results show it is one part of a system."),
            ("Cleaning does not matter.", False, "It contributes."),
            ("Cleaning alone prevents all infections.", False, "Not shown."),
            ("Only nurses&rsquo; work matters.", False, "Environment is part of the system.")], "sources": ["ray2017", "mitchell2019", "donskey2013"]},
        {"stem": "The shift gap is 30 minutes and the clinical phase takes 12, cleaning 15 and setup 3. What does this show?", "options": [
            ("No slack; a delay will squeeze contact time, so the schedule should change.", True, "Report scheduling problems."),
            ("There is plenty of time.", False, "Zero slack."),
            ("Contact time can be shortened.", False, "Never."),
            ("Skip inspection.", False, "Inspection is required.")], "sources": []},
        {"stem": "Why is the station marked &ldquo;cleaning in progress&rdquo;?", "options": [
            ("So nobody sits, sets supplies down or brings a patient before it is released.", True, "Protects the process."),
            ("To show off your work.", False, "Not the purpose."),
            ("Because it is required by PhilHealth for every station.", False, "Not the reason given here."),
            ("To tell patients to go home.", False, "Not the purpose.")], "sources": []},
        {"stem": "Where do patient belongings and papers left at a station go?", "options": [
            ("To the nurse, untouched except to move them safely.", True, "Belongings and records are not waste."),
            ("In the general waste.", False, "Never discard belongings."),
            ("In your locker for safekeeping.", False, "Hand to the nurse."),
            ("To the next patient.", False, "Never.")], "sources": []},
        {"stem": "Which item is NOT part of your environmental sequence by default?", "options": [
            ("Cleaning the wall box connections and drain.", True, "Needs a separate procedure and designated team."),
            ("Chair arms and their undersides.", False, "Part of the sequence."),
            ("Side table and call button.", False, "Part of the sequence."),
            ("Inspection before handoff.", False, "Part of the sequence.")], "sources": ["cdc_wallbox"]},
        {"stem": "During inspection you find a spot you missed, after you logged the station as complete. What do you do?", "options": [
            ("Clean it, re-time the contact, and correct the record truthfully.", True, "Honest correction keeps records useful."),
            ("Leave it; the record is done.", False, "The patient is at risk."),
            ("Clean it but leave the record as is.", False, "Correct the record."),
            ("Ask the next patient to avoid it.", False, "Never shift the risk.")], "sources": []},
        {"stem": "The next patient has already sat down at a station you have not finished. What do you do?", "options": [
            ("Stop and tell the nurse immediately; do not clean around a seated patient.", True, "The nurse decides how to correct it."),
            ("Clean around her quickly.", False, "Spraying near a patient is unsafe and incomplete."),
            ("Mark it complete.", False, "It is not complete."),
            ("Say nothing.", False, "The risk must be reported.")], "sources": []},
        {"stem": "What should a supervisor do if turnovers are routinely short of time?", "options": [
            ("Adjust schedules or products; never ask staff to cut contact time.", True, "Speed must not bypass safety."),
            ("Reward the fastest aide.", False, "Rewards shortcuts."),
            ("Remove inspection.", False, "Removes a safety check."),
            ("Do nothing.", False, "The risk persists.")], "sources": []},
    ],
    "exam": [
        {"stem": "A patient is still connected with ten minutes left. A nurse asks you to start wiping the free chair arm. What do you do?", "options": [
            ("Wait for clearance and departure; keep the next patient and supplies away.", True, "Never disinfect an occupied station."),
            ("Start on the free side.", False, "The station is occupied."),
            ("Start on the machine.", False, "Excluded and occupied."),
            ("Clean the floor under the patient.", False, "Occupied."),], "sources": ["cdc_station"]},
        {"stem": "What does a &ldquo;clean&rdquo; card on the station mean?", "options": [
            ("The assigned environmental work is complete; release is a separate unit decision.", True, "Limited meaning."),
            ("The machine is ready for treatment.", False, "Technical readiness is separate."),
            ("The prescription is set.", False, "Clinical."),
            ("The station is sterile.", False, "Not sterile.")], "sources": []},
        {"stem": "Which statement about cleaning trials is accurate?", "options": [
            ("A cleaning bundle reduced one type of resistant-bacteria infection but not all infections measured.", True, "REACH reduced VRE infections only."),
            ("Cleaning has been proven useless.", False, "Not the finding."),
            ("Cleaning prevents all hospital infections.", False, "Not the finding."),
            ("No trials have been done.", False, "Randomized trials exist.")], "sources": ["mitchell2019"]},
    ],
}
