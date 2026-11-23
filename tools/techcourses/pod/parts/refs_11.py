# -*- coding: utf-8 -*-
"""References added for Physician on Duty Module 11 (APA 7). Keys are cited in module text as [[key]].
Each entry was checked against PubMed metadata (and, for cdc2001, the CDC MMWR page) on November 23, 2026."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "torino2016": ("Torino, C., Gargani, L., Sicari, R., Letachowicz, K., Ekart, R., Fliser, D., Covic, A., Siamopoulos, K., Stavroulopoulos, A., "
                   "Massy, Z. A., Fiaccadori, E., Caiazza, A., Bachelet, T., Slotki, I., Martinez-Castelao, A., Coudert-Krier, M.-J., Rossignol, P., "
                   "Gueler, F., Hannedouche, T., . . . Zoccali, C. (2016). The agreement between auscultation and lung ultrasound in hemodialysis "
                   "patients: The LUST study. <em>Clinical Journal of the American Society of Nephrology, 11</em>(11), 2005&ndash;2011. "
                   + _doi("10.2215/CJN.03890416")),
    "alsolaiman2011": ("Al-Solaiman, Y., Estrada, E., &amp; Allon, M. (2011). The spectrum of infections in catheter-dependent hemodialysis patients. "
                       "<em>Clinical Journal of the American Society of Nephrology, 6</em>(9), 2247&ndash;2252. " + _doi("10.2215/CJN.03900411")),
    "rayner2014": ("Rayner, H. C., Zepel, L., Fuller, D. S., Morgenstern, H., Karaboyas, A., Culleton, B. F., Mapes, D. L., Lopes, A. A., "
                   "Gillespie, B. W., Hasegawa, T., Saran, R., Tentori, F., Hecking, M., Pisoni, R. L., &amp; Robinson, B. M. (2014). Recovery time, "
                   "quality of life, and mortality in hemodialysis patients: The Dialysis Outcomes and Practice Patterns Study (DOPPS). "
                   "<em>American Journal of Kidney Diseases, 64</em>(1), 86&ndash;94. " + _doi("10.1053/j.ajkd.2014.01.014")),
    "saran2003": ("Saran, R., Bragg-Gresham, J. L., Rayner, H. C., Goodkin, D. A., Keen, M. L., Van Dijk, P. C., Kurokawa, K., Piera, L., Saito, A., "
                  "Fukuhara, S., Young, E. W., Held, P. J., &amp; Port, F. K. (2003). Nonadherence in hemodialysis: Associations with mortality, "
                  "hospitalization, and practice patterns in the DOPPS. <em>Kidney International, 64</em>(1), 254&ndash;262. "
                  + _doi("10.1046/j.1523-1755.2003.00064.x")),
    "alsalmi2018": ("Al Salmi, I., Larkina, M., Wang, M., Subramanian, L., Morgenstern, H., Jacobson, S. H., Hakim, R., Tentori, F., Saran, R., "
                    "Akiba, T., Tomilina, N. A., Port, F. K., Robinson, B. M., &amp; Pisoni, R. L. (2018). Missed hemodialysis treatments: "
                    "International variation, predictors, and outcomes in the Dialysis Outcomes and Practice Patterns Study (DOPPS). "
                    "<em>American Journal of Kidney Diseases, 72</em>(5), 634&ndash;643. " + _doi("10.1053/j.ajkd.2018.04.019")),
    "chan2014": ("Chan, K. E., Thadhani, R. I., &amp; Maddux, F. W. (2014). Adherence barriers to chronic dialysis in the United States. "
                 "<em>Journal of the American Society of Nephrology, 25</em>(11), 2642&ndash;2648. " + _doi("10.1681/ASN.2013111160")),
    "cdc2001": ("Centers for Disease Control and Prevention. (2001). Recommendations for preventing transmission of infections among chronic "
                "hemodialysis patients. <em>MMWR Recommendations and Reports, 50</em>(RR-5), 1&ndash;43. "
                '<a href="https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm">https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm</a>'),
    "gordon2019": ("Gordon, C. E., Berenguer, M. C., Doss, W., Fabrizi, F., Izopet, J., Jha, V., Kamar, N., Kasiske, B. L., Lai, C.-L., "
                   "Morales, J. M., Patel, P. R., Pol, S., Silva, M. O., Balk, E. M., Earley, A., Di, M., Cheung, M., Jadoul, M., &amp; Martin, P. (2019). "
                   "Prevention, diagnosis, evaluation, and treatment of hepatitis C virus infection in chronic kidney disease: Synopsis of the "
                   "Kidney Disease: Improving Global Outcomes 2018 clinical practice guideline. <em>Annals of Internal Medicine, 171</em>(7), "
                   "496&ndash;504. " + _doi("10.7326/M19-1539")),
    "shoji2004": ("Shoji, T., Tsubakihara, Y., Fujii, M., &amp; Imai, E. (2004). Hemodialysis-associated hypotension as an independent risk factor "
                  "for two-year mortality in hemodialysis patients. <em>Kidney International, 66</em>(3), 1212&ndash;1220. "
                  + _doi("10.1111/j.1523-1755.2004.00812.x")),
    "lok2020": ("Lok, C. E., Huber, T. S., Lee, T., Shenoy, S., Yevzlin, A. S., Abreo, K., Allon, M., Asif, A., Astor, B. C., Glickman, M. H., "
                "Graham, J., Moist, L. M., Rajan, D. K., Roberts, C., Vachharajani, T. J., &amp; Valentini, R. P. (2020). KDOQI clinical practice "
                "guideline for vascular access: 2019 update. <em>American Journal of Kidney Diseases, 75</em>(4, Suppl. 2), S1&ndash;S164. "
                + _doi("10.1053/j.ajkd.2019.12.001")),
}
