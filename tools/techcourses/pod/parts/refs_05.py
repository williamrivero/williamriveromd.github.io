# -*- coding: utf-8 -*-
"""New references for Physician on Duty, Module 05 (APA 7). Each entry was checked against PubMed metadata
on November 23, 2026. Keys already in pod_src/refs.py (daugirdas2015, hall2021, and others) are not redefined."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "eknoyan2002": ("Eknoyan, G., Beck, G. J., Cheung, A. K., Daugirdas, J. T., Greene, T., Kusek, J. W., Allon, M., Bailey, J., Delmez, J. A., "
                    "Depner, T. A., Dwyer, J. T., Levey, A. S., Levin, N. W., Milford, E., Ornt, D. B., Rocco, M. V., Schulman, G., Schwab, S. J., "
                    "Teehan, B. P., &amp; Toto, R., for the Hemodialysis (HEMO) Study Group. (2002). Effect of dialysis dose and membrane flux in "
                    "maintenance hemodialysis. <em>New England Journal of Medicine, 347</em>(25), 2010&ndash;2019. " + _doi("10.1056/NEJMoa021583")),
    "locatelli2009": ("Locatelli, F., Martin-Malo, A., Hannedouche, T., Loureiro, A., Papadimitriou, M., Wizemann, V., Jacobson, S. H., Czekalski, S., "
                      "Ronco, C., &amp; Vanholder, R., for the Membrane Permeability Outcome (MPO) Study Group. (2009). Effect of membrane permeability "
                      "on survival of hemodialysis patients. <em>Journal of the American Society of Nephrology, 20</em>(3), 645&ndash;654. "
                      + _doi("10.1681/ASN.2008060590")),
    "kdoqi_hd2015": ("National Kidney Foundation. (2015). KDOQI clinical practice guideline for hemodialysis adequacy: 2015 update. "
                     "<em>American Journal of Kidney Diseases, 66</em>(5), 884&ndash;930. " + _doi("10.1053/j.ajkd.2015.07.015")),
    "blankestijn2023": ("Blankestijn, P. J., Vernooij, R. W. M., Hockham, C., Strippoli, G. F. M., Canaud, B., Hegbrant, J., Barth, C., Covic, A., "
                        "Cromm, K., Cucui, A., Davenport, A., Rose, M., T&ouml;r&ouml;k, M., Woodward, M., &amp; Bots, M. L., for the CONVINCE Scientific "
                        "Committee Investigators. (2023). Effect of hemodiafiltration or hemodialysis on mortality in kidney failure. "
                        "<em>New England Journal of Medicine, 389</em>(8), 700&ndash;709. " + _doi("10.1056/NEJMoa2304820")),
    "vernooij2024": ("Vernooij, R. W. M., Hockham, C., Strippoli, G., Green, S., Hegbrant, J., Davenport, A., Barth, C., Canaud, B., Woodward, M., "
                     "Blankestijn, P. J., &amp; Bots, M. L., for the CONVINCE Scientific Committee and the HDF Pooling Project Investigators. (2024). "
                     "Haemodiafiltration versus haemodialysis for kidney failure: An individual patient data meta-analysis of randomised controlled "
                     "trials. <em>The Lancet, 404</em>(10464), 1742&ndash;1749. " + _doi("10.1016/S0140-6736(24)01859-2")),
    "ribitsch2014": ("Ribitsch, W., Schilcher, G., Hafner-Giessauf, H., Krisper, P., Horina, J. H., Rosenkranz, A. R., &amp; Schneditz, D. (2014). "
                     "Prevalence of detectable venous pressure drops expected with venous needle dislodgement. "
                     "<em>Seminars in Dialysis, 27</em>(5), 507&ndash;511. " + _doi("10.1111/sdi.12169")),
    "frinak2023": ("Frinak, S., Kennedy, J., Zasuwa, G., Passalacqua, K. D., &amp; Yee, J. (2023). Detection of hemodialysis venous needle "
                   "dislodgment using venous access pressure measurements: A simulation study. <em>Kidney360, 4</em>(4), e476&ndash;e485. "
                   + _doi("10.34067/KID.0000000000000093")),
    "duffy2000": ("Duffy, R., Tomashek, K., Spangenberg, M., Spry, L., Dwyer, D., Safranek, T. J., Ying, C., Portesi, D., Divan, H., Kobrenski, J., "
                  "Arduino, M., Tokars, J., &amp; Jarvis, W. (2000). Multistate outbreak of hemolysis in hemodialysis patients traced to faulty "
                  "blood tubing sets. <em>Kidney International, 57</em>(4), 1668&ndash;1674. " + _doi("10.1046/j.1523-1755.2000.00011.x")),
}
