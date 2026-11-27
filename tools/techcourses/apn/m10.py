# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 10: Frequent relapses, steroid dependence and steroid resistance.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine
practice. KDIGO 2025 recommendations (1.3.3.1, 1B; 1.4.1.1, 1C) and practice points checked against the guideline and executive
summary; IPNA 2020 SRNS grades against the full text (PMC7316686); IPNA 2022 definitions and toxicity criteria against PMC9589698;
levamisole (Gruppen 2018), rituximab (Iijima 2014), tacrolimus vs cyclophosphamide (Gulati 2012) and PodoNet (Trautmann 2015)
against PubMed abstracts. No doses: every regimen follows the unit's pediatric formulary."""

MODULE = {
    "image_alt": "A Cushingoid Filipino girl of about ten, wearing glasses, sits with her parents in a pediatric nephrology clinic as the doctor sets out three options on cards on the desk.",
    "objectives": [
        "Classify a relapsing course with the IPNA 2022 definitions and recognize steroid toxicity early enough to act.",
        "Choose a steroid-sparing agent with the family, weighing the evidence, harms, cost and availability of levamisole, mycophenolate, calcineurin inhibitors, cyclophosphamide and rituximab.",
        "Work up steroid resistance with biopsy and genetic testing, start a calcineurin inhibitor for non-genetic disease, and plan for transplant recurrence risk.",
    ],
    "big": """<div class="tc-keyp"><span class="tc-lab">Your role &middot; ending the steroid cycle</span>By the time a child with relapsing nephrotic syndrome reaches you, she has usually had several full glucocorticoid courses restarted by different doctors. Your duty is to name her course correctly, count what the steroids have cost her, and lead the family to a steroid-sparing plan they can afford and sustain. For the child who never remits, your duty is a biopsy and a gene test that change treatment and, years later, the transplant conversation.</div>
{{plain:Think of glucocorticoids as a fire extinguisher. It puts out the fire every time, but a house where the fire keeps restarting cannot be sprayed every month. At some point you have to deal with what keeps lighting it.}}
<p>The picture has a limit. In steroid-sensitive disease the &ldquo;fire&rdquo; is an immune attack on the podocyte, increasingly linked to antinephrin antibodies and B cells, so steroid-sparing drugs that quiet T cells or remove B cells do address its source. In some steroid-resistant children there is no fire at all: a gene for a podocyte structural protein is broken, and no extinguisher will help. Those children need the immunosuppression stopped, not escalated. Telling the two apart is the core of this module.</p>
{{cards:Key numbers|Levamisole RCT (Gruppen 2018)::Hazard ratio for relapse 0.22; 26% vs 6% still in remission at 12 months|Rituximab RCT (Iijima 2014)::Median relapse-free period 267 vs 101 days (hazard ratio 0.27)|Monogenic cause in SRNS (IPNA 2020)::10&ndash;30% of children|Tacrolimus vs IV cyclophosphamide in SRNS (Gulati 2012)::Complete remission 52.4% vs 14.8%|Recurrence after transplant (PodoNet)::25.8% without vs 4.5% with a genetic diagnosis}}
<p>Most children with frequent relapses or steroid dependence can be kept in remission with less steroid, and many outgrow the disease. A few are steroid resistant, and among them a genetic minority will not respond to any immunosuppression. Your work is to classify the course from dated events, choose a steroid-sparing agent with the family, and investigate resistance quickly enough that the child is neither overtreated nor undertreated.</p>
""",
    "case": {"title": "The fifth relapse",
             "html": """<p>Kristine Joy Manalo is 10 years old. She was diagnosed with nephrotic syndrome at age 4 in Lipa City, Batangas, and responded fully to her first course. Since then she has relapsed again and again. In the past 12 months she has had five relapses. The last two began while her prednisone was being tapered and nine days after it was stopped. Each time a different doctor restarted a full course.</p>
<p>She weighs 41 kg, and her height has crossed down from the 50th to below the 15th percentile in two years. Her blood pressure is 124/82, her face is round, she has striae on her thighs, and last month an ophthalmologist found posterior subcapsular cataracts and prescribed glasses. She has stopped going to school because classmates tease her about her face. Her urine dipstick today is 4+; serum albumin 2.0 g/dL, creatinine 0.5 mg/dL, C3 normal.</p>
<p>The referring pediatrician&rsquo;s note reads: &ldquo;Steroid-resistant NS? For biopsy and cyclophosphamide.&rdquo; Her father drives a tricycle; her mother has read about rituximab in a parents&rsquo; Facebook group and asks whether it will &ldquo;finish&rdquo; the disease. Her grandmother wants to try herbal tea first.</p>""",
             "questions": ["How do you classify her course, and does she need a biopsy?",
                           "Which steroid-sparing option do you offer, and how do you decide with the family?",
                           "If a child does not remit by 6 weeks of glucocorticoids, what changes, and why does a genetic result matter for treatment and transplant?"]},
    "sections": [
        ("physiology", "Physiology", "Why relapses recur, why steroids harm, and why some children never respond",
         """<p><strong>Relapse.</strong> In steroid-sensitive disease the podocyte is attacked, not broken. Circulating antinephrin antibodies, produced by B cells with T-cell help, are found in most children with active, untreated disease and fall with remission, as Module 9 described. Infections stimulate the immune system and often precede relapses. Glucocorticoids suppress the attack and also act directly on the podocyte cytoskeleton, so remission comes quickly. When the drug is withdrawn, the immune drive may return.</p>
<p><strong>The cost of steroids in a growing child.</strong> Glucocorticoids blunt growth hormone action and growth plate activity, so height velocity falls. They reduce bone formation, raise blood pressure, increase appetite and fat deposition, cause cataracts and glaucoma, disturb sleep, mood and behavior, and raise blood glucose. Each restarted full course adds to a cumulative exposure. The IPNA 2022 recommendations define steroid toxicity as new or worsening obesity or overweight, sustained hypertension, hyperglycemia, behavioral or psychiatric disorders, sleep disruption, impaired growth (height velocity below the 25th percentile or height below the 3rd percentile in a child who grew normally before) and Cushingoid features, among others.[[apn10_3]]</p>
<p><strong>Resistance.</strong> Children whose disease does not remit with glucocorticoids fall into two broad groups. In one, the immune attack is stronger or different, and other immunosuppressants may still work. In the other, a variant in a gene such as <em>NPHS2</em> (podocin), <em>WT1</em> or <em>NPHS1</em> (nephrin) disrupts the podocyte&rsquo;s structure. Immunosuppression cannot repair a missing protein. The international PodoNet registry, with 1,655 children with steroid-resistant or congenital nephrotic syndrome from 67 centers, found a genetic cause in 23.6% of the 1,174 children screened, falling from 66% in congenital nephrotic syndrome to 15% to 16% in school-age children and adolescents.[[apn10_7]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Group</th><th>Mechanism</th><th>Response to immunosuppression</th><th>Recurrence after transplant</th></tr></thead>
<tbody>
<tr><td>Steroid-sensitive, relapsing</td><td>Immune podocytopathy (antinephrin antibodies, B and T cells)</td><td>Remits with glucocorticoids; steroid-sparing agents reduce relapses</td><td>Rarely reaches kidney failure</td></tr>
<tr><td>Steroid-resistant, non-genetic</td><td>Immune or circulating-factor disease</td><td>Calcineurin inhibitors and rituximab achieved complete remission in 40&ndash;45% in PodoNet</td><td>High: 25.8% in PodoNet; can begin within hours to days of grafting</td></tr>
<tr><td>Steroid-resistant, genetic</td><td>Structural podocyte gene defect</td><td>Rarely responds; immunosuppression mostly adds harm</td><td>Low: 4.5% in PodoNet</td></tr>
</tbody></table></div>
<p>These PodoNet figures come from a registry, so they describe what happened to treated children rather than what each drug causes, and genes common in Europe may be less common in Southeast Asian children.[[apn10_7]]</p>
{{key:A steroid-resistant child may have an immune disease you can treat or a structural one you cannot. Find out before you escalate.}}
{{fig:apn10_a}}
"""),
        ("sparing", "Steroid-sparing therapy", "Steroid-sparing therapy: what the evidence shows",
         """<p>KDIGO 2025 recommends glucocorticoid-sparing agents to prevent relapses, rather than no treatment or glucocorticoids alone, for children with frequently relapsing disease who develop serious glucocorticoid-related adverse effects and for all children with steroid-dependent disease (Recommendation 1.3.3.1, graded 1B).[[apn10_1]] The 2025 update removed the earlier split between first-line and alternative agents; it notes that rituximab trials used one to four doses without enough data for a specific recommendation, and that mycophenolate after rituximab may reduce treatment failure in complicated cases.[[apn10_2]] An ungraded practice point lists oral calcineurin inhibitors, cyclophosphamide, levamisole, mycophenolate mofetil (MMF) and rituximab in an unbiased order and says the choice requires careful consideration of resources, adherence, adverse effects and patient preferences; it adds that oral cyclophosphamide and levamisole may be preferable in frequently relapsing disease, and MMF, rituximab, calcineurin inhibitors and, to a lesser extent, oral cyclophosphamide in steroid-dependent disease.[[apn10_1]] The choice is therefore a shared decision, not a ladder.</p>
<p><strong>Levamisole.</strong> An international placebo-controlled trial randomized 99 children with steroid-sensitive disease and frequent relapses to levamisole or placebo for one year. Time to relapse was longer with levamisole (hazard ratio 0.22, 95% CI 0.11 to 0.43). After 12 months, 26% of children on levamisole and 6% on placebo were still in remission. Asymptomatic moderate neutropenia was the most frequent serious adverse event possibly related to the drug, in 4 of 50 children, and it reversed.[[apn10_4]] Most children still relapsed within the year, so levamisole lengthens remissions rather than ending the disease, and regular blood counts are required.</p>
<p><strong>Rituximab.</strong> A double-blind trial at nine Japanese centers randomized 48 treated children with complicated frequently relapsing or steroid-dependent disease to rituximab or placebo. The median relapse-free period was 267 days with rituximab and 101 days with placebo (hazard ratio 0.27, 95% CI 0.14 to 0.53). Serious adverse events occurred in 42% and 25% (not significantly different).[[apn10_5]] Follow-up was one year; most children relapse as B cells return, and hypogammaglobulinemia, infusion reactions and infections need monitoring. Live vaccines are avoided in the first 6 months after rituximab.[[apn10_3]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Agent</th><th>Evidence anchor</th><th>Main harms to discuss</th><th>Practical points</th></tr></thead>
<tbody>
<tr><td>Levamisole</td><td>RCT, 99 children: HR 0.22; 26% vs 6% in remission at 12 months</td><td>Neutropenia; rarely vasculitis</td><td>Inexpensive where available; needs blood counts; availability varies</td></tr>
<tr><td>Mycophenolate mofetil</td><td>Included in KDIGO 2025 options; may be used after rituximab</td><td>Gastrointestinal upset, cytopenias, teratogenicity</td><td>Twice-daily adherence; no nephrotoxicity</td></tr>
<tr><td>Calcineurin inhibitors (CNIs)</td><td>Included in KDIGO 2025 options</td><td>Nephrotoxicity, hypertension, gum hypertrophy and hirsutism (cyclosporine), diabetes (tacrolimus)</td><td>Drug levels and creatinine; relapses often follow withdrawal</td></tr>
<tr><td>Cyclophosphamide</td><td>Older trials; included in KDIGO 2025 options</td><td>Gonadal toxicity, cytopenias, infection, hemorrhagic cystitis</td><td>A single course with a cumulative ceiling the guidelines specify; counsel on fertility</td></tr>
<tr><td>Rituximab</td><td>RCT, 48 children: 267 vs 101 relapse-free days; HR 0.27</td><td>Infusion reactions, infection, hypogammaglobulinemia</td><td>Cost; infusion setting; vaccines first; relapse as B cells return</td></tr>
</tbody></table></div>
<p>None of these drugs has been shown in children to change kidney survival, because steroid-sensitive disease rarely causes kidney failure. The outcomes that matter are fewer relapses, less steroid exposure, growth, school and quality of life. Head-to-head pediatric trials remain few, so the family&rsquo;s priorities legitimately drive the choice.</p>
{{key:Choose the steroid-sparing agent with the family. The evidence supports several; their harms, costs and routines differ, and the child must live with them.}}
{{fig:apn10_b}}
"""),
        ("resistance", "Steroid resistance", "Steroid resistance: biopsy, genes and calcineurin inhibitors",
         """<p>A child with no complete remission after 4 weeks of standard glucocorticoids enters the confirmation period, from week 4 to week 6. The IPNA 2020 recommendations for steroid-resistant nephrotic syndrome (SRNS) use those two weeks to assess response to further glucocorticoids and to start renin-angiotensin-aldosterone system (RAAS) blockade (grade C, weak recommendation), and recommend genetic testing and/or kidney biopsy during the same window (grade B, moderate recommendation).[[apn10_6]] They recommend a comprehensive gene panel covering the known SRNS genes. With exome sequencing, 10% to 30% of children are now diagnosed with a monogenic disease, and the likelihood falls with older age at onset and rises with a family history or extrarenal features.[[apn10_6]]</p>
<p><strong>Treatment.</strong> The IPNA recommends a calcineurin inhibitor, cyclosporine or tacrolimus, as first-line immunosuppression once SRNS is confirmed (grade B, moderate recommendation), withholding or delaying it when estimated glomerular filtration rate (eGFR) is below 30 mL/min/1.73 m&sup2;, in AKI or with uncontrolled hypertension (grade X, strong recommendation), and withholding it and stopping glucocorticoids when a monogenic form is identified (grade B, moderate recommendation).[[apn10_6]] KDIGO 2025 likewise recommends cyclosporine or tacrolimus as initial second-line therapy for SRNS (Recommendation 1.4.1.1, graded 1C).[[apn10_1]] Where genetics or histology are not available, the IPNA allows a calcineurin inhibitor to be started; where calcineurin inhibitors are not available, cyclophosphamide may be used.[[apn10_6]]</p>
<p>The strongest pediatric comparison is a multicenter Indian trial of 131 children with SRNS randomized to tacrolimus for 12 months or six monthly infusions of intravenous cyclophosphamide, both with alternate-day prednisolone. Complete or partial remission at 6 months favored tacrolimus (hazard ratio 2.64), complete remission was 52.4% versus 14.8%, and three children needed tacrolimus for one additional remission. Withdrawals for systemic infection were more common with cyclophosphamide.[[apn10_8]] The endpoint was proteinuria remission, a strong surrogate in this disease, not kidney survival.</p>
<div class="table-wrap"><table>
<thead><tr><th>At week 6 without remission</th><th>What you do</th><th>Source and grade</th></tr></thead>
<tbody>
<tr><td>Confirm SRNS</td><td>Quantify UPCR; check albumin, creatinine, blood pressure</td><td>IPNA 2022 and 2020 definitions</td></tr>
<tr><td>Biopsy and/or gene panel</td><td>Ideally within the confirmation period</td><td>IPNA 2020, grade B, moderate</td></tr>
<tr><td>Start RAAS blockade</td><td>For antiproteinuric effect, if volume and kidney function allow</td><td>IPNA 2020, grade C, weak</td></tr>
<tr><td>Start a calcineurin inhibitor</td><td>Unless eGFR &lt;30, AKI, uncontrolled hypertension, or a monogenic cause</td><td>IPNA 2020, grade B; KDIGO 2025, 1C</td></tr>
<tr><td>Monogenic result</td><td>Stop immunosuppression; supportive care; plan kidney replacement therapy (KRT) and transplant</td><td>IPNA 2020, grade B, moderate</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">In your clinic, week six &middot; fictional</span><p>Paolo, 3, from Iloilo, is still 4+ on dipstick after 6 weeks of prednisolone. His parents are first cousins. A biopsy shows focal segmental glomerulosclerosis, and the gene panel, sent abroad, returns two pathogenic <em>NPHS2</em> variants.</p><p>You stop the prednisolone, do not start tacrolimus, continue RAAS blockade and supportive care, and begin the conversation about dialysis and transplantation, including that his disease is unlikely to recur in a graft.</p><p class="tc-scene-take"><b>What this shows.</b> A genetic answer spares a child months of toxic drugs that would not have worked.</p></div>
<p><strong>Transplant planning.</strong> Recurrence after transplant is the most feared event in non-genetic SRNS: in PodoNet it occurred in 25.8% of children without a genetic diagnosis and 4.5% with one.[[apn10_7]] The IPNA recommends discussing the anticipated recurrence risk with the family when planning kidney replacement therapy (grade A, strong recommendation), and measuring urine protein before transplantation so that recurrence can be recognized afterward (grade A, strong recommendation).[[apn10_6]] Module 26 continues this conversation.</p>
{{key:At week 6 without remission, biopsy and gene-test together, start a calcineurin inhibitor for non-genetic disease, and stop immunosuppression for genetic disease.}}
"""),
        ("practice", "Practice", "Deciding with the family, and living with the disease",
         """<p><strong>Name the course first.</strong> Lay out the dates: first remission, each relapse, what she was taking and when it stopped. Kristine&rsquo;s last two relapses came during the taper and nine days after stopping, which is steroid dependence by the IPNA 2022 definition, and she has had five relapses in 12 months, which also meets the definition of frequent relapses.[[apn10_3]] She has always remitted, so she is not steroid resistant. The Academy&rsquo;s nephrotic course classifier, linked below, applies these definitions to the dates you enter.</p>
<p><strong>Count the toxicity.</strong> Before the family meeting, list what the steroids have done: growth, weight, blood pressure, eyes, bones, mood, school. Show the family the growth chart. A cataract and a falling height centile are reasons to act now, not after the next relapse.</p>
<p><strong>Decide together.</strong> Present two or three options that are available and affordable in your setting, with the numbers above, the routine each requires (daily tablets, blood tests, infusions) and the harms. Ask what matters most to the child and family: school, appearance, fertility, cost, fewer clinic visits. A 10-year-old can give assent and should hear her options in words she understands.</p>
<div class="table-wrap"><table>
<thead><tr><th>What to monitor</th><th>Why</th><th>How often</th></tr></thead>
<tbody>
<tr><td>Height, weight, BMI on a growth chart</td><td>Steroid growth suppression and obesity</td><td>Every visit</td></tr>
<tr><td>Blood pressure, measured correctly</td><td>Steroid and CNI hypertension</td><td>Every visit</td></tr>
<tr><td>Eye examination</td><td>Cataract, glaucoma</td><td>At intervals while on steroids, per your ophthalmologist</td></tr>
<tr><td>Blood counts, creatinine, drug levels</td><td>Drug-specific toxicity</td><td>As the protocol for the chosen agent sets</td></tr>
<tr><td>Mood, sleep, school attendance</td><td>Behavioral toxicity and stigma</td><td>Every visit; involve the school when needed</td></tr>
</tbody></table></div>
<p><strong>Philippine realities.</strong> Cost and supply decide more choices than trials do. Check with the hospital pharmacy what is stocked before you offer it, ask the social service office early about financial assistance, and avoid starting a drug the family cannot continue. Herbal products are a frequent request; ask about them without judgment, explain that none has been shown to prevent relapses, and warn that some may harm the kidney or interact with immunosuppressants.</p>
{{flow:Relapsing child, clinic visit|List the dates::Remission, relapses, therapy at each relapse; classify with the IPNA definitions.|Count the toxicity::Growth chart, blood pressure, eyes, bones, mood, school.|Rule out resistance::Has she ever had complete remission within 4&ndash;6 weeks? If yes, she is not SRNS; no biopsy for typical disease.|Choose a steroid-sparing agent::Shared decision on levamisole, MMF, CNI, cyclophosphamide or rituximab; check stock and cost; consent and assent.|Prepare::Vaccines before immunosuppression where possible; baseline blood tests the protocol requires.|Follow::Relapse diary, toxicity checks, and a review date to decide whether the agent is working.}}
{{call:<ul><li>No complete remission after 4 weeks of standard glucocorticoids (enter the confirmation period; plan biopsy and genetics)</li><li>A rising creatinine on a calcineurin inhibitor</li><li>Fever or severe infection after rituximab or on combined immunosuppression</li><li>New visual symptoms, hypertensive urgency or severe mood change on steroids</li></ul>}}
{{key:Every restarted full course of glucocorticoids is a decision. If the child has toxicity, the next decision is a steroid-sparing plan.}}
"""),
    ],
    "debrief": [
        "<p><strong>Classification and biopsy.</strong> Kristine is steroid dependent (two consecutive relapses during the taper and within 14 days of stopping) and frequently relapsing (five relapses in 12 months) by the IPNA 2022 definitions. She has always remitted, so she is not steroid resistant, and with typical disease and a normal C3 she does not need a biopsy. Correct the referral note, because the label &ldquo;steroid resistant&rdquo; would send her down the wrong path.</p>",
        "<p><strong>Choosing a steroid-sparing agent.</strong> Her cataract, slowed growth, hypertension and school refusal are glucocorticoid complications, and as a steroid-dependent child she falls within KDIGO 2025&rsquo;s recommendation for a steroid-sparing agent (1B), for which the guideline suggests MMF, rituximab or a calcineurin inhibitor may be preferable. Treat the current relapse as the guideline describes with the dose from the unit formulary, then offer the options that are available and affordable: for example MMF as an oral option, a calcineurin inhibitor with levels and creatinine monitoring, or rituximab if the family can access it, with the Japanese trial&rsquo;s 267 versus 101 relapse-free days explained honestly as a longer remission, not a cure. At her age, discuss fertility before any cyclophosphamide. Ask Kristine what matters most to her, involve social service early, and talk about the herbal tea without judgment.</p>",
        "<p><strong>When a child does not remit.</strong> No complete remission at 4 weeks starts the confirmation period; none by 6 weeks is SRNS. Then biopsy and a comprehensive gene panel go together (IPNA 2020, grade B), RAAS blockade starts if safe, and a calcineurin inhibitor is first-line for non-genetic disease (IPNA grade B; KDIGO 2025, 1C). A monogenic result means stopping immunosuppression, because it rarely works and only adds harm, and it changes the transplant conversation: in PodoNet, recurrence after transplant was 4.5% with a genetic diagnosis and 25.8% without.</p>",
    ],
    "skills": {"title": 'Frequent relapses, steroid dependence and steroid resistance',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Builds a dated relapse timeline and classifies the course with the IPNA definitions", False),
                         ("Documents steroid toxicity using growth chart, blood pressure and eye findings", False),
                         ("Leads a shared decision on a steroid-sparing agent, including cost, availability and assent", False),
                         ("Plans biopsy, gene testing and calcineurin inhibitor therapy for confirmed SRNS", False)],
               "placement": "Pediatric nephrology clinic"},
    "quiz": [
        ("A child relapses twice in a row, once during the taper and once 9 days after stopping glucocorticoids, and always remits. How is the course classified?",
         ["Steroid resistant", "Steroid dependent", "Infrequently relapsing", "Late responder"],
         1, "Two consecutive relapses during therapy or within 14 days of stopping define steroid dependence (IPNA 2022). Remission each time excludes resistance."),
        ("What did the randomized levamisole trial show in frequently relapsing children?",
         ["No effect on relapse", "Hazard ratio for relapse 0.22; 26% vs 6% still in remission at 12 months", "Cure in most children", "Nephrotoxicity in half"],
         1, "Levamisole lengthened remissions; most children still relapsed within the year. Neutropenia occurred in 4 of 50 and reversed."),
        ("What proportion of children with SRNS have a monogenic cause, according to the IPNA 2020 recommendations?",
         ["Under 1%", "10% to 30%", "About 70%", "All of them"],
         1, "With exome sequencing, 10% to 30% are diagnosed with a monogenic disease, more often with early onset, family history or extrarenal features."),
        ("A child with confirmed SRNS has two pathogenic <em>NPHS2</em> variants. What does the IPNA recommend?",
         ["Escalate to tacrolimus and rituximab", "Withhold calcineurin inhibitors and stop glucocorticoids; continue supportive care", "Repeat a full steroid course", "Start cyclophosphamide"],
         1, "Monogenic SRNS rarely responds to immunosuppression (grade B, moderate recommendation to withhold CNI and stop glucocorticoids)."),
        ("In the Indian trial of tacrolimus versus intravenous cyclophosphamide for SRNS, what was the complete remission rate?",
         ["52.4% vs 14.8%", "14.8% vs 52.4%", "No difference", "90% in both groups"],
         0, "Tacrolimus was superior; three children needed tacrolimus for one additional remission, and cyclophosphamide had more withdrawals for infection."),
    ],
    "terms": [("FRNS", "Frequently relapsing nephrotic syndrome"), ("SDNS", "Steroid-dependent nephrotic syndrome"),
              ("SRNS", "Steroid-resistant nephrotic syndrome"), ("IPNA", "International Pediatric Nephrology Association"),
              ("KDIGO", "Kidney Disease: Improving Global Outcomes"), ("CNI", "Calcineurin inhibitor"), ("MMF", "Mycophenolate mofetil"),
              ("RAAS", "Renin-angiotensin-aldosterone system"), ("UPCR", "Urine protein-to-creatinine ratio"),
              ("eGFR", "Estimated glomerular filtration rate"), ("AKI", "Acute kidney injury"), ("KRT", "Kidney replacement therapy"),
              ("RCT", "Randomized controlled trial"), ("HR", "Hazard ratio"), ("CI", "Confidence interval"), ("IV", "Intravenous"),
              ("BMI", "Body mass index"), ("NPHS1, NPHS2, WT1", "Genes encoding nephrin, podocin and Wilms tumor 1 protein"),
              ("PodoNet", "International registry of steroid-resistant and congenital nephrotic syndrome"), ("NS", "Nephrotic syndrome")],
    "readings": [('nephrotic-syndrome.html', 'Nephrotic Syndrome: When the Kidney Filter Leaks Protein'),
                 ('medicines-and-your-kidneys.html', 'Multiple Medicines and Your Kidneys'),
                 ('kidney-transplant.html', 'Beyond Dialysis: Understanding Kidney Transplant')],
    "calcs": ["calc-pediatric-nephrotic-course.html", "calc-corticosteroid-conversion.html", "calc-pediatric-bp.html", "calc-pediatric-growth-percentiles.html", "calc-pediatric-bmi-zscore.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
