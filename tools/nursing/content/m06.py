# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How hemodialysis moves solutes and water, how to read and verify a prescription line by line, how fluid removal is calculated, and what Kt/V and the urea reduction ratio do and do not tell you.",
    "desc": "Module 6 of the Nephrology Nursing & Hemodialysis self-study series: diffusion, ultrafiltration and convection, prescription verification, fluid accounting and ultrafiltration rate, delivered treatment time, Kt/V and urea reduction ratio for registered nurses.",
    "keywords": "hemodialysis principles nursing, diffusion ultrafiltration convection, dialysis prescription verification, ultrafiltration rate calculation, Kt/V, urea reduction ratio, KDOQI adequacy",
    "objectives": [
        "Explain diffusion, ultrafiltration, and convection and name the driving force of each.",
        "Verify each element of a hemodialysis prescription against the order before treatment.",
        "Calculate a fluid-removal goal and hourly ultrafiltration rate, accounting for fluids given during treatment.",
        "Interpret Kt/V and urea reduction ratio and list common reasons for low delivered adequacy.",
        "Recognize when a prescribed fluid goal warrants a call to the physician.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A tea bag and a press",
         "html": """
<p>Two kitchen pictures cover most of what happens inside a dialyzer. The first is a tea bag in a cup of water. Color spreads through the porous bag from where it is concentrated to where it is not, until both sides match. Nothing pushes it. The difference in concentration does the work. The second is a coffee press. Pushing the plunger forces water through a mesh. Here the pressure does the work. The first is diffusion, and it is how hemodialysis (HD) removes urea and potassium. The second is ultrafiltration, and it is how HD removes water.</p>
<p>The pictures have two limits. A cup of tea stops changing once both sides match. In a dialyzer, fresh dialysis fluid flows continuously in the opposite direction to the blood, so the two sides never match, and the concentration difference holds along the whole length of the fibers. A coffee press also has an endless supply of water above the mesh. The blood does not. The water the machine removes must be replaced from the tissues, and that refilling has a speed limit.</p>
<p>Most sessions run as written. Some do not, because the order no longer fits the patient, the machine does not match the order, or the minutes are not delivered. Your work is to check the prescription line by line before you start, to calculate the fluid goal correctly, and to call when the numbers say the session will be unsafe or too short.</p>
<p><strong>Gradients move wastes. Pressure moves water. The patient&rsquo;s refilling sets the safe pace.</strong></p>
"""},
        {"id": "physiology", "nav": "Principles", "tag": "Physiology", "h2": "Three transport processes",
         "html": """
<div class="table-wrap"><table>
<thead><tr><th>Process</th><th>Driving force</th><th>What it mainly moves</th><th>What increases it</th></tr></thead>
<tbody>
<tr><td>Diffusion</td><td>Concentration gradient</td><td>Small solutes: urea, creatinine, potassium; bicarbonate moves into the blood</td><td>Higher blood and dialysate flow, larger membrane, longer time</td></tr>
<tr><td>Ultrafiltration (UF)</td><td>Pressure gradient across the membrane</td><td>Plasma water</td><td>Higher transmembrane pressure, more permeable membrane</td></tr>
<tr><td>Convection</td><td>Solutes carried along with ultrafiltered water</td><td>Larger &ldquo;middle&rdquo; molecules</td><td>Larger ultrafiltration volumes, as in hemodiafiltration</td></tr>
</tbody></table></div>
<p>Dialysis fluid is not plain water. Its recipe decides which way diffusion moves each substance. It holds no urea, so urea leaves the blood. Its potassium is below the patient&rsquo;s, so potassium leaves at a controlled pace. Its bicarbonate is above the patient&rsquo;s, so buffer enters. That is why the dialysate potassium and calcium are part of the prescription, and why connecting the wrong concentrate is a medication error.</p>
<p>Water removal has a ceiling set by the body, not the machine. Ultrafiltration takes water only from the bloodstream. The tissues then refill the bloodstream, but at a limited rate. When removal outpaces refilling, blood volume falls. The patient develops cramps, nausea, or low blood pressure. A large patient has more tissue fluid to draw on than a small one, so the risk depends on the rate per kilogram of body weight, not on the total alone.</p>
<p><strong>Dialysate is a prescribed drug. Check it against the order like one.</strong></p>
"""},
        {"id": "evidence", "nav": "Adequacy", "tag": "Evidence", "h2": "Dose, time, and rate",
         "html": """
<p>Dialysis dose is expressed as Kt/V. K is the dialyzer&rsquo;s urea clearance, t is the treatment time, and V is the volume of body water in which urea is spread. Clearance times time gives the volume cleaned. Dividing by V says how many times over the patient&rsquo;s body water was cleaned of urea. It is calculated from blood urea measured before and after a session.[[daugirdas1993]] The urea reduction ratio (URR) is the simpler percentage fall in urea over the session.</p>
<p>For thrice-weekly HD, the Kidney Disease Outcomes Quality Initiative (KDOQI) 2015 guideline recommends a target single-pool Kt/V of 1.4 per session, with a minimum delivered dose of 1.2 (grade 1B, a strong recommendation on moderate-quality evidence). For patients with little remaining kidney function, it recommends at least 3 hours per session (grade 1D, a strong recommendation on very low-quality evidence).[[hd2015]] A URR of about 65% corresponds roughly to the minimum Kt/V.</p>
<p>Two cautions apply. First, Kt/V is a surrogate. It measures the removal of one small molecule, not how long the patient lives or how they feel. A randomized trial found no survival benefit from pushing the dose well above the target. A patient can also have an acceptable Kt/V while fluid overloaded, malnourished, or unwell. Adequacy is a floor, not a summary of good dialysis.[[hd2015]] Second, time matters on its own, because fluid and larger solutes need hours to move out of the tissues.</p>
<p>For fluid, Flythe and colleagues analyzed 1,846 patients from the Hemodialysis Study, a randomized trial of thrice-weekly dialysis. An ultrafiltration rate (UFR) above 13 mL/kg per hour was associated with higher all-cause mortality (adjusted hazard ratio 1.59) and cardiovascular mortality (1.71), compared with rates up to 10 mL/kg per hour.[[flythe2011]] The analysis was observational. Patients with large weight gains differ in other ways, so it does not prove that the rate itself causes harm. The link is physiologically plausible, though. A Kidney Disease: Improving Global Outcomes (KDIGO) conference advised avoiding high rates by limiting weight gain between sessions and extending time where needed. That is a conference statement, not a graded recommendation.[[flythe2020]]</p>
<p><strong>A rate above 13 mL/kg per hour, or above your unit&rsquo;s limit, is a reason to call the physician before you start. It is not a limit you set alone.</strong></p>
"""},
        {"id": "bedside", "nav": "Verify and calculate", "tag": "Clinical application", "h2": "Verifying the prescription and accounting for fluid",
         "html": """
<p>Before every treatment, compare the machine and supplies with the current order, one element at a time, for the right patient. The order was written for the patient as the physician last saw them. The machine was set up by whoever prepared it. Your check is where the two meet. A second nurse check of the dialysate concentrate and the anticoagulant is good practice where staffing allows.</p>
<div class="table-wrap"><table>
<thead><tr><th>Prescription element</th><th>What to verify</th></tr></thead>
<tbody>
<tr><td>Patient identity</td><td>Two identifiers against the order and the dialyzer label</td></tr>
<tr><td>Dialyzer</td><td>Model and size; if reprocessed, the patient&rsquo;s name and reuse number</td></tr>
<tr><td>Treatment time</td><td>Ordered duration; plan for interruptions so that delivered time matches</td></tr>
<tr><td>Blood and dialysate flow</td><td>Ordered rates; what the access can deliver</td></tr>
<tr><td>Dialysate</td><td>Potassium, calcium, bicarbonate, sodium; temperature</td></tr>
<tr><td>Anticoagulation</td><td>Agent, loading and maintenance dose, stop time; bleeding risk today</td></tr>
<tr><td>Target weight and fluid goal</td><td>Pre-dialysis weight, target weight, calculated removal</td></tr>
</tbody></table></div>
<p><strong>Fluid accounting.</strong> Start with the pre-dialysis weight minus the target weight. Then <em>add</em> every fluid the patient will receive during the session: the saline used to prime and rinse back the circuit if it is returned to the patient, intravenous medicines, and anything the patient drinks. Fluid that goes in must also come out, or the patient finishes above target. Divide the total by the treatment hours for the hourly rate, and by body weight for the rate per kilogram.</p>
<p><em>Example for teaching only, not a target.</em> Pre-dialysis weight 62.4 kg, target 60.0 kg. That is 2.4 liters over a 4-hour session, or 600 mL per hour before treatment inputs. If rinse-back saline and a drink add 400 mL, the machine goal becomes 2.8 liters, or 700 mL per hour. At 60 kg, that is about 11.7 mL/kg per hour. If the weight gain were 4 kg instead, the rate would be over 13 mL/kg per hour. You would call the physician before starting and ask whether to extend the time, accept a higher post-dialysis weight today, or schedule an extra session.</p>
<p><strong>When delivered adequacy is low,</strong> look for the usual causes before assuming the prescription is wrong. Was the treatment shortened by late arrival, early sign-off, or alarms? Was blood flow lower than ordered because of access problems? Did needles placed too close together, or reversed lines, send cleaned blood back into the circuit (recirculation)? Did the dialyzer clot? Was the post-dialysis blood drawn incorrectly?</p>
<p><strong>The minutes you deliver are part of the dose. Record every minute lost and why.</strong></p>
"""},
    ],
    "case": {
        "title": "The number on the order and the patient in the chair",
        "html": """
<p>Ms. Teresita Ocampo, 55, dialyzes three times a week for 4 hours. Today is Tuesday, after a long weekend. Her session was due at seven, and she arrives at 7:40. Her pre-dialysis weight is 64.0 kg, and her target weight is 60.0 kg. Her last monthly Kt/V was 1.1. The order reads: blood flow 300 mL/min, dialysate potassium 2.0 mmol/L, time 4 hours.</p>
<p>The charge nurse, Mr. Ramon Bautista, assigns her to you. As you weigh her, Ms. Ocampo asks to finish at her usual time, because her ride is waiting.</p>
""",
        "acte": {
            "Assess": "The 4.0 kg gain. Breathing, blood pressure, and edema. Access function. What she ate and drank over the weekend. How often her sessions have been shortened.",
            "Communicate": "Call the physician before starting. Report the 4 kg gain; with treatment inputs, a rate of about 18 mL/kg per hour over the full 4 hours, and about 22 if the session is shortened; and a last Kt/V below the minimum. Ask for orders on time and fluid goal.",
            "Teach": "Why a shorter session lowers both waste removal and the amount of fluid that can be removed safely. Agree a realistic plan for weight gain between sessions.",
            "Escalate": "Breathlessness or low oxygen saturation before treatment needs immediate medical review.",
        },
        "task": "Calculate the hourly rate and the rate per kilogram for (a) the full 4 hours and (b) 3 hours 20 minutes, with 400 mL of treatment inputs. Document your call to the physician.",
    },
    "quiz": [
        {"stem": "During conventional hemodialysis, which pairing correctly matches the main process to what it removes?",
         "options": [
             ("Ultrafiltration removes urea; diffusion removes water", False, "The pairing is reversed."),
             ("Convection removes urea; osmosis removes water", False, "Convection contributes little to small-solute removal in conventional HD, and water is removed by hydrostatic pressure."),
             ("Diffusion removes urea; ultrafiltration removes water", True, "Urea moves down its concentration gradient into the dialysate. Water is pushed across the membrane by a pressure gradient."),
             ("Adsorption removes urea; diffusion removes water", False, "Adsorption to the membrane is minor and does not remove urea meaningfully."),
         ],
         "objective": "Explain diffusion, ultrafiltration, and convection and name the driving force of each.", "sources": ["hd2015"], "flag": ""},
        {"stem": "A patient is 2.4 kg above target weight and is prescribed a 4-hour session. Before any fluids given during treatment are added, what is the hourly ultrafiltration rate, and what must the nurse do before setting the machine?",
         "options": [
             ("600 mL per hour; add the volume of saline, medicines, and oral fluids the patient will receive during treatment", True, "2,400 mL divided by 4 hours is 600 mL per hour. Fluids returned or given during the session must be added to the goal, or the patient will finish above target."),
             ("600 mL per hour; no further adjustment is needed", False, "This ignores treatment inputs such as rinse-back saline and drinks."),
             ("960 mL per hour; subtract the priming volume", False, "The arithmetic is incorrect, and inputs are added, not subtracted."),
             ("240 mL per hour; add the dialysate volume", False, "The arithmetic is incorrect; dialysate does not enter the patient."),
         ],
         "objective": "Calculate a fluid-removal goal and hourly ultrafiltration rate, accounting for fluids given during treatment.", "sources": ["flythe2020", "flythe2011"], "flag": "Which inputs are counted, and rinse-back volume, follow unit procedure and machine type."},
        {"stem": "A patient&rsquo;s monthly Kt/V is 1.1 on a prescription that should deliver 1.4. Which finding is the most likely contributor?",
         "options": [
             ("The dialysate temperature was set 0.5 &deg;C lower than usual", False, "A small temperature change does not meaningfully affect urea clearance."),
             ("Several sessions this month were shortened by late arrival and early termination", True, "Delivered time is a direct component of Kt/V. Shortened sessions, reduced blood flow, access recirculation, dialyzer clotting, and sampling errors are the common causes of a low delivered dose."),
             ("The patient gained less weight between sessions than usual", False, "Smaller fluid gains do not lower urea clearance."),
             ("The dialysate potassium was changed from 2.0 to 3.0 mmol/L", False, "Dialysate potassium affects potassium removal, not urea clearance."),
         ],
         "objective": "Interpret Kt/V and urea reduction ratio and list common reasons for low delivered adequacy.", "sources": ["hd2015", "daugirdas1993"], "flag": ""},
    ],
    "reflect": "For your last three patients, was the delivered treatment time equal to the prescribed time? If not, what took the minutes away, and was it documented?",
    "practice": {
        "intro": "On a training or unconnected machine with your preceptor, then at the chairside under direct supervision.",
        "items": [
            "Verifies every prescription element against the current order using two patient identifiers.",
            "Calculates the fluid goal including treatment inputs, and the rate in mL per hour and mL/kg per hour.",
            "States when the calculated rate would prompt a call to the physician under unit policy.",
            "Identifies delivered versus prescribed time on three treatment records.",
            "Draws or simulates pre- and post-dialysis urea samples using the unit&rsquo;s method.",
        ],
    },
    "readings": [
        ("dialysis-prescription.html", "Each element of the HD prescription explained."),
        ("dialysis-adequacy.html", "Kt/V and URR in depth."),
        ("fluid-management-dialysis.html", "Weight gain between sessions and how to limit it."),
        ("dry-weight-determination.html", "How target weight is set and revised."),
        ("hd-volume-bp-tolerance-clinician.html", "Clinician reference on volume, ultrafiltration, and blood pressure."),
    ],
    "calcs": ["calc-dialysis-adequacy-ktv.html", "calc-ufr-ceiling.html", "calc-idwg-fluid.html", "calc-dialysis-prescription.html"],
    "external": [
        ("KDOQI hemodialysis adequacy guideline: 2015 update", "https://doi.org/10.1053/j.ajkd.2015.07.015"),
    ],
    "terms": [
        ("Dialyzer", "The filter containing thousands of hollow fibers in which blood and dialysis fluid exchange solutes and water."),
        ("Dialysate", "Dialysis fluid: treated water mixed with acid and bicarbonate concentrates."),
        ("Target weight", "The post-dialysis weight at which the patient is as close as possible to normal fluid status; also called dry weight."),
        ("Recirculation", "Dialyzed blood re-entering the arterial needle instead of returning to the body, which reduces delivered dose."),
        ("Kt/V", "The dimensionless measure of dialysis dose for urea: clearance times time, divided by distribution volume."),
    ],
    "image": {
        "file": "renal-nursing-06-prescription-check",
        "alt": "Nurse compares the dialysis prescription with a training machine before treatment.",
        "purpose": "Show verification as a deliberate pause before treatment.",
        "scene": "A Filipina nurse in navy scrubs stands at a hemodialysis machine in a training room, holding a clipboard in one hand and touching the edge of the machine with the other while her eyes move from paper to machine. The bloodlines hang neatly coiled and unconnected; the chair beside the machine is empty.",
        "focal": "The nurse&rsquo;s gaze moving between clipboard and machine.",
        "setting": "Clean training bay of a Philippine dialysis center; daylight.",
        "details": "Generic machine with a blank or softly glowing screen; dialyzer mounted but dry.",
        "exclusions": "No patient connected, no blood in lines, no readable screen values, labels, or manufacturer logos.",
        "archetype": "H (Clinical)", "reviewer": "Hemodialysis nurse educator and biomedical technician",
        "diagram_note": "A membrane or circuit diagram, if wanted, must be a clinician-approved vector layout with correct flow direction; use the house dialysis-circuit-schematic skill, not free image generation.",
    },
    "flags": [
        "The 13 mL/kg per hour figure is observational and is presented as a prompt to call the physician, not a limit.",
        "Worked example values are illustrative, not targets.",
    ],
    "crosswalk": {
        "ph": "PSN 2024 nurse training topics: hemodialysis indications, prescription",
        "anna": "Hemodialysis: principles, prescription, adequacy, fluid management",
        "edtna": "Principles of hemodialysis; dialysis adequacy",
        "nncc": "Hemodialysis",
    },
}
