/* born-small-planner.js — renalcarematters.com
 *
 * Birth History & Kidney Visit Planner for guides/born-small-kidneys-for-life.html.
 * Pure functions (Node-testable via tests/born-small-planner.cjs) plus a small
 * browser controller that binds to the guide's #bs-* form.
 *
 * Scope (do not change without clinical review):
 *   - Organizes reported history and builds visit questions.
 *   - Never outputs a risk tier, score, percentage, diagnosis, test order or date.
 *   - Never infers SGA, FGR or AGA from weight and gestation.
 *   - Entered values stay in memory: no storage, URL, analytics or network use.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.BornSmallPlanner = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var LB_G = 453.59237;
  var OZ_G = 28.349523125;
  var LANGS = ['en', 'tl', 'ceb', 'kap'];
  var HISTORY_KEYS = ['documentedSGA', 'documentedFGR', 'nicuCare', 'neonatalAKI', 'neonatalDialysis',
    'congenitalKidneyUrinaryCondition', 'majorCongenitalHeartCondition', 'clinicianIdentifiedCurrentConcern'];

  /* ── Strings (EN reviewed; TL/CEB/KAP are drafts pending native-speaker review) ── */
  var S = {
    en: {
      h_entered: 'What you entered', h_records: 'Records that may help', h_questions: 'Questions for your visit',
      h_plan: "Your clinician's plan", plan: ['Next review', 'Tests, if any', 'Medicine advice', 'Responsible clinician'],
      scope: 'This summary organizes reported history. It does not diagnose kidney disease or predict your risk.',
      title: 'Birth History & Kidney Visit Summary',
      f_for: 'This is for', f_weight: 'Birth weight', f_ga: 'Weeks of pregnancy at birth',
      f_documentedSGA: 'Documented SGA (small for gestational age)', f_documentedFGR: 'Documented FGR (fetal growth restriction)',
      f_nicuCare: 'NICU (neonatal intensive care unit) care', f_neonatalAKI: 'Newborn kidney injury (AKI)',
      f_neonatalDialysis: 'Newborn dialysis', f_congenitalKidneyUrinaryCondition: 'Kidney or urinary condition present from birth',
      f_majorCongenitalHeartCondition: 'Major heart condition present from birth',
      f_clinicianIdentifiedCurrentConcern: 'Current kidney or blood pressure concern identified by a clinician',
      f_source: 'Where this information came from',
      aud: { 'infant-child': 'an infant or child', adolescent: 'an adolescent', adult: 'an adult' },
      ans: { yes: 'Yes', no: 'No', unknown: 'Unknown' },
      src: { 'medical-record': 'medical record', 'family-recollection': 'family recollection', 'mixed-uncertain': 'mixed or uncertain' },
      reported: 'reported', unknown: 'Unknown', weeks: 'weeks', days: 'days', daysNotGiven: 'extra days not given',
      lbw: 'below the 2,500 g low-birth-weight threshold', vlbw: 'below 1,500 g', preterm: 'preterm birth (before 37 completed weeks)',
      records: ['Birth record or newborn discharge summary', 'Previous pediatric or kidney clinic letters', 'Family-held child-health booklet or baby book'],
      recordsUnknown: 'Some answers are unknown. That is common and does not stop you from using this summary.',
      Q: {
        base: ['Does this history change what you would check for me now?',
          'Have blood pressure and any relevant kidney tests been interpreted for my age?',
          'What should I do if vomiting, diarrhea, poor intake, or another illness develops?',
          'Which pain medicines and supplements should I check with you first?'],
        record: 'Could a birth record or newborn discharge summary clarify this history?',
        weight: 'Does my birth weight, together with the rest of my history, change the assessment you recommend?',
        vlbw: 'Was a kidney check around age two planned or done, and what did it show?',
        gestation: 'Was a kidney follow-up plan included in neonatal care?',
        pretermGrowth: 'Babies born early who were also small for their age are often offered a kidney check around age two. Was that planned or done?',
        growth: 'Can we keep the documented size and growth history distinct in my record?',
        neonatal: 'Can we review the newborn kidney event and the discharge follow-up plan?',
        congenital: 'Should the existing specialist and my usual clinician coordinate the kidney follow-up plan?',
        cardiac: 'Has my heart team included kidney checks in the regular heart follow-up?',
        current: 'Who is following this concern, and when should I be reviewed?',
        inconsistent: 'The reported dialysis and AKI history need clarification from the newborn record.',
        growthYears: 'Should my kidney checks be repeated while I am growing quickly?'
      },
      E: {
        'audience-required': 'Please choose who this planner is for.',
        format: 'Enter numbers only, using a period for decimals (for example 2.5).',
        nonpositive: 'Birth weight must be more than zero.',
        'pounds-integer': 'Pounds must be a whole number; put the rest in ounces.',
        'ounces-range': 'Ounces must be from 0 to less than 16.',
        'weeks-integer': 'Weeks must be a whole number.',
        'days-range': 'Extra days must be a whole number from 0 to 6.',
        'weeks-needed': 'Enter the weeks too, or leave both blank.',
        'weight-unusual': 'This birth weight is unusual. Check the number and unit, then tick the confirmation box.',
        'gestation-unusual': 'This number of weeks is unusual. Check it, then tick the confirmation box.'
      },
      errHead: 'Please check the following:', stale: 'Your entries changed. Press "Make my summary" again.',
      done: 'Summary ready.', copied: 'Copied.', copyFail: 'Copy did not work. Select the text below and copy it.', cleared: 'Entries cleared.'
    },
    tl: {
      h_entered: 'Ang inilagay mo', h_records: 'Mga record na maaaring makatulong', h_questions: 'Mga tanong para sa iyong pagbisita',
      h_plan: 'Plano ng iyong doktor', plan: ['Susunod na pagsusuri', 'Mga test, kung mayroon', 'Payo tungkol sa gamot', 'Responsableng doktor'],
      scope: 'Inaayos ng buod na ito ang iniulat na kasaysayan. Hindi ito nagda-diagnose ng sakit sa bato o naghuhula ng iyong panganib.',
      title: 'Buod ng Kasaysayan ng Pagsilang at Pagbisita para sa Bato',
      f_for: 'Para sa', f_weight: 'Timbang noong ipinanganak', f_ga: 'Linggo ng pagbubuntis noong ipinanganak',
      f_documentedSGA: 'Nakadokumentong SGA (maliit para sa edad ng pagbubuntis)', f_documentedFGR: 'Nakadokumentong FGR (bumagal ang paglaki sa sinapupunan)',
      f_nicuCare: 'Pangangalaga sa NICU (neonatal intensive care unit)', f_neonatalAKI: 'Pinsala sa bato noong bagong silang (AKI)',
      f_neonatalDialysis: 'Dialysis noong bagong silang', f_congenitalKidneyUrinaryCondition: 'Kondisyon sa bato o daluyan ng ihi mula pagkasilang',
      f_majorCongenitalHeartCondition: 'Malaking kondisyon sa puso mula pagkasilang',
      f_clinicianIdentifiedCurrentConcern: 'Kasalukuyang alalahanin sa bato o presyon na nakita ng doktor',
      f_source: 'Pinagmulan ng impormasyon',
      aud: { 'infant-child': 'sanggol o bata', adolescent: 'tinedyer', adult: 'nasa hustong gulang' },
      ans: { yes: 'Oo', no: 'Hindi', unknown: 'Hindi alam' },
      src: { 'medical-record': 'medical record', 'family-recollection': 'alaala ng pamilya', 'mixed-uncertain': 'halo o hindi tiyak' },
      reported: 'iniulat', unknown: 'Hindi alam', weeks: 'linggo', days: 'araw', daysNotGiven: 'hindi ibinigay ang dagdag na araw',
      lbw: 'mas mababa sa 2,500 g na hangganan ng mababang timbang', vlbw: 'mas mababa sa 1,500 g', preterm: 'maagang pagsilang (bago ang 37 buong linggo)',
      records: ['Birth record o newborn discharge summary', 'Mga naunang sulat mula sa pedia o kidney clinic', 'Child-health booklet o baby book ng pamilya'],
      recordsUnknown: 'May mga sagot na hindi alam. Karaniwan ito at hindi hadlang sa paggamit ng buod na ito.',
      Q: {
        base: ['Binabago ba ng kasaysayang ito ang dapat ninyong suriin sa akin ngayon?',
          'Nabasa ba ang aking presyon ng dugo at mga kaugnay na pagsusuri sa bato ayon sa aking edad?',
          'Ano ang dapat kong gawin kung magsuka, magtae, hindi makakain o makainom nang maayos, o magkaroon ng ibang sakit?',
          'Aling mga gamot sa sakit at supplement ang dapat ko munang itanong sa inyo?'],
        record: 'Makatutulong ba ang birth record o newborn discharge summary para linawin ang kasaysayang ito?',
        weight: 'Binabago ba ng aking timbang noong ipinanganak, kasama ng iba ko pang kasaysayan, ang pagsusuring inirerekomenda ninyo?',
        vlbw: 'May nakaplano o nagawa bang pagsusuri sa bato bandang edad dalawa, at ano ang ipinakita nito?',
        gestation: 'May kasama bang plano sa follow-up ng bato sa pangangalaga noong sanggol pa?',
        pretermGrowth: 'Ang mga sanggol na ipinanganak nang maaga at maliit din para sa kanilang edad ay kadalasang binibigyan ng pagsusuri sa bato bandang edad dalawa. Naplano o nagawa ba ito?',
        growth: 'Maaari bang panatilihing hiwalay sa aking record ang nakadokumentong kasaysayan ng laki at paglaki?',
        neonatal: 'Maaari ba nating balikan ang nangyari sa bato noong bagong silang at ang plano sa follow-up paglabas ng ospital?',
        congenital: 'Dapat bang magtulungan ang kasalukuyang espesyalista at ang aking karaniwang doktor sa plano ng follow-up sa bato?',
        cardiac: 'Isinama ba ng aking heart team ang mga pagsusuri sa bato sa regular na follow-up sa puso?',
        current: 'Sino ang sumusubaybay sa alalahaning ito, at kailan ako dapat masuri muli?',
        inconsistent: 'Kailangang linawin mula sa newborn record ang iniulat na kasaysayan ng dialysis at AKI.',
        growthYears: 'Dapat bang ulitin ang mga pagsusuri sa aking bato habang mabilis akong lumalaki?'
      },
      E: {
        'audience-required': 'Pakipili kung para kanino ang planner na ito.',
        format: 'Numero lamang, gumamit ng tuldok para sa decimal (halimbawa 2.5).',
        nonpositive: 'Dapat higit sa zero ang timbang.',
        'pounds-integer': 'Dapat buong numero ang pounds; ilagay ang natitira sa ounces.',
        'ounces-range': 'Ang ounces ay dapat mula 0 hanggang mas mababa sa 16.',
        'weeks-integer': 'Dapat buong numero ang linggo.',
        'days-range': 'Ang dagdag na araw ay dapat buong numero mula 0 hanggang 6.',
        'weeks-needed': 'Ilagay din ang linggo, o iwanang blangko ang dalawa.',
        'weight-unusual': 'Hindi karaniwan ang timbang na ito. Suriin ang numero at unit, saka i-tsek ang kahon ng kumpirmasyon.',
        'gestation-unusual': 'Hindi karaniwan ang bilang ng linggong ito. Suriin ito, saka i-tsek ang kahon ng kumpirmasyon.'
      },
      errHead: 'Pakisuri ang mga sumusunod:', stale: 'Nagbago ang mga inilagay mo. Pindutin muli ang "Gawin ang aking buod".',
      done: 'Handa na ang buod.', copied: 'Nakopya na.', copyFail: 'Hindi gumana ang pagkopya. Piliin ang teksto sa ibaba at kopyahin.', cleared: 'Nabura na ang mga inilagay.'
    },
    ceb: {
      h_entered: 'Ang imong gisulod', h_records: 'Mga record nga makatabang', h_questions: 'Mga pangutana alang sa imong pagbisita',
      h_plan: 'Plano sa imong doktor', plan: ['Sunod nga pagsusi', 'Mga test, kung aduna', 'Tambag bahin sa tambal', 'Responsable nga doktor'],
      scope: 'Gihan-ay niini nga sumaryo ang gitaho nga kasaysayan. Dili kini mo-diagnose sa sakit sa bato o motag-an sa imong peligro.',
      title: 'Sumaryo sa Kasaysayan sa Pagkatawo ug Pagbisita alang sa Bato',
      f_for: 'Alang sa', f_weight: 'Timbang sa pagkatawo', f_ga: 'Semana sa pagmabdos sa pagkatawo',
      f_documentedSGA: 'Nadokumento nga SGA (gamay alang sa edad sa pagmabdos)', f_documentedFGR: 'Nadokumento nga FGR (mihinay ang pagtubo sa tiyan)',
      f_nicuCare: 'Pag-atiman sa NICU (neonatal intensive care unit)', f_neonatalAKI: 'Kadaot sa bato sa bag-ong natawo (AKI)',
      f_neonatalDialysis: 'Dialysis sa bag-ong natawo', f_congenitalKidneyUrinaryCondition: 'Kondisyon sa bato o agianan sa ihi gikan sa pagkatawo',
      f_majorCongenitalHeartCondition: 'Dakong kondisyon sa kasingkasing gikan sa pagkatawo',
      f_clinicianIdentifiedCurrentConcern: 'Karon nga kabalaka sa bato o presyon nga nakita sa doktor',
      f_source: 'Gigikanan sa impormasyon',
      aud: { 'infant-child': 'masuso o bata', adolescent: 'tin-edyer', adult: 'hamtong' },
      ans: { yes: 'Oo', no: 'Dili', unknown: 'Wala mahibaw-i' },
      src: { 'medical-record': 'medical record', 'family-recollection': 'panumdoman sa pamilya', 'mixed-uncertain': 'sagol o dili sigurado' },
      reported: 'gitaho', unknown: 'Wala mahibaw-i', weeks: 'semana', days: 'adlaw', daysNotGiven: 'wala gihatag ang dugang nga adlaw',
      lbw: 'ubos sa 2,500 g nga utlanan sa ubos nga timbang', vlbw: 'ubos sa 1,500 g', preterm: 'sayo nga pagkatawo (sa wala pa ang 37 ka bug-os nga semana)',
      records: ['Birth record o newborn discharge summary', 'Mga nauna nga sulat gikan sa pedia o kidney clinic', 'Child-health booklet o baby book sa pamilya'],
      recordsUnknown: 'Adunay mga tubag nga wala mahibaw-i. Kasagaran kini ug dili makapugong sa paggamit niini nga sumaryo.',
      Q: {
        base: ['Mausab ba tungod niini nga kasaysayan ang angay ninyong susihon kanako karon?',
          'Gisusi ba ang akong presyon sa dugo ug mga may kalabotan nga pagsusi sa bato sumala sa akong edad?',
          'Unsa ang akong buhaton kung magsuka, magkalibanga, dili makakaon o makainom og maayo, o adunay laing sakit?',
          'Unsang mga tambal sa sakit ug supplement ang kinahanglan nako unang ipangutana kaninyo?'],
        record: 'Makatabang ba ang birth record o newborn discharge summary aron klarohon kini nga kasaysayan?',
        weight: 'Mausab ba tungod sa akong timbang sa pagkatawo, uban sa ubang bahin sa akong kasaysayan, ang pagsusi nga inyong girekomenda?',
        vlbw: 'Aduna bay giplano o nahimo nga pagsusi sa bato sa mga edad duha, ug unsa ang gipakita niini?',
        gestation: 'Apil ba ang plano sa follow-up sa bato sa pag-atiman sa bag-ong natawo?',
        pretermGrowth: 'Ang mga bata nga natawo nga sayo ug gamay usab alang sa ilang edad kasagaran gitanyagan og pagsusi sa bato sa mga edad duha. Giplano o nahimo ba kini?',
        growth: 'Mahimo bang ipabilin nga lahi sa akong record ang nadokumento nga kasaysayan sa gidak-on ug pagtubo?',
        neonatal: 'Mahimo ba natong balikan ang nahitabo sa bato sa bag-ong natawo ug ang plano sa follow-up paggawas sa ospital?',
        congenital: 'Angay bang magtinabangay ang karon nga espesyalista ug ang akong naandang doktor sa plano sa follow-up sa bato?',
        cardiac: 'Gilakip ba sa akong heart team ang mga pagsusi sa bato sa regular nga follow-up sa kasingkasing?',
        current: 'Kinsa ang nagsubay niini nga kabalaka, ug kanus-a ko angay susihon pag-usab?',
        inconsistent: 'Kinahanglang klarohon gikan sa newborn record ang gitaho nga kasaysayan sa dialysis ug AKI.',
        growthYears: 'Angay bang usbon ang mga pagsusi sa akong bato samtang paspas ako nga nagdako?'
      },
      E: {
        'audience-required': 'Palihug pilia kung alang kang kinsa kini nga planner.',
        format: 'Numero lang, gamita ang tuldok alang sa decimal (pananglitan 2.5).',
        nonpositive: 'Kinahanglan labaw sa zero ang timbang.',
        'pounds-integer': 'Kinahanglan tibuok nga numero ang pounds; ibutang ang nahabilin sa ounces.',
        'ounces-range': 'Ang ounces kinahanglan gikan 0 hangtod ubos sa 16.',
        'weeks-integer': 'Kinahanglan tibuok nga numero ang semana.',
        'days-range': 'Ang dugang nga adlaw kinahanglan tibuok nga numero gikan 0 hangtod 6.',
        'weeks-needed': 'Isulod usab ang semana, o biyai nga blangko ang duha.',
        'weight-unusual': 'Dili kasagaran kini nga timbang. Susiha ang numero ug unit, unya i-tsek ang kahon sa kumpirmasyon.',
        'gestation-unusual': 'Dili kasagaran kini nga gidaghanon sa semana. Susiha kini, unya i-tsek ang kahon sa kumpirmasyon.'
      },
      errHead: 'Palihug susiha ang mosunod:', stale: 'Nausab ang imong gisulod. Pindota pag-usab ang "Himoa ang akong sumaryo".',
      done: 'Andam na ang sumaryo.', copied: 'Nakopya na.', copyFail: 'Wala molihok ang pagkopya. Pilia ang teksto sa ubos ug kopyaha.', cleared: 'Napapas na ang gisulod.'
    },
    kap: {
      h_entered: 'Ing inilagay mu', h_records: 'Reng record a makasaup', h_questions: 'Reng kutang para king pamamisita mu',
      h_plan: 'Planu ning doktor mu', plan: ['Susunod a pamanigaral', 'Reng test, nung atin', 'Payu tungkul king gamut', 'Responsable a doktor'],
      scope: 'Ayusan na ning buod a iti ing iniulat a kasaysayan. Ali ya mag-diagnose ning sakit king batu o manula king peligru mu.',
      title: 'Buod ning Kasaysayan ning Pangabait at Pamamisita para king Batu',
      f_for: 'Para king', f_weight: 'Timbang kanitang mibait', f_ga: 'Linggu ning pamagbuntis kanitang mibait',
      f_documentedSGA: 'Nadokumentung SGA (malati para king edad ning pamagbuntis)', f_documentedFGR: 'Nadokumentung FGR (mibagal ing pamagdagul king atian)',
      f_nicuCare: 'Pamanalaga king NICU (neonatal intensive care unit)', f_neonatalAKI: 'Pinsala king batu kanitang bayung mibait (AKI)',
      f_neonatalDialysis: 'Dialysis kanitang bayung mibait', f_congenitalKidneyUrinaryCondition: 'Kondisyun king batu o dalanan ning ihi manibat kanitang mibait',
      f_majorCongenitalHeartCondition: 'Masikan a kondisyun king pusu manibat kanitang mibait',
      f_clinicianIdentifiedCurrentConcern: 'Kasalukuyang pibabalisan king batu o presyon a akit ning doktor',
      f_source: 'Pikuanan ning impormasyun',
      aud: { 'infant-child': 'sanggol o anak', adolescent: 'binatilyu o dalaga', adult: 'matwang tau' },
      ans: { yes: 'Wa', no: 'Ali', unknown: 'E balu' },
      src: { 'medical-record': 'medical record', 'family-recollection': 'gunita ning pamilya', 'mixed-uncertain': 'alu o e siguradu' },
      reported: 'iniulat', unknown: 'E balu', weeks: 'linggu', days: 'aldo', daysNotGiven: 'e mebie ing dagdag a aldo',
      lbw: 'mababa king 2,500 g a angganan ning mababang timbang', vlbw: 'mababa king 1,500 g', preterm: 'maagang pangabait (bayu ing 37 a buung linggu)',
      records: ['Birth record o newborn discharge summary', 'Reng milabas a sulat manibat king pedia o kidney clinic', 'Child-health booklet o baby book ning pamilya'],
      recordsUnknown: 'Atin reng sagot a e balu. Karaniwan ya ini at ali ya sasalangan king pamangamit king buod a iti.',
      Q: {
        base: ['Babaguan ne ning kasaysayan a iti ing dapat yung lawan kanaku ngeni?',
          'Binasa ne ing presyon ning daya ku at reng sasaup a pamanigaral king batu agpang king edad ku?',
          'Nanu ing dapat kung gawan nung mamuta ku, magtae, e makapangan o makainum ayusan, o magkasakit aliwa?',
          'Nanung gamut king sakit at supplement ing dapat kung itanung kekayu pamuna?'],
        record: 'Makasaup ya ing birth record o newborn discharge summary ban linawan ing kasaysayan a iti?',
        weight: 'Babaguan ne ning timbang ku kanitang mibait ku, kayabe ning aliwang kasaysayan ku, ing pamanigaral a irekomenda yu?',
        vlbw: 'Atin bang meplanu o megawang pamanigaral king batu kanitang adwang banwa, at nanu ing pepakit na?',
        gestation: 'Kayabe ya ing planu king follow-up ning batu king pamanalaga kanitang sanggol pa?',
        pretermGrowth: 'Deng sanggol a mibait a maaga at malati para king edad da, karaniwan dang bibiyan pamanigaral king batu kanitang adwang banwa. Meplanu o megawa ya ini?',
        growth: 'Malyari tang panatilian a miyayaliwa king record ku ing nadokumentung kasaysayan ning sukat at pamagdagul?',
        neonatal: 'Malyari tang balikan ing milyari king batu kanitang bayung mibait at ing planu king follow-up kanitang lumual king ospital?',
        congenital: 'Dapat bang magsaupan ing espesyalista ngeni at ing karaniwan kung doktor king planu king follow-up ning batu?',
        cardiac: 'Ibilang na ning heart team ku ing pamanigaral king batu king regular a follow-up ning pusu?',
        current: 'Ninu ing manubaybay king pibabalisan a iti, at kapilan ku dapat lawan pasibayu?',
        inconsistent: 'Kailangan yang linawan manibat king newborn record ing iniulat a kasaysayan ning dialysis at AKI.',
        growthYears: 'Dapat bang ulitan ing pamanigaral king batu ku kabang mabilis kung dagul?'
      },
      E: {
        'audience-required': 'Pakipili nung para kaninu ing planner a iti.',
        format: 'Numero mu pamu, gamitan ing tuldok para king decimal (alimbawa 2.5).',
        nonpositive: 'Dapat maragul king zero ing timbang.',
        'pounds-integer': 'Dapat buung numero ing pounds; ibili ing kulang king ounces.',
        'ounces-range': 'Ing ounces dapat manibat 0 anggang mababa king 16.',
        'weeks-integer': 'Dapat buung numero ing linggu.',
        'days-range': 'Ing dagdag a aldo dapat buung numero manibat 0 anggang 6.',
        'weeks-needed': 'Ibili mu naman ing linggu, o pabayan yung blangku ing adwa.',
        'weight-unusual': 'E karaniwan ing timbang a iti. Lawan ing numero at unit, kaybat i-tsek ing kahon ning kumpirmasyun.',
        'gestation-unusual': 'E karaniwan ing bilang ning linggu a iti. Lawan me, kaybat i-tsek ing kahon ning kumpirmasyun.'
      },
      errHead: 'Pakilawe deng makatuki:', stale: 'Mibayu ing inilagay mu. Pinduten pasibayu ing "Gawan ing buod ku".',
      done: 'Andya na ing buod.', copied: 'Mekopya na.', copyFail: 'E megana ing pamikopya. Pilian ing teksto king lalam at kopyan.', cleared: 'Mepalis na ing inilagay.'
    }
  };

  function str(lang) { return S[LANGS.indexOf(lang) >= 0 ? lang : 'en']; }

  /* ── Number parsing: strict, no partial parses ── */
  function parseNum(raw, opts) {
    opts = opts || {};
    var s = String(raw == null ? '' : raw).trim();
    if (s === '') return { empty: true };
    var re = opts.integer ? /^\d+$/ : /^\d+(\.\d+)?$/;
    if (!re.test(s)) {
      if (opts.integer && /^\d+\.\d+$/.test(s)) return { error: opts.intCode || 'format' };
      return { error: 'format' };
    }
    var n = Number(s);
    if (!isFinite(n)) return { error: 'format' };
    return { value: n, text: s };
  }

  function normalizeWeight(w) {
    w = w || {};
    var unit = w.unit || 'g';
    if (unit === 'lb-oz') {
      var lb = parseNum(w.value, { integer: true, intCode: 'pounds-integer' });
      var oz = parseNum(w.ounces);
      if (lb.empty && oz.empty) return { status: 'unknown' };
      if (lb.error) return { status: 'error', field: 'weight', code: lb.error };
      if (oz.error) return { status: 'error', field: 'ounces', code: oz.error };
      var pounds = lb.empty ? 0 : lb.value, ounces = oz.empty ? 0 : oz.value;
      if (ounces < 0 || ounces >= 16) return { status: 'error', field: 'ounces', code: 'ounces-range' };
      var g = pounds * LB_G + ounces * OZ_G;
      if (!(g > 0)) return { status: 'error', field: 'weight', code: 'nonpositive' };
      return finishWeight(g, { unit: 'lb-oz', pounds: pounds, ounces: ounces });
    }
    var p = parseNum(w.value);
    if (p.empty) return { status: 'unknown' };
    if (p.error) return { status: 'error', field: 'weight', code: p.error };
    if (!(p.value > 0)) return { status: 'error', field: 'weight', code: 'nonpositive' };
    var grams = unit === 'kg' ? p.value * 1000 : p.value;
    return finishWeight(grams, { unit: unit, value: p.text });
  }
  function finishWeight(grams, original) {
    return { status: 'ok', grams: grams, original: original, unusual: grams < 300 || grams > 7000,
      belowLBW: grams < 2500, belowVLBW: grams < 1500 };
  }

  function normalizeGestation(g) {
    g = g || {};
    var wk = parseNum(g.weeks, { integer: true, intCode: 'weeks-integer' });
    var dy = parseNum(g.days, { integer: true, intCode: 'days-range' });
    if (wk.empty && dy.empty) return { status: 'unknown' };
    if (wk.empty) return { status: 'error', field: 'ga-weeks', code: 'weeks-needed' };
    if (wk.error) return { status: 'error', field: 'ga-weeks', code: wk.error === 'format' ? 'weeks-integer' : wk.error };
    if (dy.error) return { status: 'error', field: 'ga-days', code: 'days-range' };
    if (!dy.empty && dy.value > 6) return { status: 'error', field: 'ga-days', code: 'days-range' };
    var weeks = wk.value, days = dy.empty ? null : dy.value;
    return { status: 'ok', weeks: weeks, days: days, totalDays: days === null ? null : weeks * 7 + days,
      unusual: weeks < 22 || weeks > 42, preterm: weeks < 37, under34: weeks < 34 };
  }

  function answer(v) { return v === 'yes' || v === 'no' ? v : 'unknown'; }

  function validate(input) {
    input = input || {};
    var errors = [], confirms = [];
    if (['infant-child', 'adolescent', 'adult'].indexOf(input.audienceAge) < 0)
      errors.push({ field: 'audience', code: 'audience-required' });
    var weight = normalizeWeight(input.birthWeight);
    if (weight.status === 'error') errors.push({ field: weight.field, code: weight.code });
    else if (weight.status === 'ok' && weight.unusual) confirms.push({ field: 'weight', code: 'weight-unusual' });
    var gestation = normalizeGestation(input.gestation);
    if (gestation.status === 'error') errors.push({ field: gestation.field, code: gestation.code });
    else if (gestation.status === 'ok' && gestation.unusual) confirms.push({ field: 'ga-weeks', code: 'gestation-unusual' });
    var needsConfirm = confirms.length > 0 && !input.confirmedUnusual;
    return { ok: errors.length === 0 && !needsConfirm, errors: errors, confirms: confirms, needsConfirm: needsConfirm,
      weight: weight, gestation: gestation };
  }

  /* ── Deterministic prompt rules (editorial, not a clinical algorithm) ── */
  var RULE_ORDER = ['base', 'record', 'weight', 'vlbw', 'gestation', 'pretermGrowth', 'growth', 'neonatal',
    'congenital', 'cardiac', 'current', 'inconsistent', 'growthYears'];

  function buildPrompts(input, v) {
    v = v || validate(input);
    var a = {};
    HISTORY_KEYS.forEach(function (k) { a[k] = answer(input[k]); });
    var w = v.weight, g = v.gestation, hit = {};
    hit.base = true;
    var anyUnknown = w.status !== 'ok' || g.status !== 'ok' ||
      HISTORY_KEYS.some(function (k) { return a[k] === 'unknown'; });
    hit.record = anyUnknown || input.sourceConfidence !== 'medical-record';
    hit.weight = w.status === 'ok' && w.belowLBW;
    hit.vlbw = w.status === 'ok' && w.belowVLBW;
    hit.gestation = g.status === 'ok' && g.preterm;
    var growthYes = a.documentedSGA === 'yes' || a.documentedFGR === 'yes';
    hit.pretermGrowth = g.status === 'ok' && g.under34 && growthYes;
    hit.growth = growthYes;
    hit.neonatal = a.neonatalAKI === 'yes' || a.neonatalDialysis === 'yes';
    hit.congenital = a.congenitalKidneyUrinaryCondition === 'yes' || a.majorCongenitalHeartCondition === 'yes';
    hit.cardiac = a.majorCongenitalHeartCondition === 'yes';
    hit.current = a.clinicianIdentifiedCurrentConcern === 'yes';
    hit.inconsistent = a.neonatalDialysis === 'yes' && a.neonatalAKI !== 'yes';
    hit.growthYears = input.audienceAge === 'adolescent' &&
      ((g.status === 'ok' && g.preterm) || (w.status === 'ok' && w.belowLBW) || growthYes || hit.neonatal);
    return RULE_ORDER.filter(function (id) { return hit[id]; });
  }

  function fmtGrams(g) { return Math.round(g).toLocaleString('en-US') + ' g'; }

  function weightText(w, t) {
    if (w.status !== 'ok') return t.unknown;
    var o = w.original, orig;
    if (o.unit === 'lb-oz') orig = o.pounds + ' lb ' + o.ounces + ' oz';
    else if (o.unit === 'kg') orig = o.value + ' kg';
    else orig = null;
    var out = orig ? orig + ' (' + fmtGrams(w.grams) + ')' : fmtGrams(w.grams);
    var notes = [];
    if (w.belowVLBW) notes.push(t.vlbw); else if (w.belowLBW) notes.push(t.lbw);
    return out + (notes.length ? ' — ' + notes.join('; ') : '');
  }

  function gestationText(g, t) {
    if (g.status !== 'ok') return t.unknown;
    var s = g.weeks + ' ' + t.weeks + (g.days === null ? ', ' + t.daysNotGiven : ' ' + g.days + ' ' + t.days);
    if (g.preterm) s += ' — ' + t.preterm;
    return s;
  }

  function buildSummary(input, lang) {
    var t = str(lang), v = validate(input);
    if (!v.ok) return { ok: false, validation: v };
    var reported = input.sourceConfidence !== 'medical-record';
    var tag = reported ? ' (' + t.reported + ')' : '';
    var entered = [
      { label: t.f_for, value: t.aud[input.audienceAge] },
      { label: t.f_weight, value: weightText(v.weight, t) + (v.weight.status === 'ok' ? tag : '') },
      { label: t.f_ga, value: gestationText(v.gestation, t) + (v.gestation.status === 'ok' ? tag : '') }
    ];
    HISTORY_KEYS.forEach(function (k) {
      var a = answer(input[k]);
      entered.push({ label: t['f_' + k], value: t.ans[a] + (a !== 'unknown' ? tag : '') });
    });
    entered.push({ label: t.f_source, value: t.src[input.sourceConfidence] || t.src['mixed-uncertain'] });
    var ids = buildPrompts(input, v), questions = [];
    ids.forEach(function (id) {
      if (id === 'base') t.Q.base.forEach(function (q) { questions.push({ id: 'base', text: q }); });
      else questions.push({ id: id, text: t.Q[id] });
    });
    var seen = {};
    questions = questions.filter(function (q) { if (seen[q.text]) return false; seen[q.text] = true; return true; });
    return { ok: true, lang: LANGS.indexOf(lang) >= 0 ? lang : 'en', title: t.title, entered: entered,
      records: t.records.slice(), recordsNote: ids.indexOf('record') >= 0 ? t.recordsUnknown : null,
      questions: questions, ruleIds: ids, planHeading: t.h_plan, planLines: t.plan.slice(), scope: t.scope,
      headings: { entered: t.h_entered, records: t.h_records, questions: t.h_questions } };
  }

  function toPlainText(sum) {
    if (!sum || !sum.ok) return '';
    var L = [sum.title, '', sum.headings.entered];
    sum.entered.forEach(function (e) { L.push('- ' + e.label + ': ' + e.value); });
    L.push('', sum.headings.records);
    sum.records.forEach(function (r) { L.push('- ' + r); });
    if (sum.recordsNote) L.push(sum.recordsNote);
    L.push('', sum.headings.questions);
    sum.questions.forEach(function (q, i) { L.push((i + 1) + '. ' + q.text); });
    L.push('', sum.planHeading);
    sum.planLines.forEach(function (p) { L.push(p + ': ______________________________'); });
    L.push('', sum.scope);
    return L.join('\n');
  }

  /* ── Browser controller ── */
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function mount(doc) {
    var $ = function (id) { return doc.getElementById(id); };
    var form = $('bs-form'), out = $('bs-summary'), live = $('bs-live'), errBox = $('bs-errors');
    if (!form || !out) return null;
    var current = null, lastInput = null;

    function lang() {
      try { var l = localStorage.getItem('wgmr-lang'); if (LANGS.indexOf(l) >= 0) return l; } catch (e) {}
      return 'en';
    }
    function radio(name) {
      var el = form.querySelector('input[name="' + name + '"]:checked');
      return el ? el.value : 'unknown';
    }
    function read() {
      return {
        audienceAge: $('bs-audience').value,
        birthWeight: { value: $('bs-weight').value, unit: $('bs-weight-unit').value, ounces: $('bs-oz').value },
        gestation: { weeks: $('bs-ga-weeks').value, days: $('bs-ga-days').value },
        documentedSGA: radio('bs-sga'), documentedFGR: radio('bs-fgr'), nicuCare: radio('bs-nicu'),
        neonatalAKI: radio('bs-aki'), neonatalDialysis: radio('bs-dialysis'),
        congenitalKidneyUrinaryCondition: radio('bs-cakut'), majorCongenitalHeartCondition: radio('bs-cardiac'),
        clinicianIdentifiedCurrentConcern: radio('bs-concern'),
        sourceConfidence: $('bs-source').value || 'mixed-uncertain',
        confirmedUnusual: $('bs-confirm').checked
      };
    }
    function say(msg) { if (live) { live.textContent = ''; setTimeout(function () { live.textContent = msg; }, 30); } }
    var FIELD_IDS = { audience: 'bs-audience', weight: 'bs-weight', ounces: 'bs-oz', 'ga-weeks': 'bs-ga-weeks', 'ga-days': 'bs-ga-days' };

    function clearErrors() {
      errBox.hidden = true; errBox.innerHTML = '';
      form.querySelectorAll('.bs-field-err').forEach(function (n) { n.textContent = ''; });
      form.querySelectorAll('[aria-invalid]').forEach(function (n) { n.removeAttribute('aria-invalid'); });
      $('bs-confirm-wrap').hidden = true;
    }
    function showErrors(v, t) {
      var items = v.errors.concat(v.needsConfirm ? v.confirms : []);
      if (v.confirms.length) $('bs-confirm-wrap').hidden = false;
      items.forEach(function (e) {
        var id = FIELD_IDS[e.field], el = id && $(id), slot = $(id + '-err');
        if (el && v.errors.indexOf(e) >= 0) el.setAttribute('aria-invalid', 'true');
        if (slot) slot.textContent = t.E[e.code];
      });
      errBox.innerHTML = '<h4>' + esc(t.errHead) + '</h4><ul>' + items.map(function (e) {
        return '<li><a href="#' + (FIELD_IDS[e.field] || 'bs-form') + '">' + esc(t.E[e.code]) + '</a></li>';
      }).join('') + '</ul>';
      errBox.hidden = false; errBox.focus();
    }
    function render(sum) {
      var h = '<h3 class="bs-sum-title">' + esc(sum.title) + '</h3>';
      h += '<h4>' + esc(sum.headings.entered) + '</h4><dl class="bs-entered">';
      sum.entered.forEach(function (e) { h += '<dt>' + esc(e.label) + '</dt><dd>' + esc(e.value) + '</dd>'; });
      h += '</dl><h4>' + esc(sum.headings.records) + '</h4><ul>';
      sum.records.forEach(function (r) { h += '<li>' + esc(r) + '</li>'; });
      h += '</ul>' + (sum.recordsNote ? '<p class="bs-note">' + esc(sum.recordsNote) + '</p>' : '');
      h += '<h4>' + esc(sum.headings.questions) + '</h4><ol>';
      sum.questions.forEach(function (q) { h += '<li data-rule="' + esc(q.id) + '">' + esc(q.text) + '</li>'; });
      h += '</ol><h4>' + esc(sum.planHeading) + '</h4><div class="bs-plan">';
      sum.planLines.forEach(function (p) { h += '<div class="bs-plan-line"><span>' + esc(p) + '</span><span class="bs-blank"></span></div>'; });
      h += '</div><p class="bs-scope">' + esc(sum.scope) + '</p>';
      out.innerHTML = h; out.hidden = false;
      $('bs-actions').hidden = false;
      $('bs-fallback').hidden = true;
    }
    function generate() {
      var t = str(lang()), input = read();
      clearErrors();
      var v = validate(input);
      if (!v.ok) { invalidate(false); showErrors(v, t); return; }
      current = buildSummary(input, lang()); lastInput = input;
      render(current); say(t.done);
    }
    function invalidate(announce) {
      if (!current) return;
      current = null; lastInput = null;
      out.innerHTML = ''; out.hidden = true; $('bs-actions').hidden = true; $('bs-fallback').hidden = true;
      if (announce) say(str(lang()).stale);
    }
    function copy() {
      if (!current) return;
      var text = toPlainText(current), t = str(lang());
      var fb = $('bs-fallback'), ta = $('bs-fallback-text');
      function fallback() { ta.value = text; fb.hidden = false; ta.focus(); ta.select(); say(t.copyFail); }
      try {
        if (navigator.clipboard && navigator.clipboard.writeText)
          navigator.clipboard.writeText(text).then(function () { say(t.copied); }, fallback);
        else fallback();
      } catch (e) { fallback(); }
    }
    function printSummary(blank) {
      doc.body.setAttribute('data-print', blank ? 'planner-blank' : 'planner');
      window.print();
      setTimeout(function () { doc.body.removeAttribute('data-print'); }, 500);
    }
    function clearAll() {
      form.reset(); clearErrors(); current = null; lastInput = null;
      out.innerHTML = ''; out.hidden = true; $('bs-actions').hidden = true; $('bs-fallback').hidden = true;
      $('bs-fallback-text').value = '';
      toggleOz(); say(str(lang()).cleared);
    }
    function toggleOz() {
      var lb = $('bs-weight-unit').value === 'lb-oz';
      $('bs-oz-wrap').hidden = !lb;
      if (!lb) $('bs-oz').value = '';
    }

    form.addEventListener('submit', function (e) { e.preventDefault(); generate(); });
    form.addEventListener('input', function () { invalidate(true); });
    form.addEventListener('change', function () { invalidate(true); });
    $('bs-weight-unit').addEventListener('change', toggleOz);
    $('bs-copy').addEventListener('click', copy);
    $('bs-print').addEventListener('click', function () { printSummary(false); });
    $('bs-clear').addEventListener('click', clearAll);
    var pb = $('bs-print-blank'); if (pb) pb.addEventListener('click', function () { printSummary(true); });
    // <option> cannot hold language spans, so options carry data-en/tl/ceb/kap and are swapped here.
    function localizeOptions() {
      var l = lang();
      form.querySelectorAll('option[data-en]').forEach(function (o) { o.textContent = o.getAttribute('data-' + l) || o.getAttribute('data-en'); });
    }
    doc.querySelectorAll('.lang-btn-g').forEach(function (b) {
      b.addEventListener('click', function () {
        setTimeout(function () {
          localizeOptions();
          if (current && lastInput) { current = buildSummary(lastInput, lang()); render(current); }
        }, 0);
      });
    });
    localizeOptions();
    doc.querySelectorAll('.bs-js-only').forEach(function (n) { n.hidden = false; });
    toggleOz();
    return { generate: generate, clear: clearAll };
  }

  if (typeof document !== 'undefined') {
    var go = function () { mount(document); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
  }

  return { normalizeWeight: normalizeWeight, normalizeGestation: normalizeGestation, validate: validate,
    buildPrompts: buildPrompts, buildSummary: buildSummary, toPlainText: toPlainText, strings: S,
    RULE_ORDER: RULE_ORDER, LB_G: LB_G, OZ_G: OZ_G };
});
