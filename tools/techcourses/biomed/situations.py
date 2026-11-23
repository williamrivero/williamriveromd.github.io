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
    ("Dead machine, live outlet", "A machine shows nothing when switched on. The outlet powers a lamp.",
     "Power is reaching the wall but not the electronics: cord, inlet, fuse, switch, or power supply.",
     "Unplug. Check the cord and inlet, then the fuses for continuity and correct rating. If a fuse has blown, find out why before replacing it.",
     "Working from the wall inward, one step at a time, finds the break quickly and safely."),
    ("A valve that hums but does not move", "A solenoid valve buzzes when energized but fluid does not flow.",
     "The coil is getting power, but the plunger is stuck, usually with scale.",
     "Descale and inspect by the manual; replace the valve if it does not free. Then ask why scale reached it.",
     "A stuck valve can mean bypass does not work when needed."),
    ("Board swapped, new alarms", "After a control board is replaced with one from a retired machine, the unit shows unfamiliar alarms.",
     "The donor board carries a different software version or configuration.",
     "Take the machine out of service, check versions against the manual, and obtain the correct board or software from the manufacturer.",
     "Boards are not interchangeable just because they fit."),
 ], "tips": [
    "When you fix an electrical fault, look for water.",
    "Same type, same rating, every time you replace a fuse.",
    "Select the meter function before you connect the probes.",
    "Record board serial numbers and software versions in the service record.",
 ]},
"03": {"scenarios": _s("02", 1, 2) + [
    ("Low water alarm on one station", "Only the machine at station 3 alarms for low water at shift start. Machines beside it are fine.",
     "The supply is adequate. Something particular to station 3 restricts flow: a kinked hose, a half-closed outlet valve, or a plugged inlet filter.",
     "Check the hose and wall valve, then the machine&rsquo;s inlet filter. Tell the water technician if the outlet itself is at fault.",
     "One machine or several is the question that sorts supply problems from machine problems."),
 ], "tips": [
    "Check descaling history before replacing any heating or degassing part.",
    "Verify temperature with a reference thermometer, not by touch.",
    "A display that reads lower than the true temperature is the dangerous direction.",
    "Look at inlet hoses and filters at every visit.",
 ]},
"04": {"scenarios": _s("02", 0) + [
    ("Meter and machine disagree by a fifth", "Your reference meter reads far higher than the machine on the same dialysate.",
     "A difference that large is almost never a calibration error. The meter is probably set to no temperature compensation, or to different units.",
     "Check the meter&rsquo;s compensation setting and units against the machine, and check it in standard solution, before touching the machine.",
     "Adjusting a correct machine to match a mis-set meter creates the error you were trying to prevent."),
    ("Cartridge nearly empty", "Late in a long treatment, the bicarbonate-stage conductivity drifts down and the machine alarms.",
     "A powder cartridge is running out, or channeling so water passes without dissolving enough.",
     "Tell the nurse; the cartridge is changed by the unit&rsquo;s procedure. If it recurs with fresh cartridges, check the bicarbonate pump and cartridge holder.",
     "Not every conductivity alarm is a machine fault; rule out the supply first."),
 ], "tips": [
    "Check your reference meter in standard solution on the day you use it.",
    "Match reference temperature and units before comparing.",
    "Never calibrate to silence an alarm.",
    "A machine that changes site gets its concentrate configuration checked.",
 ]},
"05": {"scenarios": _s("02", 3) + [
    ("More low blood pressure on one machine", "Nurses remark that patients on machine 2 &ldquo;always crash.&rdquo;",
     "It may be coincidence or patient mix, or the machine may be removing more fluid than it reports.",
     "Take it seriously. Run the tightness test and the ultrafiltration accuracy check, and tell the nurses the result either way.",
     "Clinical staff notice patterns long before an alarm does."),
    ("Air after a connector seal change", "After you replace a dialyzer connector seal, the machine fails its own pressure-holding test.",
     "The seal is not seated, is the wrong size, or air was left in the loop.",
     "Reseat or replace with the correct part, remove air, and repeat the test before release.",
     "Any work inside the balanced loop is followed by a tightness test."),
 ], "tips": [
    "Tightness first, pump accuracy second.",
    "Read the measuring cylinder at eye level.",
    "Ask nurses which machines seem to leave patients heavy or light.",
    "Replace dialyzer connector seals on schedule.",
 ]},
"06": {"scenarios": _s("03", 0) + [
    ("Circuits clotting on one machine", "Nurses report more clotted dialyzers on machine 9 than on others.",
     "Clinical causes are common, but the heparin pump may be delivering less than set: wrong syringe type configured, or the drive slipping.",
     "Check the configured syringe against the syringes in use and test delivery by the manual. Report the result to the nurse.",
     "A syringe pump is a medication device; its accuracy is part of the treatment."),
    ("A pressure line that fills with blood", "The same machine repeatedly gets blood up to the transducer protector on the venous line.",
     "A small leak in the internal pressure line or sensor lets air escape, so blood rises.",
     "Leak-test the line by the manual and repair. Decontaminate if a protector was breached.",
     "Operators blamed for wetting protectors are sometimes working with a faulty machine."),
 ], "tips": [
    "Displayed blood flow is calculated. Check its inputs.",
    "After any pump work, set and record occlusion.",
    "Verify pressures at zero and across the range, positive and negative.",
    "When the syringe supplier changes, check every machine&rsquo;s configuration.",
 ]},
"07": {"scenarios": _s("03", 1, 2, 3), "tips": O["03"]["tips"]},
"08": {"scenarios": _s("04", 0, 3) + [
    ("The machine nobody listed", "During an audit you find a dialysis machine in the isolation room that is not in the inventory.",
     "It has no maintenance history, no scheduled visits, and no electrical safety record.",
     "Add it to the inventory, tell the chief technician, and treat it as overdue: full visit and safety test before further use, as the medical director directs.",
     "Equipment outside the inventory is equipment outside the program."),
 ], "tips": O["04"]["tips"]},
"09": {"scenarios": _s("04", 1, 2) + [
    ("Standard solution left open", "The bottle of conductivity standard has been sitting uncapped on the bench all week.",
     "Evaporation has concentrated it, so it now reads higher than its label.",
     "Discard it and open a fresh bottle. Recheck any calibration done with it.",
     "A wrong standard makes a good meter wrong."),
 ], "tips": [
    "Check the due date on the instrument before every use.",
    "Record as found before as left.",
    "Pour out standard solution; never dip into the stock bottle.",
    "If a reference is found wrong, review every machine it touched.",
 ]},
"10": {"scenarios": _s("05", 0, 3) + [
    ("Drain hose in the puddle", "A machine&rsquo;s drain hose has slipped and its end sits under the water in a slow floor drain.",
     "There is no air gap, so waste water could be drawn back into the machine.",
     "Fix the hose above the drain with a visible gap, report the slow drain, and disinfect the machine before use.",
     "Backflow from a drain contaminates the fluid path with sewage organisms."),
 ], "tips": [
    "Acid for scale, bleach for organic film, never one straight after the other.",
    "No residual strips, no treatment.",
    "Write the due date on every dialysis fluid filter.",
    "Check the drain air gap whenever a machine is moved.",
 ]},
"11": {"scenarios": _s("05", 1, 2) + [
    ("Breaker trips during heat disinfection", "At night, when all machines run heat disinfection together, the circuit breaker for one row trips.",
     "The combined heater load exceeds what the circuit can carry.",
     "Report to the facility engineer. Until the circuit is corrected, stagger the disinfection start times. Check that every machine actually completed its program.",
     "A tripped breaker means machines that were not disinfected, and wiring running at its limit."),
 ], "tips": [
    "Inspect before you measure.",
    "Flex the cord during the earth test.",
    "No extension leads, no adapters.",
    "Know what the generator supplies before the power fails.",
 ]},
"12": {"scenarios": _s("06", 0, 1, 2, 3), "tips": O["06"]["tips"]},
}
