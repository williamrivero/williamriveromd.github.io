# -*- coding: utf-8 -*-
"""References for the Occupational and Physical Therapist (OT/PT) track (APA 7). Merged into SHARED.REFS like the other tracks.
Cite in module text as [[key]]. Keys are prefixed otpt_ so nothing collides with other tracks. Journal entries were built from
PubMed metadata retrieved on November 25, 2026. Regulatory entries are carried from the handoff evidence register
(03-evidence-register.md, checked November 25, 2026). The track also cites shared keys already verified for other tracks:
johansen2007, zhao2020, rockwood2005, kroenke2001, watnick2005, murtagh2007, lavery2015, hn_rayner2014, hn_cavanaugh2010."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    # ── guidelines ──
    "otpt_kdigo2024": ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. (2024). KDIGO 2024 clinical practice guideline for the "
                       "evaluation and management of chronic kidney disease. <em>Kidney International, 105</em>(4S), S117&ndash;S314. "
                       + _doi("10.1016/j.kint.2023.10.018")),
    "otpt_baker2022": ("Baker, L. A., March, D. S., Wilkinson, T. J., Billany, R. E., Bishop, N. C., Castle, E. M., Chilcot, J., Davies, M. D., "
                       "Graham-Brown, M. P. M., Greenwood, S. A., Junglee, N. A., Kanavaki, A. M., Lightfoot, C. J., Macdonald, J. H., Rossetti, "
                       "G. M. K., Smith, A. C., &amp; Burton, J. O. (2022). Clinical practice guideline exercise and lifestyle in chronic kidney "
                       "disease. <em>BMC Nephrology, 23</em>(1), 75. " + _doi("10.1186/s12882-021-02618-1")),
    "otpt_bennett2022": ("Bennett, P. N., Bohm, C., Harasemiw, O., Brown, L., Gabrys, I., Jegatheesan, D., Johnson, D. W., Lambert, K., Lightfoot, "
                         "C. J., MacRae, J., Meade, A., Parker, K., Scholes-Robertson, N., Stewart, K., Tarca, B., Verdin, N., Wang, A. Y., Warren, "
                         "M., West, M., Zimmerman, D., Li, P. K., &amp; Thompson, S. (2022). Physical activity and exercise in peritoneal dialysis: "
                         "International Society for Peritoneal Dialysis and the Global Renal Exercise Network practice recommendations. "
                         "<em>Peritoneal Dialysis International, 42</em>(1), 8&ndash;24. " + _doi("10.1177/08968608211055290")),
    # ── trials and reviews of exercise ──
    "otpt_heiwe2011": ("Heiwe, S., &amp; Jacobson, S. H. (2011). Exercise training for adults with chronic kidney disease. <em>Cochrane Database "
                       "of Systematic Reviews, 2011</em>(10), CD003236. " + _doi("10.1002/14651858.CD003236.pub2")),
    "otpt_andingrost2023": ("Anding-Rost, K., von Gersdorff, G., von Korn, P., Ihorst, G., Josef, A., Kaufmann, M., Huber, M., B&auml;r, T., "
                            "Zei&szlig;ler, S., H&ouml;fling, S., Breuer, C., G&auml;rtner, N., Haykowsky, M. J., Degenhardt, S., Wanner, C., &amp; "
                            "Halle, M. (2023). Exercise during hemodialysis in patients with chronic kidney failure. <em>NEJM Evidence, 2</em>(9), "
                            "EVIDoa2300057. " + _doi("10.1056/EVIDoa2300057")),
    "otpt_greenwood2021": ("Greenwood, S. A., Koufaki, P., Macdonald, J. H., Bhandari, S., Burton, J. O., Dasgupta, I., Farrington, K., Ford, I., "
                           "Kalra, P. A., Kean, S., Kumwenda, M., Macdougall, I. C., Messow, C.-M., Mitra, S., Reid, C., Smith, A. C., Taal, M. W., "
                           "Thomson, P. C., Wheeler, D. C., White, C., Yaqoob, M., &amp; Mercer, T. H. (2021). Randomized trial&mdash;PrEscription of "
                           "intraDialytic exercise to improve quAlity of Life in patients receiving hemodialysis. <em>Kidney International Reports, "
                           "6</em>(8), 2159&ndash;2170. " + _doi("10.1016/j.ekir.2021.05.034")),
    "otpt_grahambrown2021": ("Graham-Brown, M. P. M., March, D. S., Young, R., Highton, P. J., Young, H. M. L., Churchward, D. R., Dungey, M., "
                             "Stensel, D. J., Bishop, N. C., Brunskill, N. J., Smith, A. C., McCann, G. P., McConnachie, A., &amp; Burton, J. O. "
                             "(2021). A randomized controlled trial to investigate the effects of intra-dialytic cycling on left ventricular mass. "
                             "<em>Kidney International, 99</em>(6), 1478&ndash;1486. " + _doi("10.1016/j.kint.2021.02.027")),
    "otpt_manfredini2017": ("Manfredini, F., Mallamaci, F., D&rsquo;Arrigo, G., Baggetta, R., Bolignano, D., Torino, C., Lamberti, N., Bertoli, S., "
                            "Ciurlino, D., Rocca-Rey, L., Barill&agrave;, A., Battaglia, Y., Rapan&agrave;, R. M., Zuccal&agrave;, A., Bonanno, G., "
                            "Fatuzzo, P., Rapisarda, F., Rastelli, S., Fabrizi, F., &hellip; Zoccali, C. (2017). Exercise in patients on dialysis: A "
                            "multicenter, randomized clinical trial. <em>Journal of the American Society of Nephrology, 28</em>(4), 1259&ndash;1268. "
                            + _doi("10.1681/ASN.2016030378")),
    "otpt_painter2002": ("Painter, P. L., Hector, L., Ray, K., Lynes, L., Dibble, S., Paul, S. M., Tomlanovich, S. L., &amp; Ascher, N. L. (2002). "
                         "A randomized trial of exercise training after renal transplantation. <em>Transplantation, 74</em>(1), 42&ndash;48. "
                         + _doi("10.1097/00007890-200207150-00008")),
    "otpt_mcadams2019": ("McAdams-DeMarco, M. A., Ying, H., Van Pilsum Rasmussen, S., Schrack, J., Haugen, C. E., Chu, N. M., Gonz&aacute;lez "
                         "Fern&aacute;ndez, M., Desai, N., Walston, J. D., &amp; Segev, D. L. (2019). Prehabilitation prior to kidney "
                         "transplantation: Results from a pilot study. <em>Clinical Transplantation, 33</em>(1), e13450. " + _doi("10.1111/ctr.13450")),
    "otpt_aragoncillo2021": ("Aragoncillo Sauco, I., Hevia, C., Manzano Grossi, S., Amezquita, Y., Macias, N., Caldes, S., Ramirez Senent, B., "
                             "Hernandez Hernandez, Y., Goicoechea, M., &amp; Physicalfav Working Group. (2021). Effect of preoperative exercise on "
                             "vascular caliber and maturation of arteriovenous fistula: The Physicalfav trial, a randomized controlled study. "
                             "<em>Journal of Nephrology, 34</em>(3), 763&ndash;771. " + _doi("10.1007/s40620-020-00907-w")),
    "otpt_chen2023": ("Chen, J.-W., Fu, H.-Y., Hii, I.-H., Tseng, H.-W., Chang, P.-Y., Chang, C.-H., Chen, Y.-S., Hsu, R.-B., Wu, I.-H., Chen, "
                      "Y.-M., Chu, T.-S., Hung, K.-Y., Lin, S.-L., Wu, K.-D., &amp; Chan, C.-Y. (2023). A randomized trial of postoperative "
                      "handgrip exercises for fistula maturation in patients with newly created wrist radiocephalic arteriovenous fistulas. "
                      "<em>Kidney International Reports, 8</em>(3), 566&ndash;574. " + _doi("10.1016/j.ekir.2022.12.019")),
    "otpt_schweickert2009": ("Schweickert, W. D., Pohlman, M. C., Pohlman, A. S., Nigos, C., Pawlik, A. J., Esbrook, C. L., Spears, L., Miller, "
                             "M., Franczyk, M., Deprizio, D., Schmidt, G. A., Bowman, A., Barr, R., McCallister, K. E., Hall, J. B., &amp; Kress, "
                             "J. P. (2009). Early physical and occupational therapy in mechanically ventilated, critically ill patients: A "
                             "randomised controlled trial. <em>The Lancet, 373</em>(9678), 1874&ndash;1882. " + _doi("10.1016/S0140-6736(09)60658-9")),
    # ── cohorts and measurement ──
    "otpt_herridge2011": ("Herridge, M. S., Tansey, C. M., Matt&eacute;, A., Tomlinson, G., Diaz-Granados, N., Cooper, A., Guest, C. B., Mazer, "
                          "C. D., Mehta, S., Stewart, T. E., Kudlow, P., Cook, D., Slutsky, A. S., Cheung, A. M., &amp; Canadian Critical Care "
                          "Trials Group. (2011). Functional disability 5 years after acute respiratory distress syndrome. <em>The New England "
                          "Journal of Medicine, 364</em>(14), 1293&ndash;1304. " + _doi("10.1056/NEJMoa1011802")),
    "otpt_roshanravan2013": ("Roshanravan, B., Robinson-Cohen, C., Patel, K. V., Ayers, E., Littman, A. J., de Boer, I. H., Ikizler, T. A., "
                             "Himmelfarb, J., Katzel, L. I., Kestenbaum, B., &amp; Seliger, S. (2013). Association between physical performance "
                             "and all-cause mortality in CKD. <em>Journal of the American Society of Nephrology, 24</em>(5), 822&ndash;830. "
                             + _doi("10.1681/ASN.2012070702")),
    "otpt_studenski2011": ("Studenski, S., Perera, S., Patel, K., Rosano, C., Faulkner, K., Inzitari, M., Brach, J., Chandler, J., Cawthon, P., "
                           "Connor, E. B., Nevitt, M., Visser, M., Kritchevsky, S., Badinelli, S., Harris, T., Newman, A. B., Cauley, J., "
                           "Ferrucci, L., &amp; Guralnik, J. (2011). Gait speed and survival in older adults. <em>JAMA, 305</em>(1), 50&ndash;58. "
                           + _doi("10.1001/jama.2010.1923")),
    "otpt_guralnik1994": ("Guralnik, J. M., Simonsick, E. M., Ferrucci, L., Glynn, R. J., Berkman, L. F., Blazer, D. G., Scherr, P. A., &amp; "
                          "Wallace, R. B. (1994). A short physical performance battery assessing lower extremity function: Association with "
                          "self-reported disability and prediction of mortality and nursing home admission. <em>Journal of Gerontology, "
                          "49</em>(2), M85&ndash;M94. " + _doi("10.1093/geronj/49.2.m85")),
    "otpt_enright1998": ("Enright, P. L., &amp; Sherrill, D. L. (1998). Reference equations for the six-minute walk in healthy adults. "
                         "<em>American Journal of Respiratory and Critical Care Medicine, 158</em>(5 Pt 1), 1384&ndash;1387. "
                         + _doi("10.1164/ajrccm.158.5.9710086")),
    "otpt_cook2006": ("Cook, W. L., Tomlinson, G., Donaldson, M., Markowitz, S. N., Naglie, G., Sobolev, B., &amp; Jassal, S. V. (2006). Falls and "
                      "fall-related injuries in older dialysis patients. <em>Clinical Journal of the American Society of Nephrology, 1</em>(6), "
                      "1197&ndash;1204. " + _doi("10.2215/CJN.01650506")),
    "otpt_alem2000": ("Alem, A. M., Sherrard, D. J., Gillen, D. L., Weiss, N. S., Beresford, S. A., Heckbert, S. R., Wong, C., &amp; "
                      "Stehman-Breen, C. (2000). Increased risk of hip fracture among patients with end-stage renal disease. <em>Kidney "
                      "International, 58</em>(1), 396&ndash;399. " + _doi("10.1046/j.1523-1755.2000.00178.x")),
    "otpt_murray2006": ("Murray, A. M., Tupper, D. E., Knopman, D. S., Gilbertson, D. T., Pederson, S. L., Li, S., Smith, G. E., Hochhalter, A. K., "
                        "Collins, A. J., &amp; Kane, R. L. (2006). Cognitive impairment in hemodialysis patients is common. <em>Neurology, "
                        "67</em>(2), 216&ndash;223. " + _doi("10.1212/01.wnl.0000225182.15532.40")),
    "otpt_palmer2013": ("Palmer, S., Vecchio, M., Craig, J. C., Tonelli, M., Johnson, D. W., Nicolucci, A., Pellegrini, F., Saglimbene, V., "
                        "Logroscino, G., Fishbane, S., &amp; Strippoli, G. F. M. (2013). Prevalence of depression in chronic kidney disease: "
                        "Systematic review and meta-analysis of observational studies. <em>Kidney International, 84</em>(1), 179&ndash;191. "
                        + _doi("10.1038/ki.2013.77")),
    # ── Philippine law, regulation and payer policy (carried from the handoff evidence register) ──
    "otpt_ra5680": ("Republic of the Philippines. (1969). <em>Republic Act No. 5680: An act to regulate the practice of physical and occupational "
                    "therapy in the Philippines</em> (Secs. 2 and 12). " + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/6154")),
    "otpt_ra11241": ("Republic of the Philippines. (2019). <em>Republic Act No. 11241: Philippine Occupational Therapy Law of 2018</em> (Secs. 3, "
                     "26&ndash;29). " + _url("https://lawphil.net/statutes/repacts/ra2019/ra_11241_2019.html")),
    "otpt_prc_pt": ("Professional Regulation Commission (PRC). (2026). <em>Professional Regulatory Board of Physical Therapy</em>. Retrieved "
                    "November 25, 2026, from " + _url("https://www.prc.gov.ph/Pages/PRBv4/PhysicalOccupationalTherapyv1.htm")),
    "otpt_prc_ot": ("Professional Regulation Commission (PRC). (2026). <em>Professional Regulatory Board of Occupational Therapy</em>. Retrieved "
                    "November 25, 2026, from " + _url("https://prc.gov.ph/Pages/PRBv4/OccupationalTherapyv2.htm")),
    "otpt_doh2012": ("Department of Health (DOH). (2012). <em>Administrative Order No. 2012-0001: New rules and regulations governing the "
                     "licensure and regulation of dialysis facilities in the Philippines</em>. "
                     + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/50687")),
    "otpt_pc2025_0003": ("Philippine Health Insurance Corporation (PHIC). (2025). <em>PhilHealth Circular No. 2025-0003: Physical medicine "
                         "and rehabilitation services and assistive mobility devices</em>. "
                         + _url("https://www.philhealth.gov.ph/circulars/2025/PC2025-0003.pdf")),
    "otpt_pa2025_0014": ("Philippine Health Insurance Corporation (PHIC). (2025). <em>PhilHealth Advisory No. 2025-0014: Provider "
                         "self-assessment tools</em>. " + _url("https://www.philhealth.gov.ph/advisories/2025/PA2025-0014.pdf")),
    "otpt_pa2025_0027": ("Philippine Health Insurance Corporation (PHIC). (2025). <em>PhilHealth Advisory No. 2025-0027: Clarification on "
                         "medicines under the physical medicine and rehabilitation services benefit</em>. "
                         + _url("https://www.philhealth.gov.ph/advisories/2025/PA2025-0027.pdf")),
    "otpt_pc2024_0023": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0023: Hemodialysis "
                         "benefit package</em>. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "otpt_ph_contracted": ("Philippine Health Insurance Corporation (PHIC). (2026). <em>Contracted health facilities</em>. Retrieved "
                           "November 25, 2026, from " + _url("https://www.philhealth.gov.ph/partners/providers/facilities/contracted/")),
    "otpt_psn_cpg": ("Philippine Society of Nephrology (PSN). (2026). <em>Clinical practice guidelines and protocols</em>. Retrieved November 25, "
                     "2026, from " + _url("https://psn.org.ph/education/clinical-practice-guideline-and-protocols/")),
    "otpt_cdc_dialysis": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Dialysis safety: Infection control</em>. Retrieved "
                          "November 25, 2026, from " + _url("https://www.cdc.gov/dialysis-safety/hcp/infection-control/index.html")),
    # ── international service models (comparison only) ──
    "otpt_cfr494": ("United States Government Publishing Office. (2025). <em>42 CFR Part 494: Conditions for coverage for end-stage renal disease "
                    "facilities</em> (&sect;&sect; 494.80, 494.90). " + _url("https://www.govinfo.gov/content/pkg/CFR-2025-title42-vol5/xhtml/CFR-2025-title42-vol5-part494.html")),
    "otpt_hcpc_ot": ("Health and Care Professions Council (HCPC). (2023). <em>Standards of proficiency: Occupational therapists</em>. "
                     + _url("https://www.hcpc-uk.org/standards/standards-of-proficiency/occupational-therapists/")),
    "otpt_hcpc_pt": ("Health and Care Professions Council (HCPC). (2023). <em>Standards of proficiency: Physiotherapists</em>. "
                     + _url("https://www.hcpc-uk.org/standards/standards-of-proficiency/physiotherapists/")),
    "otpt_aus_allied": ("Services Australia. (2026). <em>Specific criteria for allied health and primary care professionals</em>. Retrieved "
                        "November 25, 2026, from " + _url("https://www.servicesaustralia.gov.au/specific-criteria-for-allied-health-and-primary-care-professionals?context=20")),
    "otpt_manitoba": ("Manitoba Renal Program. (2013). <em>Renal occupational therapy</em>. "
                      + _url("https://www.kidneyhealth.ca/renal-occupational-therapy/")),
}
