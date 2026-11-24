# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 08 (APA 7). Each entry was built from PubMed metadata
checked on November 25, 2026. Keys already defined in pod/refs.py and its parts (flythe2011, kalantar2009, torino2016,
kdigo_bpvol2020, daugirdas2001, daugirdas2015, obi2016, hall2021) are not repeated.
Module 08 owns the shared keys zoccali2013 and agarwal2009drip; module 14 reuses them."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "zoccali2013": ("Zoccali, C., Torino, C., Tripepi, R., Tripepi, G., D&rsquo;Arrigo, G., Postorino, M., Gargani, L., Sicari, R., Picano, E., "
                    "Mallamaci, F., &amp; Lung US in CKD Working Group. (2013). Pulmonary congestion predicts cardiac events and mortality in ESRD. "
                    "<em>Journal of the American Society of Nephrology, 24</em>(4), 639&ndash;646. " + _doi("10.1681/ASN.2012100990")),
    "agarwal2009drip": ("Agarwal, R., Alborzi, P., Satyan, S., &amp; Light, R. P. (2009). Dry-weight reduction in hypertensive hemodialysis "
                        "patients (DRIP): A randomized, controlled trial. <em>Hypertension, 53</em>(3), 500&ndash;507. "
                        + _doi("10.1161/HYPERTENSIONAHA.108.125674")),
    "zoccali2021": ("Zoccali, C., Torino, C., Mallamaci, F., Sarafidis, P., Papagianni, A., Ekart, R., Hojs, R., Klinger, M., Letachowicz, K., "
                    "Fliser, D., Seiler-Mu&szlig;ler, S., Lizzi, F., Wiecek, A., Miskiewicz, A., Siamopoulos, K., Balafa, O., Slotki, I., Shavit, L., "
                    "Stavroulopoulos, A., . . . London, G. M. (2021). A randomized multicenter trial on a lung ultrasound-guided treatment strategy "
                    "in patients on chronic hemodialysis with high cardiovascular risk. <em>Kidney International, 100</em>(6), 1325&ndash;1333. "
                    + _doi("10.1016/j.kint.2021.07.024")),
    "loutradis2020": ("Loutradis, C., Papagianni, A., Ekart, R., Theodorakopoulou, M., Minopoulou, I., Pagourelias, E., Douma, S., Karagiannis, A., "
                      "Mallamaci, F., Zoccali, C., London, G., &amp; Sarafidis, P. A. (2020). Excess volume removal following lung ultrasound "
                      "evaluation decreases central blood pressure and pulse wave velocity in hemodialysis patients: A LUST sub-study. "
                      "<em>Journal of Nephrology, 33</em>(6), 1289&ndash;1300. " + _doi("10.1007/s40620-020-00745-w")),
    "siriopol2017": ("Siriopol, D., Onofriescu, M., Voroneanu, L., Apetrii, M., Nistor, I., Hogas, S., Kanbay, M., Sascau, R., Scripcariu, D., "
                     "&amp; Covic, A. (2017). Dry weight assessment by combined ultrasound and bioimpedance monitoring in low cardiovascular risk "
                     "hemodialysis patients: A randomized controlled trial. <em>International Urology and Nephrology, 49</em>(1), 143&ndash;153. "
                     + _doi("10.1007/s11255-016-1471-0")),
    "hur2013": ("Hur, E., Usta, M., Toz, H., Asci, G., Wabel, P., Kahvecioglu, S., Kayikcioglu, M., Demirci, M. S., Ozkahya, M., Duman, S., "
                "&amp; Ok, E. (2013). Effect of fluid management guided by bioimpedance spectroscopy on cardiovascular parameters in hemodialysis "
                "patients: A randomized controlled trial. <em>American Journal of Kidney Diseases, 61</em>(6), 957&ndash;965. "
                + _doi("10.1053/j.ajkd.2012.12.017")),
    "onofriescu2014": ("Onofriescu, M., Hogas, S., Voroneanu, L., Apetrii, M., Nistor, I., Kanbay, M., &amp; Covic, A. C. (2014). "
                       "Bioimpedance-guided fluid management in maintenance hemodialysis: A pilot randomized controlled trial. "
                       "<em>American Journal of Kidney Diseases, 64</em>(1), 111&ndash;118. " + _doi("10.1053/j.ajkd.2014.01.420")),
    "tabinor2018": ("Tabinor, M., &amp; Davies, S. J. (2018). The use of bioimpedance spectroscopy to guide fluid management in patients receiving "
                    "dialysis. <em>Current Opinion in Nephrology and Hypertension, 27</em>(6), 406&ndash;412. " + _doi("10.1097/MNH.0000000000000445")),
    "davies2025": ("Davies, S. J., Coyle, D., Lindley, E., Keane, D., Belcher, J., Caskey, F., Dasgupta, I., Davenport, A., Farrington, K., "
                   "Mitra, S., Ormandy, P., Wilkie, M., MacDonald, J., Zanganeh, M., Andronis, L., Solis-Trapala, I., &amp; Sim, J. (2025). "
                   "BioImpedance Spectroscopy to maintain Renal Output: The BISTRO randomised controlled trial. "
                   "<em>Health Technology Assessment, 29</em>(32), 1&ndash;24. " + _doi("10.3310/RHON2378")),
    "wizemann2009": ("Wizemann, V., Wabel, P., Chamney, P., Zaluska, W., Moissl, U., Rode, C., Malecka-Masalska, T., &amp; Marcelli, D. (2009). "
                     "The mortality risk of overhydration in haemodialysis patients. <em>Nephrology Dialysis Transplantation, 24</em>(5), "
                     "1574&ndash;1579. " + _doi("10.1093/ndt/gfn707")),
    "hecking2013": ("Hecking, M., Karaboyas, A., Antlanger, M., Saran, R., Wizemann, V., Chazot, C., Rayner, H., H&ouml;rl, W. H., Pisoni, R. L., "
                    "Robinson, B. M., Sunder-Plassmann, G., Moissl, U., Kotanko, P., Levin, N. W., S&auml;emann, M. D., Kalantar-Zadeh, K., "
                    "Port, F. K., &amp; Wabel, P. (2013). Significance of interdialytic weight gain versus chronic volume overload: Consensus "
                    "opinion. <em>American Journal of Nephrology, 38</em>(1), 78&ndash;90. " + _doi("10.1159/000353104")),
    "assimon2016": ("Assimon, M. M., Wenger, J. B., Wang, L., &amp; Flythe, J. E. (2016). Ultrafiltration rate and mortality in maintenance "
                    "hemodialysis patients. <em>American Journal of Kidney Diseases, 68</em>(6), 911&ndash;922. " + _doi("10.1053/j.ajkd.2016.06.020")),
    "mermelstein2023": ("Mermelstein, A., Raimann, J. G., Wang, Y., Kotanko, P., &amp; Daugirdas, J. T. (2023). Ultrafiltration rate levels in "
                        "hemodialysis patients associated with weight-specific mortality risks. <em>Clinical Journal of the American Society of "
                        "Nephrology, 18</em>(6), 767&ndash;776. " + _doi("10.2215/CJN.0000000000000144")),
    "sars2020": ("Sars, B., van der Sande, F. M., &amp; Kooman, J. P. (2020). Intradialytic hypotension: Mechanisms and outcome. "
                 "<em>Blood Purification, 49</em>(1&ndash;2), 158&ndash;167. " + _doi("10.1159/000503776")),
}
