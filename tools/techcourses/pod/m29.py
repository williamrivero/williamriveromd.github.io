# -*- coding: utf-8 -*-
"""Physician on Duty, Module 29: A Clean Unit: Hepatitis, HIV, Tuberculosis, and Vaccines.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse reviewing a laboratory slip at the nurses&rsquo; station while, in the background, a patient is moved with her machine toward a separate room. Gloves, a sharps box, and a hand-rub dispenser are in view.",
    "objectives": [
        "Explain how hepatitis B virus (HBV), hepatitis C virus (HCV), and human immunodeficiency virus (HIV) travel between dialysis stations, and which practices interrupt each route.",
        "Apply the station, machine, and staff rules for each virus, citing the Centers for Disease Control and Prevention (CDC) 2001 recommendations and the Kidney Disease: Improving Global Outcomes (KDIGO) 2022 hepatitis C guideline with its grades.",
        "Interpret a hemodialysis serology panel and take the first steps after a new positive result.",
        "Screen for and recognize tuberculosis in a dialysis patient, and manage a patient with a respiratory infection so that others are protected.",
        "List the vaccines for dialysis patients and staff, interpret a post-vaccination antibody result, and recognize a nonresponder.",
        "Respond to a needlestick or blood splash in the first hour, per your unit&rsquo;s protocol.",
    ],
    "big": """
{{plain:Picture a row of freshly painted benches in a barangay hall, and nobody can see which bench is still wet. Whoever touches one carries a little paint to the next bench and the next hand. Blood at a dialysis station behaves the same way. A smear too small to see rides on a glove, a clamp, or a blood pressure cuff to the next chair.}}
<p>The picture has a limit: viruses differ. Hepatitis B virus (HBV) reaches very high levels in blood and survives for days on a dry surface. Hepatitis C virus (HCV) has spread between neighboring dialysis stations in many outbreaks. Human immunodeficiency virus (HIV) travels in blood too, but patient-to-patient spread in dialysis units has not been reported in the United States.[[cdc2001]] Tuberculosis and respiratory viruses travel in air. Each one needs its own rule.</p>
{{cards:Key terms for this module|Standard precautions::Practices used for every patient: hand hygiene, gloves, safe sharps and medicine handling, and cleaning.|HBsAg::Hepatitis B surface antigen, a protein of the virus. A positive test usually means current hepatitis B infection.|Anti-HBs::Antibody to hepatitis B surface antigen. A level of 10 milli-international units per milliliter (mIU/mL) or more after vaccination means protection.|Anti-HBc::Antibody to the hepatitis B core protein. It appears after infection, never after vaccination.|Anti-HCV::Antibody to hepatitis C. It shows exposure at some time and stays positive after recovery or cure.|HCV RNA::The genetic material (ribonucleic acid) of hepatitis C. A positive test means the virus is present now.|Seroconversion::A change from a negative to a positive result.|Postexposure prophylaxis (PEP)::Treatment given soon after an exposure to lower the chance that infection takes hold.}}
<p>Most shifts pass without a new infection. A few bring a new positive result, a coughing patient, or a needlestick. Your work is to keep the station rules exact, to recognize these three events, and to start the first steps your unit&rsquo;s protocol allows while you call.</p>
""",
    "case": {"title": "A new hepatitis B result", "html": """
<p>Mrs. Teresita Aquino, 61, has dialyzed for eight months at station 9 in the general area, on the Tuesday-Thursday-Saturday morning shift. Last month she spent one week in her home province for a family wake and dialyzed at a unit there.</p>
<p>At 10:00 a.m. on Thursday, during her session, the laboratory calls Nurse Paolo Cruz. Her monthly HBsAg test, drawn on Tuesday, is reactive. Last month it was nonreactive. She received a hepatitis B vaccine series, but no anti-HBs result was ever recorded. She is at hour two with stable vital signs and no complaints. The patients at stations 8 and 10 are susceptible to hepatitis B. Nurse Cruz has been covering stations 8, 9, and 10 since 7:00 a.m. He calls you to the nurses&rsquo; station (illustrative scenario).</p>
""", "questions": ["What do you do now, during this session, about Mrs. Aquino, her neighbors, and the nurse&rsquo;s assignment?",
                  "What does this result mean, what must be confirmed, and what other markers do you need?",
                  "Whom do you call, what do you tell Mrs. Aquino and when, and what is written and reported?"]},
    "sections": [
        ("routes", "How blood travels", "How Blood Travels Between Stations", """
<p>In a hemodialysis unit, many people&rsquo;s blood leaves their bodies on the same shift, handled by the same staff. Catheter infection (Modules 10 and 17) and water (Module 6) are covered elsewhere.</p>
<p>Three things decide how easily a virus travels between chairs: how much virus a drop of blood carries, how long the virus survives outside the body, and how often blood reaches a surface. Hepatitis B is the extreme case. An infected person can carry 10<sup>8</sup> to 10<sup>9</sup> virus particles in each milliliter of blood, and the virus stays viable for at least 7 days on surfaces at room temperature.[[cdc2001]] A smear too small to see can infect. Hepatitis C transmission between hemodialysis patients has been documented often, and investigations keep tracing it to lapses in infection control.[[patel2010]] Blood reaches surfaces at every needle insertion and disconnection, and the routes follow the hands.</p>
{{fig:pod29_routes}}
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>What interrupts it</th></tr></thead>
<tbody>
<tr><td>Hands and gloves: a glove that touched one line touches the next machine</td><td>Hand hygiene and fresh gloves between patients, and between dirty and clean tasks</td></tr>
<tr><td>Shared items: clamps, tape, tourniquets, and cuffs move between chairs</td><td>Each item is discarded, kept for one patient, or cleaned and disinfected[[cdc2001]]</td></tr>
<tr><td>Medicines: a multidose vial or cart touched with soiled gloves</td><td>Medicines prepared in a separate clean area. No common cart on the floor[[cdc2001]]</td></tr>
<tr><td>Surfaces: chair arms, machine panels, and priming buckets keep dried blood</td><td>Cleaning and disinfection before the next patient sits</td></tr>
</tbody></table></div>
<h3>What the outbreak investigations found</h3>
<p>In one United States clinic, 18 patients acquired hepatitis C between 2008 and 2013, an estimated attack rate of 16.7%. Viral sequencing linked 11 of them in 4 clusters. In each cluster, the patients had dialyzed at neighboring stations on the same shift, or at the same station on consecutive shifts. Investigators saw lapses in infection control and found visible and invisible blood on surfaces after cleaning.[[nguyen2016]] In a low-resource unit in Vietnam, 11 patients seroconverted to hepatitis C within 2 months. A shared machine was the likely route in only 1 case; contact through the environment explained the other 10.[[duong2016]] These were outbreak investigations, not trials. They show how spread happened, not how much each precaution prevents.</p>
{{fig:dai_prevention|Hand hygiene before and after every contact with a patient or the machine is the first barrier against blood-borne spread.}}
{{key:Most transmission in a dialysis unit travels on hands, gloves, shared items, and surfaces, not through the machine. Clean practice at the station is the main defense.}}
"""),
        ("rules", "Station rules", "The Rules for Stations, Machines, and Staff", """
<p>The rules differ by virus because the viruses differ. You apply them when you assign a station or clear a patient (Module 11).</p>
<h3>Rules for every patient</h3>
<p>The CDC recommendations of 2001 apply to all patients: any item taken to a station is discarded, kept for that patient, or disinfected, and medicines are prepared away from the treatment floor.[[cdc2001]] These recommendations predate the Grading of Recommendations Assessment, Development, and Evaluation (GRADE) system and are ungraded. KDIGO recommends that units follow standard infection-control procedures that prevent the transfer of blood between patients (1A), with regular observational audits (1C).[[kdigo_hcv2022]]</p>
{{fig:pod29_zones}}
<h3>Hepatitis B: a separate room, machine, and staff</h3>
<p>For patients positive for HBsAg, CDC adds a separate room with dedicated machines, equipment, supplies, and medicines. Staff caring for these patients do not care for susceptible patients at the same time. Isolation of this kind was associated with 70% to 80% reductions in new hepatitis B infections among hemodialysis patients.[[cdc2001]] That figure comes from experience in United States units, not from a randomized trial. Philippine licensing rules require a clinic to assign at least one machine to patients with hepatitis B.[[doh2012]]</p>
{{fig:pod11_isolation|The hepatitis B station: a separate room, a dedicated machine, and its own supplies.}}
<h3>Hepatitis C and HIV: flawless standard precautions</h3>
<p>KDIGO 2022 takes a different line for hepatitis C. Its prevention chapter was carried over unchanged from 2018.[[kdigo_hcv_synopsis2023]] It recommends not using dedicated machines for patients with hepatitis C (1D) and suggests not isolating them (2C). Their dialyzers may be reused if standard infection control is followed (2D). Prevention should rest on infection control, not mainly on treating infected patients (Not Graded).[[kdigo_hcv2022]] The logic follows from the outbreaks: a separate machine does not stop a soiled glove or a vial prepared beside a blood sample. The letters C and D show low to very low certainty, and some regulators and units still dedicate machines to hepatitis C. Where your unit&rsquo;s rule is stricter, follow it.</p>
<p>For HIV, CDC does not recommend routine testing for infection control; standard precautions apply.[[cdc2001]] Testing for clinical care is a separate question (Module 27).</p>
<div class="table-wrap"><table>
<thead><tr><th>Status</th><th>Where</th><th>Machine</th><th>Staff</th><th>Source and grade</th></tr></thead>
<tbody>
<tr><td>HBsAg positive</td><td>Separate room</td><td>Dedicated, with its own supplies and medicines</td><td>Not caring for susceptible patients at the same time</td><td>CDC 2001, not graded. Philippine licensing rule[[doh2012]]</td></tr>
<tr><td>Immune to hepatitis B</td><td>General area, or beside HBsAg-positive patients</td><td>Shared</td><td>May care for infected and immune patients on one shift</td><td>CDC 2001, not graded</td></tr>
<tr><td>Susceptible to hepatitis B</td><td>General area</td><td>Shared, never the hepatitis B machine</td><td>Not shared with an HBsAg-positive patient at the same time</td><td>CDC 2001, not graded</td></tr>
<tr><td>Hepatitis C</td><td>General area with strict precautions, unless your unit&rsquo;s rule differs</td><td>Shared (1D)</td><td>Standard precautions</td><td>KDIGO 2022: no isolation (2C), reuse allowed (2D)</td></tr>
<tr><td>HIV</td><td>General area</td><td>Shared</td><td>Standard precautions</td><td>CDC 2001, not graded</td></tr>
</tbody></table></div>
{{key:Hepatitis B gets its own room, machine, and staff. Hepatitis C is controlled by flawless standard precautions, not by a separate machine, according to KDIGO. Where your unit&rsquo;s rule differs, follow your unit&rsquo;s rule.}}
"""),
        ("serology", "Serology", "Reading the Serology Panel and the Testing Schedule", """
<p>Think of the panel as five questions. HBsAg: is hepatitis B present now? Anti-HBs: is the patient protected? Anti-HBc: was the patient ever infected? Its IgM (immunoglobulin M) form marks a recent infection. Anti-HCV: was the patient ever exposed to hepatitis C? HCV RNA: is hepatitis C present now?</p>
<p>The hepatitis B vaccine contains only the surface protein, so a vaccinated person makes anti-HBs alone. A person who meets the whole virus also makes anti-HBc. A few patients test HBsAg positive for up to 18 days after a vaccine dose.[[cdc2001]] In hepatitis C, the virus multiplies for weeks before antibody is detectable. In that window, the antibody test is negative while virus is in the blood.</p>
{{fig:pod29_markers}}
<p>In seven United Kingdom units, 2 of 348 antibody-negative patients had hepatitis C RNA. Both infections dated to holiday dialysis abroad. Only one had a raised alanine aminotransferase (ALT), the liver enzyme used for screening, and both developed antibody within 8 to 13 weeks. Of 153 travel episodes followed prospectively, 4 led to new infection (2.6%).[[ghafur2007]] The study was small, but its point is direct: a recent exposure can hide behind a negative antibody test (Module 28 covers travel).</p>
<h3>The testing schedules</h3>
<p>CDC 2001 advises monthly HBsAg for susceptible patients, yearly anti-HBs for vaccine responders, and anti-HCV every 6 months with monthly ALT.[[cdc2001]] KDIGO 2022 recommends hepatitis C screening at the start of in-center hemodialysis or on transfer (1A), then every 6 months by antibody test or nucleic acid testing (1B). It suggests ALT at the start or on transfer (2B) and monthly after that (2B). A new hepatitis C infection is reported to public health (Not Graded).[[kdigo_hcv2022]] Follow your unit&rsquo;s schedule.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Meaning</th><th>Station</th><th>Next step</th></tr></thead>
<tbody>
<tr><td>HBsAg positive, IgM anti-HBc positive</td><td>Recent hepatitis B</td><td>Hepatitis B room</td><td>Confirm, call, report, look back</td></tr>
<tr><td>HBsAg positive, IgM anti-HBc negative</td><td>Usually long-standing hepatitis B</td><td>Hepatitis B room</td><td>Confirm and call. Look back if HBsAg was negative before</td></tr>
<tr><td>Anti-HBs 10 mIU/mL or more, anti-HBc negative</td><td>Immune by vaccination</td><td>General area</td><td>Anti-HBs yearly[[cdc2001]]</td></tr>
<tr><td>Anti-HBs positive, anti-HBc positive</td><td>Immune after past infection</td><td>General area</td><td>No routine follow-up testing[[cdc2001]]</td></tr>
<tr><td>HBsAg negative, anti-HBs below 10 mIU/mL, anti-HBc negative</td><td>Susceptible</td><td>General area</td><td>Monthly HBsAg. Vaccine status to the nephrologist</td></tr>
<tr><td>Anti-HBc alone</td><td>Often a false positive</td><td>General area. Isolation not needed</td><td>Retest per protocol[[cdc2001]]</td></tr>
<tr><td>Anti-HCV positive, HCV RNA positive</td><td>Current hepatitis C</td><td>Per KDIGO or your unit&rsquo;s rule</td><td>Referral for treatment</td></tr>
<tr><td>Anti-HCV negative, HCV RNA positive</td><td>Very recent hepatitis C</td><td>As for current hepatitis C</td><td>Confirm, call, report, look back</td></tr>
</tbody></table></div>
{{formula:<strong>Worked example 1: reading three panels (illustrative values).</strong><br>Panel A: HBsAg negative, anti-HBs 4 mIU/mL, anti-HBc negative. Susceptible (nonresponder or unvaccinated). Monthly HBsAg; vaccine history to the nephrologist.<br>Panel B: HBsAg negative, anti-HBs 120 mIU/mL, anti-HBc negative. Immune by vaccination. Anti-HBs yearly.<br>Panel C: anti-HCV positive, HCV RNA positive. Current hepatitis C. Under KDIGO 2022, no dedicated machine (1D) and no isolation (2C), unless your unit&rsquo;s rule differs.<br><em>What this does not tell you:</em> a panel describes the day it was drawn, not exposure since.}}
{{formula:<strong>Worked example 2: a seroconversion rate (illustrative arithmetic).</strong><br>Formula: incidence rate = new seroconversions &divide; patient-months at risk &times; 100.<br>A unit follows 80 hepatitis C-negative patients for 6 months: 80 &times; 6 = 480 patient-months.<br>Two convert to anti-HCV positive. Rate = 2 &divide; 480 &times; 100 = 0.42 per 100 patient-months.<br>Attack rate in an outbreak = cases &divide; patients at risk &times; 100. The clinic above had 18 cases and an attack rate of 16.7%.[[nguyen2016]]<br><em>What the number does and does not tell you:</em> it lets a unit compare itself over time. In a small unit it swings widely, and one new case is a signal whatever the rate. KDIGO recommends aggressive measures when a new case is likely dialysis related (1A).[[kdigo_hcv2022]]}}
<p>The site&rsquo;s access infection rate, run chart, and quality scorecard calculators use this arithmetic (Module 31).</p>
{{key:Read every result with its date. A negative test describes the day it was drawn, not today.}}
"""),
        ("newpositive", "A new positive", "A New Positive Result: The First Steps", """
<p>A new positive result is a clinical event for one patient and a possible warning for the whole unit. It may be a laboratory error, a brief positive after a vaccine dose, an infection acquired elsewhere, or transmission in your own unit. The first steps protect today&rsquo;s patients and begin the search for the source.</p>
<p>CDC 2001 asks units to report a new HBsAg-positive or anti-HCV-positive result as the law requires, to review all patients&rsquo; results, and to investigate whether spread happened in the unit. For new hepatitis B, HBsAg is often the only marker at first, so CDC advises repeating HBsAg and testing anti-HBc, including IgM anti-HBc.[[cdc2001]] The timing follows your unit&rsquo;s protocol and the attending nephrologist. KDIGO recommends tracking all hepatitis C results to find new cases (1B). When a new case is likely dialysis related, it recommends aggressive measures on hand hygiene, glove use, injection safety, and environmental cleaning (1A).[[kdigo_hcv2022]]</p>
{{flow:A new positive result: first steps|Confirm::Check the name, the date, and the test. Ask the attending nephrologist which confirmatory test to send, per your unit&rsquo;s protocol.|Call::Call the attending nephrologist now. Make sure the Medical Director hears the same day.|Place the patient::Apply the rule for that virus. For HBsAg, the hepatitis B room and machine. For hepatitis C, the unit&rsquo;s rule.|Separate the staff::A nurse caring for an HBsAg-positive patient does not care for susceptible patients at the same time.|Look back::List the stations, shifts, and neighbors since the last negative result. Testing of others follows the protocol.|Audit::Observe hand hygiene, gloves, medicine preparation, and cleaning.|Tell the patient::In private, with time for questions, after the nephrologist has reviewed the result.|Report::Public health notification as the regulation requires, and an incident report (Module 31).}}
<h3>Privacy and treatment</h3>
<p>A hepatitis or HIV result is sensitive personal information under the Data Privacy Act.[[ra10173]] Never announce a result at the station, in the corridor, or in a group chat. Share it only with staff who need it for care.</p>
<p>KDIGO 2022 recommends that patients with chronic kidney disease and hepatitis C, including those on dialysis, be evaluated for direct-acting antiviral therapy (1A).[[kdigo_hcv2022]] The 2022 update extended sofosbuvir-based regimens to patients on dialysis.[[kdigo_hcv_synopsis2023]] The referral and drug choice belong to the attending nephrologist and the liver specialist.</p>
{{call:Stop and call the attending nephrologist on the same shift for any new positive HBsAg, anti-HCV, or HCV RNA, and for any result that conflicts with the patient&rsquo;s station assignment. Call at once if the positive result is found after the patient has already dialyzed in the general area today. Follow your unit&rsquo;s protocol for the station and the staff assignment while you call.}}
{{key:Act on a new positive result as if it were true until it is confirmed or disproved, and keep it private.}}
"""),
        ("tb", "Tuberculosis", "Tuberculosis in the Dialysis Patient", """
<p>Tuberculosis is often a sleeping infection, walled off in a small scar for years by the immune system. When immunity falls, the wall gives way.</p>
<p>The picture has a limit. In a dialysis patient the waking is often quiet too. Containment depends on T lymphocytes, the white cells that direct the walling off, and kidney failure weakens them (Module 4). The same weakness blunts the signals you rely on. Fever and cough come partly from the immune response, so they may be mild. The tuberculin skin test and the interferon-gamma release assay (IGRA) both measure a T-cell response, so both can be falsely negative. Disease outside the lungs may appear as a pleural or pericardial effusion, swollen lymph nodes, peritonitis, weight loss, or fever without a source.</p>
{{fig:pod29_tb}}
<h3>What the evidence shows</h3>
<p>The Philippines accounted for 6.8% of the world&rsquo;s tuberculosis cases in the World Health Organization (WHO) report of 2024, among the five countries with the most cases.[[who_tb2024]] Dialysis and transplant patients are at higher risk, and screening tests perform poorly in chronic kidney disease.[[romanowski2016]] A meta-analysis of 122 studies of untreated people with a positive skin test or IGRA found 0.3 cases per 1,000 person-years in the general population, and consistently higher rates in at-risk groups, including people requiring dialysis.[[campbell2020]] These cohorts describe risk, not treatment.</p>
<p>WHO recommends that people receiving dialysis be systematically tested and treated for tuberculosis infection, as a strong recommendation with low to very low certainty of evidence.[[who_tpt2024]] For transplant candidates in intermediate and high prevalence areas, KDIGO suggests latent tuberculosis screening according to local guidelines (2C).[[kdigo_txcand2020]] The test, the timing, and any preventive treatment are the attending nephrologist&rsquo;s decision under the unit&rsquo;s policy.</p>
<h3>A cough at the chair</h3>
<p>Airborne infections are not stopped by the station rules for blood. Active pulmonary tuberculosis needs airborne precautions that most outpatient units cannot provide, so where such a patient dialyzes is decided by the attending nephrologist and the Medical Director.</p>
{{flow:A cough at the door or in the chair|Mask::Give the patient a surgical mask. Staff wear the protection your unit&rsquo;s protocol sets.|Separate::Seat the patient apart from others in time or space, per protocol, before connection where possible.|Ask and examine::Cough duration, blood in the sputum, night sweats, weight loss, contacts. Temperature, oxygen saturation, and the chest.|Call::The attending nephrologist, before the patient is placed on the general floor.|Record::Symptoms, where the patient dialyzed, and who was nearby.}}
{{call:Stop and call the attending nephrologist before placing a patient on the general floor when there is cough for two weeks or more, blood in the sputum, night sweats with weight loss, an unexplained fever pattern, or known or suspected active tuberculosis. Mask and separate the patient per your unit&rsquo;s protocol while you call.}}
{{key:In a dialysis patient, tuberculosis may come without a cough, without a high fever, and with a negative test. Keep it on your list when a patient loses weight or has fluid around the lung or heart.}}
"""),
        ("covid", "Respiratory outbreaks", "Lessons From COVID-19 for the Next Respiratory Outbreak", """
<p>A dialysis patient cannot stay home when a respiratory virus spreads.</p>
<p>In the European Renal Association COVID-19 Database (ERACODA), 768 dialysis patients with COVID-19 in early 2020 had a 28-day probability of death of 25.0% (95% confidence interval 20.2% to 30.0%). Age and frailty were the main factors associated with death.[[hilbrands2020]] At the Philippine General Hospital, 25% of 68 hemodialysis patients admitted with COVID-19 in 2020 died in hospital. A low ratio of arterial to inspired oxygen (PaO<sub>2</sub>/FiO<sub>2</sub>) and the need for ventilation were independently associated with death, with wide confidence intervals in this small cohort.[[tomacruz2021]] Both were observational studies from before vaccines. Later, a research letter from the United Kingdom reported reduced neutralizing antibody responses after vaccination in hemodialysis patients.[[carr2021]] Antibody level is a surrogate, not a measure of protection from severe illness.</p>
<div class="table-wrap"><table>
<thead><tr><th>Lesson</th><th>What you do on your shift</th></tr></thead>
<tbody>
<tr><td>Screen at the door</td><td>Confirm the screening questions were asked. Check temperature</td></tr>
<tr><td>Mask and separate</td><td>Apply the unit&rsquo;s separation in time or space before connection</td></tr>
<tr><td>Cohort when cases rise</td><td>Follow the Medical Director&rsquo;s cohort plan</td></tr>
<tr><td>Staff stay home when ill</td><td>Report your own symptoms. Support colleagues who report theirs</td></tr>
<tr><td>Keep patients dialyzed</td><td>A missed session brings fluid overload and high potassium. Do not send a stable patient home without a plan (Module 30)</td></tr>
</tbody></table></div>
<p>These lessons come from pandemic practice, not graded recommendations.</p>
{{key:When a respiratory outbreak starts, ask the same questions as for tuberculosis: who has symptoms, where do they sit, and who decides where they dialyze.}}
"""),
        ("vaccines", "Vaccines", "Vaccines for Patients and Staff", """
<p>A dialysis patient&rsquo;s immune system answers a vaccine more quietly. It may need more doses, and someone has to check that the answer came.</p>
<p>The picture has a limit. The quiet answer comes from specific steps. A vaccine works when helper T cells, shown the vaccine protein, help B cells make antibody and memory. Kidney failure may weaken these steps, so antibody levels are lower, more people do not respond, and levels fall sooner. That is why dialysis vaccination ends with a blood test.</p>
<h3>Hepatitis B</h3>
<p>CDC 2001 recommends hepatitis B vaccination for all susceptible hemodialysis patients and all staff, anti-HBs one to two months after the last primary dose, revaccination and retesting of nonresponders, and yearly retesting of responders.[[cdc2001]] The Advisory Committee on Immunization Practices (ACIP) of 2018 recommends post-vaccination testing for hemodialysis patients, yearly anti-HBs to judge the need for a booster, and a booster when anti-HBs falls below 10 mIU/mL.[[acip_hbv2018]] The product, doses, and timing are set by your unit&rsquo;s protocol and the attending nephrologist.</p>
<p>A retrospective cohort from one United States dialysis organization studied 3,509 vaccine-naive dialysis patients. After a first series, 62.9% given a four-dose recombinant vaccine and 50.1% given a two-dose adjuvanted vaccine reached anti-HBs above 10 mIU/mL. Patients given up to four adjuvanted doses reached 82.0%.[[manley2023]] Anti-HBs is a surrogate for protection, not a count of infections prevented, and the best schedule remains uncertain.</p>
<h3>Influenza and pneumococcal vaccines</h3>
<p>In a registry of 118,533 United States hemodialysis patients, only 21% had received pneumococcal vaccine. Vaccination was associated with lower mortality (hazard ratio 0.94, 95% confidence interval 0.90 to 0.98), and pneumococcal plus influenza vaccination with a hazard ratio of 0.73 (0.68 to 0.78).[[gilbertson2011]] The study was observational. People who accept vaccines may be healthier in ways the analysis cannot see, so the size of the benefit is uncertain.</p>
<div class="table-wrap"><table>
<thead><tr><th>Vaccine</th><th>Who</th><th>How response is checked</th><th>Who orders it</th></tr></thead>
<tbody>
<tr><td>Hepatitis B</td><td>Every susceptible patient</td><td>Anti-HBs one to two months after the series, then yearly in responders[[cdc2001]]</td><td>Attending nephrologist, per unit protocol</td></tr>
<tr><td>Hepatitis B</td><td>Every staff member</td><td>Anti-HBs on file. A second series and retest if below 10 mIU/mL[[acip_hbv2018]]</td><td>Unit&rsquo;s employee health policy</td></tr>
<tr><td>Influenza</td><td>Patients and staff, per national program</td><td>No routine antibody test</td><td>Attending nephrologist and unit protocol</td></tr>
<tr><td>Pneumococcal</td><td>Patients, per national program</td><td>No routine antibody test</td><td>Attending nephrologist and unit protocol</td></tr>
</tbody></table></div>
{{formula:<strong>Worked example 3: vaccine response (illustrative arithmetic).</strong><br>Formula: response rate = patients with anti-HBs of 10 mIU/mL or more &divide; patients tested &times; 100.<br>Of 120 patients tested one to two months after the series, 75 have anti-HBs above 10 mIU/mL.<br>Response = 75 &divide; 120 &times; 100 = 62.5%, close to the 62.9% reported after a four-dose recombinant series.[[manley2023]]<br>Nonresponders = 120 &minus; 75 = 45. Their names go to the attending nephrologist for revaccination per CDC 2001 and the unit protocol.<br><em>What the number does and does not tell you:</em> it measures a surrogate in this group on this date. It does not show who will be protected next year, because levels fall.}}
{{key:A vaccinated dialysis patient is not a protected patient until the anti-HBs result shows it. Until then, treat the patient as susceptible.}}
"""),
        ("exposure", "Needlestick", "Needlestick and Blood Splash: The First Hour", """
<p>Dialysis staff handle large hollow needles filled with blood every shift. The risk after an injury depends on the source patient&rsquo;s virus, the amount of blood, the depth of the injury, and the worker&rsquo;s immunity. The first hour is for washing and for gathering the facts the exposure clinician needs.</p>
{{flow:Needlestick or blood splash: the first hour|Wash::Wash a wound or skin with soap and water. Flush the eyes, nose, or mouth with plenty of clean water.|Report::Tell the head nurse and the unit&rsquo;s designated exposure clinician at once.|Source::Identify the source patient and pull the latest serology. Testing of the source follows consent and protocol.|Worker::Find the worker&rsquo;s hepatitis B vaccine record and anti-HBs result.|Designated clinician::Make sure the worker reaches the designated clinician without delay. Do not prescribe outside your unit&rsquo;s protocol.|Document::Time, device, depth, body site, source, first aid, and who was informed.}}
<p>The 2025 United States Public Health Service guideline replaced the 2013 guideline on occupational HIV exposure. It brings new regimens for HIV postexposure prophylaxis, a shorter period of follow-up HIV testing, no routine laboratory tests for drug toxicity, and considerations for sources with an undetectable viral load. Prompt reporting, expert consultation, and follow-up remain the principles. Its recommendations use GRADE with the Healthcare Infection Control Practices Advisory Committee (HICPAC) scheme, or are good practice statements.[[phs_hivpep2025]]</p>
<p>For hepatitis B, management depends on the worker&rsquo;s vaccine response and the source&rsquo;s HBsAg. A worker with documented anti-HBs of 10 mIU/mL or more needs no hepatitis B postexposure management, whatever the source&rsquo;s status. For an unvaccinated worker, the source is tested for HBsAg as soon as possible.[[acip_hbv2018]]</p>
{{formula:<strong>Worked example 4: a needlestick at 3:00 p.m. (decision walk-through, illustrative).</strong><br>A nurse is stuck by a used fistula needle. The source patient is anti-HCV positive, HIV negative, and HBsAg negative on the chart.<br>Steps 1 to 3: she washes the site; the head nurse and exposure clinician are told at 3:05 p.m.; the source results and dates are confirmed.<br>Step 4: her anti-HBs of 85 mIU/mL, measured after her completed vaccine series, is on file, so hepatitis B postexposure management is not needed.[[acip_hbv2018]]<br>Step 5: the designated clinician sees her within the hour and decides on HIV prophylaxis and hepatitis C follow-up per protocol.[[phs_hivpep2025]] The event is documented.<br><em>What this does and does not tell you:</em> the source&rsquo;s status guides the clinician&rsquo;s decision but does not replace it, and a months-old test may not reflect today.}}
{{call:Stop and call for every needlestick, cut with a used instrument, or splash of blood or body fluid onto a mucous membrane or broken skin, whether or not the source is known to be positive. Start first aid, follow your unit&rsquo;s exposure protocol, and inform the designated clinician and the attending nephrologist.}}
<h3>What is uncertain</h3>
<ul>
<li>KDIGO advises against dedicated machines (1D) and isolation (2C) for hepatitis C on low to very low certainty evidence, and some regulators and units require more.[[kdigo_hcv2022]]</li>
<li>The best hepatitis B vaccine product, dose count, and booster timing for dialysis patients are uncertain; comparative data are retrospective.[[manley2023]]</li>
<li>Tuberculosis tests miss infection in dialysis patients, the WHO recommendation rests on low-certainty evidence, and Philippine data on tuberculosis in dialysis patients were not found.[[romanowski2016]][[who_tpt2024]]</li>
</ul>
{{key:After an exposure, the facts you gather in the first hour decide what the clinician can offer. Wash, report, find both results, and get the worker seen.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you do now?</strong> Act as if the result were true until confirmed or disproved. Mrs. Aquino is stable, and her blood is in a closed circuit. Whether she finishes at station 9 under strict precautions or ends early is decided with the attending nephrologist, whom you call now. Three things change at once. One nurse cares for her alone, because the CDC staff rule does not allow Nurse Cruz to care for an HBsAg-positive patient and two susceptible neighbors at the same time. The station and machine are disinfected after she leaves, per protocol, and her next sessions are planned in the hepatitis B room unless confirmation is negative.</p>
<p><strong>What does it mean?</strong> A reactive HBsAg usually means hepatitis B virus is in her blood now. Her test was negative a month ago, so if this is real, it is a new infection. Check for a labeling error and for a recent vaccine dose. The nephrologist will likely order repeat HBsAg, total and IgM anti-HBc, anti-HBs, ALT, and hepatitis C markers, since the same breaches spread both viruses. Her week in another unit is one possible source, but your unit still needs a look-back. With no anti-HBs on record, she was never shown to be protected.</p>
<p><strong>Whom do you call, and what is said and written?</strong> The attending nephrologist now, and the Medical Director the same day. Mrs. Aquino is told in private after the nephrologist has reviewed the result: what the test shows, what needs confirming, and why her station is changing. You write the call, the result, the advice, the staff reassignment, the stations and shift, and her condition. A confirmed infection is reported to the health authority as the regulation requires, and enters the quality process of Module 31. The look-back covers every patient beside her since her last negative result.</p>
"""],
    "skills": {"title": "Hand hygiene and station changeover audit",
               "intro": "Observe a nurse or a colleague through one patient changeover at a dialysis station, with your preceptor beside you. Then perform the same changeover yourself while your preceptor observes.",
               "items": [
                   ("Performs hand hygiene before approaching the station and before putting on gloves.", False),
                   ("Changes gloves and performs hand hygiene between patients, and between dirty and clean tasks at the same patient.", True),
                   ("Does not carry items from one station to another without disposal or disinfection.", False),
                   ("Prepares medicines in the designated clean area, not at the station, and uses single-dose vials per protocol.", True),
                   ("Cleans and disinfects the chair, machine surfaces, and touched items after the patient leaves and before the next patient sits.", False),
                   ("Checks the next patient&rsquo;s serology status, its date, and the station assignment before connection.", False),
                   ("For an HBsAg-positive patient, confirms the separate room, dedicated machine, supplies, and staff assignment.", True),
                   ("Disposes of sharps immediately at the point of use in a puncture-proof container.", False),
                   ("Recognizes and reports visible blood on surfaces.", False),
                   ("States the first steps after a needlestick and names the unit&rsquo;s designated exposure clinician.", False),
                   ("Records the audit and gives feedback to the observed staff member in private.", False),
               ],
               "placement": "For two weeks, observe one changeover on each of your shifts and record what you see on the audit form. Review the results with your preceptor, and present one practice the unit could improve to the head nurse and the Medical Director."},
    "quiz": [
        ("In the outbreaks described, how did hepatitis C usually spread?",
         ["The internal fluid pathway of shared machines",
          "Hands, gloves, shared items, and contaminated surfaces",
          "Contaminated dialysis water",
          "Airborne droplets between neighboring chairs"], 1,
         "Cases clustered at neighboring stations, and a shared machine explained only 1 of 11 cases in Vietnam."),
        ("Why does hepatitis B spread more easily at a dialysis station than HIV?",
         ["Hepatitis B is spread through air",
          "HIV is destroyed by the dialyzer",
          "Hepatitis B reaches very high levels in blood and survives for days on surfaces",
          "Dialysis patients are immune to HIV"], 2,
         "CDC describes very high blood levels and survival for at least 7 days on surfaces."),
        ("Under the CDC recommendations, which arrangement is correct for a patient positive for HBsAg?",
         ["A separate room and dedicated machine, with staff who do not care for susceptible patients at the same time",
          "The general area with standard precautions only",
          "A dedicated machine in the general area, with any staff assignment",
          "Dialysis only in a hospital"], 0,
         "The room and equipment rule comes with a staff rule."),
        ("What does KDIGO 2022 recommend about dedicated machines for patients with hepatitis C?",
         ["Dedicated machines are recommended (1A)",
          "Dedicated machines are suggested when the unit is busy (2C)",
          "The guideline makes no statement",
          "Not using dedicated machines (1D)"], 3,
         "KDIGO relies on standard infection control. Grade D means very low certainty, and some units keep stricter rules."),
        ("A new patient&rsquo;s panel shows HBsAg negative, anti-HBs 150 mIU/mL, and anti-HBc negative. What does it mean?",
         ["Immune by vaccination",
          "Immune after past infection",
          "Current hepatitis B infection",
          "Susceptible to hepatitis B"], 0,
         "Anti-HBs without anti-HBc is the footprint of the vaccine."),
        ("After a month of dialysis abroad, a patient is anti-HCV negative and HCV RNA positive. What is most likely?",
         ["A false-positive RNA test that can be ignored",
          "A recent infection in the window before antibody appears",
          "An old infection that has been cured",
          "Immunity to hepatitis C"], 1,
         "Antibody appears weeks after infection, so this pattern marks new infection."),
        ("A patient has positive anti-HBc with negative HBsAg and negative anti-HBs. What does CDC advise?",
         ["Move the patient to the hepatitis B room at once",
          "Ignore the result",
          "Retest, because isolated anti-HBc is often a false positive; isolation is not needed",
          "Start antiviral treatment"], 2,
         "Most isolated anti-HBc results are false positives, and HBsAg is not detectable."),
        ("A unit follows 60 hepatitis C-negative patients for 5 months and finds 1 new conversion. What is the rate per 100 patient-months?",
         ["1.7",
          "0.2",
          "0.33",
          "3.3"], 2,
         "Patient-months = 60 &times; 5 = 300. Rate = 1 &divide; 300 &times; 100 = 0.33."),
        ("At 9:00 a.m., a patient at hour one in the general area has a new reactive HBsAg. What comes first?",
         ["Tell her the diagnosis at the chair so she understands the move",
          "Wait for confirmation before changing anything",
          "Stop dialysis and send her home",
          "Call the attending nephrologist and separate her nurse from the susceptible neighbors"], 3,
         "Act as if the result is true until confirmed; disclosure happens in private."),
        ("Why can a dialysis patient with active tuberculosis have a negative interferon-gamma release assay?",
         ["The test measures a T-cell response that kidney failure weakens",
          "Dialysis removes the bacteria from the blood",
          "The test detects only tuberculosis outside the lungs",
          "Heparin interferes with the test"], 0,
         "Both tests depend on T-cell memory, blunted in kidney failure."),
        ("A man arrives with three weeks of cough, night sweats, and weight loss. What do you do first?",
         ["Connect him at his usual station",
          "Send him home without dialysis",
          "Mask and separate him, and call the attending nephrologist before he is placed on the floor",
          "Start antituberculosis drugs"], 2,
         "These features suggest active tuberculosis; the nephrologist and Medical Director decide where he dialyzes."),
        ("In 3,509 vaccine-naive dialysis patients, what share reached protective anti-HBs after a four-dose recombinant series?",
         ["About 95%",
          "About 63%",
          "About 30%",
          "About 82%"], 1,
         "It was 62.9%, which is why the antibody is checked after every series."),
        ("What is the main limitation of the registry linking pneumococcal and influenza vaccination to lower mortality?",
         ["The study was too small",
          "The vaccines were given at the wrong time",
          "It measured antibody levels only",
          "It was observational, so healthier patients may have been more likely to be vaccinated"], 3,
         "A healthy-vaccinee bias can make a vaccine look more protective than it is."),
        ("A nurse with documented anti-HBs of 90 mIU/mL is stuck by a needle from an HBsAg-positive patient. What hepatitis B management is needed?",
         ["None for hepatitis B, although the exposure is still reported and managed for other viruses",
          "Hepatitis B immune globulin in all cases",
          "A full new vaccine series",
          "Removal from patient care for six months"], 0,
         "Documented protection means no hepatitis B postexposure management. The HIV and hepatitis C pathway still applies."),
        ("A nurse is splashed in the eye with blood during disconnection. What is the correct first sequence?",
         ["Finish the disconnection, then report at the end of the shift",
          "Flush the eye, report at once, gather both serology results, and get the nurse to the designated clinician",
          "Start postexposure prophylaxis from unit stock without consulting anyone",
          "Test the nurse for HIV and wait for the result"], 1,
         "A mucous-membrane splash is an exposure. The 2025 guideline stresses prompt reporting and expert consultation."),
    ],
    "terms": [("Standard precautions", "Practices used for every patient: hand hygiene, gloves, safe sharps and medicine handling, and cleaning."),
              ("HBsAg", "Hepatitis B surface antigen. A positive test usually means current hepatitis B infection."),
              ("Anti-HBs", "Antibody to hepatitis B surface antigen. A level of 10 mIU/mL or more after vaccination means protection."),
              ("Anti-HBc", "Antibody to the hepatitis B core protein. It marks past or present infection, never vaccination."),
              ("Anti-HCV", "Antibody to hepatitis C. It shows exposure and stays positive after recovery or cure."),
              ("HCV RNA", "The genetic material of hepatitis C. A positive test means the virus is present now."),
              ("Window period", "The weeks after infection when the virus is present but the antibody test is still negative."),
              ("Seroconversion", "A change from a negative to a positive test result."),
              ("Interferon-gamma release assay (IGRA)", "A blood test for tuberculosis infection that measures a T-cell response."),
              ("Postexposure prophylaxis (PEP)", "Treatment given soon after an exposure to lower the chance of infection.")],
    "readings": [("viral-infections-vaccinations-ckd.html", "Hepatitis B, hepatitis C, HIV, and the vaccines used in kidney disease."),
                 ("tuberculosis-kidney-disease.html", "How tuberculosis presents and is screened for in people with kidney failure."),
                 ("dialysis-machine-assignment.html", "How machines and stations are assigned by serology status.")],
    "calcs": ["calc-access-infection-rate.html", "calc-qapi-run-chart-spc.html", "calc-dialysis-qapi-scorecard.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
