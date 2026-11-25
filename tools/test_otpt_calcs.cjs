// Tests for the Renal Rehabilitation Toolkit core (node tools/test_otpt_calcs.cjs).
const fs=require('fs');const s=fs.readFileSync(require('path').join(__dirname,'techcourses','otpt','toolkit','script.html'),'utf8');
const core=s.split('/* ===== OTPT-CALC-CORE')[1].split('/* ===== END')[0];
const m={exports:{}};new Function('module',"/*"+core+"\nmodule.exports=OTPT;")(m);const O=m.exports;
const a=O.sixMW('m',64,165,68,290);console.log(a.pred.toFixed(1),a.pct.toFixed(1));
console.log(O.sixMW('f',60,155,60,400));
console.log(O.sppb(10,10,4,5.9,17.5));
console.log(O.sppb(10,10,10,4.5,11),O.sppb(5,0,0,0,0),O.sppb(10,5,0,9,70));
console.log(O.stsChange('sts60',12,15),O.stsChange('sts5',20.5,18.2));
console.log(O.weekly(3,20,3,15));
console.log(O.screen({red:false,newSym:false,sbp:150,sbps:125,lo:100,hi:180,drop:20}));
console.log(O.screen({red:false,newSym:false,sbp:NaN,sbps:NaN,lo:NaN,hi:NaN,drop:NaN}));

const assert=require('assert');
assert(Math.abs(a.pred-499.09)<0.1);assert(O.sppb(10,10,4,5.9,17.5).total===7);
assert(O.sppb(10,10,10,4.5,11).total===12);assert(O.screen({red:true}).decision==='stop');
console.log('OTPT calc tests passed');
