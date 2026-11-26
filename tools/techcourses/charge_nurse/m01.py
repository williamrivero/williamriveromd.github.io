# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 01: Taking Charge. Written for this series from published sources."""

MODULE = {
    "image_alt": "A night-shift nurse handing a clipboard and keys to the incoming charge nurse at the entrance of a quiet dialysis unit before dawn.",
    "objectives": [
        "Tell the charge nurse role apart from the head nurse, the physician on duty, the attending nephrologist, and the technical staff, and say who decides what.",
        "Read a requirement by its issuer, jurisdiction, scope, clause, and version, and tell a regulation from payer policy, professional guidance, and employer policy.",
        "Explain the Department of Health (DOH) station-based limit and the Philippine Society of Nephrology (PSN) patient-based ratio, and why one cannot quietly replace the other.",
        "Use the authority to pause with a four-part statement: hazard, protection now, help needed, and recheck time.",
        "Record a decision so that the next charge nurse does not have to rebuild it at 5:35 in the morning.",
    ],
    "big": """
{{plain:Think of the charge nurse as the air-traffic controller of the dialysis floor. The controller does not fly any plane, design the runway, or repair an engine. The controller knows where every plane is, which runway is open, and which pilot can land in fog, and can hold a plane on the ground until it is safe.}}
<p>The picture has a limit. A controller watches screens and has no plane of her own. A charge nurse usually also has two or three patients of her own, so her attention is split. And unlike a control tower, a hemodialysis (HD) unit has no system that stops two machines from going wrong at the same minute. The charge nurse&rsquo;s tools are the opening checks, the assignment, the habit of walking the floor, and clear words to the people who hold each decision. Your work in this module is to know which decisions are yours, which belong to someone else, and how to say so out loud when the two collide.</p>
{{cards:Key terms for this module|Charge nurse::The registered nurse who coordinates one shift: who works where, what is checked, and who is called.|Head nurse::The nurse who leads the unit over time: staffing, training, audits, and improvement.|Physician on duty (POD)::The physician present or on call for the shift, who answers clinical questions and gives orders.|Attending nephrologist::The physician responsible for each patient&rsquo;s plan and prescription.|Technical release::A signed statement from the authorized technical staff that water or a machine is fit to use.|Escalation::Moving a problem to the person who can decide it, with the facts they need.|Requirement register::A table of the rules the unit follows, each with its source, clause, owner, and review date.}}
""",
    "case": {"title": "&ldquo;Use the PSN ratio today&rdquo;", "html": """
<p>It is Monday, 5:35 in the morning, at a 16-station hospital-based unit in Pampanga. Nurse Carmela Dizon takes charge. Two nurses have called in sick. Four nurses are present, including Carmela, plus one nursing assistant. Sixteen patients are booked for the first shift.</p>
<p>The administrator sends a text message: &ldquo;PSN allows 1:6 if there is an assistant. Open all 16.&rdquo; The licensing file on the shelf shows the DOH order with a nurse-to-station limit of 1:4. One of the four nurses is in her third week of orientation and has never connected a catheter alone.</p>
""", "questions": ["What exactly does each source count, and who issued it?",
                  "Can Carmela open all sixteen stations, and with whom carrying how many?",
                  "What does she say, to whom, and what does she write down?"]},
    "sections": [
        ("lanes", "Who decides what", "Four lanes on every shift", """
<p>Four lanes run through every dialysis shift. The <strong>attending nephrologist</strong> decides each patient&rsquo;s plan: the prescription, the dry weight, the medicines. The <strong>medical director or Dialysis Clinical Head</strong> sets unit policy. The <strong>water and biomedical staff</strong>, under the director, release water and machines. The <strong>charge nurse</strong> verifies, coordinates, holds, and escalates.</p>
{{fig:cn01_lanes}}
<p>Most charge-nurse mistakes are lane mistakes, not knowledge mistakes. A charge nurse who types a new dry weight on a verbal word, or plugs in a machine the technician tagged &ldquo;do not use,&rdquo; has left her lane. She may even be right about the patient. The record will still show that the decision was made by someone who did not hold it.</p>
<p>Charge duty is a role a staff nurse takes for a shift. The head nurse post is different. The PSN 2024 standards describe a head nurse with continuing responsibility for staffing, teaching, infection control, and improvement, and with entry requirements of structured renal nursing training of three months or more, current life support certificates, and two years of dialysis experience.[[psn2024]] Taking charge for a day does not make anyone a head nurse, and the head nurse track in this Academy covers that role.</p>
{{scene:The verbal dry weight|<p>At 6:20 the physician on duty, still on the ward, calls Nurse Jomar Pineda, who is in charge. &ldquo;Mrs. Aquino&rsquo;s dry weight is too high. Make it 52.5 in the system, I&rsquo;ll sign later.&rdquo;</p>
<p>Jomar reads it back: &ldquo;Mrs. Aquino, Bed 8, dry weight from 54.0 to 52.5 kilograms, effective today.&rdquo; He writes it as a verbal order with the time and the doctor&rsquo;s name, follows the unit&rsquo;s verbal-order procedure, and flags it on the board for countersignature before the doctor leaves the building. He does not quietly edit the prescription screen as if he had decided it. The decision stays in the doctor&rsquo;s lane; the safe recording of it is in Jomar&rsquo;s.</p>}}
{{key:Verify, hold, escalate. If a decision is not in one of those three words, ask whose lane it is.}}
"""),
        ("rules", "Reading a rule", "Read a rule by who wrote it", """
<p>Not every rule carries the same weight. A <strong>DOH administrative order</strong> is a licensing condition: the facility must meet it to keep its license to operate. A <strong>PhilHealth circular</strong> is payer policy: it decides what is reimbursed, not how a shift is staffed. A <strong>PSN guideline</strong> is professional guidance. An <strong>employer memo</strong> is local policy. These answer different questions, and people under pressure often quote the one that suits them.</p>
<p>Before you act on a rule that someone quotes at you, ask five things:</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Who issued it?</td><td>A regulator, a payer, a society, or your employer carry different authority.</td></tr>
<tr><td>Where does it apply?</td><td>A rule for hospital units may not cover freestanding units, and foreign rules do not apply here.</td></tr>
<tr><td>What does it cover?</td><td>Stations or patients? Shifts or days? Staff nurses or all nurses?</td></tr>
<tr><td>Which clause?</td><td>&ldquo;PSN says&rdquo; is not a citation. The section number is.</td></tr>
<tr><td>Which version?</td><td>An older edition may have been replaced.</td></tr>
</tbody></table></div>
<p>A <strong>requirement register</strong> keeps these answers in one place: the rule, the source, the exact clause, what it means for your unit, who owns the interpretation, and when it is next reviewed. The head nurse usually keeps it. The charge nurse is the person who most often needs it at short notice.</p>
{{scene:&ldquo;PhilHealth requires two nurses per patient&rdquo;|<p>A new administrative officer tells the charge nurse that PhilHealth requires a certain staffing level, or the claims will be denied. The charge nurse asks for the circular number. The officer cannot find it.</p>
<p>The head nurse later checks: the PhilHealth hemodialysis circular sets the covered sessions and the payment per session; staffing for licensing is in the DOH order.[[hn_philhealth2024]][[doh2012]] The officer was mixing a payer rule with a licensing rule. Nobody was lying. The five questions found the mix-up in one day instead of one argument per shift.</p>}}
"""),
        ("ratios", "The two ratios", "The two staffing ratios, side by side", """
<p>DOH Administrative Order (AO) 2012-0001 sets a nurse-to-hemodialysis-station ratio no greater than 1:4 per shift, and requires at least one nurse trained in Advanced Cardiovascular Life Support (ACLS) on each shift.[[doh2012]] The PSN 2024 standards discuss a ratio of one nurse to four patients, with an exception of one nurse to six patients when a nursing assistant is present.[[psn2024]]</p>
{{fig:cn01_ratios}}
<p>Look at what each counts. The DOH order counts <em>stations</em>. The PSN text counts <em>patients</em>. Look at who wrote each. DOH is the regulator that licenses the facility; PSN is a professional society. A professional recommendation does not amend a licensing order. Until the DOH regional licensing office, or the facility&rsquo;s compliance lead with a written interpretation from it, says otherwise, the stricter licensing condition is the one an inspector will apply.</p>
<p>A ratio is a ceiling, not a target. Four stable patients with mature fistulas are not the same load as four patients with new catheters, one of whom drops her pressure every session. Module 3 builds the assignment by need. The ratio only tells you when you have run out of room.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>What it counts</th><th>What it says</th><th>Authority</th></tr></thead>
<tbody>
<tr><td>DOH AO 2012-0001</td><td>Stations per shift</td><td>No more than 1 nurse to 4 stations; at least one ACLS-trained nurse per shift</td><td>Licensing condition</td></tr>
<tr><td>PSN 2024 standards</td><td>Patients</td><td>1 nurse to 4 patients; 1 to 6 when a nursing assistant is present</td><td>Professional guidance</td></tr>
</tbody></table></div>
{{key:When two rules disagree, do not pick the convenient one. Show both, apply the licensing condition, and ask for a written interpretation.}}
"""),
        ("evidence", "What staffing does", "What the evidence says about staffing and harm", """
<p>Why does a ratio matter at all? Because thin staffing turns into missed checks. In surveys of United States dialysis nurses, those who cared for more patients, and who reported more care left undone, also reported more adverse events: hypotension, missed treatments, and patient complaints.[[hn_thomashawkins2008]][[hn_thomashawkins2020]] In a cross-sectional study of 21,839 Korean patients, units in which every nurse had at least two years of dialysis experience met more targets for dialysis dose, blood pressure, and albumin.[[hn_jeong2023]] These are associations, not trials, and dose and albumin are surrogate markers. The mechanism is still plausible: fewer experienced eyes, more missed checks.</p>
<p>These studies are cross-sectional. They show an association, not proof that adding one nurse prevents one event. Better-run units may simply staff better and do everything else better too. Still, the direction is consistent across countries, and it matches what nurses see on the floor: when there are too few hands, the checks that take a minute are the first to go.</p>
<p>The Philippine context makes this sharper. The DOH estimated a national shortage of about 106,000 nurses in 2022, and a 2026 newspaper editorial reported a Commission on Higher Education estimate of a gap of up to 190,000 in 2025.[[cn_doh_shortage2022]][[cn_philstar2026]] A charge nurse cannot fix the shortage. She can refuse to let it become invisible, by stating clearly on each short-staffed morning what is safe to open and what is not.</p>
"""),
        ("pause", "The authority to pause", "The authority to pause, and how to use it", """
<p>Before you accept charge for the first time, find out three things: your written job description, the escalation ladder with working phone numbers, and whether you may pause an unsafe activity. If nobody can answer the third question, ask the head nurse to put the answer in writing. A charge nurse without the authority to pause is a coordinator with responsibility and no tools.</p>
<p>When you pause, use four parts:</p>
{{fig:cn01_pause}}
{{flow:The four-part pause|Hazard::&ldquo;Beds 13 to 16 have no nurse who can work alone.&rdquo;|Protection now::&ldquo;I have not connected them.&rdquo;|Help needed::&ldquo;I need one more nurse, or approval to move four patients to a later slot.&rdquo;|Recheck time::&ldquo;I will call you back at 6:00.&rdquo;}}
<p>&ldquo;We are short today&rdquo; is a feeling. The four-part statement is a decision someone can act on. It also protects you: it shows that you saw the hazard, protected the patients, asked for what you needed, and set a time to look again.</p>
{{scene:The 5:50 call|<p>Nurse Ellen Ramos is in charge at a freestanding unit in Bulacan. At 5:50 she calls the head nurse at home: &ldquo;Ma&rsquo;am, the hazard is that Kris is sick and Beds 9 to 12 have only the orientee, who is not signed off for catheters; two of them are catheter patients. I have not connected Beds 9 to 12. I need Arnel from the afternoon shift to come in early, or your approval to move those four to the 10:30 slot. I&rsquo;ll call you back at 6:10 with what I&rsquo;ve arranged.&rdquo;</p>
<p>The head nurse calls Arnel. Ellen writes two lines in the shift log. Nobody had to guess what she needed.</p>}}
"""),
        ("record", "Writing it down", "Write the decision down", """
<p>Record the rule you applied, the person you called, what was decided, who decided it, and the time. One line in the shift log is enough for most decisions. A staffing decision that left patients waiting, or moved them, deserves a line in the requirement register too, so the question is not argued again next Monday.</p>
<p>Good records are short and factual. &ldquo;5:50 called head nurse re: 3 RNs + 1 orientee for 16 stations. DOH 1:4 stations applied. Head nurse approved early call-in of Arnel. Beds 13&ndash;16 started 6:40.&rdquo; Anyone who reads that line next month knows what happened and why.</p>
{{key:If it is not written, the next charge nurse will have to decide it again, probably at 5:35 in the morning.}}
"""),
    ],
    "debrief": ["""
<p><strong>What each source counts, and who issued it.</strong> The DOH order counts stations and is a licensing condition. The PSN text counts patients and is professional guidance. The administrator is quoting the PSN exception as if it were the operating rule. Carmela does not argue about whether 1:6 is reasonable; she shows what each document says.</p>
<p><strong>Can she open all sixteen?</strong> By the station rule, four nurses cover at most sixteen stations: 16 &divide; 4 = 4 per nurse. On paper this passes. Now subtract what paper hides. Carmela is one of the four, and on a busy opening the charge role takes a large share of her time, so she can safely carry two or three chairs, not four. The orientee can carry four only if none of them is a catheter patient. And at break time, two nurses will each cover eight running machines for half an hour unless breaks are staggered. A safer plan: open fourteen stations now, with Carmela carrying two; ask the attending nephrologist which two patients can safely move to a 10:30 start or the second shift; and stagger breaks so that no nurse ever covers more than four running machines (Toolkit #c1 and #c3).</p>
<p><strong>What she says and writes.</strong> She calls the administrator: the licensing condition is 1:4 stations; a society exception does not amend it; she will open fourteen safely and move two with the attending&rsquo;s agreement. She records the call in the shift log and asks the head nurse to obtain a written interpretation from the regional licensing office, so the question is settled once.</p>
"""],
    "skills": {"title": "Taking charge: lanes, rules, and the pause",
               "intro": "A facilitator plays the administrator, the physician on duty, and the head nurse. Use the opening case and two other short-staffed mornings.",
               "items": [
                   ("States the four decision lanes and gives an example of each.", True),
                   ("Classifies a quoted requirement by issuer, jurisdiction, scope, clause, and version.", False),
                   ("Explains why the PSN 1:6 exception does not override the DOH station limit.", True),
                   ("Calculates stations per independent nurse, including the charge nurse&rsquo;s own load and break cover.", True),
                   ("Gives a four-part pause statement aloud, with a recheck time.", True),
                   ("Records a verbal order with read-back and flags it for countersignature.", True),
                   ("Writes a one-line shift-log entry for a staffing decision.", False),
                   ("Completes a requirement register entry with an owner and a review date.", False),
               ],
               "placement": "On two supervised shifts, write down every rule someone quotes to you and check its source the same day with the head nurse."},
    "quiz": [
        ("Which document can relax a DOH licensing ratio?",
         ["A PSN guideline", "An employer memo", "An official DOH amendment or written DOH interpretation", "A PhilHealth circular"], 2,
         "Only the regulator can change its own licensing condition."),
        ("What does the DOH ratio in AO 2012-0001 count?",
         ["Patients", "Stations per shift", "Sessions per day", "Machines in storage"], 1,
         "It sets a limit of one nurse to four hemodialysis stations per shift."),
        ("Which decision belongs to the charge nurse?",
         ["Changing the dialysis fluid potassium", "Releasing a repaired machine", "Holding a connection until a release is signed", "Granting an exception to the ratio"], 2,
         "Verify, hold, and escalate are the charge nurse&rsquo;s tools."),
        ("What does completing this track mean?",
         ["Appointment as head nurse", "An educational record; appointment is the employer&rsquo;s separate decision", "PSN accreditation", "Continuing professional development units"], 1,
         "No appointment, license, or accreditation follows from completing a study series."),
        ("Which is the best escalation statement?",
         ["&ldquo;We are short today.&rdquo;", "&ldquo;Beds 13 to 16 have no independent nurse; I have not connected them; I need one nurse or approval to move four patients; I will call back at 6:00.&rdquo;", "&ldquo;Please help.&rdquo;", "&ldquo;Someone should come in.&rdquo;"], 1,
         "Hazard, protection now, help needed, and recheck time."),
        ("What do the cross-sectional staffing studies in dialysis show?",
         ["Proof that one more nurse prevents deaths", "An association between more patients per nurse and more reported adverse events", "No relationship at all", "That assistants can replace nurses"], 1,
         "They show association, not causation, but the direction is consistent."),
        ("What does a PhilHealth circular mainly govern?",
         ["Staffing ratios", "Reimbursement and covered services", "Water limits", "Nurse licensing"], 1,
         "Payer rules answer payer questions; licensing rules come from DOH."),
        ("The ACLS-trained nurse goes home sick at 9 a.m. What do you do first?",
         ["Continue as usual", "Call for a replacement and tell the physician on duty", "Close the unit", "Ask the assistant to cover"], 1,
         "The shift no longer meets a licensing condition; get a replacement and keep the physician close."),
        ("Which of these is not one of the five questions to ask of a rule?",
         ["Who issued it?", "Which clause?", "Who benefits from it?", "Which version?"], 2,
         "Issuer, jurisdiction, scope, clause, and version."),
        ("Why is acuity still important when the ratio is met?",
         ["It is not; the ratio is enough", "Patients with new catheters or unstable pressure need more nursing than stable patients", "Acuity only matters for PhilHealth", "Acuity replaces the ratio"], 1,
         "The ratio is a ceiling; need decides how the load is shared."),
        ("The physician on duty asks you to type a new dry weight on his verbal word. What is the safe response?",
         ["Type it as if it were your decision", "Refuse to speak to him", "Read it back, record it as a verbal order per procedure, and flag it for countersignature", "Wait until next week"], 2,
         "The decision is his; recording it safely is yours."),
        ("What is a requirement register?",
         ["A list of staff birthdays", "A table of the rules the unit follows, with source, clause, owner, and review date", "The PhilHealth claims log", "The water log"], 1,
         "It keeps the answers to the five questions in one place."),
        ("According to the PSN 2024 standards, how much dialysis experience is expected of a head nurse?",
         ["Six months", "One year", "Two years", "Five years"], 2,
         "PSN lists two years of dialysis experience, plus structured training and life support certificates."),
        ("What should you find out before accepting charge for the first time?",
         ["Your job description, the escalation ladder, and whether you may pause an unsafe activity", "The unit&rsquo;s budget", "The physician&rsquo;s home address", "The PhilHealth payment rate"], 0,
         "Without the authority to pause, you have responsibility without tools."),
        ("What does &ldquo;technical release&rdquo; mean?",
         ["Discharge of a patient", "A signed statement that water or a machine is fit to use", "A staff resignation", "A medicine order"], 1,
         "Release belongs to the authorized technical staff; the charge nurse confirms it before use."),
    ],
    "terms": [("Charge nurse", "The registered nurse who coordinates one shift."),
              ("Head nurse", "The nurse who leads the unit over time."),
              ("Physician on duty (POD)", "The physician present or on call for the shift."),
              ("Technical release", "A signed statement that water or a machine is fit to use."),
              ("Escalation", "Moving a problem to the person who can decide it."),
              ("Requirement register", "A table of rules with source, clause, owner, and review date."),
              ("Licensing condition", "A rule a facility must meet to keep its license to operate."),
              ("Verbal order", "An order given by voice, read back, recorded, and countersigned by the prescriber.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How a dialysis unit organizes quality review and improvement."),
                 ("living-with-dialysis.html", "What dialysis asks of patients and families, for context on every shift.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c1"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
