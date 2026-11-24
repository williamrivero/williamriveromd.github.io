# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 21 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Grades for KDIGO statements were read from the full guideline texts (KDIGO 2026 anemia,
Kidney International 109(1S); KDIGO 2017 CKD-MBD, Kidney International Supplements 7(1)).
Keys already defined in pod/refs.py (daugirdas2015, hall2021) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdigo_anemia2026": ("Babitt, J. L., Berns, J. S., Bozkurt, B., Cheung Khedairy, R. S., Cuevas, Y., Effa, E. E., Eisenga, M. F., Fishbane, S., "
                         "Ginzburg, Y. Z., Haase, V. H., Hedayati, S. S., Kim, S., Moura-Neto, J. A., Nagler, E. V., Rossignol, P., Sahay, M., "
                         "Tanaka, T., Wang, A. Y.-M., Wheeler, D. C., . . . Tonelli, M. (2026). Executive summary of the KDIGO 2026 clinical "
                         "practice guideline for the management of anemia in chronic kidney disease (CKD). <em>Kidney International, 109</em>(1), "
                         "44&ndash;56. " + _doi("10.1016/j.kint.2025.06.005")),
    "kdigo_anemia2026gl": ("Kidney Disease: Improving Global Outcomes (KDIGO) Anemia Work Group. (2026). KDIGO 2026 clinical practice guideline "
                           "for the management of anemia in chronic kidney disease (CKD). <em>Kidney International, 109</em>(1S), S1&ndash;S99. "
                           + _doi("10.1016/j.kint.2025.06.006")),
    "macdougall2019": ("Macdougall, I. C., White, C., Anker, S. D., Bhandari, S., Farrington, K., Kalra, P. A., McMurray, J. J. V., Murray, H., "
                       "Tomson, C. R. V., Wheeler, D. C., Winearls, C. G., Ford, I., &amp; PIVOTAL Investigators and Committees. (2019). "
                       "Intravenous iron in patients undergoing maintenance hemodialysis. <em>New England Journal of Medicine, 380</em>(5), "
                       "447&ndash;458. " + _doi("10.1056/NEJMoa1810742")),
    "singh2021": ("Singh, A. K., Carroll, K., Perkovic, V., Solomon, S., Jha, V., Johansen, K. L., Lopes, R. D., Macdougall, I. C., Obrador, G. T., "
                  "Waikar, S. S., Wanner, C., Wheeler, D. C., Wi&#281;cek, A., Blackorby, A., Cizman, B., Cobitz, A. R., Davies, R., Dole, J., "
                  "Kler, L., . . . ASCEND-D Study Group. (2021). Daprodustat for the treatment of anemia in patients undergoing dialysis. "
                  "<em>New England Journal of Medicine, 385</em>(25), 2325&ndash;2335. " + _doi("10.1056/NEJMoa2113379")),
    "eckardt2021": ("Eckardt, K.-U., Agarwal, R., Aswad, A., Awad, A., Block, G. A., Bacci, M. R., Farag, Y. M. K., Fishbane, S., Hubert, H., "
                    "Jardine, A., Khawaja, Z., Koury, M. J., Maroni, B. J., Matsushita, K., McCullough, P. A., Lewis, E. F., Luo, W., "
                    "Parfrey, P. S., Pergola, P., . . . Chertow, G. M. (2021). Safety and efficacy of vadadustat for anemia in patients "
                    "undergoing dialysis. <em>New England Journal of Medicine, 384</em>(17), 1601&ndash;1612. " + _doi("10.1056/NEJMoa2025956")),
    "chen2019": ("Chen, N., Hao, C., Liu, B.-C., Lin, H., Wang, C., Xing, C., Liang, X., Jiang, G., Liu, Z., Li, X., Zuo, L., Luo, L., Wang, J., "
                 "Zhao, M.-H., Liu, Z., Cai, G.-Y., Hao, L., Leong, R., Wang, C., . . . Yu, K. P. (2019). Roxadustat treatment for anemia in "
                 "patients undergoing long-term dialysis. <em>New England Journal of Medicine, 381</em>(11), 1011&ndash;1022. "
                 + _doi("10.1056/NEJMoa1901713")),
    "besarab1998": ("Besarab, A., Bolton, W. K., Browne, J. K., Egrie, J. C., Nissenson, A. R., Okamoto, D. M., Schwab, S. J., &amp; "
                    "Goodkin, D. A. (1998). The effects of normal as compared with low hematocrit values in patients with cardiac disease who "
                    "are receiving hemodialysis and epoetin. <em>New England Journal of Medicine, 339</em>(9), 584&ndash;590. "
                    + _doi("10.1056/NEJM199808273390903")),
    "singh2006": ("Singh, A. K., Szczech, L., Tang, K. L., Barnhart, H., Sapp, S., Wolfson, M., Reddan, D., &amp; CHOIR Investigators. (2006). "
                  "Correction of anemia with epoetin alfa in chronic kidney disease. <em>New England Journal of Medicine, 355</em>(20), "
                  "2085&ndash;2098. " + _doi("10.1056/NEJMoa065485")),
    "pfeffer2009": ("Pfeffer, M. A., Burdmann, E. A., Chen, C.-Y., Cooper, M. E., de Zeeuw, D., Eckardt, K.-U., Feyzi, J. M., Ivanovich, P., "
                    "Kewalramani, R., Levey, A. S., Lewis, E. F., McGill, J. B., McMurray, J. J. V., Parfrey, P., Parving, H.-H., Remuzzi, G., "
                    "Singh, A. K., Solomon, S. D., Toto, R., &amp; TREAT Investigators. (2009). A trial of darbepoetin alfa in type 2 diabetes "
                    "and chronic kidney disease. <em>New England Journal of Medicine, 361</em>(21), 2019&ndash;2032. "
                    + _doi("10.1056/NEJMoa0907845")),
    "hung2014": ("Hung, S.-Y., Lin, T.-M., Chang, M.-Y., Wang, H.-H., Lee, Y.-C., Ho, L.-C., Chen, Y.-T., Hung, C.-M., &amp; Liou, H.-H. (2014). "
                 "Risk factors of sensitization to human leukocyte antigen in end-stage renal disease patients. <em>Human Immunology, 75</em>(6), "
                 "531&ndash;535. " + _doi("10.1016/j.humimm.2014.02.024")),
    "kdigo_mbd2017": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD-MBD Update Work Group. (2017). KDIGO 2017 clinical practice "
                      "guideline update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease&ndash;mineral and bone "
                      "disorder (CKD-MBD). <em>Kidney International Supplements, 7</em>(1), 1&ndash;59. " + _doi("10.1016/j.kisu.2017.04.001")),
    "ketteler2017": ("Ketteler, M., Block, G. A., Evenepoel, P., Fukagawa, M., Herzog, C. A., McCann, L., Moe, S. M., Shroff, R., Tonelli, M. A., "
                     "Toussaint, N. D., Vervloet, M. G., &amp; Leonard, M. B. (2017). Executive summary of the 2017 KDIGO Chronic Kidney "
                     "Disease&ndash;Mineral and Bone Disorder (CKD-MBD) Guideline Update: What&rsquo;s changed and why it matters. "
                     "<em>Kidney International, 92</em>(1), 26&ndash;36. " + _doi("10.1016/j.kint.2017.04.006")),
    "jamal2013": ("Jamal, S. A., Vandermeer, B., Raggi, P., Mendelssohn, D. C., Chatterley, T., Dorgan, M., Lok, C. E., Fitchett, D., &amp; "
                  "Tsuyuki, R. T. (2013). Effect of calcium-based versus non-calcium-based phosphate binders on mortality in patients with "
                  "chronic kidney disease: An updated systematic review and meta-analysis. <em>The Lancet, 382</em>(9900), 1268&ndash;1277. "
                  + _doi("10.1016/S0140-6736(13)60897-1")),
    "edmonston2025": ("Edmonston, D., Isakova, T., Dember, L. M., Waymyers, S., Andersen, D., Chan, K. E., Chakraborty, H., &amp; Wolf, M. (2025). "
                      "Higher versus lower phosphate targets for patients undergoing in-center hemodialysis: A randomized controlled trial. "
                      "<em>Journal of the American Society of Nephrology, 36</em>(12), 2445&ndash;2455. " + _doi("10.1681/ASN.0000000765")),
    "chertow2012": ("EVOLVE Trial Investigators, Chertow, G. M., Block, G. A., Correa-Rotter, R., Dr&uuml;eke, T. B., Floege, J., Goodman, W. G., "
                    "Herzog, C. A., Kubo, Y., London, G. M., Mahaffey, K. W., Mix, T. C., Moe, S. M., Trotman, M. L., Wheeler, D. C., &amp; "
                    "Parfrey, P. S. (2012). Effect of cinacalcet on cardiovascular disease in patients undergoing dialysis. <em>New England "
                    "Journal of Medicine, 367</em>(26), 2482&ndash;2494. " + _doi("10.1056/NEJMoa1205624")),
    "block2017": ("Block, G. A., Bushinsky, D. A., Cheng, S., Cunningham, J., Dehmel, B., Drueke, T. B., Ketteler, M., Kewalramani, R., "
                  "Martin, K. J., Moe, S. M., Patel, U. D., Silver, J., Sun, Y., Wang, H., &amp; Chertow, G. M. (2017). Effect of etelcalcetide "
                  "vs cinacalcet on serum parathyroid hormone in patients receiving hemodialysis with secondary hyperparathyroidism: A randomized "
                  "clinical trial. <em>JAMA, 317</em>(2), 156&ndash;164. " + _doi("10.1001/jama.2016.19468")),
    "chewcharat2025": ("Chewcharat, A., &amp; Nigwekar, S. U. (2025). Ten tips on how to deal with calciphylaxis patients. <em>Clinical Kidney "
                       "Journal, 18</em>(4), Article sfaf098. " + _doi("10.1093/ckj/sfaf098")),
}
