# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 12 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in the course (obi2016, hall2021, daugirdas2015, kdoqi_hd2015, cdc2001,
gordon2019, saha2017, greenberg2021) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "robinson2014": ("Robinson, B. M., Zhang, J., Morgenstern, H., Bradbury, B. D., Ng, L. J., McCullough, K. P., Gillespie, B. W., Hakim, R., "
                     "Rayner, H., Fort, J., Akizawa, T., Tentori, F., &amp; Pisoni, R. L. (2014). Worldwide, mortality risk is high soon after "
                     "initiation of hemodialysis. <em>Kidney International, 85</em>(1), 158&ndash;165. " + _doi("10.1038/ki.2013.252")),
    "raina2022": ("Raina, R., Davenport, A., Warady, B., Vasistha, P., Sethi, S. K., Chakraborty, R., Khooblall, P., Agarwal, N., Vij, M., "
                  "Schaefer, F., Malhotra, K., &amp; Misra, M. (2022). Dialysis disequilibrium syndrome (DDS) in pediatric patients on dialysis: "
                  "Systematic review and clinical practice recommendations. <em>Pediatric Nephrology, 37</em>(2), 263&ndash;274. "
                  + _doi("10.1007/s00467-021-05242-1")),
    "mistry2019": ("Mistry, K. (2019). Dialysis disequilibrium syndrome prevention and management. <em>International Journal of Nephrology "
                   "and Renovascular Disease, 12</em>, 69&ndash;77. " + _doi("10.2147/IJNRD.S165925")),
    "sahani2001": ("Sahani, M. M., Daoud, T. M., Sam, R., Andrews, J., Cheng, Y. L., Kjellstrand, C. M., &amp; Ing, T. S. (2001). Dialysis "
                   "disequilibrium syndrome revisited. <em>Hemodialysis International, 5</em>(1), 92&ndash;96. "
                   + _doi("10.1111/hdi.2001.5.1.92")),
    "silver1996": ("Silver, S. M., Sterns, R. H., &amp; Halperin, M. L. (1996). Brain swelling after dialysis: Old urea or new osmoles? "
                   "<em>American Journal of Kidney Diseases, 28</em>(1), 1&ndash;13. " + _doi("10.1016/s0272-6386(96)90124-9")),
    "patel2008": ("Patel, N., Dalal, P., &amp; Panesar, M. (2008). Dialysis disequilibrium syndrome: A narrative review. "
                  "<em>Seminars in Dialysis, 21</em>(5), 493&ndash;498. " + _doi("10.1111/j.1525-139X.2008.00474.x")),
    "zepedaorozco2012": ("Zepeda-Orozco, D., &amp; Quigley, R. (2012). Dialysis disequilibrium syndrome. <em>Pediatric Nephrology, 27</em>(12), "
                         "2205&ndash;2211. " + _doi("10.1007/s00467-012-2199-4")),
    "jordan2021": ("Jordan, M., Ortiz-Soriano, V., Pruitt, A., Chism, L., Liu, L. J., Chaaban, N., Elias, M., Sawaya, B. P., Chen, J., &amp; "
                   "Neyra, J. A. (2021). Kidney recovery in patients with acute kidney injury treated in outpatient hemodialysis or "
                   "rehabilitation facilities. <em>Kidney Medicine, 3</em>(6), 916&ndash;924.e1. " + _doi("10.1016/j.xkme.2021.06.012")),
    "gautam2015": ("Gautam, S. C., Brooks, C. H., Balogun, R. A., Xin, W., Ma, J. Z., &amp; Abdel-Rahman, E. M. (2015). Predictors and "
                   "outcomes of post-hospitalization dialysis dependent acute kidney injury. <em>Nephron, 131</em>(3), 185&ndash;190. "
                   + _doi("10.1159/000441607")),
    "babroudi2024": ("Babroudi, S., Weiner, D. E., Neyra, J. A., &amp; Drew, D. A. (2024). Acute kidney injury receiving dialysis and dialysis "
                     "care after hospital discharge. <em>Journal of the American Society of Nephrology, 35</em>(7), 962&ndash;971. "
                     + _doi("10.1681/ASN.0000000000000383")),
    "ortizsoriano2023": ("Ortiz-Soriano, V., Cama-Olivares, A., Liu, L. J., Armentrout, B., Colohan, D., Paladiya, R., Babroudi, S., "
                         "Aycinena, J.-C., &amp; Neyra, J. A. (2023). The optimization of outpatient hemodialysis management for acute kidney "
                         "injury requiring dialysis patients: A quality improvement study. <em>American Journal of Nephrology, 54</em>(3&ndash;4), "
                         "95&ndash;105. " + _doi("10.1159/000530444")),
}
