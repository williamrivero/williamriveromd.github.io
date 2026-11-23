# -*- coding: utf-8 -*-
# Module 13 expansion, part 2: online hemodiafiltration (HDF). Sections follow the CRRT expansion (m13_x.py).
OBJECTIVES = [
    "Explain how online hemodiafiltration (HDF) makes substitution fluid from ultrapure dialysate, and how it differs from high-flux hemodialysis (HD) and from expanded HD with medium cut-off membranes.",
    "Calculate convection volume from substitution volume and net ultrafiltration, and relate it to blood flow, filtration fraction, and treatment time.",
    "State the access, machine, water, and dialysate requirements for safe online HDF, including ultrapure dialysate and sterile, non-pyrogenic substitution fluid.",
    "Summarize the randomized evidence comparing HDF with HD, including CONVINCE, and state what remains uncertain using calibrated language.",
    "Run and monitor an HDF session, respond to HDF-specific alarms, and audit achieved convection volume at unit level.",
]
EXTRA = [
    {"after": "crrt-transitions", "id": "hdf-principles", "nav": "Online HDF", "tag": "Hemodiafiltration",
     "h2": "Online hemodiafiltration: how the machine makes fluid safe to infuse",
     "html": """
<p>Earlier in this module you built the picture of convection: water pushed across the membrane drags dissolved solutes with it, and the larger the volume moved, the more of the larger solutes leave. Hemodiafiltration (HDF) applies that picture to the ordinary outpatient session. It keeps everything that hemodialysis (HD) already does by diffusion and adds a large convective volume on top. Because far more fluid is filtered out of the blood than the patient could lose safely, most of it has to be given back as substitution fluid during the same session.</p>
<p><strong>Where the substitution fluid comes from.</strong> Many liters per session are needed, far more than could practically be hung as bags. In <em>online</em> HDF the machine makes the fluid itself, continuously, from the dialysate it is already preparing. The chain runs like this:</p>
<ol>
<li>Treated water from the unit&rsquo;s reverse osmosis (RO) loop is mixed with acid and bicarbonate concentrates inside the machine, exactly as for HD (Module 8).</li>
<li>The fresh dialysate passes through a first ultrafilter, a filter fine enough to hold back bacteria and endotoxin. The resulting fluid is <strong>ultrapure dialysate</strong>, and it is used on the dialysate side of the dialyzer.</li>
<li>A portion of that ultrapure dialysate is drawn off and passes through a second ultrafilter (on some machines a further stage as well). This cascade produces the substitution fluid, which the substitution pump infuses directly into the blood line.</li>
</ol>
<p><strong>Why it can be safe to infuse.</strong> Each ultrafilter stage removes most of what reached it, so passing fluid through filters in series reduces bacteria and endotoxin far below what any single stage achieves. The relevant international standard for dialysis fluid is Part 5 of the International Organization for Standardization (ISO) 23500 series, ISO 23500-5:2024, on the quality of dialysis fluid. It requires online-prepared substitution fluid to be sterile and non-pyrogenic, and requires the online process to be validated to produce it. Sterility at that level cannot be proved by culturing a sample at the bedside; it depends on a validated machine and filter system used exactly as the manufacturer intends, on clean water and dialysate upstream, and on disciplined disinfection. That is why every requirement in the sections below exists, and why substitution fluid is handled as an intravenous medicine, as set out in the shared safety rules earlier in this module.</p>
<p><strong>The membrane.</strong> HDF uses a high-flux dialyzer, because only a membrane with high water permeability can pass 20 or more liters of plasma water in a session at a tolerable transmembrane pressure. The dialyzer model is part of the order; it is not interchangeable with a low-flux dialyzer.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>High-flux HD</th><th>Expanded HD (medium cut-off membrane)</th><th>Online HDF</th></tr></thead>
<tbody>
<tr><td>Main clearance mechanism</td><td>Diffusion, with a small amount of internal convection</td><td>Diffusion plus more internal convection within the dialyzer</td><td>Diffusion plus deliberate, high-volume external convection</td></tr>
<tr><td>Membrane</td><td>High-flux</td><td>Medium cut-off, with larger effective pores</td><td>High-flux</td></tr>
<tr><td>Substitution fluid infused</td><td>None</td><td>None</td><td>Many liters per session, made online</td></tr>
<tr><td>Machine</td><td>Standard HD machine</td><td>Standard HD machine</td><td>HDF-capable machine with an online fluid module</td></tr>
<tr><td>Middle-molecule removal</td><td>Some</td><td>More than high-flux HD</td><td>More than high-flux HD, rising with convection volume</td></tr>
<tr><td>Main concern to watch</td><td>Dialysate quality (Module 8)</td><td>Albumin loss into the dialysate</td><td>Sterile substitution fluid, hemoconcentration, achieving the volume</td></tr>
</tbody></table></div>
<p>Expanded HD should not be confused with HDF. It aims at a similar goal, more removal of larger solutes, without infusing any fluid, but the survival trials described later in this module tested online HDF, and their results cannot simply be transferred to medium cut-off membranes, which have not yet been shown in a large randomized trial to change survival.</p>
<p><strong>What convection adds.</strong> Small solutes such as urea and potassium are already cleared efficiently by diffusion, so HDF changes them little. The gain is in &ldquo;middle molecules&rdquo;, which diffuse too slowly to be removed well. The best-known marker is beta-2 microglobulin, a protein of about 11,800 daltons whose long-term accumulation is linked to dialysis-related amyloidosis, with carpal tunnel syndrome and joint pain in patients on dialysis for many years. HDF lowers pre-dialysis beta-2 microglobulin levels more than HD does. Phosphate is also removed somewhat more, but phosphate leaves the tissues slowly, so treatment time and diet remain the main tools for it; HDF does not replace phosphate binders or dietary teaching.</p>
<p><strong>Albumin.</strong> Albumin is larger than the pores of a high-flux membrane and is largely retained, but small losses do occur in HDF and rise with very high transmembrane pressures and with some membranes. In most patients the loss is minor; it matters more in a patient who is already malnourished. Serum albumin trends are reviewed with the physician and dietitian like any other nutritional marker, and a falling albumin is reported, not attributed to HDF by the nurse.</p>
"""},
    {"after": "hdf-principles", "id": "hdf-prescription", "nav": "HDF prescription", "tag": "Hemodiafiltration",
     "h2": "The HDF prescription: convection volume and what drives it",
     "html": """
<p>An HDF order contains everything an HD order contains (Module 6) plus the parameters of convection. The single number that best summarizes the convective dose is the <strong>convection volume</strong>: the total volume of plasma water filtered across the membrane during the session.</p>
<p><strong>Convection volume = substitution volume + net ultrafiltration (UF) volume.</strong></p>
<p>Net UF is the fluid removed to bring the patient toward target weight; it is filtered out and not replaced, so it counts as convection too. Substitution volume is the fluid filtered out and then given back. Most machines display the substitution volume and the UF volume, and many also display the convection volume itself.</p>
<p><strong>The high-volume target.</strong> The large recent trial, CONVINCE, enrolled patients judged able to receive a convection volume of at least 23 liters per session, and the mean volume actually delivered in the HDF group was 25.3 liters.[[convince2023]] Earlier analyses of pooled trial data had found the lowest mortality among patients receiving the highest volumes, above 23 liters per 1.73 m&sup2; of body surface area.[[peters2016]] Many units therefore use 23 liters per session as a working target. The target for each patient is the physician&rsquo;s order and unit protocol, not the nurse&rsquo;s choice.</p>
<p><strong>Post-dilution versus pre-dilution in practice.</strong> In post-dilution, substitution fluid enters the venous line after the dialyzer. Every liter filtered carries plasma at its full solute concentration, so each liter does the most work; this is why the major trials used post-dilution. The limit is inside the fiber: as water is pulled out, the blood thickens toward the dialyzer exit. In pre-dilution, fluid enters before the dialyzer, so the blood is thinner as it passes the membrane and very high filtration is possible, but each liter filtered is partly the substitution fluid itself, so a much larger volume is needed for the same clearance. Mixed (or mid-) dilution modes split the fluid between the two points. Pre-dilution or mixed modes are used, by order, when hemoconcentration repeatedly limits post-dilution, for example in a patient with a high hematocrit or high plasma protein, or in a circuit that keeps clotting. Their volume targets are different from post-dilution targets, and the two kinds of numbers must not be compared directly.</p>
<p><strong>The determinants.</strong> In post-dilution, the safe convective flow is limited to a fraction of the blood flow (HDF machines and studies usually express this as convective flow divided by blood flow, a simpler bedside cousin of the plasma-based filtration fraction defined earlier in this module; both rise and fall together). Holding that fraction steady, convection volume is set by:</p>
<ul>
<li><strong>Effective blood flow.</strong> The single biggest lever. It depends on the access, the needle size, and an arterial pressure that allows the pump to fill.</li>
<li><strong>Effective treatment time.</strong> Every minute lost to a late start, an alarm, or early sign-off is convection lost.</li>
<li><strong>Filtration fraction the circuit tolerates.</strong> This depends on hematocrit, plasma protein, the membrane, and the machine&rsquo;s own limits.</li>
</ul>
<p><em>Worked illustration, arithmetic for teaching only; not a prescription.</em> A four-hour session lasts 240 minutes. To reach 23 liters (23,000 mL), convective flow must average 23,000 &divide; 240 = about 96 mL/min. With a blood flow of 350 mL/min, that is 96 &divide; 350 = about 27% of the blood flow. Keep the same 27% but let the access deliver only 300 mL/min, and the convective flow falls to about 81 mL/min; over 240 minutes that is about 19.4 liters, below the target, although nothing else changed. If the 300 mL/min session also ends 20 minutes early, the volume falls to about 17.8 liters. For the same patient, a session record showing a substitution volume of 21.0 liters and net UF of 2.5 liters gives a convection volume of 21.0 + 2.5 = 23.5 liters.</p>
<p>The illustration shows why blood flow and time, not the substitution setting alone, decide whether the target is reached. It also shows a trap: net UF counts toward the convection volume, but it is set by the patient&rsquo;s fluid status, never raised to make the convection number look better.</p>
<p><strong>Auto-substitution features.</strong> Some HDF machines can set the substitution rate automatically. The machine continuously reads pressures across the dialyzer, and on some models other measurements, and adjusts the substitution rate to keep filtration near the highest level the circuit can tolerate without excessive hemoconcentration. Such features usually raise achieved volumes and reduce manual adjustment, but they work within limits that the unit sets and they cannot create blood flow that the access does not deliver. How the feature works, what it measures, and when it is used are machine-specific and follow the manufacturer&rsquo;s instructions and unit protocol.</p>
<p><strong>What the nurse verifies against the order before starting</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>What to check</th></tr></thead>
<tbody>
<tr><td>Modality and mode</td><td>HDF selected on the machine; post-, pre-, or mixed dilution as ordered</td></tr>
<tr><td>Dialyzer</td><td>The high-flux model ordered; correct patient label if dialyzers are reprocessed and unit policy permits reprocessing for HDF</td></tr>
<tr><td>Blood flow and time</td><td>As ordered; needle size matched to the blood flow by the unit chart (Module 7)</td></tr>
<tr><td>Substitution setting</td><td>The ordered rate or volume, or auto-substitution if ordered</td></tr>
<tr><td>Convection volume target</td><td>Recorded on the treatment sheet so that the achieved volume can be compared at the end</td></tr>
<tr><td>Net UF goal</td><td>Calculated from today&rsquo;s pre-dialysis weight and the current target weight, as for HD</td></tr>
<tr><td>Dialysate and anticoagulation</td><td>As for HD: concentrates, temperature, and anticoagulant all match the current order</td></tr>
</tbody></table></div>
"""},
    {"after": "hdf-prescription", "id": "hdf-requirements", "nav": "Requirements", "tag": "Hemodiafiltration",
     "h2": "What safe HDF requires: patient, machine, water, and people",
     "html": """
<p>HDF is not simply a machine setting. It depends on four things being right at the same time: a patient whose access can deliver the blood flow, a machine built for it, water and dialysate of a higher microbiological quality than many units need for HD, and staff trained in its specific steps.</p>
<p><strong>The patient and the access.</strong> High convection volumes need a high, steady blood flow. A well-functioning arteriovenous fistula or graft usually provides it. A tunneled catheter may or may not, depending on its position and function; the convection volume often falls on catheter sessions, and a catheter that cannot sustain the flow limits the volume no matter what else is set. Patients for whom HDF may be less suitable, or in whom the expected benefit is less certain, include those whose access cannot provide the necessary flow, those with recurrent circuit clotting at high filtration fractions, and those whose overall goals of care favor the simplest effective treatment. Selection is the physician&rsquo;s decision. The nurse contributes the evidence: achievable blood flow, arterial and venous pressure trends, how often the target was reached, and how sessions are tolerated.</p>
<p><strong>The machine.</strong> Online HDF requires a machine designed and validated for it, with an online substitution fluid module, its own ultrafilters, a substitution pump, and the software and alarms that control filtration. A standard HD machine cannot be converted at the bedside. The machine also performs its own pre-treatment tests; on many models these include an integrity test of the ultrafilters, and a failed test means that the machine is not used for HDF until the fault is corrected.</p>
<p><strong>Water and dialysate quality.</strong> Dialysis water must meet the water standard described in Module 8.[[iso23500_3]] For HDF, the dialysate itself must also be ultrapure, and the substitution fluid sterile. The dialysis fluid standard, ISO 23500-5:2024, sets these limits:[[iso23500_5]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Fluid</th><th>Total viable microbial count</th><th>Endotoxin</th></tr></thead>
<tbody>
<tr><td>Standard dialysis fluid</td><td>Less than 100 colony-forming units (CFU) per mL</td><td>Less than 0.5 endotoxin units per mL</td></tr>
<tr><td>Ultrapure dialysis fluid</td><td>Less than 0.1 CFU per mL</td><td>Less than 0.03 endotoxin units per mL</td></tr>
<tr><td>Online-prepared substitution fluid</td><td>Sterile, produced by a process validated to achieve sterility; no culture limit is set, because sterility cannot be shown by routine sampling</td><td>Non-pyrogenic</td></tr>
</tbody></table></div>
<p>The facility&rsquo;s adopted standard, including the edition in force, governs; these values are shown so that the nurse understands the size of the step from HD to HDF. Ultrapure dialysate has a bacterial limit one thousand times stricter than standard dialysate. Reaching it consistently depends on the whole chain: a well-maintained RO loop without stagnant branches, clean concentrate handling (bicarbonate in particular supports bacterial growth), machine fluid paths disinfected on schedule, and intact ultrafilters.</p>
<ul>
<li><strong>Ultrafilters</strong> are changed at the interval the manufacturer specifies, usually counted in treatments or hours of use, and earlier if the machine reports a failed integrity test. The change, the filter lot, and the reason are logged.</li>
<li><strong>Disinfection</strong> of the machine follows the manufacturer&rsquo;s schedule and method. A skipped or incomplete disinfection is treated as a reason not to use the machine for HDF until it has been done.</li>
<li><strong>Microbiological and endotoxin testing</strong> of water and dialysate follows the unit&rsquo;s written policy, which sets the sampling points (including dialysate from HDF machines), the methods, the frequency, and the action levels. Sampling technique is the same aseptic technique taught in Module 8. Follow the Department of Health (DOH) licensing requirements and any Philippine Society of Nephrology (PSN) guidance that apply to the facility; this course does not state a testing frequency, because it must come from those sources and the unit policy.</li>
</ul>
<p><strong>Staff training and documentation.</strong> Every nurse who sets up, runs, or ends HDF needs documented training on the specific machine model, observed practice, and periodic competency review. The training covers the substitution line connection, the online priming and rinse-back steps where the machine uses them, the HDF-specific alarms, and the logs. Dialysis technicians who maintain the machines and water system need parallel training on ultrafilter changes, integrity tests, and disinfection.</p>
<p><strong>The Philippine context.</strong> Online HDF is available in a limited but growing number of Philippine units, mostly in larger urban centers, because it requires HDF-capable machines, a water system able to support ultrapure dialysate reliably, and recurring costs for ultrafilters, testing, and training. Where it is offered, the cost to the patient and what any insurer or government program will pay should be explained before the patient chooses, using the unit&rsquo;s current written information rather than figures remembered from elsewhere. Patients who cannot reach high convection volumes, or who cannot afford HDF, continue to receive good care with well-delivered high-flux HD.</p>
"""},
    {"after": "hdf-requirements", "id": "hdf-evidence", "nav": "HDF evidence", "tag": "Evidence",
     "h2": "What the trials show, and what they do not",
     "html": """
<p>For two decades, observational studies suggested that patients treated with HDF lived longer than patients on HD. Observational studies cannot separate the effect of a treatment from the effect of who receives it: healthier patients with better access are more likely to be placed on HDF and to reach high volumes. Randomized trials were needed, and their results at first appeared to disagree.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Patients and comparison</th><th>Primary outcome and result</th><th>Note on convection volume</th></tr></thead>
<tbody>
<tr><td>CONTRAST (2012)</td><td>714 patients; post-dilution online HDF versus low-flux HD</td><td>All-cause death: no significant difference (hazard ratio 0.95; 95% confidence interval 0.75 to 1.20)</td><td>In an on-treatment analysis, patients who received higher volumes had lower mortality; the authors stated that this subgroup finding required confirmation</td></tr>
<tr><td>Turkish online HDF study (2013)</td><td>782 patients; post-dilution online HDF versus high-flux HD</td><td>Composite of death and nonfatal cardiovascular events: no significant difference (event-free survival 77.6% versus 74.8%)</td><td>Mean filtration volume about 17.2 liters; in a post hoc analysis, patients above 17.4 liters had better survival</td></tr>
<tr><td>ESHOL (2013)</td><td>906 patients; high-efficiency post-dilution online HDF versus continued HD</td><td>All-cause death 30% lower with HDF (hazard ratio 0.70; 95% confidence interval 0.53 to 0.92)</td><td>Designed around high-efficiency HDF; sessions complicated by low blood pressure and all-cause hospitalization were also less frequent with HDF</td></tr>
<tr><td>CONVINCE (2023)</td><td>1,360 patients on high-flux HD for at least 3 months, all judged able to receive at least 23 liters; high-volume HDF versus continued high-flux HD</td><td>All-cause death 17.3% (118 of 683) with HDF versus 21.9% (148 of 677) with HD over a median of 30 months (hazard ratio 0.77; 95% confidence interval 0.65 to 0.93)</td><td>Mean delivered convection volume 25.3 liters per session</td></tr>
</tbody></table></div>
<p>Sources for the table: CONTRAST,[[contrast2012]] the Turkish study,[[turkhdf2013]] ESHOL,[[eshol2013]] and CONVINCE.[[convince2023]]</p>
<p><strong>Why the earlier trials differed.</strong> The most consistent explanation is the convective dose actually delivered. The trials that found no overall benefit delivered lower volumes on average, and in both of them the patients who happened to receive higher volumes did better. These were post hoc and on-treatment analyses, so they show an association, not proof: patients who reach high volumes usually have better access and better health, and those advantages could explain part of their survival. CONVINCE addressed this directly by enrolling only patients able to receive high volumes and randomizing them, and it found lower mortality with HDF.[[convince2023]] The comparison group also matters: CONTRAST compared HDF with low-flux HD, while the Turkish study and CONVINCE compared it with high-flux HD, which is the usual comparator today.</p>
<p><strong>Pooled analyses.</strong> An individual-participant analysis of four earlier trials, with 2,793 participants, estimated a 14% lower risk of all-cause death and a 23% lower risk of cardiovascular death with HDF, with the largest benefit among those receiving more than 23 liters per 1.73 m&sup2; of body surface area per session.[[peters2016]] A later individual-patient meta-analysis that added CONVINCE, with five trials and 4,153 patients, found all-cause death in 23.3% of patients on HDF and 27.0% on HD over a median of 30 months (hazard ratio 0.84; 95% confidence interval 0.74 to 0.95), no clear difference in effect across patient subgroups, and lower risk with higher convection volume in a graded pattern.[[vernooij2024]] The dose&ndash;response finding is still drawn from volumes that patients achieved rather than volumes assigned at random, so it supports, but does not prove, the idea that the volume itself is what matters.</p>
<p><strong>Quality of life.</strong> In CONVINCE, both groups reported a gradual decline in health-related quality of life over time. The decline was slower with HDF in physical function, cognitive function, pain interference, and social participation; the authors described the effect as moderate, most pronounced for cognitive function.[[convinceqol2024]] This is a meaningful finding for patients, who often value how they feel and function as much as survival, but it should not be presented as &ldquo;HDF makes you feel better&rdquo;. A patient switched to HDF may notice no difference from one session to the next.</p>
<p><strong>What remains uncertain.</strong></p>
<ul>
<li><strong>Who benefits.</strong> The trial evidence applies best to patients who can receive high volumes. Whether patients with poor access, frequent catheter use, very frail health, or twice-weekly schedules gain the same benefit is not known.</li>
<li><strong>Applicability to Asian and Philippine patients.</strong> CONVINCE was conducted in European centers, and most trial patients were European or Turkish. Body size, vascular access patterns, dialysis schedules, causes of kidney failure, and access to transplantation differ in the Philippines. Smaller body size may make a fixed 23-liter target harder or less necessary to reach; volume scaled to body surface area is one proposed answer, but it has not been tested as a target in its own right.</li>
<li><strong>Why it works.</strong> Proposed explanations include greater removal of middle molecules, less inflammation, and better blood pressure stability during treatment. None has been proven to be the cause.</li>
<li><strong>Other outcomes and newer trials.</strong> Hospitalization, cost-effectiveness in lower-income health systems, and long-term effects outside Europe are less certain. Additional trials have been conducted or are under way; their results should be read as they are published, rather than assumed in either direction.</li>
</ul>
<p><strong>How to talk about it.</strong> A fair summary for a colleague or a patient is that high-volume online HDF reduced the risk of death compared with high-flux HD in a large randomized trial of patients able to receive high volumes, and that pooled trial data point the same way. It is not accurate to say that HDF benefits every patient, that any HDF session is as good as a high-volume one, or that HD has become unsafe. The decision to offer HDF belongs to the physician and the patient, and the nurse&rsquo;s role is to make sure that, where HDF is chosen, the dose actually delivered resembles the dose that was tested.</p>
"""},
    {"after": "hdf-evidence", "id": "hdf-session", "nav": "HDF session", "tag": "Clinical application",
     "h2": "Running an HDF session: before, during, and after",
     "html": """
<p>An HDF session follows the same sequence as an HD session (Module 9), with additions at each stage. The machine&rsquo;s operator&rsquo;s manual and the unit&rsquo;s written procedure govern the exact steps, which differ between manufacturers.</p>
<p><strong>Before the session</strong></p>
<ul>
<li><strong>Machine status.</strong> Confirm from the logs that the machine has been disinfected on schedule, that its ultrafilters are within the manufacturer&rsquo;s change interval, and that the most recent dialysate culture and endotoxin results for this machine or loop are within the unit&rsquo;s limits. A machine that fails any of these checks is not used for HDF; the charge nurse and physician decide whether the patient receives HD instead.</li>
<li><strong>Self-tests.</strong> Allow the machine to complete all pre-treatment tests, including the ultrafilter integrity test where the model performs one. A failed test is never bypassed or repeated until it passes without finding the cause.</li>
<li><strong>Prescription check.</strong> Verify every item in the table in the prescription section against the current order.</li>
<li><strong>Substitution line.</strong> Connect the substitution line to the machine&rsquo;s substitution port and to the correct point on the blood line (after the dialyzer for post-dilution, before it for pre-dilution) exactly as the manufacturer&rsquo;s procedure shows, with aseptic technique. This line carries fluid straight into the bloodstream; touching or contaminating the connection is treated like contaminating an intravenous (IV) line.</li>
<li><strong>Priming.</strong> Some machines prime the circuit with online-prepared fluid instead of bagged saline; follow the machine&rsquo;s procedure and make sure all air is cleared from the substitution line.</li>
<li><strong>Patient.</strong> Assess as for HD, with particular attention to the access, because the session depends on it: thrill and bruit, recent cannulation problems, and the previous session&rsquo;s arterial and venous pressures.</li>
</ul>
<p><strong>During the session</strong></p>
<ul>
<li><strong>Reach the ordered blood flow early</strong> and keep it. A convection target is often missed simply because blood flow was kept low for the first hour.</li>
<li><strong>Watch transmembrane pressure and its trend.</strong> A slow, steady rise across the session suggests hemoconcentration or progressive clotting of the fibers; a sudden rise suggests a line or flow problem.</li>
<li><strong>Look for signs of hemoconcentration:</strong> darkening blood in the venous line, a rising pressure at the dialyzer inlet where displayed, clots or foam in the venous drip chamber, and filtration fraction alarms.</li>
<li><strong>Blood pressure and fluid.</strong> Monitor blood pressure (BP) and symptoms at the unit&rsquo;s usual intervals. Substitution fluid is volume-neutral when the machine is working correctly, so low blood pressure during HDF is assessed exactly as in HD: UF rate, target weight, and the patient&rsquo;s condition. Check that the UF volume displayed matches the expected hourly rate; a balancing fault is a fluid-safety emergency.</li>
<li><strong>Temperature.</strong> Substitution fluid is warmed to the dialysate temperature, and a large volume enters the blood directly. Report chills, rigors, or fever at once. A rigor during HDF is treated as a possible pyrogenic reaction or infection from contaminated fluid until shown otherwise: stop substitution, follow the unit protocol, keep the patient safe, and notify the physician.</li>
<li><strong>Interim volume check.</strong> At the midpoint, compare the convection volume so far with where it should be; a shortfall is easier to correct, by order, at two hours than at the end.</li>
</ul>
<div class="table-wrap"><table>
<thead><tr><th>Alarm or problem</th><th>Likely meaning</th><th>First nursing check</th><th>Escalate when</th></tr></thead>
<tbody>
<tr><td>Transmembrane pressure high</td><td>Too much filtration for the blood flow; hemoconcentration; fibers clotting</td><td>Confirm the actual blood flow (a very negative arterial pressure means the pump is not filling); look for dark streaks or clots; check lines for kinks; reduce substitution rate as the protocol allows</td><td>It recurs after correction, clotting is visible, or the protocol does not cover the next step</td></tr>
<tr><td>Substitution or infusion fault</td><td>Problem with the substitution line, pump segment, connection, or online fluid supply</td><td>Check the line for kinks, clamps, and secure connection; check for air in the line; follow the machine&rsquo;s prompts</td><td>The fault persists, air is found, or contamination of the connection is suspected</td></tr>
<tr><td>Blood leak</td><td>Blood detected in the dialysate side, usually a fiber rupture; at high transmembrane pressures, ruptures are more likely</td><td>Stop as the machine directs; inspect the dialysate outflow for pink or red color</td><td>Always: a confirmed leak means the dialyzer is changed per protocol, and blood is not returned unless the protocol allows it</td></tr>
<tr><td>Conductivity</td><td>Dialysate composition wrong; both dialysate and substitution fluid are affected</td><td>Check concentrate containers, connections, and that they match the order; the machine diverts fluid until corrected</td><td>It does not correct, or the patient has received fluid of uncertain composition</td></tr>
<tr><td>Filtration fraction limit</td><td>Convective flow too high relative to blood flow</td><td>Check that blood flow is at the ordered level and the access is delivering it; reduce substitution rate as the protocol allows</td><td>The ordered convection target cannot be reached at a safe filtration fraction; report for prescription review</td></tr>
<tr><td>Ultrafilter integrity test failed</td><td>The barrier that makes substitution fluid safe may be breached</td><td>Do not start or continue HDF on that machine</td><td>Always: report to the technician and charge nurse; HD on another machine only by order</td></tr>
</tbody></table></div>
<p>As with every alarm in this course, the cause is found before the alarm is reset, and limits are never widened to keep the session running.</p>
<p><strong>Anticoagulation.</strong> High filtration concentrates blood inside the fibers toward the dialyzer exit, so circuits in post-dilution HDF tend to clot more readily than in HD at the same anticoagulant dose. The anticoagulant and its dose remain the physician&rsquo;s order. Report repeated clotting, streaked dialyzers, or sessions shortened by clotting, because the remedy may be a different anticoagulation plan, a different dilution mode, or a different substitution setting, and each is a prescribing decision.</p>
<p><strong>Ending the session.</strong> Follow the machine&rsquo;s procedure for ending treatment and returning blood. Some machines return blood using online-prepared fluid rather than bagged saline; the return volume counts in the fluid balance either way. Disconnect the substitution line as the procedure directs and dispose of single-use components; never reuse a substitution line.</p>
<p><strong>Documentation.</strong> In addition to the usual HD record, document for every HDF session: the dilution mode; substitution volume; net UF volume; achieved convection volume; whether the ordered target was reached; the effective blood flow and effective treatment time; and, if the target was missed, the reason (access, catheter, clotting, alarms, shortened session, patient request). Record HDF-specific alarms and the action taken. A missed target is not a failure to hide; it is information the physician and the unit audit need.</p>
"""},
    {"after": "hdf-session", "id": "hdf-unit", "nav": "HDF in the unit", "tag": "Quality",
     "h2": "Introducing and auditing HDF in a dialysis unit",
     "html": """
<p>The benefit seen in trials came from high volumes delivered session after session. A unit that offers HDF without measuring what it delivers cannot know whether its patients are receiving the treatment that was tested. Auditing HDF uses the quality improvement methods from Module 12 and the water and dialysate controls from Module 8.</p>
<p><strong>Before starting an HDF program,</strong> a unit typically confirms that its water system and machines can consistently meet the ultrapure dialysate standard, with baseline culture and endotoxin results; writes procedures for setup, monitoring, alarms, ending, logs, and adverse events; trains and signs off staff on each machine model; agrees on which patients will be offered HDF and how the choice is explained; and sets the indicators it will review.</p>
<div class="table-wrap"><table>
<thead><tr><th>Area</th><th>What to monitor</th><th>Questions the review asks</th></tr></thead>
<tbody>
<tr><td>Delivered dose</td><td>Achieved convection volume per session; proportion of sessions reaching each patient&rsquo;s ordered target</td><td>Which patients repeatedly miss the target, and why: blood flow, catheter, time, clotting, alarms?</td></tr>
<tr><td>Treatment time</td><td>Effective minutes delivered versus minutes prescribed</td><td>Are late starts or early sign-offs costing volume?</td></tr>
<tr><td>Water and dialysate</td><td>Culture and endotoxin results by sampling point, including HDF machines; trend toward action levels</td><td>Is any result rising, even if still below the limit? Was the response documented?</td></tr>
<tr><td>Ultrafilters and disinfection</td><td>Change log against the manufacturer&rsquo;s interval; integrity test failures; missed disinfections</td><td>Was any machine used for HDF outside its filter interval or after a missed disinfection?</td></tr>
<tr><td>Safety events</td><td>Pyrogenic reactions, bloodstream infections, blood leaks, balancing faults, circuit clotting</td><td>Is there a cluster by machine, shift, or day? Was each event reported and investigated?</td></tr>
<tr><td>Staff competency</td><td>Training records and periodic sign-off for each nurse and technician</td><td>Is everyone who runs HDF currently signed off on that machine model?</td></tr>
<tr><td>Patient experience</td><td>Tolerance, symptoms, and patient-reported concerns</td><td>Are patients informed and comfortable with the treatment and its costs?</td></tr>
</tbody></table></div>
<p><strong>Incident reporting.</strong> Report through the unit&rsquo;s system any HDF session run with an overdue ultrafilter, a failed or bypassed integrity test, a missed disinfection, a contaminated substitution connection, a chill or fever during treatment, a fluid-balance error, or a water or dialysate result above the action level. A cluster of febrile reactions is handled under the cluster rule taught in Module 8: stop connecting new patients to the suspected source, assess those affected, and notify the physician, technician, and medical director.</p>
<p><strong>Patient education.</strong> Patients often expect a new treatment to feel different. Explain plainly:</p>
<ul>
<li><strong>What changes:</strong> the machine filters and replaces a large volume of fluid during the session; a higher blood flow is needed, so needle size or cannulation may change; setup may take a little longer; the cost may differ, and this is discussed before starting.</li>
<li><strong>What does not change:</strong> the schedule and full session time still matter; salt and fluid limits stay the same, because the fluid given back is replaced liter for liter and does not remove extra fluid; diet, phosphate binders, and other medicines continue as ordered; the access still needs daily care.</li>
<li><strong>What to report:</strong> chills, fever, or feeling unwell during or after a session; any change in the access; anything about the treatment that worries them.</li>
<li><strong>What to expect:</strong> most patients feel little difference from session to session. The benefit shown in trials was over years, and it depended on receiving the full volume regularly, which is why staying the full time and protecting the access matter.</li>
</ul>
<p>Where HDF is offered, it is a choice, not an upgrade every patient must take. A patient who stays on well-delivered high-flux HD, because of access limits, cost, or preference, has not been given second-rate care, and should never be made to feel so.</p>
"""},
]
QUIZ = [
    {"stem": "A patient on post-dilution HDF has an ordered convection volume target of at least 23 liters per session. At the end of today's session the machine shows a substitution volume of 19.8 liters and a net ultrafiltration volume of 2.4 liters. What should the nurse conclude and do?",
     "options": [
         ("The convection volume is 19.8 liters, which is the substitution volume alone; record it as below target", False, "Net ultrafiltration is also fluid filtered across the membrane and counts toward convection volume, so the substitution volume alone understates the dose."),
         ("The convection volume is 22.2 liters, below the target; document the achieved volume and the likely reason, and report the shortfall", True, "Convection volume is substitution plus net ultrafiltration: 19.8 + 2.4 = 22.2 liters. A missed target is documented with its cause (blood flow, time, clotting, alarms) so the physician can review the prescription."),
         ("The convection volume is 17.4 liters, because net ultrafiltration is subtracted from the substitution volume", False, "Net ultrafiltration is added, not subtracted; both volumes are filtered out of the blood."),
         ("Next session, increase the net ultrafiltration goal by 1 liter so that the target is reached", False, "Net ultrafiltration is set by the patient's fluid status and target weight. Raising it to improve the convection number risks low blood pressure and excessive fluid removal."),
     ],
     "objective": "Calculate convection volume from substitution volume and net ultrafiltration, and relate it to blood flow, filtration fraction, and treatment time.", "sources": ["convince2023"], "flag": ""},
    {"stem": "A patient starting online HDF asks, worried, how fluid made by the machine from tap water can be safe to run straight into her bloodstream. Which explanation is accurate?",
     "options": [
         ("The chlorine in tap water kills any germs before the machine uses it", False, "Chlorine and chloramine are removed before dialysis because they harm patients; they are not what makes substitution fluid safe."),
         ("The dialyzer membrane filters out any germs before the fluid reaches her blood, so its quality matters less than for a drip", False, "In post-dilution HDF the substitution fluid enters the blood line directly, after the dialyzer, so the dialyzer offers no protection; fluid quality is essential."),
         ("The fluid is the same as the dialysate used in ordinary hemodialysis, which is always sterile", False, "Standard dialysate is not required to be sterile. HDF requires ultrapure dialysate and a further filtering stage to produce sterile substitution fluid."),
         ("It is made from ultrapure dialysate passed through further filters, in a process validated to give sterile, fever-free fluid", True, "Online substitution fluid is produced from ultrapure dialysate through a cascade of ultrafilters in a validated process, which depends on clean water, scheduled disinfection, and filter changes."),
     ],
     "objective": "Explain how online hemodiafiltration (HDF) makes substitution fluid from ultrapure dialysate, and how it differs from high-flux hemodialysis (HD) and from expanded HD with medium cut-off membranes.", "sources": ["iso23500_5", "iso23500_3"], "flag": ""},
    {"stem": "Two hours into a post-dilution HDF session, transmembrane pressure has risen steadily, a filtration fraction alarm sounds, and the blood in the venous line looks darker than at the start. The arterial pressure is more negative than earlier. Blood pressure is stable and the patient feels well. What is the best first action?",
     "options": [
         ("Raise the transmembrane pressure alarm limit, since the patient is stable and the session still has to reach its convection target", False, "Widening a limit removes the warning without addressing hemoconcentration or clotting, and may lead to a clotted circuit or a fiber rupture."),
         ("Increase the net ultrafiltration rate so that more fluid is filtered", False, "Increasing ultrafiltration would worsen hemoconcentration and remove fluid the patient may not have to spare."),
         ("Check that the access delivers the set blood flow, look for clotting, lower substitution within protocol, and inform the physician", True, "The more negative arterial pressure suggests the pump is not getting its full flow, which raises the filtration fraction. Restoring flow, looking for clotting, and lowering substitution within protocol address the cause; the physician reviews the prescription."),
         ("Give an additional anticoagulant bolus to prevent the circuit from clotting", False, "Anticoagulant doses are given only by order. The first step is to find the cause, which here appears to be reduced blood flow."),
     ],
     "objective": "Run and monitor an HDF session, respond to HDF-specific alarms, and audit achieved convection volume at unit level.", "sources": ["anna7"], "flag": "Transmembrane pressure and filtration fraction limits and permitted substitution-rate changes are machine- and protocol-specific."},
    {"stem": "During a unit meeting, a colleague says: \"CONVINCE proved that HDF lowers deaths for every dialysis patient, so any HDF session, whatever the volume, is better than hemodialysis.\" Which response best reflects the evidence?",
     "options": [
         ("It showed lower mortality with high-volume HDF in patients able to receive at least 23 liters; benefit at lower volumes is uncertain", True, "CONVINCE enrolled only patients judged able to achieve at least 23 liters and compared high-volume HDF with high-flux HD; earlier trials with lower volumes did not show an overall benefit."),
         ("CONVINCE found no significant difference in all-cause mortality between the groups, so HDF offers no survival advantage over hemodialysis", False, "CONVINCE reported lower all-cause mortality with HDF: 17.3% versus 21.9% (hazard ratio 0.77; 95% confidence interval 0.65 to 0.93)."),
         ("CONTRAST and the Turkish trial already showed the same benefit at lower volumes, so volume does not matter", False, "Neither trial showed an overall benefit; their post hoc analyses associated better survival with higher volumes."),
         ("The benefit in CONVINCE came from pre-dilution HDF, which can be used at any blood flow", False, "CONVINCE used high-volume HDF delivered in post-dilution mode, which depends on adequate blood flow."),
     ],
     "objective": "Summarize the randomized evidence comparing HDF with HD, including CONVINCE, and state what remains uncertain using calibrated language.", "sources": ["convince2023", "contrast2012", "turkhdf2013"], "flag": ""},
    {"stem": "At the start of a shift, a nurse reviewing the machine log sees that the substitution-fluid ultrafilter on machine 4 is past the manufacturer's change interval. The machine has just passed its routine self-test, and a patient is scheduled for HDF on it in 15 minutes. What should the nurse do?",
     "options": [
         ("Proceed with HDF because the machine passed its self-test, and ask the technician to change the filter after the last shift today", False, "A passed test does not override the manufacturer's change interval; the filter is the barrier that makes substitution fluid sterile."),
         ("Run the session in pre-dilution mode, which is safer when the filter is old", False, "Dilution mode does not change the quality of the substitution fluid; in either mode it enters the blood directly."),
         ("Proceed with HDF and monitor the patient closely for chills or fever", False, "Monitoring would detect a reaction only after contaminated fluid had been infused. Prevention is required."),
         ("Withhold machine 4 from HDF until the filter is changed and logged, and tell the charge nurse so the patient's treatment is rearranged", True, "Ultrafilters are changed at the manufacturer's interval. The machine is withheld from HDF, the change is logged, and the patient's treatment is arranged under an order. The lapse is reported through the incident system."),
     ],
     "objective": "State the access, machine, water, and dialysate requirements for safe online HDF, including ultrapure dialysate and sterile, non-pyrogenic substitution fluid.", "sources": ["iso23500_3"], "flag": "Ultrafilter change interval is set by each manufacturer."},
]
TERMS = [
    ("Online hemodiafiltration", "HDF in which the machine prepares substitution fluid continuously from ultrapure dialysate during the session."),
    ("Convection volume", "Total plasma water filtered across the membrane in a session: substitution volume plus net ultrafiltration."),
    ("High-volume HDF", "HDF delivering a large convection volume per session; at least 23 liters was the entry requirement in CONVINCE."),
    ("Ultrapure dialysate", "Dialysate with a total viable count below 0.1 CFU per mL and endotoxin below 0.03 endotoxin units per mL (ISO 23500-5:2024)."),
    ("Ultrafilter (endotoxin-retentive filter)", "A filter on the dialysate path fine enough to hold back bacteria and endotoxin; used in series to make substitution fluid."),
    ("Post-dilution", "Infusing substitution fluid into the blood line after the dialyzer; the most efficient mode, limited by hemoconcentration."),
    ("Medium cut-off membrane", "A dialyzer membrane with larger effective pores used in expanded HD on a standard machine, without substitution fluid."),
    ("Beta-2 microglobulin", "A middle molecule of about 11,800 daltons used as a marker of convective removal; its accumulation is linked to dialysis-related amyloidosis."),
    ("Auto-substitution", "A machine feature that adjusts the substitution rate automatically from pressure and other measurements, within unit-set limits."),
]
FLAGS = [
    "Filtration fraction limits, transmembrane pressure limits, auto-substitution behavior, substitution line connection, online priming and rinse-back, and ultrafilter change intervals are machine-specific and follow the manufacturer and unit protocol; none are quantified.",
    "Worked convection-volume arithmetic (27% of a 350 mL/min blood flow over 240 minutes) is illustrative only and expresses convective flow as a share of whole-blood flow; the text labels it as convective flow divided by blood flow, distinct from the plasma-based filtration fraction in the base section.",
    "Testing frequency for dialysate cultures and endotoxin on HDF machines is not stated; DOH and PSN requirements specific to HDF were not verified and are referred to generically.",
    "Philippine availability is described qualitatively (limited, growing, mostly urban); no statistics and no PhilHealth coverage claim were verified, so none are stated.",
    "ESHOL convection volumes are described qualitatively (designed around high-efficiency HDF) because the achieved mean volume was not verified from the abstract.",
    "Statement that CONVINCE was conducted in European centers is from the trial's funding and registration; confirm country list if a reviewer wants it stated.",
    "Statement that medium cut-off membranes have not yet been shown in a large randomized trial to change survival should be rechecked at each review.",
    "H4RT (UK) trial results were not verified as published; it is referred to only as 'additional trials'.",
    "Albumin loss in HDF is described qualitatively; no gram figures are given.",
    "fetch_refs.py globs only m??_x.py, so it will not fetch NEW_REFS from m13_x2.py; the PMIDs below must be added to refs_pubmed_raw.json (run fetch_refs with the glob widened, or move NEW_REFS) before the check passes without reference errors.",
]
NEW_REFS = {
    "convince2023": "37326323",
    "eshol2013": "23411788",
    "contrast2012": "22539829",
    "turkhdf2013": "23229932",
    "peters2016": "26492924",
    "vernooij2024": "39489903",
    "convinceqol2024": "39089577",
}
