# -*- coding: utf-8 -*-
"""Abbreviations for the Renal Transplant Coordinator track: token -> (expansion, plain note). Merged into SHARED.ABBR
(generate_tech_courses.py) so auto_expand() and the glossary pick them up. Tokens already in the shared, nursing, or other
track tables (DOH, KDIGO, ESKD, HD, PD, CKD, NPC, DPO, SBAR, MDT, eGFR, WHO, HMO, PCSO, ...) are not repeated."""

ABBR = {
    "HTEC": ("Hospital Transplant Ethics Committee", "The hospital committee that reviews living donation for voluntariness and ethics."),
    "NTEC": ("National Transplant Ethics Committee", "The national-level ethics committee for cases referred beyond the hospital."),
    "PhilNOS": ("Philippine Network for Organ Sharing", "The national program that coordinates deceased organ donation and sharing."),
    "OPO": ("organ procurement organization", "The service that manages deceased donors and organ retrieval."),
    "HLA": ("human leukocyte antigen", "Tissue-type markers on cells that the immune system uses to tell self from non-self."),
    "PRA": ("panel reactive antibody", "An estimate of how many potential donors a person has antibodies against."),
    "cPRA": ("calculated panel reactive antibody", "A computed estimate of the share of donors a candidate is likely incompatible with."),
    "DSA": ("donor-specific antibody", "An antibody in the recipient that targets the HLA of a specific donor."),
    "KT": ("kidney transplantation", "Used in PhilHealth package and registry names."),
    "CMV": ("cytomegalovirus", "A common virus that can cause serious infection after transplant."),
    "PSTS": ("Philippine Society for Transplant Surgeons", "The professional society of transplant surgeons."),
    "RN": ("registered nurse", "A nurse licensed by the Professional Regulation Commission."),
    "OPTN": ("Organ Procurement and Transplantation Network", "The United States national transplant system; used here only for comparison."),
    "ABTC": ("American Board for Transplant Certification", "A United States certifying board for transplant coordinators; comparison only."),
    "HTA": ("Human Tissue Authority", "The United Kingdom regulator of living donation; comparison only."),
    "ATG": ("antithymocyte globulin", "An induction medicine that depletes T cells around the time of transplant."),
    "rATG": ("rabbit antithymocyte globulin", "One form of antithymocyte globulin; named in PhilHealth package codes."),
    "eATG": ("equine antithymocyte globulin", "Another form of antithymocyte globulin; named in PhilHealth package codes."),
    "PAGCOR": ("Philippine Amusement and Gaming Corporation", "A government corporation that has funded medical assistance."),
    "MAIFIP": ("Medical Assistance for Indigent and Financially Incapacitated Patients", "A DOH medical assistance program run through hospitals."),
    "LGU": ("local government unit", "A province, city, or municipality, some of which offer medical assistance."),
    "OFW": ("overseas Filipino worker", "A Filipino working abroad."),
    "KDPI": ("Kidney Donor Profile Index", "A United States score of deceased-donor kidney quality; comparison only."),
    "EPTS": ("Estimated Post-Transplant Survival", "A United States score used in allocation; comparison only."),
    "PSA": ("Philippine Statistics Authority", "The agency that issues birth, marriage, and death certificates."),
    "PNA": ("Philippine Nurses Association", "The national professional organization of nurses."),
    "ILDA": ("independent living donor advocate", "A United States role that represents only the donor's interests; comparison only."),
}
