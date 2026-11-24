# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 27 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. KDIGO grades quoted in the module were checked against the full guideline PDF at kdigo.org.
Keys already defined elsewhere (obi2016, daugirdas2015) and keys owned by Module 26 (davison2015, walavalkar2022)
are not repeated. kdigo_txcand2020 is owned here and reused by Module 29."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdigo_txcand2020": ("Chadban, S. J., Ahn, C., Axelrod, D. A., Foster, B. J., Kasiske, B. L., Kher, V., Kumar, D., Oberbauer, R., "
                         "Pascual, J., Pilmore, H. L., Rodrigue, J. R., Segev, D. L., Sheerin, N. S., Tinckam, K. J., Wong, G., &amp; "
                         "Knoll, G. A. (2020). KDIGO clinical practice guideline on the evaluation and management of candidates for kidney "
                         "transplantation. <em>Transplantation, 104</em>(4S1), S11&ndash;S103. " + _doi("10.1097/TP.0000000000003136")),
    "tonelli2011": ("Tonelli, M., Wiebe, N., Knoll, G., Bello, A., Browne, S., Jadhav, D., Klarenbach, S., &amp; Gill, J. (2011). "
                    "Systematic review: Kidney transplantation compared with dialysis in clinically relevant outcomes. "
                    "<em>American Journal of Transplantation, 11</em>(10), 2093&ndash;2109. " + _doi("10.1111/j.1600-6143.2011.03686.x")),
    "wolfe1999": ("Wolfe, R. A., Ashby, V. B., Milford, E. L., Ojo, A. O., Ettenger, R. E., Agodoa, L. Y., Held, P. J., &amp; Port, F. K. "
                  "(1999). Comparison of mortality in all patients on dialysis, patients on dialysis awaiting transplantation, and "
                  "recipients of a first cadaveric transplant. <em>New England Journal of Medicine, 341</em>(23), 1725&ndash;1730. "
                  + _doi("10.1056/NEJM199912023412303")),
    "abacan2021": ("Abacan, M. A. (2021). Profile of hospital transplant ethics committees in the Philippines. "
                   "<em>Developing World Bioethics, 21</em>(3), 139&ndash;146. " + _doi("10.1111/dewb.12281")),
    "ispd_prescribing2020": ("Brown, E. A., Blake, P. G., Boudville, N., Davies, S., de Arteaga, J., Dong, J., Finkelstein, F., Foo, M., "
                             "Hurst, H., Johnson, D. W., Johnson, M., Liew, A., Moraes, T., Perl, J., Shroff, R., Teitelbaum, I., "
                             "Wang, A. Y.-M., &amp; Warady, B. (2020). International Society for Peritoneal Dialysis practice "
                             "recommendations: Prescribing high-quality goal-directed peritoneal dialysis. <em>Peritoneal Dialysis "
                             "International, 40</em>(3), 244&ndash;253. " + _doi("10.1177/0896860819895364")),
    "ispd_peritonitis2022": ("Li, P. K.-T., Chow, K. M., Cho, Y., Fan, S., Figueiredo, A. E., Harris, T., Kanjanabuch, T., Kim, Y.-L., "
                             "Madero, M., Malyszko, J., Mehrotra, R., Okpechi, I. G., Perl, J., Piraino, B., Runnegar, N., Teitelbaum, I., "
                             "Wong, J. K.-W., Yu, X., &amp; Johnson, D. W. (2022). ISPD peritonitis guideline recommendations: 2022 update "
                             "on prevention and treatment. <em>Peritoneal Dialysis International, 42</em>(2), 110&ndash;153. "
                             + _doi("10.1177/08968608221080586")),
    "ispd_catheter2023": ("Chow, K. M., Li, P. K.-T., Cho, Y., Abu-Alfa, A., Bavanandan, S., Brown, E. A., Cullis, B., Edwards, D., "
                          "Ethier, I., Hurst, H., Ito, Y., de Moraes, T. P., Morelle, J., Runnegar, N., Saxena, A., So, S. W.-Y., Tian, N., "
                          "&amp; Johnson, D. W. (2023). ISPD catheter-related infection recommendations: 2023 update. <em>Peritoneal "
                          "Dialysis International, 43</em>(3), 201&ndash;219. " + _doi("10.1177/08968608231172740")),
    "yang_cochrane2025": ("Yang, J. W., Natale, P., Kim, S., Kim, M., Jeon, M. S., Yi, D., Hong, Y. A., Chung, S., Park, W. Y., Hyun, Y. Y., "
                          "Kwon, S. H., Shin, S. J., Park, D. A., Kim, J., Jung, J. H., Strippoli, G. F. M., &amp; Lee, J. Y. (2025). "
                          "Conservative kidney management versus dialysis for stage 5 chronic kidney disease in older people. "
                          "<em>Cochrane Database of Systematic Reviews, 12</em>(12), Article CD015151. "
                          + _doi("10.1002/14651858.CD015151.pub2")),
    "verberne2016": ("Verberne, W. R., Geers, A. B. M. T., Jellema, W. T., Vincent, H. H., van Delden, J. J. M., &amp; Bos, W. J. W. "
                     "(2016). Comparative survival among older adults with advanced kidney disease managed conservatively versus with "
                     "dialysis. <em>Clinical Journal of the American Society of Nephrology, 11</em>(4), 633&ndash;640. "
                     + _doi("10.2215/CJN.07510715")),
}
