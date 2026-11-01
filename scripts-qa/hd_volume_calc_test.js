// Tests the in-guide HD volume calculators (guides/hd-volume-bp-tolerance-clinician.html).
// Usage: node scripts-qa/hd_volume_calc_test.js   (exits 1 on any failure)
const fs=require('fs'),path=require('path'),vm=require('vm');
const html=fs.readFileSync(path.join(__dirname,'..','guides','hd-volume-bp-tolerance-clinician.html'),'utf8');
const m=html.match(/<script>\s*(\/\* HDV-CALC[\s\S]*?)<\/script>/);if(!m){console.error('HDV-CALC block not found');process.exit(1);}
const sandbox={module:{exports:{}}};vm.runInNewContext(m[1],sandbox);const H=sandbox.module.exports;
const V=require('./hd-volume-calculator-test-vectors.json');
let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
const tol=1e-9;
for(const c of V.cases){
  const r=H[c.calculator]({...c.inputs});
  if(c.error){ok(r.error===c.error,c.id+' expected '+c.error+' got '+JSON.stringify(r));continue;}
  for(const [k,v] of Object.entries(c.expected)){
    const t = (c.id.startsWith('ufr-round')) ? 1e-9 : tol;
    ok(Math.abs(r[k]-v)<=t,c.id+' '+k+' '+r[k]+' vs '+v);
  }
}
// properties
ok(JSON.stringify(H.ufr({ufVolumeMl:1000,treatmentMinutes:240,postWeightKg:70}))===JSON.stringify(H.ufr({ufVolumeMl:1*1000,treatmentMinutes:240,postWeightKg:70})),'L=mL');
ok(Math.abs(H.ufr({ufVolumeMl:3000,treatmentMinutes:240,postWeightKg:70}).hours-4)<tol,'240min=4h');
let prev=Infinity;for(let m=120;m<=600;m+=15){const x=H.ufr({ufVolumeMl:3000,treatmentMinutes:m,postWeightKg:70}).mlPerKgPerHour;ok(x<prev,'monotone time '+m);prev=x;}
prev=-1;for(let v=0;v<=6000;v+=250){const x=H.ufr({ufVolumeMl:v,treatmentMinutes:240,postWeightKg:70}).mlPerKgPerHour;ok(x>prev,'monotone vol '+v);prev=x;}
ok(H.ufr({ufVolumeMl:3639.72,treatmentMinutes:240,postWeightKg:70}).comparison==='below','12.999 below');
ok(H.ufr({ufVolumeMl:3640,treatmentMinutes:240,postWeightKg:70}).comparison==='at','13 at');
ok(H.ufr({ufVolumeMl:3640.28,treatmentMinutes:240,postWeightKg:70}).comparison==='above','13.001 above');
ok(H.ufr({ufVolumeMl:NaN,treatmentMinutes:240,postWeightKg:70}).error==='MISSING_VOLUME','empty volume');
ok(H.ufr({ufVolumeMl:Infinity,treatmentMinutes:240,postWeightKg:70}).error==='NEGATIVE_VOLUME','nonfinite rejected');
ok(H.ufr({ufVolumeMl:3000,treatmentMinutes:240,postWeightKg:70,treatmentMode:'delivered',weightBasis:'target'}).notes.length>0,'mode/basis label');
ok(H.ufr({ufVolumeMl:0,treatmentMinutes:240,postWeightKg:70}).notes.some(n=>/No inference about dialysis adequacy or safety/.test(n)),'zero msg');
const i=H.idwg({preWeightKg:72.5,previousActualPostWeightKg:70,targetWeightKg:65});ok(Math.abs(i.idwgKg-2.5)<tol,'idwg independent of target');
ok(H.idwg({preWeightKg:69,previousActualPostWeightKg:70}).notes[0].includes('not an order to give fluid'),'neg idwg msg');
ok(H.idwg({preWeightKg:72,previousActualPostWeightKg:null}).error==='MISSING_PREVIOUS_ACTUAL_POST_WEIGHT','no target substitution');
for(const [pre,post,inp,out] of [[73,70,500,200],[80.4,77.9,0,0],[61.2,60,350,120]]){const b=H.plannedBalance({preWeightKg:pre,intendedPostWeightKg:post,inputsMl:inp,nonUfOutputsMl:out});ok(Math.abs(b.predictedPostWeightKg-post)<1e-9,'roundtrip '+pre);}
ok(H.plannedBalance({preWeightKg:69.5,intendedPostWeightKg:70,inputsMl:100,nonUfOutputsMl:0}).notes[0].includes('No replacement-fluid'),'neg balance msg');
ok(H.timeComparison({ufVolumeMl:3000,weightKg:70,comparisonRate:10}).roundedUp15===270,'roundup');
ok(H.timeComparison({ufVolumeMl:3150,weightKg:70,comparisonRate:10}).roundedUp15===270,'exact 270 not 285');
ok(H.timeComparison({ufVolumeMl:3000,weightKg:70,comparisonRate:null}).error==='MISSING_COMPARISON_RATE','no default rate');
console.log('pass',pass,'fail',fail);process.exit(fail?1:0);
