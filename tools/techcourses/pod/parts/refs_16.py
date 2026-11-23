# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 16 (APA 7). Each entry was checked against PubMed metadata on November 23, 2026."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _pm(p):
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{p}/">https://pubmed.ncbi.nlm.nih.gov/{p}/</a>'


REFS = {
    "saha2017": ("Saha, M., &amp; Allon, M. (2017). Diagnosis, treatment, and prevention of hemodialysis emergencies. "
                 "<em>Clinical Journal of the American Society of Nephrology, 12</em>(2), 357&ndash;369. " + _doi("10.2215/CJN.05260516")),
    "greenberg2021": ("Greenberg, K. I., &amp; Choi, M. J. (2021). Hemodialysis emergencies: Core Curriculum 2021. "
                      "<em>American Journal of Kidney Diseases, 77</em>(5), 796&ndash;809. " + _doi("10.1053/j.ajkd.2020.11.024")),
    "vanwaeleghem2008": ("Van Waeleghem, J.-P., Chamney, M., Lindley, E. J., &amp; Panc&iacute;rov&aacute;, J. (2008). Venous needle dislodgement: "
                         "How to minimise the risks. <em>Journal of Renal Care, 34</em>(4), 163&ndash;168. " + _doi("10.1111/j.1755-6686.2008.00047.x")),
    "holmer2020": ("Holmer, M., Olde, B., Sandberg, F., &amp; S&ouml;rnmo, L. (2020). Detection of needle dislodgement using extracorporeal "
                   "pressure signals: A feasibility study. <em>ASAIO Journal, 66</em>(4), 454&ndash;462. " + _doi("10.1097/MAT.0000000000001020")),
    "ribitsch2014": ("Ribitsch, W., Schilcher, G., Hafner-Giessauf, H., Krisper, P., Horina, J. H., Rosenkranz, A. R., &amp; Schneditz, D. (2014). "
                     "Prevalence of detectable venous pressure drops expected with venous needle dislodgement. "
                     "<em>Seminars in Dialysis, 27</em>(5), 507&ndash;511. " + _doi("10.1111/sdi.12169")),
    "frinak2023": ("Frinak, S., Kennedy, J., Zasuwa, G., Passalacqua, K. D., &amp; Yee, J. (2023). Detection of hemodialysis venous needle dislodgment "
                   "using venous access pressure measurements: A simulation study. <em>Kidney360, 4</em>(4), e476&ndash;e485. " + _doi("10.34067/KID.0000000000000093")),
    "duffy2000": ("Duffy, R., Tomashek, K., Spangenberg, M., Spry, L., Dwyer, D., Safranek, T. J., Ying, C., Portesi, D., Divan, H., Kobrenski, J., "
                  "Arduino, M., Tokars, J., &amp; Jarvis, W. (2000). Multistate outbreak of hemolysis in hemodialysis patients traced to faulty "
                  "blood tubing sets. <em>Kidney International, 57</em>(4), 1668&ndash;1674. " + _doi("10.1046/j.1523-1755.2000.00011.x")),
    "tipple1991": ("Tipple, M. A., Shusterman, N., Bland, L. A., McCarthy, M. A., Favero, M. S., Arduino, M. J., Reid, M. H., &amp; Jarvis, W. R. (1991). "
                   "Illness in hemodialysis patients after exposure to chloramine contaminated dialysate. "
                   "<em>ASAIO Transactions, 37</em>(4), 588&ndash;591. " + _pm("1768494")),
    "ward1996": ("Ward, D. M. (1996). Chloramine removal from water used in hemodialysis. "
                 "<em>Advances in Renal Replacement Therapy, 3</em>(4), 337&ndash;347. " + _doi("10.1016/s1073-4449(96)80014-8")),
    "daugirdas1988": ("Daugirdas, J. T., &amp; Ing, T. S. (1988). First-use reactions during hemodialysis: A definition of subtypes. "
                      "<em>Kidney International Supplement, 24</em>, S37&ndash;S43. " + _pm("2966256")),
}
