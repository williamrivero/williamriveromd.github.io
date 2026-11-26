# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 09: Medicines, Heparin, and Blood on the Floor. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two nurses performing an independent double-check of a syringe at a medication cart.",
    "objectives": [
        "Reconcile medicines when a patient returns from a hospital stay or a new prescriber.",
        "Run a true independent double-check for high-alert medicines.",
        "Do the arithmetic for a heparin pump and recognize an implausible rate.",
        "Coordinate a blood transfusion during dialysis safely.",
        "Respond to a suspected drug or transfusion reaction, and report errors to learn from them.",
    ],
    "big": """
{{plain:A double-check is like two people reading a map. If the second person only watches the first one point and says &ldquo;yes,&rdquo; there is still only one reader.}}
<p>An independent double-check means the second nurse works it out without being told the answer. She reads the order herself, picks the vial, checks the strength, and calculates the dose before comparing with the first nurse. Anything less is a single check with two signatures.</p>
<p>The picture has a limit. Two map readers who disagree simply look again. On a dialysis floor one wrong reading can reach the patient within minutes, as a tenfold heparin dose or the wrong unit of blood, and a junior nurse may feel pressure to agree with a senior one. Independence has to be built into the steps, not left to goodwill.</p>
<p>The same discipline covers the other high-alert items on a hemodialysis (HD) floor in chronic kidney disease (CKD): erythropoietin (EPO) and other anemia medicines, and red blood cell (RBC) transfusions given to raise the hemoglobin (Hgb). Your work in this module is to make the second check truly independent for each of them.</p>
{{cards:Key terms for this module|Medication reconciliation::Comparing every medicine list a patient has, and agreeing one current list with the prescriber.|High-alert medicine::A medicine that causes serious harm when given wrongly: heparin, insulin, intravenous iron, potassium.|Independent double-check::A second nurse checks from the order without seeing the first nurse&rsquo;s answer.|Erythropoiesis-stimulating agent (ESA)::An injected medicine that stimulates red cell production.|Transfusion reaction::A harmful response to transfused blood, from mild fever to life-threatening collapse.|Near miss::An error caught before it reached the patient.}}
""",
    "case": {"title": "1,000 or 10,000?", "html": """
<p>Mrs. Rosario Navarro, 63, came back yesterday from a hospital stay for pneumonia. On the unit chart, her heparin order reads &ldquo;heparin 1,000 units/hour during dialysis.&rdquo; The handwritten discharge summary says &ldquo;heparin 10,000 u.&rdquo; Her hemoglobin is 8.4 g/dL, and the attending ordered one unit of packed red cells during today&rsquo;s session.</p>
<p>The staff nurse has prepared the heparin from the discharge note.</p>
""", "questions": ["What should have happened before the heparin was prepared?",
                  "How would a real independent double-check catch this?",
                  "How is the transfusion done safely during dialysis?"]},
    "sections": [
        ("recon", "Reconciliation", "Reconciliation at every return", """
<p>Patients on dialysis take many medicines and move between hospital, clinic, and home. In a small Canadian study of patients transferred between dialysis units, about four in five had at least one unintended medication discrepancy, most often a medicine the patient was taking that had been left off the new orders.[[cn_ledger2008]] A review in the <em>American Journal of Kidney Diseases</em> calls reconciliation the foundation of medication safety in dialysis.[[cn_frament2020]] In a United States program, adding a dialysis pharmacist was associated with fewer medication discrepancies over time.[[cn_dyer2022]]</p>
{{fig:cn09_recon}}
<p>The charge nurse&rsquo;s part is one rule: no high-alert medicine is given from a discharge note, a patient&rsquo;s bag, or a relative&rsquo;s memory until the attending or physician on duty has reconciled it into a current order.</p>
"""),
        ("highalert", "High-alert medicines", "High-alert medicines on the floor", """
<p>Heparin, intravenous iron, insulin, potassium, and anticoagulant catheter locks cause the most serious harm when wrong. Store look-alike strengths apart, label every syringe at the bedside, and protect preparation from interruptions (Module 4). If two strengths of heparin sit on one shelf, separate them today and report the storage risk.</p>
"""),
        ("double", "Double-check", "The independent double-check", """
<p>The second nurse reads the order herself, selects the vial, checks the strength and expiry, and calculates. Only then do the two compare. Any disagreement stops the process until it is resolved with the order and, if needed, the prescriber.</p>
{{scene:The watched check|<p>Nurse Paula says, &ldquo;Can you check this? It&rsquo;s 2,000 units an hour, so 2 mL an hour.&rdquo; Nurse Jonas looks, nods, and signs. That was not a double-check; Jonas heard the answer first. The next week Paula hands Jonas only the order and the vial. Jonas calculates 2 mL an hour. Paula calculates 2 mL an hour. Now two people have read the map.</p>}}
"""),
        ("pump", "Pump arithmetic", "Heparin pump arithmetic", """
{{fig:cn09_pump}}
{{formula:<strong>Pump rate (mL/h)</strong> = ordered units per hour &divide; syringe units per mL.<br>1,000 units/h with a 1,000 units/mL syringe = 1.0 mL/h. Over four hours: 4,000 units in 4 mL.}}
<p>The arithmetic is a plausibility check, not a dosing rule. The dose is the prescriber&rsquo;s. A result ten times larger or smaller than usual for that patient, or a pump rate outside the range your unit considers plausible, means stop and check the order and the syringe (Toolkit #c5).</p>
"""),
        ("blood", "Transfusion", "Transfusion during dialysis", """
<p>Two staff members check the patient&rsquo;s identity against the blood bag label at the chair. Take baseline vital signs. Start slowly and watch closely for the first fifteen minutes, when serious reactions usually show, then take vital signs per protocol.</p>
{{fig:cn09_transfusion}}
<p>Signs of a reaction include fever, chills, back pain, breathlessness, hives, and falling pressure. Stop the transfusion, keep the line open with saline per protocol, call the physician, and return the bag and tubing to the blood bank. Dialysis adds a trap: fever and chills can also come from a catheter infection or a reaction to the dialyzer.[[daugirdas1988]] Tell the physician all three possibilities, so the right tests are done.</p>
{{call:Stop the transfusion and call the physician at the first sign of fever, chills, back pain, breathlessness, hives, or falling pressure.}}
"""),
        ("report", "Reporting", "Report errors to learn from them", """
<p>Report errors and near misses through your unit&rsquo;s system, focusing on how the system let the error happen rather than who made it (Module 17). A heparin error caught by a double-check is a success of the system and a lesson about the discharge note.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Before preparation.</strong> The discharge note was never reconciled into a current order. No high-alert medicine should be prepared from it.</p>
<p><strong>The double-check (Toolkit #c5).</strong> The current order is 1,000 units/h; the syringe is 1,000 units/mL; pump rate 1.0 mL/h, 4,000 units over four hours. The discharge note&rsquo;s &ldquo;10,000&rdquo; at the same concentration would be 10 mL/h and 40,000 units, ten times the usual. A second nurse calculating from the current chart gets 1.0 mL/h; the first nurse, working from the note, gets 10 mL/h. The mismatch stops preparation. The physician clarifies: &ldquo;10,000&rdquo; was the hospital&rsquo;s daily subcutaneous prevention dose, not a dialysis infusion. The order stays at 1,000 units/h. The charge nurse files a near-miss report about unreconciled discharge notes.</p>
<p><strong>The transfusion.</strong> Identity checked at the chair by two staff, baseline vital signs, a slow start with close watching for the first fifteen minutes, and a clear plan: if fever or chills appear, stop, keep the line open, call, and consider transfusion reaction, catheter infection, and dialyzer reaction together.</p>
"""],
    "skills": {"title": "Medicines and blood",
               "intro": "Reconcile one returning patient&rsquo;s list, perform three independent double-checks, and lead a simulated transfusion reaction.",
               "items": [
                   ("Refuses to give a high-alert medicine from an unreconciled note.", True),
                   ("Performs an independent double-check without hearing the first answer.", True),
                   ("Calculates a heparin pump rate and recognizes a tenfold error.", True),
                   ("Separates look-alike strengths and labels syringes at the bedside.", False),
                   ("Runs a two-person identity check at the chair before transfusion.", True),
                   ("Stops a transfusion at the first sign of reaction and calls.", True),
                   ("Reports a near miss with a system fix.", False),
               ],
               "placement": "For two weeks, list every returning patient and whether their medicines were reconciled before the first dose of a high-alert medicine."},
    "quiz": [
        ("An independent double-check means the second nurse:",
         ["Watches the first nurse", "Works it out herself before comparing", "Signs only", "Reads the label aloud"], 1,
         "Two readers, not one reader and a witness."),
        ("2,000 units/h with a 1,000 units/mL syringe runs at:",
         ["0.5 mL/h", "2 mL/h", "20 mL/h", "200 mL/h"], 1,
         "2,000 &divide; 1,000 = 2."),
        ("A high-alert medicine order appears only on a discharge note. What do you do?",
         ["Give it", "Hold until it is reconciled into a current order", "Give half", "Ask the patient"], 1,
         "No note becomes an order by itself."),
        ("In the Canadian transfer study, unintended discrepancies affected about:",
         ["5%", "Four in five patients", "One in a hundred", "None"], 1,
         "Most often a medicine left off the new orders."),
        ("First step in a suspected transfusion reaction?",
         ["Speed up", "Stop the transfusion, keep the line open, call", "Give more blood", "Disconnect dialysis only"], 1,
         "Then return the bag and tubing to the blood bank."),
        ("Chills during a transfusion in a catheter patient. Think of:",
         ["Transfusion reaction only", "Transfusion reaction, catheter infection, or dialyzer reaction", "Anxiety", "A cold room"], 1,
         "Tell the physician all three."),
        ("Which is a high-alert medicine?",
         ["Saline flush", "Intravenous iron", "Gauze", "Lotion"], 1,
         "Heparin, insulin, IV iron, potassium, and anticoagulant locks."),
        ("When do serious transfusion reactions usually show?",
         ["After the session", "In the first fifteen minutes", "The next day only", "Never during dialysis"], 1,
         "Start slowly and watch closely."),
        ("What did adding a dialysis pharmacist show in a United States program?",
         ["More discrepancies", "Fewer medication discrepancies over time", "No change", "Higher costs only"], 1,
         "Reconciliation improves with dedicated effort."),
        ("A pump rate ten times the patient&rsquo;s usual means:",
         ["Run it carefully", "Stop and check the order and the syringe", "Halve it", "Tell the patient"], 1,
         "Arithmetic is a plausibility check."),
        ("Two heparin strengths sit on one shelf. What do you do?",
         ["Nothing", "Separate them and report the storage risk", "Use the stronger one", "Ask the patient"], 1,
         "Look-alike errors start on the shelf."),
        ("Who sets the heparin dose?",
         ["The charge nurse", "The prescriber", "The pump", "The pharmacy only"], 1,
         "The nurse checks the arithmetic."),
        ("What is returned to the blood bank after a reaction?",
         ["Nothing", "The bag and tubing", "The patient&rsquo;s chart", "The dialyzer"], 1,
         "The blood bank investigates the unit."),
        ("A near miss caught by a double-check is:",
         ["A failure", "A success of the system and a lesson to report", "Not worth reporting", "Grounds for discipline"], 1,
         "Report it so the cause is fixed."),
        ("What should travel with a reconciled list?",
         ["Nothing", "One current list agreed with the prescriber", "Every old list", "Only the discharge note"], 1,
         "One list, current, agreed."),
    ],
    "terms": [("Medication reconciliation", "Agreeing one current medicine list with the prescriber."),
              ("High-alert medicine", "A medicine that causes serious harm when given wrongly."),
              ("Independent double-check", "A second nurse checks from the order without seeing the first answer."),
              ("Erythropoiesis-stimulating agent (ESA)", "A medicine that stimulates red cell production."),
              ("Transfusion reaction", "A harmful response to transfused blood."),
              ("Near miss", "An error caught before it reached the patient.")],
    "readings": [("anemia-management.html", "Anemia in kidney disease, iron, and ESAs."),
                 ("epo-resistant-renal-anemia.html", "When anemia does not respond to treatment.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c5", "calc-transfusion-hgb.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
