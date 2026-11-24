# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 29 (APA 7). Journal entries were built from PubMed metadata
on November 25, 2026; WHO entries were checked on the WHO pages. Keys already defined in the course (cdc2001,
ra10173, doh2012, daugirdas2015, cdc_dialysis_bsi2024) are not repeated. kdigo_txcand2020 (Module 27) and
ghafur2007 (Module 28) are cited but defined by those modules."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "kdigo_hcv2022": ("Kidney Disease: Improving Global Outcomes Hepatitis C Work Group. (2022). KDIGO 2022 clinical practice guideline for the "
                      "prevention, diagnosis, evaluation, and treatment of hepatitis C in chronic kidney disease. <em>Kidney International, "
                      "102</em>(6S), S129&ndash;S205. " + _doi("10.1016/j.kint.2022.07.013")),
    "kdigo_hcv_synopsis2023": ("Awan, A. A. Y., Berenguer, M. C., Bruchfeld, A., Fabrizi, F., Goldberg, D. S., Jia, J., Kamar, N., Mohamed, R., "
                               "Pess&ocirc;a, M. G., Pol, S., Sise, M. E., Balk, E. M., Gordon, C. E., Adam, G., Cheung, M., Earley, A., Martin, P., "
                               "&amp; Jadoul, M. (2023). Prevention, diagnosis, evaluation, and treatment of hepatitis C in chronic kidney disease: "
                               "Synopsis of the Kidney Disease: Improving Global Outcomes 2022 clinical practice guideline. <em>Annals of Internal "
                               "Medicine, 176</em>(12), 1648&ndash;1655. " + _doi("10.7326/M23-2391")),
    "nguyen2016": ("Nguyen, D. B., Gutowski, J., Ghiselli, M., Cheng, T., Bel Hamdounia, S., Suryaprasad, A., Xu, F., Moulton-Meissner, H., "
                   "Hayden, T., Forbi, J. C., Xia, G.-L., Arduino, M. J., Patel, A., &amp; Patel, P. R. (2016). A large outbreak of hepatitis C "
                   "virus infections in a hemodialysis clinic. <em>Infection Control &amp; Hospital Epidemiology, 37</em>(2), 125&ndash;133. "
                   + _doi("10.1017/ice.2015.247")),
    "duong2016": ("Duong, C. M., &amp; McLaws, M.-L. (2016). An investigation of an outbreak of hepatitis C virus infections in a low-resourced "
                  "hemodialysis unit in Vietnam. <em>American Journal of Infection Control, 44</em>(5), 560&ndash;566. "
                  + _doi("10.1016/j.ajic.2016.01.014")),
    "patel2010": ("Patel, P. R., Thompson, N. D., Kallen, A. J., &amp; Arduino, M. J. (2010). Epidemiology, surveillance, and prevention of "
                  "hepatitis C virus infections in hemodialysis patients. <em>American Journal of Kidney Diseases, 56</em>(2), 371&ndash;378. "
                  + _doi("10.1053/j.ajkd.2010.01.025")),
    "acip_hbv2018": ("Schillie, S., Vellozzi, C., Reingold, A., Harris, A., Haber, P., Ward, J. W., &amp; Nelson, N. P. (2018). Prevention of "
                     "hepatitis B virus infection in the United States: Recommendations of the Advisory Committee on Immunization Practices. "
                     "<em>MMWR Recommendations and Reports, 67</em>(1), 1&ndash;31. " + _doi("10.15585/mmwr.rr6701a1")),
    "manley2023": ("Manley, H. J., Aweh, G., Frament, J., Ladik, V., &amp; Lacson, E. K. (2023). A real world comparison of HepB (Engerix-B&reg;) "
                   "and HepB-CpG (Heplisav-B&reg;) vaccine seroprotection in patients receiving maintenance dialysis. <em>Nephrology Dialysis "
                   "Transplantation, 38</em>(2), 447&ndash;454. " + _doi("10.1093/ndt/gfac039")),
    "gilbertson2011": ("Gilbertson, D. T., Guo, H., Arneson, T. J., &amp; Collins, A. J. (2011). The association of pneumococcal vaccination with "
                       "hospitalization and mortality in hemodialysis patients. <em>Nephrology Dialysis Transplantation, 26</em>(9), "
                       "2934&ndash;2939. " + _doi("10.1093/ndt/gfq853")),
    "romanowski2016": ("Romanowski, K., Clark, E. G., Levin, A., Cook, V. J., &amp; Johnston, J. C. (2016). Tuberculosis and chronic kidney "
                       "disease: An emerging global syndemic. <em>Kidney International, 90</em>(1), 34&ndash;40. "
                       + _doi("10.1016/j.kint.2016.01.034")),
    "campbell2020": ("Campbell, J. R., Winters, N., &amp; Menzies, D. (2020). Absolute risk of tuberculosis among untreated populations with a "
                     "positive tuberculin skin test or interferon-gamma release assay result: Systematic review and meta-analysis. "
                     "<em>BMJ, 368</em>, Article m549. " + _doi("10.1136/bmj.m549")),
    "who_tpt2024": ("World Health Organization. (2024). <em>WHO consolidated guidelines on tuberculosis. Module 1: Prevention. Tuberculosis "
                    "preventive treatment</em> (2nd ed.). " + _url("https://www.who.int/publications/i/item/9789240096196")),
    "who_tb2024": ("World Health Organization. (2024). <em>Tuberculosis resurges as top infectious disease killer</em> [News release, October 29, 2024]. "
                   + _url("https://www.who.int/news/item/29-10-2024-tuberculosis-resurges-as-top-infectious-disease-killer")),
    "hilbrands2020": ("Hilbrands, L. B., Duivenvoorden, R., Vart, P., Franssen, C. F. M., Hemmelder, M. H., Jager, K. J., Kieneker, L. M., "
                      "Noordzij, M., Pena, M. J., de Vries, H., Arroyo, D., Covic, A., Crespo, M., Goffin, E., Islam, M., Massy, Z. A., "
                      "Montero, N., Oliveira, J. P., Roca Mu&ntilde;oz, A., . . . Gansevoort, R. T. (2020). COVID-19-related mortality in kidney "
                      "transplant and dialysis patients: Results of the ERACODA collaboration. <em>Nephrology Dialysis Transplantation, "
                      "35</em>(11), 1973&ndash;1983. " + _doi("10.1093/ndt/gfaa261")),
    "tomacruz2021": ("Tomacruz, I. D., So, P. N., Pasilan, R. M., Camenforte, J. K., &amp; Duavit, M. I. (2021). Clinical characteristics and "
                     "short-term outcomes of chronic dialysis patients admitted for COVID-19 in Metro Manila, Philippines. <em>International "
                     "Journal of Nephrology and Renovascular Disease, 14</em>, 41&ndash;51. " + _doi("10.2147/IJNRD.S287455")),
    "carr2021": ("Carr, E. J., Wu, M., Harvey, R., Wall, E. C., Kelly, G., Hussain, S., Howell, M., Kassiotis, G., Swanton, C., Gandhi, S., "
                 "Bauer, D. L. V., Haemodialysis COVID-19 Consortium, Crick COVID Immunity Pipeline, Billany, R. E., Graham-Brown, M. P. M., "
                 "Beckett, J., Bull, K., Shankar, S., Henderson, S., . . . Beale, R. (2021). Neutralising antibodies after COVID-19 vaccination "
                 "in UK haemodialysis patients. <em>The Lancet, 398</em>(10305), 1038&ndash;1041. " + _doi("10.1016/S0140-6736(21)01854-7")),
    "phs_hivpep2025": ("Kofman, A. D., Struble, K. A., Heneine, W., Gayle, B., de Perio, M. A., Okasako-Schmucker, D. L., So, C. N., Anderson, "
                       "L. E., Stone, E. C., Henderson, D. K., &amp; Kuhar, D. T. (2025). 2025 US Public Health Service guidelines for the "
                       "management of occupational exposures to human immunodeficiency virus and recommendations for post-exposure prophylaxis "
                       "in healthcare settings. <em>Infection Control &amp; Hospital Epidemiology, 46</em>(9), 863&ndash;873. "
                       + _doi("10.1017/ice.2025.10254")),
}
