# -*- coding: utf-8 -*-
"""References for the PhilHealth Claims track (APA 7). Merged into SHARED.REFS like the POD, Head Nurse, and DCH refs.
Cite in module text as [[key]]. Keys are prefixed pc_; shared DCH keys (dch_foley2011, dch_alsalmi2018, dch_saran2003,
dch_ra10173, dch_npc1603, dch_philhealth2023acc, dch_philhealth2024q, dch_philhealth_pa2024) are cited as they are.
Journal entries come from PubMed metadata retrieved on November 24, 2026. PhilHealth issuances were located on
philhealth.gov.ph on the same date; entries whose official title could not be read in full carry a bracketed description
instead of a title, and should be replaced with the exact title before the next review."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _u(u):
    return f'<a href="{u}">{u}</a>'


_PH = "Philippine Health Insurance Corporation. "

REFS = {
    # ---- Hemodialysis benefit and limits
    "pc_pc2024_0023": (_PH + "(2024). <em>PhilHealth Circular No. 2024-0023: Institutionalization of 156 hemodialysis sessions and coverage expansion (Revision 2)</em>. " + _u("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "pc_pc2023_0009": (_PH + "(2023). <em>PhilHealth Circular No. 2023-0009: Institutionalization of 156 hemodialysis sessions</em>. " + _u("https://www.philhealth.gov.ph/circulars/2023/PC2023-0009.pdf")),
    "pc_news2024": (_PH + "(2024, October 17). <em>PhilHealth increases dialysis coverage to P1 million per year</em> [News release]. " + _u("https://www.philhealth.gov.ph/news/up/article/2024/news_6710c0050d979.php")),
    "pc_agreement_form": (_PH + "(2024). <em>Hemodialysis benefits agreement form</em> [Form]. " + _u("https://www.philhealth.gov.ph/downloads/claim/HemodialysisBenefitsAgreementForm.pdf")),
    "pc_pc2025_0007": (_PH + "(2025). <em>PhilHealth Circular No. 2025-0007: Lifting the 45-day benefit limit rule</em>. " + _u("https://www.philhealth.gov.ph/circulars/2025/PC2025-0007.pdf")),
    "pc_pa2025_0035": (_PH + "(2025). <em>PhilHealth Advisory No. 2025-0035: Effectivity of lifting of the 45-day benefit limit rule</em>. " + _u("https://www.philhealth.gov.ph/advisories/2025/PA2025-0035.pdf")),
    "pc_news2025_nkti": (_PH + "(2025, May 28). <em>PhilHealth speeds up payments, releases over P592M to NKTI in less than 5 months</em> [News release]. " + _u("https://www.philhealth.gov.ph/news/up/article/2025/news_686f52507b28b.php")),
    # ---- Eligibility and the dialysis database
    "pc_pc2022_0013": (_PH + "(2022). <em>PhilHealth Circular No. 2022-0013</em> [Immediate eligibility of members and dependents]. " + _u("https://www.philhealth.gov.ph/circulars/2022/circ2022-0013.pdf")),
    "pc_pa2016_0030": (_PH + "(2016). <em>PhilHealth Advisory No. 2016-0030</em> [Registration in the PhilHealth Dialysis Database]. " + _u("https://www.philhealth.gov.ph/advisories/2016/adv2016-0030.pdf")),
    # ---- Statement of account, eClaims, filing
    "pc_pc2023_0026": (_PH + "(2023). <em>PhilHealth Circular No. 2023-0026</em> [Electronic submission of the statement of account for all case rates claims]. " + _u("https://www.philhealth.gov.ph/circulars/2023/PC2023-0026.pdf")),
    "pc_pa2025_0040": (_PH + "(2025). <em>PhilHealth Advisory No. 2025-0040: Processing of claims of health facilities in compliance to the submission of electronic statement of account (eSOA) for all case rates claims and identified PhilHealth benefits</em>. " + _u("https://www.philhealth.gov.ph/advisories/2025/PA2025-0040.pdf")),
    "pc_pa2026_0022": (_PH + "(2026). <em>PhilHealth Advisory No. 2026-0022: Final reminder on eClaims 3.0 implementation</em>. " + _u("https://www.philhealth.gov.ph/advisories/2026/PA2026-0022.pdf")),
    "pc_pa2026_0027": (_PH + "(2026). <em>PhilHealth Advisory No. 2026-0027: Final deadline for all accredited health facilities to migrate to E-Claims version 3.0</em>. " + _u("https://www.philhealth.gov.ph/advisories/2026/PA2026-0027.pdf")),
    "pc_pa2026_0037": (_PH + "(2026). <em>PhilHealth Advisory No. 2026-0037</em> [Implementation of the PhilHealth Ticketing System, effective July 15, 2026]. " + _u("https://www.philhealth.gov.ph/advisories/2026/PA2026-0037_v1.pdf")),
    "pc_pc2019_0002": (_PH + "(2019). <em>PhilHealth Circular No. 2019-0002</em> [Claim Form 4 and its instructions]. " + _u("https://www.philhealth.gov.ph/circulars/2019/circ2019-0002.pdf")),
    "pc_pc2025_0019": (_PH + "(2025). <em>PhilHealth Circular No. 2025-0019</em> [Filing period for benefit claims]. " + _u("https://www.philhealth.gov.ph/circulars/2025/PC2025-0019.pdf")),
    "pc_pc2025_0006": (_PH + "(2025). <em>PhilHealth Circular No. 2025-0006: Flexibility in claims submission deadline for claims filed from January 1, 2018 to December 31, 2024</em>. " + _u("https://www.philhealth.gov.ph/circulars/2025/TS_PC2025-0006.pdf")),
    "pc_pa2025_0037": (_PH + "(2025). <em>PhilHealth Advisory No. 2025-0037</em> [Effectivity period of PhilHealth Circular No. 2025-0006, March 21 to September 21, 2025]. " + _u("https://www.philhealth.gov.ph/advisories/2025/PA2025-0037.pdf")),
    "pc_pa2024_0057": (_PH + "(2024). <em>PhilHealth Advisory No. 2024-0057</em> [Extended filing period for claims in areas affected by Typhoon Kristine]. " + _u("https://www.philhealth.gov.ph/advisories/2024/PA2024-0057.pdf")),
    # ---- Codes, case rates, and DRG
    "pc_pc31_2013": (_PH + "(2013). <em>PhilHealth Circular No. 31, s. 2013: All case rates (ACR) policy no. 1</em> [Governing policies in the shift of provider payment to case rates]. " + _u("https://www.philhealth.gov.ph/circulars/2013/circ31_2013.pdf")),
    "pc_pc35_2013": (_PH + "(2013). <em>PhilHealth Circular No. 35, s. 2013: ACR policy no. 2: Implementing guidelines on medical and procedure case rates</em>. " + _u("https://www.philhealth.gov.ph/circulars/2013/circ35_2013.pdf")),
    "pc_pc30_2015": (_PH + "(2015). <em>PhilHealth Circular No. 30, s. 2015: New ICD 10 codes and category titles related to chronic kidney disease</em>. " + _u("https://www.philhealth.gov.ph/circulars/2015/circ030-2015.pdf")),
    "pc_pc2017_0019": (_PH + "(2017). <em>PhilHealth Circular No. 2017-0019: Updated list of ICD-10 codes for selected medical case rates</em>. " + _u("https://www.philhealth.gov.ph/circulars/2017/circ2017-0019.pdf")),
    "pc_pc2026_0012": (_PH + "(2026). <em>PhilHealth Circular No. 2026-0012: Implementation of shadow billing for the transition to diagnosis-related groups (DRG) (Revision 2)</em>. " + _u("https://www.philhealth.gov.ph/circulars/2026/PC-2026-0012.pdf")),
    "pc_pa2026_0036": (_PH + "(2026). <em>PhilHealth Advisory No. 2026-0036: Shadow billing of diagnosis-related groups (DRG)</em>. " + _u("https://www.philhealth.gov.ph/advisories/2026/PA2026-0036.pdf")),
    "pc_pa2026_0010": (_PH + "(2026). <em>PhilHealth Advisory No. 2026-0010: Call for participation in shadow billing (submission of Claim Form 5 and electronic statement of account through eClaims 3.0)</em>. " + _u("https://www.philhealth.gov.ph/advisories/2026/PA2026-0010.pdf")),
    "pc_drg_manual": ("Philippine Institute for Development Studies, Health Economics and Finance Program. (2026). <em>Philippine diagnosis-related groups implementation manual: Details of the DRG grouper, version 1</em>. Philippine Health Insurance Corporation. " + _u("https://www.philhealth.gov.ph/partners/providers/pdf/PhilippineDiagnosis_RelatedGroupsImplementationManual.pdf")),
    # ---- Accreditation, privacy
    "pc_accred_process": (_PH + "(n.d.). <em>Accreditation process for health facilities</em> [Web page]. Retrieved November 24, 2026, from " + _u("https://www.philhealth.gov.ph/partners/providers/facilities/process.php")),
    "pc_npc_irr": ("National Privacy Commission. (2016). <em>Implementing rules and regulations of Republic Act No. 10173, known as the Data Privacy Act of 2012</em>. " + _u("https://privacy.gov.ph/implementing-rules-regulations-data-privacy-act-2012/")),
    # ---- Other renal pathways
    "pc_pc2024_0036": (_PH + "(2024). <em>PhilHealth Circular No. 2024-0036: Z benefits package for peritoneal dialysis (PD)</em>. " + _u("https://www.philhealth.gov.ph/circulars/2024/TS_PC2024-0036.pdf")),
    "pc_pa2025_0074": (_PH + "(2025). <em>PhilHealth Advisory No. 2025-0074</em> [Pilot implementation of the Z benefits package for peritoneal dialysis covering automated PD in children]. " + _u("https://www.philhealth.gov.ph/advisories/2025/PA2025-0074.pdf")),
    "pc_pc2024_0035": (_PH + "(2024). <em>PhilHealth Circular No. 2024-0035</em> [Z benefits package for kidney transplantation]. " + _u("https://www.philhealth.gov.ph/circulars/2024/archives.php")),
    "pc_pc2025_0011": (_PH + "(2025). <em>PhilHealth Circular No. 2025-0011</em> [Post-kidney transplantation services under the Z benefits package]. " + _u("https://www.philhealth.gov.ph/circulars/2025/PC2025-0011.pdf")),
    "pc_news2025_pd": (_PH + "(2025, January 27). <em>Major win for dialysis patients: Coverage for peritoneal dialysis now up to P1.2 million; assistance extended to children</em> [News release]. " + _u("https://www.philhealth.gov.ph/news/up/article/2025/news_6798250c33dae.php")),
    # ---- Journal articles (PubMed-verified)
    "pc_obialo2012": ("Obialo, C. I., Hunt, W. C., Bashir, K., &amp; Zager, P. G. (2012). Relationship of missed and shortened hemodialysis treatments to hospitalization and mortality: Observations from a US dialysis network. <em>Clinical Kidney Journal, 5</em>(4), 315&ndash;319. " + _doi("10.1093/ckj/sfs071")),
    "pc_cohen2020": ("Cohen, D. E., Gray, K. S., Colson, C., Van Wyck, D. B., Tentori, F., &amp; Brunelli, S. M. (2020). Impact of rescheduling a missed hemodialysis treatment on clinical outcomes. <em>Kidney Medicine, 2</em>(1), 12&ndash;19. " + _doi("10.1016/j.xkme.2019.10.007")),
    "pc_fotheringham2020": ("Fotheringham, J., Smith, M. T., Froissart, M., Kronenberg, F., Stenvinkel, P., Floege, J., Eckardt, K.-U., &amp; Wheeler, D. C. (2020). Hospitalization and mortality following non-attendance for hemodialysis according to dialysis day of the week: A European cohort study. <em>BMC Nephrology, 21</em>(1), 218. " + _doi("10.1186/s12882-020-01874-x")),
    "pc_flythe2012": ("Flythe, J. E., &amp; Lacson, E., Jr. (2012). Outcomes after the long interdialytic break: Implications for the dialytic prescription. <em>Seminars in Dialysis, 25</em>(1), 1&ndash;8. " + _doi("10.1111/j.1525-139X.2011.01015.x")),
    "pc_pajimna2023": ("Pajimna, J. A. T., Orpilla, G. A. L., Milan, M. J. D. C., Virtucio, C. T. S., &amp; Pamatian, J. V. M. (2023). Gaps and challenges in the provision of treatment for patients with end-stage renal disease: Perspectives from the Philippines. <em>The Lancet Regional Health &ndash; Western Pacific, 38</em>, 100889. " + _doi("10.1016/j.lanwpc.2023.100889")),
    "pc_sangthawan2022": ("Sangthawan, P., Klyprayong, P., Geater, S. L., Tanvejsilp, P., Anutrakulchai, S., Boongird, S., Gojaseni, P., Kuhiran, C., Lorvinitnun, P., Noppakun, K., Parapiboon, W., Sirilak, S., Tankee, P., Taruangsri, P., Sangsupawanich, P., Sritara, P., Chaiyakunapruk, N., &amp; Kitiyakara, C. (2022). The hidden financial catastrophe of chronic kidney disease under universal coverage and Thai &ldquo;Peritoneal Dialysis First Policy&rdquo;. <em>Frontiers in Public Health, 10</em>, 965808. " + _doi("10.3389/fpubh.2022.965808")),
    # ---- HMO claims and collections (Modules 12 to 14; located and read November 26, 2026)
    "pc_eo192_2015": ("Office of the President of the Philippines. (2015). <em>Executive Order No. 192: Transferring the regulation and supervision over health maintenance organizations from the Department of Health to the Insurance Commission, directing the implementation thereof and for other purposes</em>. " + _u("https://lawphil.net/executive/execord/eo2015/eo_192_2015.html")),
    "pc_ic_cl2024_01": ("Insurance Commission. (2024). <em>Circular Letter No. 2024-01: Guidelines defining unsound business acts and providing administrative fines for violation thereof</em> [Applies to health maintenance organizations and HMO intermediaries; number and date read from a partly illegible scan]. " + _u("https://www.insurance.gov.ph/wp-content/uploads/2024/01/IC-CL-No.-2024-01_Guidelines-Defining-Unsound-Business-Acts-and-Providing-Administrative-Fines-for-Violation-Thereof.pdf")),
    "pc_ic_cl2018_14": ("Insurance Commission. (2018). <em>Circular Letter No. 2018-14: Guidelines in the handling of complaints filed against health maintenance organizations</em>. " + _u("https://elibrary.judiciary.gov.ph/thebookshelf/showdocsfriendly/10/90030")),
    "pc_ic_cl2024_18": ("Insurance Commission. (2024). <em>Circular Letter No. 2024-18: Regulatory relief on the liquidity requirement under Circular Letter No. 2016-41</em> [Health maintenance organizations]. " + _u("https://www.insurance.gov.ph/wp-content/uploads/2024/10/IC-Circular-Letter-No.-2024-18_Regulatory-Relief-on-the-Liquidity-Reqt-under-CL-No-2016-41.pdf")),
    "pc_ic_hmo_list": ("Insurance Commission. (2025). <em>List of health maintenance organizations with certificates of authority issued by the Insurance Commission, as of 31 March 2025</em> [Updated periodically; check the current list]. " + _u("https://www.insurance.gov.ph/wp-content/uploads/2025/04/List-of-HMOs-with-CA-Issued-by-the-Insurance-Commission-as-of-31-March-2025.pdf")),
    "pc_news2026_yakap_hmo": ("Daily Tribune. (2026, October 1). <em>PhilHealth pact eyes cheaper private health plans</em> [News report on the PhilHealth YAKAP&ndash;HMO/PHI Benefit Complementation memorandum of understanding]. " + _u("https://tribune.net.ph/2026/10/01/philhealth-pact-eyes-cheaper-private-health-plans")),
    "pc_news2026_yakap_hmo2": ("Context.ph. (2026, October 1). <em>PhilHealth, insurers move to cut healthcare costs</em> [News report]. " + _u("https://context.ph/2026/10/01/philhealth-insurers-move-to-cut-healthcare-costs/")),
}
