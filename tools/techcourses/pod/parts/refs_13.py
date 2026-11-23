# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 13 (APA 7). Each entry was checked against PubMed metadata
on November 23, 2026. Keys already defined in pod_src/refs.py (daugirdas2015, kdigo_bpvol2020, flythe2011) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "flythe2015": ("Flythe, J. E., Xue, H., Lynch, K. E., Curhan, G. C., &amp; Brunelli, S. M. (2015). Association of mortality risk with various "
                   "definitions of intradialytic hypotension. <em>Journal of the American Society of Nephrology, 26</em>(3), 724&ndash;734. "
                   + _doi("10.1681/ASN.2014020222")),
    "ebpg2007": ("Kooman, J., Basci, A., Pizzarelli, F., Canaud, B., Haage, P., Fouque, D., Konner, K., Martin-Malo, A., Pedrini, L., Tattersall, J., "
                 "Tordoir, J., Vennegoor, M., Wanner, C., ter Wee, P., &amp; Vanholder, R. (2007). EBPG guideline on haemodynamic instability. "
                 "<em>Nephrology Dialysis Transplantation, 22</em>(Suppl. 2), ii22&ndash;ii44. " + _doi("10.1093/ndt/gfm019")),
    "mytemp2022": ("MyTEMP writing committee. (2022). Personalised cooler dialysate for patients receiving maintenance haemodialysis (MyTEMP): "
                   "A pragmatic, cluster-randomised trial. <em>The Lancet, 400</em>(10364), 1693&ndash;1703. "
                   + _doi("10.1016/S0140-6736(22)01805-0")),
    "mustafa2016": ("Mustafa, R. A., Bdair, F., Akl, E. A., Garg, A. X., Thiessen-Philbrook, H., Salameh, H., Kisra, S., Nesrallah, G., Al-Jaishi, A., "
                    "Patel, P., Patel, P., Mustafa, A. A., &amp; Sch&uuml;nemann, H. J. (2016). Effect of lowering the dialysate temperature in chronic "
                    "hemodialysis: A systematic review and meta-analysis. <em>Clinical Journal of the American Society of Nephrology, 11</em>(3), "
                    "442&ndash;457. " + _doi("10.2215/CJN.04580415")),
    "burton2009": ("Burton, J. O., Jefferies, H. J., Selby, N. M., &amp; McIntyre, C. W. (2009). Hemodialysis-induced cardiac injury: Determinants and "
                   "associated outcomes. <em>Clinical Journal of the American Society of Nephrology, 4</em>(5), 914&ndash;920. "
                   + _doi("10.2215/CJN.03900808")),
    "burton2009b": ("Burton, J. O., Jefferies, H. J., Selby, N. M., &amp; McIntyre, C. W. (2009). Hemodialysis-induced repetitive myocardial injury "
                    "results in global and segmental reduction in systolic cardiac function. <em>Clinical Journal of the American Society of "
                    "Nephrology, 4</em>(12), 1925&ndash;1931. " + _doi("10.2215/CJN.04470709")),
    "stefansson2014": ("Stef&aacute;nsson, B. V., Brunelli, S. M., Cabrera, C., Rosenbaum, D., Anum, E., Ramakrishnan, K., Jensen, D. E., &amp; "
                       "St&aring;lhammar, N.-O. (2014). Intradialytic hypotension and risk of cardiovascular disease. <em>Clinical Journal of the "
                       "American Society of Nephrology, 9</em>(12), 2124&ndash;2132. " + _doi("10.2215/CJN.02680314")),
    "kuipers2016": ("Kuipers, J., Oosterhuis, J. K., Krijnen, W. P., Dasselaar, J. J., Gaillard, C. A. J. M., Westerhuis, R., &amp; Franssen, C. F. M. "
                    "(2016). Prevalence of intradialytic hypotension, clinical symptoms and nursing interventions: A three-months, prospective study "
                    "of 3818 haemodialysis sessions. <em>BMC Nephrology, 17</em>, Article 21. " + _doi("10.1186/s12882-016-0231-9")),
    "kuipers2019": ("Kuipers, J., Verboom, L. M., Ipema, K. J. R., Paans, W., Krijnen, W. P., Gaillard, C. A. J. M., Westerhuis, R., &amp; "
                    "Franssen, C. F. M. (2019). The prevalence of intradialytic hypotension in patients on conventional hemodialysis: A systematic "
                    "review with meta-analysis. <em>American Journal of Nephrology, 49</em>(6), 497&ndash;506. " + _doi("10.1159/000500877")),
    "daugirdas2001": ("Daugirdas, J. T. (2001). Pathophysiology of dialysis hypotension: An update. <em>American Journal of Kidney Diseases, "
                      "38</em>(4, Suppl. 4), S11&ndash;S17. " + _doi("10.1053/ajkd.2001.28090")),
    "reeves2018": ("Reeves, P. B., &amp; Mc Causland, F. R. (2018). Mechanisms, clinical implications, and treatment of intradialytic hypotension. "
                   "<em>Clinical Journal of the American Society of Nephrology, 13</em>(8), 1297&ndash;1303. " + _doi("10.2215/CJN.12141017")),
    "kistler2018": ("Kistler, B. M., Benner, D., Burrowes, J. D., Campbell, K. L., Fouque, D., Garibotto, G., Kopple, J. D., Kovesdy, C. P., "
                    "Rhee, C. M., Steiber, A., Stenvinkel, P., ter Wee, P., Teta, D., Wang, A. Y. M., &amp; Kalantar-Zadeh, K. (2018). Eating during "
                    "hemodialysis treatment: A consensus statement from the International Society of Renal Nutrition and Metabolism. "
                    "<em>Journal of Renal Nutrition, 28</em>(1), 4&ndash;12. " + _doi("10.1053/j.jrn.2017.10.003")),
}
