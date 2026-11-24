# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 23 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod/refs.py (kistler2018, kdigo_bpvol2020, daugirdas2015) are not repeated.
kdigo_dm2022 is defined by Module 22 and cited here without being redefined."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdoqi_nut2020": ("Ikizler, T. A., Burrowes, J. D., Byham-Gray, L. D., Campbell, K. L., Carrero, J. J., Chan, W., Fouque, D., "
                      "Friedman, A. N., Ghaddar, S., Goldstein-Fuchs, D. J., Kaysen, G. A., Kopple, J. D., Teta, D., Yee-Moon Wang, A., "
                      "&amp; Cuppari, L. (2020). KDOQI clinical practice guideline for nutrition in CKD: 2020 update. "
                      "<em>American Journal of Kidney Diseases, 76</em>(3, Suppl. 1), S1&ndash;S107. " + _doi("10.1053/j.ajkd.2020.05.006")),
    "fouque2008": ("Fouque, D., Kalantar-Zadeh, K., Kopple, J., Cano, N., Chauveau, P., Cuppari, L., Franch, H., Guarnieri, G., "
                   "Ikizler, T. A., Kaysen, G., Lindholm, B., Massy, Z., Mitch, W., Pineda, E., Stenvinkel, P., Trevi&ntilde;o-Becerra, A., "
                   "&amp; Wanner, C. (2008). A proposed nomenclature and diagnostic criteria for protein-energy wasting in acute and "
                   "chronic kidney disease. <em>Kidney International, 73</em>(4), 391&ndash;398. " + _doi("10.1038/sj.ki.5002585")),
    "carrero2018": ("Carrero, J. J., Thomas, F., Nagy, K., Arogundade, F., Avesani, C. M., Chan, M., Chmielewski, M., Cordeiro, A. C., "
                    "Espinosa-Cuevas, A., Fiaccadori, E., Guebre-Egziabher, F., Hand, R. K., Hung, A. M., Ikizler, T. A., Johansson, L. R., "
                    "Kalantar-Zadeh, K., Karupaiah, T., Lindholm, B., Marckmann, P., &hellip; Kovesdy, C. P. (2018). Global prevalence of "
                    "protein-energy wasting in kidney disease: A meta-analysis of contemporary observational studies from the International "
                    "Society of Renal Nutrition and Metabolism. <em>Journal of Renal Nutrition, 28</em>(6), 380&ndash;392. "
                    + _doi("10.1053/j.jrn.2018.08.006")),
    "kalantar2001": ("Kalantar-Zadeh, K., Kopple, J. D., Block, G., &amp; Humphreys, M. H. (2001). A malnutrition-inflammation score is "
                     "correlated with morbidity and mortality in maintenance hemodialysis patients. <em>American Journal of Kidney "
                     "Diseases, 38</em>(6), 1251&ndash;1263. " + _doi("10.1053/ajkd.2001.29222")),
    "hwang2019": ("Hwang, S. H., Lee, D. H., Min, J., &amp; Jeon, J. Y. (2019). Handgrip strength as a predictor of all-cause mortality "
                  "in patients with chronic kidney disease undergoing dialysis: A meta-analysis of prospective cohort studies. "
                  "<em>Journal of Renal Nutrition, 29</em>(6), 471&ndash;479. " + _doi("10.1053/j.jrn.2019.01.002")),
    "ikizler1994": ("Ikizler, T. A., Flakoll, P. J., Parker, R. A., &amp; Hakim, R. M. (1994). Amino acid and albumin losses during "
                    "hemodialysis. <em>Kidney International, 46</em>(3), 830&ndash;837. " + _doi("10.1038/ki.1994.339")),
    "depner1996": ("Depner, T. A., &amp; Daugirdas, J. T. (1996). Equations for normalized protein catabolic rate based on two-point "
                   "modeling of hemodialysis urea kinetics. <em>Journal of the American Society of Nephrology, 7</em>(5), 780&ndash;785. "
                   + _doi("10.1681/ASN.V75780")),
    "mah2020": ("Mah, J. Y., Choy, S. W., Roberts, M. A., Desai, A. M., Corken, M., Gwini, S. M., &amp; McMahon, L. P. (2020). Oral "
                "protein-based supplements versus placebo or no treatment for people with chronic kidney disease requiring dialysis. "
                "<em>Cochrane Database of Systematic Reviews, 2020</em>(5), Article CD012616. " + _doi("10.1002/14651858.CD012616.pub2")),
    "liu2023": ("Liu, P. J., Guo, J., Zhang, Y., Wang, F., &amp; Yu, K. (2023). Effects of oral nutritional supplements on the nutritional "
                "status and inflammatory markers in patients on maintenance dialysis: A systematic review and meta-analysis of "
                "randomized clinical trials. <em>Clinical Kidney Journal, 16</em>(11), 2271&ndash;2288. " + _doi("10.1093/ckj/sfad130")),
    "cano2007": ("Cano, N. J. M., Fouque, D., Roth, H., Aparicio, M., Azar, R., Canaud, B., Chauveau, P., Combe, C., Laville, M., "
                 "Leverve, X. M., &amp; French Study Group for Nutrition in Dialysis. (2007). Intradialytic parenteral nutrition does not "
                 "improve survival in malnourished hemodialysis patients: A 2-year multicenter, prospective, randomized study. "
                 "<em>Journal of the American Society of Nephrology, 18</em>(9), 2583&ndash;2591. " + _doi("10.1681/ASN.2007020184")),
    "sullivan2009": ("Sullivan, C., Sayre, S. S., Leon, J. B., Machekano, R., Love, T. E., Porter, D., Marbury, M., &amp; Sehgal, A. R. "
                     "(2009). Effect of food additives on hyperphosphatemia among patients with end-stage renal disease: A randomized "
                     "controlled trial. <em>JAMA, 301</em>(6), 629&ndash;635. " + _doi("10.1001/jama.2009.96")),
    "clase2020": ("Clase, C. M., Carrero, J. J., Ellison, D. H., Grams, M. E., Hemmelgarn, B. R., Jardine, M. J., Kovesdy, C. P., "
                  "Kline, G. A., Lindner, G., Obrador, G. T., Palmer, B. F., Cheung, M., Wheeler, D. C., Winkelmayer, W. C., "
                  "Pecoits-Filho, R., &amp; Conference Participants. (2020). Potassium homeostasis and management of dyskalemia in kidney "
                  "diseases: Conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. "
                  "<em>Kidney International, 97</em>(1), 42&ndash;61. " + _doi("10.1016/j.kint.2019.09.018")),
    "young2018": ("Young, H. M. L., March, D. S., Graham-Brown, M. P. M., Jones, A. W., Curtis, F., Grantham, C. S., Churchward, D. R., "
                  "Highton, P., Smith, A. C., Singh, S. J., Bridle, C., &amp; Burton, J. O. (2018). Effects of intradialytic cycling "
                  "exercise on exercise capacity, quality of life, physical function and cardiovascular measures in adult haemodialysis "
                  "patients: A systematic review and meta-analysis. <em>Nephrology Dialysis Transplantation, 33</em>(8), 1436&ndash;1445. "
                  + _doi("10.1093/ndt/gfy045")),
    "zhao2026": ("Zhao, S., Zhong, G., Lv, A., Tao, Y., Liu, H., Lv, H., Zhai, Z., Li, Y., Hua, Y., Kang, Y., Zhang, Y., Huang, M., "
                 "&amp; Ni, C. (2026). Intradialytic exercise interventions to enhance physical activity levels in hemodialysis patients: "
                 "A systematic review and meta-analysis. <em>American Journal of Nephrology, 57</em>(4), 441&ndash;460. "
                 + _doi("10.1159/000548114")),
}
