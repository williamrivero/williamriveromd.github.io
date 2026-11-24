# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 08. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced."""

FIGS = {
    "pod08_tank": ("physician-on-duty-08-fill-line-tank.webp",
                   "A water tank with a dashed, blurred fill line labeled target weight (estimate). The water above the line is labeled "
                   "today&rsquo;s gain. A shaded band just under the line is labeled overload left from before, showing water the scale "
                   "cannot separate from the patient&rsquo;s own body.",
                   "The target weight is a painted line that nobody can see directly. Today&rsquo;s gain sits above it. Overload left "
                   "from earlier sessions can hide below it."),
    "pod08_wetdry": ("physician-on-duty-08-too-wet-too-dry.webp",
                     "Two patients side by side. The too wet patient has swollen ankles, sleeps propped on pillows, has a high blood pressure "
                     "reading, and a lung ultrasound screen with vertical bright lines. The too dry patient holds a cramping calf, feels dizzy "
                     "on standing, has a low blood pressure reading late in the session, and a shrinking urine cup.",
                     "Two ways a target weight can be wrong. Each produces its own pattern across sessions, not in a single visit."),
    "pod08_refill": ("physician-on-duty-08-plasma-refilling.webp",
                     "A capillary between the blood and the tissue space. Water is drawn from the plasma toward a dialyzer. Arrows show fluid "
                     "returning from the tissue space into the capillary, pulled by the protein in the blood. An inset shows the same capillary "
                     "with less albumin in the blood and thinner return arrows, so refilling is slower.",
                     "Plasma refilling. The machine removes water from the plasma. Protein in the blood pulls tissue fluid back in. "
                     "Low albumin and a nearly dry tissue space slow the return."),
    "pod08_lus": ("physician-on-duty-08-lung-ultrasound-b-lines.webp",
                  "An ultrasound probe on the side of the chest. Two screens. The dry lung shows horizontal repeating bright lines called "
                  "A-lines. The wet lung shows several vertical bright streaks running down from the lung surface, called B-lines. A label "
                  "reads: a measure, not a treatment.",
                  "Lung ultrasound counts B-lines, the vertical streaks that wet lung tissue produces. More B-lines mean more water in the lung."),
    "pod08_bia": ("physician-on-duty-08-bioimpedance-outline.webp",
                  "Electrodes on one hand and one foot of a patient lying flat. An enlarged view of tissue shows a low-frequency current "
                  "flowing around the cells through the extracellular water, and a high-frequency current passing through the cells as well.",
                  "Bioimpedance spectroscopy. Low-frequency current travels around cells and high-frequency current passes through them, "
                  "which lets the device estimate extracellular water."),
    "pod08_flesh": ("physician-on-duty-08-flesh-or-fluid.webp",
                    "Two outlines of the same patient standing on the same scale showing the same weight. Before illness, the outline shows "
                    "more muscle and less water. After illness, the outline shows thinner muscles, swollen ankles, and more water.",
                    "Flesh or fluid. After an illness the scale can show the same number while muscle has been replaced by water."),
    "pod08_notreach": ("physician-on-duty-08-goal-not-reachable.webp",
                       "An algorithm chart. Fluid goal, then hourly rate, then a decision box asking whether the rate is over the unit&rsquo;s "
                       "ceiling. If yes, call the attending nephrologist, who chooses among an extra session, a longer session, isolated "
                       "ultrafiltration, or a revised target. Every path ends at document.",
                       "When the goal cannot be reached safely, the physician on duty calculates, calls, and documents. The attending "
                       "nephrologist chooses the option."),
}
