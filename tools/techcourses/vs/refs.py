# -*- coding: utf-8 -*-
"""References for the Vascular Surgeon track (APA 7), keyed vs_<short>.
Journal entries built from PubMed metadata retrieved November 25, 2026. Policy and web sources were checked the same day.
The Philippine keys an01_1 (PSN 2024 HD guidelines), an01_2 (DOH AO 2012-0001) and an01_6 (PhilHealth PC 2024-0023)
are shared with the Attending Nephrologist track and are reused, not redefined."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


def _url(u):
    return f'<a href="{u}">{u}</a>'


def _ret(u):
    return "Retrieved November 25, 2026, from " + _url(u)


REFS = {
    # ── guidelines and reviews ──
    "vs_kdoqi": ("Lok, C. E., Huber, T. S., Lee, T., Shenoy, S., Yevzlin, A. S., Abreo, K., Allon, M., Asif, A., Astor, B. C., "
                 "Glickman, M. H., Graham, J., Moist, L. M., Rajan, D. K., Roberts, C., Vachharajani, T. J., Valentini, R. P., & "
                 "National Kidney Foundation. (2020). KDOQI clinical practice guideline for vascular access: 2019 update. "
                 "<em>American Journal of Kidney Diseases</em>, <em>75</em>(4 Suppl 2), S1&ndash;S164. " + _doi("10.1053/j.ajkd.2019.12.001")),
    "vs_ukka": ("Aitken, E., Anijeet, H., Ashby, D., Barrow, W., Calder, F., Dowds, B., Fielding, C., Gilbert, J., Jones, R., "
                "Karunanithy, N., Khawaja, Z., Roberts, E., Robson, M., Shroff, R., Stacey, H., Thomson, P., & Waters, D. (2025). "
                "UK Kidney Association clinical practice guideline on vascular access for haemodialysis. <em>BMC Nephrology</em>, "
                "<em>26</em>(1), 461. " + _doi("10.1186/s12882-025-04374-y")),
    "vs_esvs": ("Schmidli, J., Widmer, M. K., Basile, C., de Donato, G., Gallieni, M., Gibbons, C. P., Haage, P., Hamilton, G., "
                "Hedin, U., Kamper, L., Lazarides, M. K., Lindsey, B., Mestres, G., Pegoraro, M., Roy, J., Setacci, C., Shemesh, D., "
                "Tordoir, J. H. M., van Loon, M., . . . Roca-Tey, R. (2018). Editor&rsquo;s choice &ndash; Vascular access: 2018 clinical "
                "practice guidelines of the European Society for Vascular Surgery (ESVS). <em>European Journal of Vascular and "
                "Endovascular Surgery</em>, <em>55</em>(6), 757&ndash;818. " + _doi("10.1016/j.ejvs.2018.02.001")),
    "vs_svs2008": ("Sidawy, A. N., Spergel, L. M., Besarab, A., Allon, M., Jennings, W. C., Padberg, F. T., Murad, M. H., Montori, V. M., "
                   "O&rsquo;Hare, A. M., Calligaro, K. D., Macsata, R. A., Lumsden, A. B., Ascher, E., & Society for Vascular Surgery. (2008). "
                   "The Society for Vascular Surgery: Clinical practice guidelines for the surgical placement and maintenance of "
                   "arteriovenous hemodialysis access. <em>Journal of Vascular Surgery</em>, <em>48</em>(5 Suppl), 2S&ndash;25S. "
                   + _doi("10.1016/j.jvs.2008.08.042")),
    "vs_sidawy2002": ("Sidawy, A. N., Gray, R., Besarab, A., Henry, M., Ascher, E., Silva, M., Miller, A., Scher, L., Trerotola, S., "
                      "Gregory, R. T., Rutherford, R. B., & Kent, K. C. (2002). Recommended standards for reports dealing with arteriovenous "
                      "hemodialysis accesses. <em>Journal of Vascular Surgery</em>, <em>35</em>(3), 603&ndash;610. "
                      + _doi("10.1067/mva.2002.122025")),
    "vs_lok2024": ("Lok, C. E., Huber, T. S., Orchanian-Cheff, A., & Rajan, D. K. (2024). Arteriovenous access for hemodialysis: A review. "
                   "<em>JAMA</em>, <em>331</em>(15), 1307&ndash;1317. " + _doi("10.1001/jama.2024.0535")),
    # ── planning, choice, outcomes ──
    "vs_ravani2013": ("Ravani, P., Palmer, S. C., Oliver, M. J., Quinn, R. R., MacRae, J. M., Tai, D. J., Pannu, N. I., Thomas, C., "
                      "Hemmelgarn, B. R., Craig, J. C., Manns, B., Tonelli, M., Strippoli, G. F., & James, M. T. (2013). Associations between "
                      "hemodialysis access type and clinical outcomes: A systematic review. <em>Journal of the American Society of "
                      "Nephrology</em>, <em>24</em>(3), 465&ndash;473. " + _doi("10.1681/ASN.2012070643")),
    "vs_drew2015": ("Drew, D. A., Lok, C. E., Cohen, J. T., Wagner, M., Tangri, N., & Weiner, D. E. (2015). Vascular access choice in "
                    "incident hemodialysis patients: A decision analysis. <em>Journal of the American Society of Nephrology</em>, "
                    "<em>26</em>(1), 183&ndash;191. " + _doi("10.1681/ASN.2013111236")),
    "vs_aljaishi2014": ("Al-Jaishi, A. A., Oliver, M. J., Thomas, S. M., Lok, C. E., Zhang, J. C., Garg, A. X., Kosa, S. D., Quinn, R. R., "
                        "& Moist, L. M. (2014). Patency rates of the arteriovenous fistula for hemodialysis: A systematic review and "
                        "meta-analysis. <em>American Journal of Kidney Diseases</em>, <em>63</em>(3), 464&ndash;478. "
                        + _doi("10.1053/j.ajkd.2013.08.023")),
    "vs_kamar2019": ("Kamar, F., Quinn, R. R., Oliver, M. J., Viecelli, A. K., Hiremath, S., MacRae, J., Miller, L., Blake, P., Moist, L., "
                     "Garg, A. X., Lam, N. N., Kabani, R., Clarke, A., Liu, P., Gillespie, B., & Ravani, P. (2019). Outcomes of the first and "
                     "second hemodialysis fistula: A cohort study. <em>American Journal of Kidney Diseases</em>, <em>73</em>(1), 62&ndash;71. "
                     + _doi("10.1053/j.ajkd.2018.06.007")),
    "vs_elters2012": ("El Ters, M., Schears, G. J., Taler, S. J., Williams, A. W., Albright, R. C., Jenson, B. M., Mahon, A. L., "
                      "Stockland, A. H., Misra, S., Nyberg, S. L., Rule, A. D., & Hogan, M. C. (2012). Association between prior peripherally "
                      "inserted central catheters and lack of functioning arteriovenous fistulas: A case-control study in hemodialysis "
                      "patients. <em>American Journal of Kidney Diseases</em>, <em>60</em>(4), 601&ndash;608. " + _doi("10.1053/j.ajkd.2012.05.007")),
    "vs_saad2017": ("Saad, T. F., & Weiner, H. L. (2017). Venous hemodialysis catheters and cardiac implantable electronic devices: "
                    "Avoiding a high-risk combination. <em>Seminars in Dialysis</em>, <em>30</em>(3), 187&ndash;192. " + _doi("10.1111/sdi.12581")),
    # ── creation and maturation ──
    "vs_ferring2010": ("Ferring, M., Claridge, M., Smith, S. A., & Wilmink, T. (2010). Routine preoperative vascular ultrasound improves "
                       "patency and use of arteriovenous fistulas for hemodialysis: A randomized trial. <em>Clinical Journal of the American "
                       "Society of Nephrology</em>, <em>5</em>(12), 2236&ndash;2244. " + _doi("10.2215/CJN.02820310")),
    "vs_aitken2016": ("Aitken, E., Jackson, A., Kearns, R., Steven, M., Kinsella, J., Clancy, M., & Macfarlane, A. (2016). Effect of regional "
                      "versus local anaesthesia on outcome after arteriovenous fistula creation: A randomised controlled trial. "
                      "<em>Lancet</em>, <em>388</em>(10049), 1067&ndash;1074. " + _doi("10.1016/S0140-6736(16)30948-5")),
    "vs_robbin2002": ("Robbin, M. L., Chamberlain, N. E., Lockhart, M. E., Gallichio, M. H., Young, C. J., Deierhoi, M. H., & Allon, M. (2002). "
                      "Hemodialysis arteriovenous fistula maturity: US evaluation. <em>Radiology</em>, <em>225</em>(1), 59&ndash;64. "
                      + _doi("10.1148/radiol.2251011367")),
    "vs_huber2021": ("Huber, T. S., Berceli, S. A., Scali, S. T., Neal, D., Anderson, E. M., Allon, M., Cheung, A. K., Dember, L. M., "
                     "Himmelfarb, J., Roy-Chaudhury, P., Vazquez, M. A., Alpers, C. E., Robbin, M. L., Imrey, P. B., Beck, G. J., Farber, A. M., "
                     "Kaufman, J. S., Kraiss, L. W., Vongpatanasin, W., . . . Feldman, H. I. (2021). Arteriovenous fistula maturation, "
                     "functional patency, and intervention rates. <em>JAMA Surgery</em>, <em>156</em>(12), 1111&ndash;1118. "
                     + _doi("10.1001/jamasurg.2021.4527")),
    "vs_rayner2003": ("Rayner, H. C., Pisoni, R. L., Gillespie, B. W., Goodkin, D. A., Akiba, T., Akizawa, T., Saito, A., Young, E. W., "
                      "Port, F. K., & Dialysis Outcomes and Practice Patterns Study. (2003). Creation, cannulation and survival of "
                      "arteriovenous fistulae: Data from the Dialysis Outcomes and Practice Patterns Study. <em>Kidney International</em>, "
                      "<em>63</em>(1), 323&ndash;330. " + _doi("10.1046/j.1523-1755.2003.00724.x")),
    "vs_dember2008": ("Dember, L. M., Beck, G. J., Allon, M., Delmez, J. A., Dixon, B. S., Greenberg, A., Himmelfarb, J., Vazquez, M. A., "
                      "Gassman, J. J., Greene, T., Radeva, M. K., Braden, G. L., Ikizler, T. A., Rocco, M. V., Davidson, I. J., Kaufman, J. S., "
                      "Meyers, C. M., Kusek, J. W., Feldman, H. I., & Dialysis Access Consortium Study Group. (2008). Effect of clopidogrel on "
                      "early failure of arteriovenous fistulas for hemodialysis: A randomized controlled trial. <em>JAMA</em>, "
                      "<em>299</em>(18), 2164&ndash;2171. " + _doi("10.1001/jama.299.18.2164")),
    "vs_dixon2009": ("Dixon, B. S., Beck, G. J., Vazquez, M. A., Greenberg, A., Delmez, J. A., Allon, M., Dember, L. M., Himmelfarb, J., "
                     "Gassman, J. J., Greene, T., Radeva, M. K., Davidson, I. J., Ikizler, T. A., Braden, G. L., Fenves, A. Z., Kaufman, J. S., "
                     "Cotton, J. R., Martin, K. J., McNeil, J. W., . . . DAC Study Group. (2009). Effect of dipyridamole plus aspirin on "
                     "hemodialysis graft patency. <em>New England Journal of Medicine</em>, <em>360</em>(21), 2191&ndash;2201. "
                     + _doi("10.1056/NEJMoa0805840")),
    "vs_irish2017": ("Irish, A. B., Viecelli, A. K., Hawley, C. M., Hooi, L. S., Pascoe, E. M., Paul-Brent, P. A., Badve, S. V., Mori, T. A., "
                     "Cass, A., Kerr, P. G., Voss, D., Ong, L. M., Polkinghorne, K. R., & FAVOURED Study Collaborative Group. (2017). Effect of "
                     "fish oil supplementation and aspirin use on arteriovenous fistula failure in patients requiring hemodialysis: A "
                     "randomized clinical trial. <em>JAMA Internal Medicine</em>, <em>177</em>(2), 184&ndash;193. "
                     + _doi("10.1001/jamainternmed.2016.8029")),
    "vs_lok2017": ("Lok, C. E., Rajan, D. K., Clement, J., Kiaii, M., Sidhu, R., Thomson, K., Buldo, G., Dipchand, C., Moist, L., Sasal, J., "
                   "& NEAT Investigators. (2017). Endovascular proximal forearm arteriovenous fistula for hemodialysis access: Results of the "
                   "prospective, multicenter Novel Endovascular Access Trial (NEAT). <em>American Journal of Kidney Diseases</em>, "
                   "<em>70</em>(4), 486&ndash;497. " + _doi("10.1053/j.ajkd.2017.03.026")),
    "vs_wong2014": ("Wong, B., Muneer, M., Wiebe, N., Storie, D., Shurraw, S., Pannu, N., Klarenbach, S., Grudzinski, A., Nesrallah, G., & "
                    "Pauly, R. P. (2014). Buttonhole versus rope-ladder cannulation of arteriovenous fistulas for hemodialysis: A systematic "
                    "review. <em>American Journal of Kidney Diseases</em>, <em>64</em>(6), 918&ndash;936. " + _doi("10.1053/j.ajkd.2014.06.018")),
    "vs_muir2014": ("Muir, C. A., Kotwal, S. S., Hawley, C. M., Polkinghorne, K., Gallagher, M. P., Snelling, P., & Jardine, M. J. (2014). "
                    "Buttonhole cannulation and clinical outcomes in a home hemodialysis cohort and systematic review. <em>Clinical Journal "
                    "of the American Society of Nephrology</em>, <em>9</em>(1), 110&ndash;119. " + _doi("10.2215/CJN.03930413")),
    # ── dysfunction and rescue ──
    "vs_ravani2016": ("Ravani, P., Quinn, R. R., Oliver, M. J., Karsanji, D. J., James, M. T., MacRae, J. M., Palmer, S. C., & Strippoli, G. F. "
                      "(2016). Preemptive correction of arteriovenous access stenosis: A systematic review and meta-analysis of randomized "
                      "controlled trials. <em>American Journal of Kidney Diseases</em>, <em>67</em>(3), 446&ndash;460. "
                      + _doi("10.1053/j.ajkd.2015.11.013")),
    "vs_haskal2010": ("Haskal, Z. J., Trerotola, S., Dolmatch, B., Schuman, E., Altman, S., Mietling, S., Berman, S., McLennan, G., Trimmer, C., "
                      "Ross, J., & Vesely, T. (2010). Stent graft versus balloon angioplasty for failing dialysis-access grafts. <em>New "
                      "England Journal of Medicine</em>, <em>362</em>(6), 494&ndash;503. " + _doi("10.1056/NEJMoa0902045")),
    "vs_lookstein2020": ("Lookstein, R. A., Haruguchi, H., Ouriel, K., Weinberg, I., Lei, L., Cihlar, S., Holden, A., & IN.PACT AV Access "
                         "Investigators. (2020). Drug-coated balloons for dysfunctional dialysis arteriovenous fistulas. <em>New England "
                         "Journal of Medicine</em>, <em>383</em>(8), 733&ndash;742. " + _doi("10.1056/NEJMoa1914617")),
    "vs_katsanos2018": ("Katsanos, K., Spiliopoulos, S., Kitrou, P., Krokidis, M., & Karnabatidis, D. (2018). Risk of death following "
                        "application of paclitaxel-coated balloons and stents in the femoropopliteal artery of the leg: A systematic review "
                        "and meta-analysis of randomized controlled trials. <em>Journal of the American Heart Association</em>, <em>7</em>(24), "
                        "e011245. " + _doi("10.1161/JAHA.118.011245")),
    "vs_kuhan2013": ("Kuhan, G., Antoniou, G. A., Nikam, M., Mitra, S., Farquharson, F., Brittenden, J., & Chalmers, N. (2013). A meta-analysis "
                     "of randomized trials comparing surgery versus endovascular therapy for thrombosed arteriovenous fistulas and grafts in "
                     "hemodialysis. <em>Cardiovascular and Interventional Radiology</em>, <em>36</em>(3), 699&ndash;705. "
                     + _doi("10.1007/s00270-013-0564-8")),
    "vs_scheltinga2009": ("Scheltinga, M. R., van Hoek, F., & Bruijninckx, C. M. A. (2009). Time of onset in haemodialysis access-induced "
                          "distal ischaemia (HAIDI) is related to the access type. <em>Nephrology Dialysis Transplantation</em>, "
                          "<em>24</em>(10), 3198&ndash;3204. " + _doi("10.1093/ndt/gfp200")),
    "vs_scheltinga2012": ("Scheltinga, M. R., & Bruijninckx, C. M. A. (2012). Haemodialysis access-induced distal ischaemia (HAIDI) is caused "
                          "by loco-regional hypotension but not by steal. <em>European Journal of Vascular and Endovascular Surgery</em>, "
                          "<em>43</em>(2), 218&ndash;223. " + _doi("10.1016/j.ejvs.2011.10.018")),
    "vs_vanhoek2009": ("van Hoek, F., Scheltinga, M., Luirink, M., Pasmans, H., & Beerenhout, C. (2009). Banding of hemodialysis access to "
                       "treat hand ischemia or cardiac overload. <em>Seminars in Dialysis</em>, <em>22</em>(2), 204&ndash;208. "
                       + _doi("10.1111/j.1525-139X.2008.00537.x")),
    "vs_jose2017": ("Jose, M. D., Marshall, M. R., Read, G., Lioufas, N., Ling, J., Snelling, P., & Polkinghorne, K. R. (2017). Fatal dialysis "
                    "vascular access hemorrhage. <em>American Journal of Kidney Diseases</em>, <em>70</em>(4), 570&ndash;575. "
                    + _doi("10.1053/j.ajkd.2017.05.014")),
    "vs_gill2012": ("Gill, J. R., Storck, K., & Kelly, S. (2012). Fatal exsanguination from hemodialysis vascular access sites. <em>Forensic "
                    "Science, Medicine, and Pathology</em>, <em>8</em>(3), 259&ndash;262. " + _doi("10.1007/s12024-011-9303-0")),
    "vs_agarwal2023": ("Agarwal, A. K., Roy-Chaudhury, P., Mounts, P., Hurlburt, E., Pfaffle, A., & Poggio, E. C. (2023). Taurolidine/heparin "
                       "lock solution and catheter-related bloodstream infection in hemodialysis: A randomized, double-blind, active-control, "
                       "phase 3 study. <em>Clinical Journal of the American Society of Nephrology</em>, <em>18</em>(11), 1446&ndash;1455. "
                       + _doi("10.2215/CJN.0000000000000278")),
    "vs_patel2013": ("Patel, P. R., Yi, S. H., Booth, S., Bren, V., Downham, G., Hess, S., Kelley, K., Lincoln, M., Morrissette, K., Lindberg, C., "
                     "Jernigan, J. A., & Kallen, A. J. (2013). Bloodstream infection rates in outpatient hemodialysis facilities participating "
                     "in a collaborative prevention effort: A quality improvement report. <em>American Journal of Kidney Diseases</em>, "
                     "<em>62</em>(2), 322&ndash;330. " + _doi("10.1053/j.ajkd.2013.03.011")),
    "vs_basile2008": ("Basile, C., Lomonte, C., Vernaglione, L., Casucci, F., Antonelli, M., & Losurdo, N. (2008). The relationship between the "
                      "flow of arteriovenous fistula and cardiac output in haemodialysis patients. <em>Nephrology Dialysis Transplantation</em>, "
                      "<em>23</em>(1), 282&ndash;287. " + _doi("10.1093/ndt/gfm549")),
    # ── policy, training and web sources ──
    "vs_ph_pc2024_0029": ("Philippine Health Insurance Corporation. (2024). <em>Quality standards on maintenance hemodialysis</em> (PhilHealth "
                          "Circular No. 2024-0029). " + _url("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "vs_patacsi": ("Philippine Association of Thoracic and Cardiovascular Surgery, Inc. (n.d.). <em>List of accredited institutions</em>. "
                   + _ret("https://patacsi.org.ph/surgical-training/list-of-accredited-institutions/")),
    "vs_acgme": ("Accreditation Council for Graduate Medical Education. (2026). <em>ACGME program requirements for graduate medical education "
                 "in vascular surgery (integrated and independent)</em> (Effective July 1, 2026). "
                 + _url("https://www.acgme.org/globalassets/pfassets/programrequirements/2026-prs/451_vascularsurgeryintegratedindependent_2026.pdf")),
    "vs_abs": ("American Board of Surgery. (n.d.). <em>Vascular surgery: Training requirements</em>. "
               + _ret("https://www.absurgery.org/get-certified/vascular-surgery/training-requirements/")),
    "vs_cdc_core": ("Centers for Disease Control and Prevention. (2026). <em>Dialysis safety: Core interventions for bloodstream infection "
                    "prevention</em>. " + _url("https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/")),
    "vs_cdc_stew": ("Centers for Disease Control and Prevention. (n.d.). <em>Core elements of antibiotic stewardship for outpatient "
                    "hemodialysis facilities</em>. " + _ret("https://www.cdc.gov/antibiotic-use/media/pdfs/Core-Elements-Outpatient-Hemodialysis-508.pdf")),
    "vs_kdoqi_vait": ("National Kidney Foundation. (n.d.). <em>KDOQI vascular access implementation tools</em>. "
                      + _ret("https://www.kidney.org/professionals/kdoqi/guidelines-and-commentaries/vascular-access")),
}
