const assert=require('node:assert/strict');const fs=require('node:fs');const vm=require('node:vm');const path=require('node:path');
const root=path.resolve(__dirname,'..');const A=require('../assets/ckd-anemia-2026.js');let checks=0;
function eq(a,b){assert.deepEqual(a,b);checks++;}
for(const unit of ['g/dL','g/L'])eq(A.ganzoni({weight:60,actual:unit==='g/L'?80:8,target:unit==='g/L'?110:11,unit}),932);
eq(A.ganzoni({weight:60,actual:8,target:11,stores:0}),432);
for(const arg of [{weight:0,actual:8,target:11},{weight:-1,actual:8,target:11},{weight:60,actual:8,target:8},{weight:60,actual:8,target:11,stores:-1},{weight:60,actual:NaN,target:11}])eq(A.ganzoni(arg),null);
for(const [setting,ferritin,tsat,action] of [
 ['hd',500,30,'CONSIDER IRON'],['hd',501,30,'REASSESS'],['hd',500,30.1,'REASSESS'],
 ['nd',99,39.9,'CONSIDER IRON'],['nd',100,24.9,'CONSIDER IRON'],['nd',299,24.9,'CONSIDER IRON'],['nd',300,24.9,'REASSESS'],['nd',100,25,'REASSESS'],['nd',80,35,'CONSIDER IRON'],
 ['pd',80,35,'CONSIDER IRON'],['transplant',200,24,'CONSIDER IRON'],['hd',700,39.9,'REASSESS'],['hd',700.1,20,'WITHHOLD'],['hd',300,40,'WITHHOLD'],['nd',80,40,'WITHHOLD'],['hd',-1,20,'INVALID'],['hd',100,101,'INVALID']])eq(A.iron({setting,ferritin,tsat}).action,action);
eq(A.iron({setting:'hd',ferritin:600,tsat:20,ongoing:true}).action,'REVIEW MAINTENANCE');
eq(A.iron({setting:'hd',ferritin:300,tsat:40,ongoing:true}).action,'WITHHOLD');
eq(A.iron({setting:'hd',ferritin:200,tsat:20,infection:true}).action,'PAUSE');
eq(A.esa({hb:11.5,change:0,dose:6000,weeks:4}).action,'REDUCE / REVIEW');
eq(A.esa({hb:9.5,change:0,dose:6000,weeks:2}).action,'WAIT / REVIEW');
eq(A.esa({hb:9.5,change:0,dose:6000,weeks:4}).action,'REVIEW RESPONSE');
eq(A.esa({hb:10,change:1.1,dose:6000,weeks:2}).dose,4500);
eq(A.esa({hb:9,change:-1.1,dose:6000,weeks:4}).action,'EVALUATE FALL');
eq(A.initiation({setting:'nd',hb:9}).action,'INDIVIDUALIZE');
eq(A.initiation({setting:'dialysis',hb:10}).action,'CONSIDER ESA');
eq(A.lab({key:'hgb',value:110,sex:'M'}).status,'FLAG');
eq(A.lab({key:'hgb',value:120,sex:'F',onESA:true}).status,'WATCH');
eq(A.lab({key:'tsat',value:45,ferritin:300,setting:'hd'}).status,'FLAG');
eq(A.lab({key:'ferritin',value:750,tsat:20,setting:'nd'}).status,'FLAG');
function ui(page,fn,values,read,si=false){
 const html=fs.readFileSync(path.join(root,'guides',page+'.html'),'utf8');const nodes={};for(const m of html.matchAll(/\bid=["']([^"']+)["']/g))nodes[m[1]]={value:'',checked:false,style:{},textContent:'',innerHTML:'',classList:{contains:()=>si}};
 for(const [id,value]of Object.entries(values)){assert(nodes[id],page+' missing input '+id);if(typeof value==='boolean')nodes[id].checked=value;else nodes[id].value=value;}
 const document={getElementById:id=>nodes[id]||null};
 const match=html.match(new RegExp('function '+fn+'\\([^)]*\\)\\s*\\{[\\s\\S]*?^\\}','m'));assert(match,page+' missing '+fn);
 vm.runInNewContext(match[0]+';'+fn+'();',{document,CKDAnemia2026:A,console});checks++;
 return read.map(id=>{assert(nodes[id],page+' missing output '+id);return nodes[id].textContent||nodes[id].innerHTML});
}
for(const page of ['calc-iron-deficit-ganzoni','understanding-iron'])for(const si of [false,true])eq(ui(page,'calcIron',{'ir-wt':60,'ir-hgb':si?80:8,'ir-target':si?110:11,'ir-stores':500,'ir-route':'iv'},['ir-deficit-val','ir-sessions-val'],si),[932,10]);
for(const page of ['calc-esa-dose-adjustment','esa-dose-cancer-risk']){
 eq(ui(page,'calcESA',{'esa-agent':'epoetin','esa-hgb':11.5,'esa-delta':0,'esa-dose':6000,'esa-weeks':4},['esa-action-val']),['REDUCE / REVIEW']);
 eq(ui(page,'calcESAInit',{'init-agent':'epoetin','init-hgb':9.5,'init-weight':60,'init-setting':'nd'},['init-decision-val']),['INDIVIDUALIZE']);
}
for(const page of ['anemia-management','calc-iron-status-tsat','esa-dose-cancer-risk'])eq(ui(page,'calcAnemia',{'a-dialysis':'ckd','a-si':70,'a-tibc':200,'a-ferritin':80},['a-type-val']),['CONSIDER IRON']);
eq(ui('calc-iv-iron-dose','calcIVIron',{'iron-setting':'nd','iron-tsat':35,'iron-ferritin':80},['iron-decision-val']),['CONSIDER IRON']);
for(const page of ['anemia-management','calc-eri'])eq(ui(page,'calcERI',{'eri-esa-type':'cera','eri-dose':50,'eri-freq':0.25,'eri-weight':60,'eri-hgb':10},['eri-val']),['Not converted']);
ui('anemia-management','updateChecklist',{'chk-hgb':11.5,'chk-tsat':40,'chk-fer':701,'chk-esa-type':'none'},['chk-hgb-status','chk-tsat-status','chk-fer-status']);
const changedExtra=require('child_process').execFileSync('git',['diff','--name-only'],{cwd:root,encoding:'utf8'}).trim().split('\n').filter(x=>x.endsWith('.html'));
const changed=[...new Set(['anemia-management','calc-eri','calc-esa-dose-adjustment','calc-iron-deficit-ganzoni','calc-iron-status-tsat','calc-iv-iron-dose','calc-reticulocyte-rpi','calc-transfusion-hgb','esa-dose-cancer-risk','epo-resistant-renal-anemia','understanding-iron','lab-interpreter-guide','medication-operational-guide','practical-outpatient-algorithms'].map(n=>'guides/'+n+'.html').concat(changedExtra))];
for(const file of changed){const html=fs.readFileSync(path.join(root,file),'utf8');for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)){if(!/application\/ld\+json/.test(m[1]))new vm.Script(m[2],{filename:file});}checks++;}
console.log(`${checks} checks passed: thresholds, unit equivalence, invalid inputs, ESA timing, lab interpretation, embedded UI, and script syntax.`);
