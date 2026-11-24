# -*- coding: utf-8 -*-
"""References for the Dialysis Unit Operations Manager / Unit Manager in Hospital (UOM/UMH) track (APA 7).
Merged into SHARED.REFS. Cite in module text as [[key]]. New keys carry the uom_ prefix; shared keys from the POD, DCH and
PD Nurse tracks (doh2012, psn2024, iso23500_1, cdc_dialysis, dch_*, pd_ra9173) are cited as they are and not redefined here.
Journal entries were checked against PubMed metadata on November 24, 2026. Philippine legal and contribution sources carry
bracketed descriptions where the official page title is long or variable; confirm the current issuance before relying on it."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "uom_starmer2014": ("Starmer, A. J., Spector, N. D., Srivastava, R., West, D. C., Rosenbluth, G., Allen, A. D., Noble, E. L., Tse, L. L., "
                        "Dalal, A. K., Keohane, C. A., Lipsitz, S. R., Rothschild, J. M., Wien, M. F., Yoon, C. S., Zigmont, K. R., Wilson, K. M., "
                        "O&rsquo;Toole, J. K., Solan, L. G., Aylor, M., ... Landrigan, C. P. (2014). Changes in medical errors after implementation of a "
                        "handoff program. <em>New England Journal of Medicine, 371</em>(19), 1803&ndash;1812. " + _doi("10.1056/NEJMsa1405556")),
    "uom_saran2006": ("Saran, R., Bragg-Gresham, J. L., Levin, N. W., Twardowski, Z. J., Wizemann, V., Saito, A., Kimata, N., Gillespie, B. W., "
                      "Combe, C., Bommer, J., Akiba, T., Mapes, D. L., Young, E. W., &amp; Port, F. K. (2006). Longer treatment time and slower "
                      "ultrafiltration in hemodialysis: Associations with reduced mortality in the DOPPS. <em>Kidney International, 69</em>(7), "
                      "1222&ndash;1228. " + _doi("10.1038/sj.ki.5000186")),
    "uom_yoder2013": ("Yoder, L. A., Xin, W., Norris, K. C., &amp; Yan, G. (2013). Patient care staffing levels and facility characteristics in U.S. "
                      "hemodialysis facilities. <em>American Journal of Kidney Diseases, 62</em>(6), 1130&ndash;1140. " + _doi("10.1053/j.ajkd.2013.05.007")),
    "uom_perla2011": ("Perla, R. J., Provost, L. P., &amp; Murray, S. K. (2011). The run chart: A simple analytical tool for learning from variation in "
                      "healthcare processes. <em>BMJ Quality &amp; Safety, 20</em>(1), 46&ndash;51. " + _doi("10.1136/bmjqs.2009.037895")),
    "uom_eknoyan2002": ("Eknoyan, G., Beck, G. J., Cheung, A. K., Daugirdas, J. T., Greene, T., Kusek, J. W., Allon, M., Bailey, J., Delmez, J. A., "
                        "Depner, T. A., Dwyer, J. T., Levey, A. S., Levin, N. W., Milford, E., Ornt, D. B., Rocco, M. V., Schulman, G., Schwab, S. J., "
                        "Teehan, B. P., &amp; Toto, R. (2002). Effect of dialysis dose and membrane flux in maintenance hemodialysis. <em>New England "
                        "Journal of Medicine, 347</em>(25), 2010&ndash;2019. " + _doi("10.1056/NEJMoa021583")),
    "uom_gray2015": ("Gray, N. A., Wolley, M., Liew, A., &amp; Nakayama, M. (2015). Natural disasters and dialysis care in the Asia-Pacific. "
                     "<em>Nephrology, 20</em>(12), 873&ndash;880. " + _doi("10.1111/nep.12522")),
    "uom_li2024": ("Li, L. Z., Yang, P., Singer, S. J., Pfeffer, J., Mathur, M. B., &amp; Shanafelt, T. (2024). Nurse burnout and patient safety, "
                   "satisfaction, and quality of care: A systematic review and meta-analysis. <em>JAMA Network Open, 7</em>(11), e2443059. "
                   + _doi("10.1001/jamanetworkopen.2024.43059")),
    "uom_leecha2023": ("Lee, M., &amp; Cha, C. (2023). Interventions to reduce burnout among clinical nurses: Systematic review and meta-analysis. "
                       "<em>Scientific Reports, 13</em>(1), 10971. " + _doi("10.1038/s41598-023-38169-8")),
    "uom_plantinga2024": ("Plantinga, L. C., Bender, A. A., Urbanski, M., Douglas-Ajayi, C., Morgan, J. C., Woo, K., &amp; Jaar, B. G. (2024). "
                          "Patient care technician staffing and outcomes among US patients receiving in-center hemodialysis. <em>JAMA Network Open, "
                          "7</em>(3), e241722. " + _doi("10.1001/jamanetworkopen.2024.1722")),
    "uom_cdc2001": ("Centers for Disease Control and Prevention. (2001). Recommendations for preventing transmission of infections among chronic "
                    "hemodialysis patients. <em>MMWR Recommendations and Reports, 50</em>(RR-5), 1&ndash;43. "
                    + _url("https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm")),
    "uom_cdc1996": ("Centers for Disease Control and Prevention. (1996). Outbreaks of hepatitis B virus infection among hemodialysis "
                    "patients&mdash;California, Nebraska, and Texas, 1994. <em>Morbidity and Mortality Weekly Report, 45</em>(14), 285&ndash;289. "
                    + _url("https://www.cdc.gov/mmwr/preview/mmwrhtml/00040762.htm")),
    "uom_kelman2015": ("Kelman, J., Finne, K., Bogdanov, A., Worrall, C., Margolis, G., Rising, K., MaCurdy, T. E., &amp; Lurie, N. (2015). Dialysis "
                       "care and death following Hurricane Sandy. <em>American Journal of Kidney Diseases, 65</em>(1), 109&ndash;115. "
                       + _doi("10.1053/j.ajkd.2014.07.005")),
    "uom_yi2016": ("Yi, S. H., Kallen, A. J., Hess, S., Bren, V. R., Lincoln, M. E., Downham, G., Kelley, K., Booth, S. L., Weirich, H., Shugart, A., "
                   "Lines, C., Melville, A., Jernigan, J. A., Kleinbaum, D. G., &amp; Patel, P. R. (2016). Sustained infection reduction in "
                   "outpatient hemodialysis centers participating in a collaborative bloodstream infection prevention effort. <em>Infection "
                   "Control &amp; Hospital Epidemiology, 37</em>(7), 863&ndash;866. " + _doi("10.1017/ice.2016.22")),
    "uom_cohen2020": ("Cohen, D. E., Gray, K. S., Colson, C., Van Wyck, D. B., Tentori, F., &amp; Brunelli, S. M. (2020). Impact of rescheduling a "
                      "missed hemodialysis treatment on clinical outcomes. <em>Kidney Medicine, 2</em>(1), 12&ndash;19. "
                      + _doi("10.1016/j.xkme.2019.10.007")),
    "uom_kdigo_hcv2018": ("Kidney Disease: Improving Global Outcomes (KDIGO) Hepatitis C Work Group. (2018). KDIGO 2018 clinical practice guideline "
                          "for the prevention, diagnosis, evaluation, and treatment of hepatitis C in chronic kidney disease. <em>Kidney International "
                          "Supplements, 8</em>(3), 91&ndash;165. " + _url("https://kdigo.org/guidelines/hepatitis-c-in-ckd/")),
    "uom_kdigo_anemia2012": ("Kidney Disease: Improving Global Outcomes (KDIGO) Anemia Work Group. (2012). KDIGO clinical practice guideline for anemia "
                             "in chronic kidney disease. <em>Kidney International Supplements, 2</em>(4), 279&ndash;335. "
                             + _url("https://kdigo.org/guidelines/anemia-in-ckd/")),
    "uom_laborcode": ("Republic of the Philippines. (1974). <em>Presidential Decree No. 442: Labor Code of the Philippines</em> [Book III: hours of "
                      "work, overtime, night shift differential, and holiday pay, as amended]. " + _url("https://lawphil.net/statutes/presdecs/pd1974/pd_442_1974.html")),
    "uom_pd851": ("Republic of the Philippines. (1975). <em>Presidential Decree No. 851: Requiring all employers to pay their employees a 13th-month "
                  "pay</em>. " + _url("https://lawphil.net/statutes/presdecs/pd1975/pd_851_1975.html")),
    "uom_ra11210": ("Republic of the Philippines. (2019). <em>Republic Act No. 11210: 105-Day Expanded Maternity Leave Law</em>. "
                    + _url("https://lawphil.net/statutes/repacts/ra2019/ra_11210_2019.html")),
    "uom_ra11976": ("Republic of the Philippines. (2024). <em>Republic Act No. 11976: Ease of Paying Taxes Act</em>. "
                    + _url("https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html")),
    "uom_wo_ncr28": ("National Wages and Productivity Commission. (2026). <em>Wage Order No. NCR-28</em> [Minimum wage rates in the National Capital "
                     "Region]. " + _url("https://nwpc.dole.gov.ph/")),
    "uom_sss2025": ("Social Security System. (2025). <em>Schedule of SSS contributions effective January 2025</em> [Contribution rate and monthly "
                    "salary credit table]. " + _url("https://www.sss.gov.ph/")),
    "uom_ph_pa2025": ("Philippine Health Insurance Corporation. (2025). <em>PhilHealth Advisory No. 2025-0002</em> [Premium contribution rate and "
                      "income ceiling for 2025]. " + _url("https://www.philhealth.gov.ph/advisories/2025/PA2025-0002.pdf")),
    "uom_hdmf460": ("Home Development Mutual Fund. (2024). <em>HDMF Circular No. 460</em> [Revised monthly compensation ceiling for Pag-IBIG Fund "
                    "contributions]. " + _url("https://www.pagibigfund.gov.ph/")),
}
