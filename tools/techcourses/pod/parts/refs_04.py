# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 04 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod/refs.py (defilippi2017, thygesen2018, hall2021, daugirdas2015) are not repeated.
kdigo_ckd2024 is defined here because it is not yet in the live course; if Module 03 defines it first, keep one copy."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "jankowski2021": ("Jankowski, J., Floege, J., Fliser, D., B&ouml;hm, M., &amp; Marx, N. (2021). Cardiovascular disease in chronic kidney disease: "
                      "Pathophysiological insights and therapeutic options. <em>Circulation, 143</em>(11), 1157&ndash;1172. "
                      + _doi("10.1161/CIRCULATIONAHA.120.050686")),
    "go2004": ("Go, A. S., Chertow, G. M., Fan, D., McCulloch, C. E., &amp; Hsu, C. Y. (2004). Chronic kidney disease and the risks of death, "
               "cardiovascular events, and hospitalization. <em>New England Journal of Medicine, 351</em>(13), 1296&ndash;1305. "
               + _doi("10.1056/NEJMoa041031")),
    "wanner2005": ("Wanner, C., Krane, V., M&auml;rz, W., Olschewski, M., Mann, J. F., Ruf, G., Ritz, E., &amp; German Diabetes and Dialysis Study "
                   "Investigators. (2005). Atorvastatin in patients with type 2 diabetes mellitus undergoing hemodialysis. <em>New England Journal "
                   "of Medicine, 353</em>(3), 238&ndash;248. " + _doi("10.1056/NEJMoa043545")),
    "fellstrom2009": ("Fellstr&ouml;m, B. C., Jardine, A. G., Schmieder, R. E., Holdaas, H., Bannister, K., Beutler, J., Chae, D. W., Chevaile, A., "
                      "Cobbe, S. M., Gr&ouml;nhagen-Riska, C., De Lima, J. J., Lins, R., Mayer, G., McMahon, A. W., Parving, H. H., Remuzzi, G., "
                      "Samuelsson, O., Sonkodi, S., Sci, D., . . . AURORA Study Group. (2009). Rosuvastatin and cardiovascular events in patients "
                      "undergoing hemodialysis. <em>New England Journal of Medicine, 360</em>(14), 1395&ndash;1407. " + _doi("10.1056/NEJMoa0810177")),
    "baigent2011": ("Baigent, C., Landray, M. J., Reith, C., Emberson, J., Wheeler, D. C., Tomson, C., Wanner, C., Krane, V., Cass, A., Craig, J., "
                    "Neal, B., Jiang, L., Hooi, L. S., Levin, A., Agodoa, L., Gaziano, M., Kasiske, B., Walker, R., Massy, Z. A., . . . SHARP "
                    "Investigators. (2011). The effects of lowering LDL cholesterol with simvastatin plus ezetimibe in patients with chronic kidney "
                    "disease (Study of Heart and Renal Protection): A randomised placebo-controlled trial. <em>The Lancet, 377</em>(9784), "
                    "2181&ndash;2192. " + _doi("10.1016/S0140-6736(11)60739-3")),
    "kdigo_lipid2014": ("Wanner, C., Tonelli, M., &amp; Kidney Disease: Improving Global Outcomes Lipid Guideline Development Work Group Members. (2014). "
                        "KDIGO clinical practice guideline for lipid management in CKD: Summary of recommendation statements and clinical approach "
                        "to the patient. <em>Kidney International, 85</em>(6), 1303&ndash;1309. " + _doi("10.1038/ki.2014.31")),
    "pianta2012": ("Pianta, T. J., Horvath, A. R., Ellis, V. M., Leonetti, R., Moffat, C., Josland, E. A., &amp; Brown, M. A. (2012). Cardiac "
                   "high-sensitivity troponin T measurement: A layer of complexity in managing haemodialysis patients. <em>Nephrology, 17</em>(7), "
                   "636&ndash;641. " + _doi("10.1111/j.1440-1797.2012.01625.x")),
    "artunc2019": ("Artunc, F., Haag, S., Friedrich, B., Mueller, C., H&auml;ring, H. U., &amp; Peter, A. (2019). Performance of a novel high "
                   "sensitivity cardiac troponin I assay in asymptomatic hemodialysis patients: Evidence for sex-specific differences. "
                   "<em>Clinical Chemistry and Laboratory Medicine, 57</em>(8), 1261&ndash;1270. " + _doi("10.1515/cclm-2018-1176")),
    "kraus2018": ("Kraus, D., von Jeinsen, B., Tzikas, S., Palapies, L., Zeller, T., Bickel, C., Fette, G., Lackner, K. J., Drechsler, C., "
                  "Neumann, J. T., Baldus, S., Blankenberg, S., M&uuml;nzel, T., Wanner, C., Zeiher, A. M., &amp; Keller, T. (2018). Cardiac "
                  "troponins for the diagnosis of acute myocardial infarction in chronic kidney disease. <em>Journal of the American Heart "
                  "Association, 7</em>(19), Article e008032. " + _doi("10.1161/JAHA.117.008032")),
    "knott2024": ("Knott, J. D., Ola, O., De Michieli, L., Akula, A., Mehta, R. A., Dworak, M., Crockford, E., Lobo, R., Slusser, J., Rastas, N., "
                  "Karturi, S., Wohlrab, S., Hodge, D. O., Grube, E., Tak, T., Cagin, C., Gulati, R., Sandoval, Y., &amp; Jaffe, A. S. (2024). "
                  "Diagnosis of acute myocardial infarction in patients with renal failure using high-sensitivity cardiac troponin T. "
                  "<em>European Heart Journal: Acute Cardiovascular Care, 13</em>(7), 546&ndash;558. " + _doi("10.1093/ehjacc/zuae079")),
    "gallacher2022": ("Gallacher, P. J., Miller-Hodges, E., Shah, A. S. V., Farrah, T. E., Halbesma, N., Blackmur, J. P., Chapman, A. R., "
                      "Adamson, P. D., Anand, A., Strachan, F. E., Ferry, A. V., Lee, K. K., Berry, C., Findlay, I., Cruickshank, A., Reid, A., "
                      "Gray, A., Collinson, P. O., Apple, F. S., . . . High-STEACS Investigators. (2022). High-sensitivity cardiac troponin and the "
                      "diagnosis of myocardial infarction in patients with kidney impairment. <em>Kidney International, 102</em>(1), 149&ndash;159. "
                      + _doi("10.1016/j.kint.2022.02.019")),
    "yang2020": ("Yang, W. L., Fahim, M., &amp; Johnson, D. W. (2020). Pathophysiology and significance of natriuretic peptides in patients with "
                 "end-stage kidney disease. <em>Clinical Biochemistry, 83</em>, 1&ndash;11. " + _doi("10.1016/j.clinbiochem.2020.05.013")),
    "hedges2007": ("Hedges, S. J., Dehoney, S. B., Hooper, J. S., Amanzadeh, J., &amp; Busti, A. J. (2007). Evidence-based treatment "
                   "recommendations for uremic bleeding. <em>Nature Clinical Practice Nephrology, 3</em>(3), 138&ndash;153. "
                   + _doi("10.1038/ncpneph0421")),
    "kdigo_anemia2026": ("Babitt, J. L., Berns, J. S., Bozkurt, B., Cheung Khedairy, R. S., Cuevas, Y., Effa, E. E., Eisenga, M. F., Fishbane, S., "
                         "Ginzburg, Y. Z., Haase, V. H., Hedayati, S. S., Kim, S., Moura-Neto, J. A., Nagler, E. V., Rossignol, P., Sahay, M., "
                         "Tanaka, T., Yee-Moon Wang, A., Wheeler, D. C., . . . Tonelli, M. (2026). Executive summary of the KDIGO 2026 clinical "
                         "practice guideline for the management of anemia in chronic kidney disease (CKD). <em>Kidney International, 109</em>(1), "
                         "44&ndash;56. " + _doi("10.1016/j.kint.2025.06.005")),
    "kdigo_mbd2017": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD-MBD Update Work Group. (2017). KDIGO 2017 clinical practice guideline "
                      "update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease-mineral and bone disorder (CKD-MBD). "
                      "<em>Kidney International Supplements, 7</em>(1), 1&ndash;59. " + _doi("10.1016/j.kisu.2017.04.001")),
    "payne1973": ("Payne, R. B., Little, A. J., Williams, R. B., &amp; Milner, J. R. (1973). Interpretation of serum calcium in patients with "
                  "abnormal serum proteins. <em>British Medical Journal, 4</em>(5893), 643&ndash;646. " + _doi("10.1136/bmj.4.5893.643")),
    "clase2000": ("Clase, C. M., Norman, G. L., Beecroft, M. L., &amp; Churchill, D. N. (2000). Albumin-corrected calcium and ionized calcium in "
                  "stable haemodialysis patients. <em>Nephrology Dialysis Transplantation, 15</em>(11), 1841&ndash;1846. "
                  + _doi("10.1093/ndt/15.11.1841")),
    "kato2008": ("Kato, S., Chmielewski, M., Honda, H., Pecoits-Filho, R., Matsuo, S., Yuzawa, Y., Tranaeus, A., Stenvinkel, P., &amp; "
                 "Lindholm, B. (2008). Aspects of immune dysfunction in end-stage renal disease. <em>Clinical Journal of the American Society of "
                 "Nephrology, 3</em>(5), 1526&ndash;1533. " + _doi("10.2215/CJN.00950208")),
    "sarnak2000": ("Sarnak, M. J., &amp; Jaber, B. L. (2000). Mortality caused by sepsis in patients with end-stage renal disease compared with "
                   "the general population. <em>Kidney International, 58</em>(4), 1758&ndash;1764. " + _doi("10.1111/j.1523-1755.2000.00337.x")),
    "peacock2008": ("Peacock, T. P., Shihabi, Z. K., Bleyer, A. J., Dolbare, E. L., Byers, J. R., Knovich, M. A., Calles-Escandon, J., "
                    "Russell, G. B., &amp; Freedman, B. I. (2008). Comparison of glycated albumin and hemoglobin A(1c) levels in diabetic subjects "
                    "on hemodialysis. <em>Kidney International, 73</em>(9), 1062&ndash;1068. " + _doi("10.1038/ki.2008.25")),
    "kdigo_dm2022": ("Kidney Disease: Improving Global Outcomes (KDIGO) Diabetes Work Group. (2022). KDIGO 2022 clinical practice guideline for "
                     "diabetes management in chronic kidney disease. <em>Kidney International, 102</em>(5S), S1&ndash;S127. "
                     + _doi("10.1016/j.kint.2022.06.008")),
    "nathan2008": ("Nathan, D. M., Kuenen, J., Borg, R., Zheng, H., Schoenfeld, D., Heine, R. J., &amp; A1c-Derived Average Glucose Study Group. "
                   "(2008). Translating the A1C assay into estimated average glucose values. <em>Diabetes Care, 31</em>(8), 1473&ndash;1478. "
                   + _doi("10.2337/dc08-0545")),
    "lindner2014": ("Lindner, G., Funk, G. C., Pfortmueller, C. A., Leichtle, A. B., Fiedler, G. M., Schwarz, C., Exadaktylos, A. K., &amp; "
                    "Puig, S. (2014). D-dimer to rule out pulmonary embolism in renal insufficiency. <em>The American Journal of Medicine, "
                    "127</em>(4), 343&ndash;347. " + _doi("10.1016/j.amjmed.2013.12.003")),
    "matzke2011": ("Matzke, G. R., Aronoff, G. R., Atkinson, A. J., Bennett, W. M., Decker, B. S., Eckardt, K. U., Golper, T., Grabe, D. W., "
                   "Kasiske, B., Keller, F., Kielstein, J. T., Mehta, R., Mueller, B. A., Pasko, D. A., Schaefer, F., Sica, D. A., Inker, L. A., "
                   "Umans, J. G., &amp; Murray, P. (2011). Drug dosing consideration in patients with acute and chronic kidney disease: A clinical "
                   "update from Kidney Disease: Improving Global Outcomes (KDIGO). <em>Kidney International, 80</em>(11), 1122&ndash;1137. "
                   + _doi("10.1038/ki.2011.322")),
    "kdigo_ckd2024": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. (2024). KDIGO 2024 clinical practice guideline for the "
                      "evaluation and management of chronic kidney disease. <em>Kidney International, 105</em>(4S), S117&ndash;S314. "
                      + _doi("10.1016/j.kint.2023.10.018")),
}
