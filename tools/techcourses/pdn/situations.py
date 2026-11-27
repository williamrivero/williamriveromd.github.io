# -*- coding: utf-8 -*-
"""Real situations and field notes for the Pediatric Dialysis Nurse track.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters). All are fictional composites."""

def S(*rows, tips=()):
    return {"scenarios": list(rows), "tips": list(tips)}

SITUATIONS = {
"01": S(
    ("&ldquo;You&rsquo;re a dialysis nurse, right?&rdquo;", "You are asked to take a pediatric patient because you know adult hemodialysis.", "Staffing pressure treats adult authorization as pediatric authorization.", "State your authorization in one sentence, offer what you can safely do, and ask for the nephrologist and charge nurse to decide.", "Authorization is by modality, device and age band."),
    ("The unknown number", "At 2 a.m. the on-call number on the wall rings out.", "Escalation contacts were never tested.", "Use the backup route in the learning agreement; report the dead number in the morning.", "An escalation plan that fails at night is no plan."),
    ("The proud preceptor", "Your preceptor says, &ldquo;Just watch me for a week, then you&rsquo;re on your own.&rdquo;", "Supervision levels were never written.", "Ask to write the learning agreement together, with tasks, supervision levels and a review date.", "Unwritten limits are not protected."),
    tips=["Carry a card with your authorization and escalation numbers.", "Start with older, stable children."]),
"02": S(
    ("The thirsty toddler", "A relative tells a mother to restrict water in a polyuric child.", "Adult fluid rules applied to a salt-losing child.", "Advise against restriction and ask the nephrologist to counsel the family.", "Polyuric children dehydrate fast."),
    ("&ldquo;Which is better?&rdquo;", "A father asks you to choose between PD and hemodialysis.", "He wants reassurance and practical facts.", "Describe what each asks of the family; pass the choice to the nephrologist and family.", "Informed families choose sustainable modalities."),
    ("The promised benefit", "A neighbor told a family that pediatric APD is free everywhere.", "Information about a pilot has spread without its dates.", "Explain that the pilot status after July 31, 2026 must be confirmed with PhilHealth.", "Unconfirmed promises break trust."),
    tips=["Ask the cause of kidney failure at the first meeting.", "Write height in the chart every visit; eGFR needs it."]),
"03": S(
    ("The silent teenager", "A 14-year-old answers only &ldquo;okay&rdquo; while her mother talks.", "No private time has been offered.", "Explain confidentiality and its limits, then ask the mother to step out for a few minutes.", "Adolescents speak when they are given space."),
    ("The false choice", "A colleague asks a 5-year-old, &ldquo;Do you want your treatment now?&rdquo; and he says no.", "A choice was offered that could not be honored.", "Reframe with a real choice: &ldquo;Do you want to sit on Mama&rsquo;s lap or the chair?&rdquo;", "False choices create refusals."),
    ("The bruise story", "A child&rsquo;s explanation of a burn mark changes each time.", "Possible non-accidental injury.", "Record exactly what you saw and heard and report through the child protection pathway.", "Investigation belongs to trained staff."),
    tips=["Kneel to eye level.", "Never promise a child to keep a secret."]),
"04": S(
    ("The heavier Monday", "A child weighs 0.5 kg more than expected on a new scale.", "Different scale or clothing, not necessarily fluid.", "Reweigh on the usual scale with standard clothing and record PD fill state.", "Only comparable weights guide removal."),
    ("The tiny cuff", "A blood pressure of 150/95 in a 7-year-old with an adult small cuff on a thin arm.", "Wrong cuff size or technique.", "Measure arm circumference, choose the right cuff, repeat calm, compare with percentiles.", "False highs lead to unnecessary fluid removal."),
    ("The copied decimal", "A transcribed rate reads 30 mL/kg/h instead of 3.", "Copying error.", "Stop, calculate from the source order, independent check, confirm with prescriber.", "Ten-fold errors start in copying."),
    tips=["Write units at every step.", "Count flushes as intake."]),
"05": S(
    ("The quick wipe", "A colleague wipes a catheter hub for two seconds and connects while wet.", "Scrub-the-hub time and drying skipped.", "Remind kindly, model the full scrub and dry, and include it in audit.", "Friction and drying time do the work."),
    ("Diaper over the exit site", "An infant&rsquo;s PD exit-site dressing is wet with urine.", "Exit site near the diaper line or dressing poorly placed.", "Change the dressing per protocol, reposition the diaper, report for a plan.", "Diapers are an infection route."),
    ("Mupirocin from home", "A parent brings mupirocin to use on an HD catheter exit site.", "Well-meant improvisation.", "Explain that the unit follows its written protocol; refer to the nephrologist.", "An observational study linked it with more infection."),
    tips=["Audit one bundle element each week.", "Teach siblings hand hygiene too."]),
"06": S(
    ("The new bottle", "A family&rsquo;s medicine has a new brand with a different concentration.", "Same mg, different mL.", "Recalculate the volume and teach the family the new amount; involve the pharmacist.", "Concentration changes cause ten-fold errors."),
    ("Before or after?", "A child&rsquo;s antibiotic is ordered after dialysis but given before at home.", "Timing not taught or not practical.", "Explain why, adjust the routine with the family, report to the prescriber.", "The dialyzer may remove the dose."),
    ("The vomited dose", "A child vomits ten minutes after a dose.", "Unclear whether to repeat.", "Record and ask the prescriber; do not repeat on your own.", "Repeats can overdose."),
    tips=["Leading zero, no trailing zero.", "Use oral syringes for oral liquids."]),
"07": S(
    ("The adult default", "A cycler template from an adult patient is loaded for a child.", "Template shortcut.", "Clear it; program from the child&rsquo;s order and check with a second person.", "Adult fills can overfill a child."),
    ("The grunting infant", "An infant grunts and refuses to lie flat after each fill.", "Possible high intraperitoneal pressure.", "Report to the nephrologist with fill volume in mL/m&sup2; and the symptoms.", "High pressure causes breathing problems and leaks."),
    ("The old height", "BSA was calculated from a height measured a year ago.", "Growth changes BSA.", "Remeasure and recalculate; report if the fill per m&sup2; has changed.", "Scaling depends on current size."),
    tips=["Convert every fill to mL/m&sup2;.", "Ask families what the bag looks like at home."]),
"08": S(
    ("The red ring", "A faint red ring around the exit site, no discharge.", "Early irritation or early infection.", "Score it, record it, increase observation, report per protocol.", "Trends catch infections early."),
    ("Pus at the exit", "A drop of yellow discharge at the exit site.", "Exit-site infection by definition.", "Call the PD team the same day; swab per protocol.", "Purulent discharge alone is diagnostic."),
    ("Constipated and slow", "A child drains slowly after several days without stool.", "Constipation compressing the catheter tip.", "Check external causes, report for a bowel plan.", "Most outflow problems are simple."),
    tips=["Secure the catheter so play cannot tug it.", "Look before you clean."]),
"09": S(
    ("Talking while connecting", "A caregiver chats while the transfer set is uncapped.", "Droplet and touch contamination risk.", "Teach a silent connection rule.", "Connection is the riskiest moment."),
    ("The cap on the floor", "A cap falls with the line open.", "Wet contamination.", "Clamp, cover, call for transfer-set change and prophylaxis decision.", "Prompt action prevents peritonitis."),
    ("The microwave", "A family warms bags in a microwave.", "Convenience.", "Teach the approved dry warming method and explain why.", "Uneven heating burns and damages bags."),
    tips=["Weigh small drains.", "Thank caregivers who report mistakes."]),
"10": S(
    ("Alarm at 2 a.m.", "Low-drain alarms every night at the same time.", "Position or constipation.", "Download the log, address bowels and position, report the pattern.", "Patterns have causes."),
    ("The bypass habit", "A father bypasses every drain alarm.", "Alarm fatigue.", "Retrain on what a bypass leaves behind; report for setting review.", "Retained fluid raises pressure."),
    ("Power cut", "A brownout stops the cycler mid-night.", "Common in typhoon season.", "Follow the home plan; manual exchange if trained and ordered; call the hotline.", "Plans made in advance prevent missed therapy."),
    tips=["Two people check every program change.", "Read delivered therapy, not prescribed."]),
"11": S(
    ("Clear but painful", "A child on APD with a dry day has abdominal pain and fever, clear fluid.", "Short dwell may hide a high cell count.", "Call the team; sample after a 2-hour dwell per protocol.", "Clear fluid does not exclude peritonitis."),
    ("Waiting for the culture", "A colleague wants to wait for culture results before antibiotics.", "Misunderstanding of timing.", "Antibiotics as ordered once specimens are taken.", "Delays worsen outcomes."),
    ("Too many culture-negatives", "Half the program&rsquo;s episodes grew nothing.", "Sampling or lab technique problems.", "Review sample collection and culture methods with the lab.", "The benchmark is under 15%."),
    tips=["Keep the cloudy bag closed and upright.", "Time the first antibiotic dose."]),
"12": S(
    ("Blood from the fistula arm", "A ward nurse starts an IV in the arm marked for a fistula.", "Protection not communicated.", "Stop it, explain, mark the arm, add a chart alert.", "Damaged veins limit future access."),
    ("Swollen face", "A child with a central line has facial swelling.", "Possible central vein narrowing or thrombosis.", "Report urgently.", "Central veins are hard to replace."),
    ("Fast blood flow", "An order&rsquo;s blood flow equals 12 mL/min/kg.", "Possible error.", "Convert, compare with the range, confirm with the prescriber.", "Unusual numbers are questions."),
    tips=["Convert QB to mL/min/kg.", "Every bundle step, every time."]),
"13": S(
    ("The big circuit", "Only adult lines are available for a 12-kg child.", "Circuit share far above 10%.", "Calculate the share and call the nephrologist for the priming plan.", "Large circuits drop blood pressure at the start."),
    ("Cold baby", "An infant&rsquo;s temperature falls during treatment.", "Heat loss through the circuit.", "Use the warming plan and machine temperature control; report.", "Hypothermia is a pediatric risk."),
    ("Missing water check", "Today&rsquo;s water log is blank.", "Check not done.", "Do not start; report to the charge nurse and technician.", "A missing check is a failed check."),
    tips=["Say the circuit share out loud.", "Record every milliliter drawn from an infant."]),
"14": S(
    ("Headache in the first hour", "A child&rsquo;s first session; headache and vomiting at 60 minutes.", "Possible disequilibrium.", "Slow or stop per protocol, call, monitor neurology.", "Gentle starts prevent seizures."),
    ("Yawning", "A child yawns and goes quiet late in the session.", "Falling blood volume.", "Lay flat, reduce ultrafiltration per protocol, call.", "Behavior changes before blood pressure."),
    ("Different post-weight", "Post-weight taken in clothes and shoes.", "Conditions mismatched.", "Reweigh to match pre-weight conditions.", "Wrong weights mislead the next session."),
    tips=["Watch the heart rate trend.", "Use a structured handoff."]),
"15": S(
    ("Missed session, slow pulse", "Teen after a missed session with weakness and peaked T waves.", "Hyperkalemia.", "Monitor, call the team, bring the cart, do not wait for lab.", "Arrhythmias can be sudden."),
    ("Foam in the line", "Air detector alarm with foam.", "Air in the circuit.", "Stop the pump, clamp, call, position as trained.", "Air embolism is preventable and treatable early."),
    ("The empty cart", "The pediatric cart lacks small masks.", "Checks skipped.", "Restock and report; log daily checks.", "Preparation decides outcome."),
    tips=["Know your role before the emergency.", "Hand over dialysis details."]),
"16": S(
    ("Missing flushes", "A PICU balance omits drug flushes.", "Hidden intake.", "Add all flushes and diluents; recalculate %FO.", "Accurate counts guide decisions."),
    ("Ward new to PD", "Ward nurses ask how to do an acute exchange.", "Unfamiliar technique.", "Teach the closed Y system, write a bedside guide, agree call thresholds.", "Communication keeps acute PD safe."),
    ("Asked to run CKRT", "You are asked to run a pediatric CKRT circuit.", "Beyond this track&rsquo;s scope.", "Decline and escalate to the PICU team.", "CKRT needs separate training."),
    tips=["Measure urine hourly in AKI.", "Use admission weight for %FO."]),
"17": S(
    ("Same trousers", "A child&rsquo;s height has not changed in a year.", "Growth failure.", "Confirm measurement, plot, report with velocity.", "Height lost is hard to regain."),
    ("Binders at bedtime", "A child takes phosphate binders at night.", "Misunderstood timing.", "Teach to take with meals; tell the dietitian.", "Binders need food to work."),
    ("Blocked tube", "A gastrostomy tube blocks repeatedly.", "Feeds being missed.", "Check flushing technique and report.", "Missed feeds stall growth."),
    tips=["Plot every measurement.", "Ask what was eaten, not only what was prescribed."]),
"18": S(
    ("Hours done, skill not", "A caregiver completed training days but contaminates in return demonstration.", "Time counted instead of skill.", "Withhold readiness, practice the step, reassess.", "Readiness is shown."),
    ("The substitute aunt", "An aunt starts doing exchanges when the mother travels.", "Untrained caregiver.", "Train and verify the aunt before independent exchanges.", "A new caregiver is a retraining trigger."),
    ("Supplies on the floor", "PD boxes stored on the floor in a flood-prone house.", "No disaster plan.", "Move supplies above flood level; write the plan.", "Floods destroy supplies."),
    tips=["Train two caregivers.", "Use picture cards for low literacy."]),
"19": S(
    ("Skipping for prom", "A teen misses sessions around school events.", "Social priorities.", "Negotiate schedules and goals with the teen.", "Partnership beats lecture."),
    ("&ldquo;What&rsquo;s the point?&rdquo;", "A teen says nothing will ever change.", "Possible depression or hopelessness.", "Ask directly and calmly about self-harm; involve the team per protocol.", "Early support can save a life."),
    ("Transfer on birthday", "A patient is transferred to adult care on turning 18 without preparation.", "Transfer without transition.", "Advocate for a planned transition with a summary and confirmed first visit.", "Poor transitions risk graft loss."),
    tips=["Give private time at every visit.", "Confirm the first adult appointment."]),
"20": S(
    ("Old circular", "A form cites a superseded PhilHealth circular.", "Rules changed.", "Check the current issuance and date; update with the liaison.", "Outdated rules cause denied claims."),
    ("Perfect records", "Every session record matches the order exactly.", "Copy-forward documentation.", "Audit against machine data and correct practice.", "Records must show delivered care."),
    ("Ranking nurses", "A manager ranks nurses by infection rates.", "Small numbers misused.", "Present rates with denominators, case mix and causes.", "Blame hides problems."),
    tips=["Save the date you checked each rule.", "Use run charts, not single years."]),
}
