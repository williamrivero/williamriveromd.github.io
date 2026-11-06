/* al-amyloidosis-tools.js — renalcarematters.com
 *
 * Two patient tools for guides/al-amyloidosis-kidneys.html:
 *   A. Kidney Trend Comparator — descriptive arithmetic on two dated urine-protein
 *      results and two dated eGFR results.
 *   B. Shared Care Passport — records checklist + visit questions + blank plan lines.
 *
 * Pure functions are Node-testable (tests/al-amyloidosis-tools.cjs). A small browser
 * controller binds to the guide's #al-cmp-* and #al-pp-* elements.
 *
 * Scope (do not change without clinical review):
 *   - Never classifies hematologic, renal, or cardiac response, relapse, or progression.
 *   - Never converts a spot ratio into g/day, never converts mg/g <-> mg/mmol,
 *     never calculates eGFR from creatinine, never extrapolates or annualizes.
 *   - Never uses entered values to pick a study group, chart, risk, or prognosis.
 *   - Entered values live in memory only: no storage, URL, analytics, or network use.
 *   - Output text is built with textContent (no HTML interpolation of user input).
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.ALTools = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var LANGS = ['en', 'tl', 'ceb', 'kap'];
  var PROTEIN_UNITS = {
    'total-protein-24h': ['g/24h', 'mg/24h'],
    'upcr': ['mg/g', 'mg/mmol'],
    'uacr': ['mg/g', 'mg/mmol']
  };
  var EQUATIONS = ['ckd-epi-2021-cr', 'ckd-epi-2021-crcys', 'ckd-epi-2009-cr', 'mdrd', 'other', 'unknown'];

  /* ── Strings. EN reviewed; TL/CEB/KAP are drafts pending native-speaker review. ── */
  var S = {
    en: {
      title: 'Kidney Trend Comparison', pTitle: 'Urine protein', eTitle: 'eGFR (estimated filtration)',
      earlier: 'Earlier', later: 'Later', notCompared: 'Not compared', sameDate: 'Same-date results: values shown side by side, not a trend over time.',
      decreased: 'decreased by', increased: 'increased by', unchanged: 'did not change',
      pReported: 'Reported urine protein', eReported: 'Reported eGFR', pctUndefined: 'Percentage change is not defined because the earlier value is zero.',
      measure: { 'total-protein-24h': '24-hour urine total protein', upcr: 'Urine protein-to-creatinine ratio (UPCR)', uacr: 'Urine albumin-to-creatinine ratio (UACR)' },
      eq: { 'ckd-epi-2021-cr': 'CKD-EPI 2021 (creatinine)', 'ckd-epi-2021-crcys': 'CKD-EPI 2021 (creatinine + cystatin C)', 'ckd-epi-2009-cr': 'CKD-EPI 2009 (creatinine)', mdrd: 'MDRD', other: 'Other equation', unknown: 'Equation not stated' },
      limitShown: 'shown as a limit', normalized: 'converted to', between: 'between',
      R: {
        'p-missing': 'Enter both urine-protein results to compare them.',
        'p-measure-diff': 'These are different tests (for example UACR and UPCR). They measure different things and cannot be compared with each other.',
        'p-unit-diff': 'The two ratios use different units (mg/g and mg/mmol). This version does not convert between them; ask your team to report both in the same unit.',
        'p-limit': 'At least one result is shown as a limit (for example <0.2 or >90), not an exact number, so no difference is calculated.',
        'p-collection': 'At least one 24-hour collection was incomplete or its completeness is unknown, so no change is calculated. Ask your team whether each collection was complete.',
        'p-method-diff': 'The results came from different laboratory methods, so no change is calculated.',
        'p-method-unknown': 'It is not confirmed that the same laboratory method was used. Ask your team before reading much into the difference.',
        'e-missing': 'Enter both eGFR results to compare them.',
        'e-limit': 'At least one eGFR is shown as a limit (for example >90), so no difference is calculated.',
        'e-child': 'Adult eGFR values are not interpreted for children here.',
        'e-adult-unknown': 'Confirm that the results belong to an adult before comparing eGFR.',
        'e-dialysis': 'eGFR is not a meaningful measure of kidney function during dialysis.',
        'e-dialysis-unknown': 'Confirm whether dialysis is involved before comparing eGFR.',
        'e-unstable': 'During acute illness or rapidly changing kidney function, a laboratory eGFR is not reliable for comparison.',
        'e-unstable-unknown': 'Confirm that kidney function was stable at both times before comparing eGFR.',
        'e-equation-unknown': 'The eGFR equation is not stated for at least one result, so the two numbers may not be comparable.',
        'e-equation-diff': 'The two eGFR results used different equations, so the numbers are not directly comparable.'
      },
      always: 'This is a numerical comparison, not a treatment-response classification. Your team must interpret urine findings and filtration together.',
      variation: 'Small differences can reflect normal laboratory and day-to-day variation.',
      discord: 'The urine-protein value fell, but the eGFR also fell. Bring both reports to your team; a lower urine-protein value alone does not establish kidney recovery.',
      E: {
        format: 'Enter a number only, using a period for decimals (for example 3.5).',
        negative: 'Values cannot be negative.',
        'date-missing': 'Add the date of this result.',
        'date-invalid': 'This is not a valid date.',
        'date-future': 'This date is in the future.',
        'date-order': 'The later result must be dated after the earlier one.',
        'unit-mismatch': 'This unit does not match the selected test.',
        'egfr-zero': 'eGFR must be more than zero. If you are on dialysis, choose that option below.',
        'value-missing': 'Enter the value for this date, or clear the date.'
      },
      errHead: 'Please check the following:', stale: 'Your entries changed. Press "Compare" again.', done: 'Comparison ready.',
      copied: 'Copied.', copyFail: 'Copy did not work. Select the text below and copy it.', cleared: 'Entries cleared.',
      ppTitle: 'Shared Care Passport', ppGather: 'Records to gather', ppHave: 'Records you have', ppQuestions: 'Questions for your team', ppPlan: "Your team's plan (to be filled in by your clinician)",
      ppNoGather: 'You marked every record as available. Bring them to your visit.',
      ppScope: 'This passport organizes records and questions. It has not notified any clinician or arranged care, and it does not recommend tests.',
      ppNoQuestions: 'No questions selected. You can add your own on the printed copy.',
      rec: { typing: 'Report confirming amyloid and its type (biopsy and typing)', hematology: 'Latest hematology summary (light-chain results and treatment)', kidney: 'Kidney results with dates (urine protein and eGFR)', cardiac: 'Heart assessment (heart blood tests or imaging)', meds: 'Current medicine list, including nonprescription and herbal products', plan: 'Written plan for fever, illness, or reduced urine, with a contact' },
      status: { yes: 'have it', no: 'do not have it', unknown: 'not sure', 'not-requested': 'not requested' },
      autoQ: { typing: 'Can I have a copy of the report that confirmed the amyloid type?', hematology: 'Can I have a written summary of my light-chain results and treatment?', kidney: 'Can I have my urine-protein and eGFR results with their dates?', cardiac: 'Has my heart been assessed, or should it be?', meds: 'Can we review my full medicine list together?', plan: 'Who do I contact for fever, illness, or much less urine, and what should I do first?' },
      Q: {
        q1: 'Which blood response have I reached, and when will it be checked next?',
        q2: 'Which urine test will follow my kidneys, and will it always be the same test?',
        q3: 'Is my eGFR stable enough to compare over time, and how is it changing?',
        q4: 'Does my heart assessment change my fluid or blood-pressure plan?',
        q5: 'What should I do about swelling: salt, fluids, and water pills?',
        q6: 'Which medicines should I avoid or check with you first?',
        q7: 'Who coordinates my care between hematology, nephrology, and cardiology?',
        q8: 'If my kidneys fail, what are my dialysis or transplant options, and how does that affect blood treatment?'
      },
      planLines: ['Urine test we will use', 'Next assessment', 'Fluid and medicine advice', 'Fever or illness: whom to contact', 'Coordinating service'],
      ppDone: 'Passport ready.'
    },
    tl: {
      title: 'Paghahambing ng Takbo ng Bato', pTitle: 'Protina sa ihi', eTitle: 'eGFR (tinatayang pagsala)',
      earlier: 'Mas nauna', later: 'Mas huli', notCompared: 'Hindi inihambing', sameDate: 'Parehong petsa: magkatabi ang mga halaga, hindi ito takbo sa paglipas ng panahon.',
      decreased: 'bumaba nang', increased: 'tumaas nang', unchanged: 'hindi nagbago',
      pReported: 'Iniulat na protina sa ihi', eReported: 'Iniulat na eGFR', pctUndefined: 'Hindi matukoy ang porsyentong pagbabago dahil zero ang mas naunang halaga.',
      measure: { 'total-protein-24h': '24-oras na kabuuang protina sa ihi', upcr: 'Urine protein-to-creatinine ratio (UPCR)', uacr: 'Urine albumin-to-creatinine ratio (UACR)' },
      eq: { 'ckd-epi-2021-cr': 'CKD-EPI 2021 (creatinine)', 'ckd-epi-2021-crcys': 'CKD-EPI 2021 (creatinine + cystatin C)', 'ckd-epi-2009-cr': 'CKD-EPI 2009 (creatinine)', mdrd: 'MDRD', other: 'Ibang equation', unknown: 'Hindi nakasaad ang equation' },
      limitShown: 'nakasulat bilang hangganan', normalized: 'na-convert sa', between: 'sa pagitan ng',
      R: {
        'p-missing': 'Ilagay ang dalawang resulta ng protina sa ihi para maihambing.',
        'p-measure-diff': 'Magkaibang test ito (halimbawa UACR at UPCR). Magkaiba ang sinusukat nila kaya hindi maihahambing sa isa\'t isa.',
        'p-unit-diff': 'Magkaiba ang unit ng dalawang ratio (mg/g at mg/mmol). Hindi ito kino-convert ng bersyong ito; hilingin sa inyong team na iisang unit ang gamitin.',
        'p-limit': 'May resultang nakasulat bilang hangganan (halimbawa <0.2 o >90), hindi eksaktong numero, kaya walang kinukuwentang pagkakaiba.',
        'p-collection': 'May 24-oras na koleksyon na kulang o hindi alam kung kumpleto, kaya walang kinukuwentang pagbabago. Itanong sa inyong team kung kumpleto ang bawat koleksyon.',
        'p-method-diff': 'Galing sa magkaibang paraan ng laboratoryo ang mga resulta, kaya walang kinukuwentang pagbabago.',
        'p-method-unknown': 'Hindi tiyak kung iisang paraan ng laboratoryo ang ginamit. Itanong muna sa inyong team bago bigyan ng malaking kahulugan ang pagkakaiba.',
        'e-missing': 'Ilagay ang dalawang resulta ng eGFR para maihambing.',
        'e-limit': 'May eGFR na nakasulat bilang hangganan (halimbawa >90), kaya walang kinukuwentang pagkakaiba.',
        'e-child': 'Hindi binibigyang-kahulugan dito ang pang-adultong eGFR para sa mga bata.',
        'e-adult-unknown': 'Tiyakin muna na sa isang adulto ang mga resulta bago ihambing ang eGFR.',
        'e-dialysis': 'Hindi makabuluhang sukatan ng paggana ng bato ang eGFR habang nagda-dialysis.',
        'e-dialysis-unknown': 'Tiyakin muna kung may dialysis bago ihambing ang eGFR.',
        'e-unstable': 'Habang may biglaang sakit o mabilis na nagbabago ang paggana ng bato, hindi maaasahan ang eGFR sa paghahambing.',
        'e-unstable-unknown': 'Tiyakin muna na matatag ang paggana ng bato sa dalawang petsa bago ihambing ang eGFR.',
        'e-equation-unknown': 'Hindi nakasaad ang equation ng eGFR sa kahit isang resulta, kaya maaaring hindi maihahambing ang dalawang numero.',
        'e-equation-diff': 'Magkaibang equation ang ginamit sa dalawang eGFR, kaya hindi direktang maihahambing ang mga numero.'
      },
      always: 'Isa itong paghahambing ng numero, hindi pag-uuri ng tugon sa gamutan. Kailangang basahin ng inyong team nang magkasama ang resulta ng ihi at ang pagsala.',
      variation: 'Maaaring dulot ng normal na pagbabago sa laboratoryo at araw-araw ang maliliit na pagkakaiba.',
      discord: 'Bumaba ang protina sa ihi, pero bumaba rin ang eGFR. Dalhin ang dalawang ulat sa inyong team; hindi sapat ang mas mababang protina sa ihi para sabihing gumagaling ang bato.',
      E: {
        format: 'Numero lamang, gumamit ng tuldok para sa decimal (halimbawa 3.5).',
        negative: 'Hindi puwedeng negatibo ang halaga.',
        'date-missing': 'Ilagay ang petsa ng resultang ito.',
        'date-invalid': 'Hindi ito wastong petsa.',
        'date-future': 'Nasa hinaharap ang petsang ito.',
        'date-order': 'Dapat mas huli ang petsa ng mas huling resulta kaysa sa mas nauna.',
        'unit-mismatch': 'Hindi tugma ang unit na ito sa napiling test.',
        'egfr-zero': 'Dapat higit sa zero ang eGFR. Kung nagda-dialysis, piliin ang opsyong iyon sa ibaba.',
        'value-missing': 'Ilagay ang halaga para sa petsang ito, o burahin ang petsa.'
      },
      errHead: 'Pakisuri ang mga sumusunod:', stale: 'Nagbago ang mga inilagay mo. Pindutin muli ang "Ihambing".', done: 'Handa na ang paghahambing.',
      copied: 'Nakopya na.', copyFail: 'Hindi gumana ang pagkopya. Piliin ang teksto sa ibaba at kopyahin.', cleared: 'Nabura na ang mga inilagay.',
      ppTitle: 'Shared Care Passport', ppGather: 'Mga record na kailangang kunin', ppHave: 'Mga record na mayroon ka', ppQuestions: 'Mga tanong para sa inyong team', ppPlan: 'Plano ng inyong team (pupunan ng inyong doktor)',
      ppNoGather: 'Minarkahan mong mayroon ka ng lahat ng record. Dalhin ang mga ito sa iyong pagbisita.',
      ppScope: 'Inaayos ng passport na ito ang mga record at tanong. Wala itong inabisuhang doktor o inayos na pangangalaga, at hindi ito nagrerekomenda ng test.',
      ppNoQuestions: 'Walang napiling tanong. Maaari kang magdagdag ng sarili mong tanong sa naka-print na kopya.',
      rec: { typing: 'Ulat na nagkukumpirma ng amyloid at ng uri nito (biopsy at typing)', hematology: 'Pinakahuling buod mula sa hematology (resulta ng light chain at gamutan)', kidney: 'Resulta ng bato na may petsa (protina sa ihi at eGFR)', cardiac: 'Pagsusuri sa puso (blood test o imaging ng puso)', meds: 'Kasalukuyang listahan ng gamot, kasama ang nabibili nang walang reseta at herbal', plan: 'Nakasulat na plano para sa lagnat, sakit, o pagkonti ng ihi, na may contact' },
      status: { yes: 'mayroon', no: 'wala', unknown: 'hindi sigurado', 'not-requested': 'hindi hiniling' },
      autoQ: { typing: 'Maaari ba akong makakuha ng kopya ng ulat na nagkumpirma ng uri ng amyloid?', hematology: 'Maaari ba akong makakuha ng nakasulat na buod ng aking resulta ng light chain at gamutan?', kidney: 'Maaari ko bang makuha ang aking resulta ng protina sa ihi at eGFR kasama ang mga petsa?', cardiac: 'Nasuri na ba ang aking puso, o dapat ba itong suriin?', meds: 'Maaari ba nating suriin nang magkasama ang buong listahan ng aking gamot?', plan: 'Sino ang aking kokontakin kapag may lagnat, sakit, o sobrang konti ng ihi, at ano ang una kong gagawin?' },
      Q: {
        q1: 'Anong tugon ng dugo ang naabot ko na, at kailan ito susuriin muli?',
        q2: 'Anong test ng ihi ang susubaybay sa aking bato, at palagi bang iisang test ito?',
        q3: 'Matatag ba ang aking eGFR para maihambing sa paglipas ng panahon, at paano ito nagbabago?',
        q4: 'Binabago ba ng pagsusuri sa aking puso ang plano ko sa likido o presyon ng dugo?',
        q5: 'Ano ang dapat kong gawin sa pamamaga: asin, likido, at pampaihi?',
        q6: 'Aling mga gamot ang dapat kong iwasan o itanong muna sa inyo?',
        q7: 'Sino ang nag-uugnay ng aking pangangalaga sa hematology, nephrology, at cardiology?',
        q8: 'Kung humina nang tuluyan ang aking bato, ano ang mga opsyon ko sa dialysis o transplant, at paano ito makaaapekto sa gamutan sa dugo?'
      },
      planLines: ['Test ng ihi na gagamitin', 'Susunod na pagsusuri', 'Payo sa likido at gamot', 'Lagnat o sakit: sino ang kokontakin', 'Serbisyong nag-uugnay'],
      ppDone: 'Handa na ang passport.'
    },
    ceb: {
      title: 'Pagtandi sa Dagan sa Bato', pTitle: 'Protina sa ihi', eTitle: 'eGFR (gibanabana nga pagsala)',
      earlier: 'Nauna', later: 'Ulahi', notCompared: 'Wala gitandi', sameDate: 'Parehas nga petsa: magkatupad ang mga numero, dili kini dagan sa paglabay sa panahon.',
      decreased: 'mikunhod og', increased: 'misaka og', unchanged: 'wala nausab',
      pReported: 'Gitaho nga protina sa ihi', eReported: 'Gitaho nga eGFR', pctUndefined: 'Dili matino ang porsyento nga kausaban kay zero ang nauna nga numero.',
      measure: { 'total-protein-24h': '24-oras nga kinatibuk-ang protina sa ihi', upcr: 'Urine protein-to-creatinine ratio (UPCR)', uacr: 'Urine albumin-to-creatinine ratio (UACR)' },
      eq: { 'ckd-epi-2021-cr': 'CKD-EPI 2021 (creatinine)', 'ckd-epi-2021-crcys': 'CKD-EPI 2021 (creatinine + cystatin C)', 'ckd-epi-2009-cr': 'CKD-EPI 2009 (creatinine)', mdrd: 'MDRD', other: 'Laing equation', unknown: 'Wala gisulti ang equation' },
      limitShown: 'gisulat isip utlanan', normalized: 'gi-convert ngadto sa', between: 'tali sa',
      R: {
        'p-missing': 'Isulod ang duha ka resulta sa protina sa ihi aron matandi.',
        'p-measure-diff': 'Lahi kini nga mga test (pananglitan UACR ug UPCR). Lahi ang ilang gisukod busa dili sila matandi sa usag usa.',
        'p-unit-diff': 'Lahi ang unit sa duha ka ratio (mg/g ug mg/mmol). Dili kini gi-convert niini nga bersyon; hangyoa ang inyong team nga usa ra ka unit ang gamiton.',
        'p-limit': 'Adunay resulta nga gisulat isip utlanan (pananglitan <0.2 o >90), dili eksakto nga numero, busa walay gikuwenta nga kalainan.',
        'p-collection': 'Adunay 24-oras nga koleksyon nga kulang o wala mahibaw-i kung kompleto, busa walay gikuwenta nga kausaban. Pangutan-a ang inyong team kung kompleto ang matag koleksyon.',
        'p-method-diff': 'Gikan sa lahi nga pamaagi sa laboratoryo ang mga resulta, busa walay gikuwenta nga kausaban.',
        'p-method-unknown': 'Wala makumpirma nga parehas nga pamaagi sa laboratoryo ang gigamit. Pangutan-a una ang inyong team sa dili pa hatagan og dakong kahulugan ang kalainan.',
        'e-missing': 'Isulod ang duha ka resulta sa eGFR aron matandi.',
        'e-limit': 'Adunay eGFR nga gisulat isip utlanan (pananglitan >90), busa walay gikuwenta nga kalainan.',
        'e-child': 'Dili dinhi gihubad ang pang-hamtong nga eGFR alang sa mga bata.',
        'e-adult-unknown': 'Kumpirmaha una nga sa hamtong ang mga resulta sa dili pa itandi ang eGFR.',
        'e-dialysis': 'Dili makahuluganong sukod sa paglihok sa bato ang eGFR samtang nag-dialysis.',
        'e-dialysis-unknown': 'Kumpirmaha una kung adunay dialysis sa dili pa itandi ang eGFR.',
        'e-unstable': 'Samtang adunay kalit nga sakit o paspas nga nausab ang paglihok sa bato, dili kasaligan ang eGFR sa pagtandi.',
        'e-unstable-unknown': 'Kumpirmaha una nga lig-on ang paglihok sa bato sa duha ka petsa sa dili pa itandi ang eGFR.',
        'e-equation-unknown': 'Wala gisulti ang equation sa eGFR sa bisan usa ka resulta, busa basin dili matandi ang duha ka numero.',
        'e-equation-diff': 'Lahi nga equation ang gigamit sa duha ka eGFR, busa dili direkta nga matandi ang mga numero.'
      },
      always: 'Kini usa ka pagtandi sa numero, dili pagklasipikar sa tubag sa pagtambal. Kinahanglang basahon sa inyong team nga dungan ang resulta sa ihi ug ang pagsala.',
      variation: 'Ang gagmay nga kalainan mahimong tungod sa normal nga kausaban sa laboratoryo ug adlaw-adlaw.',
      discord: 'Mikunhod ang protina sa ihi, apan mikunhod usab ang eGFR. Dad-a ang duha ka report sa inyong team; dili igo ang mas ubos nga protina sa ihi aron ingnon nga naayo na ang bato.',
      E: {
        format: 'Numero lang, gamita ang tuldok alang sa decimal (pananglitan 3.5).',
        negative: 'Dili mahimong negatibo ang numero.',
        'date-missing': 'Isulod ang petsa niini nga resulta.',
        'date-invalid': 'Dili kini husto nga petsa.',
        'date-future': 'Anaa sa umaabot kini nga petsa.',
        'date-order': 'Kinahanglan mas ulahi ang petsa sa ulahi nga resulta kaysa sa nauna.',
        'unit-mismatch': 'Dili mohaum kini nga unit sa gipili nga test.',
        'egfr-zero': 'Kinahanglan labaw sa zero ang eGFR. Kung nag-dialysis, pilia kana nga opsyon sa ubos.',
        'value-missing': 'Isulod ang numero alang niini nga petsa, o papasa ang petsa.'
      },
      errHead: 'Palihug susiha ang mosunod:', stale: 'Nausab ang imong gisulod. Pindota pag-usab ang "Itandi".', done: 'Andam na ang pagtandi.',
      copied: 'Nakopya na.', copyFail: 'Wala molihok ang pagkopya. Pilia ang teksto sa ubos ug kopyaha.', cleared: 'Napapas na ang gisulod.',
      ppTitle: 'Shared Care Passport', ppGather: 'Mga record nga kinahanglan kuhaon', ppHave: 'Mga record nga anaa kanimo', ppQuestions: 'Mga pangutana alang sa inyong team', ppPlan: 'Plano sa inyong team (pun-an sa inyong doktor)',
      ppNoGather: 'Gimarkahan nimo nga anaa kanimo ang tanang record. Dad-a kini sa imong pagbisita.',
      ppScope: 'Gihan-ay niini nga passport ang mga record ug pangutana. Wala kini nagpahibalo sa bisan unsang doktor o naghikay og pag-atiman, ug wala kini nagrekomenda og test.',
      ppNoQuestions: 'Walay gipili nga pangutana. Mahimo kang magdugang og kaugalingong pangutana sa na-print nga kopya.',
      rec: { typing: 'Report nga nagkumpirma sa amyloid ug sa matang niini (biopsy ug typing)', hematology: 'Pinakaulahi nga sumaryo gikan sa hematology (resulta sa light chain ug pagtambal)', kidney: 'Resulta sa bato nga adunay petsa (protina sa ihi ug eGFR)', cardiac: 'Pagsusi sa kasingkasing (blood test o imaging sa kasingkasing)', meds: 'Karon nga lista sa tambal, apil ang dili kinahanglan og reseta ug herbal', plan: 'Sinulat nga plano alang sa hilanat, sakit, o pagkagamay sa ihi, nga adunay contact' },
      status: { yes: 'naa', no: 'wala', unknown: 'dili sigurado', 'not-requested': 'wala gihangyo' },
      autoQ: { typing: 'Makakuha ba ko og kopya sa report nga nagkumpirma sa matang sa amyloid?', hematology: 'Makakuha ba ko og sinulat nga sumaryo sa akong resulta sa light chain ug pagtambal?', kidney: 'Makuha ba nako ang akong resulta sa protina sa ihi ug eGFR uban sa mga petsa?', cardiac: 'Nasusi na ba ang akong kasingkasing, o angay ba kini susihon?', meds: 'Mahimo ba natong susihon nga dungan ang tibuok lista sa akong tambal?', plan: 'Kinsa ang akong kontakon kung adunay hilanat, sakit, o diyutay kaayo nga ihi, ug unsa ang una nakong buhaton?' },
      Q: {
        q1: 'Unsang tubag sa dugo ang akong naabot, ug kanus-a kini susihon pag-usab?',
        q2: 'Unsang test sa ihi ang mosubay sa akong bato, ug kanunay ba nga parehas nga test?',
        q3: 'Lig-on ba ang akong eGFR aron matandi sa paglabay sa panahon, ug giunsa kini pag-usab?',
        q4: 'Mausab ba tungod sa pagsusi sa akong kasingkasing ang akong plano sa likido o presyon sa dugo?',
        q5: 'Unsa ang akong buhaton sa panghubag: asin, likido, ug pampaihi?',
        q6: 'Unsang mga tambal ang angay nakong likayan o unang ipangutana kaninyo?',
        q7: 'Kinsa ang nagdumala sa akong pag-atiman tali sa hematology, nephrology, ug cardiology?',
        q8: 'Kung mapakyas ang akong bato, unsa ang akong mga opsyon sa dialysis o transplant, ug unsaon niini pag-apektar sa pagtambal sa dugo?'
      },
      planLines: ['Test sa ihi nga gamiton', 'Sunod nga pagsusi', 'Tambag sa likido ug tambal', 'Hilanat o sakit: kinsa ang kontakon', 'Serbisyo nga nagdumala'],
      ppDone: 'Andam na ang passport.'
    },
    kap: {
      title: 'Pamikumpara king Takbu ning Batu', pTitle: 'Protina king ihi', eTitle: 'eGFR (tinantyang pamanala)',
      earlier: 'Mas mumuna', later: 'Mas tauli', notCompared: 'E pikumpara', sameDate: 'Pareung petsa: magtabi la reng numeru, ali ya takbu king paglabas ning panaun.',
      decreased: 'mibaba ning', increased: 'mitas ning', unchanged: 'e mibayu',
      pReported: 'Iniulat a protina king ihi', eReported: 'Iniulat a eGFR', pctUndefined: 'E matukoy ing porsyentung pamagbayu uli ta zero ing mas mumunang numeru.',
      measure: { 'total-protein-24h': '24-oras a kabuuang protina king ihi', upcr: 'Urine protein-to-creatinine ratio (UPCR)', uacr: 'Urine albumin-to-creatinine ratio (UACR)' },
      eq: { 'ckd-epi-2021-cr': 'CKD-EPI 2021 (creatinine)', 'ckd-epi-2021-crcys': 'CKD-EPI 2021 (creatinine + cystatin C)', 'ckd-epi-2009-cr': 'CKD-EPI 2009 (creatinine)', mdrd: 'MDRD', other: 'Aliwang equation', unknown: 'E makasulat ing equation' },
      limitShown: 'makasulat bilang angganan', normalized: 'me-convert king', between: 'king pagitan ning',
      R: {
        'p-missing': 'Ilagay ing adwang resulta ning protina king ihi ban apikumpara.',
        'p-measure-diff': 'Miyayaliwang test la reti (alimbawa UACR at UPCR). Miyayaliwa ing susukatan da kaya e la apikumpara king metung at metung.',
        'p-unit-diff': 'Miyayaliwa ing unit ning adwang ratio (mg/g at mg/mmol). E la kino-convert ning bersyun a iti; pakisabyan ing team yu a metung a mu unit ing gamitan.',
        'p-limit': 'Atin resultang makasulat bilang angganan (alimbawa <0.2 o >90), ali eksaktung numeru, kaya alang kukuwentang pamiyaliwa.',
        'p-collection': 'Atin 24-oras a koleksyun a kulang o e balu nung kumpletu, kaya alang kukuwentang pamagbayu. Kutnan ing team yu nung kumpletu ing balang koleksyun.',
        'p-method-diff': 'Manibat king miyayaliwang paralan ning laboratoryu deng resulta, kaya alang kukuwentang pamagbayu.',
        'p-method-unknown': 'E siguradu nung metung a mu paralan ning laboratoryu ing ginamit. Kutnan ye pamu ing team yu bayu mu bigyan maragul a kabaldugan ing pamiyaliwa.',
        'e-missing': 'Ilagay ing adwang resulta ning eGFR ban apikumpara.',
        'e-limit': 'Atin eGFR a makasulat bilang angganan (alimbawa >90), kaya alang kukuwentang pamiyaliwa.',
        'e-child': 'E la bibigyan kabaldugan keni deng eGFR para king matwa para kareng anak.',
        'e-adult-unknown': 'Siguraduan mu pamu a king matwang tau la deng resulta bayu mu ikumpara ing eGFR.',
        'e-dialysis': 'Ali ya makabaldugan a sukat ning pamagobra ning batu ing eGFR kabang magdialysis.',
        'e-dialysis-unknown': 'Siguraduan mu pamu nung atin dialysis bayu mu ikumpara ing eGFR.',
        'e-unstable': 'Kabang atin biglang sakit o mabilis a mibabayu ing pamagobra ning batu, e maaasan ing eGFR king pamikumpara.',
        'e-unstable-unknown': 'Siguraduan mu pamu a matatag ing pamagobra ning batu king adwang petsa bayu mu ikumpara ing eGFR.',
        'e-equation-unknown': 'E makasulat ing equation ning eGFR king agyang metung a resulta, kaya malyaring e la apikumpara deng adwang numeru.',
        'e-equation-diff': 'Miyayaliwang equation ing ginamit king adwang eGFR, kaya e la direktang apikumpara deng numeru.'
      },
      always: 'Iti metung a pamikumpara ning numeru, ali ya pamag-uri ning tugon king pamanulu. Kailangan dang basan ning team yu a magkayabe ing resulta ning ihi at ing pamanala.',
      variation: 'Deng malating pamiyaliwa malyaring uli ning normal a pamagbayu king laboratoryu at aldo-aldo.',
      discord: 'Mibaba ing protina king ihi, pero mibaba mu naman ing eGFR. Darwan yu ing adwang report king team yu; e sapat ing mas mababang protina king ihi ban sabyan a mumayap ne ing batu.',
      E: {
        format: 'Numeru mu pamu, gamitan ing tuldok para king decimal (alimbawa 3.5).',
        negative: 'E malyaring negatibu ing numeru.',
        'date-missing': 'Ilagay ing petsa ning resulta a iti.',
        'date-invalid': 'Ali ya tamang petsa iti.',
        'date-future': 'Atyu ya king darating ing petsa a iti.',
        'date-order': 'Dapat mas tauli ing petsa ning mas tauling resulta kesa king mas mumuna.',
        'unit-mismatch': 'E tugma ing unit a iti king pinili mung test.',
        'egfr-zero': 'Dapat lagpas king zero ing eGFR. Nung magdialysis ka, pilian me ing opsyun a ita king lalam.',
        'value-missing': 'Ilagay ing numeru para king petsa a iti, o palisan me ing petsa.'
      },
      errHead: 'Pakilawe deng makatuki:', stale: 'Mibayu la reng inilagay mu. Pindutan me pasibayu ing "Ikumpara".', done: 'Sadya ne ing pamikumpara.',
      copied: 'Mekopya ne.', copyFail: 'E migana ing pamangopya. Pilian me ing teksto king lalam at kopyan me.', cleared: 'Mepalis ne deng inilagay.',
      ppTitle: 'Shared Care Passport', ppGather: 'Reng record a kailangan kuanan', ppHave: 'Reng record a atyu na kekayu', ppQuestions: 'Reng kutang para king team yu', ppPlan: 'Planu ning team yu (pupunan ning doktor yu)',
      ppNoGather: 'Minarkan mu a atyu na keka ing eganagang record. Darwan mu la king pamamisita mu.',
      ppScope: 'Ayusan na ning passport a iti deng record at kutang. Alang inabisuan a doktor o inayus a pamanalaga, at ali ya magrekomenda test.',
      ppNoQuestions: 'Alang pinili a kutang. Malyari kang magdagdag sariling kutang king me-print a kopya.',
      rec: { typing: 'Report a mangumpirma king amyloid at king klasi na (biopsy at typing)', hematology: 'Pekatauling buod manibat king hematology (resulta ning light chain at pamanulu)', kidney: 'Resulta ning batu a atin petsa (protina king ihi at eGFR)', cardiac: 'Pamanigaral king pusu (blood test o imaging ning pusu)', meds: 'Kasalukuyang listaan ning gamut, kayabe deng ali kailangan reseta at herbal', plan: 'Makasulat a planu para king lagnat, sakit, o pangakakaunti ning ihi, a atin contact' },
      status: { yes: 'atin', no: 'ala', unknown: 'e siguradu', 'not-requested': 'e inaus' },
      autoQ: { typing: 'Malyari ku bang kuanan kopya ning report a mekumpirma king klasi ning amyloid?', hematology: 'Malyari ku bang kuanan makasulat a buod ning resulta ning light chain ku at pamanulu?', kidney: 'Malyari ku bang kuanan deng resulta ning protina king ihi at eGFR ku kayabe deng petsa?', cardiac: 'Linawe ne ba ing pusu ku, o dapat neng lawan?', meds: 'Malyari tang lawan a magkayabe ing buung listaan ning gamut ku?', plan: 'Ninu ing kontakan ku nung atin lagnat, sakit, o kakaunti ing ihi, at nanu ing mumuna kung gawan?' },
      Q: {
        q1: 'Nanung tugon ning daya ing asaup ku na, at kapilan ya lawan pasibayu?',
        q2: 'Nanung test ning ihi ing manubaybay king batu ku, at pane ya bang metung a mu test?',
        q3: 'Matatag ya ba ing eGFR ku ban apikumpara king paglabas ning panaun, at makananu yang mibabayu?',
        q4: 'Babaguan na ba ning pamanigaral king pusu ku ing planu ku king likidu o presyon ning daya?',
        q5: 'Nanu ing dapat kung gawan king pamagbaga: asin, likidu, at pampaihi?',
        q6: 'Nanung gamut ing dapat kung likwan o kutnan pamu kekayu?',
        q7: 'Ninu ing mangasiwa king pamanalaga kanaku king hematology, nephrology, at cardiology?',
        q8: 'Nung mabigu ing batu ku, nanu deng opsyun ku king dialysis o transplant, at makananu yang mangapekto king pamanulu king daya?'
      },
      planLines: ['Test ning ihi a gamitan', 'Susunod a pamanigaral', 'Payu king likidu at gamut', 'Lagnat o sakit: ninu ing kontakan', 'Serbisyung mangasiwa'],
      ppDone: 'Sadya ne ing passport.'
    }
  };

  function str(lang) { return S[LANGS.indexOf(lang) >= 0 ? lang : 'en']; }

  /* ── Parsing ── */
  // Strict full-string number: digits with optional single decimal part, or
  // comma-grouped thousands (6,000 / 6,000.5). Rejects "2abc", "1e3", ".5", "-1", "Infinity".
  var NUM_PLAIN = /^\d+(\.\d+)?$/;
  var NUM_GROUPED = /^\d{1,3}(,\d{3})+(\.\d+)?$/;
  var LIMIT = /^[<>≤≥]\s*\d/;

  function parseValue(raw) {
    var s = (raw === undefined || raw === null) ? '' : String(raw).trim();
    if (s === '') return { status: 'blank', raw: s };
    if (LIMIT.test(s)) return { status: 'limit', raw: s };
    if (s.charAt(0) === '-' || s.charAt(0) === '−') {
      var rest = s.slice(1).trim();
      if (NUM_PLAIN.test(rest) || NUM_GROUPED.test(rest)) return { status: 'invalid', raw: s, reason: 'negative' };
      return { status: 'invalid', raw: s, reason: 'format' };
    }
    if (!(NUM_PLAIN.test(s) || NUM_GROUPED.test(s))) return { status: 'invalid', raw: s, reason: 'format' };
    var v = Number(s.replace(/,/g, ''));
    if (!isFinite(v)) return { status: 'invalid', raw: s, reason: 'format' };
    return { status: 'ok', raw: s, value: v };
  }

  // YYYY-MM-DD local calendar date. todayIso is injectable for tests.
  function parseDate(raw, todayIso) {
    var s = (raw === undefined || raw === null) ? '' : String(raw).trim();
    if (s === '') return { status: 'blank' };
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s);
    if (!m) return { status: 'invalid', reason: 'date-invalid' };
    var y = +m[1], mo = +m[2], d = +m[3];
    var dt = new Date(Date.UTC(y, mo - 1, d));
    if (dt.getUTCFullYear() !== y || dt.getUTCMonth() !== mo - 1 || dt.getUTCDate() !== d || y < 1900) return { status: 'invalid', reason: 'date-invalid' };
    if (todayIso && s > todayIso) return { status: 'invalid', reason: 'date-future', iso: s };
    return { status: 'ok', iso: s };
  }

  function todayLocalIso() {
    var t = new Date();
    function p(n) { return (n < 10 ? '0' : '') + n; }
    return t.getFullYear() + '-' + p(t.getMonth() + 1) + '-' + p(t.getDate());
  }

  /* ── Number formatting (display only; arithmetic keeps full precision) ── */
  function fmt(x) {
    if (x === null || x === undefined || !isFinite(x)) return '';
    var a = Math.abs(x), dp = a >= 100 ? 0 : (a >= 1 ? 1 : 2);
    var s = x.toFixed(dp);
    if (/^-0(\.0+)?$/.test(s)) s = s.slice(1); // normalize negative zero
    var parts = s.split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
  }
  function fmtPct(x) {
    var s = x.toFixed(1);
    if (/^-0\.0$/.test(s)) s = '0.0';
    return s;
  }

  /* ── Validation of one series (field-level errors block the whole run) ── */
  function validatePoint(prefix, pt, todayIso, errors, kind) {
    var v = parseValue(pt.value), d = parseDate(pt.date, todayIso);
    if (v.status === 'invalid') errors.push({ field: prefix + '-value', code: v.reason });
    if (kind === 'egfr' && v.status === 'ok' && v.value === 0) errors.push({ field: prefix + '-value', code: 'egfr-zero' });
    if (d.status === 'invalid') errors.push({ field: prefix + '-date', code: d.reason });
    if (v.status !== 'blank' && d.status === 'blank') errors.push({ field: prefix + '-date', code: 'date-missing' });
    if (v.status === 'blank' && d.status === 'ok') errors.push({ field: prefix + '-value', code: 'value-missing' });
    if (kind === 'protein' && pt.measure && PROTEIN_UNITS[pt.measure] && PROTEIN_UNITS[pt.measure].indexOf(pt.unit) < 0) {
      errors.push({ field: prefix + '-unit', code: 'unit-mismatch' });
    }
    return { v: v, d: d };
  }

  function exactOf(pt, parsed) {
    // A value is exact only if parsed as a plain number AND the user did not mark it as a limit.
    return parsed.status === 'ok' && (pt.shownAs === undefined || pt.shownAs === 'exact');
  }

  function toBase(value, unit) { return unit === 'mg/24h' ? value / 1000 : value; }
  function baseUnit(measure, unit) { return measure === 'total-protein-24h' ? 'g/24h' : unit; }

  function changeOf(a, b) {
    var abs = b - a;
    var pctDefined = a > 0;
    return { abs: abs, pct: pctDefined ? 100 * (b - a) / a : null, pctDefined: pctDefined, dir: abs < 0 ? 'down' : (abs > 0 ? 'up' : 'same') };
  }

  /* ── Comparator core ── */
  function compare(input, todayIso) {
    todayIso = todayIso || todayLocalIso();
    var errors = [];
    var P = input.protein || {}, G = input.egfr || {}, C = input.context || {};
    var pA = validatePoint('al-p-a', P.earlier || {}, todayIso, errors, 'protein');
    var pB = validatePoint('al-p-b', P.later || {}, todayIso, errors, 'protein');
    var eA = validatePoint('al-e-a', G.earlier || {}, todayIso, errors, 'egfr');
    var eB = validatePoint('al-e-b', G.later || {}, todayIso, errors, 'egfr');
    if (pA.d.status === 'ok' && pB.d.status === 'ok' && pB.d.iso < pA.d.iso) errors.push({ field: 'al-p-b-date', code: 'date-order' });
    if (eA.d.status === 'ok' && eB.d.status === 'ok' && eB.d.iso < eA.d.iso) errors.push({ field: 'al-e-b-date', code: 'date-order' });
    if (errors.length) return { ok: false, errors: errors };

    var res = { ok: true, errors: [], protein: proteinSeries(P, pA, pB, C), egfr: egfrSeries(G, eA, eB, C) };
    res.discordant = !!(res.protein.computed && res.egfr.computed && !res.protein.sameDate && !res.egfr.sameDate &&
      res.protein.change.dir === 'down' && res.egfr.change.dir === 'down');
    return res;
  }

  function proteinSeries(P, pA, pB, C) {
    var a = P.earlier || {}, b = P.later || {};
    var out = { kind: 'protein', entered: pA.v.status !== 'blank' || pB.v.status !== 'blank', reasons: [], cautions: [], computed: false,
      earlier: { raw: pA.v.raw, date: pA.d.iso, measure: a.measure, unit: a.unit, exact: exactOf(a, pA.v), limit: !exactOf(a, pA.v) && pA.v.status !== 'blank' },
      later: { raw: pB.v.raw, date: pB.d.iso, measure: b.measure, unit: b.unit, exact: exactOf(b, pB.v), limit: !exactOf(b, pB.v) && pB.v.status !== 'blank' } };
    if (!out.entered) return out;
    if (pA.v.status === 'blank' || pB.v.status === 'blank') { out.reasons.push('p-missing'); return out; }
    if (a.measure !== b.measure) { out.reasons.push('p-measure-diff'); return out; }
    if (a.measure !== 'total-protein-24h' && a.unit !== b.unit) { out.reasons.push('p-unit-diff'); return out; }
    if (!out.earlier.exact || !out.later.exact) out.reasons.push('p-limit');
    if (a.measure === 'total-protein-24h' && (a.collectionComplete !== 'yes' || b.collectionComplete !== 'yes')) out.reasons.push('p-collection');
    if (C.sameProteinMethod === 'no') out.reasons.push('p-method-diff');
    if (out.reasons.length) return out;
    if (C.sameProteinMethod !== 'yes') out.cautions.push('p-method-unknown');
    out.unit = baseUnit(a.measure, a.unit);
    out.earlier.base = toBase(pA.v.value, a.unit);
    out.later.base = toBase(pB.v.value, b.unit);
    out.earlier.normalized = a.unit === 'mg/24h';
    out.later.normalized = b.unit === 'mg/24h';
    out.sameDate = pA.d.iso === pB.d.iso;
    if (out.sameDate) return out;
    out.change = changeOf(out.earlier.base, out.later.base);
    out.computed = true;
    return out;
  }

  function egfrSeries(G, eA, eB, C) {
    var a = G.earlier || {}, b = G.later || {};
    var out = { kind: 'egfr', entered: eA.v.status !== 'blank' || eB.v.status !== 'blank', reasons: [], cautions: [], computed: false, unit: 'mL/min/1.73 m²',
      earlier: { raw: eA.v.raw, date: eA.d.iso, equation: a.equation, exact: exactOf(a, eA.v), limit: !exactOf(a, eA.v) && eA.v.status !== 'blank' },
      later: { raw: eB.v.raw, date: eB.d.iso, equation: b.equation, exact: exactOf(b, eB.v), limit: !exactOf(b, eB.v) && eB.v.status !== 'blank' } };
    if (!out.entered) return out;
    if (eA.v.status === 'blank' || eB.v.status === 'blank') { out.reasons.push('e-missing'); return out; }
    // Setting-level exclusions first: these make eGFR comparison inappropriate whatever the numbers.
    if (C.onDialysis === 'yes') out.reasons.push('e-dialysis');
    else if (C.onDialysis !== 'no') out.reasons.push('e-dialysis-unknown');
    if (C.adult === 'no') out.reasons.push('e-child');
    else if (C.adult !== 'yes') out.reasons.push('e-adult-unknown');
    if (C.acuteOrUnstable === 'yes') out.reasons.push('e-unstable');
    else if (C.acuteOrUnstable !== 'no') out.reasons.push('e-unstable-unknown');
    var known = EQUATIONS.slice(0, 4);
    if (known.indexOf(a.equation) < 0 || known.indexOf(b.equation) < 0) out.reasons.push('e-equation-unknown');
    else if (a.equation !== b.equation) out.reasons.push('e-equation-diff');
    if (!out.earlier.exact || !out.later.exact) out.reasons.push('e-limit');
    if (out.reasons.length) return out;
    out.earlier.base = eA.v.value; out.later.base = eB.v.value;
    out.sameDate = eA.d.iso === eB.d.iso;
    if (out.sameDate) return out;
    out.change = changeOf(out.earlier.base, out.later.base);
    out.computed = true;
    return out;
  }

  /* ── Result → language-neutral list of lines (used by both DOM render and copy text) ── */
  function seriesLines(sr, lang) {
    var t = str(lang), lines = [];
    if (!sr.entered) return lines;
    function pointText(label, p, isProtein) {
      var u = isProtein ? p.unit : sr.unit;
      var s = label + ' (' + (p.date || '?') + '): ' + p.raw + ' ' + (u || '');
      if (p.limit) s += ' [' + t.limitShown + ']';
      if (isProtein && p.normalized && p.base !== undefined) s += ' (' + t.normalized + ' ' + fmt(p.base) + ' g/24h)';
      if (isProtein && p.measure) s += ' · ' + t.measure[p.measure];
      if (!isProtein && p.equation) s += ' · ' + t.eq[p.equation];
      return s;
    }
    var isP = sr.kind === 'protein';
    lines.push({ k: 'point', text: pointText(t.earlier, sr.earlier, isP) });
    lines.push({ k: 'point', text: pointText(t.later, sr.later, isP) });
    if (sr.reasons.length) {
      lines.push({ k: 'withheld', text: t.notCompared + ':' });
      sr.reasons.forEach(function (r) { lines.push({ k: 'reason', text: t.R[r] }); });
      return lines;
    }
    if (sr.sameDate) { lines.push({ k: 'reason', text: t.sameDate }); return lines; }
    var c = sr.change, lead = isP ? t.pReported : t.eReported, unit = isP ? sr.unit : '';
    var span = ' (' + sr.earlier.date + ' → ' + sr.later.date + ')';
    var txt;
    if (c.dir === 'same') txt = lead + ' ' + t.unchanged + span + '.';
    else txt = lead + ' ' + (c.dir === 'down' ? t.decreased : t.increased) + ' ' + fmt(Math.abs(c.abs)) + (unit ? ' ' + unit : '') +
      (c.pctDefined ? ' (' + fmtPct(Math.abs(c.pct)) + '%)' : '') + span + '.';
    lines.push({ k: 'result', text: txt, abs: c.abs, pct: c.pct });
    if (!c.pctDefined) lines.push({ k: 'reason', text: t.pctUndefined });
    sr.cautions.forEach(function (r) { lines.push({ k: 'caution', text: t.R[r] }); });
    return lines;
  }

  function summaryText(res, lang) {
    var t = str(lang), out = [t.title, ''];
    [['protein', t.pTitle], ['egfr', t.eTitle]].forEach(function (pair) {
      var sr = res[pair[0]]; if (!sr || !sr.entered) return;
      out.push(pair[1]);
      seriesLines(sr, lang).forEach(function (l) { out.push((l.k === 'point' || l.k === 'withheld' ? '  ' : '  - ') + l.text); });
      out.push('');
    });
    if (res.discordant) { out.push(t.discord); out.push(''); }
    out.push(t.always); out.push(t.variation);
    return out.join('\n');
  }

  /* ── Passport ── */
  var REC_KEYS = ['typing', 'hematology', 'kidney', 'cardiac', 'meds', 'plan'];
  var Q_KEYS = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'];

  function buildPassport(input) {
    var rec = input.records || {}, qs = input.questions || [];
    var gather = [], have = [], autoQ = [];
    REC_KEYS.forEach(function (k) {
      var s = rec[k] || 'unknown';
      if (s === 'yes') have.push(k);
      else if (k === 'cardiac' && s === 'not-requested') { autoQ.push(k); }
      else { gather.push({ key: k, status: s }); autoQ.push(k); }
    });
    var questions = Q_KEYS.filter(function (q) { return qs.indexOf(q) >= 0; });
    return { gather: gather, have: have, autoQuestions: autoQ, questions: questions };
  }

  function passportText(pp, lang) {
    var t = str(lang), out = [t.ppTitle, ''];
    out.push(t.ppGather + ':');
    if (!pp.gather.length) out.push('  ' + t.ppNoGather);
    pp.gather.forEach(function (g) { out.push('  [ ] ' + t.rec[g.key] + ' (' + t.status[g.status] + ')'); });
    if (pp.have.length) { out.push(''); out.push(t.ppHave + ':'); pp.have.forEach(function (k) { out.push('  [x] ' + t.rec[k]); }); }
    out.push(''); out.push(t.ppQuestions + ':');
    var qn = 1;
    pp.autoQuestions.forEach(function (k) { out.push('  ' + (qn++) + '. ' + t.autoQ[k]); });
    pp.questions.forEach(function (q) { out.push('  ' + (qn++) + '. ' + t.Q[q]); });
    if (qn === 1) out.push('  ' + t.ppNoQuestions);
    out.push(''); out.push(t.ppPlan + ':');
    t.planLines.forEach(function (l) { out.push('  ' + l + ': ____________________'); });
    out.push(''); out.push(t.ppScope);
    return out.join('\n');
  }

  var api = { S: S, LANGS: LANGS, PROTEIN_UNITS: PROTEIN_UNITS, EQUATIONS: EQUATIONS, parseValue: parseValue, parseDate: parseDate, fmt: fmt, fmtPct: fmtPct,
    compare: compare, seriesLines: seriesLines, summaryText: summaryText, buildPassport: buildPassport, passportText: passportText, REC_KEYS: REC_KEYS, Q_KEYS: Q_KEYS };

  /* ── Browser controller ── */
  if (typeof document !== 'undefined') {
    var boot = function () { initComparator(); initPassport(); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
  }

  function curLang() {
    var b = document.querySelector('.lang-btn-g.active');
    var id = b ? b.id.replace('glb-', '') : 'en';
    return LANGS.indexOf(id) >= 0 ? id : 'en';
  }
  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function radio(name) { var r = document.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : 'unknown'; }
  function announce(id, msg) { var live = $(id); if (live) { live.textContent = ''; setTimeout(function () { live.textContent = msg; }, 30); } }
  function showJsOnly(root) { [].forEach.call(root.querySelectorAll('.al-js-only'), function (n) { n.hidden = false; }); }
  function copyText(text, fbWrap, fbArea, liveId, t) {
    function fallback() { fbArea.value = text; fbWrap.hidden = false; fbArea.focus(); fbArea.select(); announce(liveId, t.copyFail); }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(function () { announce(liveId, t.copied); }, fallback);
      else fallback();
    } catch (e) { fallback(); }
  }
  function printSection(mode) {
    document.body.setAttribute('data-print', mode);
    var done = function () { document.body.removeAttribute('data-print'); window.removeEventListener('afterprint', done); };
    window.addEventListener('afterprint', done);
    window.print();
    setTimeout(function () { if (document.body.getAttribute('data-print') === mode) done(); }, 2000);
  }

  function syncUnits(measureSel, unitSel, collWrap) {
    var units = PROTEIN_UNITS[measureSel.value] || [];
    var prev = unitSel.value;
    [].forEach.call(unitSel.options, function (o) { o.hidden = units.indexOf(o.value) < 0; o.disabled = units.indexOf(o.value) < 0; });
    if (units.indexOf(prev) < 0) unitSel.value = units[0];
    if (collWrap) collWrap.hidden = measureSel.value !== 'total-protein-24h';
  }

  function initComparator() {
    var form = $('al-cmp-form'); if (!form) return;
    var root = $('al-comparator'); showJsOnly(root);
    var out = $('al-cmp-result'), errBox = $('al-cmp-errors'), actions = $('al-cmp-actions');
    var last = null;
    ['a', 'b'].forEach(function (s) {
      var m = $('al-p-' + s + '-measure'), u = $('al-p-' + s + '-unit'), cw = $('al-p-' + s + '-coll-wrap');
      m.addEventListener('change', function () { syncUnits(m, u, cw); });
      syncUnits(m, u, cw);
    });
    function read() {
      function p(s) { return { date: $('al-p-' + s + '-date').value, value: $('al-p-' + s + '-value').value, measure: $('al-p-' + s + '-measure').value,
        unit: $('al-p-' + s + '-unit').value, shownAs: $('al-p-' + s + '-shown').value, collectionComplete: radio('al-p-' + s + '-coll') }; }
      function e(s) { return { date: $('al-e-' + s + '-date').value, value: $('al-e-' + s + '-value').value, equation: $('al-e-' + s + '-eq').value, shownAs: $('al-e-' + s + '-shown').value }; }
      return { protein: { earlier: p('a'), later: p('b') }, egfr: { earlier: e('a'), later: e('b') },
        context: { adult: radio('al-c-adult'), onDialysis: radio('al-c-dialysis'), acuteOrUnstable: radio('al-c-unstable'), sameProteinMethod: radio('al-c-method') } };
    }
    function clearErrors() {
      errBox.hidden = true; errBox.textContent = '';
      [].forEach.call(form.querySelectorAll('[aria-invalid="true"]'), function (n) { n.removeAttribute('aria-invalid'); });
      [].forEach.call(form.querySelectorAll('.al-field-err'), function (n) { n.textContent = ''; });
    }
    function invalidate() {
      if (!last) return;
      last = null; out.hidden = true; out.textContent = ''; actions.hidden = true; $('al-cmp-fallback').hidden = true;
      announce('al-cmp-live', str(curLang()).stale);
    }
    form.addEventListener('input', invalidate);
    form.addEventListener('change', invalidate);
    form.addEventListener('submit', function (ev) {
      ev.preventDefault(); clearErrors();
      var lang = curLang(), t = str(lang), res = compare(read());
      if (!res.ok) {
        errBox.appendChild(el('h4', null, t.errHead));
        var ul = el('ul');
        res.errors.forEach(function (er) {
          var f = $(er.field), li = el('li'), a = el('a', null, t.E[er.code] || er.code);
          a.href = '#' + er.field; li.appendChild(a); ul.appendChild(li);
          if (f) { f.setAttribute('aria-invalid', 'true'); var fe = $(er.field + '-err'); if (fe) fe.textContent = t.E[er.code] || er.code; }
        });
        errBox.appendChild(ul); errBox.hidden = false; errBox.focus();
        return;
      }
      render(res, lang); last = res;
    });
    function render(res, lang) {
      var t = str(lang); out.textContent = '';
      out.appendChild(el('h3', 'al-sum-title', t.title));
      var any = false;
      [['protein', t.pTitle], ['egfr', t.eTitle]].forEach(function (pair) {
        var sr = res[pair[0]]; if (!sr.entered) return; any = true;
        var box = el('div', 'al-series'); box.appendChild(el('h4', null, pair[1]));
        var ul = el('ul');
        seriesLines(sr, lang).forEach(function (l) { ul.appendChild(el('li', 'al-line al-l-' + l.k, l.text)); });
        box.appendChild(ul); out.appendChild(box);
      });
      if (res.discordant) out.appendChild(el('p', 'al-discord', t.discord));
      out.appendChild(el('p', 'al-scope-strong', t.always));
      out.appendChild(el('p', 'al-scope', t.variation));
      out.hidden = false; actions.hidden = !any;
      out.focus(); announce('al-cmp-live', t.done);
    }
    $('al-cmp-copy').addEventListener('click', function () { if (last) copyText(summaryText(last, curLang()), $('al-cmp-fallback'), $('al-cmp-fallback-text'), 'al-cmp-live', str(curLang())); });
    $('al-cmp-print').addEventListener('click', function () { if (last) printSection('comparison'); });
    $('al-cmp-print-blank').addEventListener('click', function () { printSection('comparison-blank'); });
    $('al-cmp-clear').addEventListener('click', function () {
      form.reset(); clearErrors(); last = null; out.hidden = true; out.textContent = ''; actions.hidden = true;
      $('al-cmp-fallback').hidden = true; $('al-cmp-fallback-text').value = '';
      ['a', 'b'].forEach(function (s) { syncUnits($('al-p-' + s + '-measure'), $('al-p-' + s + '-unit'), $('al-p-' + s + '-coll-wrap')); });
      announce('al-cmp-live', str(curLang()).cleared);
    });
    [].forEach.call(document.querySelectorAll('.lang-btn-g'), function (b) { b.addEventListener('click', function () { setTimeout(function () { if (last) render(last, curLang()); }, 0); }); });
  }

  function initPassport() {
    var form = $('al-pp-form'); if (!form) return;
    var root = $('al-passport'); showJsOnly(root);
    var out = $('al-pp-result'), actions = $('al-pp-actions'), last = null;
    function read() {
      var rec = {}; REC_KEYS.forEach(function (k) { rec[k] = radio('al-pp-' + k); });
      var qs = Q_KEYS.filter(function (q) { var c = $('al-pp-' + q); return c && c.checked; });
      return { records: rec, questions: qs };
    }
    function invalidate() { if (!last) return; last = null; out.hidden = true; out.textContent = ''; actions.hidden = true; }
    form.addEventListener('change', invalidate);
    form.addEventListener('submit', function (ev) { ev.preventDefault(); last = buildPassport(read()); render(last, curLang()); });
    function render(pp, lang) {
      var t = str(lang); out.textContent = '';
      out.appendChild(el('h3', 'al-sum-title', t.ppTitle));
      out.appendChild(el('h4', null, t.ppGather));
      if (!pp.gather.length) out.appendChild(el('p', 'al-note', t.ppNoGather));
      else { var ul = el('ul', 'al-checklist'); pp.gather.forEach(function (g) { ul.appendChild(el('li', null, '☐ ' + t.rec[g.key] + ' (' + t.status[g.status] + ')')); }); out.appendChild(ul); }
      if (pp.have.length) { out.appendChild(el('h4', null, t.ppHave)); var hl = el('ul', 'al-checklist'); pp.have.forEach(function (k) { hl.appendChild(el('li', null, '☑ ' + t.rec[k])); }); out.appendChild(hl); }
      out.appendChild(el('h4', null, t.ppQuestions));
      var ol = el('ol');
      pp.autoQuestions.forEach(function (k) { ol.appendChild(el('li', null, t.autoQ[k])); });
      pp.questions.forEach(function (q) { ol.appendChild(el('li', null, t.Q[q])); });
      if (!ol.children.length) out.appendChild(el('p', 'al-note', t.ppNoQuestions)); else out.appendChild(ol);
      out.appendChild(el('h4', null, t.ppPlan));
      t.planLines.forEach(function (l) { var d = el('div', 'al-plan-line'); d.appendChild(el('span', null, l)); d.appendChild(el('span', 'al-blank')); out.appendChild(d); });
      out.appendChild(el('p', 'al-scope', t.ppScope));
      out.hidden = false; actions.hidden = false; out.focus(); announce('al-pp-live', t.ppDone);
    }
    $('al-pp-copy').addEventListener('click', function () { if (last) copyText(passportText(last, curLang()), $('al-pp-fallback'), $('al-pp-fallback-text'), 'al-pp-live', str(curLang())); });
    $('al-pp-print').addEventListener('click', function () { if (last) printSection('passport'); });
    $('al-pp-print-blank').addEventListener('click', function () { printSection('passport-blank'); });
    $('al-pp-clear').addEventListener('click', function () { form.reset(); last = null; out.hidden = true; out.textContent = ''; actions.hidden = true; $('al-pp-fallback').hidden = true; $('al-pp-fallback-text').value = ''; announce('al-pp-live', str(curLang()).cleared); });
    [].forEach.call(document.querySelectorAll('.lang-btn-g'), function (b) { b.addEventListener('click', function () { setTimeout(function () { if (last) render(last, curLang()); }, 0); }); });
  }

  return api;
});
