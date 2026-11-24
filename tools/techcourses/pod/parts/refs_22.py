# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 22 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod/refs.py and its parts (daugirdas2015, kistler2018) are not repeated.
Module 22 owns kdigo_dm2022; Module 23 reuses it."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "kdigo_dm2022": ("Kidney Disease: Improving Global Outcomes (KDIGO) Diabetes Work Group. (2022). KDIGO 2022 clinical practice guideline "
                     "for diabetes management in chronic kidney disease. <em>Kidney International, 102</em>(5S), S1&ndash;S127. "
                     + _doi("10.1016/j.kint.2022.06.008")),
    "deboer2022": ("de Boer, I. H., Khunti, K., Sadusky, T., Tuttle, K. R., Neumiller, J. J., Rhee, C. M., Rosas, S. E., Rossing, P., &amp; "
                   "Bakris, G. (2022). Diabetes management in chronic kidney disease: A consensus report by the American Diabetes Association "
                   "(ADA) and Kidney Disease: Improving Global Outcomes (KDIGO). <em>Diabetes Care, 45</em>(12), 3075&ndash;3090. "
                   + _doi("10.2337/dci22-0027")),
    "galindo2020": ("Galindo, R. J., Beck, R. W., Scioscia, M. F., Umpierrez, G. E., &amp; Tuttle, K. R. (2020). Glycemic monitoring and "
                    "management in advanced chronic kidney disease. <em>Endocrine Reviews, 41</em>(5), 756&ndash;774. "
                    + _doi("10.1210/endrev/bnaa017")),
    "peacock2008": ("Peacock, T. P., Shihabi, Z. K., Bleyer, A. J., Dolbare, E. L., Byers, J. R., Knovich, M. A., Calles-Escandon, J., "
                    "Russell, G. B., &amp; Freedman, B. I. (2008). Comparison of glycated albumin and hemoglobin A1c levels in diabetic subjects "
                    "on hemodialysis. <em>Kidney International, 73</em>(9), 1062&ndash;1068. " + _doi("10.1038/ki.2008.25")),
    "ramirez2012": ("Ramirez, S. P., McCullough, K. P., Thumma, J. R., Nelson, R. G., Morgenstern, H., Gillespie, B. W., Inaba, M., "
                    "Jacobson, S. H., Vanholder, R., Pisoni, R. L., Port, F. K., &amp; Robinson, B. M. (2012). Hemoglobin A1c levels and "
                    "mortality in the diabetic hemodialysis population: Findings from the Dialysis Outcomes and Practice Patterns Study (DOPPS). "
                    "<em>Diabetes Care, 35</em>(12), 2527&ndash;2532. " + _doi("10.2337/dc12-0573")),
    "hayashi2021": ("Hayashi, A., Shimizu, N., Suzuki, A., Matoba, K., Momozono, A., Masaki, T., Ogawa, A., Moriguchi, I., Takano, K., "
                    "Kobayashi, N., &amp; Shichiri, M. (2021). Hemodialysis-related glycemic disarray proven by continuous glucose monitoring; "
                    "glycemic markers and hypoglycemia. <em>Diabetes Care, 44</em>(7), 1647&ndash;1656. " + _doi("10.2337/dc21-0269")),
    "burmeister2015": ("Burmeister, J. E., Miltersteiner, D. da R., Burmeister, B. O., &amp; Campos, J. F. (2015). Risk of hypoglycemia during "
                       "hemodialysis in diabetic patients is related to lower pre-dialysis glycemia. <em>Archives of Endocrinology and "
                       "Metabolism, 59</em>(2), 137&ndash;140. " + _doi("10.1590/2359-3997000000026")),
    "narasaki2024": ("Narasaki, Y., Kalantar-Zadeh, K., Daza, A. C., You, A. S., Novoa, A., Peralta, R. A., Siu, M. K. M., Nguyen, D. V., "
                     "&amp; Rhee, C. M. (2024). Accuracy of continuous glucose monitoring in hemodialysis patients with diabetes. "
                     "<em>Diabetes Care, 47</em>(11), 1922&ndash;1929. " + _doi("10.2337/dc24-0635")),
    "avari2023": ("Avari, P., Tang, W., Jugnee, N., Hersi, I., Al-Balah, A., Tan, T., Frankel, A. H., Oliver, N., &amp; Reddy, M. (2023). "
                  "The accuracy of continuous glucose sensors in people with diabetes undergoing hemodialysis (ALPHA study). "
                  "<em>Diabetes Technology &amp; Therapeutics, 25</em>(7), 447&ndash;456. " + _doi("10.1089/dia.2023.0013")),
    "avari2025": ("Avari, P., Pushparatnam, R., Leelarathna, L., Tan, T., Frankel, A. H., Oliver, N., &amp; Reddy, M. (2025). Accuracy of "
                  "the Dexcom G7 continuous glucose monitoring sensors in people with diabetes undergoing hemodialysis (ALPHA-2 study). "
                  "<em>Diabetes Technology &amp; Therapeutics, 27</em>(5), 402&ndash;406. " + _doi("10.1089/dia.2024.0575")),
    "villard2022": ("Villard, O., Breton, M. D., Rao, S., Voelmle, M. K., Fuller, M. R., Myers, H. E., McFadden, R. K., Luke, Z. S., "
                    "Wakeman, C. A., Clancy-Oliveri, M., Basu, A., &amp; Stumpf, M. M. (2022). Accuracy of a factory-calibrated continuous "
                    "glucose monitor in individuals with diabetes on hemodialysis. <em>Diabetes Care, 45</em>(7), 1666&ndash;1669. "
                    + _doi("10.2337/dc22-0073")),
    "nathan2008": ("Nathan, D. M., Kuenen, J., Borg, R., Zheng, H., Schoenfeld, D., &amp; Heine, R. J. (2008). Translating the A1C assay into "
                   "estimated average glucose values. <em>Diabetes Care, 31</em>(8), 1473&ndash;1478. " + _doi("10.2337/dc08-0545")),
    "bergenstal2018": ("Bergenstal, R. M., Beck, R. W., Close, K. L., Grunberger, G., Sacks, D. B., Kowalski, A., Brown, A. S., Heinemann, L., "
                       "Aleppo, G., Ryan, D. B., Riddlesworth, T. D., &amp; Cefalu, W. T. (2018). Glucose management indicator (GMI): A new "
                       "term for estimating A1C from continuous glucose monitoring. <em>Diabetes Care, 41</em>(11), 2275&ndash;2280. "
                       + _doi("10.2337/dc18-1581")),
    "ndip2010": ("Ndip, A., Lavery, L. A., Lafontaine, J., Rutter, M. K., Vardhan, A., Vileikyte, L., &amp; Boulton, A. J. M. (2010). High "
                 "levels of foot ulceration and amputation risk in a multiracial cohort of diabetic patients on dialysis therapy. "
                 "<em>Diabetes Care, 33</em>(4), 878&ndash;880. " + _doi("10.2337/dc09-2007")),
    "lavery2015": ("Lavery, L. A., Lavery, D. C., Hunt, N. A., La Fontaine, J., Ndip, A., &amp; Boulton, A. J. (2015). Amputations and "
                   "foot-related hospitalisations disproportionately affect dialysis patients. <em>International Wound Journal, 12</em>(5), "
                   "523&ndash;526. " + _doi("10.1111/iwj.12146")),
}
