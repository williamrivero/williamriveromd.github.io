# -*- coding: utf-8 -*-
# Module 13 expansion, part 3: therapeutic plasma exchange. Sections follow the HDF expansion (m13_x2.py).
OBJECTIVES = [
    "Explain what therapeutic plasma exchange removes and why, how centrifugal and membrane separation differ in principle, how the American Society for Apheresis categorizes indications, and when albumin or plasma is used as replacement fluid.",
    "Prepare for and monitor a plasma exchange session, recognize citrate-related low calcium, low blood pressure (BP), allergic reactions to plasma, and bleeding, and coordinate medicine timing, reporting each finding per order.",
]
EXTRA = [
    {"after": "hdf-unit", "id": "tpe-principles", "nav": "Plasma exchange", "tag": "Plasma exchange",
     "h2": "Therapeutic plasma exchange: removing what no dialyzer can",
     "html": """
<p>Everything in this module so far has used a membrane that keeps proteins in the blood. Continuous renal replacement therapy (CRRT) and hemodiafiltration (HDF) remove water, small solutes, and middle molecules, but they are built to hold back albumin and the large proteins of the immune system. Some diseases are driven by exactly those large proteins: an antibody that attacks nerve, muscle, or kidney; an abnormal protein that thickens the blood; or the absence of a protein that the blood needs. For these, a different idea is used. Therapeutic plasma exchange removes the patient&rsquo;s plasma itself, with everything dissolved in it, and replaces it with a fluid that does not contain the harmful substance.</p>
<p><strong>The plain model.</strong> Imagine a pot of soup with something spoiled dissolved in it. Straining the soup keeps the vegetables (the blood cells) but does not remove the spoiled taste. Plasma exchange instead ladles out broth, returns the vegetables, and tops up the pot with clean broth. Because the clean broth mixes with what remains, each ladle removes a little less of the spoiled substance than the one before, so a session removes most, but not all, of it. Substances that also sit outside the bloodstream, in the tissues, move back into the blood between sessions. This is why plasma exchange is usually given as a course of several sessions, and why it is combined with medicines that stop the body making more of the harmful substance: plasma exchange buys time, and the other treatments act on the source.</p>
<p><strong>What it removes.</strong> Antibodies and immune complexes, abnormal proteins made by some blood cancers, some lipoproteins, and some toxins bound to proteins. It also removes useful things: clotting factors, some medicines, and, if the replacement fluid lacks them, normal antibodies.</p>
<p><strong>How the plasma is separated, in principle</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Centrifugal separation</th><th>Membrane separation</th></tr></thead>
<tbody>
<tr><td>How it works</td><td>Blood is spun; the heavier cells settle outward and the lighter plasma is drawn off by density</td><td>Blood passes through a plasma filter whose pores let proteins through but hold back blood cells</td></tr>
<tr><td>Machine</td><td>A dedicated apheresis machine, often run by a blood bank or hematology service</td><td>A plasma filter on a machine able to run it, which in some hospitals is a CRRT or dialysis platform</td></tr>
<tr><td>Blood flow and access</td><td>Can often work with lower blood flows, sometimes through large peripheral veins</td><td>Usually needs higher blood flow, so a central double-lumen catheter is common</td></tr>
<tr><td>Usual anticoagulant</td><td>Citrate, mixed into the blood as it leaves the patient</td><td>Heparin or citrate, by order</td></tr>
</tbody></table></div>
<p>Neither method has been shown to be better for patients in general; the choice depends on the equipment and service available, the access, and the patient. Both are recognized in the current international guideline.[[asfa2023]]</p>
<p><strong>When it is used: the guideline categories.</strong> The American Society for Apheresis publishes evidence-based fact sheets for each disease in which apheresis has been studied. The ninth edition, published in 2023, contains 91 fact sheets and 166 graded indications.[[asfa2023]] Each indication is placed in one of four categories, which the nurse should understand because they explain why plasma exchange is urgent in one patient and debated in another:</p>
<div class="table-wrap"><table>
<thead><tr><th>Category</th><th>Meaning, in our words</th><th>Examples for plasma exchange in the 2023 edition</th></tr></thead>
<tbody>
<tr><td>I</td><td>Accepted as first-line treatment, alone or with other treatments</td><td>Thrombotic thrombocytopenic purpura; acute Guillain-Barr&eacute; syndrome; short-term treatment of a myasthenia gravis crisis; anti-glomerular basement membrane disease with lung bleeding or while the kidneys still work; symptomatic hyperviscosity from very high antibody levels</td></tr>
<tr><td>II</td><td>Accepted as second-line treatment, alone or with other treatments</td><td>Long-term treatment of myasthenia gravis</td></tr>
<tr><td>III</td><td>Best role not established; the decision is made for the individual patient</td><td>Microscopic polyangiitis and granulomatosis with polyangiitis; anti-glomerular basement membrane disease in a patient already dialysis-dependent without lung bleeding</td></tr>
<tr><td>IV</td><td>Evidence shows or suggests that apheresis is ineffective or harmful</td><td>Thrombotic microangiopathy caused by the drugs gemcitabine or quinine</td></tr>
</tbody></table></div>
<p>Source for the table: the 2023 guideline.[[asfa2023]] Categories change between editions as new trials appear; the decision to treat, the number of sessions, and the volume exchanged belong to the physician and the apheresis service.</p>
<p><strong>Replacement fluid, in principle.</strong> The removed plasma must be replaced, or the patient would lose blood volume and protein. The two main choices are:</p>
<ul>
<li><strong>Albumin solution</strong> keeps the blood volume and oncotic pressure stable and carries little risk of allergic reaction or infection, and no blood-group matching is needed. It contains no clotting factors and no antibodies, so after repeated daily sessions the patient&rsquo;s clotting factors, especially fibrinogen, may fall, and normal antibody levels fall too.</li>
<li><strong>Plasma</strong> from donors contains clotting factors and the full range of normal plasma proteins. It is chosen when the patient needs what plasma supplies, for example in thrombotic thrombocytopenic purpura, where the patient lacks an enzyme that donor plasma replaces, or when bleeding risk is high. It must be matched by blood group, it carries the allergic and transfusion risks of any blood product, and it contains citrate from the blood bank, which adds to the citrate load.</li>
</ul>
<p>Some prescriptions combine the two. The fluid type is part of the order and is checked like a blood product or an intravenous (IV) medicine, which it is.</p>
"""},
    {"after": "tpe-principles", "id": "tpe-nursing", "nav": "Plasma exchange care", "tag": "Clinical application",
     "h2": "Nursing care during plasma exchange",
     "html": """
<p>Plasma exchange is done in an intensive care unit (ICU), a ward, or an apheresis or dialysis unit, depending on how sick the patient is and which service runs the machine. The nurse who looks after the patient may be the apheresis nurse running the machine or the ward or ICU nurse caring for the patient alongside. In either role the same safety rules apply: verify the order, watch the patient more than the machine, recognize the predictable complications early, and report per order and protocol.</p>
<p><strong>Before the session</strong></p>
<ul>
<li><strong>Order and consent.</strong> Check the order: method, volume to be exchanged, replacement fluid and its amount, anticoagulant, number and spacing of sessions, and any laboratory tests before or after. Confirm that consent has been obtained per hospital policy.</li>
<li><strong>Replacement fluid.</strong> Albumin bottles and plasma units are checked against the order and, for plasma, against the patient&rsquo;s identity and blood group with a second person, following the hospital&rsquo;s transfusion procedure.</li>
<li><strong>Baseline.</strong> Record vital signs, weight, symptoms, and the neurological or other findings that the treatment is meant to improve, so that change can be measured. Check that ordered baseline results, such as calcium, blood count, and clotting tests, are available.</li>
<li><strong>Access.</strong> Assess the catheter or peripheral veins. A central catheter is handled with the same aseptic care as a dialysis catheter (Module 7), and its lumens are locked per order after use.</li>
<li><strong>Medicine timing.</strong> Plasma exchange removes medicines that stay mainly in the blood and bind to plasma proteins. Antibody-based medicines and IV immunoglobulin may be removed in large part if given shortly before a session, and some antibiotics and other drugs may need their timing adjusted. Review the medicine schedule with the physician or pharmacist, and do not give a dose that the order says to give after the session until the session has ended. Some physicians also review the timing of certain BP medicines before a session, because of reactions reported with them; that decision is the physician&rsquo;s.</li>
<li><strong>Other treatments.</strong> If the patient also receives HD or CRRT, the order states the sequence; the teams agree on the timing so that circuits are not run on the same access at cross purposes.</li>
</ul>
<p><strong>During the session: what to watch for and what to do</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Why it happens</th><th>What the nurse sees</th><th>First actions</th></tr></thead>
<tbody>
<tr><td>Citrate-related low calcium</td><td>Citrate, from the anticoagulant and from donor plasma, binds ionized calcium in the patient&rsquo;s blood</td><td>Tingling around the mouth or in the fingertips, a strange taste, chills, nausea; later muscle twitching, cramps, tetany, low BP, or rhythm changes</td><td>Tell the operator to slow the return or the citrate rate per protocol; give calcium per order or protocol; notify the physician; check ionized calcium as ordered. Severe signs are an emergency</td></tr>
<tr><td>Low BP</td><td>Blood in the circuit, slow replacement, fluid shifts, a vasovagal reaction, or an allergic reaction</td><td>Dizziness, pallor, sweating, yawning, a falling BP</td><td>Lay the patient flat, slow or pause per protocol, check that replacement keeps pace with removal, give fluid per order, and notify the physician</td></tr>
<tr><td>Allergic reaction to plasma</td><td>Reaction to donor proteins</td><td>Itching, hives, flushing; rarely wheezing, swelling of the lips or throat, and collapse</td><td>Stop the plasma, keep the line open per protocol, assess airway and breathing, notify the physician, and treat per order; anaphylaxis is managed as a medical emergency</td></tr>
<tr><td>Bleeding</td><td>Albumin replacement removes clotting factors; heparin may be used in the circuit</td><td>Oozing at the catheter or puncture sites, bruising, bleeding gums, blood in urine</td><td>Apply pressure, report, and check that ordered clotting tests are done; procedures such as catheter removal are timed with the physician</td></tr>
<tr><td>Other</td><td>Cool returning blood; low potassium after albumin; catheter infection</td><td>Shivering; weakness or rhythm change; fever or redness at the exit site</td><td>Use the blood warmer if provided; report; follow catheter-care protocol</td></tr>
</tbody></table></div>
<p>Vital signs are taken at the interval the protocol sets, more often at the start and during any reaction. The patient is asked to say at once if tingling, chills, or itching start: early citrate symptoms are subjective, and a patient who has been taught them is the first alarm.</p>
<p><strong>After the session.</strong> Record the volume of plasma removed, the replacement fluid given by type and amount, the net fluid balance, any reaction and its treatment, and vital signs at the end. Check that post-session samples are drawn as ordered, give any medicines scheduled for after the session, and reassess the findings recorded at baseline. Hand over to the next nurse the time of the next session, the pending results, and any reaction, using the unit&rsquo;s structured handoff.</p>
<p><strong>The nurse&rsquo;s place in the team.</strong> The physician decides the indication, volume, fluid, number of sessions, and medicine timing; the apheresis service runs the procedure to that order; the bedside nurse watches the patient, recognizes complications, and keeps the medicine schedule and the record accurate. Reporting promptly and coordinating between these roles is what keeps a procedure that is usually well tolerated from becoming dangerous.</p>
"""},
]
QUIZ = [
    {"stem": "A patient with severe acute Guillain-Barr&eacute; syndrome is starting plasma exchange. His wife asks why he cannot simply have dialysis, which she has seen used for other patients in the ICU. Which explanation is accurate?",
     "options": [
         ("Dialysis and plasma exchange do the same thing, but plasma exchange is faster", False, "Dialysis membranes are built to keep proteins in the blood, so they cannot remove antibodies; the two therapies remove different things."),
         ("The illness is driven by antibodies, which are large proteins that a dialyzer holds back; plasma exchange removes the plasma containing them and replaces it", True, "Plasma exchange removes plasma with its large proteins, including antibodies, and replaces it with albumin or plasma. Acute Guillain-Barr&eacute; syndrome is a Category I indication in the 2023 guideline."),
         ("Plasma exchange cleans the nerves directly by filtering the fluid around them", False, "Plasma exchange acts on the blood only; nerves recover as the harmful antibodies are reduced and the body repairs them."),
         ("Plasma exchange is used because his kidneys have failed", False, "The indication is the antibody-driven illness, not kidney failure."),
     ],
     "objective": "Explain what therapeutic plasma exchange removes and why, how centrifugal and membrane separation differ in principle, how the American Society for Apheresis categorizes indications, and when albumin or plasma is used as replacement fluid.", "sources": ["asfa2023"], "flag": ""},
    {"stem": "Thirty minutes into a centrifugal plasma exchange using citrate and plasma as replacement fluid, the patient says her lips and fingertips are tingling and she feels a little nauseated. Her BP is unchanged. What should the nurse do first?",
     "options": [
         ("Reassure her that this is normal and continue at the same rate", False, "Tingling is an early sign of citrate-related low calcium; ignoring it allows progression to tetany or rhythm problems."),
         ("Stop the procedure permanently and remove the catheter", False, "Mild citrate symptoms are usually managed by slowing the procedure and giving calcium per protocol; stopping and removing access are not first steps."),
         ("Give an antiemetic from the ward stock and continue", False, "Nausea here is part of the citrate reaction; medicines are given by order, and the cause must be addressed."),
         ("Ask the operator to slow the return or citrate rate per protocol, give calcium per order or protocol, notify the physician, and monitor closely", True, "Citrate from the anticoagulant and donor plasma binds ionized calcium. Slowing the citrate load and replacing calcium per protocol usually relieve symptoms; the physician is informed and the patient watched for progression."),
     ],
     "objective": "Prepare for and monitor a plasma exchange session, recognize citrate-related low calcium, low blood pressure (BP), allergic reactions to plasma, and bleeding, and coordinate medicine timing, reporting each finding per order.", "sources": ["asfa2023"], "flag": "Calcium replacement follows the unit protocol or order."},
]
TERMS = [
    ("Therapeutic plasma exchange", "Removal of a patient's plasma, with the substances dissolved in it, and its replacement with albumin solution or donor plasma."),
    ("Centrifugal separation", "Separating plasma from blood cells by spinning the blood, so that components separate by density."),
    ("Membrane separation", "Separating plasma from blood cells with a plasma filter whose pores pass proteins but hold back cells."),
    ("Apheresis category", "The American Society for Apheresis rating (I to IV) of how well established apheresis is for a given disease indication."),
    ("Citrate reaction", "Symptoms of low ionized calcium caused by citrate binding calcium during apheresis, starting with tingling around the mouth and fingers."),
]
FLAGS = [
    "Categories and examples were checked against the ASFA 2023 (ninth edition) category table as quoted from the guideline PDF: TTP I; acute Guillain-Barre primary treatment I; myasthenia gravis acute short-term I and long-term II; anti-GBM disease with diffuse alveolar hemorrhage I, dialysis-independent I, dialysis-dependent without hemorrhage III; symptomatic hyperviscosity in hypergammaglobulinemia I; MPA and GPA III; drug-induced TMA with gemcitabine or quinine IV. The 91 fact sheets and 166 indications are from the PubMed abstract. Recheck at each new edition.",
    "No exchange volumes, numbers of sessions, calcium doses, citrate rates, or vital-sign intervals are stated; the per-volume removal fraction is described qualitatively only.",
    "The statement that neither separation method has been shown better for patients in general is a qualitative summary; the guideline describes both methods without stating a preference.",
    "The reaction associated with certain BP medicines (angiotensin-converting enzyme inhibitors, reported mainly with albumin replacement and some adsorption columns) is phrased generically as a physician decision; no withholding interval is stated or cited.",
    "Drug removal is described in principle (protein-bound, mainly intravascular drugs, antibody medicines, IV immunoglobulin); timing is left to the physician and pharmacist.",
    "Where plasma exchange is done in Philippine hospitals (blood bank, hematology, nephrology, or dialysis services) varies and is described generically.",
    "fetch_refs.py globs m??_x*.py; confirm asfa2023 is added to refs_pubmed_raw.json. The journal title (J Clin Apher) may need a JOURNALS or TITLE_OVERRIDES entry.",
]
NEW_REFS = {
    "asfa2023": "37017433",
}
