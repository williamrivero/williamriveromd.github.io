# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 05 (Infection Prevention and Waste Management): deeper lessons.
Hand hygiene and protective equipment sequence, turnover shortcuts, disinfectant dilution arithmetic,
waste, sharps, spills and exposure, and hepatitis B, hepatitis C, and HIV in the unit."""

ADD = {
"extra": [
(1, "handsppe", "Hands and PPE order", "Hand hygiene and protective equipment, done in order", """
{{plain:Think of a fine powder, such as flour, on a busy kitchen counter. Touch the counter, then the rice pot, then the plates, and the powder goes wherever your hands go. Most infections in a dialysis unit travel the same way, on hands and gloves, from one surface to the next. The difference is that you cannot see the germs. The only protection is a habit: clean hands at fixed moments, every time, whether or not the hands look dirty.}}
<p>The picture has a limit. Flour shows you where you have been. Blood-borne germs leave no trail, and a hand that looks clean can carry enough to infect the next patient. That is why the moments below are fixed in advance and do not depend on what you see.</p>
{{flow:Hand hygiene moments in one treatment at one station|Before entering the station::Before you touch the patient, the chair, or the machine.|Before a clean task::Before you handle the dialyzer, lines, saline, or clean supplies for setup.|After blood or body fluid risk::After you handle used lines, the drain, the priming bucket, or anything wet from the circuit.|After touching the patient::After you help the patient sit, weigh the patient, or take a blood pressure.|After touching the station::After you silence an alarm or touch the screen, even if you did not touch the patient.|After removing gloves::Every time. Gloves have tiny holes, and hands are contaminated as gloves come off.}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Alcohol-based hand rub</th><th>Soap and water</th></tr></thead>
<tbody>
<tr><td>When</td><td>Routine moments, when hands are not visibly dirty</td><td>Hands visibly soiled or wet with blood or body fluid; after using the toilet; before eating</td></tr>
<tr><td>How</td><td>Use enough product to cover both hands. Rub the palms, backs, between the fingers, fingertips, thumbs, and wrists</td><td>Wet the hands, apply soap, rub the same areas, rinse, dry with a single-use towel, and use the towel to close the tap</td></tr>
<tr><td>How long</td><td>Until dry, about 20 seconds. If your hands are dry in 10 seconds, you used too little</td><td>Rub with soap for at least 20 seconds; the whole wash commonly takes 40 to 60 seconds</td></tr>
<tr><td>Common misses</td><td colspan="2">Thumbs, fingertips, and between the fingers. Rings, watches, and long or artificial nails shelter germs; follow your unit&rsquo;s rule on them</td></tr>
</tbody></table></div>
<p>Personal protective equipment (PPE) means the gloves, gown, mask, and eye protection that keep blood off your skin, eyes, and clothes. The order matters in both directions, but it matters most when you take it off. By then the outside of everything you wear is contaminated, and the order is designed so that your bare hands touch only the parts that stayed clean.[[cdc_dialysis]]</p>
{{flow:Putting on|Hand hygiene::First.|Gown or apron::Tie it fully.|Mask::Cover the nose and mouth; press the strip over the nose.|Eye protection::Goggles or a face shield. Ordinary eyeglasses are not enough.|Gloves::Last, pulled over the gown cuffs.}}
{{flow:Taking off|Gloves::Peel one off inside out, hold it in the gloved hand, slide a bare finger under the second cuff, and peel it over the first.|Hand hygiene::If your hands became contaminated.|Eye protection::Lift it from the strap or earpieces, not the front.|Gown::Untie it, pull it away from the body, and roll it inside out.|Mask::Handle the ties or loops only.|Hand hygiene::Always the final step.}}
{{key:Gloves are changed, not cleaned. One pair serves one task at one station. Alcohol rub on gloves, or the same gloves at two chairs, moves blood between patients.}}
"""),
(2, "shortcuts", "Turnover shortcuts", "Station turnover: common shortcuts and why they fail", """
<p>Section 2 gives the turnover sequence. Between shifts there is pressure to seat the next patient quickly, and that is when steps are cut. You will rarely see a shortcut cause harm on the day it happens, because the harm is an infection that appears weeks later in another patient. Each shortcut below looks harmless, and each removes a barrier that standard dialysis infection control guidance depends on.[[cdc_dialysis]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Common shortcut</th><th>Why it fails</th><th>Correct practice</th></tr></thead>
<tbody>
<tr><td>Starting to wipe while the patient is still in the chair</td><td>The patient, the belongings, and any bleeding site contaminate cleaned surfaces again, and the patient breathes disinfectant</td><td>Wait until the patient has left the station</td></tr>
<tr><td>Wiping and immediately drying, or wiping with a nearly dry cloth</td><td>Disinfectant kills only while the surface stays wet for the full contact time on the label</td><td>Use enough product to keep the surface visibly wet. Time it</td></tr>
<tr><td>Wiping in any order with one cloth</td><td>Soil from the dirtiest area is spread onto the cleanest</td><td>Work from clean to dirty and from top to bottom. Change cloths when soiled and between stations</td></tr>
<tr><td>Disinfecting over visible blood or soil</td><td>Soil shields germs from the disinfectant</td><td>Clean first, then disinfect</td></tr>
<tr><td>Emptying the priming bucket and putting it back</td><td>The bucket has held fluid from the circuit and has been touched by contaminated gloves</td><td>Empty, clean, and disinfect it after every patient, or replace it with a clean one</td></tr>
<tr><td>Leaving line clamps on the machine for the next patient</td><td>Clamps touch bloody lines and gloves</td><td>Clean and disinfect them after each patient, or keep them dedicated to one patient, as unit policy states</td></tr>
<tr><td>Skipping the blood pressure cuff, chair sides, and screen</td><td>These are the surfaces hands touch most</td><td>Follow the unit&rsquo;s checklist surface by surface</td></tr>
<tr><td>Placing new supplies on the station before it is released</td><td>Clean supplies become contaminated before the patient arrives</td><td>Bring supplies only after the contact time is complete and the surfaces are dry</td></tr>
<tr><td>Returning unused supplies to the clean cart</td><td>Anything that entered a station is treated as contaminated</td><td>Discard, dedicate to that patient, or disinfect, as policy states</td></tr>
</tbody></table></div>
<p>Notice that most of the failures come from two physical facts: a disinfectant needs time and wetness to work, and anything a gloved hand touched during treatment carries what was on the glove. Keep those two facts in mind and most of the correct practices follow.</p>
{{cards:High-touch surfaces that are often missed|Machine::The screen, front panel, dialyzer holder, pole, sides, and concentrate wands.|Chair::The armrests, side tables, recline lever, and footrest.|Patient equipment::The blood pressure cuff and tubing, clamps, television remote, and call bell.|Nearby::The countertop, the priming bucket, and the outside of the sharps container.}}
"""),
(2, "dilution", "Dilution arithmetic", "Diluting a disinfectant: the arithmetic", """
<p>Think of mixing a powdered juice drink at home. Too little powder and it tastes of nothing; too much and nobody can drink it. Disinfectants behave the same way, with higher stakes. Some arrive ready to use. Others are concentrates that must be diluted with water. Too weak, and the solution does not kill. Too strong, and it damages equipment and irritates skin and lungs. <strong>The dilution to use is always the one on the product label and in your unit&rsquo;s policy.</strong> This lesson teaches only the arithmetic, so that you can prepare that dilution correctly.</p>
{{formula:<strong>Ratio method.</strong> A dilution written 1:10 commonly means 1 part concentrate in 10 parts total, that is 1 part concentrate plus 9 parts water.<br>Concentrate needed = total volume wanted &divide; the ratio number<br>Example, 1,000 mL at 1:10: 1,000 &divide; 10 = 100 mL concentrate + 900 mL water<br>Example, 1,000 mL at 1:100: 1,000 &divide; 100 = 10 mL concentrate + 990 mL water}}
<p>Some labels mean 1 part plus 10 parts. The difference is small in the bottle and real on the surface. Read the label&rsquo;s own instructions, and if they are unclear, ask the nurse or supervisor before you mix.</p>
{{formula:<strong>Strength method.</strong> Concentrate needed = (strength wanted &divide; strength of the concentrate) &times; total volume wanted<br>Example: the policy calls for a 0.5 percent solution and the bottle is 5 percent. For 2,000 mL: (0.5 &divide; 5) &times; 2,000 = 200 mL concentrate + 1,800 mL water}}
<p>Check your answer the other way around. 200 mL in 2,000 mL is one tenth, and one tenth of 5 percent is 0.5 percent. Always confirm the strength printed on the bottle in your hand, because the same product is sold at different strengths.</p>
{{flow:Preparing a diluted disinfectant|Read::The label and the unit procedure. Note the dilution, contact time, and protective equipment.|Protect::Gloves and eye protection; work in a ventilated area.|Measure::Use a marked measuring container, not a guess or a bottle cap.|Mix::Water first, then add the concentrate, to reduce splashing.|Label::Product, dilution, date, time, and your initials.|Discard::When the label or policy says the solution expires. Many diluted solutions are made fresh each day.}}
{{stop:Never mix two chemical products together, and never mix bleach with an acid product. The gas released can injure staff and patients. If you are unsure what is in an unlabeled bottle, do not use it. Report it.}}
"""),
(3, "spillsharps", "Waste, sharps, spills", "Waste, sharps, blood spills, and exposure: the working detail", """
<p>Waste is sorted where it is produced, at the moment it is produced. Sorting later means someone handles contaminated items twice, and the second person is often the one who did not know what was in the bag.</p>
<div class="table-wrap"><table>
<thead><tr><th>Waste</th><th>Examples at a dialysis station</th><th>Container</th></tr></thead>
<tbody>
<tr><td>Sharps</td><td>Fistula needles, syringe needles, broken glass vials, lancets</td><td>Rigid, puncture-resistant sharps container</td></tr>
<tr><td>Infectious</td><td>Used bloodlines and dialyzers, bloody gauze, used gloves, soaked dressings</td><td>Leak-proof bag or bin in the color your facility assigns to infectious waste</td></tr>
<tr><td>General</td><td>Clean outer packaging, paper, food wrappers from outside the station</td><td>The color your facility assigns to general waste</td></tr>
<tr><td>Chemical</td><td>Leftover or expired disinfectant and concentrate, used test reagents</td><td>As the product information and unit procedure state</td></tr>
</tbody></table></div>
<p>The color code is on your unit&rsquo;s posted chart. Never assume it is the same as in your previous workplace.</p>
{{cards:Sharps container rules|Within reach::Placed at the point of use, upright and stable, so nobody walks with an exposed needle.|Straight in::The person who used the sharp drops it in at once, after activating any safety device.|No hands inside::Never push the contents down, reach in, or shake the container.|Fill line::Close and replace it at the marked line, commonly about three quarters full. An overfull container leaves needles within reach of the next hand.|Closed for good::A sealed container is never reopened, emptied, or reused.|No two-handed recapping::Needles are not recapped, bent, or passed from hand to hand.}}
{{flow:Blood spill response|Protect people::Keep others away from the spill. Tell the nurse if it came from a patient or a circuit.|Protect yourself::Gloves, and a gown and face protection if splashing is possible.|Remove sharps::Pick up broken glass or needles with tongs or a scoop, never with fingers.|Absorb::Cover the spill with disposable towels and wipe it up. Discard them as infectious waste.|Clean::Wash the area with detergent and water.|Disinfect::Apply the product and strength your unit names for blood spills, and leave it wet for the contact time.|Finish::Discard the materials and gloves, perform hand hygiene, and record or report as policy requires.}}
<p>Section 3 gives the first aid after a needlestick or splash. Three details complete it, and each one is about time or information.</p>
<div class="table-wrap"><table>
<thead><tr><th>Point</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Wash; do not squeeze the wound or apply bleach or other harsh chemicals</td><td>These do not lower the risk, and they damage tissue</td></tr>
<tr><td>Report at once, during the shift, even for a small scratch</td><td>If protective medicine is needed, it works best when started within hours, not days. The clinician decides; the delay is the only part you control</td></tr>
<tr><td>Tell the nurse the time, the device, and the station it came from</td><td>The clinician needs to know the source to judge the risk. Do not look up the patient&rsquo;s results yourself</td></tr>
</tbody></table></div>
{{key:Embarrassment and a busy shift are the usual reasons an exposure is reported late. Reporting is never a sign of carelessness. Not reporting is.}}
"""),
(4, "bloodborne", "Hep B, hep C, HIV", "Hepatitis B, hepatitis C, and HIV in the dialysis unit", """
<p>Three bloodborne viruses matter most in dialysis. They are not handled the same way, because they do not spread with the same ease. Hepatitis B virus can stay infectious on a dry surface for at least seven days, and it spreads from very small amounts of blood, often too little to see. That is why it alone requires isolation in standard guidance.[[cdc_dialysis]] The practical point is that, for hepatitis B, careful cleaning is not enough on its own. The machine, the supplies, and the staff are kept apart as well.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Hepatitis B (surface antigen positive)</th><th>Hepatitis C</th><th>HIV</th></tr></thead>
<tbody>
<tr><td>Room or area</td><td>Separate room or designated area</td><td>No isolation required</td><td>No isolation required</td></tr>
<tr><td>Machine</td><td>Dedicated machine that stays with hepatitis B patients</td><td>No dedicated machine required</td><td>No dedicated machine required</td></tr>
<tr><td>Equipment and supplies</td><td>Dedicated cuff, clamps, and supplies that do not leave the area</td><td>Routine dialysis precautions</td><td>Routine dialysis precautions</td></tr>
<tr><td>Staff assignment</td><td>Staff caring for these patients do not care for susceptible patients at the same time</td><td>Routine</td><td>Routine</td></tr>
<tr><td>Dialyzer reprocessing</td><td>Not reprocessed</td><td colspan="2">As your unit&rsquo;s policy states (Module 11)</td></tr>
<tr><td>What protects other patients</td><td>Separation plus routine precautions</td><td colspan="2">Routine precautions done fully at every station: hand hygiene, glove changes, no shared supplies, complete turnover</td></tr>
</tbody></table></div>
<p>This table reflects CDC guidance. Philippine units follow Department of Health rules and their own policies, which may be stricter than this table.[[doh2012]] Follow the assignment sheet your unit gives you, and ask the nurse if a patient&rsquo;s station does not match it.</p>
{{cards:What this means for the technician|Assignment first::Check the machine and station assignment before setup. A machine from the hepatitis B area never moves to the general floor.|Same care everywhere::A patient with no known infection may have one that has not been found yet. Routine precautions assume this.|Confidentiality::A patient&rsquo;s results are not discussed at the chair or outside the unit.|Your own protection::Hepatitis B vaccination and blood testing for staff are arranged per unit policy. Know your own vaccination status and keep your records.|New or returning patients::Station assignment waits for the nurse when a patient&rsquo;s status is not yet known.}}
"""),
],
"quiz_extra": [
("When removing protective equipment after turnover, which item comes off first?",
 ["Mask", "Eye protection", "Gloves", "Gown"], 2,
 "Gloves are the most contaminated item and are removed first; hand hygiene is always the final step."),
("You silence an alarm by touching the machine screen but do not touch the patient. Is hand hygiene needed before you go to another station?",
 ["Yes, the station&rsquo;s surfaces count as contaminated", "No, the patient was not touched", "Only if gloves were not worn", "Only at the end of the shift"], 0,
 "Hands or gloves that touched one station can carry germs to the next."),
("A surface is wiped and then dried with a towel 20 seconds later. The label contact time is 3 minutes. What is the status of the surface?",
 ["Disinfected, because it was wiped", "Disinfected, because it is dry", "Clean enough for the next patient", "Not disinfected; it must stay wet for the full contact time"], 3,
 "Disinfectant works only while the surface is wet for the time on the label."),
("Unit policy calls for a 0.5 percent solution. The bottle is 5 percent. How much concentrate makes 2,000 mL?",
 ["20 mL", "200 mL", "100 mL", "500 mL"], 1,
 "(0.5 divided by 5) times 2,000 equals 200 mL, with 1,800 mL of water."),
("The label ratio 1:100 is read as 1 part in 100 parts total. How much concentrate is needed for 1,000 mL?",
 ["1 mL", "100 mL", "10 mL", "110 mL"], 2,
 "1,000 divided by 100 is 10 mL, plus 990 mL of water."),
("According to CDC guidance, which patient requires a dedicated machine and a separate room or area?",
 ["A patient with HIV", "A patient with hepatitis C", "Every new patient permanently", "A patient who is hepatitis B surface antigen positive"], 3,
 "Hepatitis B survives on surfaces and spreads from tiny amounts of blood, so it alone requires isolation in that guidance."),
("After a needlestick you have washed the wound. Why must you report it during the same shift?",
 ["So that the needle can be found", "Because protective treatment, if needed, works best when started within hours", "Because reports are counted monthly", "It can wait until the next working day"], 1,
 "Speed of reporting is the part the exposed person controls."),
],
"skills_extra": [
("Puts on and removes gloves, gown, mask, and eye protection in the correct order and performs hand hygiene as the final step.", True),
("Calculates and prepares a diluted solution from a mock label using a marked measuring container, and labels it with product, dilution, date, time, and initials.", False),
("Responds to a simulated blood spill in the correct sequence: protect, absorb, clean, disinfect for the contact time, discard, hand hygiene.", True),
],
}
