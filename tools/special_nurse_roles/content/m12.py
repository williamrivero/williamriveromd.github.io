# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Why a dialysis patient's blood meets more water in a week than most people drink in a year, what chemical, microbial and endotoxin hazards travel across the membrane, what the nurse must verify before connecting, and why restart needs both technical release and clinical approval.",
    "desc": "Special Dialysis Nurse Roles Module 12: the water, dialysate and equipment safety liaison nurse. Dialysate exposure, chemical, microbiological and endotoxin hazards, the Caruaru outbreak, DOH AO 2013-0003 and ISO 23500, release evidence, common-source reactions, stop-use and authorized restart.",
    "keywords": "dialysis water safety nurse, dialysate contamination hazards, endotoxin dialysis reaction, chloramine hemolysis dialysis, Caruaru microcystin dialysis, machine disinfection release residual test, DOH AO 2013-0003 water dialysis",
    "image_alt": "A Filipino dialysis nurse and a water treatment technician together checking a signed machine release sheet beside a reverse osmosis unit.",
    "objectives": [
        "Describe the nursing and technical interface for water, dialysate and machines, and the readiness evidence the nurse checks.",
        "Recognize unsafe or unverified water and equipment status, and the patient signs of a common-source exposure.",
        "Coordinate a safe response to a failure, treating it as a patient-safety event.",
        "Verify documented technical release and clinical approval before treatment restarts.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A thin wall between the blood and a river of fluid",
         "html": """
<p>During hemodialysis the patient's blood flows on one side of a thin membrane and dialysate flows on the other, in the opposite direction. At a typical dialysate flow of 500 to 800 mL per minute, a four-hour session passes roughly 120 to 190 liters of dialysate past the blood (illustrative; the actual volume depends on the prescription). Three sessions a week means a patient's blood meets several hundred liters of fluid every week, more water than most people drink in a year.</p>
<p>The picture has a limit. A wall between two rivers sounds protective, and the membrane does hold back bacteria and large particles. But small chemicals pass straight through, and fragments of bacteria (endotoxins and other pyrogens) can cross or trigger the body from the other side. The patient has no kidneys to clear what gets in. So the quality of the water and the condition of the machine are clinical matters, and the nurse who connects the patient is the last check before exposure.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>The technician makes and releases the water and machines. The nurse checks that release has happened before connecting, recognizes when patients react, and stops use until the right people say it is safe.</div>
"""},
        {"id": "hazards", "nav": "Hazards", "tag": "Mechanism", "h2": "What can travel across the membrane",
         "html": """
<div class="table-wrap"><table>
<thead><tr><th>Hazard</th><th>Mechanism</th><th>What patients may show</th></tr></thead>
<tbody>
<tr><td>Chlorine and chloramine (added to city water to kill germs)</td><td>Oxidize hemoglobin and damage red cells</td><td>Hemolysis: falling hemoglobin, dark blood or plasma, chest or back pain, low blood pressure</td></tr>
<tr><td>Aluminum, fluoride, copper and other metals</td><td>Accumulate without kidneys; some act acutely</td><td>Aluminum: bone disease, anemia, brain dysfunction over time; acute fluoride or copper: nausea, arrhythmia, hemolysis</td></tr>
<tr><td>Bacteria and biofilm in pipes and machines</td><td>Live bacteria rarely cross an intact membrane, but their fragments do</td><td>Fever, chills and rigors during the session, low blood pressure; long-term low-grade inflammation</td></tr>
<tr><td>Endotoxin and other pyrogens</td><td>Bacterial fragments trigger cytokine release</td><td>Pyrogenic reaction: chills, fever, hypotension during dialysis, often in several patients</td></tr>
<tr><td>Residual disinfectant after cleaning</td><td>Chemical left in the circuit enters the dialysate</td><td>Hemolysis or acute reactions on the first patient after disinfection</td></tr>
<tr><td>Wrong concentrate or conductivity</td><td>Dialysate sodium or potassium far from prescribed</td><td>Cramps, seizures, arrhythmia, hemolysis</td></tr>
</tbody></table></div>
<p><strong>The lesson of Caruaru.</strong> In February 1996, at a dialysis center in Caruaru, Brazil, 116 of 130 patients developed visual disturbances, nausea and vomiting associated with dialysis. One hundred one developed acute liver failure, and 50 died. Water at that center came from a reservoir without treatment, filtration or chlorination, unlike the other center in the city, and microcystins, toxins from cyanobacteria, were found in the water and in patients' blood and liver tissue.[[caruaru1998]] The same reservoir, properly treated, did not harm patients at the other center. Water treatment and monitoring are not paperwork; they are the difference between treatment and poisoning.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>When several patients react on the same shift, the same loop or the same machine, think of a common source first: water, dialysate, disinfection or a shared supply.</div>
"""},
        {"id": "standards", "nav": "Limits in context", "tag": "Standards", "h2": "Use limits with their context",
         "html": """
<p>Water and dialysate quality limits come from specific standards. In the Philippines, DOH Administrative Order 2013-0003 sets requirements for analyzing, monitoring and maintaining water for dialysis.[[doh2013]] International standards in the ISO 23500 series set requirements for water and dialysis fluid quality, including microbiological and endotoxin limits, with separate expectations for water, standard dialysate and ultrapure fluid.[[iso23500_3]][[iso23500_5]] The CDC explains the contamination routes and why limits depend on the standard and the fluid type.[[cdc_water]]</p>
<p>Two ideas matter for the nurse more than any single number:</p>
<ul>
<li><strong>Action level versus maximum level.</strong> Many standards set an <em>action level</em> below the maximum: a result above it means the technical team must act (disinfect, investigate) before the maximum is reached. A result above the <em>maximum</em> means the water or fluid does not meet the standard.</li>
<li><strong>Context of every result.</strong> A number means nothing without the standard and edition, the fluid type (product water, dialysate, substitution fluid), the sampling point, the method and the unit of measure. This module therefore teaches interpretation and escalation, and does not give a universal number; the technical reviewer applies the facility's current standard.</li>
</ul>
<p><strong>Municipal changes.</strong> When the water utility changes treatment (for example, switching disinfectant or adding a chemical during a flood or drought), the unit's pretreatment may no longer be adequate. A utility advisory is passed to the technician and head nurse the same day.</p>
"""},
        {"id": "verify", "nav": "What the nurse verifies", "tag": "Practice", "h2": "Understand what the nurse must verify",
         "html": """
<p>The water treatment technician runs the system: pretreatment, carbon tanks, reverse osmosis (RO), the distribution loop, disinfection and testing. The biomedical technician maintains the machines. The nurse does not adjust, repair or release any of these. Before connecting a patient, the nurse checks that the evidence of release exists.</p>
<div class="tc-cards">
<div class="tc-card"><b>Water system</b>Today's daily checks signed (for example chlorine or chloramine test before the patient shift, RO alarms clear) per the unit's log.</div>
<div class="tc-card"><b>Machine after disinfection</b>Release sheet signed; residual disinfectant test documented as negative per procedure.</div>
<div class="tc-card"><b>Machine self-test</b>Passed; no unresolved alarm.</div>
<div class="tc-card"><b>Dialysate</b>Correct concentrate for the order; conductivity and temperature within the machine's set range; independent check per unit procedure.</div>
</div>
<div class="tc-stop"><span class="tc-lab">Stop</span>If the release sheet is unsigned, a required test is missing, or an alarm is unexplained, the machine stays out of use. "Conductivity looks normal" is not release.</div>
"""},
        {"id": "respond", "nav": "Failure as safety event", "tag": "Response", "h2": "Manage a failure as a patient-safety event",
         "html": """
<ol class="tc-flow">
<li><b>Stop exposure</b>On the physician's or charge nurse's direction: stop affected treatments per protocol; do not start new patients on the suspected loop or machine.</li>
<li><b>Care for patients</b>Vital signs, symptoms, blood samples as ordered (hemoglobin and signs of hemolysis, cultures for fever).</li>
<li><b>Preserve</b>Do not drain, flush or disinfect the suspected machine or loop until the technical team says samples have been taken.</li>
<li><b>Record exposures</b>Which patients, which stations, which machine numbers, times, concentrate lots.</li>
<li><b>Notify</b>Water and biomedical technicians, head nurse, clinical head, infection prevention (Module 3).</li>
<li><b>Restart</b>Only after technical release and clinical approval (below).</li>
</ol>
<div class="tc-scene"><span class="tc-lab">Saturday, 6:00 a.m. &middot; fictional</span><p>Machine 8 was chemically disinfected overnight. Its release sheet is unsigned and the residual-test box is empty. The conductivity reading looks normal and the first patient is waiting. Last Thursday, two patients on the same water loop had chills during dialysis.</p><p>Nurse Ella keeps machine 8 out of use, moves the patient to a released machine, and calls Kuya Ramil, the technician on duty. She tells the charge nurse about the unsigned release and reminds the team about Thursday's two reactions, so infection prevention and the water technician can consider them together.</p><p class="tc-scene-take"><b>What this shows.</b> Missing release evidence plus earlier reactions on the same loop is a pattern worth stopping for. The patient was dialyzed on time on another machine.</p></div>
"""},
        {"id": "restart", "nav": "Authorized restart", "tag": "Authority", "h2": "Restart only after the right people release the system",
         "html": """
<p>Two separate approvals are needed before treatment resumes on a system that failed or was suspected:</p>
<div class="tc-cards">
<div class="tc-card"><b>Technical release</b>The responsible technician documents that the cause was found and fixed, required tests passed, and the system or machine is fit for use.</div>
<div class="tc-card"><b>Clinical approval</b>The physician (or clinical head, per policy) approves resuming treatment and any patient follow-up.</div>
<div class="tc-card"><b>Team notification</b>The nurse in charge tells every shift what happened, what was done and what to watch for.</div>
</div>
<p>The nurse liaison checks that both approvals are documented before the first patient is connected. She does not sign technical release, and a technician does not approve clinical restart.</p>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 1</span>In one quarter, 12 sessions started on machines that had been out of service. Ten had documented technical release and clinical approval before connection. The measure is 10 of 12 (83 percent, 95 percent range about 55 to 95). The two gaps are reviewed as incidents. The balancing measure is downtime: treatment delays and rescheduled sessions caused by holds.</div>
"""},
    ],
    "case": {
        "title": "The unsigned release and the second patient",
        "html": """
<p><strong>Tuesday, 6:05 a.m.</strong> After overnight heat and chemical disinfection, machine 3's release sheet is unsigned and the residual disinfectant test result is missing. Conductivity looks normal. Your next patient is waiting.</p>
<p>At 6:40, Mr. Fernando Lim (station 5, same water loop) develops chills and a temperature of 38.4 °C 45 minutes into treatment; his blood pressure falls from 132/80 to 98/60. At 6:55, Mrs. Edna Valdez (station 7, same loop) reports chills too. The water technician arrives at 7:30. A colleague wants to flush and disinfect machine 3 "to be safe."</p>
""",
        "acte": {
            "Assess": "Missing release evidence on machine 3, and two pyrogenic-type reactions on the same loop within 15 minutes: a possible common source (water loop, dialysate, disinfection). Patients first.",
            "Communicate": "Keep machine 3 out of use. Tell the charge nurse and physician now about both reactions; follow their direction on stopping affected treatments and samples. Call the water and biomedical technicians.",
            "Teach": "Explain to the colleague why flushing machine 3 now could destroy evidence: the technical team needs samples first.",
            "Escalate": "Record exposures (patients, stations, machines, times, concentrate lots). Notify the head nurse, clinical head and infection prevention. No new patient starts on the loop until technical release and clinical approval are documented.",
        },
        "outcome": """
<p>Both patients recovered after their treatments were stopped and they were assessed; blood cultures were negative. The technician found a fault in the loop's disinfection cycle and a sample above the action level, disinfected the loop, retested and documented release; the clinical head approved restart that afternoon. Machine 3's release had simply not been completed; it was tested and released separately.</p>
""",
        "task": "Complete an exposure record for the two patients and a restart checklist showing both approvals, with names, times and what was verified.",
    },
    "second_round": ("A week later the city water utility announces it will switch to chloramine disinfection in your district from Monday.",
                     "A message to the water technician and head nurse, and a list of what the nurse should watch for in patients during the first week after the switch."),
    "evidence_out": "A supervised pre-connection verification on five machines, and a simulated common-source response with a documented restart.",
    "critical": "Connecting a patient to a machine or loop without documented release, or destroying evidence during a suspected common-source event.",
    "reflect": "Where in your unit is the evidence that today's water and machines were released? Could a new nurse find it in under a minute?",
    "practice": {
        "intro": "Work alongside the water and biomedical technicians; the nurse observes and verifies but does not operate or adjust technical systems.",
        "items": [
            "Walk the water treatment system with the technician and name each stage and its daily check.",
            "Verify release evidence on five machines after disinfection, with the technician.",
            "Read your unit's water and dialysate testing records and identify the standard, fluid type and sampling point for each result.",
            "Run a tabletop common-source reaction exercise with the charge nurse, technicians and infection prevention.",
            "Review how a municipal water advisory reaches the unit, and who acts on it.",
        ],
    },
    "job_aid": ("Pre-connection and restart verification", [
        "Date, shift, machine number, station",
        "Water system daily checks signed (time, initials)",
        "Machine disinfection completed; release signed by (technician)",
        "Residual disinfectant test documented negative (time)",
        "Machine self-test passed; alarms clear",
        "Concentrate matches order; conductivity and temperature in range",
        "For restart after a failure: cause and fix documented",
        "Technical release (name, time)",
        "Clinical approval (name, time)",
        "Team notified (shift, time)",
    ]),
    "metric": "Affected sessions started only after documented release (and, after a failure, clinical approval), divided by affected sessions reviewed; balanced by downtime and treatment disruption.",
    "readings": [
        ("dialysis-water-treatment-systems.html", "How dialysis water treatment works."),
        ("dialysis-machine-assignment.html", "Machine assignment in the dialysis unit."),
        ("hemodialysis-complications.html", "Complications during hemodialysis, including reactions."),
    ],
    "academy": [("Water Treatment Technician track", "water-treatment-technician.html"), ("Biomedical Equipment Technician track", "dialysis-biomedical-technician.html"), ("Hemodialysis Nurse Module 8: Equipment, water and dialysate safety", "nephrology-nursing-08-hd-equipment-water-dialysate-safety.html")],
    "calcs": ["calc-dialysis-nurse-portfolio-toolkit.html", "calc-dialysis-water-reuse.html"],
    "terms": [
        ("Dialysate", "The fluid that flows on the other side of the dialyzer membrane from the blood."),
        ("Endotoxin", "Fragments of bacterial cell walls that can trigger fever and inflammation."),
        ("Action level", "A test result that requires corrective action before the maximum limit is reached."),
        ("Residual disinfectant test", "A test confirming no cleaning chemical remains in the machine before use."),
        ("Technical release", "The technician's documented confirmation that a system or machine is fit for use."),
    ],
    "quiz": [
        {"stem": "A machine's release sheet is unsigned and the residual test is missing, but conductivity looks normal. What do you do?",
         "options": [["Keep it out of use, move the patient to a released machine and call the technician.", True, "Conductivity is not release."],
                     ["Connect the patient; conductivity is normal.", False, "Missing release evidence."],
                     ["Run a quick rinse and connect.", False, "Not a release."],
                     ["Sign the release yourself.", False, "Outside nursing authority."]], "sources": [], "critical": True},
        {"stem": "What happened at the Caruaru dialysis center in 1996?",
         "options": [["Untreated reservoir water containing microcystins caused acute liver failure in 101 patients; 50 died.", True, "Water treatment failure."],
                     ["A machine software error.", False, "Not the cause."],
                     ["A hepatitis B outbreak.", False, "Not the cause."],
                     ["Excess chlorine in treated water.", False, "Water was untreated."]], "sources": ["caruaru1998"]},
        {"stem": "Two patients on the same water loop develop chills and hypotension within 15 minutes. What should you think first?",
         "options": [["A possible common source: water, dialysate, disinfection or shared supply.", True, "Clusters suggest a shared exposure."],
                     ["Coincidence.", False, "Must be investigated."],
                     ["Both have new access infections.", False, "Possible, but a common source must be considered first."],
                     ["Anxiety.", False, "Not a safe assumption."]], "sources": ["cdc_water"]},
        {"stem": "Why should the suspected machine not be flushed immediately?",
         "options": [["Flushing may destroy the evidence the technical team needs to sample.", True, "Preserve, then investigate."],
                     ["Flushing damages the machine.", False, "Not the reason."],
                     ["Flushing takes too long.", False, "Not the reason."],
                     ["Flushing is never allowed.", False, "It is allowed after sampling."]], "sources": [], "critical": True},
        {"stem": "What do chlorine and chloramine in dialysate do to patients?",
         "options": [["Damage red cells, causing hemolysis.", True, "Oxidative injury."],
                     ["Cause hyperkalemia only.", False, "Not the main effect."],
                     ["Cause bacterial infection.", False, "They are disinfectants."],
                     ["Nothing, because the membrane blocks them.", False, "Small chemicals cross."]], "sources": ["cdc_water"]},
        {"stem": "What does an 'action level' mean?",
         "options": [["A result that requires corrective action before the maximum limit is reached.", True, "Early warning threshold."],
                     ["The maximum allowed value.", False, "That is the maximum."],
                     ["A level at which patients must be dialyzed.", False, "Not the meaning."],
                     ["The level after which no action is needed.", False, "Opposite."]], "sources": ["iso23500_5"]},
        {"stem": "Which information must accompany any water test result for it to be interpreted?",
         "options": [["Standard and edition, fluid type, sampling point, method and unit.", True, "Context determines meaning."],
                     ["The technician's age.", False, "Irrelevant."],
                     ["The weather.", False, "Irrelevant."],
                     ["Only the number.", False, "Not enough."]], "sources": ["cdc_water"]},
        {"stem": "Which Philippine issuance sets requirements for water used in dialysis?",
         "options": [["DOH Administrative Order 2013-0003.", True, "Analysis, monitoring and maintenance of dialysis water."],
                     ["RA 10173.", False, "Data privacy."],
                     ["PhilHealth Circular 2024-0023.", False, "Benefits."],
                     ["RA 7170.", False, "Organ donation."]], "sources": ["doh2013"]},
        {"stem": "Who signs technical release after a water system failure?",
         "options": [["The responsible technician.", True, "Technical release is a technical role."],
                     ["The nurse liaison.", False, "Outside nursing authority."],
                     ["The patient.", False, "No."],
                     ["The claims officer.", False, "No."]], "sources": []},
        {"stem": "Who approves resuming treatment clinically after a failure?",
         "options": [["The physician or clinical head, per policy.", True, "Clinical approval is separate from technical release."],
                     ["The technician.", False, "Technical release only."],
                     ["The first patient.", False, "No."],
                     ["Anyone on duty.", False, "Defined roles."]], "sources": []},
        {"stem": "The water utility announces a switch to chloramine. What should happen?",
         "options": [["Inform the technician and head nurse the same day so pretreatment can be reviewed.", True, "Municipal changes can overwhelm pretreatment."],
                     ["Nothing; city water is safe.", False, "Safe to drink is not safe for dialysis."],
                     ["Stop all dialysis permanently.", False, "Not proportionate."],
                     ["Add bleach to the system.", False, "Never; not a nursing action."]], "sources": ["cdc_water"]},
        {"stem": "About how much dialysate passes the blood in a four-hour session at 500 mL/min?",
         "options": [["About 120 liters.", True, "500 mL × 240 minutes."],
                     ["About 12 liters.", False, "Ten times too low."],
                     ["About 1,200 liters.", False, "Ten times too high."],
                     ["About 1 liter.", False, "Far too low."]], "sources": []},
        {"stem": "Do live bacteria usually cross an intact dialyzer membrane?",
         "options": [["Rarely, but their fragments (endotoxins) can cause reactions.", True, "Pyrogenic reactions come from fragments."],
                     ["Always.", False, "Rarely."],
                     ["Never, so bacteria in water do not matter.", False, "Fragments matter."],
                     ["Only in peritoneal dialysis.", False, "Not relevant."]], "sources": ["iso23500_5"]},
        {"stem": "What does the nurse liaison do when a technician is not immediately available and a machine lacks release?",
         "options": [["Keep it out of use and use a released machine, escalating to the technician on call.", True, "Never bypass release."],
                     ["Release it herself after a visual check.", False, "Outside authority."],
                     ["Use it for low-risk patients only.", False, "No patient should be exposed."],
                     ["Cancel the patient's session.", False, "Use another released machine."]], "sources": [], "critical": True},
        {"stem": "What is the best portfolio measure for this role?",
         "options": [["Sessions started only after documented release, divided by affected sessions reviewed.", True, "Directly measures the safeguard."],
                     ["Number of water tests performed by the nurse.", False, "Not her role."],
                     ["Days without any machine downtime.", False, "May reward bypassing holds."],
                     ["Number of technicians employed.", False, "Not a safety measure."]], "sources": []},
    ],
    "exam": [
        {"stem": "Which is required before connecting a patient to a machine after disinfection?",
         "options": [["Signed release and a documented negative residual disinfectant test.", True, "Release evidence, not appearance."],
                     ["Normal conductivity only.", False, "Not release."],
                     ["The machine looks clean.", False, "Not release."],
                     ["The patient's consent.", False, "Not a substitute for release."]], "sources": [], "critical": True},
        {"stem": "What made the Caruaru center's water dangerous?",
         "options": [["It was supplied without treatment, filtration or chlorination, and contained microcystins.", True, "Water treatment failure."],
                     ["Too much fluoride.", False, "Not the finding."],
                     ["Reused dialyzers.", False, "Not the finding."],
                     ["Staff hand hygiene.", False, "Not the finding."]], "sources": ["caruaru1998"]},
    ],
}

# ── v2 completion (24 Nov 2026): second worked scenario ──
def _sec(sid):
    return next(s for s in MODULE["sections"] if s["id"] == sid)

_sec("verify")["html"] += """
<div class="tc-scene"><span class="tc-lab">No reagent, no result &middot; fictional</span><p>Monday, 5:45 a.m. Nurse Paolo, the water and equipment liaison, checks the water log before the first patients connect. The line for the total chlorine test after the carbon tanks reads "reagent out of stock, will test later." City water pressure was low over the weekend, and the technician on duty is new.</p><p>Paolo knows why the test matters: chloramine, used to disinfect city water, passes through the dialyzer if the carbon tanks are exhausted, damages red cells and can cause hemolysis, with symptoms that are easy to miss at first (chest or back pain, dark blood in the lines, a falling hemoglobin). He does not start any treatment. He calls the chief technician, who brings test strips from the second unit, runs the test, and records a result within the unit's limit at 6:20 a.m. The technician signs the release; the charge nurse confirms the start with the physician, as the unit protocol requires. Paolo writes the delay and its cause in the log and raises reagent stock as a supply hazard at the next quality meeting.</p><p class="tc-scene-take"><b>What this shows.</b> A missing result is not a normal result. The nurse does not run or interpret the water test; she makes sure the test is done and released before patients are exposed.</p></div>
"""
