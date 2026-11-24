# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 18. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced."""

FIGS = {
    "pod18_weekly": ("physician-on-duty-18-potassium-weekly-peaks.webp",
                     "A line graph of blood potassium across one week of Monday, Wednesday, and Friday dialysis. The line climbs between sessions, "
                     "drops steeply during each session, rises a little in the hours after each session, and reaches its highest point on Monday "
                     "morning after the two-day weekend gap.",
                     "Potassium climbs between sessions and falls during each one. The highest value of the week comes before the first "
                     "session after the long gap, and a partial rebound follows every session."),
    "pod18_ssr": ("physician-on-duty-18-stabilize-shift-remove.webp",
                  "Three panels. First, a heart muscle cell membrane with calcium raising the threshold at which the cell fires. Second, a body cell "
                  "with its sodium-potassium pump driven by insulin and by a beta-agonist inhaler, moving potassium from the blood into the cell. "
                  "Third, a dialyzer removing potassium from the blood into the dialysis fluid. Labels only, no doses.",
                  "Stabilize, shift, remove. Calcium protects the heart muscle without lowering potassium. Insulin and beta-agonists move "
                  "potassium into cells for a few hours. Only dialysis, or a binder over days, takes potassium out of the body."),
    "pod18_gradient": ("physician-on-duty-18-gradient.webp",
                       "Two pairs of bars. At the start of the session, a tall bar for blood potassium stands beside a short bar for dialysis fluid "
                       "potassium, with a wide gap between them. At mid-session the blood bar is shorter and the gap between the two bars has narrowed.",
                       "The gap between blood and dialysis fluid potassium drives removal. It is widest at the start, so removal is fastest early "
                       "and slows as the session goes on."),
    "pod18_sugar": ("physician-on-duty-18-why-sugar-falls.webp",
                    "A diagram of blood passing through a dialyzer. Glucose molecules cross the membrane into dialysis fluid that holds little or no "
                    "glucose. Insulin molecules stay in the blood because the failed kidney does not clear them, and a small failed kidney sends "
                    "out little new glucose.",
                    "Why sugar falls during dialysis: glucose leaves into the dialysis fluid, insulin lingers because the kidney no longer "
                    "clears it, and the failed kidney makes little new glucose."),
    "pod18_clock": ("physician-on-duty-18-stroke-clock.webp",
                    "Three small panels showing a drooping face, one arm drifting down, and garbled speech, next to a clock face labeled last known "
                    "well and a heparin syringe labeled with the time it was given.",
                    "Face, arm, speech, and two times. The stroke clock starts when the patient was last seen normal. The heparin time tells "
                    "the stroke team what is still in the blood."),
}
