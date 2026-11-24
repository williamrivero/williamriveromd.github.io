# -*- coding: utf-8 -*-
"""Abbreviations for the PhilHealth Claims track: token -> (expansion, plain note). Merged into SHARED.ABBR.
"ACR" is deliberately absent: the shared nursing table defines it as albumin-to-creatinine ratio, so this track
always writes "case rates" or "All Case Rates" in full."""

ABBR = {
    "PDD": ("PhilHealth Dialysis Database", "The registry of patients with chronic kidney disease stage 5 on dialysis; registration is required for the dialysis benefits."),
    "PBEF": ("PhilHealth Benefit Eligibility Form", "The printed result of an eligibility check, when the facility workflow uses it."),
    "CSF": ("Claim Signature Form", "The form that carries the member&rsquo;s or patient&rsquo;s signature and consent for a claim."),
    "CF1": ("Claim Form 1", "Member and patient information for a claim."),
    "CF2": ("Claim Form 2", "Provider and service information, including the diagnosis and procedure codes and hemodialysis consumption."),
    "CF4": ("Claim Form 4", "Clinical information for the claim, where required."),
    "CF5": ("Claim Form 5", "Inpatient clinical data for diagnosis-related group shadow billing; mandatory for inpatient discharges from August 1, 2026."),
    "eSOA": ("electronic statement of account", "The bill for a claim, sent to PhilHealth as structured XML data."),
    "SOA": ("statement of account", "The itemized bill for a patient&rsquo;s care."),
    "XML": ("Extensible Markup Language", "A structured file format computers can check field by field."),
    "PDF": ("Portable Document Format", "A file that looks like a printed page; PhilHealth no longer accepts it as the statement of account."),
    "RVS": ("Relative Value Scale", "PhilHealth&rsquo;s procedure codes; 90935 is hemodialysis."),
    "DRG": ("diagnosis-related group", "A payment group assigned from a hospital case&rsquo;s full set of diagnosis and procedure codes."),
    "PRO": ("PhilHealth Regional Office", "Where a facility gets written guidance on PhilHealth rules."),
    "LHIO": ("Local Health Insurance Office", "PhilHealth&rsquo;s local office for members and facilities."),
    "DPO": ("Data Protection Officer", "The person who leads the facility&rsquo;s privacy program and incident response."),
    "NPC": ("National Privacy Commission", "The government agency that enforces the Data Privacy Act."),
    "PIN": ("PhilHealth Identification Number", "The member&rsquo;s permanent PhilHealth number."),
    "RTH": ("return to hospital", "A claim PhilHealth sends back to the facility for correction or completion."),
    "LTO": ("License to Operate", "The Department of Health license a facility needs to operate."),
    "ICD-10": ("International Classification of Diseases, 10th Revision", "The diagnosis code set PhilHealth uses, with Philippine modifications."),
}
