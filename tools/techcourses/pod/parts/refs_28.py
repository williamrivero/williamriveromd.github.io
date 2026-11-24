# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 28 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in the course (daugirdas2015, kdoqi_va2019, cdc2001) are not repeated.
Module 28 owns ghafur2007; Module 29 reuses it."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "palamuthusingam2020": ("Palamuthusingam, D., Nadarajah, A., Pascoe, E. M., Craig, J., Johnson, D. W., Hawley, C. M., &amp; Fahim, M. (2020). "
                            "Postoperative mortality in patients on chronic dialysis following elective surgery: A systematic review and "
                            "meta-analysis. <em>PLoS ONE, 15</em>(6), e0234402. " + _doi("10.1371/journal.pone.0234402")),
    "fieldingsingh2022": ("Fielding-Singh, V., Vanneman, M. W., Grogan, T., Neelankavil, J. P., Winkelmayer, W. C., Chang, T. I., Liu, V. X., &amp; "
                          "Lin, E. (2022). Association between preoperative hemodialysis timing and postoperative mortality in patients with "
                          "end-stage kidney disease. <em>JAMA, 328</em>(18), 1837&ndash;1848. " + _doi("10.1001/jama.2022.19626")),
    "lee1999": ("Lee, T. H., Marcantonio, E. R., Mangione, C. M., Thomas, E. J., Polanczyk, C. A., Cook, E. F., Sugarbaker, D. J., Donaldson, M. C., "
                "Poss, R., Ho, K. K., Ludwig, L. E., Pedan, A., &amp; Goldman, L. (1999). Derivation and prospective validation of a simple index "
                "for prediction of cardiac risk of major noncardiac surgery. <em>Circulation, 100</em>(10), 1043&ndash;1049. "
                + _doi("10.1161/01.cir.100.10.1043")),
    "acc_aha_periop2024": ("Thompson, A., Fleischmann, K. E., Smilowitz, N. R., de las Fuentes, L., Mukherjee, D., Aggarwal, N. R., Ahmad, F. S., "
                           "Allen, R. B., Altin, S. E., Auerbach, A., Berger, J. S., Chow, B., Dakik, H. A., Eisenstein, E. L., Gerhard-Herman, M., "
                           "Ghadimi, K., Kachulis, B., Leclerc, J., Lee, C. S., . . . Williams, K. A. (2024). 2024 AHA/ACC/ACS/ASNC/HRS/SCA/SCCT/"
                           "SCMR/SVM guideline for perioperative cardiovascular management for noncardiac surgery: A report of the American "
                           "College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. "
                           "<em>Circulation, 150</em>(19), e351&ndash;e442. " + _doi("10.1161/CIR.0000000000001285")),
    "acr_nkf_iodinated2020": ("Davenport, M. S., Perazella, M. A., Yee, J., Dillman, J. R., Fine, D., McDonald, R. J., Rodby, R. A., Wang, C. L., "
                              "&amp; Weinreb, J. C. (2020). Use of intravenous iodinated contrast media in patients with kidney disease: "
                              "Consensus statements from the American College of Radiology and the National Kidney Foundation. "
                              "<em>Radiology, 294</em>(3), 660&ndash;668. " + _doi("10.1148/radiol.2019192094")),
    "acr_nkf_gbcm2021": ("Weinreb, J. C., Rodby, R. A., Yee, J., Wang, C. L., Fine, D., McDonald, R. J., Perazella, M. A., Dillman, J. R., &amp; "
                         "Davenport, M. S. (2021). Use of intravenous gadolinium-based contrast media in patients with kidney disease: "
                         "Consensus statements from the American College of Radiology and the National Kidney Foundation. "
                         "<em>Radiology, 298</em>(1), 28&ndash;35. " + _doi("10.1148/radiol.2020202903")),
    "oloko2020": ("Oloko, A., Talreja, H., Davis, A., McCormick, B., Clark, E., Akbari, A., Kong, J., &amp; Hiremath, S. (2020). Does iodinated "
                  "contrast affect residual renal function in dialysis patients? A systematic review and meta-analysis. "
                  "<em>Nephron, 144</em>(4), 176&ndash;184. " + _doi("10.1159/000505576")),
    "ninan2022": ("Ninan, J., Reddy, S., &amp; Qureshi, F. (2022). Things we do for no reason: Emergent hemodialysis after intravascular "
                  "iodinated contrast exposure in chronic hemodialysis patients. <em>Journal of Hospital Medicine, 17</em>(8), "
                  "653&ndash;656. " + _doi("10.12788/jhm.3683")),
    "elters2012": ("El Ters, M., Schears, G. J., Taler, S. J., Williams, A. W., Albright, R. C., Jenson, B. M., Mahon, A. L., Stockland, A. H., "
                   "Misra, S., Nyberg, S. L., Rule, A. D., &amp; Hogan, M. C. (2012). Association between prior peripherally inserted central "
                   "catheters and lack of functioning arteriovenous fistulas: A case-control study in hemodialysis patients. "
                   "<em>American Journal of Kidney Diseases, 60</em>(4), 601&ndash;608. " + _doi("10.1053/j.ajkd.2012.05.007")),
    "erickson2014": ("Erickson, K. F., Winkelmayer, W. C., Chertow, G. M., &amp; Bhattacharya, J. (2014). Physician visits and 30-day hospital "
                     "readmissions in patients receiving hemodialysis. <em>Journal of the American Society of Nephrology, 25</em>(9), "
                     "2079&ndash;2087. " + _doi("10.1681/ASN.2013080879")),
    "ghafur2007": ("Ghafur, A., Raza, M., Labbett, W., Chawla, A., Smith, C., Ngui, S. L., Davenport, A., &amp; Geretti, A. M. (2007). "
                   "Travel-associated acquisition of hepatitis C virus infection in patients receiving haemodialysis. "
                   "<em>Nephrology Dialysis Transplantation, 22</em>(9), 2640&ndash;2644. " + _doi("10.1093/ndt/gfm202")),
    "bhattacharya2009": ("Bhattacharya, S., Price, N., Boxall, E., Adu, D., Lipkin, G., Smith, S., &amp; Osman, H. (2009). Holiday haemodialysis "
                         "and imported hepatitis C virus infection: A series of sixteen cases in two large haemodialysis units. "
                         "<em>Journal of Clinical Virology, 45</em>(4), 296&ndash;299. " + _doi("10.1016/j.jcv.2009.04.007")),
}
