# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 03: The Order, the Machine, and the Record. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two nurses reading a dialysis order aloud against a machine screen before connecting a patient.",
    "objectives": [
        "Explain diffusion, convection, and ultrafiltration, and link each line of the dialysis order to one of them.",
        "Carry out a three-way check of order, machine, and patient before connection, and hold when they disagree.",
        "Calculate the urea reduction ratio and single-pool Kt/V, and judge whether the blood sample was valid.",
        "Summarize what the major trials of dose, time, temperature, and hemodiafiltration showed, including absolute effects.",
        "Audit delivered time against prescribed time and find the sessions that lose the most.",
        "Remove outdated documents that carry prescription details.",
    ],
    "big": """
{{plain:Every session exists three times: what the physician prescribed, what the nurse programmed, and what the patient actually received. Harm lives in the gaps between them.}}
<p>A wrong dialysis fluid potassium is a gap between the first and the second. A patient who leaves forty minutes early is a gap between the second and the third. Your job is to make all three visible on the same page.</p>
{{fig:hn03_three}}
{{cards:Key terms for this module|Diffusion::Movement of a dissolved substance from a high concentration to a low one across the membrane. It clears small molecules such as urea and potassium.|Convection::Solutes dragged across the membrane with water. It clears larger &ldquo;middle&rdquo; molecules better than diffusion.|Hemodiafiltration (HDF)::Dialysis that adds a large volume of convection, replaced with sterile fluid made on line.|Urea reduction ratio (URR)::The fraction by which blood urea falls during a session.|Kt/V::A measure of the dose of dialysis: clearance (K) times time (t), divided by the volume of body water (V).|Delivered time::The minutes the patient actually received, not the minutes prescribed.}}
""",
    "case": {"title": "Three hours or four", "html": """
<p>At 1:10 in the afternoon, Mr. Arnel Cruz, a nurse with eight months in the unit, is ready to connect Mr. Romeo Dizon, 66. The signed order, dated two weeks ago, says four hours. The machine is set for three. Mr. Cruz shows you the handover sheet taped to the station, which also says three hours.</p>
<p>You look at the last month of records for the afternoon shift. Seven of Mr. Dizon&rsquo;s twelve sessions were three hours. His last single-pool Kt/V, reported this week, was 1.08.</p>
""", "questions": ["What do you do before Mr. Dizon is connected?",
                  "What do you look at before anyone changes his prescription because of the low Kt/V?",
                  "What system problem does this case reveal, and how will you fix it?"]},
    "sections": [
        ("physics", "How it works", "What each line of the order does", """
<p>Blood leaves the patient, passes through thousands of hollow fibers in the dialyzer, and returns. Dialysis fluid flows around the fibers in the opposite direction, so the gradient stays steep along the whole fiber. Small molecules such as urea and potassium move from blood into the fluid by diffusion. Water is pushed out by pressure, which is ultrafiltration. Larger molecules are carried out with that water, which is convection.</p>
{{fig:hn03_circuit}}
<div class="table-wrap"><table>
<thead><tr><th>Line of the order</th><th>What it controls</th><th>What goes wrong when it is off</th></tr></thead>
<tbody>
<tr><td>Time</td><td>Total clearance, and how gently water can be removed</td><td>Less dialysis. A faster UF rate for the same fluid</td></tr>
<tr><td>Blood flow and dialyzer</td><td>Clearance per minute</td><td>Less dialysis. Strain on the access</td></tr>
<tr><td>Dialysis fluid potassium</td><td>The gradient pulling potassium out</td><td>Too low: a fast shift and arrhythmia. Too high: potassium left behind</td></tr>
<tr><td>Dialysis fluid sodium and temperature</td><td>Pressure stability and thirst</td><td>Low pressure, cramps, or more weight gain</td></tr>
<tr><td>Dry weight and UF goal</td><td>Volume</td><td>Low pressure, or overload that persists</td></tr>
<tr><td>Anticoagulation</td><td>Keeping the circuit open</td><td>Clotting and blood loss, or bleeding</td></tr>
</tbody></table></div>
<p>Each of these is the prescriber&rsquo;s decision. Your part is to make sure the machine carries out the order that exists today.</p>
{{scene:A blood flow nobody chose|<p>Mrs. Agnes Domingo&rsquo;s order says a blood flow of 350 mL/min. For three weeks, her nurses have been running 250, because her fistula has been hard to needle and the arterial pressure alarms at higher flows. Each nurse made a reasonable decision on the day. No one decided it for the whole three weeks.</p>
<p>Less blood through the dialyzer each minute means less urea removed each minute, so her Kt/V falls. The alarms themselves were a message: a narrowing in her access, which is exactly what Module 4 teaches you to look for. The fix is not to quietly keep running 250. It is to record the actual flow and the reason at every session, so that the trend reaches the nephrologist and the access is examined.</p>}}
"""),
        ("evidence", "The trials", "What the trials of dose, time, and modality showed", """
<p><strong>Dose.</strong> The Hemodialysis (HEMO) Study randomized 1,846 patients. Raising the dose from a single-pool Kt/V of 1.32 to 1.71 did not reduce deaths (relative risk 0.96; 95% confidence interval 0.84 to 1.10). High-flux membranes did not either.[[hn_eknoyan2002]] Since then the target has been a floor, not a race. The KDOQI 2015 guideline recommends a target single-pool Kt/V of 1.4 per session for patients dialyzing three times a week, with a minimum delivered dose of 1.2.[[hn_kdoqi2015]] Below the floor, the usual causes are short delivered time, recirculation in the access, low blood flow, and a bad sample.</p>
<p><strong>Time.</strong> Observational studies link longer sessions with better survival. The TiME trial randomized 266 units and 7,035 new patients, but the two groups received 216 and 207 minutes on average, a difference of nine minutes. It found no difference in death or admission and was stopped early.[[hn_dember2019]] The trial could not answer its question because the groups barely differed. It is not evidence that time does not matter.</p>
<p><strong>Cooler dialysis fluid.</strong> Cooling tightens the vessels and was expected to protect the heart. In MyTEMP, 84 centers were randomized to a cooler fluid policy or a standard one. Cardiovascular death or admission did not differ.[[hn_mytemp2022]] Cooling may still help an individual patient with frequent low pressure. It is not a proven default for everyone.</p>
<p><strong>Hemodiafiltration.</strong> In CONVINCE, 1,360 patients able to reach a convection volume of at least 23 liters were randomized to high-dose HDF or high-flux hemodialysis. Over a median of 30 months, death from any cause occurred in 17.3% with HDF and 21.9% with hemodialysis (hazard ratio 0.77; 95% confidence interval 0.65 to 0.93).[[hn_blankestijn2023]] The absolute difference is 4.6 percentage points, so about 22 patients would need HDF for 30 months to prevent one death. Quality of life declined in both groups, more slowly with HDF.[[hn_rose2024]] The benefit applies to high-volume HDF in patients with good access flow and requires ultrapure fluid (Module 6). A pooled analysis of the randomized trials is consistent with this.[[hn_vernooij2024]]</p>
<p>A trial comparing default dialysis fluid sodium of 137 and 140 mmol/L was still running on the review date. No default sodium is evidence-based yet.</p>
{{scene:The brochure with the big number|<p>Ms. Liza Ramos brings you a supplier&rsquo;s brochure. &ldquo;It says hemodiafiltration cuts deaths by 23%. Why aren&rsquo;t we doing it for everyone?&rdquo;</p>
<p>The 23% is the relative reduction from the CONVINCE trial. Turned into the absolute terms you just read, about 22 patients would need high-volume HDF for 30 months to prevent one death. The trial enrolled patients who could reach a high convection volume, which needs good access flow, and HDF needs ultrapure fluid and machines that can make it. So a fair answer is: &ldquo;There is good trial evidence for high-volume HDF in patients who can reach the volume. Before we offer it, we need ultrapure water, compatible machines, and a way to choose who can reach the volume. Let me bring this to the clinical head with the water results.&rdquo; That answer takes the evidence seriously without promising more than it shows.</p>}}
{{fig:hn03_trials}}
{{key:When you report a trial to an administrator, give the absolute difference and who was eligible, not only the relative reduction.}}
"""),
        ("check", "The three-way check", "The three-way check before connection", """
{{flow:Before connection|Identity::Two identifiers, checked against the order.|The order::The current signed order. Check the date and version, not the handover sheet.|The machine::Read the order aloud against the screen with a second nurse, as your double-check policy requires.|What is hung::The dialyzer and the concentrate actually on the machine.|The patient::Today&rsquo;s assessment from Module 2.|Mismatch::Any mismatch is a hold.}}
<p>When the order and the screen disagree, the order governs, provided it is clear and current. When the order itself is unclear, incomplete, or seems wrong for the patient today, call the prescriber. Nurses do not resolve a discrepancy by choosing the value that seems more sensible.</p>
<p><strong>During treatment</strong>, watch the trends, keep the access visible, and escalate chest symptoms, a change in consciousness, repeated low pressure, or bleeding under the approved algorithm. <strong>At disconnection</strong>, record actual minutes, actual fluid removed, the reason for any shortfall, bleeding control, post-treatment observations, and what the patient was told.</p>
{{call:Stop and call the prescriber when the current order is unclear, incomplete, or appears unsafe for the patient today. Do not connect until the order is clarified. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("dose", "Measuring the dose", "Measuring the dose, and why the sample matters", """
{{formula:<strong>Urea reduction ratio</strong> = (pre-dialysis urea &minus; post-dialysis urea) &divide; pre-dialysis urea.<br>From 60 to 18 mg/dL: (60 &minus; 18) &divide; 60 = 70%.<br><br><strong>Single-pool Kt/V</strong> (Daugirdas second-generation formula) = &minus;ln(R &minus; 0.008 &times; t) + (4 &minus; 3.5 &times; R) &times; UF &divide; W<br>where R = post &divide; pre urea, t = hours, UF = liters removed, W = post-dialysis weight in kg.<br>R = 0.30, 4 hours, 3 L, 60 kg gives 1.46.}}
{{fig:hn03_sample}}
{{scene:The Kt/V that was too good|<p>Mr. Felipe Ocampo&rsquo;s single-pool Kt/V has been between 1.10 and 1.18 for six months. This month it is 1.71. Nothing in his prescription changed.</p>
<p>A jump that large without a change in the order is more likely to be a sampling problem than better dialysis. You ask who drew the post-dialysis sample and how. A nurse in her second week drew it after the blood had been rinsed back with saline. The saline diluted the urea, which made the post value falsely low and the dose falsely high. The result is set aside, the sample is repeated by the unit&rsquo;s method, and the new nurse&rsquo;s sampling goes into her competency plan. Had anyone acted on the 1.71, they might have shortened a session that was already too short.</p>}}
<p>A result is only as good as the sample. The post-dialysis sample must be drawn by your unit&rsquo;s slow-flow or stop-dialysate method. A sample drawn at full blood flow with recirculation, or after the blood has been rinsed back with saline, gives a falsely low urea and a falsely good dose. When a result is surprisingly good or surprisingly bad, audit the sampling before anyone changes the prescription.</p>
<p>Then look at time. Delivered minutes divided by prescribed minutes, for each patient and each shift. A unit average of 97% can hide one shift where a third of patients lose thirty minutes to late starts.</p>
{{formula:<strong>Arithmetic illustration.</strong> One hour off a four-hour session removes a quarter of the diffusion time. For the same fluid goal, it raises the UF rate by a third.}}
"""),
        ("documents", "Stale documents", "Remove documents that carry old prescriptions", """
<p>Old handover sheets, laminated cards, and notes taped to machines are a common source of wrong settings. They are written once and never updated, and they look official.</p>
<p>Anything that carries prescription details must be version-controlled or removed. The working document at the chair is the current signed order. If staff need a quick-reference card, it should come from the order, carry a date, and be replaced every time the order changes.</p>
{{scene:The card on station 4|<p>Station 4 has a laminated card listing the usual settings for the patients on that chair. It was made last year and looks official. One line says that Mr. Rogelio Santos uses a dialysis fluid potassium of 2 mmol/L. Three months ago, after a low potassium, his nephrologist changed the order to 3.</p>
<p>A busy nurse who glances at the card instead of the order will set up the old prescription, and the machine will deliver it without complaint. You remove the card that afternoon. If the staff want a quick-reference sheet, it is printed from the current orders, dated, and replaced every time an order changes.</p>}}
{{key:If a piece of paper at the chair can disagree with the order, sooner or later it will.}}
"""),
    ],
    "debrief": ["""
<p><strong>Before connection.</strong> Hold. The signed order says four hours and is current. The machine and the handover sheet say three. The order governs, so the machine is set to four hours. You do not need to call the prescriber about the time, because the order is clear. You do need to tell the physician on duty about the low Kt/V and the shortened sessions today.</p>
<p><strong>Before anyone changes the prescription.</strong> Look at the sampling first: how was the post-dialysis sample drawn, and by whom? Then look at time: seven of twelve sessions ran an hour short, which alone can explain a low dose. Check blood flow and access function. A higher blood flow or a bigger dialyzer would not fix a problem caused by an hour missing from every other session.</p>
<p><strong>The system problem.</strong> An outdated handover sheet carried an old prescription, and nobody compared it with the order. Remove it through document control. Audit the afternoon shift&rsquo;s delivered time for all patients, not only Mr. Dizon. Coach Mr. Cruz on the three-way check (Module 8) without blame: he did what the paper at the station told him to do. The fix belongs to the system.</p>
"""],
    "skills": {"title": "Three-way check and session tracer",
               "intro": "Perform the pre-connection check on a simulated patient, then trace one synthetic session through order, machine log, and nursing record.",
               "items": [
                   ("Confirms identity with two identifiers against the order.", True),
                   ("Confirms the order is current by its date and version.", True),
                   ("Reads each line of the order aloud against the machine screen with a second nurse.", True),
                   ("Checks the dialyzer and concentrate actually hung.", False),
                   ("Holds the start when any value disagrees.", True),
                   ("Calls the prescriber when the order itself is unclear, and does not choose a value herself.", True),
                   ("Calculates URR and single-pool Kt/V from synthetic values.", False),
                   ("States how the post-dialysis sample should be drawn and how a wrong method changes the result.", True),
                   ("Calculates delivered time as a percentage and names the sessions that lost 30 minutes or more.", False),
                   ("Identifies at least one document at the station that could carry an outdated prescription.", False),
               ],
               "placement": "Audit delivered minutes for one shift for two weeks. Present the percentage, the sessions that lost 30 minutes or more, and their reasons to your facilitator."},
    "quiz": [
        ("Which process clears urea and potassium mainly?",
         ["Convection", "Diffusion", "Ultrafiltration", "Adsorption"], 1,
         "Small molecules move down their concentration gradient across the membrane."),
        ("Why does dialysis fluid flow opposite to the blood?",
         ["To cool the blood", "To keep the concentration gradient steep along the whole fiber", "To prevent clotting", "To reduce noise"], 1,
         "Countercurrent flow keeps fresh fluid meeting blood that still carries solute."),
        ("The signed order says four hours, the machine is set for three, and the handover sheet says three. What governs?",
         ["The handover sheet", "The machine", "The current signed order", "The nurse&rsquo;s judgment"], 2,
         "The current order governs when it is clear. Remove the outdated sheet."),
        ("When should the nurse call the prescriber about a mismatch?",
         ["Never", "When the order itself is unclear, incomplete, or seems unsafe today", "Only after the session", "Only for potassium"], 1,
         "A clear current order is simply followed. An unclear one is clarified."),
        ("Pre-dialysis urea is 80 and post-dialysis urea is 28 mg/dL. What is the URR?",
         ["28%", "52%", "65%", "35%"], 2,
         "(80 &minus; 28) &divide; 80 = 0.65."),
        ("A patient&rsquo;s Kt/V jumps from 1.25 to 1.9 with no change in prescription. What do you check first?",
         ["Raise blood flow", "The post-dialysis sampling method", "Shorten the session", "Report excellent adequacy"], 1,
         "A sample taken at full flow or after rinse-back gives a falsely good result."),
        ("What did the HEMO Study show?",
         ["Higher dose reduced deaths", "Higher dose and high-flux membranes did not reduce deaths", "Lower dose was safe", "Hemodiafiltration was better"], 1,
         "The relative risk of death with the higher dose was 0.96."),
        ("What is the KDOQI 2015 minimum delivered single-pool Kt/V for thrice-weekly dialysis?",
         ["0.8", "1.0", "1.2", "1.8"], 2,
         "The target is 1.4, with a minimum delivered dose of 1.2."),
        ("Why is the TiME trial weak evidence against longer sessions?",
         ["It was too small", "The two groups differed by only nine minutes", "It used the wrong outcome", "It was not randomized"], 1,
         "A trial cannot show the effect of a difference it did not achieve."),
        ("What did MyTEMP show about cooler dialysis fluid as a center-wide policy?",
         ["It halved cardiac deaths", "It did not reduce cardiovascular death or admission", "It was harmful", "It reduced infections"], 1,
         "It may still help an individual patient with frequent low pressure."),
        ("In CONVINCE, death was 17.3% with HDF and 21.9% with hemodialysis. What is the absolute difference?",
         ["23%", "4.6 percentage points", "0.77", "17.3%"], 1,
         "23% is the relative reduction, and 0.77 is the hazard ratio."),
        ("Which patients were eligible for CONVINCE?",
         ["All dialysis patients", "Patients able to reach a convection volume of at least 23 liters", "Only new patients", "Only patients with catheters"], 1,
         "High-volume HDF needs good access flow."),
        ("One hour is lost from a four-hour session with the same fluid goal. What happens to the UF rate?",
         ["It falls by a quarter", "It stays the same", "It rises by a third", "It doubles"], 2,
         "Four hours of work done in three is a third faster."),
        ("Unit delivered time is 97%. Why is that not enough?",
         ["It is too low", "An average can hide individual sessions that lose 30 minutes or more", "It should be 100% exactly", "It is not measured correctly"], 1,
         "Look at the sessions, not only the average."),
        ("What should happen to a laminated card at a station that lists dialysis settings?",
         ["Keep it as a backup", "Version-control it from the order or remove it", "Update it once a year", "Let the nurses decide"], 1,
         "Any paper at the chair that can disagree with the order eventually will."),
    ],
    "terms": [("Diffusion", "Movement of a dissolved substance from a high concentration to a low one across a membrane."),
              ("Convection", "Solutes carried across a membrane with water."),
              ("Ultrafiltration", "Removal of water from the blood by pressure across the membrane."),
              ("Hemodiafiltration", "Dialysis that adds a large volume of convection, replaced with sterile fluid made on line."),
              ("Urea reduction ratio", "The fraction by which blood urea falls during a session."),
              ("Kt/V", "A measure of dialysis dose: clearance times time, divided by body water."),
              ("Recirculation", "Cleaned blood re-entering the arterial needle, which lowers the real dose."),
              ("Document control", "A system that makes sure only current versions of documents are in use.")],
    "readings": [("high-flux-hd-optimization.html", "How the dialysis prescription is tuned."),
                 ("hemodiafiltration-new-standard.html", "The evidence for hemodiafiltration in more detail."),
                 ("hemodialysis-modalities.html", "The forms of hemodialysis and how they differ.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c1", "calc-dialysis-head-nurse-toolkit.html#c12"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
