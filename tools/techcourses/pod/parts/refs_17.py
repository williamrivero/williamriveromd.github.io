# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 17 (APA 7). Each journal entry was checked against PubMed metadata
(authors, year, title, journal, volume, issue, pages, DOI) on November 25, 2026. Surviving Sepsis Campaign 2021 grades were checked
against the guideline full text (PMC8486643); 2026 statements and grades were checked against the Society of Critical Care
Medicine guideline page the same day (PubMed 41869847; the same guideline also appears in Intensive Care Medicine, PubMed 41870560). Keys already defined in the course (idsa_crbsi2009, lok2020,
cdc_dialysis_bsi2024, patel2013, hall2021, daugirdas2015, greenberg2021) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "prescott2026": ("Prescott, H. C., Antonelli, M., Alhazzani, W., M&oslash;ller, M. H., Alshamsi, F., Azevedo, L. C. P., Belley-Cote, E., "
                     "De Waele, J., Derde, L., Dionne, J. C., Evans, L., Gershengorn, H. B., Hodgson, C. L., Honarmand, K., Kesecioglu, J., "
                     "McIntyre, L., Mer, M., Nunnally, M. E., Oczkowski, S. J. W., . . . Coopersmith, C. M. (2026). Surviving Sepsis "
                     "Campaign: International guidelines for management of sepsis and septic shock 2026. <em>Critical Care Medicine, "
                     "54</em>(4), 725&ndash;812. " + _doi("10.1097/CCM.0000000000007075")),
    "evans2021": ("Evans, L., Rhodes, A., Alhazzani, W., Antonelli, M., Coopersmith, C. M., French, C., Machado, F. R., Mcintyre, L., "
                  "Ostermann, M., Prescott, H. C., Schorr, C., Simpson, S., Wiersinga, W. J., Alshamsi, F., Angus, D. C., Arabi, Y., "
                  "Azevedo, L., Beale, R., Beilman, G., . . . Levy, M. (2021). Surviving sepsis campaign: International guidelines for "
                  "management of sepsis and septic shock 2021. <em>Intensive Care Medicine, 47</em>(11), 1181&ndash;1247. "
                  + _doi("10.1007/s00134-021-06506-y")),
    "singer2016": ("Singer, M., Deutschman, C. S., Seymour, C. W., Shankar-Hari, M., Annane, D., Bauer, M., Bellomo, R., Bernard, G. R., "
                   "Chiche, J.-D., Coopersmith, C. M., Hotchkiss, R. S., Levy, M. M., Marshall, J. C., Martin, G. S., Opal, S. M., "
                   "Rubenfeld, G. D., van der Poll, T., Vincent, J.-L., &amp; Angus, D. C. (2016). The Third International Consensus "
                   "Definitions for Sepsis and Septic Shock (Sepsis-3). <em>JAMA, 315</em>(8), 801&ndash;810. "
                   + _doi("10.1001/jama.2016.0287")),
    "seymour2016": ("Seymour, C. W., Liu, V. X., Iwashyna, T. J., Brunkhorst, F. M., Rea, T. D., Scherag, A., Rubenfeld, G., Kahn, J. M., "
                    "Shankar-Hari, M., Singer, M., Deutschman, C. S., Escobar, G. J., &amp; Angus, D. C. (2016). Assessment of clinical "
                    "criteria for sepsis: For the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). "
                    "<em>JAMA, 315</em>(8), 762&ndash;774. " + _doi("10.1001/jama.2016.0288")),
    "quittnatpelletier2016": ("Quittnat Pelletier, F., Joarder, M., Poutanen, S. M., &amp; Lok, C. E. (2016). Evaluating approaches for the "
                              "diagnosis of hemodialysis catheter-related bloodstream infections. <em>Clinical Journal of the American "
                              "Society of Nephrology, 11</em>(5), 847&ndash;854. " + _doi("10.2215/CJN.09110815")),
    "rha2023": ("Rha, B., See, I., Dunham, L., Kutty, P. K., Moccia, L., Apata, I. W., Ahern, J., Jung, S., Li, R., Nadle, J., Petit, S., "
                "Ray, S. M., Harrison, L. H., Bernu, C., Lynfield, R., Dumyati, G., Tracy, M., Schaffner, W., Ham, D. C., . . . Novosad, S. "
                "(2023). Vital signs: Health disparities in hemodialysis-associated <em>Staphylococcus aureus</em> bloodstream infections, "
                "United States, 2017&ndash;2020. <em>MMWR. Morbidity and Mortality Weekly Report, 72</em>(6), 153&ndash;159. "
                + _doi("10.15585/mmwr.mm7206e1")),
    "kantor1983": ("Kantor, R. J., Carson, L. A., Graham, D. R., Petersen, N. J., &amp; Favero, M. S. (1983). Outbreak of pyrogenic "
                   "reactions at a dialysis center: Association with infusion of heparinized saline solution. <em>The American Journal "
                   "of Medicine, 74</em>(3), 449&ndash;456. " + _doi("10.1016/0002-9343(83)90978-6")),
    "hindman1975": ("Hindman, S. H., Favero, M. S., Carson, L. A., Petersen, N. J., Schonberger, L. B., &amp; Solano, J. T. (1975). "
                    "Pyrogenic reactions during haemodialysis caused by extramural endotoxin. <em>The Lancet, 2</em>(7938), 732&ndash;734. "
                    + _doi("10.1016/s0140-6736(75)90721-7")),
    "jackson1994": ("Jackson, B. M., Beck-Sague, C. M., Bland, L. A., Arduino, M. J., Meyer, L., &amp; Jarvis, W. R. (1994). Outbreak of "
                    "pyrogenic reactions and gram-negative bacteremia in a hemodialysis center. <em>American Journal of Nephrology, "
                    "14</em>(2), 85&ndash;89. " + _doi("10.1159/000168694")),
    "gordon1992": ("Gordon, S. M., Oettinger, C. W., Bland, L. A., Oliver, J. C., Arduino, M. J., Aguero, S. M., McAllister, S. K., "
                   "Favero, M. S., &amp; Jarvis, W. R. (1992). Pyrogenic reactions in patients receiving conventional, high-efficiency, "
                   "or high-flux hemodialysis treatments with bicarbonate dialysate containing high concentrations of bacteria and "
                   "endotoxin. <em>Journal of the American Society of Nephrology, 2</em>(9), 1436&ndash;1444. "
                   + _doi("10.1681/ASN.V291436")),
    "pericas2021": ("Peric&agrave;s, J. M., Llopis, J., Jim&eacute;nez-Exposito, M. J., Kourany, W. M., Almirante, B., Carosi, G., "
                    "Durante-Mangoni, E., Fortes, C. Q., Giannitsioti, E., Lerakis, S., Montagna-Mella, R., Ambrosioni, J., Tan, R.-S., "
                    "Mestres, C. A., Wray, D., Pachirat, O., Moreno, A., Chu, V. H., de Lazzari, E., . . . Mir&oacute;, J. M. (2021). "
                    "Infective endocarditis in patients on chronic hemodialysis. <em>Journal of the American College of Cardiology, "
                    "77</em>(13), 1629&ndash;1640. " + _doi("10.1016/j.jacc.2021.02.014")),
    "alchalabi2023": ("Al-Chalabi, S., Tay, T., Chinnadurai, R., &amp; Kalra, P. A. (2023). Risk factors for infective endocarditis in "
                      "patients receiving hemodialysis: A propensity score matched cohort study. <em>Clinical Nephrology, 100</em>(2), "
                      "51&ndash;59. " + _doi("10.5414/CN111117")),
    "holland2014": ("Holland, T. L., Arnold, C., &amp; Fowler, V. G., Jr. (2014). Clinical management of <em>Staphylococcus aureus</em> "
                    "bacteremia: A review. <em>JAMA, 312</em>(13), 1330&ndash;1341. " + _doi("10.1001/jama.2014.9743")),
    "madhavan2019": ("Madhavan, K., Chieng, L. O., Armstrong, V. L., &amp; Wang, M. Y. (2019). Spondylodiscitis in end-stage renal disease: "
                     "A systematic review. <em>Journal of Neurosurgery: Spine, 30</em>(5), 674&ndash;682. "
                     + _doi("10.3171/2018.9.SPINE18824")),
    "philipneri2003": ("Philipneri, M., Al-Aly, Z., Amin, K., Gellens, M. E., &amp; Bastani, B. (2003). Routine replacement of tunneled, "
                       "cuffed, hemodialysis catheters eliminates paraspinal/vertebral infections in patients with catheter-associated "
                       "bacteremia. <em>American Journal of Nephrology, 23</em>(4), 202&ndash;207. " + _doi("10.1159/000071479")),
    "cdc_core2013": ("Centers for Disease Control and Prevention. (2013). <em>CDC approach to BSI prevention in dialysis facilities (i.e., the "
                     "Core Interventions for dialysis bloodstream infection (BSI) prevention)</em> [Fact sheet]. "
                     '<a href="https://www.cdc.gov/dialysis/PDFs/Dialysis-Core-Interventions-5_10_13.pdf">'
                     "https://www.cdc.gov/dialysis/PDFs/Dialysis-Core-Interventions-5_10_13.pdf</a>"),
}
