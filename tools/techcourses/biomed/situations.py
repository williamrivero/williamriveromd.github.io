# -*- coding: utf-8 -*-
"""Real situations and field notes for the twelve Biomedical Technician modules.
Reuses the scenarios written for the original six modules (situations_legacy.py), redistributed, plus new ones."""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("bm_sit_legacy", Path(__file__).resolve().parent / "situations_legacy.py")
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
O = _m.SITUATIONS


def _s(old, *idx):
    return [O[old]["scenarios"][i] for i in idx]


SITUATIONS = {
"01": {"scenarios": _s("01", 0, 1, 2, 3), "tips": O["01"]["tips"]},
"02": {"scenarios": [
    ("Dead machine, live outlet", "At 6:15 in the morning, machine 5 shows a blank screen when you switch it on. You plug a desk lamp into the same outlet, and the lamp lights.",
     "Power reaches the wall but not the electronics. The break lies somewhere between the plug and the power supply: the cord, the inlet, a fuse, the switch, or the power supply itself.",
     "Unplug the machine. Check the cord and the inlet, then test the fuses for continuity and for the correct rating. If a fuse has blown, find out why before you replace it.",
     "Working from the wall inward, one step at a time, finds the break quickly and keeps you away from live parts."),
    ("A valve that hums but does not move", "During a bench test, a solenoid valve buzzes each time it is energized, but no fluid flows past it. The machine is due for descaling next week.",
     "The coil is receiving power, but the plunger is stuck. Scale is the usual cause.",
     "Descale and inspect the valve by the manual. Replace it if it does not free. Then ask why scale reached it.",
     "A stuck valve can mean that bypass does not work at the moment it is needed."),
    ("Board swapped, new alarms", "On Monday, after a control board is replaced with one taken from a retired machine, the unit shows alarms that nobody on the floor has seen before.",
     "The donor board carries a different software version or a different configuration.",
     "Take the machine out of service. Check the versions against the manual, and obtain the correct board or software from the manufacturer.",
     "Boards are not interchangeable just because they fit. A board that fits but does not match can make a machine behave in ways no one expects."),
 ], "tips": [
    "When you fix an electrical fault, look for water nearby.",
    "Replace a fuse with the same type and the same rating, every time.",
    "Select the meter function before you connect the probes.",
    "Write board serial numbers and software versions in the service record.",
 ]},
"03": {"scenarios": _s("02", 1, 2) + [
    ("Low water alarm on one station", "At shift start, only the machine at station 3 alarms for low water. The machines on either side of it are running normally.",
     "The supply is adequate, because the neighbors are fine. Something particular to station 3 restricts flow: a kinked hose, a half-closed outlet valve, or a plugged inlet filter.",
     "Check the hose and the wall valve, then the machine&rsquo;s inlet filter. Tell the water technician if the outlet itself is at fault.",
     "&ldquo;One machine or several?&rdquo; is the question that separates supply problems from machine problems."),
 ], "tips": [
    "Check the descaling history before you replace any heating or degassing part.",
    "Verify temperature with a reference thermometer, never by touch.",
    "A display that reads lower than the true temperature is the dangerous direction, because the dialysate is hotter than it shows.",
    "Look at the inlet hoses and filters at every visit.",
 ]},
"04": {"scenarios": _s("02", 0) + [
    ("Meter and machine disagree by a fifth", "During a calibration round, your reference meter reads about a fifth higher than the machine on the same dialysate sample.",
     "A difference that large is almost never a calibration error. The meter is probably set to no temperature compensation, or to different units.",
     "Before you touch the machine, check the meter&rsquo;s compensation setting and units against the machine&rsquo;s, and check the meter in standard solution.",
     "Adjusting a correct machine to match a mis-set meter creates the very error you were trying to prevent."),
    ("Cartridge nearly empty", "In the fourth hour of a long treatment, the bicarbonate-stage conductivity drifts slowly down and the machine alarms.",
     "A powder cartridge is running out, or channeling, so that water passes through without dissolving enough powder.",
     "Tell the nurse; the cartridge is changed by the unit&rsquo;s procedure. If the alarm recurs with fresh cartridges, check the bicarbonate pump and the cartridge holder.",
     "Not every conductivity alarm is a machine fault. Rule out the supply first."),
 ], "tips": [
    "Check your reference meter in standard solution on the day you use it.",
    "Match the reference temperature and the units before you compare readings.",
    "Never calibrate to silence an alarm.",
    "When a machine moves to another site, check its concentrate configuration.",
 ]},
"05": {"scenarios": _s("02", 3) + [
    ("More low blood pressure on one machine", "Over two weeks, nurses remark that patients on machine 2 &ldquo;always crash&rdquo; in the last hour.",
     "It may be coincidence or the mix of patients. It may also be a machine that removes more fluid than it reports.",
     "Take the report seriously. Run the tightness test and the ultrafiltration accuracy check, and tell the nurses the result either way.",
     "Clinical staff notice patterns long before any alarm does."),
    ("Air after a connector seal change", "Right after you replace a dialyzer connector seal, the machine fails its own pressure-holding test.",
     "The seal is not seated, is the wrong size, or air was left in the loop.",
     "Reseat the seal or replace it with the correct part, remove the air, and repeat the test before release.",
     "Any work inside the balanced loop is followed by a tightness test, because a tiny leak there changes how much fluid the patient loses."),
 ], "tips": [
    "Prove tightness first, then pump accuracy.",
    "Read the measuring cylinder at eye level.",
    "Ask the nurses which machines seem to leave patients heavy or light.",
    "Replace dialyzer connector seals on schedule.",
 ]},
"06": {"scenarios": _s("03", 0) + [
    ("Circuits clotting on one machine", "Over one month, nurses report more clotted dialyzers on machine 9 than on any other machine.",
     "Clinical causes are common. The heparin pump may also be delivering less than its setting, because the wrong syringe type is configured or the drive is slipping.",
     "Check the configured syringe against the syringes actually in use, and test delivery by the manual. Report the result to the nurse.",
     "A syringe pump is a medication device. Its accuracy is part of the treatment."),
    ("A pressure line that fills with blood", "Three times this week, blood has risen up to the transducer protector on the venous line of the same machine.",
     "A small leak in the internal pressure line or sensor lets air escape, so blood rises to take its place.",
     "Leak-test the line by the manual and repair it. Decontaminate if a protector was breached.",
     "Operators blamed for wetting protectors are sometimes working with a faulty machine."),
 ], "tips": [
    "Displayed blood flow is calculated, not measured. Check its inputs.",
    "After any pump work, set the occlusion and record it.",
    "Verify pressures at zero and across the range, both positive and negative.",
    "When the syringe supplier changes, check the configuration of every machine.",
 ]},
"07": {"scenarios": _s("03", 1, 2, 3), "tips": O["03"]["tips"]},
"08": {"scenarios": _s("04", 0, 3) + [
    ("The machine nobody listed", "During a Saturday audit you find a dialysis machine in the isolation room that does not appear in the inventory.",
     "It has no maintenance history, no scheduled visits, and no electrical safety record.",
     "Add it to the inventory, tell the chief technician, and treat it as overdue. It needs a full visit and a safety test before further use, as the medical director directs.",
     "Equipment outside the inventory is equipment outside the program."),
 ], "tips": O["04"]["tips"]},
"09": {"scenarios": _s("04", 1, 2) + [
    ("Standard solution left open", "On Friday you notice that the bottle of conductivity standard has stood uncapped on the bench since Monday.",
     "Water has evaporated from it, so it is now more concentrated and reads higher than its label.",
     "Discard it and open a fresh bottle. Recheck any calibration done with it.",
     "A wrong standard makes a good meter wrong, and the meter then makes every machine wrong."),
 ], "tips": [
    "Read the due date on the instrument before every use.",
    "Record the as-found value before the as-left value.",
    "Pour out standard solution; never dip a probe into the stock bottle.",
    "If a reference is found to be wrong, review every machine it touched.",
 ]},
"10": {"scenarios": _s("05", 0, 3) + [
    ("Drain hose in the puddle", "At the start of the morning shift, a machine&rsquo;s drain hose has slipped, and its end sits under the water pooled in a slow floor drain.",
     "There is no air gap, so waste water could be drawn back into the machine.",
     "Fix the hose above the drain with a visible gap, report the slow drain, and disinfect the machine before use.",
     "Backflow from a drain contaminates the fluid path with sewage organisms."),
 ], "tips": [
    "Use acid for scale and bleach for organic film, and never run one straight after the other.",
    "No residual strips, no treatment.",
    "Write the due date on every dialysis fluid filter.",
    "Check the drain air gap whenever a machine is moved.",
 ]},
"11": {"scenarios": _s("05", 1, 2) + [
    ("Breaker trips during heat disinfection", "At about ten at night, when all the machines start heat disinfection together, the circuit breaker for one row trips.",
     "The combined load of the heaters exceeds what the circuit can carry.",
     "Report it to the facility engineer. Until the circuit is corrected, stagger the start times of disinfection. Check that every machine actually completed its program.",
     "A tripped breaker means machines that were not disinfected, and wiring that is running at its limit."),
 ], "tips": [
    "Inspect before you measure.",
    "Flex the cord during the earth test.",
    "No extension leads, and no adapters.",
    "Know what the generator supplies before the power fails.",
 ]},
"12": {"scenarios": _s("06", 0, 1, 2, 3), "tips": O["06"]["tips"]},
}
