# -*- coding: utf-8 -*-
"""References for the Renal Transplant Coordinator (RTC) track (APA 7). Merged into SHARED.REFS like the other tracks.
Cite in module text as [[key]]. Keys are prefixed rtc_ so nothing collides with other tracks.
Journal entries were built from PubMed metadata retrieved on November 25, 2026. Regulatory entries were checked against
the issuing body's public pages on the same date (PhilHealth circular index and PC 2026-0019 text) or carried from the
handoff source register (sources.json, checked November 25, 2026). Replace any entry whose URL changes before publication."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    # ── peer-reviewed evidence ──
    "rtc_sullivan2012": ("Sullivan, C., Leon, J. B., Sayre, S. S., Marbury, M., Ivers, M., Pencak, J. A., Bodziak, K. A., Hricik, D. E., "
                         "Morrison, E. J., Albert, J. M., Navaneethan, S. D., Reyes, C. M., &amp; Sehgal, A. R. (2012). Impact of navigators "
                         "on completion of steps in the kidney transplant process: A randomized, controlled trial. <em>Clinical Journal of the "
                         "American Society of Nephrology, 7</em>(10), 1639&ndash;1645. " + _doi("10.2215/CJN.11731111")),
    "rtc_rodrigue2014": ("Rodrigue, J. R., Paek, M. J., Egbuna, O., Waterman, A. D., Schold, J. D., Pavlakis, M., &amp; Mandelbrot, D. A. "
                         "(2014). Making house calls increases living donor inquiries and evaluations for blacks on the kidney transplant "
                         "waiting list. <em>Transplantation, 98</em>(9), 979&ndash;986. " + _doi("10.1097/TP.0000000000000165")),
    "rtc_wolfe1999": ("Wolfe, R. A., Ashby, V. B., Milford, E. L., Ojo, A. O., Ettenger, R. E., Agodoa, L. Y., Held, P. J., &amp; Port, F. K. "
                      "(1999). Comparison of mortality in all patients on dialysis, patients on dialysis awaiting transplantation, and "
                      "recipients of a first cadaveric transplant. <em>The New England Journal of Medicine, 341</em>(23), 1725&ndash;1730. "
                      + _doi("10.1056/NEJM199912023412303")),
    "rtc_tonelli2011": ("Tonelli, M., Wiebe, N., Knoll, G., Bello, A., Browne, S., Jadhav, D., Klarenbach, S., &amp; Gill, J. (2011). "
                        "Systematic review: Kidney transplantation compared with dialysis in clinically relevant outcomes. <em>American "
                        "Journal of Transplantation, 11</em>(10), 2093&ndash;2109. " + _doi("10.1111/j.1600-6143.2011.03686.x")),
    "rtc_segev2010": ("Segev, D. L., Muzaale, A. D., Caffo, B. S., Mehta, S. H., Singer, A. L., Taranto, S. E., McBride, M. A., &amp; "
                      "Montgomery, R. A. (2010). Perioperative mortality and long-term survival following live kidney donation. "
                      "<em>JAMA, 303</em>(10), 959&ndash;966. " + _doi("10.1001/jama.2010.237")),
    "rtc_lentine2016": ("Lentine, K. L., Lam, N. N., Axelrod, D., Schnitzler, M. A., Garg, A. X., Xiao, H., Dzebisashvili, N., Schold, J. D., "
                        "Brennan, D. C., Randall, H., King, E. A., &amp; Segev, D. L. (2016). Perioperative complications after living kidney "
                        "donation: A national study. <em>American Journal of Transplantation, 16</em>(6), 1848&ndash;1857. "
                        + _doi("10.1111/ajt.13687")),
    "rtc_muzaale2014": ("Muzaale, A. D., Massie, A. B., Wang, M. C., Montgomery, R. A., McBride, M. A., Wainright, J. L., &amp; Segev, D. L. "
                        "(2014). Risk of end-stage renal disease following live kidney donation. <em>JAMA, 311</em>(6), 579&ndash;586. "
                        + _doi("10.1001/jama.2013.285141")),
    "rtc_mjoen2014": ("Mj&oslash;en, G., Hallan, S., Hartmann, A., Foss, A., Midtvedt, K., &Oslash;yen, O., Reis&aelig;ter, A., Pfeffer, P., "
                      "Jenssen, T., Leivestad, T., Line, P. D., &Oslash;vrehus, M., Dale, D. O., Pihlstr&oslash;m, H., Holme, I., Dekker, F. W., "
                      "&amp; Holdaas, H. (2014). Long-term risks for kidney donors. <em>Kidney International, 86</em>(1), 162&ndash;167. "
                      + _doi("10.1038/ki.2013.460")),
    "rtc_grams2016": ("Grams, M. E., Sang, Y., Levey, A. S., Matsushita, K., Ballew, S., Chang, A. R., Chow, E. K., Kasiske, B. L., "
                      "Kovesdy, C. P., Nadkarni, G. N., Shalev, V., Segev, D. L., Coresh, J., Lentine, K. L., &amp; Garg, A. X. (2016). "
                      "Kidney-failure risk projection for the living kidney-donor candidate. <em>The New England Journal of Medicine, "
                      "374</em>(5), 411&ndash;421. " + _doi("10.1056/NEJMoa1510491")),
    "rtc_dew2007": ("Dew, M. A., DiMartini, A. F., De Vito Dabbs, A., Myaskovsky, L., Steel, J., Unruh, M., Switzer, G. E., Zomak, R., "
                    "Kormos, R. L., &amp; Greenhouse, J. B. (2007). Rates and risk factors for nonadherence to the medical regimen after "
                    "adult solid organ transplantation. <em>Transplantation, 83</em>(7), 858&ndash;873. "
                    + _doi("10.1097/01.tp.0000258599.65257.a6")),
    "rtc_butler2004": ("Butler, J. A., Roderick, P., Mullee, M., Mason, J. C., &amp; Peveler, R. C. (2004). Frequency and impact of "
                       "nonadherence to immunosuppressants after renal transplantation: A systematic review. <em>Transplantation, "
                       "77</em>(5), 769&ndash;776. " + _doi("10.1097/01.tp.0000110408.83054.88")),
    "rtc_fu2021": ("Fu, R., Sekercioglu, N., Hishida, M., &amp; Coyte, P. C. (2021). Economic consequences of adult living kidney donation: "
                   "A systematic review. <em>Value in Health, 24</em>(4), 592&ndash;601. " + _doi("10.1016/j.jval.2020.10.005")),
    "rtc_przech2018": ("Przech, S., Garg, A. X., Arnold, J. B., Barnieh, L., Cuerden, M. S., Dipchand, C., Feldman, L., Gill, J. S., "
                       "Karpinski, M., Knoll, G., Lok, C., Miller, M., Monroy, M., Nguan, C., Prasad, G. V. R., Sarma, S., Sontrop, J. M., "
                       "Storsley, L., &amp; Klarenbach, S. (2018). Financial costs incurred by living kidney donors: A prospective cohort "
                       "study. <em>Journal of the American Society of Nephrology, 29</em>(12), 2847&ndash;2857. "
                       + _doi("10.1681/ASN.2018040398")),
    "rtc_wiseman2017": ("Wiseman, J. F., Jacobs, C. L., Larson, D. B., Berglund, D. M., Garvey, C. A., Ibrahim, H. N., &amp; Matas, A. J. "
                        "(2017). Financial burden borne by laparoscopic living kidney donors. <em>Transplantation, 101</em>(9), "
                        "2253&ndash;2257. " + _doi("10.1097/TP.0000000000001568")),
    "rtc_barnieh2021": ("Barnieh, L., Arnold, J. B., Boudville, N., Cuerden, M. S., Dew, M. A., Dipchand, C., Feldman, L. S., Gill, J. S., "
                        "Karpinski, M., Klarenbach, S., Knoll, G., Lok, C., Miller, M., Monroy, M., Nguan, C., Prasad, G. V. R., Sontrop, J. M., "
                        "Storsley, L., &amp; Garg, A. X. (2021). Living kidney donors&rsquo; financial expenses and mental health. "
                        "<em>Transplantation, 105</em>(6), 1356&ndash;1364. " + _doi("10.1097/TP.0000000000003401")),
    "rtc_kdigo2020": ("Chadban, S. J., Ahn, C., Axelrod, D. A., Foster, B. J., Kasiske, B. L., Kher, V., Kumar, D., Oberbauer, R., Pascual, J., "
                      "Pilmore, H. L., Rodrigue, J. R., Segev, D. L., Sheerin, N. S., Tinckam, K. J., Wong, G., &amp; Knoll, G. A. (2020). "
                      "KDIGO clinical practice guideline on the evaluation and management of candidates for kidney transplantation. "
                      "<em>Transplantation, 104</em>(4S1 Suppl 1), S11&ndash;S103. " + _doi("10.1097/TP.0000000000003136")),
    "rtc_kdigo2017": ("Lentine, K. L., Kasiske, B. L., Levey, A. S., Adams, P. L., Alber&uacute;, J., Bakr, M. A., Gallon, L., Garvey, C. A., "
                      "Guleria, S., Li, P. K., Segev, D. L., Taler, S. J., Tanabe, K., Wright, L., Zeier, M. G., Cheung, M., &amp; Garg, A. X. "
                      "(2017). KDIGO clinical practice guideline on the evaluation and care of living kidney donors. <em>Transplantation, "
                      "101</em>(8S Suppl 1), S1&ndash;S109. " + _doi("10.1097/TP.0000000000001769")),
    "rtc_kdigo2009": ("Kidney Disease: Improving Global Outcomes Transplant Work Group. (2009). KDIGO clinical practice guideline for the "
                      "care of kidney transplant recipients. <em>American Journal of Transplantation, 9</em>(Suppl 3), S1&ndash;S155. "
                      + _doi("10.1111/j.1600-6143.2009.02834.x")),
    "rtc_istanbul2018": ("Muller, E., Dominguez-Gil, B., &amp; Martin, D. (2019). The Declaration of Istanbul on Organ Trafficking and "
                         "Transplant Tourism (2018 edition) introduction. <em>Transplantation, 103</em>(2), 217. "
                         + _doi("10.1097/TP.0000000000002541")),
    # ── Philippine law, regulation, and payer policy ──
    "rtc_doh2021": ("Department of Health. (2021). <em>Guidelines on ethical organ donation and transplantation from living donors</em> "
                    "(Administrative Order No. 2021-0059). " + _url("https://drive.google.com/file/d/1h1_yZ80SVrozcnLo4BvGgQhlDPzSn81f/view")),
    "rtc_doh2008": ("Department of Health. (2008). <em>Administrative Order No. 2008-0034 on the authorization of transplant facilities</em>. "
                    + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43997")),
    "rtc_doh2010a": ("Department of Health. (2010). <em>Administrative Order No. 2010-0018</em>. "
                     + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/52059")),
    "rtc_doh2010b": ("Department of Health. (2010). <em>Administrative Order No. 2010-0019 on deceased organ donation, including procurement "
                     "and clinical transplant coordinators</em>, as amended by Administrative Order No. 2010-0019-A. "
                     + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/52063")),
    "rtc_doh2023wait": ("Department of Health. (2023). <em>Department Memorandum No. 2023-0175</em> [National waiting list for organ "
                        "transplantation]. " + _url("https://sites.google.com/view/doh-hfdb/2023-updates/dm-2023-0175")),
    "rtc_doh2023annual": ("Department of Health. (2023). <em>Department Memorandum No. 2023-0209</em> [Annual reporting of transplant "
                          "facilities]. " + _url("https://sites.google.com/view/doh-hfdb/2023-updates/dm-2023-0209")),
    "rtc_doh2025transport": ("Department of Health. (2025). <em>Department Memorandum No. 2025-0031</em> [Organ transport]. "
                             + _url("https://sites.google.com/view/doh-hfdb/2025-q1-updates/dm-2025-0031")),
    "rtc_ra7170": ("Republic Act No. 7170. (1992). <em>Organ Donation Act of 1991</em>. "
                   + _url("https://elibrary.judiciary.gov.ph//thebookshelf//showdocs/2/2912")),
    "rtc_ra10364": ("Republic Act No. 10364. (2013). <em>Expanded Anti-Trafficking in Persons Act of 2012</em>, amending Republic Act "
                    "No. 9208; further amended by Republic Act No. 11862 (2022). "
                    + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/52337")),
    "rtc_ph2024": ("Philippine Health Insurance Corporation. (2024). <em>Z Benefits Package for Kidney Transplantation</em> (PhilHealth "
                   "Circular No. 2024-0035). " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0035.pdf")),
    "rtc_ph2026": ("Philippine Health Insurance Corporation. (2026). <em>Z Benefits Package for Kidney Transplantation (Revision 1)</em> "
                   "(PhilHealth Circular No. 2026-0019; published November 21, 2026). "
                   + _url("https://www.philhealth.gov.ph/circulars/2026/PC2026-0019.pdf")),
    "rtc_ph2026index": ("Philippine Health Insurance Corporation. (2026). <em>PhilHealth circulars 2026</em> [Index page]. Retrieved "
                        "November 25, 2026, from " + _url("https://www.philhealth.gov.ph/circulars/2026/")),
    "rtc_phsat": ("Philippine Health Insurance Corporation. (2025). <em>Self-assessment/survey tool for Z Benefit Package for kidney "
                  "transplant</em> (PHIC-ACCRE-ZBEN-SAT V.2025). "
                  + _url("https://www.philhealth.gov.ph/downloads/accreditation/SAT_KidneyTransplant_v2025.pdf")),
    "rtc_ph2015": ("Philippine Health Insurance Corporation. (2015). <em>PhilHealth Circular No. 014-2015</em> [Includes Annex B.1, "
                   "historical criteria for the transplant coordinator]. " + _url("https://www.philhealth.gov.ph/circulars/2015/circ014-2015.pdf")),
    "rtc_pa2026": ("Philippine Health Insurance Corporation. (2026). <em>Implementation of the Kidney Transplantation (KT) Data Registry "
                   "System</em> (PhilHealth Advisory No. 2026-0026). "
                   + _url("https://www.philhealth.gov.ph/advisories/2026/PA2026-0026.pdf")),
    "rtc_ph2025a": ("Philippine Health Insurance Corporation. (2025). <em>Z Benefits Package for Post-Kidney Transplantation Services in "
                    "Adults</em> (PhilHealth Circular No. 2025-0012). " + _url("https://www.philhealth.gov.ph/circulars/2025/PC2025-0012.pdf")),
    "rtc_ph2025c": ("Philippine Health Insurance Corporation. (2025). <em>Z Benefits Package for Post-Kidney Transplantation Services in "
                    "Children</em> (PhilHealth Circular No. 2025-0011). " + _url("https://www.philhealth.gov.ph/circulars/2025/PC2025-0011.pdf")),
    "rtc_ra10173": ("Republic Act No. 10173. (2012). <em>Data Privacy Act of 2012</em>. " + _url("https://privacy.gov.ph/data-privacy-act/")),
    "rtc_psn": ("Philippine Society of Nephrology. (n.d.). <em>Clinical practice guidelines and protocols</em>. Retrieved November 25, 2026, "
                "from " + _url("https://psn.org.ph/education/clinical-practice-guideline-and-protocols/")),
    "rtc_who2010": ("World Health Organization. (2010). <em>WHO guiding principles on human cell, tissue and organ transplantation</em>. "
                    + _url("https://www.who.int/publications/i/item/WHO-HTP-EHT-CPR-2010.01")),
    # ── international comparison ──
    "rtc_optn": ("Organ Procurement and Transplantation Network. (n.d.). <em>OPTN policies</em>. Health Resources and Services "
                 "Administration. " + _url("https://www.hrsa.gov/sites/default/files/hrsa/optn/optn_policies.pdf")),
    "rtc_abtc": ("American Board for Transplant Certification. (n.d.). <em>Certification examinations</em>. Retrieved November 25, 2026, "
                 "from " + _url("https://abtc.net/candidates/certification-examinations")),
    "rtc_hta": ("Human Tissue Authority. (n.d.). <em>Living organ donation: Legal framework</em>. Retrieved November 25, 2026, from "
                + _url("https://www.hta.gov.uk/guidance-professionals/guidance-sector/organ-donation-and-transplantation/living-organ-donation/living-organ-donation-legal-framework")),
}
