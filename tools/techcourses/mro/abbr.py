# -*- coding: utf-8 -*-
"""Abbreviations for the Medical Records Officer track: token -> (expansion, plain note). Merged into SHARED.ABBR
(generate_tech_courses.py) so auto_expand() and the glossary pick them up. Tokens already in the shared or nursing
tables (DOH, HD, PD, CKD, AKI, PSN, SOP, WHO, ...) are not repeated."""

ABBR = {
    "MRO": ("medical records officer", "The person designated to keep a facility&rsquo;s records."),
    "PIC": ("personal information controller", "The organization that decides how personal data are used and owns breach-notification decisions."),
    "DPO": ("data protection officer", "The person who advises on privacy and handles breach assessment."),
    "NPC": ("National Privacy Commission", "The Philippine body that enforces the Data Privacy Act."),
    "DBNMS": ("Data Breach Notification Management System", "The NPC&rsquo;s online channel for breach notifications."),
    "PDD": ("PhilHealth Dialysis Database", "PhilHealth&rsquo;s eligibility database for the hemodialysis package."),
    "PRDR": ("Philippine Renal Disease Registry", "The national registry of patients on kidney replacement therapy."),
    "REDCOP": ("Renal Disease Control Program", "The DOH program the registry supports."),
    "EHR": ("electronic health record", "A computerized record of a patient&rsquo;s care."),
    "EMR": ("electronic medical record", "A computerized record used within one facility."),
    "MPI": ("master patient index", "The list linking each person to one chart number."),
    "PIN": ("PhilHealth Identification Number", "The member number PhilHealth assigns."),
    "NAP": ("National Archives of the Philippines", "Approves disposal schedules and authority for public records."),
    "JAO": ("joint administrative order", "An order issued jointly by two or more agencies."),
    "YAKAP": ("Yaman ng Kalusugan Program", "PhilHealth&rsquo;s primary-care benefit."),
    "SOA": ("statement of account", "The itemized bill submitted with a claim."),
    "eSOA": ("electronic statement of account", "The electronic form of the statement of account."),
    "CI": ("confidence interval", "The range in which the true rate plausibly lies."),
    "PWD": ("person with disability", "Eligible for a PWD identification card and related benefits."),
    "HMO": ("health maintenance organization", "A private health plan."),
    "ESRD": ("end-stage renal disease", "Kidney failure treated with dialysis or transplant."),
    "AO": ("administrative order", "A numbered DOH issuance with rules."),
    "DC": ("department circular", "A numbered DOH issuance that disseminates or clarifies policy."),
    "DRG": ("diagnosis-related group", "A payment method that groups hospital cases by diagnosis."),
    "LTO": ("License to Operate", "The DOH license a facility needs to run."),
    "HIM": ("health information management", "The profession that manages health records."),
    "NHS": ("National Health Service", "England&rsquo;s public health system."),
    "NSW": ("New South Wales", "An Australian state."),
}
