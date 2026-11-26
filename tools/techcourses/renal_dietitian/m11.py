# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 11: Acute Kidney Injury and Inpatient Nutrition Support. Written for this series from published sources."""

MODULE = {
    "image_alt": "An intensive care bedside with a feeding pump and a continuous kidney replacement machine; a dietitian speaking with the team.",
    "objectives": [
        "Explain why critical illness and acute kidney injury (AKI) raise protein needs instead of lowering them.",
        "Choose a defensible weight for calculation when the patient is swollen with fluid.",
        "Match protein to illness severity and the type of kidney replacement therapy (KRT), using the European Society for Clinical Nutrition and Metabolism (ESPEN) ranges.",
        "Identify refeeding risk and follow the hospital&rsquo;s protocol.",
        "Count energy from non-food sources such as dextrose and propofol.",
        "Write a clear inpatient handoff and a discharge plan.",
    ],
    "big": """
{{plain:A critically ill patient is a house on fire. The body burns its own muscle to supply amino acids for repair and immunity, whatever you feed it. Feeding cannot stop the fire, but it can stop the house from being burned to the frame. A kidney diet built for a quiet house, low in protein, is the wrong plan during a fire.}}
<p>The picture has a limit. A fire burns at one speed; critical illness moves in phases. In the first days the body makes much of its own glucose and handles extra fuel poorly, so pushing full feeds too early can cause overfeeding, high blood glucose, and refeeding shifts, while protein needs stay high and rise further when kidney replacement therapy removes amino acids. Your work in this module is to match protein to the illness and the type of KRT, build feeding up in steps, and check every day what was actually delivered.</p>
{{cards:Key terms for this module|Acute kidney injury (AKI)::A fall in kidney function over hours to days, measured by rising creatinine or falling urine output.|Kidney replacement therapy (KRT)::Dialysis in any form: intermittent HD, prolonged intermittent, or continuous.|Continuous kidney replacement therapy (CKRT)::Dialysis run 24 hours a day in the intensive care unit (ICU); also called CRRT.|Catabolism::Breakdown of body tissue, mainly muscle, for fuel and amino acids.|Refeeding syndrome::Dangerous shifts of phosphate, potassium, and magnesium into cells when feeding restarts after starvation.|Enteral nutrition::Feeding into the gut, by mouth or tube.|Parenteral nutrition::Feeding into a vein.}}
{{flow:Order of work at the bedside|Before illness::Usual weight and intake; days without food.|Now::Illness severity, fluid status, KRT type.|Risk::Refeeding risk; swallowing; gut function.|Targets::Weight basis, protein range, energy.|Route::Mouth, tube, or vein.|Delivery::Prescribed versus delivered, every day.}}
""",
    "case": {"title": "The old order", "html": """
<p>Mr. Navarro, 61, is in the ICU with pneumonia and septic shock. He has had almost nothing to eat for six days. He developed AKI and started CKRT this morning. Before illness he weighed 69 kg. Today he weighs 78 kg with swollen legs and arms after large volumes of intravenous fluid.</p>
<p>His chart still carries an outpatient order: &ldquo;Low-protein renal diet, 0.6 g/kg.&rdquo; His phosphate has fallen from 3.8 to 2.1 mg/dL over two days. He is on a propofol infusion for sedation. The ICU team asks you to &ldquo;start renal feeds.&rdquo;</p>
""", "questions": ["Which weight will you calculate from, and why?",
                  "What protein range fits him now, and what about the old order?",
                  "What risk must be managed before feeds are increased?"]},
    "sections": [
        ("why", "Why needs rise", "Critical illness turns protein needs upside down", """
<p>In stable CKD, protein is kept moderate. In critical illness, stress hormones and inflammation drive rapid muscle breakdown, and the patient can lose a large share of muscle in the first week in the ICU. Kidney replacement therapy adds another loss: CKRT removes amino acids continuously, on the order of 10 to 15 g a day, along with water-soluble vitamins and trace elements.[[espen2021]]</p>
<p>So the outpatient instinct to restrict protein &ldquo;for the kidneys&rdquo; is wrong here. ESPEN advises against reducing protein intake in order to avoid or delay dialysis in hospitalized patients.[[espen2024]] Kidney function will be supported by the machine if needed. Muscle cannot be replaced that way.</p>
{{key:An outpatient low-protein order should not follow a patient into the ICU. Flag it on the first day and ask the team to cancel it.}}
<p><strong>Example from practice.</strong> Mrs. Macaraeg, 62, usual weight 55 kg, is admitted to the ICU with sepsis and starts continuous kidney replacement therapy. Her chart still carries her clinic order, 0.6 g/kg, about 33 g of protein a day. CKRT removes about 10 to 15 g of amino acids a day, so her net intake would be about 18 to 23 g.[[espen2021]] Her ICU target on continuous therapy is 1.5 to 1.7 g/kg, about 83 to 94 g.[[espen2024]] The old order gives her about a quarter of what she needs. Flag it on day one.</p>
"""),
        ("targets", "Targets", "Choose the weight, then the range", """
<p><strong>The weight.</strong> Fluid given during resuscitation can add many kilograms. Calculating from the swollen weight overfeeds; calculating from an ideal weight may underfeed a large patient. Use the most recent dry or usual weight before illness when you can find it, from the family, clinic records, or the last dialysis chart, and write down where it came from. For obesity, follow your hospital&rsquo;s adjusted-weight method and say so.</p>
<p><strong>The protein range.</strong> ESPEN gives starting ranges by setting. They are expert-based reference values that ESPEN rates at its weakest grade of recommendation (grade 0), not doses proven in trials, so adjust them to tolerance and to the team&rsquo;s plan.[[espen2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>Protein (g/kg/day)</th></tr></thead>
<tbody>
<tr><td>Hospitalized with AKI, not acutely or critically ill</td><td>0.8 to 1.0</td></tr>
<tr><td>Critically ill, no KRT</td><td>Start at 1.0, rise toward 1.3 as tolerated</td></tr>
<tr><td>Critically ill on intermittent KRT</td><td>1.3 to 1.5</td></tr>
<tr><td>Critically ill on continuous or prolonged intermittent KRT</td><td>1.5 to 1.7</td></tr>
</tbody></table></div>
<p><strong>Energy.</strong> In the first days of critical illness, the body makes much of its own glucose, and full feeding can add to that rather than replace it. Most ICU teams therefore build up energy over several days rather than giving the full target at once, and use indirect calorimetry when it is available. Follow your ICU&rsquo;s protocol. Count energy that is not food: dextrose in intravenous fluids and CKRT solutions, and propofol, which is given in a fat emulsion that supplies about 1.1 kcal per mL.[[espen2021]]</p>
{{fig:rd11_targets}}
<p><strong>Example from practice.</strong> Mr. Ledesma, 59, weighed 70 kg before his illness and weighs 81 kg after resuscitation fluids. He is on intermittent hemodialysis. At 1.3 to 1.5 g/kg, his protein target is 91 to 105 g on the usual weight, and 105 to 122 g on today&rsquo;s swollen weight. Calculating from the swollen weight would overshoot by about 15 g a day. He is also on propofol at 20 mL an hour: 480 mL a day &times; 1.1 kcal = about 530 kcal of fat that no one wrote down as nutrition. Count it before setting the feed rate.[[espen2021]]</p>
"""),
        ("refeeding", "Refeeding", "Refeeding risk: start low, watch phosphate", """
<p>After days without food, the body switches to burning fat, and stores of phosphate, potassium, magnesium, and thiamine run down. When carbohydrate arrives, insulin rises and drives these minerals into cells to build new tissue and make energy. Blood levels can fall within hours. Severe low phosphate weakens the breathing muscles and the heart.</p>
<p>The American Society for Parenteral and Enteral Nutrition (ASPEN) consensus lists risk factors that include little or no intake for five to six days or more, recent weight loss, low body mass index, and low potassium, phosphate, or magnesium before feeding. For patients at risk, it advises starting feeding at a low level and building up over several days, giving thiamine before feeding begins, and checking potassium, magnesium, and phosphate often in the first days.[[aspen2020]] These are consensus recommendations, not trial results. Your hospital&rsquo;s protocol sets the numbers. Thiamine and electrolyte replacement are medical orders.</p>
{{stop:A patient with several days of minimal intake and a falling phosphate is at refeeding risk now. Tell the ICU team before feeds are increased, and ask that the refeeding protocol be started.}}
<p>CKRT adds its own phosphate loss, because most CKRT fluids contain little or none. A falling phosphate in a patient on CKRT may come from both causes at once.</p>
<p><strong>Example from practice.</strong> Ms. Alcantara, 45, weighs 42 kg (body mass index 17) and has eaten almost nothing for seven days. Her phosphate is 2.8 mg/dL. The feed is increased to full rate on day two, and by evening her phosphate is 1.4 mg/dL and she feels weak. She had several ASPEN risk factors: no intake for more than five days, a low body mass index, and a low-normal phosphate.[[aspen2020]] The consensus advises a cautious start, for example 10 to 20 kcal/kg in the first 24 hours, here about 420 to 840 kcal, then building up over several days. Thiamine goes in before feeding starts, with frequent electrolyte checks. You call the ICU team before the next increase, and the hospital&rsquo;s refeeding protocol is started.</p>
"""),
        ("route", "Route and delivery", "Route, delivery, and handoff", """
<p>Feed by mouth when the patient can swallow safely and eat enough. When the gut works but intake falls short, a feeding tube is usually the next step. Parenteral nutrition is for patients whose gut cannot be used or cannot meet needs; the choice and timing belong to the team. Standard tube-feeding formulas are suitable for most patients with AKI. Specialized &ldquo;renal&rdquo; formulas are concentrated and lower in potassium and phosphate; they suit patients with fluid limits or high electrolytes, but on CKRT, where electrolytes are being removed, a standard formula is often better.[[espen2021]]</p>
<p>Every day, compare what was prescribed with what was delivered. Feeds stop for procedures, scans, and turning. A patient prescribed 1,800 kcal who receives 900 is underfed, whatever the order says.</p>
{{cards:A good inpatient handoff includes|Weight basis::Which weight and where it came from.|KRT type::Intermittent, prolonged, or continuous, and recent changes.|Targets::Protein range and energy with the guideline named.|Refeeding status::Risk, protocol started, latest phosphate, potassium, magnesium.|Delivery::Percentage of target delivered and the reasons for gaps.|Discharge::Kidney recovery trend, intake, and when the outpatient plan must be rewritten.}}
<p>At discharge, kidney function may recover fully, partly, or not at all. Do not let the hospital plan simply carry over. Write down that the diet must be reassessed when the patient is seen as an outpatient, with the latest kidney function.</p>
{{fig:rd11_route}}
<p><strong>Example from practice.</strong> Mr. Sarmiento, 64, on CKRT, has a tube feed prescribed at 1,800 kcal a day. Over three days the pump history shows 1,800 kcal, then 700 kcal (CT scan and an extubation trial), then 1,100 kcal (feeds held for turning and a high gastric residual). He received an average of about 1,200 kcal a day, 67% of target. You report the number and the reasons and ask whether the unit&rsquo;s protocol allows a volume-based or catch-up approach. The order said 1,800. The patient got 1,200.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Which weight?</strong> The 69 kg before illness, not the 78 kg today. He has about 9 kg of resuscitation fluid on board. Write down where the 69 kg came from, and that it is an estimate.</p>
<p><strong>What protein range?</strong> He is critically ill and on continuous KRT, so ESPEN&rsquo;s reference is 1.5 to 1.7 g/kg/day. At 69 kg, that is about 104 to 117 g a day. That is the range to reach as tolerated over the coming days, not on day one. The outpatient order of 0.6 g/kg would give him 41 g, less than half his need while he loses amino acids to the machine and muscle to sepsis. Ask the ICU team to cancel it today.</p>
<p><strong>What must be managed first?</strong> Refeeding risk. Six days without food and a phosphate already falling from 3.8 to 2.1 mg/dL, with CKRT removing more. Tell the team before feeds go up, and ask for the refeeding protocol: thiamine before feeding, a low starting rate, and frequent checks of phosphate, potassium, and magnesium. The physician orders the replacement.</p>
<p><strong>And &ldquo;start renal feeds&rdquo;?</strong> Talk it through. On CKRT, a standard formula may be the better choice. Count the propofol as fat energy. Then track every day how much of the prescription he actually receives. In the ICU, the dietitian&rsquo;s plan is only as good as the feed that reaches the patient, and you are the one who checks.</p>
"""],
    "skills": {"title": "ICU nutrition assessment and handoff",
               "intro": "Use a fictional ICU chart with a fluid balance, KRT orders, and three days of laboratory results.",
               "items": [
                   ("Finds and documents a pre-illness weight and explains why the current weight is not used.", False),
                   ("Identifies the KRT type and matches the ESPEN protein range.", False),
                   ("Flags any outpatient protein restriction for cancellation.", True),
                   ("Recognizes refeeding risk from intake history and falling phosphate, and asks for the protocol before feeds increase.", True),
                   ("Counts energy from dextrose and propofol.", False),
                   ("Recommends a route and formula and explains the choice for a patient on CKRT.", False),
                   ("Compares prescribed and delivered intake and lists reasons for gaps.", False),
                   ("Writes a handoff with weight basis, KRT type, targets, refeeding status, delivery, and discharge plan.", False),
               ],
               "placement": "Join one ICU or nutrition support team round and calculate prescribed versus delivered intake for two patients."},
    "quiz": [
        ("A patient on CKRT weighed 69 kg before illness and 78 kg now with edema. Which weight is the better basis?",
         ["78 kg", "69 kg, with the source documented", "An average of the two", "A population average"], 1,
         "Resuscitation fluid inflates today&rsquo;s weight."),
        ("ESPEN&rsquo;s protein reference for a critically ill patient on continuous KRT is:",
         ["0.6 to 0.8 g/kg/day", "0.8 to 1.0 g/kg/day", "1.3 to 1.5 g/kg/day", "1.5 to 1.7 g/kg/day"], 3,
         "Continuous therapy removes amino acids and illness raises needs."),
        ("At 69 kg, 1.5 to 1.7 g/kg/day is about:",
         ["41 to 48 g", "69 to 76 g", "104 to 117 g", "150 g"], 2,
         "1.5 × 69 = 103.5; 1.7 × 69 = 117.3."),
        ("Should protein be reduced to delay dialysis in a hospitalized patient with AKI?",
         ["Yes, always", "No; ESPEN advises against it", "Only on weekends", "Only if albumin is low"], 1,
         "Muscle loss is the greater harm; dialysis can support the kidney."),
        ("An outpatient low-protein order is still active in the ICU. The dietitian should:",
         ["Follow it", "Flag it to the team for cancellation", "Lower it further", "Ignore the order"], 1,
         "Outpatient restrictions do not fit critical illness."),
        ("Which is a refeeding risk factor?",
         ["Eating normally until yesterday", "Little or no intake for five days or more", "High phosphate", "Obesity alone with normal intake"], 1,
         "Prolonged starvation depletes phosphate, potassium, magnesium, and thiamine."),
        ("Why does phosphate fall when feeding restarts?",
         ["It is lost in stool", "Insulin drives it into cells", "It binds to protein", "Dialysis adds it"], 1,
         "New tissue building and energy production pull phosphate into cells."),
        ("Who orders thiamine and electrolyte replacement?",
         ["The dietitian", "The physician", "The patient", "The pharmacist alone"], 1,
         "The dietitian flags the risk and asks for the protocol."),
        ("Propofol supplies about:",
         ["No energy", "1.1 kcal per mL as fat", "4 kcal per mL as protein", "10 kcal per mL"], 1,
         "It is given in a fat emulsion; count it in energy intake."),
        ("Why might a standard formula suit a patient on CKRT better than a renal formula?",
         ["It contains more potassium and phosphate, which CKRT removes", "It is cheaper only", "Renal formulas contain no protein", "Standard formulas are always better"], 0,
         "CKRT removes electrolytes; renal formulas restrict them."),
        ("A patient was prescribed 1,800 kcal but received 900 kcal because feeds were stopped for scans. You should:",
         ["Record 1,800 kcal as given", "Record delivered intake and work with the team to reduce interruptions", "Ignore it", "Double tomorrow&rsquo;s rate without discussion"], 1,
         "Delivered intake is what the patient gets."),
        ("In the first days of critical illness, ICU teams usually:",
         ["Give full energy at once", "Build energy up over several days", "Give no nutrition for two weeks", "Give only protein"], 1,
         "Gradual build-up avoids overfeeding when the body makes its own glucose."),
        ("Phosphate is falling in a patient on CKRT. Possible causes include:",
         ["Refeeding and CKRT losses", "Too much phosphate in the formula only", "High protein only", "Dehydration only"], 0,
         "Both can act together."),
        ("At discharge after AKI, the diet should:",
         ["Continue unchanged forever", "Be reassessed with the latest kidney function at follow-up", "Return to the old outpatient order", "Be stopped"], 1,
         "Kidney recovery varies; the plan must follow it."),
        ("The ESPEN protein ranges are best described as:",
         ["Doses proven in large trials", "Expert-based reference values to adjust to tolerance", "Legal requirements", "Maximums never to exceed"], 1,
         "They guide practice where trials are limited."),
    ],
    "terms": [("Indirect calorimetry", "Measuring energy use from oxygen consumed and carbon dioxide produced."),
              ("Resuscitation fluid", "Intravenous fluid given to restore blood pressure in shock."),
              ("Propofol", "A sedative given in a fat emulsion."),
              ("Effluent", "Fluid removed by CKRT, carrying waste, electrolytes, and amino acids."),
              ("Thiamine", "Vitamin B1, needed to use carbohydrate; depleted in starvation.")],
    "readings": [("crrt-continuous-renal-replacement-therapy.html", "How continuous kidney replacement therapy works."),
                 ("aki-does-not-end-at-discharge.html", "Follow-up after acute kidney injury."),
                 ("aki-icu-dialysis-decisions.html", "Dialysis decisions in the ICU.")],
    "calcs": ["calc-crrt-dose.html", "calc-energy-expenditure.html", "calc-electrolyte-repletion.html", "calc-aki-staging.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
