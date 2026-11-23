# -*- coding: utf-8 -*-
"""Real situations and field notes for the twelve Water Treatment modules.
Reuses the scenarios written for the original six modules (situations_legacy.py), redistributed, plus new ones."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("wt_sit_legacy", Path(__file__).resolve().parent / "situations_legacy.py")
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
O = _m.SITUATIONS


def _s(old, *idx):
    return [O[old]["scenarios"][i] for i in idx]


SITUATIONS = {
"01": {"scenarios": _s("01", 0, 1, 2, 3), "tips": O["01"]["tips"]},
"02": {"scenarios": [
    ("Four new stations", "Management adds four dialysis stations. Nothing in the water room is changed.",
     "Peak demand has risen by a third. The reverse osmosis unit may keep up, but water now passes through the carbon faster.",
     "Ask for the carbon contact time and softener capacity to be recalculated at the new peak flow, and report the result to the medical director.",
     "A system can fail its design quietly: the first sign may be chlorine breakthrough months later."),
    ("A valve nobody can name", "You find an unlabeled valve on a side branch near the softener. Nobody knows what it does.",
     "It may be an old bypass or a drain. In the wrong position it could let untreated water past a stage.",
     "Do not operate it. Trace the pipe in both directions, mark it on the drawing, tag it, and ask the supplier to confirm its purpose.",
     "Unknown valves are how bypasses get left open."),
    ("The drawing does not match", "The system drawing shows one carbon tank. Two are installed.",
     "The system was modified and the drawing was never updated.",
     "Mark up the drawing by hand with the date and your name, and ask for a corrected version.",
     "In an emergency, people follow the drawing. A wrong drawing sends them the wrong way."),
 ] + _s("06", 0), "tips": [
    "Know which source you are on today, and who tells you when it changes.",
    "Tag every valve with a number that matches the drawing.",
    "Bypass valves on carbon and reverse osmosis stay closed and tagged during treatment.",
    "Keep the design-stage feed water report; it is your reference for every later comparison.",
 ]},
"03": {"scenarios": _s("02", 0, 1, 2) + [
    ("Backwash at ten in the morning", "The sediment filter starts to backwash mid-shift and machines alarm for low water pressure.",
     "The timer has drifted or was reset after a power cut.",
     "Tell the charge nurse why the pressure dropped, let the cycle finish or stop it by procedure, and correct the timer.",
     "Every automatic valve in the water room has a clock, and every clock is wrong after a power interruption."),
 ], "tips": O["02"]["tips"]},
"04": {"scenarios": _s("02", 3) + _s("04", 0, 1) + [
    ("The utility changes disinfectant", "A notice in the newspaper says the water district will switch from chlorine to chloramine next month.",
     "Chloramine is harder to remove and needs the full carbon contact time. Carbon that coped with chlorine may not cope with chloramine.",
     "Give the notice to the medical director and the system supplier now. Ask whether the carbon type and contact time are adequate, and plan more frequent testing through the changeover.",
     "Chloramine changeovers are a classic cause of patient injury in dialysis units."),
 ], "tips": [
    "Total chlorine, every time. Never free chlorine.",
    "Test after the worker tank first; if anything shows, test after the polisher at once.",
    "Once a week, prove the kit reads positive on feed water.",
    "Never leave the carbon bypass open, and never accept regenerated carbon.",
 ]},
"05": {"scenarios": _s("03", 0, 1, 3) + [
    ("Low flow on a cold morning", "Product flow is a tenth lower than yesterday. Feed water temperature has dropped four degrees overnight.",
     "Cold water passes through the membrane more slowly. This fall is about what the temperature change predicts.",
     "Record both readings and the temperature. If flow recovers as the water warms, no fault exists; if it does not, report.",
     "Checking temperature first prevents a needless service call and teaches you your system&rsquo;s normal behavior."),
 ], "tips": O["03"]["tips"]},
"06": {"scenarios": _s("03", 2) + _s("05", 3) + [
    ("The loop is switched off at night", "To save electricity, the guard switches off the loop pump every evening.",
     "Water stands still in the loop for ten hours a night, which is ideal for biofilm.",
     "Report it. Explain that continuous circulation is a safety feature, and ask that the pump be left on or the system be set to flush periodically.",
     "Small savings on electricity can cost a loop replacement."),
    ("A lamp that glows", "The ultraviolet lamp is lit, but its hour counter shows it is far past the maker&rsquo;s replacement hours.",
     "The lamp&rsquo;s output has probably fallen below an effective level even though it still glows.",
     "Replace it by procedure, clean the sleeve, reset the hours, and record it.",
     "A weak lamp gives false confidence while bacteria pass."),
 ], "tips": [
    "Keep the loop running day and night.",
    "Unused outlets are disconnected, flushed, and still included in disinfection.",
    "Write the installation date on every lamp, filter, and hose.",
    "If the loop is clean and the machines are not, look at the hoses.",
 ]},
"07": {"scenarios": [
    ("Conductivity alarms after the new batch", "Ten minutes after a fresh bicarbonate batch is put on line, machines across the unit alarm for low conductivity.",
     "The batch is probably too weak: too much water or too little powder.",
     "Take the batch off line, tell the charge nurse the likely cause, verify the batch, and discard it if out of range. Prepare a new one.",
     "A shared supply error reaches every station at once."),
    ("No label on the jug", "A full container of clear liquid sits in the mixing area with no label.",
     "It could be bicarbonate, acid, disinfectant, or water. Nobody can know.",
     "Do not use it and do not smell or taste it. Quarantine it and discard by procedure.",
     "Unlabeled containers are how disinfectant ends up in a concentrate line."),
    ("Slime in the mixing tank", "When the bicarbonate tank is emptied, the walls feel slippery.",
     "Biofilm has formed. The cleaning frequency is not keeping up.",
     "Report it, clean and disinfect the tank and lines by procedure, and review the schedule. Ask for dialysis fluid cultures from the machines.",
     "Contaminated bicarbonate bypasses every barrier in the water room."),
    ("A forced connector", "An acid outlet connector has been filed down so that a different hose will fit.",
     "Someone defeated the feature that prevents acid and bicarbonate from being swapped.",
     "Remove it from use, report it, and have the correct connector fitted.",
     "Connector shapes are a safety system, not an inconvenience."),
 ], "tips": [
    "Read the whole label: type, formula, proportioning system, lot, expiry.",
    "Label every batch when you mix it, including the discard time.",
    "Never top up old bicarbonate with new.",
    "Store look-alike acid formulas on separate shelves.",
 ]},
"08": {"scenarios": _s("04", 2, 3) + [
    ("Checks done after the shift started", "The log shows the chlorine test timed at 06:40. The first patient was connected at 06:15.",
     "Treatment began on water that had not been released.",
     "Report it as an incident. Agree with the charge nurse a fixed rule: no connection until the technician has said &ldquo;released.&rdquo;",
     "A test done after the fact protects nobody."),
    ("A gauge with a fogged face", "One pressure gauge has condensation inside and its needle no longer moves smoothly.",
     "The gauge is failing. Its readings cannot be trusted.",
     "Note it in the log, report it for replacement, and do not record its reading as valid.",
     "A wrong reading written neatly is worse than a blank with a reason."),
 ], "tips": O["04"]["tips"]},
"09": {"scenarios": _s("05", 0, 1) + [
    ("The laboratory used the wrong method", "The report shows &ldquo;no growth at 48 hours, 37 &deg;C.&rdquo;",
     "This is a clinical method. Water bacteria may not have had time or the right conditions to grow.",
     "Tell the medical director the result may be falsely reassuring, and arrange with the laboratory for the dialysis water method.",
     "A string of perfect results from the wrong method hides a real problem."),
    ("A report nobody signed", "Filing last month&rsquo;s papers, you find a chemical analysis showing aluminum above its limit. It has no reviewer&rsquo;s signature.",
     "The result was never acted on.",
     "Take it to the medical director today, with the reverse osmosis rejection trend for that period.",
     "Laboratory results are only useful when someone reads them."),
 ], "tips": O["05"]["tips"]},
"10": {"scenarios": _s("05", 2) + _s("06", 3) + [
    ("Residual at one outlet", "After rinsing, every outlet tests negative except the one at the isolation room, which stays faintly positive.",
     "That branch is longer or has less flow, so disinfectant is still washing out.",
     "Keep flushing that outlet and retest until negative. Do not release the system while any outlet is positive. Report the branch as a possible dead leg.",
     "One missed outlet is one patient exposed to disinfectant."),
    ("Disinfection postponed again", "The monthly disinfection has been put off twice because the unit ran extra shifts.",
     "Counts are probably climbing, and biofilm is maturing.",
     "Report the overdue status in writing and ask for a fixed slot. Bring culture sampling forward.",
     "Disinfection that waits for a quiet day never happens."),
 ], "tips": [
    "Disinfect on schedule, before counts rise.",
    "Check the strength on the stock container every time.",
    "High-range strip to prove it arrived; residual strip to prove it has gone.",
    "Never mix bleach and acid products.",
 ]},
"11": {"scenarios": [
    ("The wrong cartridge", "The store sends a cartridge that fits the housing but is rated coarser than the one specified.",
     "It will pass finer particles that the membrane then has to cope with.",
     "Do not fit it. Obtain the specified part.",
     "A part that fits is not necessarily the right part."),
    ("Preservative taste", "After a membrane change, product conductivity is high for the first hour.",
     "New membranes are shipped in a preservative that must be flushed out.",
     "Continue flushing to drain by the supplier&rsquo;s method until readings are normal, then record the new baseline.",
     "Preservative must not reach patients, and the first readings are not a true baseline."),
    ("Service on a treatment day", "A supplier arrives unannounced at 09:00 to change the fine filter while patients are on dialysis.",
     "Opening a housing interrupts supply and risks contamination.",
     "Refer them to the charge nurse; the work is rescheduled for a time when no patient is connected.",
     "Maintenance is planned around patients, never the other way."),
    ("A meter that was never checked", "The handheld chlorine meter has been in use for two years with no record of verification.",
     "Its readings may have drifted.",
     "Verify it against a standard by the maker&rsquo;s method, or have it checked, and compare with a fresh reagent kit meanwhile.",
     "Every instrument that tests the water needs testing itself."),
 ], "tips": [
    "Note every valve position before any work starts.",
    "Flush, restore, test, record: the same four steps after every change.",
    "Stay with the service engineer and walk the system together before they leave.",
    "Write the installation date on everything you replace.",
 ]},
"12": {"scenarios": _s("06", 1, 2) + [
    ("Nobody answers", "At 05:30 chlorine is above the limit after both tanks. The charge nurse has not arrived and the medical director&rsquo;s phone is off.",
     "The hold is clear. What is missing is someone to tell.",
     "Place the hold, post a notice at the nurses&rsquo; station, and work down the escalation list until you reach a responsible person. Record each attempt with the time.",
     "A hold that nobody knows about will be bypassed by the first person who starts a machine."),
    ("The generator runs the lights only", "During a power cut the lights stay on but the reverse osmosis unit stops.",
     "The generator does not supply the water system, or its changeover failed.",
     "Tell the charge nurse immediately that there is no water production, and how much reserve there is, if any.",
     "Knowing in advance what the generator powers belongs in the contingency plan, not in the dark."),
 ], "tips": O["06"]["tips"]},
}
