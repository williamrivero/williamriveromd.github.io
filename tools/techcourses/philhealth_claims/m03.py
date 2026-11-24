# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 03: The Hemodialysis Benefit, Patient Charges, and the Agreement Form."""

MODULE = {
    "image_alt": "A man and his niece read a one-page form together before his dialysis session, with a staff member's hand offering a pen.",
    "objectives": [
        "State the current hemodialysis benefit: who qualifies, how many sessions, the package rate and its split, and the annual maximum.",
        "Explain in plain words why erythropoietin, intravenous iron, anticoagulation, and routine tests are part of a covered session.",
        "Recognize a covered, clinically indicated item billed to a patient, and route its correction and refund review.",
        "Explain the per-session agreement form in the patient&rsquo;s language and check understanding with teach-back.",
        "Handle a premium choice such as hemodiafiltration without losing the patient&rsquo;s hemodialysis benefit.",
    ],
    "big": """
{{plain:The hemodialysis package is a fixed price for a complete session, like a set meal. The price covers everything a safe session needs: the filter, the lines, the medicines the failing kidneys can no longer replace, and the tests that check the treatment is working. If a set meal includes rice, the restaurant cannot charge you separately for the rice.}}
<p>The picture has a limit. A meal is the same for every diner; a dialysis session is not. Some items, such as an iron dose or a particular test, are given only when the patient&rsquo;s condition calls for it. The package covers them <em>when they are clinically indicated</em>, and only the treating team decides that. Billing staff never decide whether a patient needed a medicine; they make sure that a covered, indicated item is not charged to the patient.[[dch_philhealth_pa2024]]</p>
{{cards:Key terms for this module|Package rate::The fixed amount PhilHealth pays for each covered session.|Professional fee::The part of the package for the nephrologist&rsquo;s professional services.|Clinically indicated::Ordered by the treating team because the patient&rsquo;s condition calls for it.|No copay::Patients pay nothing for covered, indicated items within the package.|Agreement form::The Hemodialysis Benefits Agreement Form, completed for each session (Annex A of the circular).|Teach-back::Asking the patient to say back, in their own words, what you explained.}}
""",
    "case": {"title": "A kit, a premium line, and a worried niece", "html": """
<p>Mr. Ernesto Dizon (fictional, SIM-03), 54, chose hemodiafiltration, a premium form of dialysis, after his nephrologist discussed it with him. His niece Bea brings his latest statement to the desk. It shows a separate 400-peso charge for a dialysis kit that the nurse documented as indicated, and a 1,500-peso &ldquo;premium modality&rdquo; line. She cannot find a signed premium agreement in the copies the family kept.</p>
<p>&ldquo;We thought PhilHealth covers everything,&rdquo; Bea says. &ldquo;Will he lose his benefit because he chose this treatment?&rdquo;</p>
""", "questions": ["Does Mr. Dizon keep his hemodialysis benefit?",
                  "What happens to the 400-peso kit charge, and to the premium line?",
                  "What do you say to Bea in two sentences, and how do you check she understood?"]},
    "sections": [
        ("benefit", "The benefit", "What the current benefit covers", """
<p>PhilHealth Circular 2024-0023, Revision 2, covers up to 156 hemodialysis sessions per calendar year for members and qualified dependents with chronic kidney disease stage 5 who are registered in the PhilHealth Dialysis Database.[[pc_pc2024_0023]] The number is not arbitrary: it is three sessions a week for 52 weeks, the standard schedule for adequate hemodialysis.[[pc_pc2023_0009]] Unused sessions do not carry over to the next year.</p>
{{formula:<strong>The arithmetic.</strong> 3 sessions a week &times; 52 weeks = 156 sessions. Package rate: 6,350 pesos per session (6,000 for the facility, 350 for the professional). Annual maximum: 156 &times; 6,350 = 990,600 pesos per patient per calendar year.}}
<p>The general 45-day benefit limit was lifted by PhilHealth Circular 2025-0007, effective April 4, 2025. That change does <strong>not</strong> apply to hemodialysis, which keeps its own 156-session limit.[[pc_pc2025_0007]][[pc_pa2025_0035]]</p>
{{key:Coverage rules decide who pays. They never decide whether a patient is dialyzed today.}}
"""),
        ("why", "Why these items", "Why the package includes medicines and tests", """
<p>Each item in the package exists because failing kidneys need it replaced or watched. Understanding why helps you spot a charge that should not be there.</p>
{{fig:pc_package}}
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Why a dialysis patient needs it</th></tr></thead>
<tbody>
<tr><td>Dialyzer, bloodlines, dialysis kit</td><td>The filter and tubing that clean the blood; the needles and dressings that reach it.</td></tr>
<tr><td>Anticoagulant (heparin or enoxaparin)</td><td>Blood clots when it touches plastic; without it the filter and lines block.</td></tr>
<tr><td>Erythropoietin</td><td>Healthy kidneys make this hormone, which tells the bone marrow to make red cells. Failing kidneys stop, so patients become anemic.</td></tr>
<tr><td>Intravenous iron (iron sucrose)</td><td>The marrow needs iron to use erythropoietin, and dialysis patients lose iron through blood tests and the circuit.</td></tr>
<tr><td>Routine laboratory tests</td><td>Potassium, phosphate, hemoglobin, and dialysis adequacy tell the team whether treatment is enough and safe.</td></tr>
</tbody></table></div>
<p>PhilHealth clarified that it covers the services in the circular&rsquo;s minimum-standards table, that their provision depends on the patient&rsquo;s clinical assessment, and that the no-copay provision applies to them.[[dch_philhealth_pa2024]] When you are unsure whether an item was indicated, ask the treating team. Do not decide it in billing.</p>
"""),
        ("charges", "Patient charges", "Catching a covered item on the bill", """
<p>Out-of-pocket costs for dialysis can be ruinous. In Thailand, where dialysis is covered under universal health coverage, half of hemodialysis patients still faced catastrophic health spending in a 2022 national study, driven largely by travel and items outside the package.[[pc_sangthawan2022]] Philippine authors describe out-of-pocket payments and administrative delays as continuing barriers for dialysis patients here too.[[pc_pajimna2023]] A wrong charge on a statement is not a small matter to the family who pays it.</p>
{{fig:pc_covered}}
<p>When a covered, indicated item appears as a patient charge, keep the original statement, ask billing to correct it, match the corrected electronic statement of account and patient statement, and send any payment already collected to finance for the approved refund process. Calculator 5 in the claims toolkit flags these lines automatically.</p>
<p><strong>Premium choices.</strong> A patient who chooses a premium modality such as hemodiafiltration keeps the hemodialysis benefit. Show the benefit on the bill, charge only the allowed difference that the patient agreed to in writing, and route any discount or social-service help to billing. A signed premium agreement cannot turn a covered kit into an extra charge.</p>
{{call:Billing a covered item to a patient after you have identified it as covered is a critical error in this course. Hold the statement and correct it.}}
"""),
        ("agreement", "The agreement form", "Explaining the benefit, session by session", """
<p>The circular requires a completed Hemodialysis Benefits Agreement Form (Annex A) for each treatment session. PhilHealth&rsquo;s published form restates the 156-session allocation and the 6,350-peso package rate.[[pc_agreement_form]] Explain it in the patient&rsquo;s language, have it signed by the right person on the right date, and give the patient a copy. Never backdate it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Say</th><th>Avoid</th></tr></thead>
<tbody>
<tr><td>&ldquo;This kit is covered by PhilHealth, so you should not be charged for it.&rdquo; / &ldquo;Kasama po sa PhilHealth ang kit na ito, kaya hindi po kayo dapat singilin dito.&rdquo;</td><td>&ldquo;Everything is free.&rdquo;</td></tr>
<tr><td>&ldquo;Can you tell me which item is included and which one we are still checking?&rdquo; / &ldquo;Puwede po ba ninyong ulitin kung alin ang kasama at alin pa ang aming sinusuri?&rdquo;</td><td>&ldquo;Do you understand?&rdquo;</td></tr>
<tr><td>&ldquo;His dialysis continues while we sort out the bill.&rdquo;</td><td>Linking treatment to payment</td></tr>
<tr><td>&ldquo;We will tell you by Friday.&rdquo;</td><td>Promising a refund before the record is checked</td></tr>
</tbody></table></div>
<p>Teach-back is the check: ask the patient or family to say back, in their own words, what is covered and what is still being reviewed. If they cannot, the explanation failed, not the family.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The benefit stays.</strong> Choosing hemodiafiltration does not cost Mr. Dizon his hemodialysis benefit. The circular preserves it, and it should appear on his bill.</p>
<p><strong>The charges.</strong> The 400-peso kit was documented as indicated and is covered: the copay is zero. Keep the original statement, correct the line, reconcile the electronic statement of account, and send it to finance for refund review if it was paid. Hold the 1,500-peso premium line until you find the signed premium agreement; if there is none, it cannot be charged.</p>
<p><strong>What to say.</strong> &ldquo;His dialysis benefit still applies to this session. We will correct the charge for the covered kit and review the separate premium line with you before we finalize the bill.&rdquo; Then ask Bea to say back which item is covered and which one is being checked.</p>
"""],
    "skills": {"title": "Benefit explanation and bill check",
               "intro": "Check three fictional statements with planted errors, then explain one to a supervisor playing a family member, in English or Filipino.",
               "items": [
                   ("States the session limit, package rate, split, and annual maximum correctly.", False),
                   ("Identifies a covered, indicated item charged to the patient.", True),
                   ("Keeps the original statement and routes correction and refund review to the right owners.", True),
                   ("Holds a premium charge that has no signed agreement.", False),
                   ("Explains the benefit in plain language and states that treatment continues.", False),
                   ("Uses teach-back and corrects the explanation if the family cannot say it back.", False),
                   ("Completes the agreement form for the correct session date, without backdating.", True),
               ],
               "placement": "Review five patient statements at your unit with your billing lead and report any covered item charged to a patient."},
    "quiz": [
        ("What amount of the package goes to the professional?",
         ["6,000 pesos", "350 pesos per qualifying session", "1,350 pesos", "Nothing"], 1,
         "6,000 pesos goes to the facility."),
        ("Can a signed premium agreement turn a covered kit into a payable extra?",
         ["Yes", "No; the covered-item copay stays zero", "Only for HDF", "Only if the patient insists"], 1,
         "Correct the bill."),
        ("What is the maximum annual hemodialysis package value per patient?",
         ["624,000 pesos", "990,600 pesos", "1.2 million pesos", "Unlimited"], 1,
         "156 &times; 6,350 pesos."),
        ("A patient asks whether unused sessions roll over to next year. What is the answer?",
         ["Yes", "No; they expire at year-end", "Only 10 sessions", "Only for dependents"], 1,
         "The allocation is per calendar year."),
        ("Erythropoietin is billed separately, and nursing documented it as indicated. What do you do?",
         ["Leave it", "Correct the bill; the covered item&rsquo;s copay is zero", "Ask the patient to pay half", "Send it to PhilHealth as an appeal"], 1,
         "Covered and indicated means no copay."),
        ("The patient chose HDF and signed a premium agreement. Does the hemodialysis benefit still apply?",
         ["No", "Yes; show the benefit and charge only the documented allowed difference", "Only for the first month", "Only if PhilHealth approves"], 1,
         "The circular preserves the HD benefit."),
        ("Why do dialysis patients need erythropoietin?",
         ["It cleans the blood", "Failing kidneys stop making the hormone that drives red-cell production", "It prevents clotting", "It lowers potassium"], 1,
         "That is why anemia is common in kidney failure."),
        ("Why is an anticoagulant used during hemodialysis?",
         ["To lower blood pressure", "Blood clots when it touches the plastic circuit", "To treat anemia", "To remove fluid"], 1,
         "Without it the filter blocks."),
        ("Who decides whether an item was clinically indicated?",
         ["Billing", "The treating team", "The patient", "PhilHealth&rsquo;s call center"], 1,
         "Billing asks; it does not decide."),
        ("Does the lifting of the 45-day benefit limit change the hemodialysis limit?",
         ["Yes, HD is now unlimited", "No; HD keeps its 156-session limit", "Yes, HD is now 200", "Only for dependents"], 1,
         "PhilHealth Circular 2025-0007 excludes hemodialysis."),
        ("How often is the agreement form completed?",
         ["Once a year", "For each treatment session", "Only at transfer", "Never"], 1,
         "A grouped claim still needs one per session."),
        ("Which is the better teach-back question?",
         ["&ldquo;Do you understand?&rdquo;", "&ldquo;Can you tell me which item is included and which one we are still checking?&rdquo;", "&ldquo;Any questions?&rdquo;", "&ldquo;Sign here.&rdquo;"], 1,
         "Teach-back asks the family to say it back."),
        ("Why is 156 the session number?",
         ["A budget guess", "Three sessions a week for 52 weeks", "Two sessions a week for 78 weeks", "PhilHealth&rsquo;s founding year"], 1,
         "The standard schedule for adequate hemodialysis."),
        ("What did a 2022 Thai national study find about hemodialysis patients under universal coverage?",
         ["No out-of-pocket costs", "Half still faced catastrophic health spending", "Costs were lower than peritoneal dialysis", "Travel was free"], 1,
         "Coverage gaps still hurt families."),
        ("A family is told a charge will be refunded before anyone checked the record. What went wrong?",
         ["Nothing", "A promise was made before verification; promise a date to check instead", "The refund was too small", "PhilHealth should have been told"], 1,
         "Give a date, not a guarantee."),
    ],
    "terms": [("Package rate", "The fixed amount PhilHealth pays per covered session."),
              ("Clinically indicated", "Ordered by the treating team because the patient&rsquo;s condition calls for it."),
              ("No copay", "Patients pay nothing for covered, indicated items."),
              ("Agreement form", "The Hemodialysis Benefits Agreement Form, completed for each session."),
              ("Hemodiafiltration", "A premium form of dialysis that adds convection to diffusion."),
              ("Teach-back", "Asking the patient to say back what was explained.")],
    "readings": [("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members."),
                 ("hmo-ckd-coverage.html", "How HMO coverage fits with PhilHealth for kidney care.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
