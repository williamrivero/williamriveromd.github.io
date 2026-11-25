# -*- coding: utf-8 -*-
"""References for the Renal Social Worker (SW) track (APA 7). Merged into SHARED.REFS like the other tracks.
Cite in module text as [[key]]. New keys are prefixed sw_ so nothing collides with other tracks.
Journal entries were built from PubMed metadata retrieved on November 25, 2026. Regulatory entries carry the source register
of the handoff package (references/SOURCE-REGISTER.md, checked November 25, 2026) with its retrieval limits.
Also cited from the Physician-on-Duty package (already verified there): palmer2013, watnick2005, kroenke2001,
palmer_cochrane2016, friedli2017, mehrotra2019, cukor2014, kurella2005, saran2003, alsalmi2018, chan2014, davison2015,
song2024, kopp2007, anderson2009, ra10173."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


REFS = {
    # ── peer-reviewed evidence (PubMed-verified November 25, 2026) ──
    "sw_taylor2017": ("Taylor, D. M., Fraser, S. D. S., Bradley, J. A., Bradley, C., Draper, H., Metcalfe, W., Oniscu, G. C., Tomson, C. R. V., "
                      "Ravanan, R., &amp; Roderick, P. J. (2017). A systematic review of the prevalence and associations of limited health "
                      "literacy in CKD. <em>Clinical Journal of the American Society of Nephrology, 12</em>(7), 1070&ndash;1084. "
                      + _doi("10.2215/CJN.12921216")),
    "sw_moist2008": ("Moist, L. M., Bragg-Gresham, J. L., Pisoni, R. L., Saran, R., Akiba, T., Jacobson, S. H., Fukuhara, S., Mapes, D. L., "
                     "Rayner, H. C., Saito, A., &amp; Port, F. K. (2008). Travel time to dialysis as a predictor of health-related quality of "
                     "life, adherence, and mortality: The Dialysis Outcomes and Practice Patterns Study (DOPPS). <em>American Journal of "
                     "Kidney Diseases, 51</em>(4), 641&ndash;650. " + _doi("10.1053/j.ajkd.2007.12.021")),
    "sw_gilbertson2019": ("Gilbertson, E. L., Krishnasamy, R., Foote, C., Kennard, A. L., Jardine, M. J., &amp; Gray, N. A. (2019). Burden of "
                          "care and quality of life among caregivers for adults receiving maintenance dialysis: A systematic review. "
                          "<em>American Journal of Kidney Diseases, 73</em>(3), 332&ndash;343. " + _doi("10.1053/j.ajkd.2018.09.006")),
    "sw_gillespie2026": ("Gillespie, K. M., Purtell, L., Finderup, J., Schjerning, N., &amp; Bonner, A. (2026). Interventions to reduce burden "
                         "among informal caregivers of people with chronic kidney disease: Systematic review and meta-analysis. <em>Journal "
                         "of Renal Care, 52</em>(2), e70063. " + _doi("10.1111/jorc.70063")),
    "sw_walavalkar2022": ("Walavalkar, A., Craswell, A., &amp; Gray, N. A. (2022). Experiences of caregivers of patients with conservatively "
                          "managed kidney failure: A mixed methods systematic review. <em>Canadian Journal of Kidney Health and Disease, "
                          "9</em>, 20543581221089080. " + _doi("10.1177/20543581221089080")),
    "sw_natale2019": ("Natale, P., Palmer, S. C., Ruospo, M., Saglimbene, V. M., Rabindranath, K. S., &amp; Strippoli, G. F. (2019). "
                      "Psychosocial interventions for preventing and treating depression in dialysis patients. <em>Cochrane Database of "
                      "Systematic Reviews, 12</em>(12), CD004542. " + _doi("10.1002/14651858.CD004542.pub3")),
    "sw_ok2021": ("Ok, E., &amp; Kutlu, Y. (2021). The effect of motivational interviewing on adherence to treatment and quality of life "
                  "in chronic hemodialysis patients: A randomized controlled trial. <em>Clinical Nursing Research, 30</em>(3), 322&ndash;333. "
                  + _doi("10.1177/1054773820974158")),
    "sw_yon2017": ("Yon, Y., Mikton, C. R., Gassoumis, Z. D., &amp; Wilber, K. H. (2017). Elder abuse prevalence in community settings: "
                   "A systematic review and meta-analysis. <em>The Lancet Global Health, 5</em>(2), e147&ndash;e156. "
                   + _doi("10.1016/S2214-109X(17)30006-2")),
    "sw_dazzi2014": ("Dazzi, T., Gribble, R., Wessely, S., &amp; Fear, N. T. (2014). Does asking about suicide and related behaviours "
                     "induce suicidal ideation? What is the evidence? <em>Psychological Medicine, 44</em>(16), 3361&ndash;3363. "
                     + _doi("10.1017/S0033291714001299")),
    "sw_dodd2018": ("Dodd, R., Palagyi, A., Guild, L., Jha, V., &amp; Jan, S. (2018). The impact of out-of-pocket costs on treatment "
                    "commencement and adherence in chronic kidney disease: A systematic review. <em>Health Policy and Planning, 33</em>(9), "
                    "1047&ndash;1054. " + _doi("10.1093/heapol/czy081")),
    "sw_villanueva2025": ("Villanueva, A. R., de Leon, D., Encarnacion, P. J., Cunanan, E., Estabillo, A. P., Gonzales, C. J., Kimwell, M. J., "
                          "Mallari-Catungal, M., Taneo, M. J., Tan-Lim, D. D., Perlas Tiongco, R. H., Togonon-Lea&ntilde;o, J. I., "
                          "De Lara-Valenzona, M. R., Yu, D., Cabotaje Crisostomo, A., &amp; Montilla, P. J. (2025). Cost-of-illness analysis "
                          "of chronic kidney disease (CKD) management in the Philippines. <em>Journal of Medical Economics, 28</em>(1), "
                          "494&ndash;507. " + _doi("10.1080/13696998.2025.2481766")),
    "sw_ethier2024": ("Ethier, I., Hayat, A., Pei, J., Hawley, C. M., Johnson, D. W., Francis, R. S., Wong, G., Craig, J. C., Viecelli, A. K., "
                      "Htay, H., Ng, S., Leibowitz, S., &amp; Cho, Y. (2024). Peritoneal dialysis versus haemodialysis for people commencing "
                      "dialysis. <em>Cochrane Database of Systematic Reviews, 6</em>(6), CD013800. " + _doi("10.1002/14651858.CD013800.pub2")),
    "sw_bhargava2021": ("Bhargava, V., Jasuja, S., Tang, S. C., Bhalla, A. K., Sagar, G., Jha, V., Ramachandran, R., Sahay, M., Alexander, S., "
                        "Vachharajani, T., Lydia, A., Mostafi, M., Pisharam, J. K., Jacob, C., Gunawan, A., Leong, G. B., Thwin, K. T., "
                        "Agrawal, R. K., Vareesangthip, K., Tanchanco, R., Choong, L., &amp; Herath, C. (2021). Peritoneal dialysis: Status "
                        "report in South and South East Asia. <em>Nephrology, 26</em>(11), 898&ndash;906. " + _doi("10.1111/nep.13949")),
    "sw_maldonado2015": ("Maldonado, J. R., Sher, Y., Lolak, S., Swendsen, H., Skibola, D., Neri, E., David, E. E., Sullivan, C., &amp; "
                         "Standridge, K. (2015). The Stanford Integrated Psychosocial Assessment for Transplantation: A prospective study "
                         "of medical and psychosocial outcomes. <em>Psychosomatic Medicine, 77</em>(9), 1018&ndash;1030. "
                         + _doi("10.1097/PSY.0000000000000241")),
    "sw_okeeffe2018": ("O&rsquo;Keeffe, L. M., Ramond, A., Oliver-Williams, C., Willeit, P., Paige, E., Trotter, P., Evans, J., Wadstr&ouml;m, J., "
                       "Nicholson, M., Collett, D., &amp; Di Angelantonio, E. (2018). Mid- and long-term health risks in living kidney "
                       "donors: A systematic review and meta-analysis. <em>Annals of Internal Medicine, 168</em>(4), 276&ndash;284. "
                       + _doi("10.7326/M17-1235")),
    "sw_muzaale2014": ("Muzaale, A. D., Massie, A. B., Wang, M. C., Montgomery, R. A., McBride, M. A., Wainright, J. L., &amp; Segev, D. L. "
                       "(2014). Risk of end-stage renal disease following live kidney donation. <em>JAMA, 311</em>(6), 579&ndash;586. "
                       + _doi("10.1001/jama.2013.285141")),
    "sw_sullivan2012": ("Sullivan, C., Leon, J. B., Sayre, S. S., Marbury, M., Ivers, M., Pencak, J. A., Bodziak, K. A., Hricik, D. E., "
                        "Morrison, E. J., Albert, J. M., Navaneethan, S. D., Reyes, C. M., &amp; Sehgal, A. R. (2012). Impact of navigators "
                        "on completion of steps in the kidney transplant process: A randomized, controlled trial. <em>Clinical Journal of "
                        "the American Society of Nephrology, 7</em>(10), 1639&ndash;1645. " + _doi("10.2215/CJN.11731111")),
    "sw_chadban2020": ("Chadban, S. J., Ahn, C., Axelrod, D. A., Foster, B. J., Kasiske, B. L., Kher, V., Kumar, D., Oberbauer, R., Pascual, J., "
                       "Pilmore, H. L., Rodrigue, J. R., Segev, D. L., Sheerin, N. S., Tinckam, K. J., Wong, G., &amp; Knoll, G. A. (2020). "
                       "KDIGO clinical practice guideline on the evaluation and management of candidates for kidney transplantation. "
                       "<em>Transplantation, 104</em>(4S1 Suppl 1), S11&ndash;S103. " + _doi("10.1097/TP.0000000000003136")),
    "sw_kdigo2017": ("Lentine, K. L., Kasiske, B. L., Levey, A. S., Adams, P. L., Alber&uacute;, J., Bakr, M. A., Gallon, L., Garvey, C. A., "
                     "Guleria, S., Li, P. K., Segev, D. L., Taler, S. J., Tanabe, K., Wright, L., Zeier, M. G., Cheung, M., &amp; Garg, A. X. "
                     "(2017). KDIGO clinical practice guideline on the evaluation and care of living kidney donors. <em>Transplantation, "
                     "101</em>(8S Suppl 1), S1&ndash;S109. " + _doi("10.1097/TP.0000000000001769")),
    "sw_ra10364": ("Republic Act No. 10364. (2013). <em>Expanded Anti-Trafficking in Persons Act of 2012</em>, amending Republic Act No. 9208; "
                   "further amended by Republic Act No. 11862 (2022). " + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/52337")),
    "sw_ra7170": ("Republic Act No. 7170. (1992). <em>Organ Donation Act of 1991</em>. " + _url("https://elibrary.judiciary.gov.ph//thebookshelf//showdocs/2/2912")),
    "sw_lundorff2017": ("Lundorff, M., Holmgren, H., Zachariae, R., Farver-Vestergaard, I., &amp; O&rsquo;Connor, M. (2017). Prevalence of "
                        "prolonged grief disorder in adult bereavement: A systematic review and meta-analysis. <em>Journal of Affective "
                        "Disorders, 212</em>, 138&ndash;149. " + _doi("10.1016/j.jad.2017.01.030")),
    "sw_coyne2023": ("Coyne, E., Briggs, J., Loud, F., Bristow, P., Young, H. M. L., Castle, E. M., Lightfoot, C. J., Graham-Brown, M., "
                     "Eyre, M., Ormandy, P., Sachar, A., Bevin, A., Burton, J. O., Wilkinson, T. J., Koufaki, P., Macdonald, J., Ashman, N., "
                     "&amp; Greenwood, S. A. (2023). Achieving consensus on psychosocial and physical rehabilitation management for people "
                     "living with kidney disease. <em>Clinical Kidney Journal, 16</em>(11), 2185&ndash;2193. " + _doi("10.1093/ckj/sfad116")),

    # ── Philippine law, regulation and payer rules (source register PH01–PH17) ──
    "sw_ra4373": ("Republic Act No. 4373. (1965). <em>An act to regulate the practice of social work and the operation of social work "
                  "agencies in the Philippines and for other purposes</em>. Professional Regulation Commission. "
                  + _url("https://www.prc.gov.ph/sites/default/files/Social%20Workers%20Law%20-%20RA%20No.%204373_0.PDF")),
    "sw_ra10847": ("Republic Act No. 10847. (2016). <em>An act amending Republic Act No. 4373</em> [Social work practice]. Supreme Court "
                   "E-Library. " + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/67160")),
    "sw_prc2023": ("Professional Regulatory Board for Social Workers. (2023). <em>Adoption of the Philippine Social Work Code of Ethics</em> "
                   "(Board Resolution No. 05, Series of 2023). Professional Regulation Commission. "
                   + _url("https://www.prc.gov.ph/sites/default/files/2023-05%20published%20Social%20worker.pdf")),
    "sw_doh2012": ("Department of Health. (2012). <em>Rules and regulations governing the licensure and regulation of dialysis facilities "
                   "in the Philippines</em> (Administrative Order No. 2012-0001). "
                   + _url("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/50687")),
    "sw_dohtool2015": ("Department of Health, Health Facilities and Services Regulatory Bureau. (2015). <em>Assessment tool for licensing a "
                       "dialysis clinic</em> (Revision 3, April 13, 2015) [Full text not retrieved; listing only]. "
                       + _url("https://hfsrb.doh.gov.ph/wp-content/uploads/2021/06/rev3-4132015-DOH-HDC-LTO-AT-frm-11282014.pdf")),
    "sw_psn2024": ("Philippine Society of Nephrology. (2024). <em>Hemodialysis guidelines for nephrologists</em> (3rd ed.). "
                   + _url("https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf")),
    "sw_dm2024": ("Department of Health. (2024). <em>Demographic and assessment tools for medical social workers</em> (Department "
                  "Memorandum No. 2024-0372; overview only reviewed). " + _url("https://sites.google.com/view/doh-hfdb/2024-q3-updates/dm-2024-0372")),
    "sw_phic2024hd": ("Philippine Health Insurance Corporation. (2024). <em>PhilHealth Circular No. 2024-0023</em> [Hemodialysis benefit "
                      "package]. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "sw_phic2024ts": ("Philippine Health Insurance Corporation. (2024). <em>Tamang Sagot: PhilHealth Circular No. 2024-0023</em> "
                      "[Official questions and answers]. " + _url("https://www.philhealth.gov.ph/circulars/2024/TS_PC2024-0023.pdf")),
    "sw_phic2024q": ("Philippine Health Insurance Corporation. (2024). <em>PhilHealth Circular No. 2024-0029</em> [Quality standards for "
                     "maintenance hemodialysis]. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "sw_phic2024pd": ("Philippine Health Insurance Corporation. (2024). <em>PhilHealth Circular No. 2024-0036</em> [Z Benefits for "
                      "peritoneal dialysis; full text not retrieved]. " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0036.pdf")),
    "sw_phic2025pdnews": ("Philippine Health Insurance Corporation. (2025, January 27). <em>Peritoneal dialysis benefit package</em> "
                          "[Official news explainer]. " + _url("https://www.philhealth.gov.ph/news/up/article/2025/news_6798250c33dae.php")),
    "sw_phic2026kt": ("Philippine Health Insurance Corporation. (2026). <em>Z Benefits Package for Kidney Transplantation (Revision 1)</em> "
                      "(PhilHealth Circular No. 2026-0019; published November 21, 2026). "
                      + _url("https://www.philhealth.gov.ph/circulars/2026/PC2026-0019.pdf")),
    "sw_dswd_aics": ("Department of Social Welfare and Development. (2023). <em>Assistance to Individuals in Crisis Situation (AICS): "
                     "Citizen&rsquo;s Charter (onsite)</em>. " + _url("https://aics.dswd.gov.ph/wp-content/uploads/2023/08/AICS-Citizens-Charter-Onsite.pdf")),
    "sw_pcso_map": ("Philippine Charity Sweepstakes Office. (n.d.). <em>Medical Access Program</em>. Retrieved November 25, 2026, from "
                    + _url("https://www.pcso.gov.ph/ProgramsAndServices/CAD/MedicalAccessProgram.aspx")),
    "sw_ra11463": ("Republic Act No. 11463. (2019). <em>Malasakit Centers Act</em>. "
                   + _url("https://issuances-library.senate.gov.ph/sites/default/files/2025-02/RA11463.pdf")),
    "sw_doh2021": ("Department of Health. (2021). <em>Guidelines on ethical organ donation and transplantation from living donors</em> "
                   "(Administrative Order No. 2021-0059; identity confirmed through official references, full text pending). "
                   + _url("https://sites.google.com/view/doh-hfdb/about/2023-activities/hfdb-q3-20230706-031")),
    "sw_nmmc": ("Northern Mindanao Medical Center. (n.d.). <em>Medical Social Work Department</em> [Department of Health hospital "
                "service description]. Retrieved November 25, 2026, from " + _url("https://nmmc.doh.gov.ph/medical-social-work-department/")),

    # ── international comparison (INT01–INT03) ──
    "sw_cfr494": ("Centers for Medicare &amp; Medicaid Services. (2025). <em>Conditions for coverage for end-stage renal disease "
                  "facilities: Personnel qualifications</em> (42 C.F.R. &sect; 494.140). U.S. Government Publishing Office. "
                  + _url("https://www.govinfo.gov/content/pkg/CFR-2025-title42-vol5/pdf/CFR-2025-title42-vol5-sec494-140.pdf")),
    "sw_nhs_job": ("East and North Hertfordshire NHS Trust. (2026). <em>Renal social worker</em> [Job specification; employer example]. "
                   + _url("https://apps.trac.jobs/job-advert/8131276?ShowJobAdvert=&amp;feedid=9002&amp;set-locale=en-gb")),
    "sw_nt_renal": ("Northern Territory Government. (n.d.). <em>Renal social worker</em> [Service description]. Retrieved November 25, 2026, "
                    "from " + _url("https://nt.gov.au/wellbeing/allied-health/kidney-and-renal-services/renal-social-worker")),
}
