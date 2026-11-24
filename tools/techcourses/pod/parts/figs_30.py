# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 30. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced.
The site figure "typhoon" was not reused: its wind speed bands do not match PAGASA's current five-level table
(checked November 25, 2026), so pod30_typhoon_signals replaces it for this module."""

FIGS = {
    "pod30_manual_return": ("physician-on-duty-30-manual-blood-return.webp",
                            "Three steps in a row at a dark dialysis machine. A nurse fits the hand crank to the blood pump and turns it. "
                            "Her eyes stay on the venous drip chamber and the venous line. At the end she closes the venous line clamp "
                            "as saline reaches the patient. The circuit follows the standard blood path from the arterial line through "
                            "the pump and dialyzer to the venous line.",
                            "Manual blood return without power. One nurse turns the blood pump by hand and watches the venous drip "
                            "chamber and line until the clamp is closed, because the air detector may not work."),
    "pod30_return_or_clamp": ("physician-on-duty-30-return-or-clamp.webp",
                              "Two panels side by side. Left, labeled Return the blood by hand: a sound circuit with no air and normal "
                              "dark red blood, and time to finish. Right, labeled Clamp and cut, do not return: air or foam in the venous "
                              "line, translucent wine-colored blood suggesting hemolysis, a clotted dialyzer, or an exit sign for "
                              "immediate evacuation.",
                              "Return the blood when the session ends for a cause outside the patient and the circuit is sound. Clamp "
                              "without return when there is air, possible hemolysis, a clotted circuit, or no time to stay."),
    "pod30_water_to_blood": ("physician-on-duty-30-water-to-blood.webp",
                             "One mechanism from left to right: city water enters the water room, passes the treatment train, becomes "
                             "dialysis fluid in the machine, and flows past a thin dialyzer membrane with blood on the other side. Small "
                             "icons for chloramine, fluoride, and microcystin, a toxin from blue-green algae, cross the membrane into "
                             "the blood when a stage fails.",
                             "Why a fault in the water reaches the blood. Small dissolved substances in the dialysis fluid cross the "
                             "membrane directly, without the gut or a working kidney in the way."),
    "pod30_typhoon_signals": ("physician-on-duty-30-typhoon-signals.webp",
                              "A reference card of the five Philippine Atmospheric, Geophysical and Astronomical Services Administration "
                              "(PAGASA) tropical cyclone wind signals, from Signal No. 1 to Signal No. 5, with the wind speed range and "
                              "lead time from PAGASA&rsquo;s current table. Beside Signal No. 4 and No. 5, icons show loss of power, "
                              "telecommunications, and potable water, and a dialysis unit&rsquo;s matching step: confirm the storm plan, "
                              "move sessions earlier as the nephrologist decides, and check the generator fuel and water storage.",
                              "PAGASA&rsquo;s five wind signals. At Signal No. 4 and No. 5, loss of power, telecommunications, and "
                              "potable water is expected, which are the three things a dialysis unit runs on."),
    "pod30_grab_bag": ("physician-on-duty-30-grab-bag.webp",
                       "A reference card showing an open grab bag by a unit exit and its contents laid out and labeled: the patient "
                       "list and tracking sheet, emergency contacts and the partner-unit list, line clamps and disconnection kits, "
                       "a medication and dialysis summary for each patient, a flashlight, and a power bank. A smaller panel shows "
                       "a patient&rsquo;s own emergency packet with a medicine list and the unit&rsquo;s phone numbers.",
                       "The unit grab bag and the patient&rsquo;s emergency packet. The dialysis summary lets another unit treat a "
                       "displaced patient without guessing the prescription."),
    "pod30_evacuation_routes": ("physician-on-duty-30-evacuation-routes.webp",
                                "A simple top-down floor plan of a generic dialysis unit, read from top to bottom: treatment chairs, "
                                "two marked exits, the route arrows, and an outdoor assembly point. Numbered steps beside it show the "
                                "order: disconnect as the plan directs, move patients who cannot walk first with their assigned "
                                "staff, take the grab bag, and count everyone at the assembly point.",
                                "Know the exits and the assembly point before your first shift. Patients who cannot walk are moved "
                                "first by staff assigned in advance, and everyone is counted at the assembly point."),
}
