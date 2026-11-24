# -*- coding: utf-8 -*-
"""References for the Medical Records Officer (MRO) track (APA 7). Merged into SHARED.REFS like the other tracks.
Cite in module text as [[key]]. Keys are prefixed mro_ so nothing collides with other tracks. The track also cites
shared keys defined elsewhere, unchanged: doh2012, psn2024 (shared.py) and dch_philhealth2024, dch_philhealth2024q,
dch_ra10173, dch_npc1603, dch_cfr494, dch_doh_rao_tool (DCH refs.py).
Journal entries were built from PubMed metadata retrieved on November 24, 2026. Regulatory entries were checked
against the issuing body's public pages on the same date. Two entries carry bracketed notes in place of a verified
official title (mro_npc2023_06, mro_nsw2025); replace them before publication."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    # ── peer-reviewed evidence ──
    "mro_just2016": ("Just, B. H., Marc, D., Munns, M., &amp; Sandefer, R. (2016). Why patient matching is a challenge: Research on "
                     "master patient index (MPI) data discrepancies in key identifying fields. <em>Perspectives in Health Information "
                     "Management, 13</em>(Spring), 1e. https://pubmed.ncbi.nlm.nih.gov/27134610/"),
    "mro_adelman2019": ("Adelman, J. S., Applebaum, J. R., Schechter, C. B., Berger, M. A., Reissman, S. H., Thota, R., Racine, A. D., "
                        "Vawdrey, D. K., Green, R. A., Salmasian, H., Schiff, G. D., Wright, A., Landman, A., Bates, D. W., Koppel, R., "
                        "Galanter, W. L., Lambert, B. L., Paparella, S., &amp; Southern, W. N. (2019). Effect of restriction of the number "
                        "of concurrently open records in an electronic health record on wrong-patient order errors: A randomized clinical "
                        "trial. <em>JAMA, 321</em>(18), 1780&ndash;1787. " + _doi("10.1001/jama.2019.3698")),
    "mro_salmasian2020": ("Salmasian, H., Blanchfield, B. B., Joyce, K., Centeio, K., Schiff, G. B., Wright, A., Baugh, C. W., Schuur, J. D., "
                          "Bates, D. W., Adelman, J. S., &amp; Landman, A. B. (2020). Association of display of patient photographs in the "
                          "electronic health record with wrong-patient order entry errors. <em>JAMA Network Open, 3</em>(11), e2019652. "
                          + _doi("10.1001/jamanetworkopen.2020.19652")),
    "mro_lima2023": ("Lima, M. M. S., Rocha, F. G. S., Fernandes, C. D. S., Barros, L. M., Galindo Neto, N. M., &amp; Caetano, J. &Aacute;. "
                     "(2023). Patient safety in hemodialysis clinics: Perception of the nursing team. <em>Revista Ga&uacute;cha de "
                     "Enfermagem, 44</em>, e20230022. " + _doi("10.1590/1983-1447.2023.20230022.en")),
    "mro_tsou2017": ("Tsou, A. Y., Lehmann, C. U., Michel, J., Solomon, R., Possanza, L., &amp; Gandhi, T. (2017). Safe practices for copy "
                     "and paste in the EHR: Systematic review, recommendations, and novel model for health IT collaboration. <em>Applied "
                     "Clinical Informatics, 8</em>(1), 12&ndash;34. " + _doi("10.4338/ACI-2016-09-R-0150")),
    "mro_longenecker2000": ("Longenecker, J. C., Coresh, J., Klag, M. J., Levey, A. S., Martin, A. A., Fink, N. E., &amp; Powe, N. R. (2000). "
                            "Validation of comorbid conditions on the end-stage renal disease medical evidence report: The CHOICE study. "
                            "<em>Journal of the American Society of Nephrology, 11</em>(3), 520&ndash;529. " + _doi("10.1681/ASN.V113520")),
    "mro_bell2020": ("Bell, S. K., Delbanco, T., Elmore, J. G., Fitzgerald, P. S., Fossa, A., Harcourt, K., Leveille, S. G., Payne, T. H., "
                     "Stametz, R. A., Walker, J., &amp; DesRoches, C. M. (2020). Frequency and types of patient-reported errors in "
                     "electronic health record ambulatory care notes. <em>JAMA Network Open, 3</em>(6), e205867. "
                     + _doi("10.1001/jamanetworkopen.2020.5867")),
    "mro_larsen2018": ("Larsen, E., Fong, A., Wernz, C., &amp; Ratwani, R. M. (2018). Implications of electronic health record downtime: "
                       "An analysis of patient safety event reports. <em>Journal of the American Medical Informatics Association, 25</em>(2), "
                       "187&ndash;191. " + _doi("10.1093/jamia/ocx057")),
    "mro_larsen2019": ("Larsen, E., Hoffman, D., Rivera, C., Kleiner, B. M., Wernz, C., &amp; Ratwani, R. M. (2019). Continuing patient care "
                       "during electronic health record downtime. <em>Applied Clinical Informatics, 10</em>(3), 495&ndash;504. "
                       + _doi("10.1055/s-0039-1692678")),
    "mro_fang2025": ("Fang, Q., Liang, J., Xiang, P., Zhao, M., He, Y., Zhang, Z., Wan, H., Hu, Y., Wang, T., &amp; Lei, J. (2025). "
                     "Electronic health record downtime events of a hospital: A retrospective analysis from adverse event reports. "
                     "<em>Applied Clinical Informatics, 16</em>(5), 1419&ndash;1429. " + _doi("10.1055/a-2701-5819")),
    # ── Philippine authorities ──
    "mro_doh2021rds": ("Department of Health. (2021). <em>Department Circular No. 2021-0226: Dissemination of the approved records "
                       "disposition schedule (RDS)</em> [Retention periods as stated in the DOH response to a Freedom of Information "
                       "request]. Retrieved November 24, 2026, from https://foi.gov.ph/agencies/doh/retention-and-disposal-of-records"),
    "mro_doh2025icd11": ("Department of Health. (2025). <em>Administrative Order No. 2025-0021: ICD-11 implementation guidelines</em>. "
                         "Retrieved November 24, 2026, from https://sites.google.com/view/doh-hfdb/2025-q4-updates/ao-2025-0021"),
    "mro_ph2017icd": ("Philippine Health Insurance Corporation. (2017). <em>PhilHealth Advisory No. 2017-0008: Clarification on 2016 ICD-10 "
                      "updates</em>. https://www.philhealth.gov.ph/advisories/2017/adv2017-0008.pdf"),
    "mro_ph2023": ("Philippine Health Insurance Corporation. (2023). <em>PhilHealth Circular No. 2023-0009: Institutionalization of 156 "
                   "hemodialysis sessions</em>. https://www.philhealth.gov.ph/circulars/2023/PC2023-0009.pdf"),
    "mro_ph2024ts": ("Philippine Health Insurance Corporation. (2024). <em>Tamang sagot: PhilHealth Circular No. 2024-0023 (Revision 2)</em>. "
                     "https://www.philhealth.gov.ph/circulars/2024/TS_PC2024-0023.pdf"),
    "mro_ph2025_45day": ("Philippine Health Insurance Corporation. (2025). <em>PhilHealth Advisory No. 2025-0035: Effectivity of lifting of "
                         "the 45-day benefit limit rule</em>. https://www.philhealth.gov.ph/advisories/2025/PA2025-0035.pdf"),
    "mro_ph2025news": ("Philippine Health Insurance Corporation. (2025, March 27). <em>PhilHealth&rsquo;s expanded benefits bring financial "
                       "relief to dialysis patients</em> [News release]. https://www.philhealth.gov.ph/news/up/article/2025/news_67e9e793775ed.php"),
    "mro_ph2016pdd": ("Philippine Health Insurance Corporation. (2016). <em>PhilHealth Circular No. 2016-0007</em> [PhilHealth Dialysis "
                      "Database]. https://www.philhealth.gov.ph/circulars/2016/circ2016-007.pdf"),
    "mro_ph2025acc": ("Philippine Health Insurance Corporation. (2025). <em>PhilHealth Advisory No. 2025-0055: Application for renewal of "
                      "accreditation of health facilities for calendar year 2026</em>. https://www.philhealth.gov.ph/advisories/2025/PA2025-0055.pdf"),
    "mro_ph2025emr": ("Philippine Health Insurance Corporation. (2025). <em>PhilHealth Advisory No. 2025-0077: Decommissioning of the "
                      "PhilHealth eKonsulta system</em>. https://www.philhealth.gov.ph/advisories/2025/PA2025-0077.pdf"),
    "mro_ph2023medusa": ("Philippine Health Insurance Corporation. (2023, October 2). <em>Urgent notice to the public</em>. "
                         "https://www.philhealth.gov.ph/ofclstmnts/2023/UN2023-10-03.pdf"),
    "mro_jao2021": ("Department of Health &amp; Philippine Health Insurance Corporation. (2021). <em>Joint Administrative Order No. 2021-0002: "
                    "Mandatory adoption and use of national health data standards for interoperability</em>. "
                    "https://law.upd.edu.ph/wp-content/uploads/2021/06/DOH-PHIC-JAO-No-2021-002.pdf"),
    "mro_ra9470": ("Republic Act No. 9470: National Archives of the Philippines Act of 2007. (2007). Congress of the Philippines. "
                   "https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/19575"),
    "mro_npc_irr": ("National Privacy Commission. (2016). <em>Implementing rules and regulations of Republic Act No. 10173, known as the "
                    "Data Privacy Act of 2012</em>. https://privacy.gov.ph/implementing-rules-regulations-data-privacy-act-2012/"),
    "mro_npc2023_06": ("National Privacy Commission. (2023). <em>NPC Circular No. 2023-06</em> [Minimum security requirements for personal "
                       "data; confirm the official title before publication]. https://privacy.gov.ph/"),
    "mro_npc2026dbnms": ("National Privacy Commission. (2026). <em>NPC Advisory No. 2026-02</em> [Guidelines on submitting breach "
                         "notifications through the Data Breach Notification Management System], as summarized by Baker McKenzie. "
                         "https://www.bakermckenzie.com/en/insight/publications/2026/06/philippines-data-breach-notification-procedure-further-clarified"),
    "mro_npc_ao2020": ("National Privacy Commission. (2020). <em>Advisory Opinion No. 2020-009</em>. "
                       "https://www.privacy.gov.ph/wp-content/uploads/2020/10/Redacted-Advisory-Opinion-No.-2020-009.pdf"),
    "mro_who_icd11": ("World Health Organization. (2025). <em>ICD-11 implementation: Frequently asked questions</em>. "
                      "https://www.who.int/standards/classifications/frequently-asked-questions/icd-11-implementation"),
    # ── international comparators ──
    "mro_nhs_code": ("NHS England. (n.d.). <em>Records management code of practice</em>. Retrieved November 24, 2026, from "
                     "https://digital.nhs.uk/data-and-information/information-governance/guidance/records-management-code-of-practice/records-management-obligations"),
    "mro_nsw2025": ("NSW Health. (2025). <em>Policy Directive PD2025_035</em> [Health care records; confirm the official title before "
                    "publication]. https://www1.health.nsw.gov.au/pds/ActivePDSDocuments/PD2025_035.pdf"),
    "mro_cihi_corr": ("Canadian Institute for Health Information. (n.d.). <em>Canadian Organ Replacement Register (CORR)</em>. Retrieved "
                      "November 24, 2026, from https://www.cihi.ca/en/canadian-organ-replacement-register-corr"),
    "mro_nrdo": ("National Registry of Diseases Office. (n.d.). <em>Legislation</em>. Retrieved November 24, 2026, from "
                 "https://www.nrdo.gov.sg/legislation/"),
    "mro_bls": ("U.S. Bureau of Labor Statistics. (n.d.). <em>Medical records specialists: Occupational outlook handbook</em>. Retrieved "
                "November 24, 2026, from https://www.bls.gov/ooh/healthcare/medical-records-and-health-information-technicians.htm"),
}
