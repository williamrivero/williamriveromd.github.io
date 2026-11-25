# -*- coding: utf-8 -*-
"""Abbreviations for the Renal Social Worker track: token -> (expansion, plain note). Merged into SHARED.ABBR
(generate_tech_courses.py) so auto_expand() and the glossary pick them up. Tokens already in the shared, nursing, or other
track tables (DOH, PSN, PRC, DSWD, PCSO, LGU, PWD, OFW, HD, PD, CKD, CKM, KDIGO, eGFR, HTEC, DPO, NPC, SBAR, MDT, QI ...)
are not repeated."""

ABBR = {
    "PHQ-9": ("Patient Health Questionnaire-9", "Nine questions on the past two weeks, each scored 0 to 3; a screen, not a diagnosis."),
    "PHQ-2": ("Patient Health Questionnaire-2", "The first two PHQ-9 questions, used as a quick first screen."),
    "CBT": ("cognitive behavioral therapy", "A structured talking therapy that works on thoughts and habits."),
    "AICS": ("Assistance to Individuals in Crisis Situation", "A DSWD program that may give medical, transport, or other crisis aid after assessment."),
    "SDG": ("Sustainable Development Goal", "United Nations targets; SDG 3.8.2 tracks households with large health spending."),
    "OARS": ("open questions, affirmations, reflections, and summaries", "The four core skills of motivational interviewing."),
    "SIPAT": ("Stanford Integrated Psychosocial Assessment for Transplantation", "A structured psychosocial rating used by some transplant programs."),
    "ACP": ("advance care planning", "Conversations about what matters most and who speaks for a person who cannot."),
    "NCMH": ("National Center for Mental Health", "The national mental health hospital; runs a crisis hotline."),
    "VAWC": ("violence against women and their children", "Named in Republic Act No. 9262; barangay and police desks handle reports."),
    "RSW": ("registered social worker", "A social worker licensed by the Professional Regulation Commission."),
    "MSW": ("Master of Social Work", "A graduate degree; required for some posts abroad, not for Philippine licensure."),
    "SSS": ("Social Security System", "The social insurance agency for private-sector workers."),
    "GSIS": ("Government Service Insurance System", "The social insurance agency for government workers."),
    "DOLE": ("Department of Labor and Employment", "The agency for workers' rights and employment programs."),
    "FTE": ("full-time equivalent", "One full-time position's worth of working hours."),
    "CHD": ("Center for Health Development", "A DOH regional office; its licensing section inspects facilities."),
    "PGD": ("prolonged grief disorder", "Grief that stays intense and disabling well beyond expected time; a diagnosis made by a mental health clinician."),
    "BHW": ("barangay health worker", "A community health volunteer in the barangay."),
    "HR-QOL": ("health-related quality of life", "How a person rates their own physical and mental well-being."),
}
