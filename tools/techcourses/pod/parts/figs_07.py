# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 07. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced."""

FIGS = {
    "pod07_order": ("physician-on-duty-07-annotated-order.webp",
                    "A model hemodialysis order form with each line labeled: dialyzer, session time, blood flow rate, dialysis fluid flow rate, "
                    "dialysis fluid potassium, calcium, sodium, and bicarbonate, fluid temperature, anticoagulation, fluid removal goal, and "
                    "weekly schedule. A stamp across the form reads: illustrative values, not targets.",
                    "Every line of the order controls one part of the session. The attending nephrologist writes it. You check that the "
                    "machine matches it and that it still fits today&rsquo;s patient."),
    "pod07_kgradient": ("physician-on-duty-07-potassium-gradient.webp",
                        "Two panels of a dialyzer fiber. In the left panel, blood with normal potassium faces dialysis fluid with very little "
                        "potassium, and many potassium ions cross the membrane quickly. In the right panel, the gap is small and few ions cross. "
                        "Beside each panel, a heart muscle cell shows its electrical charge across the cell membrane, which shifts when blood "
                        "potassium falls fast.",
                        "Potassium moves down the gap between blood and dialysis fluid. A steep gap lowers blood potassium fast, and the heart "
                        "muscle&rsquo;s electrical balance shifts with it."),
    "pod07_cool": ("physician-on-duty-07-cool-dialysate.webp",
                   "Two dialysis patients side by side. On the left, warm dialysis fluid returns warm blood, skin vessels open, and the "
                   "patient looks flushed. On the right, slightly cooler fluid returns cooler blood, and the small vessels stay narrower.",
                   "Cooler dialysis fluid keeps the vessels of the skin narrower. It helps some patients hold their pressure. As a policy for "
                   "every patient in a center, it did not reduce cardiovascular events in a large trial."),
    "pod07_ktv": ("physician-on-duty-07-adequacy-cleaned.webp",
                  "A large water tank labeled V, the body water, beside a smaller stream of cleaned water labeled K times t, the dialyzer "
                  "clearance multiplied by session time. A gauge shows how many tank volumes the stream has cleared of urea, which is Kt/V.",
                  "Kt/V compares the volume of blood water cleared of urea during the session (K &times; t) with the volume of water in the "
                  "body (V). It measures small-solute removal only."),
    "pod07_diffconv": ("physician-on-duty-07-diffusion-vs-convection.webp",
                       "One dialyzer fiber shown twice. In the diffusion panel, small solutes such as urea and potassium cross the membrane from "
                       "high to low concentration while larger middle molecules stay behind. In the convection panel, water is pushed through "
                       "the membrane and carries both small solutes and larger middle molecules with it, and clean replacement fluid is added "
                       "back to the blood.",
                       "Diffusion moves small molecules well. Convection drags larger middle molecules with the water. Hemodiafiltration combines "
                       "the two and replaces the water removed with ultrapure fluid."),
}
