# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 18 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in the course (palmer2016, montague2008, pun2011, greenberg2021, saha2017,
daugirdas2015) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "clase2020": ("Clase, C. M., Carrero, J. J., Ellison, D. H., Grams, M. E., Hemmelgarn, B. R., Jardine, M. J., Kovesdy, C. P., Kline, G. A., "
                  "Lindner, G., Obrador, G. T., Palmer, B. F., Cheung, M., Wheeler, D. C., Winkelmayer, W. C., Pecoits-Filho, R., &amp; Conference "
                  "Participants. (2020). Potassium homeostasis and management of dyskalemia in kidney diseases: Conclusions from a Kidney Disease: "
                  "Improving Global Outcomes (KDIGO) Controversies Conference. <em>Kidney International, 97</em>(1), 42&ndash;61. "
                  + _doi("10.1016/j.kint.2019.09.018")),
    "mahoney2005": ("Mahoney, B. A., Smith, W. A. D., Lo, D. S., Tsoi, K., Tonelli, M., &amp; Clase, C. M. (2005). Emergency interventions for "
                    "hyperkalaemia. <em>Cochrane Database of Systematic Reviews, 2005</em>(2), CD003235. " + _doi("10.1002/14651858.CD003235.pub2")),
    "allon1995": ("Allon, M., &amp; Shanklin, N. (1995). Effect of albuterol treatment on subsequent dialytic potassium removal. "
                  "<em>American Journal of Kidney Diseases, 26</em>(4), 607&ndash;613. " + _doi("10.1016/0272-6386(95)90597-9")),
    "jessen2025": ("Jessen, M. K., Andersen, L. W., Djakow, J., Chong, N. K., Stankovic, N., Staehr, C., Vammen, L., Petersen, A. H., Johannsen, C. M., "
                   "Eggertsen, M. A., Mortensen, S. &Oslash;., H&oslash;ybye, M., N&oslash;rholt, C., Holmberg, M. J., Granfeldt, A., &amp; International "
                   "Liaison Committee on Resuscitation (ILCOR) Advanced Paediatric Life Support Task Forces. (2025). Pharmacological interventions for the "
                   "acute treatment of hyperkalaemia: A systematic review and meta-analysis. <em>Resuscitation, 208</em>, 110489. "
                   + _doi("10.1016/j.resuscitation.2025.110489")),
    "fishbane2019": ("Fishbane, S., Ford, M., Fukagawa, M., McCafferty, K., Rastogi, A., Spinowitz, B., Staroselskiy, K., Vishnevskiy, K., Lisovskaja, V., "
                     "Al-Shurbaji, A., Guzman, N., &amp; Bhandari, S. (2019). A phase 3b, randomized, double-blind, placebo-controlled study of sodium "
                     "zirconium cyclosilicate for reducing the incidence of predialysis hyperkalemia. <em>Journal of the American Society of Nephrology, "
                     "30</em>(9), 1723&ndash;1733. " + _doi("10.1681/ASN.2019050450")),
    "fishbane2025": ("Fishbane, S., Dember, L. M., Jadoul, M., Kovesdy, C. P., Guzman, N., Kordzakhia, G., Lisovskaja, V., Sekar, P., Wessman, P., "
                     "Al-Shurbaji, A., &amp; Herzog, C. A. (2025). The randomized DIALIZE-Outcomes trial evaluated sodium zirconium cyclosilicate in "
                     "hemodialysis. <em>Kidney International, 108</em>(4), 686&ndash;694. " + _doi("10.1016/j.kint.2025.06.016")),
    "middleton2024": ("Middleton, J. P., Sun, S., Murray, S., Davenport, C. A., &amp; Daubert, J. P. (2024). Randomized trial of patiromer on efficacy "
                      "to reduce episodic hyperkalemia in patients with ESKD treated with hemodialysis. <em>Kidney International Reports, 9</em>(11), "
                      "3218&ndash;3225. " + _doi("10.1016/j.ekir.2024.08.005")),
    "natale2020": ("Natale, P., Palmer, S. C., Ruospo, M., Saglimbene, V. M., &amp; Strippoli, G. F. (2020). Potassium binders for chronic "
                   "hyperkalaemia in people with chronic kidney disease. <em>Cochrane Database of Systematic Reviews, 2020</em>(6), CD013165. "
                   + _doi("10.1002/14651858.CD013165.pub2")),
    "karaboyas2017": ("Karaboyas, A., Zee, J., Brunelli, S. M., Usvyat, L. A., Weiner, D. E., Maddux, F. W., Nissenson, A. R., Jadoul, M., Locatelli, F., "
                      "Winkelmayer, W. C., Port, F. K., Robinson, B. M., &amp; Tentori, F. (2017). Dialysate potassium, serum potassium, mortality, and "
                      "arrhythmia events in hemodialysis: Results from the Dialysis Outcomes and Practice Patterns Study (DOPPS). <em>American Journal "
                      "of Kidney Diseases, 69</em>(2), 266&ndash;277. " + _doi("10.1053/j.ajkd.2016.09.015")),
    "apel2014": ("Apel, J., Reutrakul, S., &amp; Baldwin, D. (2014). Hypoglycemia in the treatment of hyperkalemia with insulin in patients with "
                 "end-stage renal disease. <em>Clinical Kidney Journal, 7</em>(3), 248&ndash;250. " + _doi("10.1093/ckj/sfu026")),
    "schafers2012": ("Schafers, S., Naunheim, R., Vijayan, A., &amp; Tobin, G. (2012). Incidence of hypoglycemia following insulin-based acute "
                     "stabilization of hyperkalemia treatment. <em>Journal of Hospital Medicine, 7</em>(3), 239&ndash;242. " + _doi("10.1002/jhm.977")),
    "mcnicholas2018": ("McNicholas, B. A., Pham, M. H., Carli, K., Chen, C. H., Colobong-Smith, N., Anderson, A. E., &amp; Pham, H. (2018). Treatment of "
                       "hyperkalemia with a low-dose insulin protocol is effective and results in reduced hypoglycemia. <em>Kidney International "
                       "Reports, 3</em>(2), 328&ndash;336. " + _doi("10.1016/j.ekir.2017.10.009")),
    "hayashi2021": ("Hayashi, A., Shimizu, N., Suzuki, A., Matoba, K., Momozono, A., Masaki, T., Ogawa, A., Moriguchi, I., Takano, K., Kobayashi, N., "
                    "&amp; Shichiri, M. (2021). Hemodialysis-related glycemic disarray proven by continuous glucose monitoring; glycemic markers and "
                    "hypoglycemia. <em>Diabetes Care, 44</em>(7), 1647&ndash;1656. " + _doi("10.2337/dc21-0269")),
    "abe2015": ("Abe, M., &amp; Kalantar-Zadeh, K. (2015). Haemodialysis-induced hypoglycaemia and glycaemic disarrays. <em>Nature Reviews "
                "Nephrology, 11</em>(5), 302&ndash;313. " + _doi("10.1038/nrneph.2015.38")),
    "burmeister2015": ("Burmeister, J. E., Miltersteiner, D. da R., Burmeister, B. O., &amp; Campos, J. F. (2015). Risk of hypoglycemia during "
                       "hemodialysis in diabetic patients is related to lower pre-dialysis glycemia. <em>Archives of Endocrinology and Metabolism, "
                       "59</em>(2), 137&ndash;140. " + _doi("10.1590/2359-3997000000026")),
    "titoff2019": ("T&iacute;toff, V., Moury, H. N., T&iacute;toff, I. B., &amp; Kelly, K. M. (2019). Seizures, antiepileptic drugs, and CKD. "
                   "<em>American Journal of Kidney Diseases, 73</em>(1), 90&ndash;101. " + _doi("10.1053/j.ajkd.2018.03.021")),
    "seliger2003": ("Seliger, S. L., Gillen, D. L., Longstreth, W. T., Kestenbaum, B., &amp; Stehman-Breen, C. O. (2003). Elevated risk of stroke "
                    "among patients with end-stage renal disease. <em>Kidney International, 64</em>(2), 603&ndash;609. "
                    + _doi("10.1046/j.1523-1755.2003.00101.x")),
    "toyoda2005": ("Toyoda, K., Fujii, K., Fujimi, S., Kumai, Y., Tsuchimochi, H., Ibayashi, S., &amp; Iida, M. (2005). Stroke in patients on "
                   "maintenance hemodialysis: A 22-year single-center study. <em>American Journal of Kidney Diseases, 45</em>(6), 1058&ndash;1066. "
                   + _doi("10.1053/j.ajkd.2005.02.028")),
    "tariq2013": ("Tariq, N., Adil, M. M., Saeed, F., Chaudhry, S. A., &amp; Qureshi, A. I. (2013). Outcomes of thrombolytic treatment for acute "
                  "ischemic stroke in dialysis-dependent patients in the United States. <em>Journal of Stroke and Cerebrovascular Diseases, "
                  "22</em>(8), e354&ndash;e359. " + _doi("10.1016/j.jstrokecerebrovasdis.2013.03.016")),
    "ovbiagele2014": ("Ovbiagele, B., Smith, E. E., Schwamm, L. H., Grau-Sepulveda, M. V., Saver, J. L., Bhatt, D. L., Hernandez, A. F., Peterson, E. D., "
                      "&amp; Fonarow, G. C. (2014). Chronic kidney disease and bleeding complications after intravenous thrombolytic therapy for acute "
                      "ischemic stroke. <em>Circulation: Cardiovascular Quality and Outcomes, 7</em>(6), 929&ndash;935. "
                      + _doi("10.1161/CIRCOUTCOMES.114.001144")),
    "prabhakaran2026": ("Prabhakaran, S., Gonzalez, N. R., Zachrison, K. S., Adeoye, O., Alexandrov, A. W., Ansari, S. A., Chapman, S., Czap, A. L., "
                        "Dumitrascu, O. M., Ishida, K., Jadhav, A. P., Johnson, B., Johnston, K. C., Khatri, P., Kimberly, W. T., Lee, V. H., "
                        "Leslie-Mazwi, T. M., Mac Grory, B., Madsen, T. E., &hellip; Peer Review Committee. (2026). 2026 guideline for the early "
                        "management of patients with acute ischemic stroke: A guideline from the American Heart Association/American Stroke "
                        "Association. <em>Stroke, 57</em>(8), e316&ndash;e436. " + _doi("10.1161/STR.0000000000000513")),
}
