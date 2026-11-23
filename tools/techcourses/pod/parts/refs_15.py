# -*- coding: utf-8 -*-
"""New references for Physician on Duty Module 15 (APA 7). Author lists, volumes, pages, and DOIs were copied from
PubMed metadata on November 23, 2026. Keys already in pod_src/refs.py (daugirdas2015, foley2011, montague2008,
palmer2016, and others) are not redefined here."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


_AHA2025 = ("2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care. "
            "<em>Circulation, 152</em>(16_suppl_2), ")

REFS = {
    "erc2025_special": ("Lott, C., Karageorgos, V., Abelairas-Gomez, C., Alfonzo, A., Bierens, J., Cantellow, S., Debaty, G., Einav, S., "
                        "Fischer, M., Gonz&aacute;lez-Salvado, V., Greif, R., Metelmann, B., Metelmann, C., Meyer, T., Paal, P., Peran, D., "
                        "Scapigliati, A., Spartinou, A., Thies, K., . . . Deakin, C. D. (2025). European Resuscitation Council guidelines 2025 "
                        "special circumstances in resuscitation. <em>Resuscitation, 215</em>(Suppl. 1), Article 110753. "
                        + _doi("10.1016/j.resuscitation.2025.110753")),
    "aha2025_special": ("Cao, D., Arens, A. M., Chow, S. L., Easter, S. R., Hoffman, R. S., Lagina, A. T., Lavonas, E. J., Patil, K. D., "
                        "Sutherland, L. D., Tijssen, J. A., Wang, G. S., Zelop, C. M., Rodriguez, A. J., Drennan, I. R., &amp; McBride, M. E. (2025). "
                        "Part 10: Adult and pediatric special circumstances of resuscitation: " + _AHA2025 + "S578&ndash;S672. "
                        + _doi("10.1161/CIR.0000000000001380")),
    "aha2025_bls": ("Kleinman, M. E., Buick, J. E., Huber, N., Idris, A. H., Levy, M., Morgan, S. G., Nassal, M. M. J., Neth, M. R., Norii, T., "
                    "Nunnally, M. E., Rodriguez, A. J., Walsh, B. K., &amp; Drennan, I. R. (2025). Part 7: Adult basic life support: "
                    + _AHA2025 + "S448&ndash;S478. " + _doi("10.1161/CIR.0000000000001369")),
    "aha2025_systems": ("Dezfulian, C., Caba&ntilde;as, J. G., Buckley, J. R., Cash, R. E., Crowe, R. P., Drennan, I. R., Mahgoub, M., "
                        "Mannarino, C. N., May, T., Salcido, D. D., Uzendu, A. I., Vogelsong, M. A., Worth, J. A., &amp; Girotra, S. (2025). "
                        "Part 4: Systems of care: " + _AHA2025 + "S353&ndash;S384. " + _doi("10.1161/CIR.0000000000001378")),
    "greenberg2021": ("Greenberg, K. I., &amp; Choi, M. J. (2021). Hemodialysis emergencies: Core Curriculum 2021. "
                      "<em>American Journal of Kidney Diseases, 77</em>(5), 796&ndash;809. " + _doi("10.1053/j.ajkd.2020.11.024")),
    "karnik2001": ("Karnik, J. A., Young, B. S., Lew, N. L., Herget, M., Dubinsky, C., Lazarus, J. M., &amp; Chertow, G. M. (2001). "
                   "Cardiac arrest and sudden death in dialysis units. <em>Kidney International, 60</em>(1), 350&ndash;357. "
                   + _doi("10.1046/j.1523-1755.2001.00806.x")),
    "davis2008": ("Davis, T. R., Young, B. A., Eisenberg, M. S., Rea, T. D., Copass, M. K., &amp; Cobb, L. A. (2008). Outcome of cardiac arrests "
                  "attended by emergency medical services staff at community outpatient dialysis centers. "
                  "<em>Kidney International, 73</em>(8), 933&ndash;939. " + _doi("10.1038/sj.ki.5002749")),
    "pun2011": ("Pun, P. H., Lehrich, R. W., Honeycutt, E. F., Herzog, C. A., &amp; Middleton, J. P. (2011). Modifiable risk factors associated "
                "with sudden cardiac arrest within hemodialysis clinics. <em>Kidney International, 79</em>(2), 218&ndash;227. "
                + _doi("10.1038/ki.2010.315")),
    "pun2019": ("Pun, P. H., Dupre, M. E., Starks, M. A., Tyson, C., Vellano, K., Svetkey, L. P., Hansen, S., Frizzelle, B. G., McNally, B., "
                "Jollis, J. G., Al-Khatib, S. M., &amp; Granger, C. B. (2019). Outcomes for hemodialysis patients given cardiopulmonary "
                "resuscitation for cardiac arrest at outpatient dialysis clinics. "
                "<em>Journal of the American Society of Nephrology, 30</em>(3), 461&ndash;470. " + _doi("10.1681/ASN.2018090911")),
    "herzog2007": ("Herzog, C. A., Littrell, K., Arko, C., Frederick, P. D., &amp; Blaney, M. (2007). Clinical characteristics of dialysis "
                   "patients with acute myocardial infarction in the United States: A collaborative project of the United States Renal Data "
                   "System and the National Registry of Myocardial Infarction. <em>Circulation, 116</em>(13), 1465&ndash;1472. "
                   + _doi("10.1161/CIRCULATIONAHA.107.696765")),
    "defilippi2017": ("deFilippi, C. R., &amp; Herzog, C. A. (2017). Interpreting cardiac biomarkers in the setting of chronic kidney disease. "
                      "<em>Clinical Chemistry, 63</em>(1), 59&ndash;65. " + _doi("10.1373/clinchem.2016.254748")),
    "thygesen2018": ("Thygesen, K., Alpert, J. S., Jaffe, A. S., Chaitman, B. R., Bax, J. J., Morrow, D. A., &amp; White, H. D. (2018). "
                     "Fourth universal definition of myocardial infarction (2018). <em>Circulation, 138</em>(20), e618&ndash;e651. "
                     + _doi("10.1161/CIR.0000000000000617")),
    "gulati2021": ("Gulati, M., Levy, P. D., Mukherjee, D., Amsterdam, E., Bhatt, D. L., Birtcher, K. K., Blankstein, R., Boyd, J., "
                   "Bullock-Palmer, R. P., Conejo, T., Diercks, D. B., Gentile, F., Greenwood, J. P., Hess, E. P., Hollenberg, S. M., "
                   "Jaber, W. A., Jneid, H., Joglar, J. A., Morrow, D. A., . . . Shaw, L. J. (2021). 2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR "
                   "guideline for the evaluation and diagnosis of chest pain: A report of the American College of Cardiology/American Heart "
                   "Association Joint Committee on Clinical Practice Guidelines. <em>Circulation, 144</em>(22), e368&ndash;e454. "
                   + _doi("10.1161/CIR.0000000000001029")),
    "roychaudhury2018": ("Roy-Chaudhury, P., Tumlin, J. A., Koplan, B. A., Costea, A. I., Kher, V., Williamson, D., Pokhariyal, S., &amp; "
                         "Charytan, D. M. (2018). Primary outcomes of the Monitoring in Dialysis Study indicate that clinically significant "
                         "arrhythmias are common in hemodialysis patients and related to dialytic cycle. "
                         "<em>Kidney International, 93</em>(4), 941&ndash;951. " + _doi("10.1016/j.kint.2017.11.019")),
    "buiten2014": ("Buiten, M. S., de Bie, M. K., Rotmans, J. I., Gabre&euml;ls, B. A., van Dorp, W., Wolterbeek, R., Trines, S. A., "
                   "Schalij, M. J., Jukema, J. W., Rabelink, T. J., &amp; van Erven, L. (2014). The dialysis procedure as a trigger for atrial "
                   "fibrillation: New insights in the development of atrial fibrillation in dialysis patients. <em>Heart, 100</em>(9), "
                   "685&ndash;690. " + _doi("10.1136/heartjnl-2013-305417")),
    "turakhia2018": ("Turakhia, M. P., Blankestijn, P. J., Carrero, J.-J., Clase, C. M., Deo, R., Herzog, C. A., Kasner, S. E., Passman, R. S., "
                     "Pecoits-Filho, R., Reinecke, H., Shroff, G. R., Zareba, W., Cheung, M., Wheeler, D. C., Winkelmayer, W. C., &amp; "
                     "Wanner, C. (2018). Chronic kidney disease and arrhythmias: Conclusions from a Kidney Disease: Improving Global Outcomes "
                     "(KDIGO) Controversies Conference. <em>European Heart Journal, 39</em>(24), 2314&ndash;2325. "
                     + _doi("10.1093/eurheartj/ehy060")),
}
