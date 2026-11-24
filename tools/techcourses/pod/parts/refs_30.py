# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 30 (APA 7). Journal entries were checked against PubMed metadata
on November 25, 2026; web sources were checked on the same date. Keys already defined or registered in the course
(foley2011, saran2003, ward1996, tipple1991, greenberg2021, daugirdas2015, doh2012, psn2024) are not repeated.
Module 30 owns doh_ao2013_0003; Module 31 reuses it."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "anderson2009": ("Anderson, A. H., Cohen, A. J., Kutner, N. G., Kopp, J. B., Kimmel, P. L., &amp; Muntner, P. (2009). Missed dialysis sessions "
                     "and hospitalization in hemodialysis patients after Hurricane Katrina. <em>Kidney International, 75</em>(11), 1202&ndash;1208. "
                     + _doi("10.1038/ki.2009.5")),
    "lurie2015": ("Lurie, N., Finne, K., Worrall, C., Jauregui, M., Thaweethai, T., Margolis, G., &amp; Kelman, J. (2015). Early dialysis and "
                  "adverse outcomes after Hurricane Sandy. <em>American Journal of Kidney Diseases, 66</em>(3), 507&ndash;512. "
                  + _doi("10.1053/j.ajkd.2015.04.050")),
    "kelman2015": ("Kelman, J., Finne, K., Bogdanov, A., Worrall, C., Margolis, G., Rising, K., MaCurdy, T. E., &amp; Lurie, N. (2015). Dialysis "
                   "care and death following Hurricane Sandy. <em>American Journal of Kidney Diseases, 65</em>(1), 109&ndash;115. "
                   + _doi("10.1053/j.ajkd.2014.07.005")),
    "murakami2015": ("Murakami, N., Siktel, H. B., Lucido, D., Winchester, J. F., &amp; Harbord, N. B. (2015). Disaster preparedness and awareness "
                     "of patients on hemodialysis after Hurricane Sandy. <em>Clinical Journal of the American Society of Nephrology, 10</em>(8), "
                     "1389&ndash;1396. " + _doi("10.2215/CJN.10181014")),
    "kopp2007": ("Kopp, J. B., Ball, L. K., Cohen, A., Kenney, R. J., Lempert, K. D., Miller, P. E., Muntner, P., Qureshi, N., &amp; Yelton, S. A. "
                 "(2007). Kidney patient care in disasters: Lessons from the hurricanes and earthquake of 2005. <em>Clinical Journal of the "
                 "American Society of Nephrology, 2</em>(4), 814&ndash;824. " + _doi("10.2215/CJN.03481006")),
    "sever2023": ("Sever, M. S., Luyckx, V., Tonelli, M., Kazancioglu, R., Rodgers, D., Gallego, D., Tuglular, S., &amp; Vanholder, R. (2023). "
                  "Disasters and kidney care: Pitfalls and solutions. <em>Nature Reviews Nephrology, 19</em>(10), 672&ndash;686. "
                  + _doi("10.1038/s41581-023-00743-8")),
    "lameire2020": ("Lameire, N., Sever, M. S., Van Biesen, W., &amp; Vanholder, R. (2020). Role of the international and national renal "
                    "organizations in natural disasters: Strategies for renal rescue. <em>Seminars in Nephrology, 40</em>(4), 393&ndash;407. "
                    + _doi("10.1016/j.semnephrol.2020.06.007")),
    "gray2015": ("Gray, N. A., Wolley, M., Liew, A., &amp; Nakayama, M. (2015). Natural disasters and dialysis care in the Asia-Pacific. "
                 "<em>Nephrology, 20</em>(12), 873&ndash;880. " + _doi("10.1111/nep.12522")),
    "sever2012": ("Sever, M. S., Vanholder, R., &amp; RDRTF of ISN Work Group on Recommendations for the Management of Crush Victims in Mass "
                  "Disasters. (2012). Recommendation for the management of crush victims in mass disasters. <em>Nephrology Dialysis "
                  "Transplantation, 27</em>(Suppl. 1), i1&ndash;i67. " + _doi("10.1093/ndt/gfs156")),
    "kaya2024": ("Kaya, B., Balal, M., Seyrek, N., Mete, B., &amp; Karayaylali, I. (2024). Hemodialysis experience after Kahramanmara&#351; "
                 "earthquake. <em>Journal of Clinical Medicine, 13</em>(21), Article 6610. " + _doi("10.3390/jcm13216610")),
    "tani2014": ("Tani, Y., Nakayama, M., Tanaka, K., Hayashi, Y., Asahi, K., Kamata, T., Ogihara, M., Sato, K., Matsushima, M., &amp; "
                 "Watanabe, T. (2014). Blood pressure elevation in hemodialysis patients after the Great East Japan Earthquake. "
                 "<em>Hypertension Research, 37</em>(2), 139&ndash;144. " + _doi("10.1038/hr.2013.116")),
    "jochimsen1998": ("Jochimsen, E. M., Carmichael, W. W., An, J. S., Cardo, D. M., Cookson, S. T., Holmes, C. E., Antunes, M. B., "
                      "de Melo Filho, D. A., Lyra, T. M., Barreto, V. S., Azevedo, S. M., &amp; Jarvis, W. R. (1998). Liver failure and death "
                      "after exposure to microcystins at a hemodialysis center in Brazil. <em>New England Journal of Medicine, 338</em>(13), "
                      "873&ndash;878. " + _doi("10.1056/NEJM199803263381304")),
    "arnow1994": ("Arnow, P. M., Bland, L. A., Garcia-Houchins, S., Fridkin, S., &amp; Fellner, S. K. (1994). An outbreak of fatal fluoride "
                  "intoxication in a long-term hemodialysis unit. <em>Annals of Internal Medicine, 121</em>(5), 339&ndash;344. "
                  + _doi("10.7326/0003-4819-121-5-199409010-00005")),
    "deoliveira2009": ("de Oliveira, R. M., de los Santos, C. A., Antonello, I., &amp; d&rsquo;Avila, D. (2009). Warning: An anemia outbreak due "
                       "to chloramine exposure in a clean hemodialysis unit. An issue to be revisited. <em>Renal Failure, 31</em>(1), 81&ndash;83. "
                       + _doi("10.1080/08860220802546503")),
    "doh_ao2013_0003": ("Department of Health. (2013). <em>Implementing guidelines in the analysis, monitoring and maintenance of water used in "
                        "dialysis facilities pursuant to Administrative Order No. 2012-0001</em> (Administrative Order No. 2013-0003). "
                        + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036")),
    "iso23500_3_2024": ("International Organization for Standardization. (2024). <em>Preparation and quality management of fluids for "
                        "haemodialysis and related therapies: Part 3. Water for haemodialysis and related therapies</em> (ISO Standard No. "
                        "23500-3:2024). " + _url("https://www.iso.org/standard/84370.html")),
    "pagasa_tcws": ("Philippine Atmospheric, Geophysical and Astronomical Services Administration. (n.d.). <em>Tropical cyclone wind signal</em>. "
                    "Retrieved November 25, 2026, from " + _url("https://pagasa.dost.gov.ph/learning-tools/tropical-cyclone-wind-signal")),
    "cdc_emergency2024": ("Centers for Disease Control and Prevention. (2024). <em>What to do when you need dialysis during an "
                          "emergency</em>. Last reviewed May 15, 2024. " + _url("https://www.cdc.gov/kidney-disease/caring/index.html")),
    "kcer_diet": ("Kidney Community Emergency Response Coalition. (n.d.). <em>3-day emergency kidney diet</em> [Handout]. American Kidney Fund. "
                  "Retrieved November 25, 2026, from " + _url("https://www.kidneyfund.org/sites/default/files/media/documents/3-day-emergency-diet.pdf")),
}
