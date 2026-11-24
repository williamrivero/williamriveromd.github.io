# -*- coding: utf-8 -*-
"""New illustrated figures for Physician on Duty, Module 31. key: (file in images/, alt text, default caption).
The image files do not exist yet; the page leaves the slot empty until the art is produced.
Reused site figures: dashboard, fishbone, pdsa."""

FIGS = {
    "pod31_model_event_note": ("physician-on-duty-31-model-event-note.webp",
                               "A reference card showing a handwritten-style event note for a fictional patient on a dialysis progress "
                               "sheet. Eight labels point to its parts: date, clock time, findings with units, actions taken, the "
                               "patient&rsquo;s response, the call made to the attending nephrologist, the advice received, and the plan "
                               "with the person responsible. A small box at the bottom shows how a late entry is labeled.",
                               "A model event note. Each of the eight elements answers a question a later reader cannot ask you."),
    "pod31_privacy_at_the_station": ("physician-on-duty-31-privacy-at-the-station.webp",
                                     "A reference card with five panels showing privacy risks in a dialysis unit, each beside the safer "
                                     "practice: a wall board with full names next to one with station numbers; a phone photographing a "
                                     "treatment sheet next to the unit&rsquo;s approved system; a group chat with a patient&rsquo;s name next "
                                     "to a message with a record number only; a station label showing hepatitis B status next to a plain "
                                     "isolation sign; and an open chart on a chair next to a closed chart at the station.",
                                     "Five ways patient data leak in a dialysis unit, and the safer practice for each."),
    "pod31_run_chart_shift": ("physician-on-duty-31-run-chart-shift.webp",
                              "A run chart of the percentage of patients dialyzing through a catheter over twelve months, with values "
                              "30, 28, 31, 29, 30, 27, 24, 23, 22, 22, 21, and 20 percent. A horizontal median line sits at 25.5 percent. "
                              "The last six points, months 7 to 12, all lie below the median and are circled and labeled as a shift. "
                              "The data are illustrative.",
                              "Six consecutive points below the median form a shift: a signal that something changed around month 7. "
                              "Illustrative data."),
    "pod31_weak_vs_strong_actions": ("physician-on-duty-31-weak-vs-strong-actions.webp",
                                     "A ladder of corrective actions after an incident, from weaker at the bottom to stronger at the top. "
                                     "The lower rungs show reminders, warning signs, and retraining. The middle rungs show checklists and "
                                     "double checks. The top rungs show standardized equipment, simplified processes, and forcing "
                                     "functions, such as a treatment sheet that cannot be closed until the medication line is signed.",
                                     "Fixes that depend on people remembering are weaker than fixes that change the system. Reviews "
                                     "often stop at the lower rungs."),
}
