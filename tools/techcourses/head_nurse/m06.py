# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 06: Water, Machines, and Supplies. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse and a water technician checking a chlorine test kit beside the carbon tanks in a dialysis water room.",
    "objectives": [
        "Explain why water that is safe to drink is not safe for dialysis.",
        "Name the main contaminants, the stage that removes each, and how each harms patients.",
        "Read the water log and machine records before opening, and treat a missing result as an abnormal one.",
        "Contain a shared hazard: hold new starts, protect connected patients, and list everyone exposed.",
        "State the three documents required before restart.",
        "Calculate reverse osmosis rejection and carbon contact time and say what a change means.",
    ],
    "big": """
{{plain:A person drinks about two liters of water a day, and the gut decides what gets in. A dialysis patient&rsquo;s blood meets about 120 liters of fluid in one session, separated only by a thin membrane that lets small molecules through. The water room is doing the job of the gut wall. If it fails, it fails for every patient on the shift at once.}}
<p>The picture has a limit. The gut can adapt and repair. A water system cannot. It only does what it was built and maintained to do, and it fails without warning.</p>
{{fig:hn06_volume}}
{{cards:Key terms for this module|Reverse osmosis (RO)::A membrane that removes most dissolved salts, metals, and microbes from water under pressure.|Carbon tank::A tank of activated carbon that removes chlorine and chloramine.|Chloramine::A disinfectant added by water utilities. It damages red blood cells.|Endotoxin::Fragments of bacterial cell walls that cross the membrane and cause fever and inflammation.|CFU/mL::Colony-forming units per milliliter, a count of live bacteria.|Action level::A result below the maximum limit that still triggers corrective action, usually half the limit.|Release::A signed decision by the designated person that water or a machine may be used.}}
""",
    "case": {"title": "It looks fine, says the voice on the phone", "html": """
<p>At 11:50, before the second shift, the technician, Mr. Jun Mendoza, tests total chlorine after the carbon tanks. The result is above the limit in the unit&rsquo;s procedure. The first-shift result at 5:30 was normal.</p>
<p>Three second-shift patients are already connected because they arrived early. Four are waiting. Mr. Mendoza calls the water consultant, who says on the phone: &ldquo;It&rsquo;s probably the test kit. It looks fine. Carry on and I&rsquo;ll come tomorrow.&rdquo;</p>
""", "questions": ["What do you do about the four waiting patients and the three who are connected?",
                  "Who else may have been exposed, and why?",
                  "What has to exist before the unit restarts?"]},
    "sections": [
        ("contaminants", "What can go wrong", "Each contaminant has a signature", """
<div class="table-wrap"><table>
<thead><tr><th>Contaminant</th><th>Source</th><th>What it does</th><th>How it presents</th></tr></thead>
<tbody>
<tr><td>Chlorine and chloramine</td><td>Added by the water utility. Removed by carbon</td><td>Damages hemoglobin and red cell membranes</td><td>Hemolysis: dark or cherry-red blood in the venous line, chest or back pain, breathlessness. Several patients at once. Poor response to anemia treatment over time</td></tr>
<tr><td>Aluminum</td><td>Utility treatment chemicals</td><td>Builds up in brain and bone</td><td>Confusion, bone disease, anemia, over months</td></tr>
<tr><td>Fluoride</td><td>Utility dosing errors</td><td>Binds calcium, affects the heart</td><td>Itching, chest pain, arrhythmia, arrest</td></tr>
<tr><td>Calcium and magnesium</td><td>Hard water. Removed by the softener</td><td>Hard water syndrome</td><td>Nausea, vomiting, high blood pressure, weakness</td></tr>
<tr><td>Bacteria and endotoxin</td><td>Biofilm in stagnant pipes, tanks, and bicarbonate</td><td>Endotoxin triggers inflammation</td><td>Chills and fever in the first hour, low pressure. Chronic inflammation</td></tr>
</tbody></table></div>
<p>Chloramine deserves its own sentence. Reverse osmosis does not reliably remove it. Carbon is the only barrier, carbon runs out without warning, and the test is the last line of defense. That is why total chlorine is tested before every shift.</p>
"""),
        ("train", "The treatment train", "How the system works, and what the standards say", """
{{fig:hn06_train}}
<p>Water passes through a sediment filter, a softener that protects the reverse osmosis membrane from scale, two carbon tanks in series, and the reverse osmosis unit. Product water goes to a loop that keeps it moving to the machines and back, because standing water grows biofilm.</p>
<p>The international standard is ISO 23500-3, reissued as a second edition in April 2024.[[hn_iso2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Fluid</th><th>Bacteria</th><th>Endotoxin</th></tr></thead>
<tbody>
<tr><td>Dialysis water</td><td>Under 100 CFU/mL</td><td>Under 0.25 EU/mL</td></tr>
<tr><td>Standard dialysis fluid</td><td>Under 100 CFU/mL</td><td>Under 0.5 EU/mL</td></tr>
<tr><td>Ultrapure dialysis fluid, needed for hemodiafiltration</td><td>Under 0.1 CFU/mL</td><td>Under 0.03 EU/mL</td></tr>
</tbody></table></div>
<p>Action levels are usually set at half the maximum, so the unit acts at 50 CFU/mL before the limit is reached. These standards come from outbreak investigations and expert consensus, not trials. No one will ever randomize patients to contaminated water. The limits that bind your unit are the ones adopted in its approved procedure under the DOH water order.[[hn_doh2013]] Know where that page is.</p>
"""),
        ("opening", "Before you open", "What you see with your own eyes before opening", """
<p>You do not run the water plant. You read its evidence, and you hold the floor when the evidence is missing.</p>
{{flow:Before opening|Chlorine::Total chlorine tested this shift, after the carbon, within limit, signed.|Softener and RO::Hardness and RO readings logged and within range.|Cultures and endotoxin::Latest results on file, none above action level without a documented response.|Machines::Disinfection complete, self-tests passed, repairs released in writing.|Concentrates::Match the orders. Bicarbonate mixed today and labeled.|Supplies::Emergency stock, expiry dates, and lot records in order.}}
<p>Record dialyzer and bloodline lot numbers for each patient and session, so that a recall can be traced in minutes. Where dialyzer reuse is approved, check patient identification, residual-disinfectant tests, and performance records every time.</p>
{{key:A missing result is an abnormal result. If you cannot see it, the gate is closed.}}
"""),
        ("hazard", "Containing a hazard", "When a result is abnormal or missing", """
<p>Do not start new patients on the affected system. For patients already connected, call the physician. Whether to stop, and whether to return blood, is a medical decision under the event algorithm. Blood is not returned when hemolysis is suspected.</p>
<p>Call the water or biomedical lead. Record the result, the sample point, the time, and every patient and station exposed since the last normal result. Arrange other capacity for waiting patients (Module 12).</p>
{{call:Stop and call the attending nephrologist and the clinical head as soon as a water result is above the adopted limit or is missing. Hold all new starts on the affected system. Do not return blood if hemolysis is suspected. Follow your unit&rsquo;s protocol while you call.}}
{{fig:hn06_restart}}
<p><strong>Restart requires three documents:</strong> the corrective action, a repeat test within the limit from the same sample point, and a release signed by the designated person. A phone call saying &ldquo;it looks fine&rdquo; is none of the three.</p>
"""),
        ("numbers", "Numbers to read", "Two numbers that show a system wearing out", """
{{formula:<strong>RO rejection</strong> = (1 &minus; product conductivity &divide; feed conductivity) &times; 100.<br>Feed 400 and product 12 &micro;S/cm gives 97%.<br><br><strong>Carbon contact time</strong> = total carbon volume (L) &divide; flow (L/min).<br>200 L &divide; 18 L/min = 11.1 minutes.}}
<p>A falling rejection trend means the RO membrane is failing even when today&rsquo;s product water still looks acceptable. The design standard for carbon contact time is at least 10 minutes in total at the highest flow the system will run, usually at least 5 minutes in each of two carbon tanks in series (a worker tank and a polisher tank), so that the second tank catches what breaks through the first.[[hn_cfr494]] Adding stations raises flow and quietly shortens contact time, so ask for it to be recalculated whenever the unit expands.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Waiting and connected patients.</strong> Hold the four waiting patients. The result is above the limit, and an opinion over the phone does not change it. Call the physician on duty about the three connected patients at once. Look at their venous lines for dark or cherry-red blood and ask about chest or back pain and breathlessness. Follow the physician&rsquo;s orders on stopping. If hemolysis is suspected, the blood is not returned.</p>
<p><strong>Who else was exposed?</strong> Every patient dialyzed since the last normal result at 5:30. Carbon can exhaust partway through a shift, so first-shift patients may have been exposed late in their sessions. List them by name, station, and time. The physician may order blood counts or other tests and calls to check on them at home.</p>
<p><strong>Before restart.</strong> The water lead switches or replaces the carbon and retests from the same sample point. Restart needs the corrective action record, the repeat test within the limit, and the signed release. Tell the consultant politely that the unit will restart when those three exist. Then add a question to the next quality meeting: why was the carbon not changed before it exhausted?</p>
"""],
    "skills": {"title": "Water event tabletop",
               "intro": "Lead a tabletop exercise with a mock water log and an abnormal result while your facilitator plays the technician and the physician.",
               "items": [
                   ("Reads the log and identifies the abnormal or missing result.", True),
                   ("Holds all new starts on the affected system.", True),
                   ("Calls the physician about connected patients and does not decide on blood return herself.", True),
                   ("States that blood is not returned if hemolysis is suspected.", True),
                   ("Calls the water or biomedical lead and the clinical head.", True),
                   ("Lists every patient exposed since the last normal result.", True),
                   ("Arranges or requests alternate capacity for waiting patients.", False),
                   ("Names the three documents required before restart.", True),
                   ("Declines to restart on a verbal assurance alone.", True),
                   ("Calculates RO rejection or carbon contact time from mock values.", False),
               ],
               "placement": "For two weeks, check the water log and machine release records yourself before every opening you lead. Record any gap and how it was closed."},
    "quiz": [
        ("Why is drinking water not safe for dialysis?",
         ["It tastes different", "The blood meets about 120 liters across a thin membrane, without the gut&rsquo;s protection", "It is too cold", "It contains too little sodium"], 1,
         "Small contaminants pass the membrane freely."),
        ("Which stage is the only reliable barrier to chloramine?",
         ["Softener", "Carbon tanks", "Reverse osmosis", "Sediment filter"], 1,
         "Reverse osmosis does not reliably remove chloramine."),
        ("Why is total chlorine tested every shift when cultures are monthly?",
         ["It is cheaper", "Carbon can exhaust within hours, and chloramine causes hemolysis", "Cultures are unreliable", "PhilHealth requires it"], 1,
         "The test is the last line of defense."),
        ("Three connected patients develop chest pain and dark, cherry-red blood in the venous lines. What is the rule about the blood?",
         ["Return it quickly", "Do not return it. Stop and clamp", "Return half", "Flush with saline and return"], 1,
         "Suspected hemolysis means the circuit is the cause."),
        ("What is the ISO limit for bacteria in dialysis water?",
         ["Under 10 CFU/mL", "Under 100 CFU/mL", "Under 1,000 CFU/mL", "Under 0.1 CFU/mL"], 1,
         "Endotoxin must be under 0.25 EU/mL."),
        ("Which fluid must be ultrapure?",
         ["Water for cleaning floors", "Fluid for hemodiafiltration", "Concentrate", "Drinking water"], 1,
         "High-volume HDF infuses fluid directly into the blood."),
        ("What is an action level?",
         ["The maximum limit", "A lower level, usually half the limit, that triggers corrective action", "The level at which the unit closes", "The patient&rsquo;s blood level"], 1,
         "It lets the unit act before the limit is reached."),
        ("Can yesterday&rsquo;s normal result clear today&rsquo;s abnormal one?",
         ["Yes", "No. Today&rsquo;s verification and the release process do", "Only if the consultant agrees", "Only for the first shift"], 1,
         "Each result stands for its own time."),
        ("How should a missing water result be treated?",
         ["As normal", "As abnormal", "As not needed", "As the technician&rsquo;s problem only"], 1,
         "If you cannot see it, the gate is closed."),
        ("What three documents are required before restart?",
         ["A phone call, a text, and an email", "Corrective action, a repeat test within limit, and a signed release", "The invoice, the roster, and the log", "Patient consent, a memo, and a photo"], 1,
         "A verbal assurance is none of them."),
        ("Feed conductivity is 400 and product is 12 &micro;S/cm. What is the RO rejection?",
         ["3%", "88%", "97%", "33%"], 2,
         "(1 &minus; 12 &divide; 400) &times; 100 = 97%."),
        ("Why must carbon contact time be recalculated when stations are added?",
         ["More stations use less water", "Higher flow shortens contact time", "Carbon expires faster", "It is a licensing formality"], 1,
         "Contact time is volume divided by flow."),
        ("What enables a fast, targeted recall of a dialyzer lot?",
         ["Keeping invoices", "Recording lot numbers for each patient and session", "Asking staff to remember", "Checking expiry dates"], 1,
         "Lot numbers link the product to the patients."),
        ("Two patients have chills and fever within the first hour. Which contaminant group comes first to mind?",
         ["Aluminum", "Bacteria and endotoxin", "Fluoride", "Calcium"], 1,
         "Endotoxin causes early pyrogenic reactions."),
        ("Who releases a water system after correction?",
         ["The head nurse", "The designated technical authority", "The administrator", "Any nurse"], 1,
         "You confirm that the signed release exists."),
    ],
    "terms": [("Reverse osmosis", "A membrane that removes most dissolved salts, metals, and microbes from water."),
              ("Carbon tank", "A tank of activated carbon that removes chlorine and chloramine."),
              ("Chloramine", "A water disinfectant that damages red blood cells."),
              ("Endotoxin", "Fragments of bacterial cell walls that cause fever and inflammation."),
              ("Action level", "A level below the limit that triggers corrective action."),
              ("Ultrapure dialysis fluid", "Dialysis fluid with very low bacteria and endotoxin, needed for hemodiafiltration."),
              ("Empty-bed contact time", "The time water spends in the carbon, equal to carbon volume divided by flow."),
              ("Hemolysis", "Breakdown of red blood cells, which releases their contents into the blood.")],
    "readings": [("dialysis-water-treatment-systems.html", "How dialysis water systems work."),
                 ("hemodiafiltration-new-standard.html", "Why hemodiafiltration needs ultrapure fluid."),
                 ("hemodialysis-complications.html", "Complications that can come from the fluid.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c8"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
