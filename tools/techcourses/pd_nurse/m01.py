# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 01: How peritoneal dialysis works, and what the PD nurse does.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain diffusion, osmotic ultrafiltration and fluid reabsorption across the peritoneal membrane, and why each changes during a dwell.",
        "Explain why water removal and small-solute clearance can move in different directions in the same patient.",
        "Explain the role of residual kidney function in volume and solute control, and why its loss changes how you read a peritoneal dialysis (PD) record.",
        "Distinguish continuous ambulatory PD (CAPD) and automated PD (APD) by workflow, dwell pattern, equipment and failure modes.",
        "Separate what you observe, record and teach from what requires a prescriber&rsquo;s order, and state when to escalate.",
    ],
    "big": """
<p>Most of what goes wrong in peritoneal dialysis (PD) is slow and quiet. A drain volume falls by a few hundred milliliters a day. Urine output halves over two months. Ankles swell a little more each week. Very little of it announces itself as an emergency. By the time the patient feels unwell, the problem has usually been visible in the diary for weeks.</p>
<p>That is the job of this module. You will learn enough physiology that small numbers mean something to you. You will learn the two ways PD is delivered and how each one fails. And you will learn where your decisions end and the nephrologist&rsquo;s begin, so that you bring the whole pattern forward early, with numbers, instead of waiting for a crisis.</p>
{{plain:Picture a tea bag in a cup of hot water. Flavor moves from where it is concentrated, the leaves, to where it is not, the water. Leave the bag longer and the cup darkens, but more and more slowly, because the difference between inside and outside keeps shrinking. That is diffusion. It is how urea, creatinine and potassium move from the blood into the dialysis solution.}}
<p>The picture has a limit. A tea bag does not pull water. PD solution does: its glucose, or icodextrin, draws water out of the blood by osmosis. And unlike a cup, the abdomen keeps absorbing fluid back into the body, through lymphatics and tissue, the whole time the solution sits there. So every PD dwell runs three processes at once: solute diffusion, osmotic water removal and steady fluid reabsorption. Each changes on its own clock. Most of what you read in a PD record is the balance among the three.</p>
{{cards:Key terms for this module|Dwell::The time the solution stays in the abdomen between fill and drain.|Ultrafiltration (UF)::Fluid removed by dialysis. Net UF is the drained volume minus the filled volume.|Residual kidney function::The filtering and urine the patient&rsquo;s own kidneys still provide.|Icodextrin::A large glucose polymer that is absorbed slowly, used for long dwells.|Effluent::The fluid drained out after a dwell.|Cycler::The machine that performs automated exchanges, usually overnight.}}
""",
    "case": {"title": "Positive numbers, rising weight", "html": """
<p><strong>Aling Rosario, 58</strong>, a retired public-school teacher from Malolos, has been on CAPD for seven months with four 2-liter exchanges a day. Nurse <strong>Paolo</strong> reviews her diary at a routine clinic visit.</p>
<p>Every exchange shows positive net ultrafiltration, drain greater than fill. The daily total is about 600 mL, much as it was three months ago. Her daughter has written each number neatly in a school notebook.</p>
<p>But her morning weight has climbed 2.4 kg over five weeks. Her ankles pit to mid-shin. Her urine diary, which read about 700 mL a day when she started, now reads about 250 mL. She says she feels &ldquo;a little heavy&rdquo; and has started using a second pillow at night.</p>
""", "questions": ["Is a positive ultrafiltration total enough to call her volume status stable?",
                  "What four questions would you ask before you call?",
                  "What belongs to you, and what belongs to the nephrologist?"]},
    "sections": [
        ("the-physiology", "The physiology", "The physiology: three processes in one dwell", """
<p>You do not need to calculate transport to be a good PD nurse. You do need a working model, because every number in the diary is the output of that model. Start with the membrane, then follow a single dwell from fill to drain.</p>
<h3>The membrane is not a single sheet</h3>
<p>The peritoneum is a large, folded membrane that lines the abdominal wall and covers the bowel. What actually limits transport is the wall of the small blood vessels beneath it. That wall behaves as if it has pores of three sizes.[[pd_morelle2021]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Pathway</th><th>What crosses</th><th>Why it matters at the bedside</th></tr></thead>
<tbody>
<tr><td>Many small pores</td><td>Water and small solutes such as urea, creatinine, potassium and glucose</td><td>Most clearance and much of the water removal</td></tr>
<tr><td>A few large pores</td><td>Proteins, including albumin</td><td>PD patients lose albumin into the effluent every day, which is one reason nutrition gets attention</td></tr>
<tr><td>Water-only channels (aquaporin-1)</td><td>Water without sodium</td><td>Explains the early &ldquo;sodium sieving&rdquo; of a strong glucose dwell</td></tr>
</tbody></table></div>
<p>This three-pore model is established physiology.[[pd_morelle2021]] It explains most of what follows.</p>
{{fig:pd01_pores}}
<h3>Diffusion runs down a gradient that fades</h3>
<p>At the start of a dwell, the dialysis solution contains almost no urea. The gradient between blood and solution is steep, so urea moves quickly. Within a few hours, the solution approaches the blood level and movement slows. Larger molecules diffuse more slowly and keep gaining for longer. This is why the prescriber chooses dwell length and the number of exchanges deliberately. A longer dwell does not keep cleaning at the same rate. It mostly gives the slow molecules more time.</p>
<h3>Osmotic water removal also fades</h3>
<p>Glucose draws water into the abdomen. But glucose is itself absorbed across the membrane into the blood, so the osmotic pull weakens as the dwell goes on. Early in a glucose dwell, about half of the water moves through the aquaporins and leaves sodium behind. That is sodium sieving, seen about one hour into a strong dwell.[[pd_morelle2021]]</p>
<p>Meanwhile, reabsorption never stops. Lymphatics and the surrounding tissue keep taking fluid back into the body. Once the osmotic pull has faded, reabsorption wins. A long glucose dwell can therefore end with less fluid out than went in.</p>
<p>Icodextrin behaves differently. It is a large glucose polymer that is absorbed slowly, so it keeps pulling water through the small pores for many hours. That is why it is often prescribed for the long night dwell in CAPD or the long day dwell in APD.[[pd_morelle2021]] Whether a patient receives it is the prescriber&rsquo;s decision.</p>
<h3>Example: one night, two numbers</h3>
<p>Mang Tonyo, 66, does four CAPD exchanges a day with glucose solution. His daytime dwells last about four hours. His night dwell lasts about nine hours, from 10 PM to 7 AM.</p>
<div class="table-wrap"><table>
<thead><tr><th>Exchange</th><th>Filled</th><th>Drained</th><th>Net UF</th></tr></thead>
<tbody>
<tr><td>7 AM (night dwell drained)</td><td>2,000 mL</td><td>1,850 mL</td><td>&minus;150 mL</td></tr>
<tr><td>11 AM</td><td>2,000 mL</td><td>2,250 mL</td><td>+250 mL</td></tr>
<tr><td>3 PM</td><td>2,000 mL</td><td>2,200 mL</td><td>+200 mL</td></tr>
<tr><td>7 PM</td><td>2,000 mL</td><td>2,250 mL</td><td>+250 mL</td></tr>
<tr><td><strong>Day total</strong></td><td></td><td></td><td><strong>+550 mL</strong></td></tr>
</tbody></table></div>
<p>The night dwell gave 150 mL back to his body. The day total still looks positive, so the problem is easy to miss. The pattern is exactly what the physiology predicts: the osmotic pull was spent long before morning, and reabsorption continued. Your job is not to change his solution. Your job is to notice that the long dwell is net negative, check that the diary was measured correctly, and report it with his weight, blood pressure and urine trend. The prescriber decides whether a different solution or dwell pattern is needed.</p>
{{key:Read the long dwell on its own. A positive daily total can hide a long dwell that is giving fluid back.}}
<h3>Water removal and clearance can move apart</h3>
<p>A patient can have good urea removal and poor fluid removal, or the reverse. The difference often lies in how fast the membrane transports.</p>
<div class="table-wrap"><table>
<thead><tr><th>Membrane pattern</th><th>Small solutes</th><th>Glucose gradient</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Fast transporter</td><td>Equilibrate quickly; good clearance in short dwells</td><td>Absorbed quickly; osmotic pull lost early</td><td>Poor drain after long dwells, rising weight, edema</td></tr>
<tr><td>Slow transporter</td><td>Equilibrate slowly</td><td>Kept longer</td><td>Good fluid removal in long dwells; clearance may be lower</td></tr>
</tbody></table></div>
<p>Consider two patients on the same four-exchange prescription. Ms. Divina drains well all day and her weight is steady, yet the team notes falling appetite and laboratory trends that suggest low clearance. Mr. Arnel feels well and eats normally, yet his night drains are always short and his ankles swell. Same prescription, opposite problems. The formal measurement behind this, the peritoneal equilibration test (PET), is the subject of Module 6. For now, remember that one good number does not prove the other.</p>
<h3>Residual kidney function carries more weight than most nurses expect</h3>
<p>Many people start PD still passing several hundred milliliters of urine a day. That urine removes sodium, water and middle molecules continuously, every hour, without any exchange. In observational studies, preserving it is associated with better survival in PD.[[pd_brown2020]] The studies cannot show that protecting urine output causes the better survival, because patients who keep their urine differ in other ways. The direction is consistent, and the physiology makes it plausible.</p>
<p>When urine output falls, the patient loses a fluid-removal route that the PD prescription was never designed to replace. Do the arithmetic for Aling Rosario. Her urine fell from about 700 mL to about 250 mL a day. That is about 450 mL a day that must now leave by some other route, or stop coming in. Her exchange UF did not change. So the 450 mL stays in her body each day, and her weight tells you where it went.</p>
{{key:Whenever you read a PD record, ask what the kidneys are still contributing. Count urine and UF together.}}
<h3>What this means at the bedside</h3>
<div class="table-wrap"><table>
<thead><tr><th>Process</th><th>What normally happens</th><th>What weakens it</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>Diffusion of small solutes</td><td>Gradient steep early, flattens over hours</td><td>Missed exchanges, short total therapy time, membrane change, low drain volume</td><td>Fatigue, poor appetite, nausea, itch; laboratory trends the team reviews</td></tr>
<tr><td>Osmotic ultrafiltration</td><td>Strong early, fades as glucose is absorbed</td><td>Long glucose dwell, fast transport, peritonitis, wrong solution strength</td><td>Falling drain volumes, rising weight, edema, breathlessness</td></tr>
<tr><td>Fluid reabsorption</td><td>Continuous through lymphatics and tissue</td><td>Higher in some patients; makes long dwells net negative</td><td>Drain less than fill after a long dwell</td></tr>
<tr><td>Residual urine</td><td>Removes sodium and water daily</td><td>Kidney-toxic medicines, low blood pressure, infection, time</td><td>Falling urine volume in the diary, new edema despite unchanged PD</td></tr>
</tbody></table></div>
"""),
        ("capd-and-apd", "CAPD and APD", "CAPD and APD: two ways to deliver the same therapy", """
<p>Both forms of PD use the same membrane and the same physiology. They differ in who does the exchanges, when, and what can go wrong.</p>
<h3>Continuous ambulatory PD</h3>
<p>Continuous ambulatory PD (CAPD) uses manual exchanges, usually three to five a day. Solution sits in the abdomen almost all the time. Each exchange is drain, then fill, then dwell. The patient is free between exchanges but must stop, wash, set up and connect for each one. That is about half an hour, several times a day, every day.</p>
<p>The failure modes are human. Technique gets rushed when the patient is late for work. An exchange gets skipped during a family wake. The patient touches the connector while answering the door. A stronger bag is mistaken for a weaker one in poor light. None of these happens because the patient is careless. They happen because a skill repeated more than a thousand times a year drifts.</p>
{{fig:pd01_day}}
<h3>Automated PD</h3>
<p>Automated PD (APD) uses a cycler, usually overnight, to do several short exchanges while the patient sleeps. Many prescriptions add a long day dwell, often called the &ldquo;last fill,&rdquo; or a midday exchange. The daytime is mostly free, which suits work and school.</p>
<p>APD keeps the human failure modes and adds the machine. The cycler program may not match the written order. Drain alarms interrupt sleep, and a tired patient may bypass them. A brownout stops treatment halfway through the night. The long day dwell may give fluid back if its solution does not suit the patient&rsquo;s membrane.</p>
<h3>Example: two households, two sets of risks</h3>
<p><strong>Nanay Celia, 61</strong>, runs a sari-sari store from the front of her house in Bulacan. She does CAPD. Her exchange corner is behind the store, near the counter where customers call out. Her risk is interruption. A customer calls while her line is open, and she reaches for the gate. You would teach her to finish the connection before answering, to hang a &ldquo;Sandali lang po&rdquo; sign during exchanges, and to treat any touch of the open connector as a contamination event.</p>
<p><strong>Jun, 34</strong>, drives a jeepney in Quezon City and starts work at 5 AM. He chose APD so he can dialyze while he sleeps. His risks are power and fatigue. His barangay loses power during typhoons, and he admits to pressing through drain alarms because he needs his sleep. You would check that his written plan covers a power failure, review his treatment record for repeated alarms, and report a pattern of shortened therapy to the nephrologist.</p>
<p>Neither form is better for every person. The choice depends on the person&rsquo;s life, home, transport, electricity, storage space and membrane characteristics. The prescriber selects the regimen. You make sure the person can carry it out safely, and that what is delivered matches what is ordered.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>CAPD</th><th>APD</th></tr></thead>
<tbody>
<tr><td>Who exchanges</td><td>Patient or helper, by hand</td><td>Cycler, set up by patient or helper</td></tr>
<tr><td>When</td><td>Several times through the day</td><td>Mostly overnight, often with a day dwell</td></tr>
<tr><td>Typical failure modes</td><td>Skipped or rushed exchanges, touch contamination, wrong bag</td><td>Program mismatch, bypassed alarms, power loss, net-negative day dwell</td></tr>
<tr><td>What you check</td><td>Diary, technique, supplies, bag labels</td><td>Treatment record against the order, alarms, power plan, day dwell drain</td></tr>
</tbody></table></div>
{{key:Both forms share three requirements: a working catheter, consistent aseptic technique and a reliable plan for when something goes wrong.}}
"""),
        ("what-the-pd", "Your role", "What the PD nurse does, and where the line sits", """
<p>Under the Philippine Nursing Act (Republic Act 9173), nursing practice includes assessment, health teaching, collaboration with the team and carrying out written orders.[[pd_ra9173]] In PD that becomes a clear division of work.</p>
<div class="table-wrap"><table>
<thead><tr><th>You do</th><th>You route to the prescriber</th></tr></thead>
<tbody>
<tr><td>Verify patient, modality, solution, strength and volumes against the written order</td><td>Any change in solution strength, dwell, cycler program or icodextrin use</td></tr>
<tr><td>Compare what was actually delivered with what was ordered</td><td>Any medicine start, stop or dose change, including antibiotics</td></tr>
<tr><td>Assess volume status, symptoms, exit site and effluent</td><td>Interpretation of PET and adequacy results for a prescription change</td></tr>
<tr><td>Teach, observe return demonstration and judge readiness under program criteria</td><td>Modality change, catheter procedures and admission decisions</td></tr>
<tr><td>Triage calls, activate the PD pathway and document a closed-loop handoff</td><td>Diagnosis of peritonitis and the choice of treatment</td></tr>
</tbody></table></div>
<p>The line is not about importance. Your observations are often the first warning the team gets. A nephrologist who sees a patient every month or two depends on you to notice what happened in between.</p>
<h3>Example: three calls on a Monday morning</h3>
<p><strong>Call one.</strong> A patient&rsquo;s son asks whether his mother can &ldquo;just use the stronger bag&rdquo; because her feet are swollen. Changing solution strength is a prescription change. You assess her by phone: weight trend, breathing, urine, missed exchanges, salt and fluid intake. You tell him not to change the bag on his own, and you call the nephrologist with the pattern.</p>
<p><strong>Call two.</strong> A patient on APD reports that the cycler showed a total therapy time two hours shorter than usual, after repeated drain alarms. Comparing delivered therapy with the order is yours. You ask him to read the treatment record aloud, check his position and lines with him, and document the gap. If the pattern repeats, it goes to the nephrologist.</p>
<p><strong>Call three.</strong> A patient asks you to explain why her 7 AM drain is always smaller than the others. Teaching is yours. You explain the fading glucose gradient and reabsorption in plain words, and you record the question so the team knows she is watching.</p>
<p>In each call you did real work: you assessed, verified, taught and reported. You did not change a solution, a program or a medicine.</p>
<h3>Reporting a pattern</h3>
<p>A good report lets the nephrologist decide without calling you back. Use a structured handoff such as SBAR: Situation, Background, Assessment, Recommendation.</p>
<div class="table-wrap"><table>
<thead><tr><th>Weak report</th><th>Useful report</th></tr></thead>
<tbody>
<tr><td>&ldquo;Doc, Aling Rosario seems puffy.&rdquo;</td><td>&ldquo;Aling Rosario, CAPD seven months. Weight up 2.4 kg in five weeks, pitting to mid-shin, two pillows now. Urine down from about 700 to about 250 mL a day. Exchange UF unchanged at about 600 mL. No missed exchanges. More soup since the rains. Not breathless at rest. Requesting review of her fluid plan this week.&rdquo;</td></tr>
</tbody></table></div>
{{key:Report a pattern with numbers, times and what you already checked. Leave the decision on the prescription with the prescriber.}}
"""),
        ("red-flags-in", "Red flags", "Red flags in this module", """
<p>Most findings in this module go to a same-day or next-visit review. A few do not wait.</p>
{{stop:<ul><li>Positive ultrafiltration on paper, yet weight rising and urine falling: the total fluid picture is worsening. Report the same day.</li><li>New breathlessness at rest, inability to lie flat, or chest pain: emergency pathway, not routine review.</li><li>Any cloudy effluent, even with no pain: same-day PD team contact (Module 7).</li></ul>}}
<p>For example, if Aling Rosario had told Paolo she could not lie down at all last night and was breathless sitting in the clinic, the plan changes. She goes to the emergency department under your local pathway, and the nephrologist is called on the way. A routine fluid review would be too slow.</p>
{{call:Call the nephrologist or follow your emergency pathway for breathlessness at rest, chest pain or confusion. Do not wait for the next clinic visit.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is positive UF enough?</strong> No. Paolo does not stop at &ldquo;UF is positive.&rdquo; Her fluid leaves by two routes, the exchanges and her kidneys. One route held steady. The other fell by about 450 mL a day. Her weight gain over five weeks is the sum of that difference.</p>
<p><strong>The four questions.</strong> Is she breathless lying flat? Mildly; two pillows now instead of one. Are all four exchanges being done? Yes; she has not missed any. Has her fluid and salt intake changed? She admits to more <em>sabaw</em> since the rains started. Are drain volumes measured the same way? Yes; same bathroom scale, same method.</p>
<p><strong>What the pattern means.</strong> The PD prescription has not changed, but one of her fluid-removal routes has. Paolo records weight, blood pressure, edema, urine trend and diary totals. He screens for emergency features and finds none at rest. He calls the nephrologist the same day with the full pattern.</p>
<p><strong>Whose decision.</strong> Solution strength, icodextrin and diuretics belong to the nephrologist. The teaching about salt and fluid belongs to Paolo, and so does the follow-up call in three days to see whether her weight has turned.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete both tasks with a peer while your preceptor observes.",
               "items": [("Using a simple drawing, explain fill, dwell and drain to a peer acting as a new patient. Include why the long dwell may return less fluid than it received.", False),
                         ("Sort ten statements supplied by your preceptor into &ldquo;nursing observation to record and report&rdquo; and &ldquo;change that requires a new order.&rdquo;", False)]},
    "quiz": [
        ("Which process moves urea from blood into dialysis solution during a dwell?",
         ["Diffusion down a concentration gradient", "Osmotic ultrafiltration through aquaporins", "Lymphatic absorption", "Active tubular secretion"], 0,
         "Urea moves from the high level in the blood to the low level in fresh solution. Aquaporins move water, not urea. Lymphatics return fluid to the body. Tubular secretion happens in the kidney, not the peritoneum."),
        ("Why does net ultrafiltration slow, and sometimes reverse, late in a long glucose dwell?",
         ["The catheter becomes obstructed", "Urea concentration rises in the blood", "Glucose is absorbed, the osmotic gradient fades, and reabsorption continues", "The patient&rsquo;s urine output increases"], 2,
         "The osmotic pull is spent as glucose crosses into the blood, while lymphatic and tissue reabsorption keep going. Obstruction causes a poor drain, not a reversal. Blood urea and urine output do not drive water removal in the dwell."),
        ("Why is icodextrin often used for the long dwell?",
         ["It clears potassium faster than glucose", "It prevents peritonitis", "It replaces residual kidney function", "It is absorbed slowly and sustains water removal over many hours"], 3,
         "Its large molecules stay in the abdomen and keep drawing water through the small pores. It does not prevent infection or replace the kidneys. Whether it is used is the prescriber&rsquo;s decision."),
        ("Aling Rosario&rsquo;s exchanges show positive net UF, but her weight is rising and her urine has fallen. What is the best interpretation?",
         ["Volume status is fine because UF is positive", "Total fluid removal has fallen; assess the whole balance and report the trend", "The scale is broken", "She should skip an exchange to rest the membrane"], 1,
         "Urine and UF are two routes for the same fluid. When urine falls and UF does not rise, the difference stays in the body. Check the scale, but do not assume it. Skipping an exchange is unsafe."),
        ("Which statement about CAPD and APD is correct?",
         ["APD never has a day dwell", "APD adds programming and machine-related failure modes to the human ones", "CAPD uses a cycler overnight", "CAPD is always better for working adults"], 1,
         "APD keeps the human risks and adds program mismatch, alarms and power dependence. Many APD prescriptions include a day dwell. The cycler belongs to APD. Neither form suits everyone."),
        ("What does sodium sieving early in a strong glucose dwell reflect?",
         ["Protein leak through large pores", "Potassium moving into the solution", "Contamination of the bag", "Water crossing aquaporins without sodium"], 3,
         "Water moving through aquaporins leaves sodium behind, so the solution&rsquo;s sodium falls briefly. The other options describe unrelated processes."),
        ("Why do PD patients lose albumin into the effluent every day?",
         ["Through large pores in the peritoneal capillaries", "Because glucose binds albumin", "Because of tubular damage", "Only during peritonitis"], 0,
         "A small number of large pores lets protein out. Losses rise during peritonitis but happen every day. Glucose binding and tubular damage are not the mechanism."),
        ("Mr. Arnel feels well, but his night drains are always short and his ankles swell. Which membrane pattern fits best?",
         ["Slow transport with excellent long-dwell UF", "No difference from any other patient", "Fast transport, with early loss of the glucose gradient in long dwells", "No glucose absorption"], 2,
         "Fast transporters absorb glucose quickly, lose their osmotic pull early and drain short after long dwells. Slow transporters do the opposite. The prescriber confirms the pattern with a PET."),
        ("Which action is within the PD nurse&rsquo;s role without a new order?",
         ["Changing the solution from 1.5% to 2.5% glucose", "Starting intraperitoneal antibiotics on suspicion", "Comparing delivered therapy with the written order and reporting a discrepancy", "Adding icodextrin for the night dwell"], 2,
         "Verification and reporting are core nursing work. Solution, icodextrin and antibiotics are prescription decisions. Antibiotics may be given under a written standing protocol, but never on the nurse&rsquo;s own decision."),
        ("Aling Rosario&rsquo;s urine fell from about 700 mL to about 250 mL a day, and her exchange UF did not change. About how much extra fluid stays in her body each day?",
         ["About 450 mL", "About 250 mL", "About 700 mL", "None, because UF is positive"], 0,
         "700 minus 250 is about 450 mL a day that no longer leaves by the kidneys. With unchanged UF and intake, it accumulates, which matches her weight gain."),
        ("Which finding in this module calls for the emergency pathway rather than routine review?",
         ["Mild ankle edema", "New breathlessness at rest", "One slightly smaller drain", "A question about diet"], 1,
         "Breathlessness at rest may mean acute fluid overload or a heart problem. Edema and one small drain need assessment and trend review. A diet question is routine teaching."),
        ("How should you report a worsening fluid pattern?",
         ["&ldquo;She seems puffy.&rdquo;", "Only the last exchange volume", "Wait for the next clinic visit", "Weight trend, blood pressure, edema, urine and UF totals, intake change, and what you checked"], 3,
         "A complete report with numbers lets the prescriber decide without calling you back. A vague word, a single number or a delay does not."),
        ("Mang Tonyo&rsquo;s night dwell drains 150 mL less than was filled, but his day total is +550 mL. What is the best response?",
         ["Ignore it, because the daily total is positive", "Tell him to shorten the night dwell himself", "Check the measurement, then report the net-negative long dwell with his weight, blood pressure and urine trend", "Change his night bag to icodextrin"], 2,
         "A positive total can hide a long dwell that gives fluid back. Confirm the numbers and report the pattern. Changing dwell length or solution is a prescription decision."),
        ("In observational studies, preserved residual kidney function in PD is:",
         ["Proven by randomized trials to double survival", "Associated with better survival", "Unrelated to outcomes", "Harmful"], 1,
         "The evidence is observational. It shows an association, not proof that protecting urine output causes longer survival. The other options overstate or contradict the data."),
        ("A patient asks why he cannot leave the night dwell in longer &ldquo;for more cleaning.&rdquo; The best answer explains that:",
         ["Longer dwells always clean better", "The catheter will block", "Transport slows as the gradient flattens and fluid may be absorbed back, so the prescriber sets the dwell length", "Longer dwells cause peritonitis"], 2,
         "Small-solute transport plateaus and a long glucose dwell can turn net negative. Blockage and infection are not the reason."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Icodextrin", "A large glucose polymer solution absorbed slowly, used for long dwells."),
              ("Residual kidney function", "The filtering and urine output the patient's own kidneys still provide."),
              ("Aquaporin", "A water-only channel in capillary walls that lets water cross without sodium."),
              ("Sodium sieving", "The early fall in dialysate sodium when water crosses aquaporins without sodium."),
              ("Fast transporter", "A membrane that equilibrates small solutes quickly and loses the glucose gradient early."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Last fill", "The final APD fill that stays in during the day, also called the day dwell."),
              ("Peritoneal equilibration test (PET)", "A standardized 4-hour dwell that measures how fast solutes cross the membrane and how much water is removed."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("SBAR", "Situation, Background, Assessment, Recommendation: a structured handoff."),
              ("Return demonstration", "The learner performs the skill while the trainer observes.")],
    "readings": [("peritoneal-dialysis-ckd.html", "The patient-facing guide to PD that your patients may read."),
                 ("dialysis-adequacy.html", "How dialysis dose is measured and why it is only part of the picture.")],
    "calcs": ["calc-pd-adequacy.html"],
}
