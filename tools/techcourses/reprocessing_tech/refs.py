# -*- coding: utf-8 -*-
"""References for the Dialyzer Reprocessing Technician track (APA 7). Merged into SHARED.REFS by generate_tech_courses.py.
Journal entries were checked against PubMed on November 25, 2026; issuances against the issuing body's site or the
v0.1 source register (accessed November 25, 2026). Shared keys used as well: doh2012, doh_water, psn2024, aami_reuse,
iso23500_1, iso23500_3, iso23500_5, cdc_dialysis, cdc_water."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    # ── Issuances and standards ──
    "rt_phic0023": ("Philippine Health Insurance Corporation (PhilHealth). (2024). <em>PhilHealth Circular No. 2024-0023</em> "
                    "[Hemodialysis benefit package]. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "rt_phic0029": ("Philippine Health Insurance Corporation (PhilHealth). (2024). <em>PhilHealth Circular No. 2024-0029</em> "
                    "[Quality standards for hemodialysis facilities]. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "rt_cfr494": ("Centers for Medicare &amp; Medicaid Services (CMS). (2025). <em>42 CFR Part 494: Conditions for coverage for end-stage renal disease facilities</em> "
                  "(&sect;&sect; 494.50, 494.140). " + _url("https://www.govinfo.gov/content/pkg/CFR-2025-title42-vol5/xhtml/CFR-2025-title42-vol5-part494.html")),
    "rt_cms_somh": ("Centers for Medicare &amp; Medicaid Services (CMS). (2026). <em>State operations manual, Appendix H: Guidance to surveyors, end stage renal disease facilities</em> "
                    "(rev. August 17, 2026). " + _url("https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/som107ap_h_esrd.pdf")),
    "rt_my2026": ("Ministry of Health Malaysia. (2026). <em>National haemodialysis quality standards</em> (3rd ed.). "
                  + _url("https://www.moh.gov.my/images/04-penerbitan/penerbitan-klinikal/perkhidmatan-perubatan/National_Haemodialysis_Standards_2026_3rd_Edition.pdf")),
    "rt_fda_restart": ("U.S. Food and Drug Administration (FDA). (n.d.). <em>Reopening dialysis clinics after restoration of power and water</em>. "
                       + _url("https://www.fda.gov/medical-devices/emergency-situations-medical-devices/reopening-dialysis-clinics-after-restoration-power-and-water")),
    "rt_cdc2001": ("Centers for Disease Control and Prevention. (2001). Recommendations for preventing transmission of infections among chronic hemodialysis patients. "
                   "<em>MMWR Recommendations and Reports, 50</em>(RR-5), 1&ndash;43."),
    # ── Outcome and performance studies ──
    "rt_galvao2012": ("Galvao, T. F., Silva, M. T., Araujo, M. E., Bulbol, W. S., &amp; Cardoso, A. L. (2012). Dialyzer reuse and mortality risk in patients with "
                      "end-stage renal disease: A systematic review. <em>American Journal of Nephrology, 35</em>(3), 249&ndash;258. " + _doi("10.1159/000336532")),
    "rt_lacson2011": ("Lacson, E., Jr., Wang, W., Mooney, A., Ofsthun, N., Lazarus, J. M., &amp; Hakim, R. M. (2011). Abandoning peracetic acid-based dialyzer reuse "
                      "is associated with improved survival. <em>Clinical Journal of the American Society of Nephrology, 6</em>(2), 297&ndash;302. " + _doi("10.2215/CJN.03160410")),
    "rt_bond2011": ("Bond, T. C., Nissenson, A. R., Krishnan, M., Wilson, S. M., &amp; Mayne, T. (2011). Dialyzer reuse with peracetic acid does not impact patient "
                    "mortality. <em>Clinical Journal of the American Society of Nephrology, 6</em>(6), 1368&ndash;1374. " + _doi("10.2215/CJN.10391110")),
    "rt_argyropoulos2015": ("Argyropoulos, C., Roumelioti, M.-E., Sattar, A., Kellum, J. A., Weissfeld, L., &amp; Unruh, M. L. (2015). Dialyzer reuse and outcomes "
                            "of high flux dialysis. <em>PLoS ONE, 10</em>(6), e0129575. " + _doi("10.1371/journal.pone.0129575")),
    "rt_cheung1999": ("Cheung, A. K., Agodoa, L. Y., Daugirdas, J. T., Depner, T. A., Gotch, F. A., Greene, T., Levin, N. W., &amp; Leypoldt, J. K. (1999). "
                      "Effects of hemodialyzer reuse on clearances of urea and beta2-microglobulin. <em>Journal of the American Society of Nephrology, 10</em>(1), "
                      "117&ndash;127. " + _doi("10.1681/ASN.V101117")),
    "rt_kerr1994": ("Kerr, P. G., Mattingly, S., Lo, A., &amp; Atkins, R. C. (1994). The adequacy of Fragmin as a single bolus dose with reused dialyzers. "
                    "<em>Artificial Organs, 18</em>(6), 416&ndash;419. " + _doi("10.1111/j.1525-1594.1994.tb02226.x")),
    "rt_wei1994": ("Wei, S. S., Ellis, P. W., Magnusson, M. O., &amp; Paganini, E. P. (1994). Effect of heparin modeling on delivered hemodialysis therapy. "
                   "<em>American Journal of Kidney Diseases, 23</em>(3), 389&ndash;393. " + _doi("10.1016/s0272-6386(12)81001-8")),
    "rt_prapunwatana2025": ("Prapunwatana, P., Thongsricome, T., Leelahavanichkul, A., Injan, P., Chariyavilaskul, P., Susantitaphong, P., Avihingsanon, Y., "
                            "Eiam-Ong, S., &amp; Tiranathanagul, K. (2025). Plausibility of super high-flux dialyzer reuse in maintenance hemodialysis. "
                            "<em>Frontiers in Medicine, 12</em>, 1655099. " + _doi("10.3389/fmed.2025.1655099")),
    "rt_robinson2005": ("Robinson, B. M., &amp; Feldman, H. I. (2005). Dialyzer reuse and patient outcomes: What do we know now? <em>Seminars in Dialysis, 18</em>(3), "
                        "175&ndash;179. " + _doi("10.1111/j.1525-139X.2005.18303.x")),
    "rt_upadhyay2019": ("Upadhyay, A. (2019). Dialyzer reuse: Is it safe and worth it? <em>Jornal Brasileiro de Nefrologia, 41</em>(3), 312&ndash;314. "
                        + _doi("10.1590/2175-8239-JBN-2019-0134")),
    "rt_slyby2000": ("Slyby, T., Huff, G., &amp; Henger, M. J. (2000). Dialyzer reprocessing: Improved treatment quality and increased dialyzer reuse using a team "
                     "approach. <em>Nephrology Nursing Journal, 27</em>(5), 483&ndash;488."),
    # ── Outbreaks and infection ──
    "rt_beck1990": ("Beck-Sague, C. M., Jarvis, W. R., Bland, L. A., Arduino, M. J., Aguero, S. M., &amp; Verosic, G. (1990). Outbreak of gram-negative bacteremia "
                    "and pyrogenic reactions in a hemodialysis center. <em>American Journal of Nephrology, 10</em>(5), 397&ndash;403. " + _doi("10.1159/000168155")),
    "rt_jackson1994": ("Jackson, B. M., Beck-Sague, C. M., Bland, L. A., Arduino, M. J., Meyer, L., &amp; Jarvis, W. R. (1994). Outbreak of pyrogenic reactions and "
                       "gram-negative bacteremia in a hemodialysis center. <em>American Journal of Nephrology, 14</em>(2), 85&ndash;89. " + _doi("10.1159/000168694")),
    "rt_gordon1992": ("Gordon, S. M., Oettinger, C. W., Bland, L. A., Oliver, J. C., Arduino, M. J., Aguero, S. M., McAllister, S. K., Favero, M. S., &amp; Jarvis, W. R. (1992). "
                      "Pyrogenic reactions in patients receiving conventional, high-efficiency, or high-flux hemodialysis treatments with bicarbonate dialysate "
                      "containing high concentrations of bacteria and endotoxin. <em>Journal of the American Society of Nephrology, 2</em>(9), 1436&ndash;1444. "
                      + _doi("10.1681/ASN.V291436")),
    "rt_archibald2006": ("Archibald, L. K., Khoi, N. N., Jarvis, W. R., Reller, L. B., Cam, P. D., Thu, T. A., &amp; Hung, N. V. (2006). Pyrogenic reactions in "
                         "hemodialysis patients, Hanoi, Vietnam. <em>Infection Control and Hospital Epidemiology, 27</em>(4), 424&ndash;426. " + _doi("10.1086/503347")),
    "rt_roth2000": ("Roth, V. R., &amp; Jarvis, W. R. (2000). Outbreaks of infection and/or pyrogenic reactions in dialysis patients. <em>Seminars in Dialysis, 13</em>(2), "
                    "92&ndash;96. " + _doi("10.1046/j.1525-139x.2000.00027.x")),
    "rt_duong2016": ("Duong, C. M., &amp; McLaws, M.-L. (2016). An investigation of an outbreak of hepatitis C virus infections in a low-resourced hemodialysis unit "
                     "in Vietnam. <em>American Journal of Infection Control, 44</em>(5), 560&ndash;566. " + _doi("10.1016/j.ajic.2016.01.014")),
    "rt_heikens2019": ("Heikens, E., Hetem, D. J., Jousma-Rutjes, J. P. W., Nijhuis, W., Boland, G. J., Hommes, N. H., Thang, O. H. D., &amp; Schuurman, R. (2019). "
                       "Hepatitis C virus transmission in a Dutch haemodialysis unit: Detailed outbreak investigation using NS5A gene sequencing. "
                       "<em>Journal of Hospital Infection, 101</em>(3), 333&ndash;338. " + _doi("10.1016/j.jhin.2018.11.015")),
    "rt_jochimsen1998": ("Jochimsen, E. M., Carmichael, W. W., An, J. S., Cardo, D. M., Cookson, S. T., Holmes, C. E., Antunes, M. B., de Melo Filho, D. A., Lyra, T. M., "
                         "Barreto, V. S., Azevedo, S. M., &amp; Jarvis, W. R. (1998). Liver failure and death after exposure to microcystins at a hemodialysis center "
                         "in Brazil. <em>New England Journal of Medicine, 338</em>(13), 873&ndash;878. " + _doi("10.1056/NEJM199803263381304")),
    # ── Occupational and environmental ──
    "rt_casey2017": ("Casey, M. L., Hawley, B., Edwards, N., Cox-Ganser, J. M., &amp; Cummings, K. J. (2017). Health problems and disinfectant product exposure among "
                     "staff at a large multispecialty hospital. <em>American Journal of Infection Control, 45</em>(10), 1133&ndash;1138. " + _doi("10.1016/j.ajic.2017.04.003")),
    "rt_hawley2017": ("Hawley, B., Casey, M., Virji, M. A., Cummings, K. J., Johnson, A., &amp; Cox-Ganser, J. (2017). Respiratory symptoms in hospital cleaning staff "
                      "exposed to a product containing hydrogen peroxide, peracetic acid, and acetic acid. <em>Annals of Work Exposures and Health, 62</em>(1), "
                      "28&ndash;40. " + _doi("10.1093/annweh/wxx087")),
    "rt_barraclough2020": ("Barraclough, K. A., &amp; Agar, J. W. M. (2020). Green nephrology. <em>Nature Reviews Nephrology, 16</em>(5), 257&ndash;268. "
                           + _doi("10.1038/s41581-019-0245-1")),
}
