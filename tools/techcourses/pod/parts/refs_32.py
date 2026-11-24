# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 32 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined elsewhere (muller2018, greenberg2021, aha2025_bls, aha2025_systems,
daugirdas2015, doh2012, psn2024) and keys defined by Module 31 (starmer2014, holley2006) are not repeated."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "cook2011": ("Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., &amp; Hamstra, S. J. (2011). "
                 "Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. "
                 "<em>JAMA, 306</em>(9), 978&ndash;988. " + _doi("10.1001/jama.2011.1234")),
    "mcgaghie2011": ("McGaghie, W. C., Issenberg, S. B., Cohen, E. R., Barsuk, J. H., &amp; Wayne, D. B. (2011). Does simulation-based medical "
                     "education with deliberate practice yield better results than traditional clinical education? A meta-analytic comparative "
                     "review of the evidence. <em>Academic Medicine, 86</em>(6), 706&ndash;711. " + _doi("10.1097/ACM.0b013e318217e119")),
    "barsuk2014": ("Barsuk, J. H., Cohen, E. R., Potts, S., Demo, H., Gupta, S., Feinglass, J., McGaghie, W. C., &amp; Wayne, D. B. (2014). "
                   "Dissemination of a simulation-based mastery learning intervention reduces central line-associated bloodstream infections. "
                   "<em>BMJ Quality &amp; Safety, 23</em>(9), 749&ndash;756. " + _doi("10.1136/bmjqs-2013-002665")),
    "cheng2014": ("Cheng, A., Eppich, W., Grant, V., Sherbino, J., Zendejas, B., &amp; Cook, D. A. (2014). Debriefing for technology-enhanced "
                  "simulation: A systematic review and meta-analysis. <em>Medical Education, 48</em>(7), 657&ndash;666. "
                  + _doi("10.1111/medu.12432")),
    "aha2025_education": ("Donoghue, A. J., Auerbach, M., Banerjee, A., Blewer, A. L., Cheng, A., Kadlec, K. D., Lin, Y., Diederich, E., Sawyer, T., "
                          "Stallings, D. T., Toft, L. E. B., Torman, D., Wright, J. I., Schexnayder, S. M., &amp; Dainty, K. N. (2025). Part 12: "
                          "Resuscitation education science: 2025 American Heart Association guidelines for cardiopulmonary resuscitation and "
                          "emergency cardiovascular care. <em>Circulation, 152</em>(16 Suppl. 2), S719&ndash;S750. "
                          + _doi("10.1161/CIR.0000000000001374")),
    "grace2024": ("Grace, M. A., &amp; O&rsquo;Malley, R. (2024). Using in situ simulation to identify latent safety threats in emergency medicine: "
                  "A systematic review. <em>Simulation in Healthcare, 19</em>(4), 243&ndash;253. " + _doi("10.1097/SIH.0000000000000748")),
    "khan2013": ("Khan, K. Z., Ramachandran, S., Gaunt, K., &amp; Pushkar, P. (2013). The Objective Structured Clinical Examination (OSCE): "
                 "AMEE Guide No. 81. Part I: An historical and theoretical perspective. <em>Medical Teacher, 35</em>(9), e1437&ndash;e1446. "
                 + _doi("10.3109/0142159X.2013.818634")),
    "tencate2005": ("ten Cate, O. (2005). Entrustability of professional activities and competency-based training. "
                    "<em>Medical Education, 39</em>(12), 1176&ndash;1177. " + _doi("10.1111/j.1365-2929.2005.02341.x")),
}
