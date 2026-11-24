# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 31 (APA 7). Journal entries were built from PubMed metadata
on November 25, 2026; web sources were checked on the same date. Keys already defined or registered in the course
(doh2012, psn2024, ra10173, muller2018, kdoqi_hd2015, saran2003, patel2013, rosenblum2014, cdc_dialysis_bsi2024)
are not repeated. Module 31 owns starmer2014 and holley2006 (Module 32 reuses them).
doh_ao2013_0003 is owned by Module 30 and repeated here with identical text."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "starmer2014": ("Starmer, A. J., Spector, N. D., Srivastava, R., West, D. C., Rosenbluth, G., Allen, A. D., Noble, E. L., Tse, L. L., "
                    "Dalal, A. K., Keohane, C. A., Lipsitz, S. R., Rothschild, J. M., Wien, M. F., Yoon, C. S., Zigmont, K. R., Wilson, K. M., "
                    "O&rsquo;Toole, J. K., Solan, L. G., Aylor, M., . . . Landrigan, C. P. (2014). Changes in medical errors after implementation "
                    "of a handoff program. <em>New England Journal of Medicine, 371</em>(19), 1803&ndash;1812. " + _doi("10.1056/NEJMsa1405556")),
    "holley2006": ("Holley, J. L. (2006). A descriptive report of errors and adverse events in chronic hemodialysis units. "
                   "<em>Nephrology News &amp; Issues, 20</em>(12), 57&ndash;58, 60&ndash;61, 63 passim. "
                   + _url("https://pubmed.ncbi.nlm.nih.gov/17125098/")),
    "thomashawkins2015": ("Thomas-Hawkins, C., &amp; Flynn, L. (2015). Patient safety culture and nurse-reported adverse events in outpatient "
                          "hemodialysis units. <em>Research and Theory for Nursing Practice, 29</em>(1), 53&ndash;65. "
                          + _doi("10.1891/1541-6577.29.1.53")),
    "perla2011": ("Perla, R. J., Provost, L. P., &amp; Murray, S. K. (2011). The run chart: A simple analytical tool for learning from variation "
                  "in healthcare processes. <em>BMJ Quality &amp; Safety, 20</em>(1), 46&ndash;51. " + _doi("10.1136/bmjqs.2009.037895")),
    "sheetz2021": ("Sheetz, K. H., Gerhardinger, L., Ryan, A. M., &amp; Waits, S. A. (2021). Changes in dialysis center quality associated with "
                   "the End-Stage Renal Disease Quality Incentive Program: An observational study with a regression discontinuity design. "
                   "<em>Annals of Internal Medicine, 174</em>(8), 1058&ndash;1064. " + _doi("10.7326/M20-6662")),
    "peerally2017": ("Peerally, M. F., Carr, S., Waring, J., &amp; Dixon-Woods, M. (2017). The problem with root cause analysis. "
                     "<em>BMJ Quality &amp; Safety, 26</em>(5), 417&ndash;422. " + _doi("10.1136/bmjqs-2016-005511")),
    "taylor2014": ("Taylor, M. J., McNicholas, C., Nicolay, C., Darzi, A., Bell, D., &amp; Reed, J. E. (2014). Systematic review of the "
                   "application of the plan-do-study-act method to improve quality in healthcare. <em>BMJ Quality &amp; Safety, 23</em>(4), "
                   "290&ndash;298. " + _doi("10.1136/bmjqs-2013-001862")),
    "li_soliman2011": ("<em>Li v. Spouses Soliman</em>, G.R. No. 165279 (2011). Supreme Court of the Philippines, en banc, June 7, 2011. "
                       + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/1/37801")),
    "npc_circular16_03": ("National Privacy Commission. (2016). <em>Personal data breach management</em> (NPC Circular No. 16-03). "
                          + _url("https://privacy.gov.ph/?p=553")),
    "philhealth_pc2024_0023": ("Philippine Health Insurance Corporation. (2024). <em>[News release on PhilHealth Circular No. "
                               "2024-0023, adjusted hemodialysis package]</em>. Released October 17, 2024. "
                               + _url("https://www.philhealth.gov.ph/news/up/article/2024/news_6710c0050d979.php")),
    "doh_ao2013_0003": ("Department of Health. (2013). <em>Implementing guidelines in the analysis, monitoring and maintenance of water used in "
                        "dialysis facilities pursuant to Administrative Order No. 2012-0001</em> (Administrative Order No. 2013-0003). "
                        + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036")),
}
