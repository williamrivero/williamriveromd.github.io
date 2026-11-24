# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 06 (APA 7). Journal entries were built from PubMed metadata
on November 25, 2026; the ISO entries were checked against the ISO catalog pages and the ISO 23500-1:2024 preview.
Keys already defined in the course (daugirdas2015, greenberg2021, tipple1991, ward1996, duffy2000) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "iso23500_1_2024": ("International Organization for Standardization. (2024). <em>Preparation and quality management of fluids for "
                        "haemodialysis and related therapies: Part 1. General requirements</em> (ISO Standard No. 23500-1:2024, 2nd ed.). "
                        + _url("https://www.iso.org/standard/84368.html")),
    "iso23500_3_2024": ("International Organization for Standardization. (2024). <em>Preparation and quality management of fluids for "
                        "haemodialysis and related therapies: Part 3. Water for haemodialysis and related therapies</em> (ISO Standard No. "
                        "23500-3:2024, 2nd ed.). " + _url("https://www.iso.org/standard/84370.html")),
    "iso23500_5_2024": ("International Organization for Standardization. (2024). <em>Preparation and quality management of fluids for "
                        "haemodialysis and related therapies: Part 5. Quality of dialysis fluid for haemodialysis and related therapies</em> "
                        "(ISO Standard No. 23500-5:2024, 2nd ed.). " + _url("https://www.iso.org/standard/84372.html")),
    "ebpg_purity2002": ("European Best Practice Guidelines Expert Group on Hemodialysis, European Renal Association. (2002). Section IV. "
                        "Dialysis fluid purity. <em>Nephrology Dialysis Transplantation, 17</em>(Suppl. 7), 45&ndash;62. "
                        + _url("https://pubmed.ncbi.nlm.nih.gov/12386221/")),
    "coulliette2013": ("Coulliette, A. D., &amp; Arduino, M. J. (2013). Hemodialysis and water quality. <em>Seminars in Dialysis, 26</em>(4), "
                       "427&ndash;438. " + _doi("10.1111/sdi.12113")),
    "alfrey1976": ("Alfrey, A. C., LeGendre, G. R., &amp; Kaehny, W. D. (1976). The dialysis encephalopathy syndrome: Possible aluminum "
                   "intoxication. <em>New England Journal of Medicine, 294</em>(4), 184&ndash;188. " + _doi("10.1056/NEJM197601222940402")),
    "berend2001": ("Berend, K., van der Voet, G., &amp; Boer, W. H. (2001). Acute aluminum encephalopathy in a dialysis center caused by a "
                   "cement mortar water distribution pipe. <em>Kidney International, 59</em>(2), 746&ndash;753. "
                   + _doi("10.1046/j.1523-1755.2001.059002746.x")),
    "arnow1994": ("Arnow, P. M., Bland, L. A., Garcia-Houchins, S., Fridkin, S., &amp; Fellner, S. K. (1994). An outbreak of fatal fluoride "
                  "intoxication in a long-term hemodialysis unit. <em>Annals of Internal Medicine, 121</em>(5), 339&ndash;344. "
                  + _doi("10.7326/0003-4819-121-5-199409010-00005")),
    "jochimsen1998": ("Jochimsen, E. M., Carmichael, W. W., An, J. S., Cardo, D. M., Cookson, S. T., Holmes, C. E., Antunes, M. B., "
                      "de Melo Filho, D. A., Lyra, T. M., Barreto, V. S., Azevedo, S. M., &amp; Jarvis, W. R. (1998). Liver failure and death "
                      "after exposure to microcystins at a hemodialysis center in Brazil. <em>New England Journal of Medicine, 338</em>(13), "
                      "873&ndash;878. " + _doi("10.1056/NEJM199803263381304")),
    "glorieux2009": ("Glorieux, G., Schepers, E., Schindler, R., Lemke, H. D., Verbeke, F., Dhondt, A., Lameire, N., &amp; Vanholder, R. (2009). "
                     "A novel bio-assay increases the detection yield of microbiological impurity of dialysis fluid, in comparison to the "
                     "LAL-test. <em>Nephrology Dialysis Transplantation, 24</em>(2), 548&ndash;554. " + _doi("10.1093/ndt/gfn485")),
    "susantitaphong2013": ("Susantitaphong, P., Riella, C., &amp; Jaber, B. L. (2013). Effect of ultrapure dialysate on markers of "
                           "inflammation, oxidative stress, nutrition and anemia parameters: A meta-analysis. <em>Nephrology Dialysis "
                           "Transplantation, 28</em>(2), 438&ndash;446. " + _doi("10.1093/ndt/gfs514")),
    "asci2013": ("Asci, G., T&ouml;z, H., Ozkahya, M., Duman, S., Demirci, M. S., Cirit, M., Sipahi, S., Dheir, H., Bozkurt, D., Kircelli, F., "
                 "Ok, E. S., Erten, S., Ertilav, M., Kose, T., Basci, A., Raimann, J. G., Levin, N. W., Ok, E., &amp; EGE Study Group. (2013). "
                 "The impact of membrane permeability and dialysate purity on cardiovascular outcomes. <em>Journal of the American Society "
                 "of Nephrology, 24</em>(6), 1014&ndash;1023. " + _doi("10.1681/ASN.2012090908")),
}
