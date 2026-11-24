# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 04: Protecting the Access. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse examining a forearm fistula with a stethoscope while the patient watches, the arm uncovered on a pillow.",
    "objectives": [
        "Examine a fistula, graft, and catheter, and name the findings that stop cannulation.",
        "Explain how narrowing, clotting, and aneurysm change what you see, hear, and feel.",
        "Explain why the venous pressure alarm can stay silent when a needle comes out.",
        "Lead the first minute of access bleeding or needle dislodgement.",
        "Summarize the Philippine and international evidence on catheter infection and how to reduce it.",
        "Keep a list of patients on long-term catheters with a plan for each.",
    ],
    "big": """
{{plain:A fistula is a high-flow shortcut built into a low-flow arm. The pump takes 250 to 400 milliliters of blood a minute from it and returns the same amount through a second needle. If the return needle slips out and the pump keeps running, the pump empties the patient onto the floor at pump speed.}}
<p>The picture has a limit. Water in a pipe has no defenses. The patient&rsquo;s blood pressure falls as blood is lost, which brings its own danger, and the patient may not feel the needle move.</p>
{{cards:Key terms for this module|Arteriovenous fistula (AVF)::A direct connection between an artery and a vein, usually in the arm, made by a surgeon.|Arteriovenous graft (AVG)::A synthetic tube joining an artery and a vein.|Thrill::The buzzing felt over a working access.|Bruit::The sound heard over a working access with a stethoscope.|Stenosis::A narrowing in the access or its vein.|Venous needle dislodgement (VND)::The return needle coming out of the vein during treatment.|Tunneled catheter::A catheter that runs under the skin before entering a large vein in the neck or chest, with a cuff that anchors it.}}
""",
    "case": {"title": "The blanket", "html": """
<p>It is a cold afternoon, and Mrs. Imelda Santiago, 72, has asked for a blanket. It covers her left arm, where both fistula needles sit. At 3:20 her nurse, Ms. Grace Aquino, is charting observations at the next station. Mrs. Santiago says she feels faint. She looks pale. You notice that the sleeve of her blouse, just above the blanket, is dark and wet.</p>
<p>The machine is running at a blood flow of 350 mL/min. No alarm is sounding.</p>
""", "questions": ["What do you do in the first sixty seconds, and in what order?",
                  "Why is no alarm sounding?",
                  "What will you change in the unit after Mrs. Santiago is safe?"]},
    "sections": [
        ("exam", "Look, listen, feel", "Examining the access before every cannulation", """
<p>A healthy fistula has a soft, continuous thrill and a low-pitched bruit through the whole heartbeat. The vein collapses when the arm is raised. A narrowing changes all of this, and the change tells you where the narrowing is.</p>
{{fig:hn04_llf}}
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>What it suggests</th></tr></thead>
<tbody>
<tr><td>Pulsatile access, high-pitched bruit heard only in systole, vein does not collapse when the arm is raised, bleeding after needle removal lasts longer than usual, rising venous pressures</td><td>A narrowing downstream, on the outflow side</td></tr>
<tr><td>Weak thrill, vein fills poorly, difficulty reaching the prescribed blood flow</td><td>A narrowing upstream, on the inflow side</td></tr>
<tr><td>No thrill, no bruit</td><td>Clotting</td></tr>
<tr><td>Thin, shiny, or scabbed skin over a bulge</td><td>An aneurysm at risk of rupture</td></tr>
<tr><td>Redness, warmth, discharge, pain</td><td>Infection</td></tr>
<tr><td>Cold, pale, numb, or painful hand</td><td>The fistula stealing blood from the hand</td></tr>
</tbody></table></div>
<p>A mature fistula is often described by the rule of sixes: flow above 600 mL/min, diameter at least 6 millimeters, depth no more than 6 millimeters. The KDOQI 2019 guideline moved away from &ldquo;fistula first&rdquo; toward an access plan built around each patient&rsquo;s life, and it relies on regular physical examination by trained staff as the core of monitoring.[[hn_lok2020]]</p>
{{scene:Twenty-five minutes of bleeding|<p>Mr. Nestor Aguilar&rsquo;s fistula has served him for four years. Over the past three weeks, his nurses have noticed that his needle sites bleed for 20 to 25 minutes after removal instead of the usual 10. His venous pressure at the same blood flow has crept from about 160 to about 210 mm Hg. The fistula now feels pulsatile, like a pulse rather than a buzz, and the vein stays full when he raises his arm.</p>
<p>Each finding alone could be dismissed. Together they point to one place: a narrowing downstream, on the outflow side, pushing pressure back into the access. The nurse who records the trend and raises it gives the nephrologist the chance to refer him for imaging and treatment of the narrowing while the fistula still works. The nurse who simply holds pressure longer each week waits for the morning it clots.</p>}}
{{call:Stop and call the attending nephrologist before cannulation for an absent thrill or bruit, scabbed or shiny skin over an aneurysm, signs of infection, or a cold, painful hand. Do not cannulate through or beside a scabbed aneurysm. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("alarm", "The silent alarm", "Why the alarm may not sound", """
<p>The venous pressure the machine reads comes mostly from the resistance of the needle and the line, not from the pressure inside the vein. When the needle slips out, that resistance is still there. The reading may fall only a little and stay inside the alarm window.</p>
{{fig:hn04_alarm}}
<p>In a bench simulation of 19 needle dislodgements under different pressures and flows, the machine alarm sounded in only 8, or 42%.[[hn_frinak2023]] This was a simulation, not a study of patients, but it matches the experience of many units and the advice of the American Nephrology Nurses Association task force.[[hn_speranzareid2021]]</p>
{{formula:<strong>Blood-loss clock.</strong> Pump speed (mL/min) &times; minutes unobserved.<br>350 mL/min &times; 4 minutes = 1,400 mL. For a 55-kg patient with about 3,850 mL of blood, that is more than a third.}}
<p>The protection is human, not mechanical. No blanket over the access, ever. Lines taped by the unit&rsquo;s method, with no tension. Venous alarm limits set close to the running pressure. And every observation round includes looking at the needle sites.</p>
{{key:The only reliable detector of a dislodged needle is a nurse who can see the access.}}
"""),
        ("bleed", "First minute", "The first sixty seconds of access bleeding", """
{{fig:hn04_bleed}}
{{flow:Access bleeding or needle dislodgement|Stop::Stop the blood pump.|Clamp::Clamp both lines near the access.|Press::Firm, direct pressure on the site with gauze.|Call by name::&ldquo;Grace, call the physician on duty and tell me when you have reached him.&rdquo;|Lay flat::Lay the patient flat and check pressure, pulse, and consciousness.|Save::Keep the needle, the tape, and the lines. Record the times.}}
<p>Do not restart, and do not return blood through a needle that has been out of the vein. The physician decides whether and how the session continues. Module 7 covers the team roles when the bleeding is severe.</p>
<p>A ruptured aneurysm bleeds fast and does not stop easily. Teach patients and families to press hard with a clean cloth and call for emergency help.</p>
{{scene:The drill that took 95 seconds|<p>On a quiet Thursday, you run an unannounced drill with a practice arm and a circuit filled with colored water. You tell a nurse, &ldquo;The venous needle is out. Go.&rdquo; She looks for gauze first, then for gloves, then stops the pump. Ninety-five seconds pass before the pump stops. At 300 mL/min, that would have cost close to half a liter.</p>
<p>No one is blamed. You talk through the order: pump first, because the pump is what moves the blood. The gauze can wait the three seconds it takes to press a button. The next week, the same nurse stops the pump in under ten seconds. The drill takes five minutes and costs nothing. Repeated every month with different nurses, it turns a written flow into a reflex.</p>}}
"""),
        ("catheters", "Catheters", "Catheters: the access with the most infection", """
<p>A catheter gives organisms a plastic surface on which to build a slimy layer called a biofilm. For catheters used for months, most bloodstream infections start inside the lumen, from the hub each time it is opened. That is why hub handling matters more than the dressing.</p>
<p>Unplanned starts are common in this region. About 70% of patients in lower and lower-middle income countries of South and Southeast Asia start hemodialysis without a prepared access.[[hn_ramachandran2022]] Many units therefore carry many catheters for many months.</p>
<div class="table-wrap"><table>
<thead><tr><th>Evidence</th><th>Finding</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Philippine single-center cohort</td><td>6.72 catheter-related bloodstream infections per 1,000 catheter-days, mortality 6.09%. Gram-negative organisms were most common, including <em>Burkholderia cepacia</em> complex, <em>Enterobacter</em>, and <em>Acinetobacter</em>. Using the catheter for transfusion or intravenous medicines was a risk factor[[hn_pasilan2024]]</td><td>One center. May not represent your unit</td></tr>
<tr><td>Antimicrobial barrier caps, United States</td><td>0.26 vs 0.59 positive blood cultures per 1,000 catheter-days with chlorhexidine-coated caps[[hn_hymes2017]]. A second trial compared them with another connector system[[hn_brunelli2018]]</td><td>Cluster-randomized. Industry-linked. Check local availability and cost</td></tr>
<tr><td>Buttonhole versus rope-ladder cannulation</td><td>No consistent pain benefit in randomized trials, and more infection with buttonhole[[hn_wong2014]]</td><td>Systematic review</td></tr>
</tbody></table></div>
<p>The gram-negative pattern in the Philippine cohort points toward water, solutions, and multidose containers as possible sources. That is an inference from the organisms, not a finding of the study. It is why Module 5 treats medicine preparation as part of access care.</p>
<p>The dialysis catheter is for dialysis. Using it for transfusion or other infusions needs an explicit order and the same aseptic technique.</p>
{{scene:The transfusion overnight|<p>Mr. Danilo Reyes, 60, dialyzes through a tunneled neck catheter. He was admitted overnight for anemia, and the ward ran a unit of blood through his dialysis catheter because his arm veins were hard to find. At his next session, 40 minutes after connection, he shivers and his temperature is 38.6 &deg;C.</p>
<p>The nurse calls the physician, who orders blood cultures from the catheter and a vein and starts treatment. You record that the catheter was used for a transfusion, by whom, and when, because the Philippine cohort found exactly this to be a risk factor. Then you act on the system: a label on every dialysis catheter that reads &ldquo;For dialysis only,&rdquo; a note to the wards that refer patients to your unit, and a line in the discharge summary template. One infection is a patient event. A label prevents the next one.</p>}}
"""),
        ("list", "The catheter list", "Keep a list of every long-term catheter", """
<p>Each month, list every patient dialyzing through a catheter for more than 90 days. For each one, record the reason and the next step toward a permanent access: vein mapping, surgical referral, a maturing fistula, or a documented decision to stay with a catheter.</p>
{{formula:<strong>Catheter dependence</strong> = patients on a catheter more than 90 days &divide; all patients.<br>9 of 95 = 9.5%.}}
<p>The list belongs to the nephrologists and the access surgeon as much as to you. Your contribution is to keep it current and to bring it to the monthly review, so that no catheter stays in by default.</p>
{{scene:Seven months by default|<p>At the monthly review, the catheter list shows that Mrs. Erlinda Castro has dialyzed through a catheter for seven months. Vein mapping was done in May. A referral to the access surgeon was written the same week. Nothing has happened since.</p>
<p>No one decided that Mrs. Castro should keep a catheter. The referral was simply lost between visits. When the nurse asks her, Mrs. Castro says she could not afford the surgeon&rsquo;s fee and was embarrassed to say so. The nephrologist asks the social worker to help with coverage and a referral to a government hospital, and a fistula is created in September. Without the list, the eighth month and the ninth would have passed the same way.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The first sixty seconds.</strong> Pull back the blanket and call for help in the same motion. Stop the blood pump, clamp both lines, and press hard on the site. Name your helpers: Ms. Aquino on the site, another nurse on Mrs. Santiago&rsquo;s airway, pressure, and consciousness, someone to call the physician on duty, and one nurse to watch the other patients. Lay her flat. Do not return blood through the needle that came out.</p>
<p><strong>Why no alarm?</strong> The venous pressure reading comes mostly from needle resistance, so it may stay inside its window after the needle leaves the vein. At 350 mL/min, a few unobserved minutes can cost more than a liter. Use the blood-loss clock to estimate how much, and tell the physician.</p>
<p><strong>What changes?</strong> This is a system failure, not one nurse&rsquo;s. Make &ldquo;access visible&rdquo; an item on the observation round sheet. Offer warmer alternatives that leave the arm uncovered: a blanket tucked below the elbow, a warmer room for older patients. Review taping and alarm-limit practice. Then measure: audit visible access at random times for a month (Module 11).</p>
"""],
    "skills": {"title": "Access examination and bleeding response",
               "intro": "Examine a fistula on a volunteer patient or model, then respond to a simulated dislodgement while your facilitator observes.",
               "items": [
                   ("Looks at the skin, the arm, and the hand before touching.", True),
                   ("Feels the thrill and listens to the bruit along the whole access.", True),
                   ("Performs the arm elevation test and states what it shows.", False),
                   ("Names each finding that stops cannulation.", True),
                   ("Recognizes the simulated bleed without waiting for an alarm.", True),
                   ("Stops the pump, clamps both lines, and applies direct pressure in that order.", True),
                   ("Calls for help by name and asks for a report back.", True),
                   ("Lays the patient flat and checks pressure, pulse, and consciousness.", False),
                   ("Does not restart or return blood through the dislodged needle.", True),
                   ("Estimates blood loss with the blood-loss clock.", False),
                   ("Keeps the needle, tape, and lines and records the times.", False),
               ],
               "placement": "For one month, check at random times whether every access on the floor is visible. Record the result per round and share it with the team weekly."},
    "quiz": [
        ("What does a healthy fistula feel and sound like?",
         ["Pulsatile with a high-pitched systolic bruit", "A soft continuous thrill and a low-pitched continuous bruit", "No thrill and no bruit", "A weak thrill only"], 1,
         "Flow continues through the whole heartbeat."),
        ("A fistula is pulsatile, the bruit is high-pitched and systolic only, and bleeding lasts longer after needle removal. What is likely?",
         ["Normal fistula", "Narrowing on the outflow side", "Infection", "Steal"], 1,
         "Downstream narrowing raises pressure in the access."),
        ("The usual thrill is absent before treatment. What do you do?",
         ["Cannulate with smaller needles", "Do not cannulate and call for urgent review", "Massage the access", "Raise the blood flow"], 1,
         "No thrill suggests clotting."),
        ("You see shiny, scabbed skin over a fistula bulge. What is correct?",
         ["Cannulate beside it", "Cannulate through it", "Do not cannulate there, arrange urgent review, and teach direct pressure", "Cover it and proceed"], 2,
         "Scabbed skin over an aneurysm signals a risk of rupture."),
        ("Why can the venous pressure alarm stay silent when the needle comes out?",
         ["Alarms are often off", "Most of the reading is needle and line resistance, which does not change", "Blood clots at once", "The pump stops automatically"], 1,
         "The reading may stay inside its alarm window."),
        ("In the bench simulation, how often did the machine alarm sound after dislodgement?",
         ["Every time", "In 8 of 19 cases", "Never", "In 18 of 19 cases"], 1,
         "It sounded in 42% of simulations."),
        ("The pump runs at 300 mL/min and a dislodgement goes unnoticed for 5 minutes. What is the potential loss?",
         ["300 mL", "600 mL", "1,500 mL", "3,000 mL"], 2,
         "300 &times; 5 = 1,500 mL."),
        ("What is the first action when a needle site bleeds heavily?",
         ["Call the physician", "Stop the blood pump", "Remove the other needle", "Raise the arm"], 1,
         "Stopping the pump stops the loss from the circuit. Clamp, press, and call follow at once."),
        ("Why is a blanket over the access arm unsafe?",
         ["It cools the access", "It hides bleeding that the alarm may not detect", "It raises venous pressure", "It is against PhilHealth rules"], 1,
         "Only a visible access protects against silent bleeding."),
        ("For catheters used for months, where do most bloodstream infections start?",
         ["At the exit site", "Inside the lumen, from the hub", "In the dialyzer", "In the skin of the arm"], 1,
         "That is why hub handling matters most."),
        ("What did the Philippine catheter cohort report?",
         ["Mostly gram-positive infections", "6.72 infections per 1,000 catheter-days, mostly gram-negative", "No deaths", "Infections only in the first week"], 1,
         "Use of the catheter for transfusion or medicines was a risk factor."),
        ("What should the gram-negative pattern make you audit?",
         ["Hand cream", "Water, solutions, multidose containers, and non-dialysis use of the catheter", "The dialysis machine paint", "Patient diet"], 1,
         "This is an inference from the organisms, not a study finding."),
        ("What did the systematic review find about buttonhole cannulation?",
         ["Less pain in randomized trials", "No consistent pain benefit in randomized trials and more infection", "Fewer aneurysms", "Better flow"], 1,
         "Use it only for selected patients under a strict protocol."),
        ("What did the KDOQI 2019 guideline change about access planning?",
         ["Fistula for everyone", "An access plan built around each patient&rsquo;s life", "Catheters first", "No physical examination"], 1,
         "It replaced fistula first with an individualized life plan."),
        ("Nine of 95 patients have had a catheter for more than 90 days. What is the catheter dependence?",
         ["9%", "9.5%", "90%", "0.95%"], 1,
         "9 &divide; 95 = 9.5%."),
    ],
    "terms": [("Arteriovenous fistula", "A direct connection between an artery and a vein, made by a surgeon."),
              ("Arteriovenous graft", "A synthetic tube joining an artery and a vein."),
              ("Thrill", "The buzzing felt over a working access."),
              ("Bruit", "The sound heard over a working access."),
              ("Stenosis", "A narrowing in the access or its vein."),
              ("Aneurysm", "A bulging segment of the access."),
              ("Venous needle dislodgement", "The return needle coming out of the vein during treatment."),
              ("Biofilm", "A slimy layer of organisms that grows on plastic and resists antibiotics.")],
    "readings": [("hemodialysis-access-lifeline.html", "Making the access last a lifetime."),
                 ("dialysis-access-care.html", "Caring for the access at home."),
                 ("dialysis-access-infection.html", "Access infection, its signs, and its prevention.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c7", "calc-dialysis-head-nurse-toolkit.html#c6"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
