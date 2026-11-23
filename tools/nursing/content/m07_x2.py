# -*- coding: utf-8 -*-
# Module 7 expansion, part 2: tuberculosis, the unit vaccination program, and respiratory-virus seasons.
OBJECTIVES = [
    "Recognize the higher risk and often atypical presentation of tuberculosis in patients on hemodialysis, and apply symptom screening, cough triage, masking, separation, and reporting in an open dialysis unit.",
    "Run the unit vaccination program for patients and staff, including hepatitis B antibody follow-up, yearly influenza vaccine, pneumococcal and coronavirus disease 2019 (COVID-19) vaccines, and a recording and recall system.",
    "Apply respiratory-virus season measures in the unit, recognize a possible outbreak, and report it through the infection-control system.",
]
EXTRA = [
    {"after": "program", "id": "tb", "nav": "Tuberculosis", "tag": "Clinical application",
     "h2": "Tuberculosis in the dialysis unit",
     "html": """
<p>The blood-borne viruses earlier in this module travel through blood and contaminated surfaces. Tuberculosis travels through the air. A person with infectious lung or throat disease releases tiny droplets when coughing, sneezing, singing, or talking. Those droplets can stay suspended in a room for a long time. Now picture a dialysis unit: many patients sitting near one another for four hours, several times a week, for years. One undiagnosed case can expose many people.</p>
<p><strong>Why patients on dialysis are at higher risk.</strong> Kidney failure weakens the part of the immune system that keeps tuberculosis in check. Malnutrition, diabetes, older age, and crowded living conditions add to the risk. Many patients were infected in the past, often without knowing it, and can develop active disease when their immunity falls. A review of the evidence concluded that patients on dialysis and transplant recipients appear to have a higher risk of tuberculosis than the general population, and that screening and diagnostic tests perform less well in them.[[romanowski2016]] The Philippines has one of the highest tuberculosis burdens in the world. A Filipino patient on dialysis therefore carries both a higher personal risk and a higher chance of past exposure.</p>
<p><strong>The presentation is often atypical.</strong> In dialysis patients, tuberculosis outside the lungs is relatively common: in the lymph nodes, the pleura, the abdomen, or the bones. The early signs look like kidney failure itself: low-grade fever, night sweats, poor appetite, weight loss, fatigue, a new pleural effusion, or swollen lymph nodes in the neck. Report a patient whose appetite and weight keep falling despite adequate dialysis, or who has unexplained fever, so that the physician can consider tuberculosis. Writing &ldquo;poor appetite, probably uremic&rdquo; is not enough.</p>
<p><strong>Symptom screening of patients.</strong> Ask every new or visiting patient the screening questions before the first treatment. Rescreen current patients at the interval the unit policy sets, and whenever symptoms appear. The questions follow the national program&rsquo;s screening form. The usual ones cover:</p>
<ul>
<li>cough, especially a cough lasting two weeks or more, or any cough with blood;</li>
<li>fever, often in the afternoon or evening, and night sweats;</li>
<li>unexplained weight loss or loss of appetite;</li>
<li>contact at home or at work with a person on tuberculosis treatment;</li>
<li>previous tuberculosis treatment, and whether it was completed.</li>
</ul>
<p>The physician orders the chest X-ray and laboratory tests. Your part is to ask the questions the same way every time, record the answers, and act on a positive screen at once, not at the end of the shift.</p>
<p><strong>Cough triage and masking.</strong> Identify a patient with a significant cough at the door, not after the patient reaches the station. Give a surgical mask and show how to wear it over the nose and mouth. Keep the patient apart from others while the charge nurse and physician on duty decide where and when the treatment can safely take place. A mask on the patient limits what reaches the air. It is the single most useful immediate step. Mask companions who cough as well.</p>
<p><strong>Airborne precautions in an open unit.</strong> Most Philippine outpatient units are open rooms without a negative-pressure isolation room. A patient with suspected or confirmed infectious tuberculosis is therefore managed under a written plan that the physician and the infection-control officer apply case by case. Depending on the facility, the plan may include:</p>
<ul>
<li>treatment in a hospital airborne-isolation room until the patient is judged non-infectious;</li>
<li>scheduling on the last shift of the day, at the station farthest from other patients and closest to an exhaust fan or open window, with nobody seated nearby;</li>
<li>the patient masked for the entire session, including arrival and departure;</li>
<li>staff caring for the patient wearing a fitted N95 or equivalent respirator, as fit-tested under the facility&rsquo;s occupational health program, rather than a surgical mask;</li>
<li>a small number of named staff assigned, so that the exposed group is known.</li>
</ul>
<p>Tuberculosis does not travel through the blood circuit. Clean and disinfect the machine and station with the standard procedure taught earlier in this module. No special machine is needed. The physician decides, under the unit&rsquo;s policy, when airborne precautions begin and end and when the patient returns to an ordinary station. Do not relax precautions because a patient feels better or because a station is needed for someone else.</p>
<p><strong>Latent infection.</strong> A person can carry tuberculosis bacteria without symptoms and without being infectious. This is latent infection, and it can later turn into active disease. Screening for latent infection is part of the evaluation for a kidney transplant,[[txcand2020]] and some units screen dialysis patients as policy. The tuberculin skin test is often falsely negative in kidney failure, so many centers prefer an interferon-gamma release assay, a blood test. The choice of test and any preventive treatment are physician decisions. You make sure ordered tests are done and results reach the chart. You also explain that a positive test for latent infection is not the same as being contagious.</p>
<p><strong>Treatment and reporting.</strong> Tuberculosis is reportable. Patients with active disease are notified to the Department of Health (DOH) National Tuberculosis Control Program through the facility&rsquo;s designated process. Their treatment is usually given as directly observed treatment, coordinated with a health center or treatment facility in the program. Some tuberculosis medicines are removed by dialysis or need dose changes in kidney failure, so the physician orders the timing of doses on dialysis days. Doses scheduled after a session may be given and observed in the unit if the plan says so. Confirm that the dialysis unit and the treatment facility know about each other. Record doses given in the unit. Report missed doses, side effects such as jaundice, vision change, or numbness, and any interruption of treatment. Treatment stopped early is a leading cause of drug-resistant tuberculosis.</p>
<p><strong>Contact tracing and staff exposure.</strong> When a patient is found to have infectious tuberculosis after sitting on the open floor, the physician and infection-control officer decide who counts as a contact. You help by listing, from the station and assignment records, who shared the shift and the nearby stations, which staff cared for the patient, and for how long. Exposed staff follow the occupational health pathway for screening and follow-up. They do not arrange their own tests informally. A staff member with symptoms of tuberculosis reports them and stays away from patient care until assessed and cleared, under the same rules as any infectious illness among staff.</p>
<p><strong>Mask the cough at the door, separate the patient, and report the same hour. A falling appetite with fever is tuberculosis until someone has looked.</strong></p>
"""},
    {"after": "tb", "id": "vaccination", "nav": "Vaccination program", "tag": "Evidence",
     "h2": "The unit vaccination program",
     "html": """
<p>Vaccines work less well in kidney failure than in healthy adults. The same weakened immune response that raises the risk of infection also blunts the response to a vaccine. They remain an important part of dialysis care, because they are safe and because infection is so common in these patients. A practical review notes that most guidance for people with kidney disease focuses on hepatitis B, influenza, and pneumococcal vaccines, in addition to the vaccines recommended for every adult of the same age.[[krueger2020]] The same review notes that studies have suggested better responses when vaccines are given before dialysis starts, which is one reason to raise vaccination early in chronic kidney disease care.[[krueger2020]] Most of these studies measure an antibody level, which is a surrogate. The review notes that more data are needed on how well the vaccines prevent actual infection in this group.[[krueger2020]]</p>
<p>The dialysis unit sees its patients more often than any other part of the health system, so it is the natural place to run the program. Running it is largely nursing work: knowing who is due, making sure the order is written, giving the vaccine where the unit does so, and recording it so that the next person can find it.</p>
<p><strong>Hepatitis B: the program in detail.</strong> The summary table earlier in this module listed the parts. These are the details you apply:[[cdc2001]]</p>
<ul>
<li><strong>Who.</strong> Every patient and staff member who is susceptible: without protective antibody and not already infected.</li>
<li><strong>Dose and schedule.</strong> Patients on dialysis receive a dialysis formulation or a higher-dose schedule, according to the product used and current DOH and CDC guidance. The adult schedule for staff is different. The dose and schedule are written in the order, and you check the product label against it. The vaccine is given by intramuscular injection into the deltoid muscle of an adult. A series begun before dialysis is completed at the higher dose recommended for hemodialysis (HD) patients.</li>
<li><strong>Antibody check.</strong> The antibody to hepatitis B surface antigen is measured 1 to 2 months after the last dose of the series. A level of at least 10 mIU/mL counts as a response.</li>
<li><strong>Non-response.</strong> A patient or staff member who does not respond receives one more complete series and is tested again. No further doses are recommended after a second series without response. That person remains susceptible and is managed as such, including the monthly HBsAg testing that applies to susceptible patients.</li>
<li><strong>Follow-up.</strong> In patients who responded, the antibody level is checked every year, and a booster dose is given if it has fallen below 10 mIU/mL. Staff who responded do not need booster doses or routine retesting.</li>
</ul>
<p><strong>Influenza.</strong> Influenza vaccine is given every year, because the circulating strains change and protection fades. Include patients and staff. Staff vaccination also protects patients, who can catch influenza from the people caring for them. The formulation and timing follow the vaccine available in the Philippines for the season and current DOH advice. An annual campaign at the chair, on dialysis days, usually reaches more patients than a referral to another clinic.</p>
<p><strong>Pneumococcal vaccine.</strong> Pneumococcal pneumonia and bloodstream infection are serious in dialysis patients. Several pneumococcal vaccine products exist, and the recommended product, sequence, and interval between doses have changed over time. The physician orders them according to current guidance. Your task is to know which products the patient has already received, and when, so that doses are neither missed nor repeated.</p>
<p><strong>Coronavirus disease 2019 (COVID-19).</strong> COVID-19 vaccination and booster doses follow current DOH guidance, which has changed repeatedly and will change again. Check the current advisory. Do not rely on what was recommended in an earlier year.</p>
<p><strong>Recording and recall.</strong> A vaccination program fails quietly, through missing dates, not through dramatic errors. A workable system has these parts:</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>A vaccination register for each patient</td><td>Product, lot number, dose, date, site, and who gave it, for every vaccine, including those given elsewhere when the patient brings proof</td></tr>
<tr><td>Antibody results beside the hepatitis B entries</td><td>Shows at a glance whether a patient is a responder, a non-responder, or due for the yearly check</td></tr>
<tr><td>A due list reviewed each month</td><td>Names patients due for a dose, an antibody test, or the yearly influenza vaccine, so that orders can be obtained in advance</td></tr>
<tr><td>Declinations recorded</td><td>A patient who declines is given information, the decision is respected and recorded, and the offer is repeated at the next due date</td></tr>
<tr><td>A staff register kept by occupational health</td><td>Hepatitis B series and antibody result for every staff member, influenza each year, and other vaccines under facility policy</td></tr>
<tr><td>A copy for the patient</td><td>A card or booklet the patient carries, which travels with them to other units and hospitals</td></tr>
</tbody></table></div>
<p>Vaccine handling follows the cold chain. Keep vaccines in a dedicated refrigerator with a temperature log, never in the door or beside food. Set aside and report a vaccine exposed to the wrong temperature. Do not use it. Coverage figures, such as the proportion of patients with a documented influenza vaccine this season, belong on the unit dashboard described in Module 12.</p>
<p><strong>A completed series is not protection. The antibody result is. Record it, and recall the patient when it is due.</strong></p>
"""},
    {"after": "vaccination", "id": "respiratory", "nav": "Respiratory seasons", "tag": "Clinical application",
     "h2": "Respiratory-virus seasons in the unit",
     "html": """
<p>Influenza, COVID-19, respiratory syncytial virus, and the many viruses that cause colds spread readily in a dialysis unit. Most clinic patients can stay home when they are unwell. Dialysis patients cannot. Missing treatment is dangerous. So the unit has to treat people who may be infectious while protecting everyone else in the room. In the Philippines, respiratory illness tends to rise during the rainy season and at other times of the year too. Apply the measures below whenever local cases rise, not only in a fixed month.</p>
<p><strong>Screening at entry.</strong> Ask every patient and companion about symptoms before they enter the treatment floor: fever or chills, cough, sore throat, runny nose, shortness of breath, loss of smell or taste, and close contact with a sick household member. Check temperature where the unit policy requires it. Ask patients to call ahead if they become unwell, so that the unit can prepare a place for them. Tell them plainly that being sick is not a reason to skip dialysis.</p>
<p><strong>Masks and hand hygiene.</strong> A patient or companion with respiratory symptoms wears a surgical mask from arrival to departure. In a season of high transmission the unit may require masks for everyone on the floor. Follow the current policy. Place hand hygiene stations and tissues at the entrance and in the waiting area, where crowding is often worse than on the treatment floor.</p>
<p><strong>Separating symptomatic patients.</strong> Seat a patient with symptoms at a station set aside under the unit policy, as far from others as the floor plan allows. Where possible, the same staff care for that patient for the whole session. Some units group symptomatic patients on one shift, or treat a patient with confirmed COVID-19 or influenza on a designated shift or in an isolation room. The physician and the infection-control officer decide these arrangements and how long they last. You apply them. Do not move a patient back to an ordinary station on your own judgment. The hepatitis B isolation rules still apply in full. A patient with hepatitis B who also has a respiratory illness is never moved into the general area to make room.</p>
<p><strong>Cleaning.</strong> The standard cleaning and disinfection of the station after each patient, taught earlier in this module, is enough for respiratory viruses on surfaces. In a season of high transmission, clean high-touch surfaces in shared areas more often: the weighing scale, chair arms in the waiting area, door handles, and the reception counter.</p>
<p><strong>Staff illness.</strong> If you have fever or a new respiratory illness, report it to the head nurse before the shift and do not come to work ill. A unit that rewards attendance at any cost will be staffed by people spreading infection to patients. The facility&rsquo;s policy sets testing, the period off work, and the conditions for return. Staff follow them, and managers plan cover so that reporting sick is possible without leaving patients unsafe.</p>
<p><strong>Recognizing a possible outbreak.</strong> A working rule many infection-control programs use: two or more cases of the same respiratory illness, linked in time and place within a few days, are a possible outbreak until shown otherwise. &ldquo;Linked&rdquo; means, for example, patients on the same shift, or a patient and the staff member who cared for them. This is a convention, not a cited standard, and the unit&rsquo;s own policy sets the exact definition. When you notice the pattern, do not wait to be certain:</p>
<ol>
<li>Tell the head nurse and the physician on duty the same day, with the names, dates of onset, shifts, and stations.</li>
<li>The infection-control officer is informed and decides on testing, added precautions, and whether to change seating or shifts.</li>
<li>Reporting to the DOH follows the facility&rsquo;s surveillance process for notifiable diseases. You supply accurate information and do not report on your own outside that process.</li>
<li>Patients and staff are told what they need to know, without naming the people who are ill.</li>
</ol>
<p><strong>Dialysis cannot be skipped, so the unit must make it safe to come in sick. Mask, separate, and report a second linked case the same day.</strong></p>
"""},
]
QUIZ = [
    {"stem": "A patient arrives for his usual session with a cough that he says has lasted three weeks, night sweats, and a weight loss of 3 kg over the past month. The unit is an open room with no isolation room, and every station is occupied on this shift. What do you do first?",
     "options": [
         ("Seat him at his usual station and start treatment, since tuberculosis is not spread through the dialysis circuit", False, "Tuberculosis spreads through the air, not the circuit; seating him among other patients without masking or separation exposes everyone nearby."),
         ("Give him a surgical mask, keep him apart from other patients, and inform the charge nurse and physician so that a safe place and time for treatment can be decided", True, "Masking the coughing patient and separating him at once reduces airborne spread. Where and when he is dialyzed, and any testing, are decided by the physician under the unit plan, and the screen is recorded."),
         ("Send him home and ask him to return after a chest X-ray shows he is not infectious", False, "A patient on dialysis cannot safely miss treatment. The unit must arrange a safe place to dialyze him while the evaluation proceeds."),
         ("Ask him to wear an N95 respirator and treat him at his usual station", False, "A surgical mask is the appropriate mask for the patient; fitted respirators protect staff. Separation from other patients is still needed, and the decision on placement belongs to the physician and infection-control officer."),
     ],
     "objective": "Recognize the higher risk and often atypical presentation of tuberculosis in patients on hemodialysis, and apply symptom screening, cough triage, masking, separation, and reporting in an open dialysis unit.", "sources": ["romanowski2016"], "flag": "Placement of a patient with suspected infectious tuberculosis in an open unit is set by facility policy; no national rule was verified."},
    {"stem": "A patient completed his hepatitis B vaccine series at the dialysis dose. An antibody test 6 weeks after the last dose shows a level below 10 mIU/mL. He has never had a second series. What is the appropriate next step?",
     "options": [
         ("Record him as immune because he has completed the series", False, "Completing the series does not establish protection; the antibody result does, and his is below the level taken as a response."),
         ("Arrange, by order, one more complete series and repeat the antibody test afterward, and keep him under monthly HBsAg testing", True, "A non-responder receives one additional complete series and is retested. Until he responds he remains susceptible, including monthly HBsAg testing."),
         ("Give a single booster dose and stop testing", False, "A single booster is for responders whose antibody has fallen over time; a non-responder to the primary series needs a full second series and a repeat test."),
         ("Assign him to the hepatitis B isolation station because he is not protected", False, "The isolation station is for patients who are HBsAg-positive. Seating a susceptible patient there would expose him to infection."),
     ],
     "objective": "Run the unit vaccination program for patients and staff, including hepatitis B antibody follow-up, yearly influenza vaccine, pneumococcal and coronavirus disease 2019 (COVID-19) vaccines, and a recording and recall system.", "sources": ["cdc2001"], "flag": ""},
]
TERMS = [
    ("Latent tuberculosis infection", "Infection with tuberculosis bacteria without symptoms or infectiousness, which can later become active disease."),
    ("Interferon-gamma release assay", "A blood test for tuberculosis infection, often preferred over the skin test in kidney failure."),
    ("Directly observed treatment", "Tuberculosis treatment in which a health worker or trained observer watches each dose being taken."),
    ("Cough triage", "Identifying patients with a cough at entry, masking them, and separating them from others before they reach the treatment floor."),
    ("Airborne precautions", "Measures against infections spread through the air: patient masking, separation or an isolation room, ventilation, and fitted respirators for staff."),
    ("Hepatitis B non-responder", "A person whose antibody level stays below 10 mIU/mL after a complete vaccine series."),
    ("Outbreak (working definition)", "Two or more linked cases of the same infection in the same place and period; the exact definition is set by unit policy."),
]
FLAGS = [
    "Philippine tuberculosis burden is stated qualitatively; the WHO Philippines country office (November 2025) reported that the Philippines had about 6.8% of the world's estimated cases in 2024 and an incidence of 625 per 100,000, which could be added with a WHO reference if a non-PubMed reference key is created.",
    "Program name 'National Tuberculosis Control Program' follows the DOH manual of procedures; the current national plan is PhilSTEP2 (2025-2030). Confirm the program name and reporting route at each review.",
    "The two-week cough criterion follows common national screening practice and was not verified against the current DOH screening form.",
    "No tuberculosis, influenza, or pneumococcal recommendations appear in CDC 2001; those statements rest on Romanowski 2016 and Krueger 2020 and on general practice. Pneumococcal products and COVID-19 schedules are deliberately not specified.",
    "Hepatitis B dialysis dose is not quantified in the text; CDC 2001 supports intramuscular deltoid route, anti-HBs testing 1-2 months after the series, 10 mIU/mL threshold, one repeat series for non-responders, yearly retesting with booster in patient responders, and no boosters for staff responders.",
    "Outbreak working definition (two or more linked cases) is a common infection-control convention, not a cited standard; unit policy governs.",
    "Krueger 2020 title is stored in title case by PubMed; a sentence-case TITLE_OVERRIDES entry for PMID 31585683 may be needed in common.py.",
]
NEW_REFS = {
    "romanowski2016": "27178832",
    "krueger2020": "31585683",
}
