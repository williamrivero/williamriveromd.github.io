# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 19 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in the course (daugirdas2015, turakhia2018, kcuk_bleed, greenberg2021,
saha2017) are not repeated. mavrakanas2017 is defined here and shared with Module 20."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "shen2012": ("Shen, J. I., &amp; Winkelmayer, W. C. (2012). Use and safety of unfractionated heparin for anticoagulation during "
                 "maintenance hemodialysis. <em>American Journal of Kidney Diseases, 60</em>(3), 473&ndash;486. "
                 + _doi("10.1053/j.ajkd.2012.03.017")),
    "shen2013": ("Shen, J. I., Mitani, A. A., Chang, T. I., &amp; Winkelmayer, W. C. (2013). Use and safety of heparin-free maintenance "
                 "hemodialysis in the USA. <em>Nephrology Dialysis Transplantation, 28</em>(6), 1589&ndash;1602. "
                 + _doi("10.1093/ndt/gft067")),
    "murea2018": ("Murea, M., Russell, G. B., Daeihagh, P., Saran, A. M., Pandya, K., Cabrera, M., Burkart, J. M., &amp; Freedman, B. I. "
                  "(2018). Efficacy and safety of low-dose heparin in hemodialysis. <em>Hemodialysis International, 22</em>(1), 74&ndash;81. "
                  + _doi("10.1111/hdi.12563")),
    "francois2022": ("Fran&ccedil;ois, K., De Clerck, D., Tonnelier, A., Cambier, M.-L., Orlando, C., Jochmans, K., Cools, W., &amp; "
                     "Wissing, K. M. (2022). Dialyzer performance during hemodialysis without systemic anticoagulation using a "
                     "heparin-grafted dialyzer combined with a citrate-enriched dialysate: Results of the randomized crossover "
                     "noninferiority EvoCit study. <em>American Journal of Kidney Diseases, 79</em>(1), 79&ndash;87.e1. "
                     + _doi("10.1053/j.ajkd.2021.04.004")),
    "vandenbosch2021": ("Vandenbosch, I., Dejongh, S., Claes, K., Bammens, B., De Vusser, K., Van Craenenbroeck, A., Kuypers, D., "
                        "Evenepoel, P., &amp; Meijers, B. (2021). Strategies for asymmetrical triacetate dialyser heparin-free effective "
                        "haemodialysis: The SAFE study. <em>Clinical Kidney Journal, 14</em>(8), 1901&ndash;1907. "
                        + _doi("10.1093/ckj/sfaa228")),
    "cuker2018": ("Cuker, A., Arepally, G. M., Chong, B. H., Cines, D. B., Greinacher, A., Gruel, Y., Linkins, L. A., Rodner, S. B., "
                  "Selleng, S., Warkentin, T. E., Wex, A., Mustafa, R. A., Morgan, R. L., &amp; Santesso, N. (2018). American Society of "
                  "Hematology 2018 guidelines for management of venous thromboembolism: Heparin-induced thrombocytopenia. "
                  "<em>Blood Advances, 2</em>(22), 3360&ndash;3392. " + _doi("10.1182/bloodadvances.2018024489")),
    "lo2006": ("Lo, G. K., Juhl, D., Warkentin, T. E., Sigouin, C. S., Eichler, P., &amp; Greinacher, A. (2006). Evaluation of pretest "
               "clinical score (4 T&rsquo;s) for the diagnosis of heparin-induced thrombocytopenia in two clinical settings. "
               "<em>Journal of Thrombosis and Haemostasis, 4</em>(4), 759&ndash;765. " + _doi("10.1111/j.1538-7836.2006.01787.x")),
    "mannucci1983": ("Mannucci, P. M., Remuzzi, G., Pusineri, F., Lombardi, R., Valsecchi, C., Mecca, G., &amp; Zimmerman, T. S. (1983). "
                     "Deamino-8-D-arginine vasopressin shortens the bleeding time in uremia. <em>New England Journal of Medicine, "
                     "308</em>(1), 8&ndash;12. " + _doi("10.1056/NEJM198301063080102")),
    "hedges2007": ("Hedges, S. J., Dehoney, S. B., Hooper, J. S., Amanzadeh, J., &amp; Busti, A. J. (2007). Evidence-based treatment "
                   "recommendations for uremic bleeding. <em>Nature Clinical Practice Nephrology, 3</em>(3), 138&ndash;153. "
                   + _doi("10.1038/ncpneph0421")),
    "kaw2006": ("Kaw, D., &amp; Malhotra, D. (2006). Platelet dysfunction and end-stage renal disease. <em>Seminars in Dialysis, "
                "19</em>(4), 317&ndash;322. " + _doi("10.1111/j.1525-139X.2006.00179.x")),
    "wasse2003": ("Wasse, H., Gillen, D. L., Ball, A. M., Kestenbaum, B. R., Seliger, S. L., Sherrard, D., &amp; Stehman-Breen, C. O. "
                  "(2003). Risk factors for upper gastrointestinal bleeding among end-stage renal disease patients. <em>Kidney "
                  "International, 64</em>(4), 1455&ndash;1461. " + _doi("10.1046/j.1523-1755.2003.00225.x")),
    "yang2013": ("Yang, J.-Y., Lee, T.-C., Montez-Rath, M. E., Chertow, G. M., &amp; Winkelmayer, W. C. (2013). Risk factors of "
                 "short-term mortality after acute nonvariceal upper gastrointestinal bleeding in patients on dialysis: A "
                 "population-based study. <em>BMC Nephrology, 14</em>, Article 97. " + _doi("10.1186/1471-2369-14-97")),
    "mavrakanas2017": ("Mavrakanas, T. A., Samer, C. F., Nessim, S. J., Frisch, G., &amp; Lipman, M. L. (2017). Apixaban "
                       "pharmacokinetics at steady state in hemodialysis patients. <em>Journal of the American Society of Nephrology, "
                       "28</em>(7), 2241&ndash;2248. " + _doi("10.1681/ASN.2016090980")),
    "pokorney2022": ("Pokorney, S. D., Chertow, G. M., Al-Khalidi, H. R., Gallup, D., Dignacco, P., Mussina, K., Bansal, N., "
                     "Gadegbeku, C. A., Garcia, D. A., Garonzik, S., Lopes, R. D., Mahaffey, K. W., Matsuda, K., Middleton, J. P., "
                     "Rymer, J. A., Sands, G. H., Thadhani, R., Thomas, K. L., Washam, J. B., . . . RENAL-AF Investigators. (2022). "
                     "Apixaban for patients with atrial fibrillation on hemodialysis: A multicenter randomized controlled trial. "
                     "<em>Circulation, 146</em>(23), 1735&ndash;1745. " + _doi("10.1161/CIRCULATIONAHA.121.054990")),
    "reinecke2023": ("Reinecke, H., Engelbertz, C., Bauersachs, R., Breithardt, G., Echterhoff, H.-H., Ger&szlig;, J., Haeusler, K. G., "
                     "Hewing, B., Hoyer, J., Juergensmeyer, S., Klingenheben, T., Knapp, G., Rump, L. C., Schmidt-Guertler, H., "
                     "Wanner, C., Kirchhof, P., &amp; Goerlich, D. (2023). A randomized controlled trial comparing apixaban with the "
                     "vitamin K antagonist phenprocoumon in patients on chronic hemodialysis: The AXADIA-AFNET 8 study. "
                     "<em>Circulation, 147</em>(4), 296&ndash;309. " + _doi("10.1161/CIRCULATIONAHA.122.062779")),
    "winkelmayer2026": ("Winkelmayer, W. C., Montez-Rath, M. E., He, M., Erickson, K. F., Gregg, L. P., Khairallah, P., Chertow, G. M., "
                        "Chang, T. I., &amp; Niu, J. (2026). Initiation of apixaban versus warfarin in patients with kidney failure on "
                        "hemodialysis with newly diagnosed atrial fibrillation: A target trial emulation. <em>American Journal of "
                        "Kidney Diseases</em>. Advance online publication. " + _doi("10.1053/j.ajkd.2026.08.009")),
}
