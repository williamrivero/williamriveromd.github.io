# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 25 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. The UK pregnancy guideline grades were checked against the guideline text (PMC6822421).
Keys already defined in pod/refs.py (daugirdas2015) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "johansen2007": ("Johansen, K. L., Chertow, G. M., Jin, C., &amp; Kutner, N. G. (2007). Significance of frailty among dialysis patients. "
                     "<em>Journal of the American Society of Nephrology, 18</em>(11), 2960&ndash;2967. " + _doi("10.1681/ASN.2007020221")),
    "zhao2020": ("Zhao, Y., Liu, Q., &amp; Ji, J. (2020). The prevalence of frailty in patients on hemodialysis: A systematic review and "
                 "meta-analysis. <em>International Urology and Nephrology, 52</em>(1), 115&ndash;120. " + _doi("10.1007/s11255-019-02310-2")),
    "cheng2024": ("Cheng, M., He, M., Ning, L., Gan, H., Liu, H., Liu, Q., Shi, F., Luo, Y., &amp; Zeng, Z. (2024). Association between frailty "
                  "and adverse outcomes in patients undergoing maintenance hemodialysis: A systematic review and meta-analysis. "
                  "<em>Renal Failure, 46</em>(2), Article 2367716. " + _doi("10.1080/0886022X.2024.2367716")),
    "rockwood2005": ("Rockwood, K., Song, X., MacKnight, C., Bergman, H., Hogan, D. B., McDowell, I., &amp; Mitnitski, A. (2005). A global "
                     "clinical measure of fitness and frailty in elderly people. <em>CMAJ, 173</em>(5), 489&ndash;495. " + _doi("10.1503/cmaj.050051")),
    "alfaadhel2015": ("Alfaadhel, T. A., Soroka, S. D., Kiberd, B. A., Landry, D., Moorhouse, P., &amp; Tennankore, K. K. (2015). Frailty and "
                      "mortality in dialysis: Evaluation of a clinical frailty scale. <em>Clinical Journal of the American Society of Nephrology, "
                      "10</em>(5), 832&ndash;840. " + _doi("10.2215/CJN.07760814")),
    "murray2006": ("Murray, A. M., Tupper, D. E., Knopman, D. S., Gilbertson, D. T., Pederson, S. L., Li, S., Smith, G. E., Hochhalter, A. K., "
                   "Collins, A. J., &amp; Kane, R. L. (2006). Cognitive impairment in hemodialysis patients is common. <em>Neurology, 67</em>(2), "
                   "216&ndash;223. " + _doi("10.1212/01.wnl.0000225182.15532.40")),
    "chiu2009": ("Chiu, Y.-W., Teitelbaum, I., Misra, M., de Leon, E. M., Adzize, T., &amp; Mehrotra, R. (2009). Pill burden, adherence, "
                 "hyperphosphatemia, and quality of life in maintenance dialysis patients. <em>Clinical Journal of the American Society of "
                 "Nephrology, 4</em>(6), 1089&ndash;1096. " + _doi("10.2215/CJN.00290109")),
    "davison2015": ("Davison, S. N., Levin, A., Moss, A. H., Jha, V., Brown, E. A., Brennan, F., Murtagh, F. E. M., Naicker, S., Germain, M. J., "
                    "O&rsquo;Donoghue, D. J., Morton, R. L., Obrador, G. T., &amp; Kidney Disease: Improving Global Outcomes. (2015). Executive "
                    "summary of the KDIGO Controversies Conference on Supportive Care in Chronic Kidney Disease: Developing a roadmap to improving "
                    "quality care. <em>Kidney International, 88</em>(3), 447&ndash;459. " + _doi("10.1038/ki.2015.110")),
    "house2019": ("House, A. A., Wanner, C., Sarnak, M. J., Pi&ntilde;a, I. L., McIntyre, C. W., Komenda, P., Kasiske, B. L., Deswal, A., "
                  "deFilippi, C. R., Cleland, J. G. F., Anker, S. D., Herzog, C. A., Cheung, M., Wheeler, D. C., Winkelmayer, W. C., "
                  "McCullough, P. A., &amp; Conference Participants. (2019). Heart failure in chronic kidney disease: Conclusions from a Kidney "
                  "Disease: Improving Global Outcomes (KDIGO) Controversies Conference. <em>Kidney International, 95</em>(6), 1304&ndash;1317. "
                  + _doi("10.1016/j.kint.2019.02.022")),
    "navaneethan2010": ("Navaneethan, S. D., Vecchio, M., Johnson, D. W., Saglimbene, V., Graziano, G., Pellegrini, F., Lucisano, G., Craig, J. C., "
                        "Ruospo, M., Gentile, G., Manfreda, V. M., Querques, M., Stroumza, P., Torok, M., Celia, E., Gelfman, R., Ferrari, J. N., "
                        "Bednarek-Skublewska, A., Dulawa, J., &hellip; Strippoli, G. F. M. (2010). Prevalence and correlates of self-reported "
                        "sexual dysfunction in CKD: A meta-analysis of observational studies. <em>American Journal of Kidney Diseases, 56</em>(4), "
                        "670&ndash;685. " + _doi("10.1053/j.ajkd.2010.06.016")),
    "hladunewich2014": ("Hladunewich, M. A., Hou, S., Odutayo, A., Cornelis, T., Pierratos, A., Goldstein, M., Tennankore, K., Keunen, J., Hui, D., "
                        "&amp; Chan, C. T. (2014). Intensive hemodialysis associates with improved pregnancy outcomes: A Canadian and United States "
                        "cohort comparison. <em>Journal of the American Society of Nephrology, 25</em>(5), 1103&ndash;1109. "
                        + _doi("10.1681/ASN.2013080825")),
    "piccoli2016": ("Piccoli, G. B., Minelli, F., Versino, E., Cabiddu, G., Attini, R., Vigotti, F. N., Rolfo, A., Giuffrida, D., Colombi, N., "
                    "Pani, A., &amp; Todros, T. (2016). Pregnancy in dialysis patients in the new millennium: A systematic review and "
                    "meta-regression analysis correlating dialysis schedules and pregnancy outcomes. <em>Nephrology Dialysis Transplantation, "
                    "31</em>(11), 1915&ndash;1934. " + _doi("10.1093/ndt/gfv395")),
    "wiles2019": ("Wiles, K., Chappell, L., Clark, K., Elman, L., Hall, M., Lightstone, L., Mohamed, G., Mukherjee, D., Nelson-Piercy, C., "
                  "Webster, P., Whybrow, R., &amp; Bramham, K. (2019). Clinical practice guideline on pregnancy and renal disease. "
                  "<em>BMC Nephrology, 20</em>(1), Article 401. " + _doi("10.1186/s12882-019-1560-2")),
    "rahbar2026": ("Rahbar, M., Latifi, M., Talebian, M. T., Hajialireza Tehrani, T., &amp; Dehghani, S. (2026). Elevated beta-human chorionic "
                   "gonadotropin levels in a patient with end-stage renal disease awaiting kidney transplantation: A case report. "
                   "<em>Journal of Medical Case Reports, 20</em>(1). " + _doi("10.1186/s13256-026-05983-3")),
    "watson2011": ("Watson, A. R., Harden, P. N., Ferris, M. E., Kerr, P. G., Mahan, J. D., Ramzy, M. F., International Society of Nephrology, "
                   "&amp; International Pediatric Nephrology Association. (2011). Transition from pediatric to adult renal services: A consensus "
                   "statement by the International Society of Nephrology (ISN) and the International Pediatric Nephrology Association (IPNA). "
                   "<em>Kidney International, 80</em>(7), 704&ndash;707. " + _doi("10.1038/ki.2011.209")),
}
