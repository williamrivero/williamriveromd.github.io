# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 26 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in pod_src/refs.py (saran2003, alsalmi2018, chan2014, daugirdas2015) are not repeated.
Module 26 owns davison2015 and walavalkar2022; Module 27 reuses them."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "palmer2013": ("Palmer, S., Vecchio, M., Craig, J. C., Tonelli, M., Johnson, D. W., Nicolucci, A., Pellegrini, F., Saglimbene, V., "
                   "Logroscino, G., Fishbane, S., &amp; Strippoli, G. F. M. (2013). Prevalence of depression in chronic kidney disease: "
                   "Systematic review and meta-analysis of observational studies. <em>Kidney International, 84</em>(1), 179&ndash;191. "
                   + _doi("10.1038/ki.2013.77")),
    "watnick2005": ("Watnick, S., Wang, P.-L., Demadura, T., &amp; Ganzini, L. (2005). Validation of 2 depression screening tools in dialysis "
                    "patients. <em>American Journal of Kidney Diseases, 46</em>(5), 919&ndash;924. " + _doi("10.1053/j.ajkd.2005.08.006")),
    "kroenke2001": ("Kroenke, K., Spitzer, R. L., &amp; Williams, J. B. (2001). The PHQ-9: Validity of a brief depression severity measure. "
                    "<em>Journal of General Internal Medicine, 16</em>(9), 606&ndash;613. " + _doi("10.1046/j.1525-1497.2001.016009606.x")),
    "kurella2005": ("Kurella, M., Kimmel, P. L., Young, B. S., &amp; Chertow, G. M. (2005). Suicide in the United States end-stage renal disease "
                    "program. <em>Journal of the American Society of Nephrology, 16</em>(3), 774&ndash;781. " + _doi("10.1681/ASN.2004070550")),
    "palmer_cochrane2016": ("Palmer, S. C., Natale, P., Ruospo, M., Saglimbene, V. M., Rabindranath, K. S., Craig, J. C., &amp; Strippoli, G. F. M. "
                            "(2016). Antidepressants for treating depression in adults with end-stage kidney disease treated with dialysis. "
                            "<em>Cochrane Database of Systematic Reviews, 2016</em>(5), Article CD004541. "
                            + _doi("10.1002/14651858.CD004541.pub3")),
    "friedli2017": ("Friedli, K., Guirguis, A., Almond, M., Day, C., Chilcot, J., Da Silva-Gane, M., Davenport, A., Fineberg, N. A., Spencer, B., "
                    "Wellsted, D., &amp; Farrington, K. (2017). Sertraline versus placebo in patients with major depressive disorder undergoing "
                    "hemodialysis: A randomized, controlled feasibility trial. <em>Clinical Journal of the American Society of Nephrology, "
                    "12</em>(2), 280&ndash;286. " + _doi("10.2215/CJN.02120216")),
    "mehrotra2019": ("Mehrotra, R., Cukor, D., Unruh, M., Rue, T., Heagerty, P., Cohen, S. D., Dember, L. M., Diaz-Linhart, Y., Dubovsky, A., "
                     "Greene, T., Grote, N., Kutner, N., Trivedi, M. H., Quinn, D. K., Ver Halen, N., Weisbord, S. D., Young, B. A., Kimmel, P. L., "
                     "&amp; Hedayati, S. S. (2019). Comparative efficacy of therapies for treatment of depression for patients undergoing "
                     "maintenance hemodialysis: A randomized clinical trial. <em>Annals of Internal Medicine, 170</em>(6), 369&ndash;379. "
                     + _doi("10.7326/M18-2229")),
    "cukor2014": ("Cukor, D., Ver Halen, N., Asher, D. R., Coplan, J. D., Weedon, J., Wyka, K. E., Saggi, S. J., &amp; Kimmel, P. L. (2014). "
                  "Psychosocial intervention improves depression, quality of life, and fluid adherence in hemodialysis. <em>Journal of the "
                  "American Society of Nephrology, 25</em>(1), 196&ndash;206. " + _doi("10.1681/ASN.2012111134")),
    "jhamb2023": ("Jhamb, M., Steel, J. L., Yabes, J. G., Roumelioti, M.-E., Erickson, S., Devaraj, S. M., Vowles, K. E., Vodovotz, Y., Beach, S., "
                  "Weisbord, S. D., Rollman, B. L., &amp; Unruh, M. (2023). Effects of technology assisted stepped collaborative care intervention "
                  "to improve symptoms in patients undergoing hemodialysis: The T&#256;Ccare randomized clinical trial. <em>JAMA Internal "
                  "Medicine, 183</em>(8), 795&ndash;805. " + _doi("10.1001/jamainternmed.2023.2215")),
    "gillespie2026": ("Gillespie, K. M., Purtell, L., Finderup, J., Schjerning, N., &amp; Bonner, A. (2026). Interventions to reduce burden among "
                      "informal caregivers of people with chronic kidney disease: Systematic review and meta-analysis. <em>Journal of Renal "
                      "Care, 52</em>(2), Article e70063. " + _doi("10.1111/jorc.70063")),
    "walavalkar2022": ("Walavalkar, A., Craswell, A., &amp; Gray, N. A. (2022). Experiences of caregivers of patients with conservatively managed "
                       "kidney failure: A mixed methods systematic review. <em>Canadian Journal of Kidney Health and Disease, 9</em>, "
                       "Article 20543581221089080. " + _doi("10.1177/20543581221089080")),
    "davison2015": ("Davison, S. N., Levin, A., Moss, A. H., Jha, V., Brown, E. A., Brennan, F., Murtagh, F. E. M., Naicker, S., Germain, M. J., "
                    "O&rsquo;Donoghue, D. J., Morton, R. L., Obrador, G. T., &amp; Kidney Disease: Improving Global Outcomes. (2015). Executive "
                    "summary of the KDIGO Controversies Conference on Supportive Care in Chronic Kidney Disease: Developing a roadmap to "
                    "improving quality care. <em>Kidney International, 88</em>(3), 447&ndash;459. " + _doi("10.1038/ki.2015.110")),
    "oconnor2013": ("O&rsquo;Connor, N. R., Dougherty, M., Harris, P. S., &amp; Casarett, D. J. (2013). Survival after dialysis discontinuation and "
                    "hospice enrollment for ESRD. <em>Clinical Journal of the American Society of Nephrology, 8</em>(12), 2117&ndash;2122. "
                    + _doi("10.2215/CJN.04110413")),
    "song2024": ("Song, M.-K., Manatunga, A., Plantinga, L., Metzger, M., Kshirsagar, A. V., Lea, J., Abdel-Rahman, E. M., Jhamb, M., Wu, E., "
                 "Englert, J., &amp; Ward, S. E. (2024). Effectiveness of an advance care planning intervention in adults receiving dialysis "
                 "and their families: A cluster randomized clinical trial. <em>JAMA Network Open, 7</em>(1), Article e2351511. "
                 + _doi("10.1001/jamanetworkopen.2023.51511")),
}
