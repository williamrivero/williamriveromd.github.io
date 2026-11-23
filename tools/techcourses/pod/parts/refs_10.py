# -*- coding: utf-8 -*-
"""New references for Physician on Duty, Module 10: The Lifeline II: Catheters (APA 7).
Journal entries were checked against PubMed metadata on November 23, 2026. CDC entries were read on cdc.gov the same day."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    "kdoqi_va2019": ("Lok, C. E., Huber, T. S., Lee, T., Shenoy, S., Yevzlin, A. S., Abreo, K., Allon, M., Asif, A., Astor, B. C., Glickman, M. H., "
                     "Graham, J., Moist, L. M., Rajan, D. K., Roberts, C., Vachharajani, T. J., Valentini, R. P., &amp; National Kidney Foundation. (2020). "
                     "KDOQI clinical practice guideline for vascular access: 2019 update. "
                     "<em>American Journal of Kidney Diseases, 75</em>(4, Suppl. 2), S1&ndash;S164. " + _doi("10.1053/j.ajkd.2019.12.001")),
    "idsa_crbsi2009": ("Mermel, L. A., Allon, M., Bouza, E., Craven, D. E., Flynn, P., O&rsquo;Grady, N. P., Raad, I. I., Rijnders, B. J. A., "
                       "Sherertz, R. J., &amp; Warren, D. K. (2009). Clinical practice guidelines for the diagnosis and management of intravascular "
                       "catheter-related infection: 2009 update by the Infectious Diseases Society of America. "
                       "<em>Clinical Infectious Diseases, 49</em>(1), 1&ndash;45. " + _doi("10.1086/599376")),
    "cdc_dialysis_bsi2024": ("Centers for Disease Control and Prevention. (2024, March 29). <em>Best practices for bloodstream infection prevention "
                             "in dialysis setting</em>. " + _url("https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/index.html")),
    "cdc_scrubhub": ("Centers for Disease Control and Prevention. (n.d.). <em>Hemodialysis central venous catheter scrub-the-hub protocol</em>. "
                     "National Center for Emerging and Zoonotic Infectious Diseases, Division of Healthcare Quality Promotion. "
                     + _url("https://www.cdc.gov/dialysis-safety/media/pdfs/Hemodialysis-Central-Venous-Catheter-STH-Protocol-P.pdf")),
    "ravani2013": ("Ravani, P., Palmer, S. C., Oliver, M. J., Quinn, R. R., MacRae, J. M., Tai, D. J., Pannu, N. I., Thomas, C., Hemmelgarn, B. R., "
                   "Craig, J. C., Manns, B., Tonelli, M., Strippoli, G. F. M., &amp; James, M. T. (2013). Associations between hemodialysis access type "
                   "and clinical outcomes: A systematic review. <em>Journal of the American Society of Nephrology, 24</em>(3), 465&ndash;473. "
                   + _doi("10.1681/ASN.2012070643")),
    "hemmelgarn2011": ("Hemmelgarn, B. R., Moist, L. M., Lok, C. E., Tonelli, M., Manns, B. J., Holden, R. M., LeBlanc, M., Faris, P., Barre, P., "
                       "Zhang, J., &amp; Scott-Douglas, N. (2011). Prevention of dialysis catheter malfunction with recombinant tissue plasminogen "
                       "activator. <em>New England Journal of Medicine, 364</em>(4), 303&ndash;312. " + _doi("10.1056/NEJMoa1011376")),
    "rosenblum2014": ("Rosenblum, A., Wang, W., Ball, L. K., Latham, C., Maddux, F. W., &amp; Lacson, E., Jr. (2014). Hemodialysis catheter care "
                      "strategies: A cluster-randomized quality improvement initiative. <em>American Journal of Kidney Diseases, 63</em>(2), "
                      "259&ndash;267. " + _doi("10.1053/j.ajkd.2013.08.019")),
    "patel2013": ("Patel, P. R., Yi, S. H., Booth, S., Bren, V., Downham, G., Hess, S., Kelley, K., Lincoln, M., Morrissette, K., Lindberg, C., "
                  "Jernigan, J. A., &amp; Kallen, A. J. (2013). Bloodstream infection rates in outpatient hemodialysis facilities participating in a "
                  "collaborative prevention effort: A quality improvement report. <em>American Journal of Kidney Diseases, 62</em>(2), 322&ndash;330. "
                  + _doi("10.1053/j.ajkd.2013.03.011")),
    "pannu2006": ("Pannu, N., Jhangri, G. S., &amp; Tonelli, M. (2006). Optimizing dialysis delivery in tunneled dialysis catheters. "
                  "<em>ASAIO Journal, 52</em>(2), 157&ndash;162. " + _doi("10.1097/01.mat.0000202081.13974.39")),
    "greenberg2021": ("Greenberg, K. I., &amp; Choi, M. J. (2021). Hemodialysis emergencies: Core curriculum 2021. "
                      "<em>American Journal of Kidney Diseases, 77</em>(5), 796&ndash;809. " + _doi("10.1053/j.ajkd.2020.11.024")),
    "cdc_bsi2011": ("O&rsquo;Grady, N. P., Alexander, M., Burns, L. A., Dellinger, E. P., Garland, J., Heard, S. O., Lipsett, P. A., Masur, H., "
                    "Mermel, L. A., Pearson, M. L., Raad, I. I., Randolph, A. G., Rupp, M. E., Saint, S., &amp; Healthcare Infection Control Practices "
                    "Advisory Committee. (2011). Guidelines for the prevention of intravascular catheter-related infections. "
                    "<em>Clinical Infectious Diseases, 52</em>(9), e162&ndash;e193. " + _doi("10.1093/cid/cir257")),
    "mccarthy2016": ("McCarthy, C. J., Behravesh, S., Naidu, S. G., &amp; Oklu, R. (2016). Air embolism: Practical tips for prevention and treatment. "
                     "<em>Journal of Clinical Medicine, 5</em>(11), Article 93. " + _doi("10.3390/jcm5110093")),
    "goossens2015": ("Goossens, G. A. (2015). Flushing and locking of venous catheters: Available evidence and evidence deficit. "
                     "<em>Nursing Research and Practice, 2015</em>, Article 985686. " + _doi("10.1155/2015/985686")),
    "agarwal2013": ("Agarwal, A. K. (2013). Central vein stenosis. <em>American Journal of Kidney Diseases, 61</em>(6), 1001&ndash;1015. "
                    + _doi("10.1053/j.ajkd.2012.10.024")),
}
