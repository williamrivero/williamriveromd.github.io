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
 for(const sel of html.matchAll(/<select\b[^>]*id=["']([^"']+)["'][^>]*>([\s\S]*?)<\/select>/g)){
  if(sel[1]==='a-dialysis'){const options=[...sel[2].matchAll(/<option\b[^>]*value=["']([^"']*)["']/g)].map(m=>m[1]);assert.equal(new Set(options).size,options.length,page+' duplicate population option');checks++;}
 }
 for(const [id,value]of Object.entries(values)){assert(nodes[id],page+' missing input '+id);if(typeof value==='boolean')nodes[id].checked=value;else nodes[id].value=value;}
 const document={getElementById:id=>nodes[id]||null};
 const match=html.match(new RegExp('function '+fn+'\\([^)]*\\)\\s*\\{[\\s\\S]*?^\\}','m'));assert(match,page+' missing '+fn);
 vm.runInNewContext(match[0]+';'+fn+'();',{document,CKDAnemia2026:A,console});checks++;
 return read.map(id=>{assert(nodes[id],page+' missing output '+id);return nodes[id].textContent||nodes[id].innerHTML});
}
for(const page of ['calc-iron-deficit-ganzoni','understanding-iron'])for(const si of [false,true])eq(ui(page,'calcIron',{'ir-wt':60,'ir-hgb':si?80:8,'ir-target':si?110:11,'ir-stores':500,'ir-route':'iv'},['ir-deficit-val','ir-sessions-val'],si),[932,10]);
for(const page of ['calc-esa-dose-adjustment','esa-dose-cancer-risk']){
 eq(ui(page,'calcESA',{'esa-agent':'epoetin','esa-hgb':11.5,'esa-delta':0,'esa-dose':6000,'esa-weeks':4},['esa-action-val']),['REDUCE / REVIEW']);
 eq(ui(page,'calcESAInit',{'init-agent':'epoetin','init-hgb':9.5,'init-weight':60,'init-setting':'nondialysis'},['init-decision-val']),['INDIVIDUALIZE']);
}
for(const page of ['anemia-management','calc-iron-status-tsat','esa-dose-cancer-risk'])eq(ui(page,'calcAnemia',{'a-dialysis':'ckd','a-si':70,'a-tibc':200,'a-ferritin':80},['a-type-val']),['CONSIDER IRON']);
eq(ui('calc-iv-iron-dose','calcIVIron',{'iron-setting':'nd','iron-tsat':35,'iron-ferritin':80},['iron-decision-val']),['CONSIDER IRON']);
for(const page of ['anemia-management','calc-eri'])eq(ui(page,'calcERI',{'eri-esa-type':'cera','eri-dose':50,'eri-freq':0.25,'eri-weight':60,'eri-hgb':10},['eri-val']),['Not converted']);
ui('anemia-management','updateChecklist',{'chk-hgb':11.5,'chk-tsat':40,'chk-fer':701,'chk-esa-type':'none'},['chk-hgb-status','chk-tsat-status','chk-fer-status']);
eq(A.ganzoni({weight:60,actual:80,target:110,unit:'g/dL'}),null);
eq(A.iron({setting:'pd',ferritin:300,tsat:24}).action,'REASSESS');
eq(A.iron({setting:'hd',ferritin:700,tsat:39,ongoing:true}).action,'REVIEW MAINTENANCE');
eq(A.lab({key:'tsat',value:110,ferritin:200}).status,'FLAG');
eq(A.lab({key:'hgb',value:110,age:12}).status,'WATCH');
const changedExtra=require('child_process').execFileSync('git',['diff','--name-only'],{cwd:root,encoding:'utf8'}).trim().split('\n').filter(x=>x.endsWith('.html'));
const changed=[...new Set(['anemia-management','calc-eri','calc-esa-dose-adjustment','calc-iron-deficit-ganzoni','calc-iron-status-tsat','calc-iv-iron-dose','calc-reticulocyte-rpi','calc-transfusion-hgb','esa-dose-cancer-risk','epo-resistant-renal-anemia','understanding-iron','lab-interpreter-guide','medication-operational-guide','practical-outpatient-algorithms'].map(n=>'guides/'+n+'.html').concat(changedExtra))];
for(const file of changed){const html=fs.readFileSync(path.join(root,file),'utf8');for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)){if(!/application\/ld\+json/.test(m[1]))new vm.Script(m[2],{filename:file});}checks++;}
// Re-audit additions (Nov 6, 2026): profound iron deficiency, transplant extension, TSAT entry check, nutrition calculators, stale-threshold lint.
eq(A.iron({setting:'nd',ferritin:20,tsat:10}).profound,true);
eq(/Profound iron deficiency/.test(A.iron({setting:'hd',ferritin:25,tsat:15}).detail),true);
eq(A.iron({setting:'nd',ferritin:30,tsat:19}).profound,false);
eq(/extension/.test(A.iron({setting:'transplant',ferritin:80,tsat:20}).detail),true);
eq(/extension/.test(A.iron({setting:'nd',ferritin:80,tsat:20}).detail),false);
eq(ui('calc-iron-status-tsat','calcAnemia',{'a-dialysis':'hd','a-si':300,'a-tibc':250,'a-ferritin':200},['a-type-val']),['CHECK ENTRY']);
eq(ui('calc-iv-iron-dose','calcIVIron',{'iron-setting':'transplant','iron-tsat':20,'iron-ferritin':80},['iron-decision-val']),['CONSIDER IRON']);
eq(ui('calc-iv-iron-dose','calcIVIron',{'iron-setting':'hd','iron-tsat':25,'iron-ferritin':600},['iron-decision-val']),['REASSESS']);
for(const page of ['calc-ckd-nutrition-rx','ckd-dri-calculator']){
 const html=fs.readFileSync(path.join(root,'guides',page+'.html'),'utf8');
 assert(/stage==='HD'\)\{ feTarget='IV iron preferred'; feNote='[^']*ferritin &le;500 ng\/mL and TSAT &le;30%/.test(html),page+' HD iron rule');checks++;
 assert(/stage==='PD'\)\{ feTarget='Oral or IV iron'/.test(html),page+' PD iron rule');checks++;
 assert(!/TSAT 20–40%|ferritin &lt;100 or TSAT &lt;20%/.test(html),page+' stale iron targets');checks++;
}
// Stale thresholds must not reappear anywhere in guides or downloads.
const stale=[/\(target\s*[−-]\s*actual[^)]*\)\s*×\s*0\.24\s*\+\s*500/i,/Target: ferritin 200–500, TSAT 20–40%/,/ferritin (?:&gt;|>)\s?800 (?:or|o) TSAT/,/ferritin (?:&gt;|>)\s?800 n(?:in)?g\/mL, TSAT (?:&gt;|>)50%/,/KDIGO 2024 (?:CKD Anemia|iron targets|\(anemia)/,/Hgb\) 100–115 g\/L \(KDIGO 2024\)/,/TSAT 30–50%/,/and its 2024 update/,/Population-specific reference<\/a>\.<\/p>/];
for(const dir of ['guides','downloads'])for(const file of fs.readdirSync(path.join(root,dir)).filter(f=>f.endsWith('.html'))){
 const html=fs.readFileSync(path.join(root,dir,file),'utf8');for(const re of stale)assert(!re.test(html),`${dir}/${file} contains stale iron text ${re}`);checks++;
}
// Iron-tool pages keep exactly one full KDIGO table (in Evidence), not one per accordion.
for(const page of ['calc-iron-deficit-ganzoni','calc-iron-status-tsat','calc-iv-iron-dose']){const html=fs.readFileSync(path.join(root,'guides',page+'.html'),'utf8');eq([page,(html.match(/<td>Withhold routine iron<\/td>/g)||[]).length],[page,1]);}
console.log(`${checks} checks passed: thresholds, unit equivalence, invalid inputs, ESA timing, lab interpretation, embedded UI, and script syntax.`);
