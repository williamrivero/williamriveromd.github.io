# -*- coding: utf-8 -*-
"""Interactive branching cases for Disaster Preparedness and Response (10 cases, Modules 2 to 11). Writes
data/academy-cases/dp-*.json in the apply_cases.py schema, with a "unit board" in place of the bedside monitor (strip off;
fields: time, alert, power, water, patients connected, staff, roads). Run from the repo root:
    python3 tools/techcourses/disaster/cases.py
Every decision node sits on every path (weaker choices show their consequence and rejoin). Every case has at least one
harmful choice that teaches a hard rule. Clinical content follows the module text; Signed off by Dr. Rivero, November 28, 2026.
Every name and identifier is fictional."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "academy-cases"
P = "disaster-preparedness-"
NOTE = ("Fictional unit and patients. Your unit protocol, the attending nephrologist and your local "
        "disaster authorities decide every real event.")
LBL = {"time": "Time", "alert": "Alert", "power": "Power", "water": "Water", "on": "On machines", "staff": "Staff", "roads": "Roads",
       "note": "Board note"}
ORDER = ["time", "alert", "power", "water", "on", "staff", "roads", "note"]


def ch(grade, text, feedback, nxt, then=None, board=None):
    c = {"grade": grade, "text": text, "feedback": f"<p>{feedback}</p>", "next": nxt}
    if then:
        c["then"] = f"<p>{then}</p>"
    if board:
        c["vitals"] = board
    return c


def node(short, scene, prompt, choices, board=None):
    n = {"short": short, "scene": f"<p>{scene}</p>" if scene else "", "prompt": prompt, "choices": choices}
    if board:
        n["vitals"] = board
    return n


def end(title, text, board=None):
    e = {"end": True, "title": title, "text": f"<p>{text}</p>"}
    if board:
        e["vitals"] = board
    return e


def debrief(points):
    return "<h4>What this case teaches</h4><ul>" + "".join(f"<li><b>{a}</b> {b}</li>" for a, b in points) + "</ul>"


CASES = []


def case(cid, page, title, board, intro, nodes, deb):
    CASES.append({"id": cid, "page": P + page + ".html", "title": title,
                  "decisions": sum(1 for n in nodes.values() if "choices" in n), "monitorTitle": "Unit board", "strip": False,
                  "note": NOTE, "labels": LBL, "monitorOrder": ORDER, "monitor": board, "intro": intro, "start": "n1",
                  "nodes": nodes, "debrief": deb})


# ─────────────────────────── 02 ───────────────────────────
case("dp02-pump", "02-hazards-and-dependencies", "The map that missed the pump",
     {"time": "Sat 2:00 p.m.", "alert": "None (annual review)", "power": "Main", "water": "Normal", "on": "0", "staff": "Safety nurse, 2 technicians", "roads": "Open"},
     "<p>You are the safety nurse of a 20-station unit in San Fernando, Pampanga, running the annual hazard and dependency review before typhoon season with the water treatment and biomedical technicians. The generator log shows a monthly test, each one &ldquo;passed.&rdquo;</p>",
     {"n1": node("Review", "", "How do you check the power line on the dependency map?", [
         ch("best", "Walk the panel with both technicians and run the generator under real load with the water system on.", "Testing the whole chain is the only way to see what the generator really carries. A voltage check on an unloaded generator misses dependencies. Watch the loop pressure while the generator carries the load.", "n2", board={"power": "Generator (test, under load)", "note": "Test running"}),
         ch("poor", "Accept the monthly log: it says &ldquo;passed&rdquo; every month, and the generator has never failed a test.", "The log tests the generator alone, not what it feeds. That is how this unit missed the problem.", "n2", then="The head nurse asks you to run a loaded test anyway.", board={"power": "Generator (test, under load)", "note": "Test running"}),
         ch("ok", "Ask the technicians whether everything important is on the generator circuit, and note their answer on the map.", "Asking helps, but people often assume. Walk the panel and test under load to be sure.", "n2", then="The technicians are not sure about the booster pump, so you run a loaded test.", board={"power": "Generator (test, under load)", "note": "Test running"})]),
      "n2": node("11 minutes in", "Eleven minutes into the loaded test, every machine in rinse mode alarms for low water pressure. The booster pump that feeds the reverse osmosis system is on the utility breaker, not the generator circuit.", "What do you do with this finding?", [
          ch("best", "Report it today with an interim plan and a date to rewire the pump onto the generator.", "A single point of failure that could stop every treatment is reported the day it is found, with an interim plan and an owner. Tell the unit manager and the Dialysis Clinical Head; interim plan: fill the storage tank before storms and add a manual transfer step to the outage protocol.", "n3", board={"water": "Low pressure (test)", "note": "Pump on utility only"}),
          ch("poor", "Note it for next year&rsquo;s budget meeting, when rewiring can be costed together with the other repairs.", "Typhoon season is weeks away. A known gap that stops all treatment cannot wait a year.", "n3", then="The unit manager hears about it and asks for an interim plan this week.", board={"water": "Low pressure (test)", "note": "Pump on utility only"}),
          ch("harmful", "Leave it: in a real outage the storage tank usually lasts long enough for the sessions already running.", "The tank lasted eleven minutes. Patients would be connected when the water stops, which turns an outage into an emergency take-off.", "n3", then="The Dialysis Clinical Head overrules you and orders an interim plan and rewiring.", board={"water": "Low pressure (test)", "note": "Pump on utility only"})]),
      "n3": node("The map", "The rewiring is scheduled for next month.", "How do you update the dependency map and the test?", [
          ch("best", "Draw the &ldquo;fail together&rdquo; line, mark the pump as a single point of failure, and test under load.", "The map should show what fails together, and the test should test the whole chain so the gap cannot hide again. Keep it marked until rewired; the monthly test runs under load with the water system and loop pressure checked.", "end", board={"note": "Map and test updated"}),
          ch("ok", "Update the map with the finding now, and keep the monthly test as it is until the pump is rewired.", "The map is right, but an unchanged test would miss the next gap.", "end", then="You add the loaded test to the protocol as well.", board={"note": "Map and test updated"}),
          ch("poor", "Leave the map unchanged until the rewiring is done, so it shows the system as it will be.", "Until the fix, the map must show the risk; staff plan from it.", "end", then="You update it after the head nurse asks.", board={"note": "Map and test updated"})]),
      "end": end("Before the season", "The pump is moved onto the generator circuit before typhoon season, the map shows the line, and the monthly test now runs under load. The next brownout passes without a single alarm.")},
     debrief([("Test the whole chain,", "not one machine: a generator test with no load misses what it feeds."),
              ("Report a single point of failure the day you find it,", "with an interim plan, an owner and a date."),
              ("Draw what fails together", "on the map, so the next person sees it.")]))

# ─────────────────────────── 03 ───────────────────────────
case("dp03-sunday", "03-unit-plan-and-command", "Signal No. 2 on a Sunday",
     {"time": "Sun 11:00 a.m.", "alert": "Signal No. 2 (Bulacan)", "power": "Main", "water": "Normal", "on": "0 (closed Sundays)", "staff": "19 on list", "roads": "Open, rain"},
     "<p>PAGASA has raised Tropical Cyclone Wind Signal No. 2 for Bulacan. You are the head nurse of a 16-station unit in Malolos, also acting as safety nurse. The plan says: &ldquo;Signal No. 2: activate the call-down; ask the attending nephrologist about early dialysis.&rdquo; The Monday&ndash;Wednesday&ndash;Friday group has 30 patients.</p>",
     {"n1": node("11:00 a.m.", "", "Who activates the plan?", [
         ch("best", "You are the on-call lead: activate it now, log the time, and tell the managers.", "The plan names who activates it. Logging the time starts the record and the clock. Tell the unit manager and the Dialysis Clinical Head.", "n2", board={"note": "Plan active 11:05"}),
         ch("poor", "Wait until Monday morning to see how the storm develops before activating anything.", "Signal No. 2 means gale-force winds within 24 hours. Monday morning is too late to move sessions or reach staff.", "n2", then="At 2:00 p.m. the unit manager calls and asks why nothing has started. You activate.", board={"note": "Plan active 14:00"}),
         ch("poor", "Text each staff member to decide for themselves what to do, since they know their own roads best.", "A plan with no lead is not a plan. One person activates; everyone else follows the plan.", "n2", then="Replies conflict, so you activate the plan formally.", board={"note": "Plan active 12:00"})]),
      "n2": node("Call-down", "", "In what order do you call?", [
          ch("best", "Staff first, then the 30 Monday patients, then the rest.", "Capacity is set by staff. Patients get a real answer only once you know who can come. Staff first to know who can work Monday, especially the charge nurse from the flood-prone barangay.", "n3", board={"staff": "12 can come Mon", "note": "Call-down running"}),
          ch("ok", "Monday patients first, since they are the ones at risk, and then staff once the patients are informed.", "Patients hear early, but you may promise sessions you cannot staff.", "n3", then="Two patients are told to come early before you know the shift can run; you call them back.", board={"staff": "12 can come Mon", "note": "Call-down running"}),
          ch("poor", "Post the whole call list, with addresses, in the staff and patient group chat so everyone can help call.", "The call list is personal data under the Data Privacy Act. Share it only with the callers.", "n3", then="The records officer removes the post and you split the list among three callers.", board={"staff": "12 can come Mon", "note": "Call-down running"})]),
      "n3": node("Early dialysis", "Twelve staff can work Monday. Five Monday patients live in barangays that flooded last year; two had potassium above 6 mmol/L last week.", "What do you do about early dialysis?", [
          ch("best", "Call the attending nephrologist with the flagged Monday list and ask who comes early.", "Early dialysis is the nephrologist&rsquo;s decision. Your job is to give the facts and then make the roster work. Flags: flood-prone barangays, recent high potassium, large weight gains; ask for a decision on who comes early and when.", "n4", board={"note": "Nephrologist: 9 early, Sun 4 p.m."}),
          ch("harmful", "Move all 30 patients to a shortened Sunday night session yourself, without calling the nephrologist.", "Any change to schedule or session length is the nephrologist&rsquo;s decision, and shortened sessions need a written order and the six conditions.", "n4", then="The nephrologist hears of it, stops the plan, and decides on 9 patients for early dialysis.", board={"note": "Nephrologist: 9 early, Sun 4 p.m."}),
          ch("poor", "Do nothing about early dialysis until Signal No. 3 is raised, since the track may still change.", "Signal No. 3 brings storm-force winds within 18 hours; roads may already be closing.", "n4", then="At 3:00 p.m. you call the nephrologist after all.", board={"note": "Nephrologist: 9 early, Sun 6 p.m."})]),
      "n4": node("The receiving unit", "Calling the receiving unit in the plan, you learn its contact person retired in June.", "What now?", [
          ch("best", "Call the unit&rsquo;s main line for the current contact, add a second receiving unit, record both fixes.", "A receiving unit is useful only if someone there answers and expects your patients. Confirm capacity, and write both fixes into the after-action notes.", "end", board={"note": "2 receiving units confirmed"}),
          ch("poor", "Assume the unit will still take patients if needed, since the agreement is signed and still valid.", "Without a named contact, a patient may arrive at a unit that cannot take them.", "end", then="Monday, a patient is turned away and you find the new contact then.", board={"note": "1 receiving unit confirmed"})]),
      "end": end("Sunday night", "Nine patients dialyze early on Sunday evening, staff know Monday&rsquo;s plan, and two receiving units are confirmed. The after-action notes list three fixes: deputies for every role, receiving-unit contacts checked yearly, and a call-down drill before the season.")},
     debrief([("One named person activates the plan,", "and logs the time."),
              ("Staff first, then patients due soonest.", "Protect the call list as personal data."),
              ("Early dialysis is the nephrologist&rsquo;s decision;", "the unit supplies the facts and the roster.")]))

# ─────────────────────────── 04 ───────────────────────────
case("dp04-gobag", "04-ready-patients", "Mang Ernesto&rsquo;s go-bag",
     {"time": "Thu 9:00 a.m.", "alert": "None (pre-season)", "power": "Main", "water": "Normal", "on": "14", "staff": "6", "roads": "Open"},
     "<p>Mr. Ernesto Villanueva, 67, on hemodialysis through a left forearm fistula, and his daughter Liza bring his go-bag to the pre-season check. It holds a two-year-old prescription photocopy, loose mixed pills, instant noodles, two bananas, a phone with no power bank and a note with the unit&rsquo;s landline.</p>",
     {"n1": node("The card", "", "What do you do about his emergency card?", [
         ch("best", "Fill in a new card with everything another unit needs to dialyze him; Liza photographs it.", "A receiving unit needs exactly these facts to dialyze him safely. Access type and side, dry weight, last potassium with its date, medicines, allergies, PhilHealth number, this unit and the backup unit with two phone numbers, and a family contact.", "n2", board={"note": "Card updated"}),
         ch("ok", "Write his name and the unit&rsquo;s phone number on a card for now, and complete the rest at his next session.", "Better than nothing, but a strange unit would still have to guess his access, dry weight and medicines.", "n2", then="You complete the full card before he leaves.", board={"note": "Card updated"}),
         ch("poor", "Keep the old prescription photocopy; it has most of the facts a receiving unit would ask for.", "It is two years old. His dry weight and medicines have changed.", "n2", then="Liza asks for a proper card, and you make one.", board={"note": "Card updated"})]),
      "n2": node("The food", "", "What do you say about the noodles and bananas?", [
          ch("best", "Swap them for low-potassium, low-salt foods and give him the three-day diet sheet.", "The emergency diet limits potassium, salt and fluid until the next session; the sheet gives the amounts and the team sets his fluid number. Noodles and their seasoning are very salty and bananas are high in potassium. Choose white rice, unsalted crackers and drained canned fruit, use one measured cup for drinks, and fill in his fluid allowance with him.", "n3", board={"note": "Diet sheet given; fluid allowance filled in"}),
          ch("harmful", "Keep the bananas: they help with the cramps he gets after long gaps between sessions.", "Bananas are high in potassium, which builds up dangerously between missed sessions.", "n3", then="The dietitian, passing by, explains the risk and goes through the three-day diet sheet with them.", board={"note": "Diet sheet given; fluid allowance filled in"}),
          ch("poor", "The noodles are fine if he drinks less water with them and skips half the seasoning packet.", "The salt drives thirst; limiting fluid after salty food is very hard.", "n3", then="You give him the three-day diet sheet and fill in his fluid allowance.", board={"note": "Diet sheet given; fluid allowance filled in"})]),
      "n3": node("Liza&rsquo;s question", "Liza asks: &ldquo;If the power goes out while he is on the machine, should he pull the needles out himself? Patients abroad are taught to.&rdquo;", "How do you answer?", [
          ch("best", "No: patients stay connected and wait; a nurse takes him off safely.", "That is the Academy rule. In a six-country study, fewer than half of patients identified even the first stage of self-disconnection correctly. Stay calm, keep the fistula arm still. Pulling needles under stress can cause bleeding and lose the fistula.", "end", board={"note": "Rule on the machine taught"}),
          ch("harmful", "Show her how to pull the needles and press on the sites, just in case no nurse can reach him.", "Self-disconnection is not taught; it risks bleeding, air entry and a lost access.", "end", then="The charge nurse corrects this and teaches the rule instead.", board={"note": "Rule on the machine taught"}),
          ch("ok", "Tell her to ask the nephrologist at the next visit, since the doctor decides what patients are taught.", "The rule is already clear; give it now and explain why.", "end", then="You explain the rule before they leave.", board={"note": "Rule on the machine taught"})]),
      "end": end("Ready", "Mang Ernesto leaves with a current card, a written medicine list and an agreed extra supply, the three-day diet sheet with his fluid allowance filled in, a power bank on Liza&rsquo;s list, and one rule he can say back: stay calm, stay connected, protect the arm, wait for staff.")},
     debrief([("The card carries what a stranger needs:", "access, dry weight, last potassium, medicines, allergies, units and contacts."),
              ("The emergency diet limits potassium, salt and fluid;", "the sheet gives the amounts and the team sets the fluid number."),
              ("Patients are not taught to self-disconnect.", "They stay connected and wait for staff.")]))

# ─────────────────────────── 05 ───────────────────────────
case("dp05-thursday", "05-typhoons-and-floods", "Signal No. 3 by Thursday",
     {"time": "Tue 7:00 p.m.", "alert": "Forecast: Signal No. 3 Wed night", "power": "Main", "water": "Normal", "on": "0 (shift ended)", "staff": "22 on roster", "roads": "Open"},
     "<p>You are the head nurse of a 24-station unit in Quezon City. Landfall is forecast for Thursday morning. The Tuesday&ndash;Thursday&ndash;Saturday group has 40 patients; Thursday falls on landfall. Eight staff live in Marikina and Rizal, where roads flood first.</p>",
     {"n1": node("Tuesday 7 p.m.", "", "What do you do first?", [
         ch("best", "Activate the plan and call staff first.", "Capacity comes from staff. You cannot offer Thursday patients a Wednesday slot you cannot staff. Find out who can work an added Wednesday evening shift and who can stay overnight.", "n2", board={"staff": "11 can work Wed eve", "note": "Plan active"}),
         ch("poor", "Text all 40 Thursday patients to come on Wednesday, so nobody misses a session.", "You do not yet know who can be dialyzed or staffed, and the nephrologist has not decided.", "n2", then="You stop the texts and call staff first.", board={"staff": "11 can work Wed eve", "note": "Plan active"}),
         ch("poor", "Wait for PAGASA to actually raise Signal No. 3 before changing anything.", "By then the lead time is mostly gone.", "n2", then="On Wednesday morning you start the call-down, with less time.", board={"staff": "9 can work Wed eve", "note": "Plan active (late)"})]),
      "n2": node("Who comes early", "Eleven staff can work Wednesday evening, enough for 18 chairs. Among Thursday patients: a 74-year-old woman with heart failure who gained 3.5 kg, two with potassium above 6 mmol/L last week, and three who depend on tricycles.", "How is early dialysis decided?", [
          ch("best", "Give the attending nephrologist the flagged list and the 18-chair limit, and ask for the decision.", "The nephrologist decides; the unit supplies facts and limits. Ask for the early-dialysis decision and the order.", "n3", board={"on": "Wed eve: 18 booked", "note": "Nephrologist decided"}),
          ch("harmful", "Shorten every Wednesday evening session to two hours so all 40 can fit, without asking the nephrologist.", "Shortened sessions need a written order and all six conditions, and high-risk patients like the woman with heart failure keep full sessions.", "n3", then="The nephrologist stops it and sets a roster of 18 early sessions, with receiving units for others.", board={"on": "Wed eve: 18 booked", "note": "Nephrologist decided"}),
          ch("poor", "Let patients choose: whoever calls back first gets a Wednesday slot, which is fair to everyone.", "First come is not medical need.", "n3", then="You give the list to the nephrologist, who reorders it.", board={"on": "Wed eve: 18 booked", "note": "Nephrologist decided"})]),
      "n3": node("Getting home", "", "How do you staff Wednesday evening and get everyone home?", [
          ch("best", "Van for the flood-zone staff, two staying over, an ACLS nurse on, and a last safe session time.", "Nobody is sent onto flooded roads to keep a schedule. The unit van takes the Marikina and Rizal staff; the last safe session time gets the last patient and staff home before Signal No. 3.", "n4", board={"alert": "Signal No. 3 Wed 10 p.m.", "roads": "Flooding begins", "note": "All home by 9:30 p.m."}),
          ch("harmful", "Ask the Marikina staff to come in Thursday morning during landfall for the remaining patients.", "Travel during landfall puts staff at serious risk, and the unit will be closed.", "n4", then="The unit manager cancels Thursday; the remaining patients go to the backup plan.", board={"alert": "Signal No. 3 Wed 10 p.m.", "roads": "Flooding begins", "note": "Thursday cancelled"})]),
      "n4": node("The week after", "The unit reopens Saturday. The next week, a nurse who waded through flood water to reach a patient&rsquo;s house reports fever and muscle pain.", "What do you tell her?", [
          ch("best", "Report it and see a physician today: it can be leptospirosis.", "Leptospirosis follows flood exposure; early assessment matters. Preventive treatment after exposure is a physician&rsquo;s decision. Fever and muscle pain after wading can be leptospirosis, which can damage the kidneys.", "end", board={"note": "Staff referred"}),
          ch("poor", "Take paracetamol and keep working; it is probably a cold from the rain, and the unit needs her.", "Fever after wading needs a physician&rsquo;s assessment.", "end", then="Two days later she is worse and is seen at the hospital.", board={"note": "Staff referred (late)"})]),
      "end": end("After the storm", "Eighteen patients dialyzed early, the rest were placed or dialyzed Saturday by the nephrologist&rsquo;s roster, and every staff member got home before the storm.")},
     debrief([("Staff first:", "capacity comes from the people who can safely come."),
              ("Early dialysis and any shortening are the nephrologist&rsquo;s decisions.", "The unit brings facts and limits."),
              ("Nobody travels into a storm to keep a schedule;", "fever after wading means a physician, the same day.")]))

# ─────────────────────────── 06 ───────────────────────────
case("dp06-quake", "06-earthquake-on-the-machine", "Magnitude 6.8 at 9:40 a.m.",
     {"time": "9:40 a.m.", "alert": "Strong shaking", "power": "Main (flickering)", "water": "Normal", "on": "16", "staff": "5", "roads": "Unknown"},
     "<p>You are the charge nurse of a second-floor unit in Lipa, Batangas. Sixteen patients are connected. The ground starts to shake hard; ceiling panels fall near Station 4.</p>",
     {"n1": node("Shaking", "", "What do you and the staff do during the shaking?", [
         ch("best", "Stay low beside patients, shield heads, steady access arms: &ldquo;Stay connected!&rdquo;", "Protect in place. Disconnecting or moving during shaking causes falls, bleeding and air entry. Call out &ldquo;Stay connected, cover your head!&rdquo; Nobody disconnects and nobody runs.", "n2", board={"alert": "Shaking stopped (40 s)", "note": "PHIVOLCS: M6.8"}),
         ch("harmful", "Start disconnecting the patients nearest the falling panels, so they can move away from them.", "Disconnecting with unsteady hands during shaking risks bleeding, air in a catheter and lost access.", "n2", then="A needle pulls out at Station 4; you press and clamp it as the shaking stops.", board={"alert": "Shaking stopped (40 s)", "note": "PHIVOLCS: M6.8; Stn 4 needle out"}),
         ch("poor", "Run to the exit to open the doors before the frames jam, so everyone can get out later.", "Running during shaking risks falls and leaves patients alone.", "n2", then="You fall against a cart; a nurse shields the patients near you.", board={"alert": "Shaking stopped (40 s)", "note": "PHIVOLCS: M6.8"})]),
      "n2": node("Checks", "The shaking stops. A saline pole has tipped at Station 9.", "What do you check, in what order?", [
          ch("best", "Every patient first, then machines, then the room, then count everyone.", "Patients first, then equipment, then building. Patients: conscious, breathing, needles and lines secure, no blood at connections. Room: gas, fire, cracks, exits.", "n3", board={"note": "Checks done; crack in a column"}),
          ch("ok", "Machines first, to stop the alarms so staff can hear each other and the patients.", "Alarms matter, but a dislodged needle bleeds faster than an alarm harms.", "n3", then="You switch to checking patients first.", board={"note": "Checks done; crack in a column"}),
          ch("poor", "Go and look at the walls for cracks, since the building decides whether anyone can stay.", "The building matters, but the patients come first.", "n3", then="A nurse calls you back to a bleeding access site at Station 9.", board={"note": "Checks done; crack in a column"})]),
      "n3": node("Station 12", "The patient at Station 12 is pulling at his lines, shouting to be taken off.", "What do you do?", [
          ch("best", "Hold his access arm, check the needles, and tell him calmly that staff will take him off.", "Calm, specific words prevent the most dangerous self-disconnection. Staff will take him off if the unit leaves; the team is deciding now.", "n4"),
          ch("harmful", "Let him pull his own needles out to calm him, and press on the sites for him.", "Self-disconnection risks bleeding and a lost access, and it panics other patients.", "n4", then="His venous needle comes out; you press and clamp the site."),
          ch("poor", "Take him off at once, before deciding whether the unit evacuates, so he stops panicking.", "Ending one session may be reasonable, but act on the stay-or-go decision, with the blood rule.", "n4", then="You take him off by protocol once the decision is made.")]),
      "n4": node("Stay or go", "The facilities officer confirms a new crack across a column on your floor. In the venous line at Station 4, where the panels fell, you see foam.", "What do you do?", [
          ch("best", "Evacuate with staff take-off and the blood rule; Station 4 clamped, blood not returned.", "Visible structural damage means evacuate. Blood that may contain air is never returned. At Station 4, possible air: clamp and do not return the blood. Elsewhere return if quick and safe, or clamp and disconnect; close catheter clamps before separating lines. Then the stairs.", "end", board={"on": "0", "note": "Evacuated by stairs; all counted"}),
          ch("harmful", "Return everyone&rsquo;s blood quickly, including Station 4, to save volume before the stairs.", "Returning a line with foam can push air into the patient.", "end", then="The circuit nurse stops the Station 4 return and clamps the line.", board={"on": "0", "note": "Evacuated by stairs; all counted"}),
          ch("poor", "Keep the sessions running until the building official arrives and decides about the cracks.", "With a cracked column and aftershocks expected, staying to finish the schedule risks everyone.", "end", then="An aftershock hits; the incident lead orders the take-off.", board={"on": "0", "note": "Evacuated by stairs; all counted"})]),
      "end": end("The assembly point", "All sixteen patients and five staff are counted in the parking lot. The building stays closed until a qualified engineer checks it.")},
     debrief([("During shaking, protect in place:", "patients stay connected and covered; staff stay low beside them."),
              ("After shaking, patients first,", "then machines, then the building, then a count."),
              ("The blood rule is the same everywhere:", "never return blood after air, hemolysis or a severe reaction.")]))

# ─────────────────────────── 07 ───────────────────────────
case("dp07-smoke", "07-fire-and-evacuation", "Smoke from the reprocessing room",
     {"time": "2:10 p.m.", "alert": "Smoke seen", "power": "Main", "water": "Normal", "on": "12", "staff": "6", "roads": "Open"},
     "<p>You are a nurse in a ground-floor unit in Cebu City. You smell smoke and see it coming from under the reprocessing room door. Twelve patients are connected; three use wheelchairs and one came on a stretcher. The alarm has not sounded.</p>",
     {"n1": node("2:10 p.m.", "", "What do you do first?", [
         ch("best", "Raise the alarm, close the door if safe, tell the charge nurse; someone free calls the fire bureau.", "Alarm and contain first; roles go to people who are free. A staff member without a patient calls the Bureau of Fire Protection (BFP).", "n2", board={"alert": "Fire alarm on; BFP called", "note": "Charge nurse is incident lead"}),
         ch("harmful", "Leave the patient you are with and run for the extinguisher, since a small fire is easiest to put out early.", "A staff member never leaves a connected patient alone to fetch an extinguisher.", "n2", then="Your patient&rsquo;s alarm sounds; another nurse covers. The charge nurse raises the alarm.", board={"alert": "Fire alarm on; BFP called", "note": "Charge nurse is incident lead"}),
         ch("poor", "Open the door to see how big the fire is before deciding whether to evacuate.", "Opening the door feeds the fire and lets smoke out.", "n2", then="Smoke pours out; you close it and raise the alarm.", board={"alert": "Fire alarm on; BFP called", "note": "Smoke in corridor"})]),
      "n2": node("The technician", "The technician tried an extinguisher on a small flame, but smoke keeps coming.", "What now?", [
          ch("best", "He leaves and closes the door; the lead orders evacuation and oxygen off.", "Fight only a small fire with an exit behind you; when it grows, leave and contain. The incident lead asks for oxygen not in use to be turned off.", "n3", board={"note": "Evacuation ordered"}),
          ch("poor", "He keeps fighting it with a second extinguisher, since the fire is still small and he is trained.", "A growing fire in a room with chemicals is for firefighters.", "n3", then="The smoke thickens; the incident lead orders him out and the evacuation.", board={"note": "Evacuation ordered"})]),
      "n3": node("Take-off", "", "How are patients taken off and moved?", [
          ch("best", "Staff take patients off one by one, nearest the smoke first; helpers move the rest by the sheet.", "In a fire there is rarely time to return blood. Mobility categories and helpers were set at the start of the shift. Clamp and disconnect, catheter clamps closed before separating lines, pressure on fistula sites; helpers move wheelchair and stretcher patients by the evacuation sheet.", "n4", board={"on": "0", "note": "All out to assembly point"}),
          ch("poor", "Return each patient&rsquo;s blood fully before disconnecting, so nobody leaves with a blood loss.", "Rinse-back takes minutes per patient that a fire does not give.", "n4", then="The incident lead orders clamp and disconnect for the rest.", board={"on": "0", "note": "All out to assembly point"}),
          ch("harmful", "Tell patients to disconnect themselves to save time while staff move the wheelchairs.", "Patients are not taught to self-disconnect; under stress it causes bleeding and air entry.", "n4", then="A patient bleeds from a pulled needle; a nurse presses it and takes over.", board={"on": "0", "note": "All out to assembly point"})]),
      "n4": node("Assembly point", "Across the street, the census nurse checks the list. One patient, Mrs. Dela Paz, is not checked off.", "What happens?", [
          ch("best", "Report at once to the incident lead for the firefighters; nobody re-enters.", "Firefighters search; staff stay out. The incident lead tells the firefighters where she was last seen.", "end", board={"note": "Found: left with family, recorded"}),
          ch("harmful", "Two nurses go back in to look for her quickly, since they know the unit layout.", "Re-entering a burning building risks more lives.", "end", then="The incident lead stops them at the door and tells the firefighters.", board={"note": "Found: left with family, recorded"}),
          ch("poor", "Assume she went home with her family, and call her phone once everyone is settled.", "Assumptions lose people.", "end", then="A firefighter asks for the count; you report her missing.", board={"note": "Found: left with family, recorded"})]),
      "end": end("Counted", "Mrs. Dela Paz had left with her daughter and is recorded as leaving. Everyone is accounted for. The unit stays closed until the building is cleared.")},
     debrief([("Never leave a connected patient", "to fetch an extinguisher; give that job to someone free."),
              ("In a fire, clamp and disconnect", "is usually right; patients never disconnect themselves."),
              ("A named census nurse", "counts every patient; nobody re-enters a burning building.")]))

# ─────────────────────────── 08 ───────────────────────────
case("dp08-brownout", "08-power-water-supplies", "Brownout at 4:20 p.m.",
     {"time": "5:10 p.m.", "alert": "Utility outage since 4:20", "power": "Generator", "water": "Normal", "on": "12", "staff": "5", "roads": "Open"},
     "<p>You are the charge nurse of a 15-station unit in Ormoc, Leyte. The utility power failed at 4:20 p.m. and the generator started. At 5:10 p.m. the technician reports that the promised fuel delivery has not come: the generator will run out within the hour. The utility says power will return &ldquo;tonight.&rdquo;</p>",
     {"n1": node("5:10 p.m.", "", "What do you do now?", [
         ch("best", "No new connections; end sessions while the generator runs; call for fuel and the nephrologist.", "A known end time lets you take patients off safely before the power goes. Normal rinse-back with working alarms; call the backup fuel supplier and the attending nephrologist about patients cut short.", "n2", board={"note": "Orderly take-off started"}),
         ch("poor", "Wait for the utility to restore power tonight, and keep all sessions running on the generator.", "&ldquo;Tonight&rdquo; is not a time. Waiting turns a planned take-off into a manual one.", "n2", then="At 6:05 the generator stops with patients still on.", board={"time": "6:05 p.m.", "power": "Battery only", "on": "2", "note": "Generator stopped"}),
         ch("harmful", "Connect the evening shift on schedule; the utility should be back before the fuel runs low.", "Connecting new patients on a generator about to run dry exposes them to an emergency take-off.", "n2", then="At 6:05 the generator stops with more patients connected.", board={"time": "6:05 p.m.", "power": "Battery only", "on": "4", "note": "Generator stopped"})]),
      "n2": node("6:05 p.m.", "The generator stops. Machines alarm on battery. Patients at Stations 3 and 11 are still connected.", "What do you do first?", [
          ch("best", "Walk the floor: airway, consciousness and access for every patient; then decide.", "Patients first, machines second. Uncover the needle sites; decide with the physician-on-duty.", "n3", board={"time": "6:05 p.m.", "power": "Battery only"}),
          ch("ok", "Open the take-off kits first, so the supplies are ready when the decision is made.", "Useful, but look at the patients before the equipment.", "n3", then="You walk the floor next.", board={"time": "6:06 p.m.", "power": "Battery only"}),
          ch("poor", "Go to the generator room to see what happened and whether it can be restarted.", "That is the technician&rsquo;s job; your place is with the patients.", "n3", then="A nurse calls you back to the floor.", board={"time": "6:08 p.m.", "power": "Battery only"})]),
      "n3": node("Manual return", "The battery runs down; the blood pumps stop. Both circuits at Stations 3 and 11 look sound so far.", "How is the blood returned?", [
          ch("best", "One nurse at each station cranks and watches the venous line until the clamp closes.", "Without power, the operator&rsquo;s eyes replace the air detector: one staff member per patient. Watch the venous drip chamber and line all the way.", "n4", board={"power": "None", "note": "Manual return in progress"}),
          ch("harmful", "One nurse cranks both stations in turn, checking the lines between, to free staff for the others.", "Nobody watches the venous line while the other station is cranked; air can enter unseen.", "n4", then="The charge nurse sends a second nurse to Station 11.", board={"power": "None", "note": "Manual return in progress"}),
          ch("poor", "Wait for power before returning the blood, since cranking by hand is slow and tiring.", "Standing blood clots by the minute; the chance to return it is shrinking.", "n4", then="You start the manual return a few minutes later.", board={"power": "None", "note": "Manual return in progress"})]),
      "n4": node("Station 11", "At Station 11 the crank stiffens; the dialyzer shows dark streaks and the venous pressure rises. The circuit is clotting.", "What now?", [
          ch("best", "Stop, clamp and cut: never force a clotted circuit back.", "Clotted blood is not forced back. The nephrologist decides the next session and any blood count check. Record the blood not returned and tell the attending nephrologist.", "end", board={"on": "0", "note": "Stn 11 clamped; Stn 3 returned"}),
          ch("harmful", "Crank harder to push the blood through, since the clot is probably only in the chamber.", "Forcing a clotting circuit can send clots or rupture the circuit.", "end", then="The physician-on-duty stops you; the circuit is clamped.", board={"on": "0", "note": "Stn 11 clamped; Stn 3 returned"})]),
      "end": end("6:40 p.m.", "Both patients are off. Station 3&rsquo;s blood was returned by hand; Station 11&rsquo;s was not. Times, methods and volumes are recorded, and the nephrologist has set their next sessions.")},
     debrief([("A known end time is a gift:", "take patients off in order while the power still runs."),
              ("Without power, one staff member per patient", "watches the venous line, because the air detector may not work."),
              ("Never force a clotted circuit back;", "clamp, record and tell the nephrologist.")]))

# ─────────────────────────── 09 ───────────────────────────
case("dp09-ash", "09-heat-ashfall-outbreaks", "Ash on the windshield",
     {"time": "5:30 a.m.", "alert": "Volcano alert raised (PHIVOLCS)", "power": "Main", "water": "Normal", "on": "0 (opens 6:00)", "staff": "4 of 6 arrived", "roads": "Ash, slippery"},
     "<p>You are the charge nurse of a 12-station unit in Tanauan, Batangas. Fine gray ash covers the roads and cars after an eruption. The first shift starts at 6:00 a.m. The waiting-area windows are open, and the water room draws from a rooftop tank with a loose cover.</p>",
     {"n1": node("5:30 a.m.", "", "What do you do before the first patient arrives?", [
         ch("best", "Close up, set an ash-cleaning point, cover the intakes and tank, masks ready.", "Close, cover, clean: keep ash out of the building, the air and the water. Close windows and doors; ask the building staff to cover the air intakes and secure the rooftop tank cover.", "n2", board={"note": "Building closed; ash point set"}),
         ch("ok", "Start the first patients on time, then close the windows and doors once everyone is connected.", "Every minute with open windows lets ash in.", "n2", then="You close up after the first connections.", board={"note": "Building closed late"}),
         ch("poor", "Keep the windows open for ventilation, as usual, since the unit gets warm without them.", "Ash irritates eyes and lungs and gets into equipment.", "n2", then="Ash drifts across the waiting area; you close the windows.", board={"note": "Building closed late"})]),
      "n2": node("The water", "At 6:20 a.m. the water technician reports the pre-filter pressure drop is rising fast.", "What do you do?", [
          ch("best", "Stop new starts; the technician checks and tests the water; follow the water failure steps.", "Ash may be entering the water. No new patient starts on water that may fail. Check the tank and filters, and keep to the steps until the water is released.", "n3", board={"water": "Testing; no new starts"}),
          ch("harmful", "Ask the technician to bypass the pre-filter so the pressure holds and the sessions can go on.", "Bypassing a filter lets ash and particles further into the treatment train, putting every patient on the loop at risk.", "n3", then="The technician refuses and stops new starts until the water is tested.", board={"water": "Testing; no new starts"})]),
      "n3": node("The coughing patient", "Water tests pass and are signed at 8:00 a.m. An older patient with chronic lung disease arrives coughing after waiting outside in the ash.", "What happens before he is connected?", [
          ch("best", "The physician-on-duty examines him first; he wears a mask.", "A clinical assessment comes before connection. Breathing and oxygen saturation; call the attending nephrologist if he is unwell.", "end", board={"water": "Released 8:00", "on": "11", "note": "Physician reviewed"}),
          ch("poor", "Connect him as usual; the cough will settle once he is indoors and away from the ash.", "He may need hospital care, not a routine session.", "end", then="Twenty minutes in he is breathless; the physician-on-duty examines him then.", board={"water": "Released 8:00", "on": "11", "note": "Physician reviewed (late)"})]),
      "end": end("Mid-morning", "The building is closed against ash, the water was tested and released before treatments resumed, and the coughing patient was examined first. Two staff who could not travel safely stayed home.")},
     debrief([("Close, cover, clean:", "the building, the intakes, and people at the door."),
              ("Ash in the water is a water event;", "never bypass a filter to keep pressure up."),
              ("Patients exposed to ash or heat", "are examined before connection when they are unwell.")]))

# ─────────────────────────── 10 ───────────────────────────
case("dp10-twelve", "10-keeping-everyone-dialyzed", "Twelve chairs, forty patients",
     {"time": "Day 2, 7:00 a.m.", "alert": "Post-typhoon", "power": "Generator", "water": "12 chairs' worth", "on": "0", "staff": "Enough for 12 chairs", "roads": "Partly open"},
     "<p>You are the head nurse of a 20-station unit in Tacloban, two days after a typhoon. The unit can run 12 chairs for one long shift. Forty patients are due. Two receiving units (Ormoc and Palo) can take six each tomorrow. The tracking board: 31 reached, 4 dialyzed at a hospital, 5 not reached.</p>",
     {"n1": node("7:00 a.m.", "", "How are today&rsquo;s 12 chairs filled?", [
         ch("best", "Give the attending each patient&rsquo;s key facts; the nephrologist sets the priority roster.", "Priority is a medical decision; your job is the facts. Time since last treatment, last potassium, fluid status and symptoms.", "n2", board={"note": "Roster set by nephrologist"}),
         ch("harmful", "First come, first served at the door, since everyone has waited and it is easy to explain.", "Arrival order is not medical need; the patient with a potassium of 6.9 could wait behind someone stable.", "n2", then="The physician-on-duty stops the queue and calls the nephrologist.", board={"note": "Roster set by nephrologist"}),
         ch("poor", "You choose the 12 yourself, based on who seems sickest when they arrive.", "Your observations help, but the decision belongs to the nephrologist.", "n2", then="The nephrologist reviews your list and changes three names.", board={"note": "Roster set by nephrologist"})]),
      "n2": node("Shortened sessions", "The Dialysis Clinical Head suggests shortening sessions to fit more patients today.", "What has to be true?", [
          ch("best", "All six conditions, with the high-risk patients excluded.", "Shortened sessions are a conditional option, used only when all six hold. The shortage recorded by the Dialysis Clinical Head, a written nephrologist order, an end or review date, high-risk patients (potassium 6.9, the breathless woman) excluded, potassium and fluid monitored, and a recorded return to full sessions.", "n3", board={"on": "15 (3 shortened by order)", "note": "Written order; review in 3 days"}),
          ch("harmful", "Shorten everyone by 90 minutes, including the high-potassium and breathless patients, to fit 16.", "High-risk patients keep full sessions or move first to a receiving unit.", "n3", then="The nephrologist cancels it and writes an order for three stable patients only.", board={"on": "15 (3 shortened by order)", "note": "Written order; review in 3 days"}),
          ch("poor", "Never shorten; send everyone beyond 12 home with the diet sheet and a slot tomorrow.", "Shortening is not required, but refusing every option may leave overdue patients waiting days.", "n3", then="The nephrologist decides on three shortened sessions with an order.", board={"on": "15 (3 shortened by order)", "note": "Written order; review in 3 days"})]),
      "n3": node("Receiving units", "", "How are 12 patients sent to Ormoc and Palo tomorrow?", [
          ch("best", "Confirm the accepting person by name, send a handoff for each patient, arrange transport, record it.", "A receiving unit can dialyze safely only with the facts and only if it expects the patient. The handoff: prescription, access type and side, last laboratory results with hepatitis status, medicines, allergies, dry weight; record each placement on the board.", "n4", board={"note": "12 placed with handoffs"}),
          ch("poor", "Text each unit the patients&rsquo; names and send them, since the units already know how to dialyze.", "Without a handoff, the receiving unit must guess the prescription and hepatitis status.", "n4", then="Palo calls back asking for prescriptions; you send full handoffs.", board={"note": "12 placed with handoffs"})]),
      "n4": node("Not reached", "Five patients are still not reached after 24 hours.", "What now?", [
          ch("best", "Keep them on the board and get help to find them.", "A patient not reached may be in danger. Tell the incident lead and the attending nephrologist; ask the social worker, barangay health workers and the LDRRMO to help.", "end", board={"note": "3 found; 2 still searching"}),
          ch("poor", "Mark them as &ldquo;probably dialyzed elsewhere&rdquo; and close the board.", "Assumptions lose patients.", "end", then="A week later one arrives at the hospital with severe hyperkalemia.", board={"note": "Board reopened"})]),
      "end": end("Day 3", "Fifteen patients dialyzed by the nephrologist&rsquo;s roster, twelve placed with handoffs, and three of five missing patients found; the search continues for two.")},
     debrief([("The nephrologist sets the priority roster", "from time since treatment, potassium, fluid and symptoms."),
              ("Shortened sessions need all six conditions,", "and high-risk patients are excluded."),
              ("Every placement needs a named accepting person and a handoff;", "no patient leaves the board until found.")]))

# ─────────────────────────── 11 ───────────────────────────
case("dp11-gate", "11-reopening-and-recovery", "The gate that wasn&rsquo;t signed",
     {"time": "Day 5, 7:00 a.m.", "alert": "Flood receded", "power": "Main (stable)", "water": "Tests pending", "on": "0", "staff": "Full roster", "roads": "Open"},
     "<p>You are the head nurse of a 14-station unit in Marikina, closed four days after a flood reached the water room. Four gates are signed: building, staff, supplies and cart, records. The water technician says by phone, &ldquo;Readings look fine, you can start,&rdquo; but the test results are not back. Twenty patients are waiting.</p>",
     {"n1": node("7:00 a.m.", "The owner asks you to open &ldquo;since everything else is signed.&rdquo;", "Do you open?", [
         ch("best", "No: the water gate is not signed, and a phone opinion is not a release.", "One unsigned gate keeps the unit closed. The unit stays closed until the water technician and the medical head sign.", "n2", board={"note": "Closed: water gate open"}),
         ch("harmful", "Yes: open on the technician&rsquo;s verbal OK, since the patients are overdue and the water looked clear.", "If the flooded water system is contaminated, every patient on the loop is exposed at once.", "n2", then="The medical head arrives and stops the first connection; the unit stays closed until the results are signed.", board={"note": "Closed: water gate open"})]),
      "n2": node("The waiting patients", "", "What happens for the twenty waiting patients?", [
          ch("best", "The attending reviews them by priority; the most urgent go to a receiving unit today.", "Keeping the unit closed does not mean leaving patients without a plan. With a handoff; the others get diet and medicine reminders and a slot once the water is released.", "n3", board={"note": "4 sent to receiving unit"}),
          ch("poor", "Send them all home and tell them to come back tomorrow, when the water should be released.", "Some are overdue and may not be safe to wait.", "n3", then="The nephrologist calls you and sends four to a receiving unit.", board={"note": "4 sent to receiving unit"})]),
      "n3": node("Reopening", "At 1:00 p.m. the water results pass and the release is signed. All five gates are signed.", "What do you do first on reopening?", [
          ch("best", "Build the reconciliation board for all 52 and flag those who missed three or more.", "Reconciliation shows who needs what next and measures the plan. Where each was dialyzed, sessions missed, extra session needed, laboratory tests needed; the seven flagged go to the nephrologist.", "end", board={"water": "Released 1:00 p.m.", "on": "14", "note": "Reconciliation started"}),
          ch("poor", "Resume the normal schedule; patients will tell you at their next session if they missed any.", "Patients who missed sessions need review, extra sessions or tests; waiting for them to say so misses some.", "end", then="The nephrologist asks for the reconciliation; you build it that evening.", board={"water": "Released 1:00 p.m.", "on": "14", "note": "Reconciliation started (late)"})]),
      "end": end("Reopened", "The unit opened only after all five gates were signed. The reconciliation board found seven patients who needed extra sessions and laboratory tests.")},
     debrief([("Five signed gates;", "a verbal &ldquo;it looks fine&rdquo; is not a release."),
              ("A closed unit still has a plan", "for every waiting patient, by the nephrologist&rsquo;s priority."),
              ("Reopening starts with reconciliation:", "who was dialyzed where, and who needs what next.")]))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("dp*.json"):
        old.unlink()
    for c in CASES:
        (OUT / f"{c['id']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"disaster cases: {len(CASES)} written to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
