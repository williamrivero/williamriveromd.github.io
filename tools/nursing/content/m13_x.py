# -*- coding: utf-8 -*-
# Module 13 expansion, part 1: continuous kidney replacement therapy (CRRT) in depth.
# Hemodiafiltration (part 2) lives in m13_x2.py and attaches after "crrt-transitions".
OBJECTIVES = [
    "Compare the continuous therapy modes and prolonged intermittent therapy by what each removes, by which mechanism, and when each is chosen.",
    "Calculate a prescribed and a delivered continuous therapy dose and explain why downtime matters.",
    "Monitor regional citrate and heparin anticoagulation and recognize citrate accumulation and citrate excess.",
    "Keep an hourly fluid balance that reconciles machine fluid removal, the patient's total balance, and the prescribed goal.",
    "Troubleshoot circuit pressure alarms and complications, and interrupt, hand over, or stop continuous therapy safely.",
]
EXTRA = [
    {"after": "bedside", "id": "crrt-modes", "nav": "CRRT modes", "tag": "Continuous therapy", "h2": "The four continuous modes, and the prolonged intermittent alternative",
     "html": """
<p>Continuous renal replacement therapy (CRRT) is the form of kidney replacement therapy (KRT) built for the patient with acute kidney injury (AKI) who is too unstable for a standard 4-hour session. It runs around the clock in the intensive care unit (ICU), usually through a non-tunneled dialysis central venous catheter (CVC), and it removes solute and fluid slowly enough that blood pressure (BP) and brain water shift very little from hour to hour. The guideline suggests continuous therapy rather than standard intermittent therapy for hemodynamically unstable patients and for those with brain injury or raised intracranial pressure, and it describes continuous and intermittent therapy as complementary rather than competing.[[aki2012]]</p>
<p>Every continuous machine is a combination of the same building blocks described above: a blood pump, a filter, an effluent pump that pulls fluid out of the filter, and, depending on the mode, a pump for dialysate, one or two pumps for replacement fluid, and syringe or infusion pumps for anticoagulant. Most current machines weigh each bag on integrated scales or measure volumes with balancing chambers, and calculate the fluid balance from those weights every few seconds. The name of the mode simply tells you which of those pumps are running.</p>
<div class="table-wrap"><table>
<thead><tr><th>Mode</th><th>What runs</th><th>Main mechanism</th><th>What it removes best</th><th>Typical reason it is chosen</th></tr></thead>
<tbody>
<tr><td>Slow continuous ultrafiltration (SCUF)</td><td>Blood pump and effluent pump only; no dialysate, no replacement fluid</td><td>Ultrafiltration (UF) alone</td><td>Water, with only small amounts of solute carried along</td><td>Fluid overload, for example in heart failure resistant to diuretics, when potassium, acid&ndash;base, and urea are acceptable</td></tr>
<tr><td>Continuous venovenous hemofiltration (CVVH)</td><td>Replacement fluid, pre-filter, post-filter, or both; no dialysate</td><td>Convection</td><td>Small and middle molecules, in proportion to the volume filtered</td><td>Unit preference, or when larger molecules are a target; demands careful attention to filtration fraction</td></tr>
<tr><td>Continuous venovenous hemodialysis (CVVHD)</td><td>Dialysate flowing countercurrent; no replacement fluid</td><td>Diffusion</td><td>Small molecules: potassium, urea, hydrogen ions</td><td>Common with regional citrate protocols; lower filtration fraction, so filters tend to last longer</td></tr>
<tr><td>Continuous venovenous hemodiafiltration (CVVHDF)</td><td>Both dialysate and replacement fluid</td><td>Diffusion plus convection</td><td>Small molecules efficiently, plus some middle molecules</td><td>A flexible default in many ICUs; the mode used in the two large dose trials discussed below</td></tr>
</tbody></table></div>
<p>In every mode the machine also performs net UF: the effluent pump draws slightly more out than the dialysate and replacement pumps put in, and the difference is the fluid taken from the patient. The prescriber sets that difference separately from the clearance settings, which is why a patient can receive a high clearance dose with zero net fluid removal, or a large fluid removal with modest clearance.</p>
<p><strong>No mode has proven survival benefit over another.</strong> The choice depends on what the patient most needs (fluid, potassium, acid&ndash;base, a specific toxin), on the anticoagulation plan, on the machine and fluids the hospital stocks, and on the team&rsquo;s training. Your job is to know which mode is running and therefore which fluids, pumps, and checks apply.</p>
<p><strong>Prolonged intermittent therapy.</strong> Sustained low-efficiency dialysis (SLED), one form of prolonged intermittent renal replacement therapy (PIRRT), uses a standard hemodialysis (HD) machine with reduced blood and dialysate flows, run for roughly 6 to 12 hours, often overnight. It sits between the two extremes:</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>CRRT</th><th>SLED or PIRRT</th><th>Intermittent HD</th></tr></thead>
<tbody>
<tr><td>Duration</td><td>Around the clock</td><td>Roughly 6 to 12 hours, per order</td><td>About 3 to 5 hours</td></tr>
<tr><td>Machine</td><td>Dedicated continuous machine with bagged fluids</td><td>Standard HD machine with treated water and online dialysate</td><td>Standard HD machine</td></tr>
<tr><td>Hemodynamic gentleness</td><td>Highest</td><td>Intermediate to high</td><td>Lowest; needs an otherwise stable patient</td></tr>
<tr><td>Staffing</td><td>ICU nurse, with dialysis team support per hospital model</td><td>Dialysis nurse present or on call during the run, per hospital model</td><td>Dialysis nurse</td></tr>
<tr><td>Time off the machine for procedures and mobilization</td><td>Little</td><td>The rest of the day</td><td>Most of the day</td></tr>
<tr><td>Cost of consumables</td><td>Highest: dedicated sets and many liters of bagged fluid</td><td>Lower</td><td>Lowest</td></tr>
</tbody></table></div>
<p><strong>The Philippine picture.</strong> Continuous machines and their bagged fluids are found mainly in tertiary hospital ICUs, and the consumables are expensive for families and hospitals alike. In many Philippine hospitals, SLED on a standard HD machine, with water from the hemodialysis water system or a portable reverse osmosis unit that meets the water standard (Module 8), is the practical way to give an unstable patient a gentler treatment.[[iso23500_3]] The principles in this module apply to both: slow removal, careful anticoagulation, hourly accounting, and early reporting. When the hospital cannot offer the therapy a patient needs, the honest conversation and the referral belong to the physician; your part is accurate, timely data.</p>
"""},
    {"after": "crrt-modes", "id": "crrt-prescription", "nav": "Dose and settings", "tag": "Prescription", "h2": "Reading the prescription: dose, flows, and fluid removal",
     "html": """
<p>A complete continuous therapy order has separate lines for each pump. Read it as a set of independent instructions, because a change in one line does not automatically change the others.</p>
<div class="table-wrap"><table>
<thead><tr><th>Order element</th><th>What it controls</th><th>What the nurse checks</th></tr></thead>
<tbody>
<tr><td>Mode</td><td>Which pumps and fluids are used</td><td>The machine program matches the order; the correct fluids are hung</td></tr>
<tr><td>Blood flow</td><td>How fast blood passes through the filter</td><td>Set value; whether the catheter actually delivers it without access alarms</td></tr>
<tr><td>Dialysate rate</td><td>Diffusive clearance</td><td>Correct bag composition and rate</td></tr>
<tr><td>Replacement fluid rate and site (pre-filter, post-filter, or split)</td><td>Convective clearance and filtration fraction</td><td>Correct bag, rate, and line position</td></tr>
<tr><td>Net fluid removal</td><td>How much fluid leaves the patient each hour through the machine</td><td>Hourly target, upper and lower limits, and the conditions for stopping or reducing it</td></tr>
<tr><td>Anticoagulation</td><td>Whether the circuit is protected from clotting, and how</td><td>Agent, protocol, and laboratory monitoring schedule</td></tr>
<tr><td>Fluid composition</td><td>Potassium, phosphate, calcium, and bicarbonate in the bags</td><td>The label of every bag against the order; additives only as ordered and labeled</td></tr>
</tbody></table></div>
<p><strong>Dose is effluent.</strong> In continuous therapy, clearance of small solutes is approximately equal to the volume of effluent produced, so the dose is expressed as effluent volume per kilogram of body weight per hour. Effluent is everything the effluent pump removes: spent dialysate, filtered replacement fluid, and the net fluid removed from the patient.</p>
<p>The guideline recommends <em>delivering</em> an effluent volume of 20 to 25 mL/kg per hour for continuous therapy in AKI, and notes that this usually requires a higher prescribed volume.[[aki2012]] Two large randomized trials explain why more is not better:</p>
<ul>
<li>The RENAL trial assigned 1,508 critically ill adults with AKI to post-dilution CVVHDF at an effluent of 40 or 25 mL/kg per hour. Mortality at 90 days was 44.7% in both groups, and low phosphate was more common with the higher intensity.[[renal2009]]</li>
<li>The VA/NIH ATN trial assigned 1,124 critically ill adults to intensive or less-intensive therapy; unstable patients received CVVHDF at 35 or 20 mL/kg per hour. Mortality at 60 days was 53.6% and 51.5%, with no difference in recovery of kidney function.[[atn2008]]</li>
</ul>
<p>A higher dose therefore costs more fluid, removes more phosphate, potassium, nutrients, and antibiotics, and has not improved survival. The practical problem in most ICUs is the opposite: delivering less than was prescribed.</p>
<p><strong>Delivered versus prescribed dose.</strong> Every minute the blood pump is stopped, no clearance occurs. Bag changes, alarms, filter clotting, circuit changes, trips to imaging, and access problems all subtract from the day. Pre-filter replacement fluid also dilutes the blood before it reaches the filter, so each liter of effluent carries slightly less solute than it would in post-dilution. This is why the prescription is usually set above the target, and why recording downtime is a nursing task with direct consequences for dose.</p>
<p><strong>A worked example</strong> (an illustrative calculation, not an order). A 70 kg patient on CVVHDF has dialysate at 1,000 mL per hour, post-filter replacement at 600 mL per hour, and net removal of 100 mL per hour.</p>
<ol>
<li>Effluent = 1,000 + 600 + 100 = 1,700 mL per hour.</li>
<li>Prescribed dose = 1,700 &divide; 70 = about 24.3 mL/kg per hour.</li>
<li>Over the day, the circuit clots once and the patient goes to a computed tomography scan; the machine ran for 20 of 24 hours.</li>
<li>Delivered dose = 24.3 &times; 20 &divide; 24 = about 20.2 mL/kg per hour, at the bottom of the target band, before any allowance for dilution.</li>
</ol>
<p>The site&rsquo;s continuous therapy dose calculator performs the same arithmetic, including a correction for pre-filter replacement. Use it to check your understanding, not to change a prescription.</p>
<p><strong>Blood flow is not dose.</strong> In continuous therapy, blood flow does not set clearance the way it does in intermittent HD; the effluent does. Blood flow matters for filter life and filtration fraction: if blood flow falls (for example because of repeated access alarms) while the replacement rate stays the same, a larger share of the plasma is being filtered, the blood in the fibers thickens, and the filter clots sooner.</p>
<p><strong>Net removal is a rate, not just a daily total.</strong> A goal of &ldquo;2 liters negative by tomorrow&rdquo; is achieved safely only if the hourly rate is one the circulation can refill from the tissues. The prescriber sets the rate and the limits; the nurse watches the patient&rsquo;s response to it hour by hour, as described in the fluid section below.</p>
"""},
    {"after": "crrt-prescription", "id": "crrt-anticoag", "nav": "Anticoagulation", "tag": "Anticoagulation", "h2": "Keeping the circuit open: no anticoagulant, heparin, or regional citrate",
     "html": """
<p>Blood in a plastic circuit clots. A clotted filter stops treatment, loses the blood in the circuit if it cannot be returned, costs a new set, and lowers the delivered dose. There are three broad strategies, and the prescriber chooses among them for each patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Strategy</th><th>How it works</th><th>Main risk</th><th>Nursing monitoring, per protocol</th></tr></thead>
<tbody>
<tr><td>No anticoagulant</td><td>Relies on the patient&rsquo;s own clotting problem, pre-filter dilution, adequate blood flow, and fewer interruptions</td><td>Short filter life and lost blood</td><td>Pressure trends; filter appearance; prompt response to alarms</td></tr>
<tr><td>Unfractionated heparin</td><td>Infused into the circuit before the filter; it also enters the patient</td><td>Bleeding in the patient; heparin-induced thrombocytopenia</td><td>Clotting tests and platelet count as ordered; bleeding from catheter sites, wounds, gut, and airway</td></tr>
<tr><td>Regional citrate</td><td>Infused before the filter; binds calcium so the blood in the circuit cannot clot; calcium is replaced into the patient</td><td>Low ionized calcium, citrate accumulation, alkalosis, errors with the calcium infusion</td><td>Patient ionized calcium and post-filter ionized calcium; total calcium; blood gases and sodium</td></tr>
</tbody></table></div>
<p>The guideline suggests regional citrate rather than heparin for continuous therapy in patients who have no contraindication to citrate, and suggests unfractionated or low-molecular-weight heparin for those who cannot receive citrate.[[aki2012]] In the RICH trial, 596 critically ill patients completed treatment with either regional citrate or systemic heparin. Median filter life was 47 hours with citrate and 26 hours with heparin, and bleeding complications were less frequent with citrate (5.1% compared with 16.9%). New infections were more frequent in the citrate group (68.0% compared with 55.4%), and because the trial stopped early it could not answer whether either strategy changes survival.[[rich2020]]</p>
<p><strong>How citrate works, step by step.</strong></p>
<ol>
<li>Citrate solution is infused into the blood line just after it leaves the patient. Citrate binds ionized calcium, and the clotting cascade cannot run without ionized calcium, so the blood in the circuit does not clot.</li>
<li>In the filter, much of the citrate&ndash;calcium complex passes into the effluent and is discarded.</li>
<li>The calcium lost this way is replaced by a separate calcium infusion into the patient, either through the return line or a separate central line, according to the machine and protocol.</li>
<li>The citrate that does reach the patient is metabolized, mainly by the liver and also by muscle, and each molecule yields bicarbonate. This is why citrate protocols use fluids with less buffer than heparin protocols.</li>
</ol>
<p><strong>Two calcium numbers, two different questions.</strong> The <em>post-filter</em> ionized calcium, sampled from the circuit after the filter, answers &ldquo;Is the circuit anticoagulated enough?&rdquo; It guides the citrate rate. The <em>patient</em> ionized calcium, sampled from an arterial line or the patient&rsquo;s own vein, answers &ldquo;Is the patient safe?&rdquo; It guides the calcium infusion. Mixing up the sample sites leads to the wrong adjustment, so label every sample with its site and time. Target ranges and the adjustments for each result come from the unit&rsquo;s protocol.</p>
<p><strong>Low ionized calcium in the patient</strong> shows as tingling around the mouth or in the fingers, muscle cramps or spasm, a falling BP, arrhythmia, or a prolonged QT interval on the electrocardiogram. Check first that the calcium infusion is running, connected, and not empty; a calcium bag that ran out unnoticed is a common cause. Report at once.</p>
<p><strong>Citrate accumulation</strong> happens when citrate enters the patient faster than the body can metabolize it. The patients at risk are those with severe liver failure and those with severe shock and poor tissue perfusion, often signaled by a high or rising lactate. Because accumulated citrate keeps binding calcium, the pattern is:</p>
<ul>
<li>Total calcium rising while patient ionized calcium stays low or falls, so the total-to-ionized calcium ratio rises</li>
<li>A calcium infusion requirement that keeps increasing to hold the patient&rsquo;s ionized calcium in range</li>
<li>Worsening metabolic acidosis with an increasing anion gap, because citrate is not being turned into bicarbonate</li>
</ul>
<p>A rising ratio is reported, not managed alone; the threshold that triggers action, and the response (reducing blood flow and citrate, increasing clearance, or changing to another strategy) are set by the protocol and the prescriber.</p>
<p><strong>Citrate excess with normal metabolism</strong> is the opposite problem: the body metabolizes all the citrate it receives, and the bicarbonate produced accumulates. The patient develops metabolic alkalosis, sometimes with high sodium, since many citrate solutions carry sodium. Report a rising bicarbonate or pH; the prescriber adjusts the fluids or rates.</p>
<p><strong>Heparin and the platelet count.</strong> A platelet count that falls substantially after several days of heparin, new clotting in the circuit or the patient despite heparin, or skin lesions at injection sites raise the possibility of heparin-induced thrombocytopenia. Report it promptly. If the diagnosis is suspected or confirmed, the guideline recommends stopping all heparin, including heparin catheter locks and flushes, and using a non-heparin anticoagulant chosen by the prescriber.[[aki2012]] Other causes of a falling platelet count in the ICU, including sepsis and the circuit itself, are discussed under complications.</p>
<p><strong>Safety rules for every strategy.</strong> Anticoagulant and calcium infusions are high-alert medicines: double-check the bag, concentration, rate, and line at every change; never run the calcium infusion through the same line as the citrate; and never restart a stopped citrate or calcium infusion without knowing why it stopped. No doses appear in this module; every rate comes from the prescriber&rsquo;s order and the unit protocol.</p>
"""},
    {"after": "crrt-anticoag", "id": "crrt-fluid", "nav": "Fluid balance", "tag": "Fluid management", "h2": "Hourly fluid balance: three numbers that must agree",
     "html": """
<p>Continuous therapy is often started largely to remove fluid. Fluid overload, defined in one large multicenter study as a gain of more than 10% of body weight, was associated with higher mortality in critically ill adults with AKI, and among patients who received dialysis, survivors had less fluid accumulated when treatment started.[[bouchard2009]] The study was observational, so it shows association rather than proof that removing fluid saves lives, but it is the reason fluid balance is watched so closely.</p>
<p><strong>The three numbers.</strong> Confusion between them is the most common fluid error in continuous therapy.</p>
<div class="table-wrap"><table>
<thead><tr><th>Number</th><th>What it is</th><th>Where it comes from</th></tr></thead>
<tbody>
<tr><td>Machine net removal</td><td>The fluid the machine took out of the patient, after subtracting what it put back as dialysate and replacement fluid</td><td>The machine&rsquo;s balance display for the hour</td></tr>
<tr><td>Patient total balance</td><td>Everything in minus everything out: all infusions, flushes, medicines, nutrition, and blood products, minus urine, drains, gastric losses, stool, and machine net removal</td><td>The nurse&rsquo;s hourly intake and output record</td></tr>
<tr><td>Prescribed goal</td><td>What the prescriber wants the patient&rsquo;s balance to be per hour or per day, with limits</td><td>The order</td></tr>
</tbody></table></div>
<p>The machine knows nothing about the antibiotic infusion, the nutrition feed, or the urine bag. A machine that removed exactly what was set can still leave the patient positive if other intake is high.</p>
<p><strong>A worked hour</strong> (illustrative). The order asks for a patient total balance of 100 mL negative per hour.</p>
<ul>
<li>Intake: infusions 180 mL, enteral feed 60 mL, line flushes 10 mL = 250 mL</li>
<li>Output: urine 20 mL, surgical drain 30 mL = 50 mL</li>
<li>Machine net removal: 250 mL</li>
<li>Patient total balance = 250 &minus; 50 &minus; 250 = 50 mL negative</li>
</ul>
<p>The machine performed as set, yet the patient is 50 mL short of the goal this hour. Some units allow nurses to adjust machine removal within written limits to meet a total-balance goal; others require a call each time. Follow the order and protocol, and document which number you adjusted and why.</p>
<p><strong>Citrate and calcium infusions</strong> add volume. Depending on the machine, these may or may not be included in the machine&rsquo;s balance calculation. Find out how your machine handles them, so that they are counted once, not twice and not never.</p>
<p><strong>When to call.</strong></p>
<ul>
<li>BP falls, vasopressor needs rise, heart rate climbs, or lactate rises during removal: these suggest removal is outpacing refill from the tissues. Reduce or pause removal only as the protocol allows, and report.</li>
<li>The cumulative balance drifts from the goal by more than the protocol&rsquo;s limit over several hours, in either direction.</li>
<li>The machine reports a balance error or a fluid-loss limit has been reached.</li>
<li>Urine output rises noticeably (possible recovery; see transitions below) or the patient&rsquo;s weight, edema, or lung findings move against the goal.</li>
</ul>
<p><strong>Cumulative balance.</strong> Total the hourly patient balances across the shift and the day, and carry the running total forward from the time therapy began, and ideally from ICU admission. The site&rsquo;s continuous therapy flowsheet and fluid-removal calculators follow the same logic: hourly entries, a running total, and comparison with the goal. A daily weight, on the same bed scale and with the same equipment on the bed, is a useful cross-check but not a substitute for the hourly record.</p>
<p><strong>Handling bags on machines that weigh them.</strong> Integrated scales assume that nothing touches the bags except the machine. Common errors include:</p>
<ul>
<li>A bag swinging, touching the machine frame, or with a line resting on it while the scale reads</li>
<li>Changing a bag without using the machine&rsquo;s bag-change function, so the scale reads a sudden &ldquo;loss&rdquo; or &ldquo;gain&rdquo;</li>
<li>Hanging the wrong bag on the wrong scale, for example dialysate on the replacement scale</li>
<li>Clamps left closed after a change, or a frangible seal not fully broken</li>
<li>Draining effluent without pausing the effluent scale per the manufacturer&rsquo;s steps</li>
<li>Overriding repeated balance alarms instead of finding the cause</li>
</ul>
<p>Each of these produces an error in fluid the machine believes it removed or returned. Most machines stop treatment when cumulative balance errors exceed a set limit, precisely because unnoticed errors can reach liters over a day. Repeated balance alarms are reported and the scales checked, not cleared and restarted.</p>
<p><strong>Documentation every hour:</strong> machine net removal, all intake, all output, patient total balance, cumulative balance, the prescribed goal, vital signs, circuit pressures, any downtime with its cause and duration, and any adjustment made with its authority.</p>
"""},
    {"after": "crrt-fluid", "id": "crrt-circuit", "nav": "Circuit and alarms", "tag": "Circuit management", "h2": "The circuit: priming, pressures, filter life, and alarms",
     "html": """
<p><strong>Priming and connection.</strong> The set is loaded and primed exactly as the manufacturer directs, with the prime solution ordered by the unit, checking that the filter and all lines are free of air and that every clamp is in the right position. Connection to the catheter is an aseptic procedure (Module 7): mask, hand hygiene, clean gloves or sterile technique per policy, scrubbed hubs, and both lumens aspirated and flushed before connection, as described above for the shared safety rules. At start, the blood flow is usually increased in steps while you watch the patient&rsquo;s BP and the access and return pressures.</p>
<p><strong>The pressure points.</strong> Machines name and display them differently, but the physiology is the same.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pressure</th><th>Where it is measured</th><th>What a change usually means</th></tr></thead>
<tbody>
<tr><td>Access (arterial) pressure</td><td>Between the catheter and the blood pump; normally negative</td><td>More negative: the pump is pulling against a resistance in the catheter or vein</td></tr>
<tr><td>Pre-filter pressure</td><td>After the blood pump, before the filter; positive</td><td>Rising: clot forming in the filter, or a blockage further downstream</td></tr>
<tr><td>Return (venous) pressure</td><td>After the filter, before blood re-enters the patient; positive</td><td>Higher: blockage in the return line, catheter, or vein, or clot in the air trap. Lower or sudden fall: possible disconnection</td></tr>
<tr><td>Effluent pressure</td><td>On the fluid side of the filter</td><td>Becoming more negative: the membrane is clogging and the pump must pull harder</td></tr>
<tr><td>Transmembrane pressure</td><td>Calculated across the membrane from the other pressures</td><td>A steady rise: the membrane pores are clogging, which lowers convective clearance and warns of filter failure</td></tr>
<tr><td>Pressure drop</td><td>Pre-filter pressure minus the pressure at the filter outlet</td><td>A rise: the blood channels inside the filter are clotting</td></tr>
</tbody></table></div>
<p><strong>Trends matter more than single numbers.</strong> Record pressures hourly. A transmembrane pressure or pressure drop that rises over several hours predicts clotting long before the circuit stops, which gives time to report and to plan a controlled change with blood return instead of losing the circuit.</p>
<p><strong>Troubleshooting.</strong> Always look at the patient before the machine.</p>
<div class="table-wrap"><table>
<thead><tr><th>Alarm or trend</th><th>Likely cause</th><th>First nursing checks</th></tr></thead>
<tbody>
<tr><td>Access pressure too negative, often with coughing or position change</td><td>Catheter tip against the vessel wall, kink, low circulating volume, clot in the lumen</td><td>Position of head and hip (femoral catheters kink when the patient sits up); external kinks and clamps; dressing tension; a gentle flush per protocol; report persistent alarms. Reversing the lines is done only on a physician order or protocol, and increases recirculation</td></tr>
<tr><td>Return pressure high</td><td>Kinked or clamped return line, clot in the air trap or return lumen, patient position</td><td>Line path and clamps; air trap for clot; patient position; report if not resolved</td></tr>
<tr><td>Return pressure suddenly low</td><td>Disconnection or line separation</td><td>Look at every connection at once; stop the blood pump if blood is leaking; this is an emergency</td></tr>
<tr><td>Pre-filter pressure, transmembrane pressure, or pressure drop rising steadily</td><td>Filter clotting; post-dilution with high filtration fraction; low blood flow; inadequate anticoagulation</td><td>Anticoagulant and calcium infusions running and connected; recent interruptions; filter and air trap for dark streaks; report the trend and prepare for a planned change</td></tr>
<tr><td>Air detector alarm</td><td>Air in the return line, often from a loose connection, an empty bag, or a micro-leak</td><td>Do not override; inspect the line and air trap; remove air only by the manufacturer&rsquo;s procedure; check every connection and bag</td></tr>
<tr><td>Blood leak detector alarm</td><td>Red cells in the effluent from a ruptured fiber, or a dirty or misread sensor</td><td>Look at the effluent; follow the manufacturer&rsquo;s procedure; a confirmed leak means the filter is changed</td></tr>
<tr><td>Balance or scale alarm</td><td>Bag touching, wrong bag, clamp closed, empty or full bag</td><td>Bags hanging freely; clamps; bag levels; use the bag-change function</td></tr>
</tbody></table></div>
<p><strong>What shortens filter life.</strong> High filtration fraction, especially with post-dilution replacement; low or interrupted blood flow; frequent access alarms; a pump left stopped with blood in the circuit; inadequate or interrupted anticoagulation; and air in the circuit. Most of these are within nursing reach: a well-positioned catheter, quick responses to alarms, minimal unnecessary stops, and anticoagulant and calcium bags changed before they run out.</p>
<p><strong>Planned change versus clotted circuit.</strong> A circuit is changed when it reaches the manufacturer&rsquo;s maximum running time, when pressures show impending clotting, or when the treatment is paused for long enough that the circuit would clot. In a planned change, the blood in the circuit is returned to the patient using the machine&rsquo;s procedure, which saves a meaningful volume of blood in an anemic ICU patient. When the circuit has already clotted, or the return pressure is very high, returning the blood can push clot toward the patient. Most protocols forbid returning blood from a clotted circuit; follow yours, document the estimated blood lost, and report it.</p>
<p><strong>Machine-specific steps</strong> for priming, bag changes, blood return, and alarm handling come from the manufacturer&rsquo;s instructions and the unit&rsquo;s competency program. This module explains the reasons behind them; it does not replace them.</p>
"""},
    {"after": "crrt-circuit", "id": "crrt-complications", "nav": "Complications", "tag": "Complications", "h2": "Complications, and what continuous clearance takes away",
     "html": """
<p>Continuous clearance does not choose what it removes. Over days, it takes out heat, electrolytes, nutrients, and medicines as steadily as it removes urea and potassium.</p>
<p><strong>Hypothermia.</strong> Blood outside the body loses heat, and room-temperature fluids flowing at liters per hour cool it further. Machines have blood or fluid warmers, but patients still cool, particularly at high effluent rates. Cooling hides fever: a patient on continuous therapy may have a normal temperature despite sepsis. Look for other signs of infection (rising white cell count, new hypotension, rising lactate, a rising warmer setting needed to keep the patient warm) and report them.</p>
<p><strong>Electrolytes.</strong> Low phosphate is common and was more frequent with higher-intensity therapy in the RENAL trial.[[renal2009]] Low potassium and low magnesium are also common after the first day, especially with potassium-free or low-potassium fluids. Replacement is given as ordered, either intravenously or by changing to fluids that contain the electrolyte; the nurse ensures the laboratory schedule is followed and results are acted on.</p>
<p><strong>Acid&ndash;base.</strong> Bicarbonate-buffered fluids correct metabolic acidosis over hours to days, and the guideline suggests bicarbonate rather than lactate as the buffer, especially in shock, liver failure, or lactic acidosis.[[aki2012]] Overcorrection can cause metabolic alkalosis, particularly with citrate. Follow blood gases as ordered.</p>
<p><strong>Bleeding.</strong> Sources include the catheter site, recent surgical wounds, the gut, and the airway; heparin increases the risk. Check sites with each assessment and report new bleeding, a falling hemoglobin, or blood in drains, stool, or the endotracheal tube.</p>
<p><strong>Catheter problems.</strong> Dialysis catheters in the ICU are a source of bloodstream infection and of dysfunction from clot, kinking, or malposition. The catheter is reserved for kidney replacement therapy, handled aseptically at every connection, and inspected each shift (Module 7). Report fever, redness, discharge, or pain at the site, and repeated access alarms that do not respond to repositioning.</p>
<p><strong>Drug removal.</strong> Many medicines, including many antibiotics, are removed by continuous therapy, and their dosing differs from both normal kidney function and intermittent HD. Under-dosing an antibiotic in sepsis is as dangerous as overdosing. When a new medicine is ordered or the effluent rate changes substantially, ask the pharmacist or prescriber whether the dose has been adjusted for continuous therapy. Note the time of any long interruption, because it changes how much drug is removed.</p>
<p><strong>Nutrition.</strong> Amino acids, glucose (with some fluids), and water-soluble vitamins and trace elements pass into the effluent. Critically ill patients on continuous therapy have high protein needs; the dietitian and prescriber set the plan. Feeding interruptions for procedures are recorded so that intake can be compared with the plan.</p>
<p><strong>Low platelets.</strong> A falling platelet count in an ICU patient on continuous therapy may come from sepsis, medicines, consumption in the circuit, or heparin-induced thrombocytopenia. The cause is the prescriber&rsquo;s to determine; the nurse&rsquo;s role is to notice the trend and report it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Watch for</th><th>How you notice it</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Hypothermia</td><td>Core temperature trend; cool skin; shivering</td><td>Check the warmer; warming measures per protocol; report; remember that fever may be hidden</td></tr>
<tr><td>Low phosphate, potassium, or magnesium</td><td>Scheduled laboratory results; weakness; new arrhythmia on the monitor</td><td>Report; replace as ordered; confirm the bag composition</td></tr>
<tr><td>Low ionized calcium</td><td>Tingling, spasm, hypotension, prolonged QT interval</td><td>Check the calcium infusion; report at once</td></tr>
<tr><td>Rising total-to-ionized calcium ratio or rising calcium requirement</td><td>Laboratory trend on citrate</td><td>Report; follow the citrate accumulation protocol</td></tr>
<tr><td>Metabolic alkalosis</td><td>Rising bicarbonate and pH on blood gases</td><td>Report for adjustment of fluids or rates</td></tr>
<tr><td>Bleeding</td><td>Site checks; falling hemoglobin; blood in drains, stool, or airway</td><td>Pressure where appropriate; report; review anticoagulation with the prescriber</td></tr>
<tr><td>Catheter infection</td><td>Fever (which may be masked), redness, discharge, rising white cell count</td><td>Report; cultures as ordered; aseptic handling</td></tr>
<tr><td>Inadequate drug levels</td><td>New antibiotic order; change in effluent rate</td><td>Ask the pharmacist or prescriber about continuous therapy dosing</td></tr>
<tr><td>Falling platelet count</td><td>Daily blood count trend</td><td>Report; ask whether heparin-induced thrombocytopenia should be considered</td></tr>
<tr><td>Hemodynamic instability</td><td>Falling BP or rising vasopressor needs during removal</td><td>Reduce or pause removal within protocol; report</td></tr>
</tbody></table></div>
"""},
    {"after": "crrt-complications", "id": "crrt-transitions", "nav": "Transitions", "tag": "Transitions of care", "h2": "Interruptions, transport, recovery, step-down, and handoff",
     "html": """
<p><strong>Planned interruptions.</strong> Scans, operations, and procedures often need the patient off the machine. Discuss the plan with the team before the time comes. The usual options are:</p>
<ul>
<li><strong>Return the blood and disconnect</strong>, locking the catheter per protocol, and starting a new circuit later. This is the safest choice for long absences, at the cost of a new set.</li>
<li><strong>Disconnect and recirculate</strong> the circuit through a sterile connection, if the protocol and the manufacturer permit, for a short absence, accepting a risk of clotting and contamination and a maximum recirculation time.</li>
</ul>
<p>Either way, stop or adjust the anticoagulant and calcium infusions exactly as the protocol directs when the circuit stops. A calcium infusion that keeps running after citrate has stopped will raise the patient&rsquo;s calcium; a citrate infusion that runs without blood flow is a hazard. Record the time off and the reason, because it affects delivered dose and drug dosing.</p>
<p><strong>Transport</strong> of a patient still connected is unusual and done only where the machine and protocol allow it. More often the circuit is disconnected before transport. In either case, the catheter is secured and capped aseptically, and the team carries the plan for reconnection.</p>
<p><strong>Recognizing recovery.</strong> A rising urine output without diuretics is often the first sign of returning kidney function. Report it, together with the trend in creatinine and potassium. The prescriber may order a trial off therapy, with urine output, fluid balance, potassium, and acid&ndash;base watched closely; your hourly record is the evidence on which the decision to stay off or restart is made.</p>
<p><strong>Step-down to intermittent therapy.</strong> When the patient no longer needs vasopressors and can tolerate fluid removal over a few hours, the team may move from continuous therapy to SLED or intermittent HD, often to allow mobilization and reduce cost. The handover between ICU nurse and dialysis nurse should include the catheter&rsquo;s function, the cumulative fluid balance, the last laboratory values, the anticoagulation history, and any heparin-induced thrombocytopenia concerns.</p>
<p><strong>Stopping.</strong> Therapy is stopped on an order: when the kidneys have recovered enough, when the patient moves to intermittent therapy, or when goals of care change. The ending is planned: blood returned per protocol, infusions stopped in the correct order, the catheter locked or removed as ordered, and the final balances recorded.</p>
<p><strong>Handoff.</strong> A structured handoff in the Situation&ndash;Background&ndash;Assessment&ndash;Recommendation format reduces omissions.[[muller2018]] For a patient on continuous therapy it should include:</p>
<ul>
<li>Situation: mode, settings, anticoagulation, and current circuit age</li>
<li>Background: reason for therapy, start date, and important events (clotted circuits, bleeding, line changes)</li>
<li>Assessment: hourly and cumulative balance against the goal, latest calcium and electrolyte results, pressure trends, temperature, urine output</li>
<li>Recommendation: pending laboratory tests, the next planned circuit change, any interruption scheduled, and the questions to raise with the prescriber</li>
</ul>
<p><strong>When continuous therapy is a trial.</strong> For some patients, continuous therapy is started as a time-limited trial with agreed goals and a date to review them, as discussed in Modules 4 and 5. The nurse&rsquo;s accurate record of how the patient is responding is part of that review, and the family&rsquo;s questions are brought to the team rather than answered alone.</p>
"""},
]
QUIZ = [
    {"stem": "A patient in the intensive care unit has severe fluid overload from heart failure that has not responded to diuretics. Potassium, bicarbonate, and urea are within acceptable ranges. Which continuous mode is designed for exactly this situation?",
     "options": [
         ("Continuous venovenous hemodialysis, because diffusion is the most efficient way to remove fluid", False, "Diffusion removes small solutes such as potassium and urea; fluid is removed by ultrafiltration, which every mode can perform. Hemodialysis adds clearance the patient does not need."),
         ("Slow continuous ultrafiltration, which removes fluid without dialysate or replacement fluid", True, "Slow continuous ultrafiltration runs only the blood and effluent pumps and removes water with little solute. It suits fluid overload when chemistry is acceptable."),
         ("Continuous venovenous hemofiltration at a high replacement rate, to remove middle molecules", False, "Large replacement volumes add convective clearance that is not the problem here and increase filtration fraction and cost."),
         ("Intermittent hemodialysis for 4 hours, to remove the excess fluid quickly", False, "Rapid removal over a short session is what an unstable, overloaded patient may not tolerate; the question asks for the continuous mode designed for fluid alone."),
     ],
     "objective": "Compare the continuous therapy modes and prolonged intermittent therapy by what each removes, by which mechanism, and when each is chosen.",
     "sources": ["aki2012"], "flag": ""},
    {"stem": "An 80 kg patient on continuous venovenous hemodiafiltration has dialysate at 1,200 mL per hour, post-filter replacement at 600 mL per hour, and net removal of 200 mL per hour. The circuit ran for 18 of the last 24 hours because of two clotted filters. What best describes the delivered dose?",
     "options": [
         ("About 25 mL/kg per hour, because the prescription determines the dose", False, "25 mL/kg per hour is the prescribed dose (2,000 mL per hour divided by 80 kg). It ignores the 6 hours without clearance."),
         ("About 22.5 mL/kg per hour, because only the dialysate and replacement fluid count toward effluent", False, "Net fluid removal is also part of effluent. Leaving it out understates the prescribed dose and still ignores downtime."),
         ("It cannot be estimated without the blood flow rate", False, "In continuous therapy, small-solute clearance approximates effluent volume; blood flow matters for filter life, not for this calculation."),
         ("About 19 mL/kg per hour, below the recommended delivered range", True, "Effluent is 1,200 + 600 + 200 = 2,000 mL per hour, or 25 mL/kg per hour prescribed. Running 18 of 24 hours gives about 18.8 mL/kg per hour delivered, below the guideline&rsquo;s 20 to 25 mL/kg per hour."),
     ],
     "objective": "Calculate a prescribed and a delivered continuous therapy dose and explain why downtime matters.",
     "sources": ["aki2012"], "flag": "Illustrative arithmetic; the delivered-dose calculation ignores the small reduction from pre-filter dilution because all replacement here is post-filter."},
    {"stem": "A patient with liver failure and septic shock has been on continuous therapy with regional citrate for 30 hours. The calcium infusion has been increased three times to keep the patient's ionized calcium in range, total calcium is rising, and the metabolic acidosis is worsening. What is the most likely explanation?",
     "options": [
         ("Citrate accumulation from impaired citrate metabolism", True, "A rising total-to-ionized calcium ratio, a rising calcium requirement, and worsening acidosis together are the pattern of citrate accumulation. Liver failure and shock are the main risk factors. Report it and follow the protocol."),
         ("Citrate excess with normal metabolism, which causes metabolic acidosis", False, "When citrate is fully metabolized, the extra bicarbonate causes metabolic alkalosis, not acidosis."),
         ("The post-filter ionized calcium is too low, so the citrate infusion should be increased", False, "Post-filter calcium reflects circuit anticoagulation. Increasing citrate in a patient who cannot metabolize it would worsen accumulation."),
         ("Heparin-induced thrombocytopenia, which consumes calcium", False, "This patient is on citrate, and heparin-induced thrombocytopenia is a platelet and clotting disorder, not a cause of this calcium pattern."),
     ],
     "objective": "Monitor regional citrate and heparin anticoagulation and recognize citrate accumulation and citrate excess.",
     "sources": ["aki2012", "rich2020"], "flag": "The ratio threshold that triggers action is not stated; it comes from the unit protocol."},
    {"stem": "The order asks for a patient total balance of 100 mL negative each hour. In the last hour, the continuous machine removed exactly the 150 mL net it was set to remove. Intravenous infusions and enteral feed totaled 230 mL, and urine was 30 mL. What is the patient's balance for the hour?",
     "options": [
         ("150 mL negative, matching the machine display", False, "The machine counts only its own fluids. It does not know about infusions, feeds, or urine."),
         ("80 mL negative, ahead of the goal", False, "This adds the urine to intake rather than subtracting it as output."),
         ("50 mL positive, 150 mL off the goal", True, "Intake 230 mL minus urine 30 mL minus machine removal 150 mL = 50 mL positive. The machine worked as set, but the total balance missed the goal; act within the order and protocol and document."),
         ("Zero, because intake and output balance", False, "Intake (230 mL) does not equal total output (30 + 150 = 180 mL)."),
     ],
     "objective": "Keep an hourly fluid balance that reconciles machine fluid removal, the patient's total balance, and the prescribed goal.",
     "sources": ["bouchard2009"], "flag": ""},
    {"stem": "Over 4 hours, the transmembrane pressure and the pressure drop across the filter of a patient on continuous therapy with heparin have risen steadily. Access and return pressures are stable, and the patient is comfortable. What is the most appropriate nursing response?",
     "options": [
         ("Reposition the patient's head and hip and flush the catheter, because this is an access problem", False, "Access problems show in the access pressure, which is stable. A rising transmembrane pressure and pressure drop point to the filter."),
         ("Check that the heparin infusion is running, report the trend, and prepare for a planned circuit change with blood return", True, "These trends warn that the filter is clotting. Confirming anticoagulation and planning a controlled change allows the blood to be returned before the circuit clots."),
         ("Increase the post-filter replacement rate to flush the filter", False, "More post-filter replacement raises the filtration fraction and speeds clotting; rates are changed only on order."),
         ("Wait until the machine alarms, since the circuit is still running", False, "Once the circuit clots, its blood usually cannot be returned. Trends are acted on before the alarm."),
     ],
     "objective": "Troubleshoot circuit pressure alarms and complications, and interrupt, hand over, or stop continuous therapy safely.",
     "sources": ["anna7"], "flag": "Pressure names and alarm limits vary by machine; confirm with the manufacturer's instructions."},
]
TERMS = [
    ("Effluent", "All fluid removed by the effluent pump: spent dialysate, filtered replacement fluid, and the net fluid removed from the patient. In continuous therapy its volume approximates small-solute clearance."),
    ("Prescribed dose", "The effluent rate the order sets, expressed per kilogram of body weight per hour."),
    ("Delivered dose", "The dose the patient actually received, after subtracting time the circuit was not running."),
    ("Downtime", "Time during a continuous therapy day when the blood pump is stopped, for example for bag changes, clotting, or procedures."),
    ("Net fluid removal", "The fluid the machine removes from the patient each hour beyond what it returns as dialysate and replacement fluid."),
    ("Patient total balance", "All fluid in minus all fluid out, including machine net removal, for a set period."),
    ("Post-filter ionized calcium", "Ionized calcium measured in blood sampled after the filter; used to judge circuit anticoagulation with citrate."),
    ("Citrate accumulation", "Build-up of citrate in a patient who cannot metabolize it, shown by a rising total-to-ionized calcium ratio, a rising calcium requirement, and worsening acidosis."),
    ("Transmembrane pressure", "The pressure difference across the filter membrane; a steady rise indicates clogging of the membrane."),
    ("Pressure drop", "The difference between the pressure entering and leaving the filter on the blood side; a rise indicates clotting in the blood channels."),
    ("Recirculation (circuit)", "Connecting the ends of a disconnected circuit so that blood or prime keeps moving during a short interruption, where the protocol and manufacturer permit."),
    ("Prolonged intermittent renal replacement therapy", "Kidney replacement run on a standard machine for about 6 to 12 hours at reduced flows; sustained low-efficiency dialysis is one form."),
]
FLAGS = [
    "KDIGO 2012 AKI guideline: recommendation to deliver an effluent volume of 20 to 25 mL/kg per hour for continuous therapy (graded 1A in the guideline), with the note that a higher prescription is usually required; suggestion of regional citrate over heparin when no contraindication (2B); suggestion of continuous over intermittent therapy for hemodynamic instability and for brain injury or raised intracranial pressure (2B); bicarbonate buffer preference; stopping all heparin in heparin-induced thrombocytopenia. Wording and grades were taken from the guideline text from memory; reviewer to confirm against the published guideline (grades are not stated in the lesson).",
    "SLED duration 'roughly 6 to 12 hours' and the mode-selection table are general practice descriptions without a single cited source; confirm against unit practice.",
    "Statement that portable reverse osmosis units used for SLED must meet the dialysis water standard cites ISO 23500-3 for the water standard only; local practice for bedside water in Philippine ICUs needs reviewer confirmation.",
    "Citrate protocol details (citrate and calcium infusion sites, sample sites, target ranges for patient and post-filter ionized calcium, total-to-ionized calcium ratio threshold for action, response to accumulation) are deliberately left to the unit protocol. The ratio threshold was not stated because no source within the course's journal list was used to verify it.",
    "Whether citrate and calcium infusions are counted in the machine's fluid balance depends on the machine; confirm with the manufacturer for each model in use.",
    "Pressure names, sign conventions, alarm limits, maximum circuit running time, recirculation permission and maximum recirculation time, blood-return procedure, and the rule on returning blood from a clotted circuit are machine- and protocol-specific; confirm with the manufacturer and unit policy.",
    "Nurse-adjusted fluid removal to meet a total-balance goal is allowed in some units and not others; the lesson defers to the order and protocol.",
    "Complications and nursing watch table (hypothermia, electrolyte losses other than phosphate, nutrient and drug removal, platelet fall, catheter infection) are general clinical knowledge; only low phosphate is tied to a trial result (RENAL). Consider adding a dedicated CRRT drug-dosing or nutrition reference.",
    "Worked dose and fluid-balance examples are illustrative arithmetic, not prescriptions.",
    "Quiz item 5 cites the ANNA Core Curriculum for circuit pressure interpretation; reviewer to confirm the chapter covers continuous therapy pressure monitoring.",
]
NEW_REFS = {
    "renal2009": "19846848",
    "atn2008": "18492867",
    "rich2020": "33095849",
    "bouchard2009": "19436332",
}
