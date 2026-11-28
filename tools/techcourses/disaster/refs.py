# -*- coding: utf-8 -*-
"""References for Disaster Preparedness and Response (APA 7). Merged into SHARED.REFS like the other tracks.
Journal entries come from the blueprint's source register (DISASTER_PREPAREDNESS_BLUEPRINT.md section 14), checked against
PubMed on November 28, 2026. Philippine sources: official pages checked the same day. DRAFT pending clinical sign-off."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    # ── Dialysis and disasters ──
    "dp_anderson2009": ("Anderson, A. H., Cohen, A. J., Kutner, N. G., Kopp, J. B., Kimmel, P. L., &amp; Muntner, P. (2009). Missed dialysis "
                        "sessions and hospitalization in hemodialysis patients after Hurricane Katrina. <em>Kidney International, 75</em>(11), "
                        "1202&ndash;1208. " + _doi("10.1038/ki.2009.5")),
    "dp_kutner2009": ("Kutner, N. G., Muntner, P., Huang, Y., Zhang, R., Cohen, A. J., Anderson, A. H., &amp; Eggers, P. W. (2009). Effect of "
                      "Hurricane Katrina on the mortality of dialysis patients. <em>Kidney International, 76</em>(7), 760&ndash;766. "
                      + _doi("10.1038/ki.2009.268")),
    "dp_kelman2015": ("Kelman, J., Finne, K., Bogdanov, A., Worrall, C., Margolis, G., Rising, K., MaCurdy, T. E., &amp; Lurie, N. (2015). "
                      "Dialysis care and death following Hurricane Sandy. <em>American Journal of Kidney Diseases, 65</em>(1), 109&ndash;115. "
                      + _doi("10.1053/j.ajkd.2014.07.005")),
    "dp_lurie2015": ("Lurie, N., Finne, K., Worrall, C., Jauregui, M., Thaweethai, T., Margolis, G., &amp; Kelman, J. (2015). Early dialysis "
                     "and adverse outcomes after Hurricane Sandy. <em>American Journal of Kidney Diseases, 66</em>(3), 507&ndash;512. "
                     + _doi("10.1053/j.ajkd.2015.04.050")),
    "dp_remigio2023": ("Remigio, R. V., Song, H., Raimann, J. G., Kotanko, P., Maddux, F. W., Lasky, R. A., He, X., &amp; Sapkota, A. (2023). "
                       "Inclement weather and risk of missing scheduled hemodialysis appointments among patients with kidney failure. "
                       "<em>Clinical Journal of the American Society of Nephrology, 18</em>(7), 904&ndash;912. "
                       + _doi("10.2215/CJN.0000000000000174")),
    "dp_rivera2022": ("Rivera-Hernandez, M., Kim, D., Nguyen, K. H., Thorsness, R., Lee, Y., Swaminathan, S., Mehrotra, R., &amp; Trivedi, A. N. "
                      "(2022). Changes in migration and mortality among patients with kidney failure in Puerto Rico after Hurricane Maria. "
                      "<em>JAMA Health Forum, 3</em>(8), e222534. " + _doi("10.1001/jamahealthforum.2022.2534")),
    "dp_bonilla2019": ("Bonilla-F&eacute;lix, M., &amp; Su&aacute;rez-Rivera, M. (2019). Disaster management in a nephrology service: Lessons "
                       "learned from Hurricane Maria. <em>Blood Purification, 47</em>(1&ndash;3), 199&ndash;204. " + _doi("10.1159/000494580")),
    "dp_aviles2021": ("Avil&eacute;s Mendoza, G. J., Finne, K. P., Torre Leon, F., Burke, L. M., Cabrera-Marquez, J., Mercado Casillas, A. M., "
                      "Malave, G., Brown, C., Kelman, J., &amp; Kopp, J. B. (2021). Observations from the emergency management of dialysis "
                      "patients evacuated from the US Virgin Islands to Puerto Rico following hurricane Irma. <em>BMC Health Services "
                      "Research, 21</em>(1), 1239. " + _doi("10.1186/s12913-021-07194-6")),
    "dp_haga2013": ("Haga, N., Hata, J., Yabe, M., Ishibashi, K., Takahashi, N., Kumagai, K., Ogawa, S., Kataoka, M., Akaihata, H., &amp; "
                    "Kojima, Y. (2013). The Great East Japan Earthquake affected the laboratory findings of hemodialysis patients in "
                    "Fukushima. <em>BMC Nephrology, 14</em>, 239. " + _doi("10.1186/1471-2369-14-239")),
    "dp_ido2022": ("Ido, K., Miyazaki, M., &amp; Nakayama, M. (2022). Hemodialysis record sharing: Solution for work burden reduction and "
                   "disaster preparedness. <em>JMIR Formative Research, 6</em>(7), e32925. " + _doi("10.2196/32925")),
    "dp_ozen2026": ("Ozen, N., Ozturk, S., Dunya, C. P., Hryszko, T., Fernandes, F., Vovlianou, S., Rotmans, J. I., Lindhard, K., Velarde, "
                    "E. C., Parmaksiz, E., Kaya, D., Kocak, S. Y., Turan, F., Celik, A., Coban, I., Sousa, C. N., &amp; Unver, V. (2026). An "
                    "international multicentre study of haemodialysis patients&rsquo; knowledge of safe self-disconnection from the dialysis "
                    "machine in emergencies. <em>Journal of Renal Care, 52</em>(3), e70080. " + _doi("10.1111/jorc.70080")),
    "dp_lin2021": ("Lin, W.-H., Lin, Y.-J., Wang, M.-F., Yeh, S.-M., Hsu, T.-C., &amp; Chang, Y.-T. (2021). [A project to improve the ability "
                   "of hemodialysis staff to respond to fire emergencies]. <em>Hu Li Za Zhi, 68</em>(2), 65&ndash;74. "
                   + _doi("10.6224/JN.202104_68(2).09")),
    "dp_kawabata2017": ("Kawabata, C., Hamanoue, S., Maekawa, A., Toyoda, M., Miyata, A., &amp; Uekihara, S. (2017). Communication with "
                        "peritoneal dialysis patients post-Kumamoto earthquake. <em>Peritoneal Dialysis International, 37</em>(4), 484&ndash;485. "
                        + _doi("10.3747/pdi.2016.00310")),
    "dp_sever2023": ("Sever, M. S., Luyckx, V., Tonelli, M., Kazancioglu, R., Rodgers, D., Gallego, D., Tuglular, S., &amp; Vanholder, R. "
                     "(2023). Disasters and kidney care: Pitfalls and solutions. <em>Nature Reviews Nephrology, 19</em>(10), 672&ndash;686. "
                     + _doi("10.1038/s41581-023-00743-8")),
    "dp_sandal2025": ("Sandal, S., El Wazze, S., Nijjar, D., Ethier, I., Paparella, A. N., Hales, L., Finkle, S. N., Jha, V., &amp; Stigant, C. "
                      "(2025). A roadmap for disaster risk reduction and management in kidney care: A scoping review and content analysis. "
                      "<em>Journal of the American Society of Nephrology, 36</em>(7), 1363&ndash;1379. " + _doi("10.1681/ASN.0000000635")),
    "dp_sandal2026": ("Sandal, S., Clarke, A., Le, A., Paparella, A. N., Berry, W. A. D., &amp; Vanholder, R. (2026). Disasters and hazard "
                      "exposure in end-stage kidney disease: A scoping review of patient outcomes. <em>Clinical Kidney Journal, 19</em>(10), "
                      "sfag318. " + _doi("10.1093/ckj/sfag318")),
    "dp_sever2024": ("Sever, M. S., Vanholder, R., &amp; Lameire, N. (2024). Disaster preparedness for people with kidney disease and kidney "
                     "healthcare providers. <em>Current Opinion in Nephrology and Hypertension, 33</em>(6), 613&ndash;620. "
                     + _doi("10.1097/MNH.0000000000001014")),
    "dp_hyre2007": ("Hyre, A. D., Cohen, A. J., Kutner, N., Alper, A. B., &amp; Muntner, P. (2007). Prevalence and predictors of posttraumatic "
                    "stress disorder among hemodialysis patients following Hurricane Katrina. <em>American Journal of Kidney Diseases, "
                    "50</em>(4), 585&ndash;593. " + _doi("10.1053/j.ajkd.2007.07.013")),
    "dp_edmondson2013": ("Edmondson, D., Gamboa, C., Cohen, A., Anderson, A. H., Kutner, N., Kronish, I., Mills, M. A., &amp; Muntner, P. "
                         "(2013). Association of posttraumatic stress disorder and depression with all-cause and cardiovascular disease "
                         "mortality and hospitalization among Hurricane Katrina survivors with end-stage renal disease. <em>American Journal "
                         "of Public Health, 103</em>(4), e130&ndash;e137. " + _doi("10.2105/AJPH.2012.301146")),
    # ── Drills and training ──
    "dp_hsu2004": ("Hsu, E. B., Jenckes, M. W., Catlett, C. L., Robinson, K. A., Feuerstein, C., Cosgrove, S. E., Green, G. B., &amp; Bass, "
                   "E. B. (2004). Effectiveness of hospital staff mass-casualty incident training methods: A systematic literature review. "
                   "<em>Prehospital and Disaster Medicine, 19</em>(3), 191&ndash;199. " + _doi("10.1017/s1049023x00001771")),
    # ── Philippine law, policy and public guidance ──
    "dp_ra10121": ("Congress of the Philippines. (2010, May 27). <em>Republic Act No. 10121: Philippine Disaster Risk Reduction and Management "
                   "Act of 2010</em>. Senate of the Philippines Legislative Reference. "
                   + _url("https://issuances-library.senate.gov.ph/legislative-issuance/republic-act-no-10121")),
    "dp_doh2019": ("Department of Health. (2019, October 29). <em>National policy on disaster risk reduction and management in health (DRRM-H)</em> "
                   "(Administrative Order No. 2019-0046). Republic of the Philippines."),
    "dp_doh2020": ("Department of Health. (2020). <em>Guidelines on the institutionalization of disaster risk reduction and management in "
                   "health (DRRM-H) in province-wide and city-wide health systems</em> (Administrative Order No. 2020-0036). Republic of the "
                   "Philippines."),
    "dp_doh2013": ("Department of Health. (2013, March 21). <em>Policies and guidelines on hospitals safe from disasters</em> (Administrative "
                   "Order No. 2013-0014). Supreme Court E-Library. " + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocsfriendly/10/70762")),
    "dp_ra9514": ("Bureau of Fire Protection. (2019). <em>Revised implementing rules and regulations of Republic Act No. 9514, the Fire Code "
                  "of the Philippines of 2008</em>. Republic of the Philippines."),
    "dp_ra10173": ("Republic of the Philippines. (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. "
                   + _url("https://privacy.gov.ph/data-privacy-act/")),
    "dp_pagasa_tcws": ("Philippine Atmospheric, Geophysical and Astronomical Services Administration. (n.d.). <em>Tropical cyclone wind "
                       "signal</em>. Retrieved November 28, 2026, from "
                       + _url("https://pagasa.dost.gov.ph/learning-tools/tropical-cyclone-wind-signal")),
    "dp_ocd_nsed": ("Office of Civil Defense &amp; National Disaster Risk Reduction and Management Council. (2026). <em>Nationwide "
                    "Simultaneous Earthquake Drill</em> [Quarterly national campaign; 2026 drills held March 12, June 18, September 10 and "
                    "November 5]. Republic of the Philippines."),
    "dp_fema2025": ("Federal Emergency Management Agency. (2025, January 21). <em>Fact sheet: Earthquake information for people with "
                    "disabilities</em>. Retrieved November 28, 2026, from "
                    + _url("https://www.fema.gov/press-release/20250121/fact-sheet-earthquake-information-people-disabilities")),
}
