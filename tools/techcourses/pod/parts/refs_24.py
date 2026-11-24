# -*- coding: utf-8 -*-
"""References added for Physician on Duty, Module 24 (APA 7). Each entry was checked against PubMed metadata
on November 25, 2026. Keys already defined in the course (daugirdas2015, rayner2014) are not repeated.
raina2022 is written identically to the draft entry for Module 12 so the two merge without conflict."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


REFS = {
    "murtagh2007": ("Murtagh, F. E., Addington-Hall, J., &amp; Higginson, I. J. (2007). The prevalence of symptoms in end-stage renal disease: "
                    "A systematic review. <em>Advances in Chronic Kidney Disease, 14</em>(1), 82&ndash;99. " + _doi("10.1053/j.ackd.2006.10.001")),
    "mehrotra2023": ("Mehrotra, R., Davison, S. N., Farrington, K., Flythe, J. E., Foo, M., Madero, M., Morton, R. L., Tsukamoto, Y., Unruh, M. L., "
                     "Cheung, M., Jadoul, M., Winkelmayer, W. C., Brown, E. A., &amp; Conference Participants. (2023). Managing the symptom burden "
                     "associated with maintenance dialysis: Conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies "
                     "Conference. <em>Kidney International, 104</em>(3), 441&ndash;454. " + _doi("10.1016/j.kint.2023.05.019")),
    "rayner2017": ("Rayner, H. C., Larkina, M., Wang, M., Graham-Brown, M., van der Veer, S. N., Ecder, T., Hasegawa, T., Kleophas, W., Bieber, B. A., "
                   "Tentori, F., Robinson, B. M., &amp; Pisoni, R. L. (2017). International comparisons of prevalence, awareness, and treatment of "
                   "pruritus in people on hemodialysis. <em>Clinical Journal of the American Society of Nephrology, 12</em>(12), 2000&ndash;2007. "
                   + _doi("10.2215/CJN.03280317")),
    "fishbane2020": ("Fishbane, S., Jamal, A., Munera, C., Wen, W., Menzaghi, F., &amp; KALM-1 Trial Investigators. (2020). A phase 3 trial of "
                     "difelikefalin in hemodialysis patients with pruritus. <em>New England Journal of Medicine, 382</em>(3), 222&ndash;232. "
                     + _doi("10.1056/NEJMoa1912770")),
    "topf2022": ("Topf, J., Wooldridge, T., McCafferty, K., Sch&ouml;mig, M., Csiky, B., Zwiech, R., Wen, W., Bhaduri, S., Munera, C., Lin, R., "
                 "Jebara, A., Cirulli, J., &amp; Menzaghi, F. (2022). Efficacy of difelikefalin for the treatment of moderate to severe pruritus in "
                 "hemodialysis patients: Pooled analysis of KALM-1 and KALM-2 phase 3 studies. <em>Kidney Medicine, 4</em>(8), Article 100512. "
                 + _doi("10.1016/j.xkme.2022.100512")),
    "hercz2020": ("Hercz, D., Jiang, S. H., &amp; Webster, A. C. (2020). Interventions for itch in people with advanced chronic kidney disease. "
                  "<em>Cochrane Database of Systematic Reviews, 2020</em>(12), Article CD011393. " + _doi("10.1002/14651858.CD011393.pub2")),
    "simonsen2017": ("Simonsen, E., Komenda, P., Lerner, B., Askin, N., Bohm, C., Shaw, J., Tangri, N., &amp; Rigatto, C. (2017). Treatment of uremic "
                     "pruritus: A systematic review. <em>American Journal of Kidney Diseases, 70</em>(5), 638&ndash;655. " + _doi("10.1053/j.ajkd.2017.05.018")),
    "liu2024": ("Liu, Y., Du, Q., &amp; Jiang, Y. (2024). Prevalence of restless legs syndrome in maintenance hemodialysis patients: A systematic "
                "review and meta-analysis. <em>Sleep Medicine, 114</em>, 15&ndash;23. " + _doi("10.1016/j.sleep.2023.11.1138")),
    "sloand2004": ("Sloand, J. A., Shelly, M. A., Feigin, A., Bernstein, P., &amp; Monk, R. D. (2004). A double-blind, placebo-controlled trial of "
                   "intravenous iron dextran therapy in patients with ESRD and restless legs syndrome. <em>American Journal of Kidney Diseases, "
                   "43</em>(4), 663&ndash;670. " + _doi("10.1053/j.ajkd.2003.11.021")),
    "safarpour2023": ("Safarpour, Y., Vaziri, N. D., &amp; Jabbari, B. (2023). Restless legs syndrome in chronic kidney disease: A systematic review. "
                      "<em>Tremor and Other Hyperkinetic Movements, 13</em>, Article 10. " + _doi("10.5334/tohm.752")),
    "hargrove2021": ("Hargrove, N., El Tobgy, N., Zhou, O., Pinder, M., Plant, B., Askin, N., Bieber, L., Collister, D., Whitlock, R., Tangri, N., "
                     "&amp; Bohm, C. (2021). Effect of aerobic exercise on dialysis-related symptoms in individuals undergoing maintenance "
                     "hemodialysis: A systematic review and meta-analysis of clinical trials. <em>Clinical Journal of the American Society of "
                     "Nephrology, 16</em>(4), 560&ndash;574. " + _doi("10.2215/CJN.15080920")),
    "mehrotra2024": ("Mehrotra, R., Cukor, D., McCurry, S. M., Rue, T., Roumelioti, M. E., Heagerty, P. J., &amp; Unruh, M. (2024). Effectiveness of "
                     "existing insomnia therapies for patients undergoing hemodialysis: A randomized clinical trial. <em>Annals of Internal "
                     "Medicine, 177</em>(2), 177&ndash;188. " + _doi("10.7326/M23-1794")),
    "tobin2022": ("Tobin, D. G., Lockwood, M. B., Kimmel, P. L., Dember, L. M., Eneanya, N. D., Jhamb, M., Nolin, T. D., Becker, W. C., Fischer, M. J., "
                  "&amp; HOPE Consortium. (2022). Opioids for chronic pain management in patients with dialysis-dependent kidney failure. "
                  "<em>Nature Reviews Nephrology, 18</em>(2), 113&ndash;128. " + _doi("10.1038/s41581-021-00484-6")),
    "coluzzi2020": ("Coluzzi, F., Caputi, F. F., Billeci, D., Pastore, A. L., Candeletti, S., Rocco, M., &amp; Romualdi, P. (2020). Safe use of "
                    "opioids in chronic kidney disease and hemodialysis patients: Tips and tricks for non-pain specialists. <em>Therapeutics and "
                    "Clinical Risk Management, 16</em>, 821&ndash;837. " + _doi("10.2147/TCRM.S262843")),
    "dember2025": ("Dember, L. M., Hsu, J. Y., Mehrotra, R., Cavanaugh, K. L., Kalim, S., Charytan, D. M., Fischer, M. J., Jhamb, M., Johansen, K. L., "
                   "Becker, W. C., Pellegrino, B., Eneanya, N. D., Schrauben, S. J., Pun, P. H., Unruh, M. L., Morasco, B. J., Mehta, M., "
                   "Miyawaki, N., Penfield, J., . . . HOPE Consortium. (2025). Pain coping skills training for patients receiving hemodialysis: "
                   "The HOPE Consortium randomized clinical trial. <em>JAMA Internal Medicine, 185</em>(2), 197&ndash;207. "
                   + _doi("10.1001/jamainternmed.2024.7140")),
    "ju2018": ("Ju, A., Unruh, M., Davison, S., Dapueto, J., Dew, M. A., Fluck, R., Germain, M., Jassal, S. V., Obrador, G., O&rsquo;Donoghue, D., "
               "Josephson, M. A., Craig, J. C., Viecelli, A., O&rsquo;Lone, E., Hanson, C. S., Manns, B., Sautenet, B., Howell, M., Reddy, B., "
               ". . . SONG-HD Fatigue Workshop Collaborators. (2018). Establishing a core outcome measure for fatigue in patients on "
               "hemodialysis: A Standardized Outcomes in Nephrology&ndash;Hemodialysis (SONG-HD) consensus workshop report. <em>American "
               "Journal of Kidney Diseases, 72</em>(1), 104&ndash;112. " + _doi("10.1053/j.ajkd.2017.12.018")),
    "davison2006": ("Davison, S. N., Jhangri, G. S., &amp; Johnson, J. A. (2006). Longitudinal validation of a modified Edmonton symptom assessment "
                    "system (ESAS) in haemodialysis patients. <em>Nephrology Dialysis Transplantation, 21</em>(11), 3189&ndash;3195. "
                    + _doi("10.1093/ndt/gfl380")),
    "weisbord2004": ("Weisbord, S. D., Fried, L. F., Arnold, R. M., Rotondi, A. J., Fine, M. J., Levenson, D. J., &amp; Switzer, G. E. (2004). "
                     "Development of a symptom assessment instrument for chronic hemodialysis patients: The Dialysis Symptom Index. "
                     "<em>Journal of Pain and Symptom Management, 27</em>(3), 226&ndash;240. " + _doi("10.1016/j.jpainsymman.2003.07.004")),
    "mantilla2024": ("Mantilla-Manosalva, N., Guadarrama, S., Bedoya-Mu&ntilde;oz, L. J., Giraldo-Moreno, S., Cuellar-Valencia, L., "
                     "Iriarte-Arist&iacute;zabal, M. F., Le&oacute;n, M. X., Mendoza-Montenegro, F. A., &amp; Correa-Morales, J. E. (2024). "
                     "Pharmacological treatment for dialysis-related muscle cramps: A systematic review. <em>Seminars in Dialysis, 37</em>(6), "
                     "415&ndash;423. " + _doi("10.1111/sdi.13223")),
    "chewcharat2022": ("Chewcharat, A., Chewcharat, P., Liu, W., Cellini, J., Phipps, E. A., Melendez Young, J. A., &amp; Nigwekar, S. U. (2022). "
                       "The effect of levocarnitine supplementation on dialysis-related hypotension: A systematic review, meta-analysis, and "
                       "trial sequential analysis. <em>PLOS ONE, 17</em>(7), Article e0271307. " + _doi("10.1371/journal.pone.0271307")),
    "raina2022": ("Raina, R., Davenport, A., Warady, B., Vasistha, P., Sethi, S. K., Chakraborty, R., Khooblall, P., Agarwal, N., Vij, M., "
                  "Schaefer, F., Malhotra, K., &amp; Misra, M. (2022). Dialysis disequilibrium syndrome (DDS) in pediatric patients on dialysis: "
                  "Systematic review and clinical practice recommendations. <em>Pediatric Nephrology, 37</em>(2), 263&ndash;274. "
                  + _doi("10.1007/s00467-021-05242-1")),
}
