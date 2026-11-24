# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 07 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod/refs.py (kdoqi_hd2015, eknoyan2002, locatelli2009, blankestijn2023,
vernooij2024, mytemp2022, pun2011, karnik2001, daugirdas2015) are not repeated.
vilar2022 and fernandezlucas2025 are shared with Module 03; Module 03 should reuse these keys and this exact text."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "gotch1985": ("Gotch, F. A., &amp; Sargent, J. A. (1985). A mechanistic analysis of the National Cooperative Dialysis Study (NCDS). "
                  "<em>Kidney International, 28</em>(3), 526&ndash;534. " + _doi("10.1038/ki.1985.160")),
    "owen1993": ("Owen, W. F., Lew, N. L., Liu, Y., Lowrie, E. G., &amp; Lazarus, J. M. (1993). The urea reduction ratio and serum albumin "
                 "concentration as predictors of mortality in patients undergoing hemodialysis. <em>New England Journal of Medicine, 329</em>(14), "
                 "1001&ndash;1006. " + _doi("10.1056/NEJM199309303291404")),
    "daugirdas1993": ("Daugirdas, J. T. (1993). Second generation logarithmic estimates of single-pool variable volume Kt/V: An analysis of error. "
                      "<em>Journal of the American Society of Nephrology, 4</em>(5), 1205&ndash;1213. " + _doi("10.1681/ASN.V451205")),
    "daugirdas1995": ("Daugirdas, J. T., &amp; Schneditz, D. (1995). Overestimation of hemodialysis dose depends on dialysis efficiency by regional "
                      "blood flow but not by conventional two pool urea kinetic analysis. <em>ASAIO Journal, 41</em>(3), M719&ndash;M724. "
                      + _doi("10.1097/00002480-199507000-00107")),
    "daugirdas2010": ("Daugirdas, J. T., Depner, T. A., Greene, T., Levin, N. W., Chertow, G. M., Rocco, M. V., &amp; Frequent Hemodialysis Network "
                      "Trial Group. (2010). Standard Kt/Vurea: A method of calculation that includes effects of fluid removal and residual kidney "
                      "clearance. <em>Kidney International, 77</em>(7), 637&ndash;644. " + _doi("10.1038/ki.2009.525")),
    "fhn2010": ("FHN Trial Group. (2010). In-center hemodialysis six times per week versus three times per week. <em>New England Journal of "
                "Medicine, 363</em>(24), 2287&ndash;2300. " + _doi("10.1056/NEJMoa1001593")),
    "rocco2011": ("Rocco, M. V., Lockridge, R. S., Beck, G. J., Eggers, P. W., Gassman, J. J., Greene, T., Larive, B., Chan, C. T., Chertow, G. M., "
                  "Copland, M., Hoy, C. D., Lindsay, R. M., Levin, N. W., Ornt, D. B., Pierratos, A., Pipkin, M. F., Rajagopalan, S., Stokes, J. B., "
                  "Unruh, M. L., . . . Frequent Hemodialysis Network (FHN) Trial Group. (2011). The effects of frequent nocturnal home hemodialysis: "
                  "The Frequent Hemodialysis Network Nocturnal Trial. <em>Kidney International, 80</em>(10), 1080&ndash;1091. "
                  + _doi("10.1038/ki.2011.213")),
    "jadoul2012": ("Jadoul, M., Thumma, J., Fuller, D. S., Tentori, F., Li, Y., Morgenstern, H., Mendelssohn, D., Tomo, T., Ethier, J., Port, F., "
                   "&amp; Robinson, B. M. (2012). Modifiable practices associated with sudden death among hemodialysis patients in the Dialysis "
                   "Outcomes and Practice Patterns Study. <em>Clinical Journal of the American Society of Nephrology, 7</em>(5), 765&ndash;774. "
                   + _doi("10.2215/CJN.08850811")),
    "tentori2013": ("Tentori, F., Karaboyas, A., Robinson, B. M., Morgenstern, H., Zhang, J., Sen, A., Ikizler, T. A., Rayner, H., Fissell, R. B., "
                    "Vanholder, R., Tomo, T., &amp; Port, F. K. (2013). Association of dialysate bicarbonate concentration with mortality in the "
                    "Dialysis Outcomes and Practice Patterns Study (DOPPS). <em>American Journal of Kidney Diseases, 62</em>(4), 738&ndash;746. "
                    + _doi("10.1053/j.ajkd.2013.03.035")),
    "maduell2013": ("Maduell, F., Moreso, F., Pons, M., Ramos, R., Mora-Maci&agrave;, J., Carreras, J., Soler, J., Torres, F., Campistol, J. M., "
                    "Martinez-Castelao, A., &amp; ESHOL Study Group. (2013). High-efficiency postdilution online hemodiafiltration reduces "
                    "all-cause mortality in hemodialysis patients. <em>Journal of the American Society of Nephrology, 24</em>(3), 487&ndash;497. "
                    + _doi("10.1681/ASN.2012080875")),
    "rose2024": ("Rose, M., Fischer, F. H., Liegl, G., Strippoli, G. F. M., Hockham, C., Vernooij, R. W. M., Barth, C., Canaud, B., Covic, A., "
                 "Cromm, K., Cucui, A. M., Davenport, A., Fischer, K. I., Hegbrant, J., Jaha, H., Schappert, A., T&ouml;r&ouml;k, M., Woodward, M., "
                 "Bots, M. L., . . . CONVINCE Scientific Committee and CONVINCE Investigators. (2024). The CONVINCE randomized trial found positive "
                 "effects on quality of life for patients with chronic kidney disease treated with hemodiafiltration. <em>Kidney International, "
                 "106</em>(5), 961&ndash;971. " + _doi("10.1016/j.kint.2024.07.014")),
    "cromm2026": ("Cromm, K., Fischer, F., Pellegrino, G., Vernooij, R. W. M., Riazy, L., Barth, C., Blankestijn, P. J., Bots, M. L., Canaud, B., "
                  "Davenport, A., Hegbrant, J., Woodward, M., Rose, M., &amp; Strippoli, G. F. M. (2026). Patient-reported outcomes with high-volume "
                  "hemodiafiltration versus high-flux hemodialysis across clinical subgroups: Results from the CONVINCE trial. <em>Clinical Journal "
                  "of the American Society of Nephrology</em>. Advance online publication. " + _doi("10.2215/CJN.0000001253")),
    "schouten2025": ("Schouten, A. E. M., Fischer, F., Blankestijn, P. J., Vernooij, R. W. M., Hockham, C., Strippoli, G. F. M., Canaud, B., "
                     "Hegbrant, J., Barth, C., Cromm, K., Davenport, A., Fischer, K. I., Rose, M., T&ouml;r&ouml;k, M., Woodward, M., Bots, M. L., "
                     "de Wit, G. A., Frederix, G. W. J., van der Meulen, M. P., &amp; CONVINCE Scientific Committee. (2025). A health economic "
                     "evaluation of the multinational, randomized controlled CONVINCE trial: Cost-utility of high-dose online hemodiafiltration "
                     "compared to high-flux hemodialysis. <em>Kidney International, 107</em>(4), 728&ndash;739. " + _doi("10.1016/j.kint.2024.12.018")),
    "vernooij2026": ("Vernooij, R. W., Strippoli, G. F., Veltkamp, D. M., Nistor, I., Craig, J. C., Saglimbene, V. M., Covic, A. C., &amp; "
                     "Vecchio, M. (2026). Haemodiafiltration, haemofiltration and haemodialysis for adults with kidney failure. <em>Cochrane "
                     "Database of Systematic Reviews, 2026</em>(10), Article CD006258. " + _doi("10.1002/14651858.CD006258.pub3")),
    "vilar2022": ("Vilar, E., Kaja Kamal, R. M., Fotheringham, J., Busby, A., Berdeprado, J., Kislowska, E., Wellsted, D., Alchi, B., Burton, J. O., "
                  "Davenport, A., &amp; Farrington, K. (2022). A multicenter feasibility randomized controlled trial to assess the impact of "
                  "incremental versus conventional initiation of hemodialysis on residual kidney function. <em>Kidney International, 101</em>(3), "
                  "615&ndash;625. " + _doi("10.1016/j.kint.2021.07.025")),
    "fernandezlucas2025": ("Fern&aacute;ndez Lucas, M., Muriel, A., Mendiola, N. R., Merino, J. L., Collado, A., D&iacute;az Dom&iacute;nguez, M. E., "
                           "Ru&iacute;z-Roso, G., S&aacute;nchez, R., Herrero, J. A., Bouarich, H., L&oacute;pez de la Manzanara, V., &amp; Zamora, J. "
                           "(2025). Randomized trial of twice-weekly versus thrice-weekly hemodiafiltration for initiation of renal replacement "
                           "therapy. <em>Kidney International Reports, 10</em>(12), 4188&ndash;4198. " + _doi("10.1016/j.ekir.2025.09.048")),
}
