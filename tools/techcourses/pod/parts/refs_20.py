# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 20 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod_src/refs.py (daugirdas2015) are not repeated.
mavrakanas2017 is cited by this module but defined once, in Module 19 (refs_19.py)."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdigo_ckd2024": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. (2024). KDIGO 2024 clinical practice guideline for the "
                      "evaluation and management of chronic kidney disease. <em>Kidney International, 105</em>(4S), S117&ndash;S314. "
                      + _doi("10.1016/j.kint.2023.10.018")),
    "kdigo_dm2022": ("Kidney Disease: Improving Global Outcomes (KDIGO) Diabetes Work Group. (2022). KDIGO 2022 clinical practice guideline for "
                     "diabetes management in chronic kidney disease. <em>Kidney International, 102</em>(5S), S1&ndash;S127. "
                     + _doi("10.1016/j.kint.2022.06.008")),
    "deboer2022": ("de Boer, I. H., Khunti, K., Sadusky, T., Tuttle, K. R., Neumiller, J. J., Rhee, C. M., Rosas, S. E., Rossing, P., &amp; "
                   "Bakris, G. (2022). Diabetes management in chronic kidney disease: A consensus report by the American Diabetes Association (ADA) "
                   "and Kidney Disease: Improving Global Outcomes (KDIGO). <em>Diabetes Care, 45</em>(12), 3075&ndash;3090. "
                   + _doi("10.2337/dci22-0027")),
    "ishida2018": ("Ishida, J. H., McCulloch, C. E., Steinman, M. A., Grimes, B. A., &amp; Johansen, K. L. (2018). Gabapentin and pregabalin use "
                   "and association with adverse outcomes among hemodialysis patients. <em>Journal of the American Society of Nephrology, 29</em>(7), "
                   "1970&ndash;1978. " + _doi("10.1681/ASN.2018010096")),
    "muanda2022": ("Muanda, F. T., Weir, M. A., Ahmadi, F., Sontrop, J. M., Cowan, A., Fleet, J. L., Blake, P. G., &amp; Garg, A. X. (2022). "
                   "Higher-dose gabapentinoids and the risk of adverse events in older adults with CKD: A population-based cohort study. "
                   "<em>American Journal of Kidney Diseases, 80</em>(1), 98&ndash;107.e1. " + _doi("10.1053/j.ajkd.2021.11.007")),
    "kimmel2017": ("Kimmel, P. L., Fwu, C.-W., Abbott, K. C., Eggers, A. W., Kline, P. P., &amp; Eggers, P. W. (2017). Opioid prescription, "
                   "morbidity, and mortality in United States dialysis patients. <em>Journal of the American Society of Nephrology, 28</em>(12), "
                   "3658&ndash;3670. " + _doi("10.1681/ASN.2017010098")),
    "payne2017": ("Payne, L. E., Gagnon, D. J., Riker, R. R., Seder, D. B., Glisic, E. K., Morris, J. G., &amp; Fraser, G. L. (2017). "
                  "Cefepime-induced neurotoxicity: A systematic review. <em>Critical Care, 21</em>(1), Article 276. "
                  + _doi("10.1186/s13054-017-1856-1")),
    "maan2022": ("Maan, G., Keitoku, K., Kimura, N., Sawada, H., Pham, A., Yeo, J., Hagiya, H., &amp; Nishimura, Y. (2022). Cefepime-induced "
                 "neurotoxicity: Systematic review. <em>Journal of Antimicrobial Chemotherapy, 77</em>(11), 2908&ndash;2921. "
                 + _doi("10.1093/jac/dkac271")),
    "hardi2025": ("Hardi, H., Louisa, M., Widyahening, I. S., Chandra, J. R., Mahata, L. E., Soetikno, V., Gayatri, A., &amp; Instiaty, I. (2025). "
                  "Unveiling predisposing factors for cefepime-induced neurotoxicity: A systematic review and meta-analysis. "
                  "<em>British Journal of Clinical Pharmacology, 91</em>(8), 2192&ndash;2204. " + _doi("10.1002/bcp.70120")),
    "brandariz2021": ("Brandariz-Nu&ntilde;ez, D., Correas-Sanahuja, M., Maya-Gallego, S., &amp; Mart&iacute;n Herranz, I. (2021). Neurotoxicity "
                      "associated with acyclovir and valacyclovir: A systematic review of cases. <em>Journal of Clinical Pharmacy and "
                      "Therapeutics, 46</em>(4), 918&ndash;926. " + _doi("10.1111/jcpt.13464")),
    "wolf2018": ("Wolf, E., Kothari, N. R., Roberts, J. K., &amp; Sparks, M. A. (2018). Baclofen toxicity in kidney disease. "
                 "<em>American Journal of Kidney Diseases, 71</em>(2), 275&ndash;280. " + _doi("10.1053/j.ajkd.2017.07.005")),
    "chiu2009": ("Chiu, Y.-W., Teitelbaum, I., Misra, M., de Leon, E. M., Adzize, T., &amp; Mehrotra, R. (2009). Pill burden, adherence, "
                 "hyperphosphatemia, and quality of life in maintenance dialysis patients. <em>Clinical Journal of the American Society of "
                 "Nephrology, 4</em>(6), 1089&ndash;1096. " + _doi("10.2215/CJN.00290109")),
    "beers2023": ("2023 American Geriatrics Society Beers Criteria&reg; Update Expert Panel. (2023). American Geriatrics Society 2023 updated AGS "
                  "Beers Criteria&reg; for potentially inappropriate medication use in older adults. <em>Journal of the American Geriatrics "
                  "Society, 71</em>(7), 2052&ndash;2081. " + _doi("10.1111/jgs.18372")),
}
