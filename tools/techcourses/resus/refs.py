# -*- coding: utf-8 -*-
"""References for the Dialysis Team Resuscitation Lab (APA 7). Merged into SHARED.REFS like the other tracks.
New keys below were built from PubMed metadata retrieved on November 28, 2026. Also cited, already defined and verified in
other packages: aha2025_bls, aha2025_special, aha2025_systems, aha2025_education, erc2025_special, karnik2001, davis2008,
pun2011, pun2019, hn_lehrich2007, foley2011, montague2008, apel2014, jessen2025, mccarthy2016, greenberg2021, cheng2014,
mcgaghie2011, an06_1, doh2012, psn2024."""


def _doi(d):
    return f'<a href="https://doi.org/{d}">https://doi.org/{d}</a>'


_AHA = ("2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care. "
        "<em>Circulation, 152</em>(16_suppl_2), ")
_AAP = ("2025 American Heart Association and American Academy of Pediatrics guidelines for cardiopulmonary resuscitation and "
        "emergency cardiovascular care. <em>Circulation, 152</em>(16_suppl_2), ")

REFS = {
    "aha2025_als": ("Wigginton, J. G., Agarwal, S., Bartos, J. A., Coute, R. A., Drennan, I. R., Haamid, A., Kudenchuk, P. J., Link, M. S., "
                    "Panchal, A. R., Pelter, M. M., Del Rios, M., Rodriguez, A. J., Perman, S. M., Sanko, S., Kotini-Shah, P., &amp; Kurz, M. C. "
                    "(2025). Part 9: Adult advanced life support: " + _AHA + "S538&ndash;S577. " + _doi("10.1161/CIR.0000000000001376")),
    "aha2025_pbls": ("Joyner, B. L., Dewan, M., Bavare, A., de Caen, A., DiMaria, K., Donofrio-Odmann, J., Fosse, G., Haskell, S., Mahgoub, M., "
                     "Meckler, G., Requist, J., Schexnayder, S. M., Olech Smith, M., Werho, D., &amp; Raymond, T. T. (2025). Part 6: Pediatric "
                     "basic life support: " + _AAP + "S424&ndash;S447. " + _doi("10.1161/CIR.0000000000001370")),
    "aha2025_pals": ("Lasa, J. J., Dhillon, G. S., Duff, J. P., Hayes, J., Kamath-Rayne, B. D., Levy, A., Mahgoub, M., Morgan, R. W., "
                     "McCormick, T., Roberts, J. S., Ross, C. E., Schexnayder, S. M., Sweberg, T., Vald&eacute;s, S. O., &amp; Topjian, A. A. (2025). "
                     "Part 8: Pediatric advanced life support: " + _AAP + "S479&ndash;S537. " + _doi("10.1161/CIR.0000000000001368")),
    "aha2025_post": ("Hirsch, K. G., Amorim, E., Coppler, P. J., Drennan, I. R., Elliott, A., Gordon, A. J., Jentzer, J. C., Johnson, N. J., "
                     "Moskowitz, A., Mumma, B. E., Presciutti, A. M., Rodriguez, A. J., Yen, A. F., &amp; Rittenberger, J. C. (2025). Part 11: "
                     "Post-cardiac arrest care: " + _AHA + "S673&ndash;S718. " + _doi("10.1161/CIR.0000000000001375")),
    "aha2025_ethics": ("Elmer, J., Atkins, D. L., Daya, M. R., Del Rios, M., Fry, J. T., Henderson, C. M., Lewis-Newby, M., Madrigal, V. N., "
                       "Marco, C. A., Ornato, J. P., Paquette, E. T., Parnia, S., Rodriguez, A. J., Shapiro, J. P., Schexnayder, S. M., Weiss, E. M., "
                       "Zientek, D. M., &amp; Idris, A. H. (2025). Part 3: Ethics: " + _AHA + "S323&ndash;S352. " + _doi("10.1161/CIR.0000000000001371")),
    "farkas2020": ("Farkas, J. D., Long, B., Koyfman, A., &amp; Menson, K. (2020). BRASH syndrome: Bradycardia, renal failure, AV blockade, "
                   "shock, and hyperkalemia. <em>The Journal of Emergency Medicine, 59</em>(2), 216&ndash;223. " + _doi("10.1016/j.jemermed.2020.05.001")),
    "abelairas2024": ("Abelairas-G&oacute;mez, C., Cortegiani, A., Sawyer, T., Greif, R., Donoghue, A., &amp; International Liaison Committee on "
                      "Resuscitation (ILCOR) Education, Implementation and Teams (EIT) Task Force. (2024). Rapid cycle deliberate practice approach "
                      "on resuscitation training: A systematic review. <em>Resuscitation Plus, 18</em>, Article 100648. "
                      + _doi("10.1016/j.resplu.2024.100648")),
    "patocka2026": ("Patocka, C., Anderson, I., Brennan, E., Lacroix, L., Pandya, A., Ganshorn, H., &amp; Hall, A. K. (2026). The impact of "
                    "simulation-based spaced training for skills acquisition on learning and performance outcomes among healthcare professionals: "
                    "A systematic review. <em>Simulation in Healthcare, 21</em>(4), 241&ndash;246. " + _doi("10.1097/SIH.0000000000000898")),
}
