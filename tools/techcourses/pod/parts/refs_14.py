# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 14 (APA 7). Each entry was built from PubMed metadata checked
on November 25, 2026. Keys already defined in the course (daugirdas2015, kdigo_bpvol2020, flythe2011, hall2021, torino2016)
are not repeated. zoccali2013 and agarwal2009drip are defined by Module 08 (refs_08.py) and are cited here, not defined."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "sarafidis2017": ("Sarafidis, P. A., Persu, A., Agarwal, R., Burnier, M., de Leeuw, P., Ferro, C. J., Halimi, J.-M., Heine, G. H., Jadoul, M., "
                      "Jarraya, F., Kanbay, M., Mallamaci, F., Mark, P. B., Ortiz, A., Parati, G., Pontremoli, R., Rossignol, P., Ruilope, L., "
                      "Van der Niepen, P., . . . Zoccali, C. (2017). Hypertension in dialysis patients: A consensus document by the European Renal "
                      "and Cardiovascular Medicine (EURECA-m) working group of the European Renal Association-European Dialysis and Transplant "
                      "Association (ERA-EDTA) and the Hypertension and the Kidney working group of the European Society of Hypertension (ESH). "
                      "<em>Nephrology Dialysis Transplantation, 32</em>(4), 620&ndash;640. " + _doi("10.1093/ndt/gfw433")),
    "agarwal2010": ("Agarwal, R. (2010). Blood pressure and mortality among hemodialysis patients. <em>Hypertension, 55</em>(3), 762&ndash;768. "
                    + _doi("10.1161/HYPERTENSIONAHA.109.144899")),
    "alborzi2007": ("Alborzi, P., Patel, N., &amp; Agarwal, R. (2007). Home blood pressures are of greater prognostic value than hemodialysis unit "
                    "recordings. <em>Clinical Journal of the American Society of Nephrology, 2</em>(6), 1228&ndash;1234. " + _doi("10.2215/CJN.02250507")),
    "agarwal2009abpm": ("Agarwal, R. (2009). Volume-associated ambulatory blood pressure patterns in hemodialysis patients. <em>Hypertension, "
                        "54</em>(2), 241&ndash;247. " + _doi("10.1161/HYPERTENSIONAHA.109.136366")),
    "heerspink2009": ("Heerspink, H. J. L., Ninomiya, T., Zoungas, S., de Zeeuw, D., Grobbee, D. E., Jardine, M. J., Gallagher, M., Roberts, M. A., "
                      "Cass, A., Neal, B., &amp; Perkovic, V. (2009). Effect of lowering blood pressure on cardiovascular events and mortality in "
                      "patients on dialysis: A systematic review and meta-analysis of randomised controlled trials. <em>The Lancet, 373</em>(9668), "
                      "1009&ndash;1015. " + _doi("10.1016/S0140-6736(09)60212-9")),
    "miskulin2018": ("Miskulin, D. C., Gassman, J., Schrader, R., Gul, A., Jhamb, M., Ploth, D. W., Negrea, L., Kwong, R. Y., Levey, A. S., Singh, A. K., "
                     "Harford, A., Paine, S., Kendrick, C., Rahman, M., &amp; Zager, P. (2018). BP in dialysis: Results of a pilot study. "
                     "<em>Journal of the American Society of Nephrology, 29</em>(1), 307&ndash;316. " + _doi("10.1681/ASN.2017020135")),
    "agarwal2014hdpal": ("Agarwal, R., Sinha, A. D., Pappas, M. K., Abraham, T. N., &amp; Tegegne, G. G. (2014). Hypertension in hemodialysis patients "
                         "treated with atenolol or lisinopril: A randomized controlled trial. <em>Nephrology Dialysis Transplantation, 29</em>(3), "
                         "672&ndash;681. " + _doi("10.1093/ndt/gft515")),
    "georgianos2024": ("Georgianos, P. I., &amp; Agarwal, R. (2024). Resistant hypertension in dialysis: Epidemiology, diagnosis, and management. "
                       "<em>Journal of the American Society of Nephrology, 35</em>(4), 505&ndash;514. " + _doi("10.1681/ASN.0000000000000315")),
    "georgianos2019": ("Georgianos, P. I., &amp; Agarwal, R. (2019). Systolic and diastolic hypertension among patients on hemodialysis: Musings on "
                       "volume overload, arterial stiffness, and erythropoietin. <em>Seminars in Dialysis, 32</em>(6), 507&ndash;512. "
                       + _doi("10.1111/sdi.12837")),
    "inrig2009": ("Inrig, J. K., Patel, U. D., Toto, R. D., &amp; Szczech, L. A. (2009). Association of blood pressure increases during hemodialysis "
                  "with 2-year mortality in incident hemodialysis patients: A secondary analysis of the Dialysis Morbidity and Mortality Wave 2 "
                  "Study. <em>American Journal of Kidney Diseases, 54</em>(5), 881&ndash;890. " + _doi("10.1053/j.ajkd.2009.05.012")),
    "inrig2010": ("Inrig, J. K. (2010). Antihypertensive agents in hemodialysis patients: A current perspective. <em>Seminars in Dialysis, "
                  "23</em>(3), 290&ndash;297. " + _doi("10.1111/j.1525-139X.2009.00697.x")),
    "singh2022": ("Singh, A. T., Waikar, S. S., &amp; Mc Causland, F. R. (2022). Association of different definitions of intradialytic hypertension "
                  "with long-term mortality in hemodialysis. <em>Hypertension, 79</em>(4), 855&ndash;862. " + _doi("10.1161/HYPERTENSIONAHA.121.18058")),
    "adejumo2024": ("Adejumo, O. A., Edeki, I. R., Oyedepo, D. S., Yisau, O. E., Ige, O. O., Ekrikpo, I. U., Moussa, A. S., Palencia, H., "
                    "Noubiap, J. J., &amp; Ekrikpo, U. E. (2024). The prevalence and risk of mortality associated with intradialytic hypertension "
                    "among patients with end-stage kidney disease on haemodialysis: A systematic review and meta-analysis. <em>PLOS ONE, "
                    "19</em>(6), Article e0304633. " + _doi("10.1371/journal.pone.0304633")),
    "iatridi2023": ("Iatridi, F., Theodorakopoulou, M. P., Karpetas, A., Sgouropoulou, V., Georgiou, A., Karkamani, E., Karagiannidis, A., "
                    "Papagianni, A., &amp; Sarafidis, P. (2023). Association of intradialytic hypertension with future cardiovascular events and "
                    "mortality in hemodialysis patients: Effects of ambulatory blood pressure. <em>American Journal of Nephrology, 54</em>(7&ndash;8), "
                    "299&ndash;307. " + _doi("10.1159/000531477")),
    "vanburen2016": ("Van Buren, P. N., &amp; Inrig, J. K. (2016). Mechanisms and treatment of intradialytic hypertension. <em>Blood Purification, "
                     "41</em>(1&ndash;3), 188&ndash;193. " + _doi("10.1159/000441313")),
    "iatridi2022": ("Iatridi, F., Theodorakopoulou, M. P., Papagianni, A., &amp; Sarafidis, P. (2022). Intradialytic hypertension: Epidemiology and "
                    "pathophysiology of a silent killer. <em>Hypertension Research, 45</em>(11), 1713&ndash;1725. " + _doi("10.1038/s41440-022-01001-3")),
    "bress2024": ("Bress, A. P., Anderson, T. S., Flack, J. M., Ghazi, L., Hall, M. E., Laffer, C. L., Still, C. H., Taler, S. J., Zachrison, K. S., "
                  "Chang, T. I., &amp; American Heart Association Council on Hypertension; Council on Cardiovascular and Stroke Nursing; and Council "
                  "on Clinical Cardiology. (2024). The management of elevated blood pressure in the acute care setting: A scientific statement "
                  "from the American Heart Association. <em>Hypertension, 81</em>(8), e94&ndash;e106. " + _doi("10.1161/HYP.0000000000000238")),
    "jones2025": ("Jones, D. W., Ferdinand, K. C., Taler, S. J., Johnson, H. M., Shimbo, D., Abdalla, M., Altieri, M. M., Bansal, N., Bello, N. A., "
                  "Bress, A. P., Carter, J., Cohen, J. B., Collins, K. J., Commodore-Mensah, Y., Davis, L. L., Egan, B., Khan, S. S., "
                  "Lloyd-Jones, D. M., Melnyk, B. M., . . . Williamson, J. D. (2025). 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM "
                  "guideline for the prevention, detection, evaluation and management of high blood pressure in adults: A report of the "
                  "American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. "
                  "<em>Circulation, 152</em>(11), e114&ndash;e218. " + _doi("10.1161/CIR.0000000000001356")),
}
