# -*- coding: utf-8 -*-
# Module 15 expansion: the diseases (nephrotic, nephritic, lupus and vasculitis, diabetic and polycystic),
# kidney biopsy nursing, and immunosuppression safety. Sections attach after the base "bedside" section.
OBJECTIVES = [
    "Distinguish the main causes of nephrotic and nephritic presentations in children and adults, and recognize rapidly progressive glomerulonephritis as an emergency.",
    "Describe how lupus nephritis, antineutrophil cytoplasmic antibody vasculitis, diabetic kidney disease, and polycystic kidney disease affect the kidney, and the nurse's role in monitoring, teaching, and family referral.",
    "Prepare a patient for kidney biopsy, monitor afterward, and recognize and report bleeding.",
    "Monitor for the adverse effects of glucocorticoids, cyclophosphamide, mycophenolate, rituximab, and calcineurin inhibitors, and support infection prevention, vaccination, and contraception counseling.",
]
EXTRA = [
    {"after": "bedside", "id": "nephrotic", "nav": "Nephrotic diseases", "tag": "Nephrotic syndrome", "h2": "The diseases that make the filter leak, by age",
     "html": """
<p>Nephrotic syndrome is a pattern, not a diagnosis. The same swelling and foamy urine can come from very different diseases. The cause decides the treatment, the chance of relapse, and the risk to the kidney. Age is the first clue.</p>
<div class="table-wrap"><table><thead><tr><th>Disease</th><th>Who it typically affects</th><th>What injures the filter</th><th>Usual course</th></tr></thead><tbody>
<tr><td>Minimal change disease</td><td>Most children with nephrotic syndrome; a smaller share of adults</td><td>Podocyte foot processes flatten, probably from circulating immune factors. The biopsy looks almost normal under the light microscope</td><td>Usually responds to glucocorticoids, but relapses are common, often triggered by infections. Kidney function is usually preserved</td></tr>
<tr><td>Focal segmental glomerulosclerosis</td><td>Adults and some children; a pattern of scarring with several possible causes</td><td>Podocyte loss from a circulating factor, a genetic defect, a virus, a medicine, or overwork in a reduced number of nephrons (for example after severe obesity or loss of kidney mass)</td><td>Variable. The cause matters, because only some forms respond to immunosuppression. Can progress to kidney failure</td></tr>
<tr><td>Membranous nephropathy</td><td>Adults, more often middle-aged and older</td><td>Antibodies against a podocyte protein (most often the phospholipase A2 receptor) form deposits under the podocyte. Sometimes secondary to hepatitis B, lupus, cancer, or medicines</td><td>Some patients remit without immunosuppression. High clot risk when albumin is very low</td></tr>
<tr><td>Diabetic kidney disease</td><td>Adults with long-standing diabetes</td><td>Pressure and metabolic injury; thickened membrane and scarred glomeruli</td><td>Slow progression; covered later in this module and in Module 2</td></tr>
<tr><td>Lupus nephritis (membranous form)</td><td>Mostly young women</td><td>Immune deposits under the podocytes</td><td>Covered in the lupus section</td></tr>
<tr><td>Amyloidosis</td><td>Older adults, or people with long-standing inflammation</td><td>Abnormal protein fibrils are deposited in the glomerulus</td><td>Needs treatment of the underlying disorder; often involves the heart</td></tr>
</tbody></table></div>
<p><strong>Secondary causes the team looks for.</strong> Before calling a nephrotic syndrome a primary kidney disease, the physician looks for infections (hepatitis B, hepatitis C, human immunodeficiency virus, syphilis), cancers, medicines such as nonsteroidal anti-inflammatory drugs, and systemic diseases such as lupus and diabetes. The guideline advises testing for hepatitis B in proteinuric glomerular disease. It warns that some immunosuppressive drugs, such as cyclophosphamide and rituximab, can accelerate hepatitis B replication and should be avoided while it is active.[[gn2021]] That is why blood is drawn for viral tests before treatment starts, and why you check that the results are in the chart before the first dose.</p>
<p><strong>Children with nephrotic syndrome.</strong> Most children respond to a course of glucocorticoids, and many relapse. A relapse often starts with a cold or another infection. Many pediatric units teach families to test the first-morning urine at home with a dipstick and to keep a diary. Then a relapse is recognized when protein returns, before the swelling does. You teach how to read the strip, which result means &ldquo;call the clinic,&rdquo; and to bring the diary to every visit.[[gn2021]]</p>
<p>A child with nephrotic syndrome can be dangerously dry inside the blood vessels while looking swollen. Abdominal pain, cold hands and feet, a fast pulse, low urine output, or dizziness may mean the circulation is underfilled. Report them at once. A child with ascites, fever, and abdominal pain may have peritonitis, which also needs urgent review.</p>
<p><strong>Edema care.</strong> Swollen skin is fragile. Keep it clean and dry. Moisturize without rubbing. Check pressure areas. Elevate swollen legs when the patient sits, and support a swollen scrotum with a folded towel or a support garment. Avoid tight clothing, adhesive tape on swollen skin, and intramuscular injections into edematous tissue unless the order says otherwise. A cut or an insect bite on a swollen leg deserves attention, because cellulitis spreads quickly there.</p>
<p><strong>Nutrition.</strong> Patients often believe they must eat a lot of protein to &ldquo;replace what they lose.&rdquo; Very high protein intake adds to the work of the glomeruli and does not raise albumin in a meaningful way. The dietitian sets a normal, adequate protein intake. Salt restriction is the main dietary measure for edema, with fluid restriction only if ordered (Module 2 gives Filipino food examples). High lipids usually improve when proteinuria remits. The physician may add a statin when they persist.</p>
<p><strong>Remission and relapse, in words patients understand.</strong> &ldquo;Complete remission&rdquo; means the leak has nearly stopped and albumin has returned toward normal. &ldquo;Partial remission&rdquo; means the leak is much smaller but not gone. A &ldquo;relapse&rdquo; is the leak returning after a remission. &ldquo;Steroid-dependent&rdquo; means the disease relapses whenever glucocorticoids are reduced or stopped. &ldquo;Steroid-resistant&rdquo; means it did not respond to them. Both terms usually lead the physician to add another immunosuppressive medicine. Patients who hear these words on rounds are often frightened. A plain explanation from you helps them stay on treatment.</p>
<p><strong>In a child in remission, protein returning on the home dipstick is the earliest sign of relapse. Teach the family to read it, and to call before the swelling comes back.</strong></p>
"""},
    {"after": "nephrotic", "id": "nephritic", "nav": "Nephritic diseases", "tag": "Nephritic syndrome", "h2": "The diseases that make the filter bleed, and the emergency of rapid progression",
     "html": """
<p>In nephritic disease the glomerulus is inflamed. The speed of the inflammation matters more than its name. Some diseases cause a single episode that heals. Some smolder for decades. Some destroy kidney function in weeks.</p>
<div class="table-wrap"><table><thead><tr><th>Disease</th><th>Typical story</th><th>Course and treatment in outline</th></tr></thead><tbody>
<tr><td>Kidney disease after a streptococcal infection</td><td>A child or young adult develops dark urine, eyelid swelling, and high blood pressure one to several weeks after a sore throat or infected skin sores (for example infected scabies or impetigo). Complement levels are low</td><td>Usually heals in children with supportive care (salt and fluid control, blood pressure treatment). Adults and people with other illnesses recover less completely. Preventing and treating skin infection in the community is the real prevention</td></tr>
<tr><td>Immunoglobulin A nephropathy</td><td>Visible blood in the urine during or just after a throat or chest infection, or blood and protein found on a routine check. Young and middle-aged adults; common in East Asia</td><td>Many patients progress slowly over years. Treatment combines kidney-protective medicines with, for some patients, medicines that reduce the harmful antibody and immune-complex production[[igan2025]]</td></tr>
<tr><td>Immunoglobulin A vasculitis</td><td>Mostly children: a raised, purple rash on the legs and buttocks, joint pain, abdominal pain, and blood in the urine</td><td>Usually self-limiting in children. Urine and blood pressure are followed, because some develop lasting kidney disease</td></tr>
<tr><td>Lupus nephritis</td><td>Young women with rash, joint pain, mouth ulcers, fever, low blood counts</td><td>See the next section</td></tr>
<tr><td>Antineutrophil cytoplasmic antibody vasculitis</td><td>Older adults with weeks of fever, weight loss, joint pain, nasal crusting or bleeding, cough, or coughing blood</td><td>See the next section</td></tr>
<tr><td>Disease from antibodies against the glomerular basement membrane</td><td>Rapid kidney failure, sometimes with bleeding in the lungs; rare</td><td>An emergency, treated urgently with immunosuppression and usually plasma exchange</td></tr>
<tr><td>Kidney disease linked to infection elsewhere</td><td>Endocarditis, infected devices or shunts, hepatitis B or C</td><td>Treat the infection first. Immunosuppression may be harmful while it is active[[gn2021]]</td></tr>
</tbody></table></div>
<p><strong>Immunoglobulin A nephropathy in more detail.</strong> This is the most common glomerulonephritis in many parts of the world. The 2025 KDIGO update encourages a more liberal approach to kidney biopsy. It sets a stricter proteinuria goal than before: below 0.5 g per day and ideally below 0.3 g per day, with a stable eGFR.[[igan2025]] Proteinuria is a surrogate outcome here, a marker used because it tracks the risk of kidney failure. The update describes two aims.[[igan2025]]</p>
<ul>
<li>Reduce production of the harmful immunoglobulin A and its immune complexes. Current options are a targeted-release form of budesonide or reduced-dose systemic glucocorticoids, and, in Chinese patients, mycophenolate.</li>
<li>Manage the consequences of nephron loss: healthy lifestyle teaching, renin&ndash;angiotensin system inhibitors, sodium-glucose cotransporter-2 inhibitors, and dual endothelin and angiotensin receptor blockers.</li>
</ul>
<p>For you, this means a patient with immunoglobulin A nephropathy is often on several kidney-protective medicines at once, each with its own monitoring (Module 2). Proteinuria results are the main measure of whether treatment is working.</p>
<p><strong>Rapidly progressive glomerulonephritis: why hours and days matter.</strong> When inflammation fills the glomerular capsule with crescents, filtering units are destroyed and replaced by scar. Scarred glomeruli do not recover. The three main causes are antineutrophil cytoplasmic antibody vasculitis, antibodies against the glomerular basement membrane, and severe immune-complex disease such as lupus. The patient may have only a rising creatinine and blood in the urine. Or the patient may be critically ill with kidney failure and bleeding in the lungs, a combination called pulmonary&ndash;renal syndrome.</p>
<p>You often notice first. Report urgently:</p>
<ul>
<li>A creatinine that is higher on each daily result, or urine output that is falling.</li>
<li>Blood in the urine with a rising creatinine in a patient with fever, weight loss, rash, joint pain, or sinus symptoms.</li>
<li>Coughing blood, rising breathlessness, or falling oxygen saturation in a patient with kidney inflammation. Bleeding in the lungs can kill within hours.</li>
<li>Blood pressure rising sharply, with headache, confusion, or visual change.</li>
<li>Signs of fluid overload: crackles, raised neck veins, breathlessness lying flat.</li>
</ul>
<p><strong>Nursing in the first days.</strong> Within a short time these patients may need an urgent kidney biopsy, high-dose IV glucocorticoids, a first immunosuppressive infusion, plasma exchange through a dialysis-type catheter, and hemodialysis (HD). Help the team move fast and safely. Confirm that baseline blood tests, viral screening, and blood group are sent as ordered. Prepare access and equipment. Check blood glucose after high-dose glucocorticoids. Watch oxygen saturation and breathing closely. Keep an exact intake-and-output record. Explain to the family what is happening and why speed matters.</p>
<p>During plasma exchange, watch for tingling around the mouth and fingers (low calcium from citrate, as in Module 13), allergic reactions to replacement plasma, a drop in blood pressure, and bleeding. Follow the unit protocol. Some patients with advanced scarring remain on dialysis; others recover enough function to stop. That uncertainty is hard for families. Honest updates from the physician, supported by you, help.</p>
<p><strong>A creatinine that climbs every day, with blood in the urine, is an emergency until proven otherwise. Call the same hour, not on the next round.</strong></p>
"""},
    {"after": "nephritic", "id": "lupus-vasculitis", "nav": "Lupus and vasculitis", "tag": "Systemic disease", "h2": "Lupus nephritis and antineutrophil cytoplasmic antibody vasculitis",
     "html": """
<p>Both diseases are systemic. The kidney is one target of an immune disorder that can also affect skin, joints, lungs, nerves, and blood. Both are treated with glucocorticoids combined with stronger immunosuppressive medicines. Both relapse. You will meet these patients again and again over many years.</p>
<p><strong>Lupus nephritis.</strong> Systemic lupus erythematosus mainly affects women of childbearing age. Many people with lupus develop kidney involvement. It may show as protein in the urine, blood in the urine, high blood pressure, or a rising creatinine. Treatment depends on the type of glomerular injury, so a kidney biopsy is usually done. Pathologists grade lupus nephritis into classes: mild changes; proliferative (actively inflamed) forms that need strong treatment; a membranous (leaking) form; and finally advanced scarring. The 2024 KDIGO update gives this framework:[[ln2024]]</p>
<ul>
<li>Hydroxychloroquine is recommended for all patients with lupus nephritis unless there is a contraindication (grade 1C: strong recommendation, low-certainty evidence).</li>
<li>Active proliferative lupus nephritis (the two proliferative classes, with or without a membranous component) is treated first with glucocorticoids plus one of: a mycophenolic acid medicine; low-dose IV cyclophosphamide; belimumab combined with either of those; or a mycophenolic acid medicine combined with a calcineurin inhibitor when kidney function is not severely reduced (grade 1B: strong, moderate certainty).</li>
<li>Lower glucocorticoid doses than in the past may be as effective with fewer harms. Mycophenolic acid is the preferred agent for long-term treatment, which continues for years.</li>
<li>The membranous form is managed with renin&ndash;angiotensin system blockade, blood pressure control, and hydroxychloroquine. Immunosuppression is added for heavy, nephrotic-range proteinuria.</li>
<li>A poor response may come from missed doses or underdosing as well as from resistant disease. The first step the guideline names is to check adherence before calling treatment a failure.</li>
<li>Pregnancy should be avoided while lupus nephritis is active, while the patient takes medicines that can harm the fetus, and for at least six months after the disease becomes inactive. If kidney failure occurs, transplantation is preferred to long-term dialysis. These are practice points.</li>
</ul>
<p>The same update advises that hydroxychloroquine continue during pregnancy. It lists glucocorticoids, hydroxychloroquine, azathioprine, tacrolimus, and cyclosporine as immunosuppressive medicines considered safe in pregnancy.[[ln2024]] Mycophenolate and cyclophosphamide are not on that list. That is why contraception counseling is part of starting treatment (see the immunosuppression section).</p>
<p><strong>You and the patient with lupus.</strong> Many patients are young women in school or early in their careers. The treatment changes how they look (glucocorticoid weight gain, acne, hair loss), whether they can have children, and how often they miss work for infusions and tests. Cost is a constant pressure. Stopping medicines when they feel well is common. What you can do:</p>
<ul>
<li>Teach the warning signs of a flare: new swelling, foamy or dark urine, rising blood pressure on home readings, rash, joint pain, mouth ulcers, fever, unusual tiredness.</li>
<li>Ask at every visit about missed doses, and why. Cost, side effects, and fear about fertility are common reasons. Each has a solution the team can look for.</li>
<li>Teach sun protection, because sunlight can trigger flares.</li>
<li>Remind patients on hydroxychloroquine that regular eye checks, arranged by the physician, are part of safe long-term use.</li>
<li>Screen for low mood and anxiety, and refer to the physician or mental health services (Module 14).</li>
</ul>
<p><strong>Antineutrophil cytoplasmic antibody vasculitis.</strong> This disease mainly affects older adults. Antibodies against proteins inside neutrophils activate these white cells, which then inflame the walls of small blood vessels. In the kidney the result is often rapidly progressive glomerulonephritis. In the lung it causes cough, nodules, or bleeding. In the nose and sinuses it causes crusting, bleeding, or deformity. Elsewhere it causes rash, nerve damage, and weeks of fever and weight loss. Early on it is easily mistaken for infection.</p>
<p>The 2024 KDIGO update advises that waiting for a kidney biopsy to be done or reported should not delay starting treatment (a practice point).[[aav2024]] In outline, it advises:[[aav2024]]</p>
<ul>
<li>Initial treatment with glucocorticoids combined with rituximab or cyclophosphamide (grade 1B).</li>
<li>Avacopan, a newer oral medicine that blocks a complement receptor, as an option to reduce glucocorticoid exposure. Patients at high risk of glucocorticoid toxicity are likely to benefit most (practice point).</li>
<li>Glucocorticoids tapered faster than in older regimens. A lower-dose regimen was as effective in trials, with fewer harms.</li>
<li>Plasma exchange considered for selected patients, such as those with very severe kidney failure or bleeding in the lungs with low oxygen (practice point).</li>
<li>Maintenance treatment afterward with rituximab, or azathioprine with low-dose glucocorticoids (grade 1C). The best duration is not precisely known; the guideline places it between about 18 months and 4 years. Relapses are treated again, preferably with rituximab (practice points).</li>
</ul>
<p><strong>You and the patient with vasculitis.</strong> These patients are often older and frail, and already unwell from weeks of illness before diagnosis. Infection is one of the most serious threats in the first year of treatment. Watch oxygen saturation and breathing. Report coughing blood at once. Check glucose and blood pressure during high-dose glucocorticoids. Protect the skin and mobility of a weak patient. Make sure ordered preventive medicines and vaccinations are not missed. After discharge, the most important teaching is what relapse can look like (nasal crusting or bleeding, cough, rash, joint pain, blood or foam in the urine) and that infections must be reported early.</p>
<p><strong>In both diseases, the treatment that saves the kidney also opens the door to infection. Watch for both, at every contact.</strong></p>
"""},
    {"after": "lupus-vasculitis", "id": "diabetic-pkd", "nav": "Diabetic and cystic", "tag": "Systemic and inherited disease", "h2": "Diabetic kidney disease, when it may not be diabetic, and polycystic kidney disease",
     "html": """
<p><strong>Diabetic kidney disease: a slow glomerular injury.</strong> Diabetes, together with hypertension, accounts for most CKD in the Philippines. Module 2 covers the medicines and targets that slow it. Here the question is mechanism.</p>
<p>High blood sugar and high pressure inside the glomerulus work together. Early on, each nephron filters more than usual (hyperfiltration). Over years the basement membrane thickens, the supporting tissue between the capillaries expands, podocytes are lost, and glomeruli scar. Albumin leaks first in small amounts and later, in some patients, in nephrotic amounts. Filtration falls slowly. That is why medicines that lower glomerular pressure, such as renin&ndash;angiotensin system inhibitors and sodium-glucose cotransporter-2 inhibitors, protect the kidney (Module 2).[[ckd2024]]</p>
<p>The textbook picture needs two corrections. Some people with diabetes lose filtration with very little albumin in the urine, so a normal albumin result does not exclude diabetic kidney disease. And heavy proteinuria or steady progression do not by themselves prove another disease, because both occur in ordinary diabetic kidney disease.</p>
<p><strong>When the kidney disease may not be diabetic.</strong> A person with diabetes can also develop any disease in this module, and some of those are treatable. Physicians become suspicious when the story does not fit the usual slow course. You see the urine results, the blood pressure trend, and the patient more often than anyone. You are well placed to notice and report:</p>
<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Why it raises the question</th></tr></thead><tbody>
<tr><td>Blood in the urine, especially with red-cell casts or dysmorphic red cells</td><td>Diabetic kidney disease rarely causes an active, bleeding urine; this suggests glomerulonephritis</td></tr>
<tr><td>A rapid fall in eGFR, or AKI without a clear cause</td><td>Diabetic kidney disease usually declines slowly over years</td></tr>
<tr><td>Sudden heavy proteinuria or a sudden nephrotic syndrome</td><td>A leak that appears quickly may have another cause, such as membranous nephropathy or minimal change disease</td></tr>
<tr><td>Kidney disease early in the course of diabetes</td><td>Diabetic injury usually takes years to develop, although type 2 diabetes is often diagnosed late</td></tr>
<tr><td>No diabetic eye disease</td><td>Useful mainly in type 1 diabetes; in type 2 diabetes its absence does not exclude diabetic kidney disease</td></tr>
<tr><td>Rash, joint pain, fever, weight loss, sinus or lung symptoms</td><td>Suggest a systemic disease such as lupus or vasculitis</td></tr>
</tbody></table></div>
<p>A kidney biopsy may then show diabetic disease alone, another disease alone, or both. The decision to investigate belongs to the physician. Your part is to see that the finding is reported, not filed as &ldquo;expected in a diabetic.&rdquo;</p>
<p><strong>Polycystic kidney disease.</strong> Autosomal dominant polycystic kidney disease is the most common inherited kidney disease. Fluid-filled cysts grow from the tubules over decades. The kidneys enlarge, and kidney function usually falls in middle age, at a speed that varies widely. It is not a glomerular disease. It belongs here because it is a systemic, inherited cause of kidney failure that you will meet in every clinic and dialysis unit. Each child of an affected parent has a one-in-two chance of inheriting the gene.</p>
<p>The 2025 KDIGO guideline, the first on this disease, gives you several practical anchors:[[adpkd2025]]</p>
<ul>
<li><strong>Blood pressure</strong> often rises early, before kidney function falls. The guideline sets tighter targets for younger adults with preserved function than for the general CKD population, using home measurement where possible. Children of affected parents are advised to have yearly standardized blood pressure checks from early school age.</li>
<li><strong>Water intake:</strong> a high water intake is recommended for people with early and moderate CKD from this disease, to prevent dehydration and reduce stone risk.</li>
<li><strong>Slowing progression:</strong> tolvaptan, a medicine that blocks the kidney&rsquo;s response to antidiuretic hormone, is recommended for adults at risk of rapid progression whose eGFR is not too low and who have no contraindication. It causes thirst and large urine volumes. It can injure the liver, so liver tests are checked on a strict schedule, and the medicine is held at once if liver enzymes rise. You check that the scheduled tests are done. Teach the patient to report yellow eyes, dark urine, unusual tiredness, or right-sided abdominal pain.</li>
<li><strong>Complications:</strong> pain from enlarging cysts; visible blood in the urine when a cyst bleeds; cyst infection, treated with a longer antibiotic course than an ordinary urinary infection; and kidney stones. Patients with very large kidneys or liver are advised to avoid contact and collision sports.</li>
<li><strong>Brain aneurysm:</strong> screening for intracranial aneurysms is recommended for people with a personal or family history of aneurysm or bleeding around the brain, or a family history of unexplained sudden death. Stopping smoking and controlling blood pressure are critical for everyone. Teach that a sudden, severe headache is an emergency.</li>
<li><strong>Pregnancy and medicines:</strong> medicines that can harm the fetus, such as tolvaptan and renin&ndash;angiotensin system inhibitors, are stopped before conception, and genetic counseling is offered.</li>
</ul>
<p><strong>Family screening: your role.</strong> The guideline recommends ultrasound as the usual first screening test for at-risk adults. Genetic testing with a panel of known cystic disease genes is used when the answer is unclear. Testing of adults should be patient-centered, with counseling about what a positive or a negative result would mean. For at-risk children, the family and the physician weigh the benefits and harms of screening together.[[adpkd2025]] In practice you can:</p>
<ol>
<li>Draw a simple family tree with the patient, marking relatives with kidney disease, dialysis, transplants, brain hemorrhage, or early death.</li>
<li>Explain the one-in-two inheritance in plain words. A relative who carries the gene can still benefit from early blood pressure control and kidney protection.</li>
<li>Offer blood pressure checks to relatives who come to clinic, and refer interested adult relatives to the physician to discuss screening.</li>
<li>Respect that some adults choose not to be tested, and that the result can affect employment, insurance, and family plans. Keep the patient&rsquo;s results confidential from relatives unless the patient agrees.</li>
<li>Remind parents that children of affected parents need their blood pressure checked, even if the family has decided not to test them yet.</li>
</ol>
<p><strong>In a patient with diabetes, an active urine sediment or a fast fall in filtration is never &ldquo;just diabetes&rdquo; until a physician has looked. Report it.</strong></p>
"""},
    {"after": "diabetic-pkd", "id": "biopsy", "nav": "Kidney biopsy", "tag": "Procedure nursing", "h2": "Kidney biopsy: nursing care before, during, and after",
     "html": """
<p>A kidney biopsy removes a few thin cores of kidney tissue with a needle. A pathologist examines the glomeruli under the light microscope, with immune stains, and by electron microscopy. The guideline calls it the gold standard for diagnosing glomerular disease.[[gn2021]] Most biopsies of a patient&rsquo;s own kidneys are done through the skin of the back under ultrasound guidance, with the patient lying face down. A transplanted kidney is biopsied through the front of the abdomen, with the patient on the back. Patients with a high bleeding risk may need a different route, decided by the physician.</p>
<p>The main risk is bleeding. The kidney receives a large share of the cardiac output, and the needle passes through a very vascular organ. Most bleeds are small and stop by themselves. A few need transfusion, a procedure to block the bleeding vessel, or, rarely, surgery. Your preparation and observation keep the small bleeds small and catch the large ones early.</p>
<p><strong>Before the biopsy.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Check</th><th>Why it matters</th></tr></thead><tbody>
<tr><td>Consent obtained by the physician and signed; the patient can explain in their own words why the biopsy is done and what the risks are</td><td>Informed consent is the physician&rsquo;s duty. You confirm it is present and valid, and call the physician if the patient is unsure or has new questions</td></tr>
<tr><td>Identity, procedure, and side (or transplant kidney) confirmed against the order</td><td>Standard procedural safety</td></tr>
<tr><td>Medication history: anticoagulants, antiplatelet medicines, nonsteroidal anti-inflammatory drugs, and herbal or food supplements that affect bleeding</td><td>These are stopped or adjusted only by order and protocol, often days in advance. A missed instruction can mean a cancelled or unsafe biopsy</td></tr>
<tr><td>Blood count, platelet count, clotting tests, blood group and crossmatch, as the protocol requires; results reviewed before the procedure</td><td>Low platelets or abnormal clotting raise bleeding risk. Blood must be available if needed</td></tr>
<tr><td>Blood pressure within the target set by the physician</td><td>High blood pressure increases bleeding. Report a high reading before the patient goes to the procedure</td></tr>
<tr><td>Kidney function and the dialysis plan</td><td>High urea impairs platelet function, and the physician may order a medicine to improve it. A patient on HD may need a session without heparin before and after, by order</td></tr>
<tr><td>Fasting, IV access, and pregnancy testing for women of childbearing age, per protocol</td><td>Preparation for sedation, fluids, or emergency treatment</td></tr>
<tr><td>Teaching: lying face down, holding the breath on command, staying still, and what bed rest will mean afterward</td><td>Movement and breathing move the kidney. A patient who knows what to expect cooperates better</td></tr>
<tr><td>Empty bladder before the procedure</td><td>Comfort during bed rest; easier observation of the first urine afterward</td></tr>
</tbody></table></div>
<p><strong>During the biopsy.</strong> Position the patient as the operator directs, usually face down with a pillow or rolled towel under the abdomen to push the kidney toward the back. Monitor vital signs and comfort, coach breath-holding, and reassure. Handle specimens exactly as the pathology protocol requires: the correct container or medium for each examination, correct labels, and prompt delivery. A lost or mishandled core may mean repeating the whole procedure.</p>
<p><strong>After the biopsy.</strong></p>
<ul>
<li>Apply pressure and a dressing as directed. Turn the patient onto the back if ordered, which also presses on the site.</li>
<li>Keep the patient on bed rest for the period in the protocol, then mobilize gradually.</li>
<li>Check blood pressure, pulse, the dressing, and pain at the intervals in the protocol, more often in the first hours. Compare with the pre-biopsy baseline, not with normal values.</li>
<li>Look at every void. Save it or describe its color. Some blood-tinged urine is common at first. Report increasing redness, clots, or difficulty passing urine.</li>
<li>Encourage fluids if allowed, and give pain relief as ordered. Avoid nonsteroidal anti-inflammatory drugs unless the physician orders them.</li>
<li>Check hemoglobin as ordered, and report a fall.</li>
<li>Anticoagulant and antiplatelet medicines restart only when the physician says so.</li>
</ul>
<p><strong>What to report at once.</strong> A falling blood pressure or rising pulse. Increasing pain in the flank, back, abdomen, or groin. Swelling or a growing bruise at the site. Heavy blood or clots in the urine, or inability to pass urine, since clots can block the bladder. Dizziness, pallor, sweating, or restlessness. A falling hemoglobin. These may be signs of bleeding that needs urgent imaging and treatment. In practice, most serious bleeding shows itself early, which is why observation is most intense in the first hours. Delayed bleeding can occur, so discharge teaching matters.</p>
<p><strong>Discharge teaching.</strong> Avoid heavy lifting, strenuous exercise, and contact sports for the period the unit advises. Take only the pain relievers the physician allows. Return at once for heavy blood in the urine, clots, inability to pass urine, increasing pain, dizziness, or fainting. Know when and how the results will be explained. Results can take days, and waiting is stressful; tell the patient when to expect them.</p>
<p><strong>After a biopsy, compare every reading with the patient&rsquo;s own baseline. A pulse that climbs while the pressure drifts down is bleeding until proven otherwise.</strong></p>
"""},
    {"after": "biopsy", "id": "immunosuppression", "nav": "Immunosuppression safety", "tag": "Medicine safety", "h2": "Glucocorticoids and immunosuppressive medicines: what the nurse watches",
     "html": """
<p>The medicines that control glomerular inflammation work by damping the immune system. Their benefit and their main danger come from the same action. Module 11 covers the immunosuppressants used after transplantation, and several are the same drugs. This section is about what you check, teach, and report. Doses, timing, and changes are always set by the physician&rsquo;s order and the protocol. You never start, stop, or adjust them, but you may hold a dose and call when the protocol says so.</p>
<div class="table-wrap"><table><thead><tr><th>Medicine</th><th>How it works, in brief</th><th>What you watch and teach</th></tr></thead><tbody>
<tr><td>Glucocorticoids (prednisone, methylprednisolone)</td><td>Broadly suppress inflammation and immune cells</td><td>Blood glucose (high readings often in the afternoon), blood pressure and fluid retention, mood change, sleeplessness, and confusion, infection with blunted fever, stomach pain or black stools, muscle weakness, bone loss, weight gain and changes in appearance, eye problems with long use. Take with food as ordered. Never stop suddenly after more than a short course, because the body&rsquo;s own cortisol production is suppressed</td></tr>
<tr><td>Cyclophosphamide (IV pulses or tablets)</td><td>Kills rapidly dividing immune cells</td><td>Blood count before each dose as ordered; report low white cells. Bladder irritation and bleeding, which is why fluids, frequent voiding, and any protective medicine are given exactly as ordered. Nausea and hair loss. Harm to fertility and to the fetus. Handle as a hazardous drug under the hospital&rsquo;s policy for gloves, spills, and body fluids</td></tr>
<tr><td>Mycophenolate (mycophenolate mofetil or mycophenolic acid)</td><td>Blocks the multiplication of lymphocytes</td><td>Diarrhea, nausea, abdominal pain; low white cells and anemia on blood counts; infection. Causes birth defects and miscarriage: confirm the patient has had contraception counseling before starting and understands that pregnancy must be planned with the physician</td></tr>
<tr><td>Rituximab (IV infusion)</td><td>An antibody that removes B cells, the cells that make antibodies</td><td>Infusion reactions, especially with the first dose: fever, chills, rash, itching, throat tightness, breathlessness, low blood pressure. Give ordered premedication, run the infusion at the protocol rate, check vital signs as the protocol requires, and stop and call per protocol if a reaction occurs. Hepatitis B screening must be done beforehand, because the virus can reactivate. Vaccines given after rituximab work poorly, so vaccination is best completed before</td></tr>
<tr><td>Calcineurin inhibitors (tacrolimus, cyclosporine, voclosporin)</td><td>Block the signals that activate T cells; also stabilize podocytes</td><td>Blood levels drawn at the time ordered (usually just before a dose). Rising creatinine, because these drugs narrow the vessels into the glomerulus. Blood pressure; potassium, magnesium, and glucose; tremor. Many drug interactions, including some antibiotics and antifungals, and grapefruit or pomelo (suha), which may raise blood levels. Report any new medicine started by another doctor</td></tr>
<tr><td>Hydroxychloroquine (in lupus)</td><td>Modulates immune signaling</td><td>Usually well tolerated; long-term eye checks as arranged by the physician</td></tr>
</tbody></table></div>
<p><strong>Before treatment starts: the safety checklist.</strong> Many harms of immunosuppression are prevented by steps taken before the first dose. Check that each one has been addressed, or deliberately decided against by the physician:</p>
<ul>
<li><strong>Infection screening</strong> for tuberculosis, hepatitis B, and hepatitis C as clinically appropriate, with results in the chart.[[gn2021]]</li>
<li><strong>Vaccination:</strong> pneumococcal vaccination is advised for patients with glomerular disease and nephrotic syndrome.[[gn2021]] Influenza and hepatitis B vaccination are commonly part of kidney care. Vaccines work best before immunosuppression, especially before rituximab. Live vaccines are generally avoided during strong immunosuppression. The physician decides which vaccines and when.</li>
<li><strong>Pneumocystis prophylaxis:</strong> preventive trimethoprim&ndash;sulfamethoxazole should be considered for patients on high-dose glucocorticoids.[[gn2021]] When it is ordered, give it as ordered and watch potassium and creatinine, because trimethoprim can raise both. The creatinine rise is partly from blocked secretion, not kidney injury (Module 1).</li>
<li><strong>Pregnancy and contraception:</strong> confirm whether a woman of childbearing age could be pregnant. See that she is referred for contraception counseling before mycophenolate or cyclophosphamide. The guideline ties pregnancy planning in lupus nephritis to disease activity and medicine choice.[[ln2024]]</li>
<li><strong>Fertility:</strong> before cyclophosphamide, make sure the patient has had the chance to discuss its effects on fertility, and options to protect it, with the physician.</li>
<li><strong>Bone and stomach protection</strong> during long glucocorticoid courses, as ordered.</li>
<li><strong>Baseline measurements:</strong> weight, blood pressure, glucose, blood count, and kidney and liver tests, so later changes can be recognized.</li>
</ul>
<p><strong>Teaching for life on immunosuppression.</strong></p>
<ul>
<li>Report fever, chills, cough, painful urination, skin redness, diarrhea, or mouth sores early. Tell every health worker that you take immunosuppressive medicines. Fever may be absent even in serious infection.</li>
<li>Wash hands often. Avoid close contact with people who have chickenpox, measles, or influenza. Eat well-cooked food and drink clean water.</li>
<li>Take medicines at the same time every day, with a written schedule and a pillbox. Do not stop or change a medicine without the physician. Do not start herbal products or new medicines without asking.</li>
<li>Check blood glucose and blood pressure at home if advised, and bring the record.</li>
<li>Plan any pregnancy with the physician, and use the contraception agreed during counseling.</li>
<li>Keep every blood-test appointment. For many of these medicines, the blood count or drug level decides the next dose.</li>
</ul>
<p><strong>Cost and continuity.</strong> In the Philippines many of these medicines, especially the biological ones, are expensive. They may be paid out of pocket or through hospital or government assistance programs. A patient who runs out of mycophenolate or misses a rituximab infusion because of cost is at risk of relapse. Ask about supply at each visit. Involve the social worker early. Tell the physician when cost is affecting treatment, so the plan can be adjusted openly rather than abandoned quietly.</p>
<p><strong>Before the first dose, ask four questions: are the viral screens back, are the vaccines done, could she be pregnant, and can the family afford the next month?</strong></p>
"""},
]
QUIZ = [
    {"stem": "A 68-year-old woman has had fever, weight loss, and nasal crusting with bloody discharge for six weeks. On admission her creatinine is higher than at her clinic visit a month ago, the dipstick shows blood and protein, and overnight her creatinine has risen again. This morning she coughs up streaks of blood. What is the most important nursing action?",
     "options": [
         ("Record the findings and report them on the routine ward round later this morning", False, "A rapidly rising creatinine with blood in the urine and coughing blood suggests rapidly progressive glomerulonephritis with lung bleeding. Waiting for the round delays treatment that protects the kidneys and lungs."),
         ("Call the physician now with SBAR, check oxygen saturation and breathing, and prepare for urgent investigations", True, "This picture fits antineutrophil cytoplasmic antibody vasculitis with kidney and lung involvement. Kidney function and lung bleeding can worsen within hours to days, so immediate escalation and close respiratory monitoring are needed."),
         ("Encourage oral fluids, because the rising creatinine is probably from dehydration after weeks of fever", False, "Dehydration does not explain blood in the urine and coughing blood. Extra fluid may also worsen breathing if the kidneys are failing."),
         ("Start a urine collection for 24-hour protein so that the result is ready for the physician", False, "Measuring protein is not the priority while the patient may be bleeding into the lungs and losing kidney function quickly."),
     ],
     "objective": "Distinguish the main causes of nephrotic and nephritic presentations in children and adults, and recognize rapidly progressive glomerulonephritis as an emergency.",
     "sources": ["aav2024"], "flag": ""},
    {"stem": "A 7-year-old with steroid-sensitive nephrotic syndrome has been in remission for two months. His mother has been testing his first-morning urine at home. Which finding should she be taught to report to the clinic?",
     "options": [
         ("A negative protein result on most mornings with an occasional trace", False, "Trace or negative results on most mornings fit remission. Units set the exact rule, but this pattern is not a relapse."),
         ("Protein returning on the dipstick for several consecutive mornings, especially during a cold", True, "Persistent proteinuria on home testing, often triggered by an infection, signals relapse before the swelling returns, so the clinic can act early."),
         ("Darker urine after a hot day when he drank less water", False, "Concentrated urine after less fluid is expected and is not, on its own, a sign of relapse."),
         ("Urine that is pale and plentiful after drinking more water", False, "Dilute urine after more fluid is normal."),
     ],
     "objective": "Distinguish the main causes of nephrotic and nephritic presentations in children and adults, and recognize rapidly progressive glomerulonephritis as an emergency.",
     "sources": ["gn2021"], "flag": "The number of consecutive positive readings that defines relapse is set by the unit protocol."},
    {"stem": "A 34-year-old man with type 2 diabetes for three years attends the CKD clinic. His eGFR was stable last year but has fallen markedly over two months, and today's urinalysis shows red cells, with red-cell casts reported on microscopy. He had no diabetic eye disease at his last examination. What should you do?",
     "options": [
         ("Document the result as expected in a patient with diabetes, and reinforce glucose control", False, "Red-cell casts and a rapid fall in eGFR are not typical of diabetic kidney disease. Filing them as expected may delay the diagnosis of a treatable disease."),
         ("Report the findings to the physician, noting the rapid eGFR fall, the active urine sediment, and the short duration of diabetes", True, "These features suggest a glomerular disease other than, or in addition to, diabetic kidney disease. The physician decides on investigation, which may include a kidney biopsy."),
         ("Advise the patient to stop his renin&ndash;angiotensin system inhibitor because it is lowering the eGFR", False, "Nurses do not stop medicines, and an active, bleeding urine is not explained by the medicine."),
         ("Repeat the urinalysis in a year at his next routine check", False, "A rapid change with an active sediment needs prompt review, not routine follow-up."),
     ],
     "objective": "Describe how lupus nephritis, antineutrophil cytoplasmic antibody vasculitis, diabetic kidney disease, and polycystic kidney disease affect the kidney, and the nurse's role in monitoring, teaching, and family referral.",
     "sources": ["ckd2024"], "flag": ""},
    {"stem": "Four hours after a percutaneous biopsy of her own kidney, a patient's pulse has risen from 78 to 110, her blood pressure has fallen from 132/84 to 102/64, and she reports increasing back pain. Her last void was pink with small clots. What should you do first?",
     "options": [
         ("Give the ordered pain relief and recheck the vital signs at the next scheduled time", False, "Pain relief is appropriate, but a rising pulse, a falling blood pressure, and increasing pain suggest significant bleeding that needs urgent review, not routine observation."),
         ("Encourage her to walk to the toilet to help pass the clots", False, "Mobilizing a patient who may be bleeding can worsen bleeding and risks fainting. She stays on bed rest."),
         ("Call the physician immediately, keep her on bed rest, monitor vital signs closely, and prepare for blood tests and IV access per protocol", True, "These are signs of post-biopsy bleeding. Immediate escalation allows urgent hemoglobin, imaging, transfusion, or a procedure to stop the bleeding, as the physician decides."),
         ("Restart her usual aspirin, since the biopsy is over", False, "Antiplatelet medicines restart only when the physician says so, and certainly not while bleeding is suspected."),
     ],
     "objective": "Prepare a patient for kidney biopsy, monitor afterward, and recognize and report bleeding.",
     "sources": ["gn2021"], "flag": "Observation intervals and bed-rest duration follow the unit protocol."},
    {"stem": "Ten minutes into her first rituximab infusion for membranous nephropathy, a patient develops chills, an itchy rash, and throat tightness. Her blood pressure has dropped from her baseline. What should you do?",
     "options": [
         ("Slow the infusion slightly and recheck in 30 minutes, since reactions are common with the first dose", False, "Throat tightness and a falling blood pressure are signs of a significant reaction. The protocol response is to stop the infusion and call, not to continue at a slower rate."),
         ("Stop the infusion, keep the IV line open per protocol, assess airway, breathing, and circulation, and call the physician", True, "Infusion reactions are most common with the first dose. Stopping the infusion, supporting the airway and circulation, and following the reaction protocol come first. Whether and how to restart is the physician's decision."),
         ("Complete the infusion quickly so that the patient receives the full dose before the reaction worsens", False, "Speeding the infusion would worsen the reaction."),
         ("Give an extra dose of glucocorticoid from the ward stock without an order", False, "Medicines for a reaction are given according to the protocol or an order, not improvised from stock."),
     ],
     "objective": "Monitor for the adverse effects of glucocorticoids, cyclophosphamide, mycophenolate, rituximab, and calcineurin inhibitors, and support infection prevention, vaccination, and contraception counseling.",
     "sources": ["gn2021"], "flag": "Premedication, infusion rates, and the reaction algorithm follow the hospital's rituximab protocol."},
]
TERMS = [
    ("Minimal change disease", "A cause of nephrotic syndrome, most common in children, in which the biopsy looks almost normal under the light microscope; usually responds to glucocorticoids."),
    ("Focal segmental glomerulosclerosis", "A pattern of scarring in parts of some glomeruli, caused by podocyte loss from several possible causes."),
    ("Membranous nephropathy", "A cause of nephrotic syndrome in adults in which antibodies against a podocyte protein form deposits under the podocytes."),
    ("Immunoglobulin A nephropathy", "Glomerulonephritis caused by deposits containing immunoglobulin A; often shows as blood in the urine during or after an infection."),
    ("Rapidly progressive glomerulonephritis", "Glomerular inflammation with many crescents that can destroy kidney function within weeks; a medical emergency."),
    ("Lupus nephritis", "Kidney inflammation caused by systemic lupus erythematosus, graded by biopsy class."),
    ("Antineutrophil cytoplasmic antibody vasculitis", "Inflammation of small blood vessels driven by antibodies that activate neutrophils; often affects the kidney, lungs, and nose."),
    ("Pulmonary&ndash;renal syndrome", "Glomerulonephritis together with bleeding in the lungs."),
    ("Plasma exchange", "Removal of the patient&rsquo;s plasma, with its harmful antibodies, and replacement with albumin solution or donor plasma."),
    ("Autosomal dominant polycystic kidney disease", "An inherited disease in which cysts enlarge the kidneys; each child of an affected parent has a one-in-two chance of inheriting it."),
    ("Infusion reaction", "Fever, chills, rash, breathlessness, or low blood pressure during or soon after an infusion of a biological medicine such as rituximab."),
    ("Trough level", "The blood level of a medicine measured just before the next dose; used to adjust calcineurin inhibitors."),
    ("Pneumocystis pneumonia", "A lung infection caused by a fungus that mainly affects people on strong immunosuppression; often prevented with trimethoprim&ndash;sulfamethoxazole."),
]
FLAGS = [
    "Lupus nephritis (2024) and antineutrophil cytoplasmic antibody vasculitis (2024) statements were checked against the full guideline texts in the November 2026 rewrite. Grades stated: lupus Rec 10.2.1.1 hydroxychloroquine 1C; Rec 10.2.3.1.1 initial Class III/IV therapy 1B; vasculitis Rec 9.3.1.1 initial therapy 1B; Rec 9.3.2.1 maintenance 1C. Ungraded practice points labeled as such: lupus 10.3.2.1 (avoid pregnancy while active, on teratogenic drugs, and for at least six months after inactivity), 10.3.2.2 and 10.3.2.3 (hydroxychloroquine in pregnancy; pregnancy-safe agents), 10.3.4.1 (transplant preferred); vasculitis 9.1.1 (do not delay treatment for biopsy), 9.3.1.7 (avacopan), 9.3.1.9 (plasma exchange), 9.3.2.2 (maintenance 18 months to 4 years), 9.3.3.1 (relapse, preferably rituximab).",
    "Pregnancy-safe agents in lupus updated in the rewrite from the 2021 list ('calcineurin inhibitors') to the 2024 list (glucocorticoids, hydroxychloroquine, azathioprine, tacrolimus, cyclosporine; PP 10.3.2.3), and the citation moved from gn2021 to ln2024 accordingly.",
    "Lupus membranous class: earlier text said immunosuppression 'considered for some patients'; the 2024 guideline (Figure 10) adds combined immunosuppression for nephrotic-range proteinuria. Text updated.",
    "Vasculitis: earlier text said 'a compatible illness with a positive antibody test supports starting treatment'; replaced with the verified practice point that waiting for biopsy should not delay treatment.",
    "Immunoglobulin A nephropathy (2025) and polycystic kidney disease (2025) statements come from executive summaries and KDIGO 'top takeaways' documents; no grades are stated. Proteinuria goal (below 0.5 g per day, ideally below 0.3 g per day) is from the abstract of the 2025 executive summary (PMID 40975525).",
    "The lupus calcineurin inhibitor eGFR cut-off is described qualitatively ('when kidney function is not severely reduced'); the long-term treatment duration (at least 36 months, PP 10.2.3.2.4) is described as 'continues for years'. The plasma exchange creatinine threshold is deliberately not quoted.",
    "Polycystic kidney disease: blood pressure targets, water intake volume, and tolvaptan liver-test schedule are described qualitatively; numbers available in KDIGO 2025 if a reviewer wants them stated.",
    "Red flags for non-diabetic kidney disease in diabetes are drawn from clinical practice and the site guide diabetes-kidney-disease-not-always-diabetic.html; no guideline citation is attached to that table.",
    "Post-streptococcal glomerulonephritis, immunoglobulin A vasculitis, amyloidosis, and focal segmental glomerulosclerosis descriptions are general clinical knowledge, not cited.",
    "Kidney biopsy nursing (consent, bleeding-risk checks, positioning, observation, discharge advice) is general practice; observation intervals, bed-rest duration, activity restriction, and hemoglobin check timing are left to the unit protocol. The earlier uncited claim that most serious bleeding appears 'within the first day' was softened to 'shows itself early'; consider adding a biopsy-complication reference.",
    "Immunosuppressant adverse-effect table is general pharmacology without a single cited source; pomelo interaction is stated with 'may'. Consider adding a drug reference. Live-vaccine advice is stated generally and deferred to the physician.",
    "Hazardous-drug handling for cyclophosphamide defers to hospital policy.",
]
NEW_REFS = {
    "gn2021": "34556256",
    "ln2024": "38182286",
    "aav2024": "38388102",
    "igan2025": "40975525",
    "adpkd2025": "39848746",
}
