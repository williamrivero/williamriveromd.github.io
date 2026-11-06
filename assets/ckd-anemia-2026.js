/* KDIGO 2026 Anemia in CKD: shared adult decision support.
 * Recommendations 2.1–2.4, 3.2.1–3.3.1; practice points 2.2, 2.5, 2.7–2.8,
 * 3.4.1.2–3.4.3.5. Product labels and clinical judgment remain necessary.
 */
(function (root) {
  'use strict';
  const finite = x => Number.isFinite(x);
  function iron({setting, tsat, ferritin, ongoing=false, infection=false}) {
    if (!['hd','nd','pd','transplant'].includes(setting) || !finite(tsat) || tsat<0 || tsat>100 || !finite(ferritin) || ferritin<0) return {action:'INVALID', detail:'Enter a valid adult population, TSAT 0–100%, and nonnegative ferritin.'};
    const monitor=setting==='hd'?'Check Hb, ferritin, and TSAT every 1–3 months (often monthly in HD), sooner with blood loss, hospitalization, or ESA changes.':'Check Hb, ferritin, and TSAT every 3 months during iron treatment, sooner when clinically indicated.';
    if(infection) return {action:'PAUSE', detail:'Consider temporarily suspending iron during systemic infection. Evaluate the infection and reassess before restarting. Inflammation alone does not establish infection or iron overload.',monitor};
    if(ferritin>700 || tsat>=40) return {action:'WITHHOLD',detail:'Withhold routine iron: ferritin >700 ng/mL or TSAT ≥40%. Assess trends and clinical context; an elevated ferritin alone does not diagnose iron overload.',monitor};
    const eligible=setting==='hd' ? ferritin<=500 && tsat<=30 : (ferritin<100 && tsat<40)||(ferritin>=100 && ferritin<300 && tsat<25);
    const route=setting==='hd'?'IV iron is suggested; use a proactive, monitored regimen and the formulation’s dosing limits.':'Oral or IV iron may be chosen according to severity, response, tolerance, preference, availability, and cost. Switch an optimal oral regimen to IV if ineffective after 1–3 months or poorly tolerated.';
    const profound=ferritin<30 && tsat<20;
    const profoundNote=profound?' Profound iron deficiency (ferritin <30 ng/mL and TSAT <20%): even without anemia, KDIGO 2026 suggests considering oral or IV iron, especially with symptoms.':'';
    const extension=setting==='transplant'?' Kidney transplant recipients: KDIGO 2026 applies the non-dialysis criteria (Appendix Figure 4); monitor phosphate after iron preparations that raise FGF23.':'';
    if(ongoing) return {action:'REVIEW MAINTENANCE',eligible,profound,detail:'No routine laboratory withhold threshold is met. Review the current regimen against Hb and iron trends, blood loss, response, and tolerance; this is not an automatic instruction to continue or increase iron. '+route+extension,monitor};
    return eligible?{action:'CONSIDER IRON',eligible,profound,detail:'If anemia is present, these results meet KDIGO 2026 suggested iron-initiation criteria. '+route+profoundNote+extension,monitor}:{action:'REASSESS',eligible,profound,detail:'The suggested iron-initiation criteria are not met. This does not establish adequate iron, iron overload, or a mandatory stop to an existing regimen. Investigate persistent anemia and individualize further management.'+extension,monitor};
  }
  function ganzoni({weight,actual,target,unit='g/dL',stores=500}) {
    if(!['g/dL','g/L'].includes(unit)||![weight,actual,target,stores].every(finite)||weight<=0||actual<=0||target<=actual||stores<0) return null;
    const scale=unit==='g/L'?10:1;
    if(actual/scale>25 || target/scale>25) return null;
    const gap=(target-actual)/scale;
    return Math.round((weight*gap*2.4+stores)*100)/100;
  }
  function esa({hb,change,dose,weeks}) {
    if(![hb,change,dose,weeks].every(finite)||hb<=0||dose<=0||weeks<0) return {action:'REVIEW',detail:'Enter Hb, its change over 2–4 weeks, the current dose, and weeks since the last dose change.'};
    if(hb>=11.5) return {action:'REDUCE / REVIEW',dose:dose*0.75,detail:'Adult ESA maintenance targets should be below 11.5 g/dL. Review a dose reduction; if Hb is above the target, a temporary hold may be appropriate under the product label or local protocol. Monitor Hb in 2–4 weeks.'};
    if(change>1) return {action:'REDUCE',dose:dose*0.75,detail:'Hb rose >1 g/dL in 2–4 weeks. Reduce ESA by 25–50%; the displayed dose illustrates a 25% reduction. Recheck Hb in 2–4 weeks.'};
    if(change < -1) return {action:'EVALUATE FALL',detail:'Evaluate blood loss, hemolysis, illness, iron availability, and transfusion need. A rapid decline should not automatically trigger an ESA increase.'};
    if(hb>=11 && change>0) return {action:'REVIEW REDUCTION',dose:dose*0.75,detail:'Hb is approaching 11.5 g/dL and rising. Review a preventive reduction under the selected protocol; 25% is an example, not a universal KDIGO dose rule.'};
    if(hb<10 && change<0.5) return weeks<4?{action:'WAIT / REVIEW',dose,detail:'Avoid routine dose adjustments more often than every 4 weeks. Review symptoms and reversible causes; recheck Hb in 2–4 weeks.'}:{action:'REVIEW RESPONSE',detail:'Hb remains low after at least 4 weeks. Check iron, inflammation, bleeding, adherence, dialysis adequacy, and other causes before deciding whether a product-specific dose increase is appropriate. Do not repeatedly escalate without evaluating hyporesponsiveness.'};
    return {action:'MAINTAIN / REVIEW',dose,detail:'Use the lowest dose that achieves the individualized goal below 11.5 g/dL. Recheck Hb in 2–4 weeks after initiation or adjustment; during maintenance monitor at least every 3 months, usually more often in HD.'};
  }
  function initiation({setting,hb}) {
    if(!['dialysis','nd'].includes(setting)||!finite(hb)||hb<=0) return {action:'REVIEW',detail:'Select the adult dialysis setting and enter a valid Hb.'};
    return setting==='dialysis'?{action:hb<=10?'CONSIDER ESA':'USUALLY DEFER',detail:'For HD or PD, KDIGO suggests ESA initiation when Hb is ≤9–10 g/dL after correcting reversible causes. Select the threshold within that range using symptoms, risks, and preferences; this result is not an automatic start order.'}:{action:'INDIVIDUALIZE',detail:'For non-dialysis CKD, including transplant recipients, there is no single automatic Hb <10 initiation rule. Weigh anemia symptoms, transfusion avoidance, ESA harms, and patient preferences after correcting reversible causes.'};
  }
  function lab({key,value,sex='M',age,onESA=false,setting='nd',ferritin,tsat}) {
    if(!finite(value)||value<0) return {status:'FLAG',note:'Enter a valid nonnegative result.'};
    if(finite(age)&&age<18) return {status:'WATCH',note:'Pediatric anemia and iron interpretation require age-specific specialist assessment; adult treatment criteria are not applied.'};
    if(key==='tsat'&&value>100) return {status:'FLAG',note:'TSAT must be between 0 and 100%; check the entry and units.'};
    if(key==='hgb') {
      const anemia=value<(sex==='F'?120:130);
      return {status:anemia?'FLAG':onESA&&value>=115?'WATCH':'NORMAL',note:(anemia?'Below the adult sex-specific anemia threshold; evaluate the cause. ':'Not below the adult sex-specific anemia threshold. ')+(onESA?(value>=115?'On ESA: Hb is at/above the maintenance ceiling; review dose and trend. ':'On ESA: individualize the goal below 115 g/L. '):'Anemia diagnosis is separate from an ESA treatment goal. ')+(value<70?'Prompt clinical assessment is needed; transfusion depends on symptoms, signs, and urgency. ':'')};
    }
    const r=iron({setting,tsat:key==='tsat'?value:tsat,ferritin:key==='ferritin'?value:ferritin});
    if((key==='tsat'&&value>=40)||(key==='ferritin'&&value>700)) return {status:'FLAG',note:'KDIGO 2026: withhold routine iron and review the combined ferritin/TSAT results and clinical context. A high ferritin alone does not diagnose iron overload.'};
    if(r.action==='INVALID') return {status:'WATCH',note:'Interpret ferritin and TSAT together. Neither an isolated value nor a general laboratory range establishes CKD iron-treatment eligibility.'};
    return {status:'WATCH',note:r.detail};
  }
  const api={iron,ganzoni,esa,initiation,lab};root.CKDAnemia2026=api;if(typeof module!=='undefined'&&module.exports)module.exports=api;
})(typeof globalThis!=='undefined'?globalThis:this);
