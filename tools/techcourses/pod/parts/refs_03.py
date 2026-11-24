# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 03 (APA 7). Each journal entry was built from PubMed metadata
on November 25, 2026. Keys already defined in pod/refs.py (meyer2007, obi2016, daugirdas2015) are not repeated.
kdoqi_hd2015 is defined in parts/refs_05.py; it is repeated here with identical text so that this part validates alone."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdoqi_hd2015": ("National Kidney Foundation. (2015). KDOQI clinical practice guideline for hemodialysis adequacy: 2015 update. "
                     "<em>American Journal of Kidney Diseases, 66</em>(5), 884&ndash;930. " + _doi("10.1053/j.ajkd.2015.07.015")),
    "vanholder2003": ("Vanholder, R., De Smet, R., Glorieux, G., Argil&eacute;s, A., Baurmeister, U., Brunet, P., Clark, W., Cohen, G., "
                      "De Deyn, P. P., Deppisch, R., Descamps-Latscha, B., Henle, T., J&ouml;rres, A., Lemke, H. D., Massy, Z. A., "
                      "Passlick-Deetjen, J., Rodriguez, M., Stegmayr, B., Stenvinkel, P., . . . European Uremic Toxin Work Group (EUTox). (2003). "
                      "Review on uremic toxins: Classification, concentration, and interindividual variability. <em>Kidney International, 63</em>(5), "
                      "1934&ndash;1943. " + _doi("10.1046/j.1523-1755.2003.00924.x")),
    "duranton2012": ("Duranton, F., Cohen, G., De Smet, R., Rodriguez, M., Jankowski, J., Vanholder, R., Argiles, A., &amp; European Uremic "
                     "Toxin Work Group. (2012). Normal and pathologic concentrations of uremic toxins. <em>Journal of the American Society of "
                     "Nephrology, 23</em>(7), 1258&ndash;1270. " + _doi("10.1681/ASN.2011121175")),
    "rosner2021": ("Rosner, M. H., Reis, T., Husain-Syed, F., Vanholder, R., Hutchison, C., Stenvinkel, P., Blankestijn, P. J., Cozzolino, M., "
                   "Juillard, L., Kashani, K., Kaushik, M., Kawanishi, H., Massy, Z., Sirich, T. L., Zuo, L., &amp; Ronco, C. (2021). "
                   "Classification of uremic toxins and their role in kidney failure. <em>Clinical Journal of the American Society of "
                   "Nephrology, 16</em>(12), 1918&ndash;1928. " + _doi("10.2215/CJN.02660221")),
    "cooper2010": ("Cooper, B. A., Branley, P., Bulfone, L., Collins, J. F., Craig, J. C., Fraenkel, M. B., Harris, A., Johnson, D. W., "
                   "Kesselhut, J., Li, J. J., Luxton, G., Pilmore, A., Tiller, D. J., Harris, D. C., Pollock, C. A., &amp; IDEAL Study. (2010). "
                   "A randomized, controlled trial of early versus late initiation of dialysis. <em>New England Journal of Medicine, 363</em>(7), "
                   "609&ndash;619. " + _doi("10.1056/NEJMoa1000552")),
    "kdigo_ckd2024": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. (2024). KDIGO 2024 clinical practice guideline for the "
                      "evaluation and management of chronic kidney disease. <em>Kidney International, 105</em>(4S), S117&ndash;S314. "
                      + _doi("10.1016/j.kint.2023.10.018")),
    "chan2019": ("Chan, C. T., Blankestijn, P. J., Dember, L. M., Gallieni, M., Harris, D. C. H., Lok, C. E., Mehrotra, R., Stevens, P. E., "
                 "Wang, A. Y., Cheung, M., Wheeler, D. C., Winkelmayer, W. C., Pollock, C. A., &amp; Conference Participants. (2019). "
                 "Dialysis initiation, modality choice, access, and prescription: Conclusions from a Kidney Disease: Improving Global Outcomes "
                 "(KDIGO) Controversies Conference. <em>Kidney International, 96</em>(1), 37&ndash;47. " + _doi("10.1016/j.kint.2019.01.017")),
    "shafi2010": ("Shafi, T., Jaar, B. G., Plantinga, L. C., Fink, N. E., Sadler, J. H., Parekh, R. S., Powe, N. R., &amp; Coresh, J. (2010). "
                  "Association of residual urine output with mortality, quality of life, and inflammation in incident hemodialysis patients: "
                  "The Choices for Healthy Outcomes in Caring for End-Stage Renal Disease (CHOICE) Study. <em>American Journal of Kidney "
                  "Diseases, 56</em>(2), 348&ndash;358. " + _doi("10.1053/j.ajkd.2010.03.020")),
    "bargman2001": ("Bargman, J. M., Thorpe, K. E., &amp; Churchill, D. N. (2001). Relative contribution of residual renal function and "
                    "peritoneal clearance to adequacy of dialysis: A reanalysis of the CANUSA study. <em>Journal of the American Society of "
                    "Nephrology, 12</em>(10), 2158&ndash;2162. " + _doi("10.1681/ASN.V12102158")),
    "moist2000": ("Moist, L. M., Port, F. K., Orzol, S. M., Young, E. W., Ostbye, T., Wolfe, R. A., Hulbert-Shearon, T., Jones, C. A., &amp; "
                  "Bloembergen, W. E. (2000). Predictors of loss of residual renal function among new dialysis patients. <em>Journal of the "
                  "American Society of Nephrology, 11</em>(3), 556&ndash;564. " + _doi("10.1681/ASN.V113556")),
    "sirich2024": ("Sirich, T. L., Tan, Z., Highland, B. R., Lin, Z., Russell, G. B., &amp; Murea, M. (2024). Longitudinal changes in kidney "
                   "solute clearance in a prospective cohort of patients initiating chronic hemodialysis. <em>Kidney International Reports, "
                   "9</em>(6), 1774&ndash;1782. " + _doi("10.1016/j.ekir.2024.03.015")),
    "vilar2022": ("Vilar, E., Kaja Kamal, R. M., Fotheringham, J., Busby, A., Berdeprado, J., Kislowska, E., Wellsted, D., Alchi, B., "
                  "Burton, J. O., Davenport, A., &amp; Farrington, K. (2022). A multicenter feasibility randomized controlled trial to assess "
                  "the impact of incremental versus conventional initiation of hemodialysis on residual kidney function. <em>Kidney "
                  "International, 101</em>(3), 615&ndash;625. " + _doi("10.1016/j.kint.2021.07.025")),
    "murea2022": ("Murea, M., Patel, A., Highland, B. R., Yang, W., Fletcher, A. J., Kalantar-Zadeh, K., Dressler, E., &amp; Russell, G. B. "
                  "(2022). Twice-weekly hemodialysis with adjuvant pharmacotherapy and transition to thrice-weekly hemodialysis: A pilot "
                  "study. <em>American Journal of Kidney Diseases, 80</em>(2), 227&ndash;240.e1. " + _doi("10.1053/j.ajkd.2021.12.001")),
    "fernandezlucas2025": ("Fern&aacute;ndez Lucas, M., Muriel, A., Mendiola, N. R., Merino, J. L., Collado, A., D&iacute;az Dom&iacute;nguez, M. E., "
                           "Ru&iacute;z-Roso, G., S&aacute;nchez, R., Herrero, J. A., Bouarich, H., L&oacute;pez de la Manzanara, V., &amp; "
                           "Zamora, J. (2025). Randomized trial of twice-weekly versus thrice-weekly hemodiafiltration for initiation of renal "
                           "replacement therapy. <em>Kidney International Reports, 10</em>(12), 4188&ndash;4198. "
                           + _doi("10.1016/j.ekir.2025.09.048")),
    "kittiskulnam2025": ("Kittiskulnam, P., Tiranathanagul, K., Susantitaphong, P., Phannajit, J., Chongpison, Y., Asavapujanamanee, P., "
                         "Surattichaiyakul, B., Takkavatakarn, K., Katavetin, P., Metta, K., &amp; Praditpornsilpa, K. (2025). Stepwise "
                         "incremental hemodialysis and low-protein diet supplemented with keto-analogues preserve residual kidney function: "
                         "A randomized controlled trial. <em>Nutrients, 17</em>(15), Article 2422. " + _doi("10.3390/nu17152422")),
    "murea2024": ("Murea, M., Raimann, J. G., Divers, J., Maute, H., Kovach, C., Abdel-Rahman, E. M., Awad, A. S., Flythe, J. E., "
                  "Gautam, S. C., Niyyar, V. D., Roberts, G. V., Jefferson, N. M., Shahidul, I., Nwaozuru, U., Foley, K. L., Trembath, E. J., "
                  "Rosales, M. L., Fletcher, A. J., Hiba, S. I., . . . Two Plus Research Consortium. (2024). Comparative effectiveness of an "
                  "individualized model of hemodialysis vs conventional hemodialysis: A study protocol for a multicenter randomized "
                  "controlled trial (the TwoPlus trial). <em>Trials, 25</em>(1), Article 424. " + _doi("10.1186/s13063-024-08281-9")),
    "obi2016incr": ("Obi, Y., Streja, E., Rhee, C. M., Ravel, V., Amin, A. N., Cupisti, A., Chen, J., Mathew, A. T., Kovesdy, C. P., "
                    "Mehrotra, R., &amp; Kalantar-Zadeh, K. (2016). Incremental hemodialysis, residual kidney function, and mortality risk in "
                    "incident dialysis patients: A cohort study. <em>American Journal of Kidney Diseases, 68</em>(2), 256&ndash;265. "
                    + _doi("10.1053/j.ajkd.2016.01.008")),
    "garofalo2019": ("Garofalo, C., Borrelli, S., De Stefano, T., Provenzano, M., Andreucci, M., Cabiddu, G., La Milia, V., Vizzardi, V., "
                     "Sandrini, M., Cancarini, G., Cupisti, A., Bellizzi, V., Russo, R., Chiodini, P., Minutolo, R., Conte, G., &amp; "
                     "De Nicola, L. (2019). Incremental dialysis in ESRD: Systematic review and meta-analysis. <em>Journal of Nephrology, "
                     "32</em>(5), 823&ndash;836. " + _doi("10.1007/s40620-018-00577-9")),
}
