1. Goals, task, key decisions & reasoning

Build a Nursing Education section for Renal Care Matters (https://renalcarematters.com). The audience is Philippine-licensed registered nurses entering nephrology or hemodialysis practice. The series should follow Philippine practice expectations and internationally recognized nephrology nursing curriculum domains.

Your assignment as Claude Code:
- Inspect the website repository and adapt the implementation to its existing framework, content model, build process, navigation, and design system.
- Improve the curriculum and write the lessons, cases, and self-assessments from validated primary sources. Treat the draft below as a starting point for review.
- Architect an image plan for all 12 modules, then produce a self-contained production brief a GPT image-generation session can use without access to this conversation or repository.
- Build and verify the website integration. Keep production deployment outside this handoff unless separately authorized.

Proposed website structure:
- Add Nursing Education under Guides and feature a course card on the Guides index. Use the existing Dialysis Staff / HD Tech discovery path where it fits, with clear Registered Nurses audience labeling on the course itself. Decide whether a dedicated nurse filter is warranted after inspecting how role tags work.
- Suggested hub URL: /guides/nephrology-nursing/. Prefer the site's established URL and trailing-slash conventions. Give each module a stable, shareable URL.
- Hub title: Nephrology Nursing & Hemodialysis. Show two learner paths, a module directory, the syllabus, curriculum sources, and an educator/preceptor resource.
- Both paths share one set of 12 modules. The Nephrology Nursing path emphasizes assessment, CKD, AKI, treatment choices, PD, transplant, and longitudinal care. The Hemodialysis Nursing path covers the common foundations and emphasizes prescription, vascular access, water and equipment safety, intradialytic monitoring, and emergency response.
- Public-facing label: Self-study for registered nurses. Keep supervised training details on the syllabus or educator page. A quiz score attests to self-assessment completion. A clinical preceptor or training provider signs off on practice competencies.
- Recommended publication sequence: hub and Modules 1 and 6–9 first, then Modules 2–5 and 10–12. Implement the common architecture for all 12. If building in phases, label forthcoming modules and avoid linking to unavailable pages.
- Each module should contain objectives, an original lesson, assigned reading, a realistic nursing case, a quiz, answer rationales, and previous/next links. Include a supervised practice prompt when appropriate.
- Preserve the site's free, no-account approach for public learning. Keep quizzes usable on mobile and with a keyboard. Avoid sending quiz responses or any patient information to a server. Use fictional or de-identified scenarios.

2. Progress update

Verified on the public site in November 2026:
- The primary navigation includes Guides, Tools, Drugs, Specialties, and About.
- The Guides index has a Dialysis Staff / HD Tech filter and topic groupings for HD prescription, vascular access, complications, unit operations, PD, AKI, and critical care.
- Existing site content includes a clinical and engineering reference on hemodialysis water treatment, a dialysis-unit code blue and ACLS guide, dialysis quality management, and a CRRT reference. These are strong candidates for assigned reading after review.
- The site describes its resources as free, independent, and available without an account. Its patient guides use English, Tagalog, Cebuano, and Kapampangan. The proposed RN material starts in English. Check existing templates for how untranslated content should appear.

Completed in the planning conversation:
- Drafted a 12-module syllabus and 36 short-answer questions with rationales. Section 3 preserves the scope and the answer the draft intended to test. Revalidate the answers before publication.
- Proposed one course hub, two paths through shared modules, and a first release centered on HD safety.
- Identified Philippine and international curriculum and practice references.

Outstanding:
- Repository, framework, branch, hosting workflow, and content ownership for existing guides remain unverified. No source files, public pages, or images were created during planning.
- The public DOH, PSN, PRC, and international references must be rechecked for revisions or scope changes before publication. Clinical reviewers and any actual training provider remain to be identified.
- The three questions per module are draft formative checks. The 60-item final described below is a blueprint. No final exam was written.

3. Important files, links, names, figures & details

Public website:
- Home: https://renalcarematters.com/
- Guides: https://renalcarematters.com/guides/
- CRRT reference: https://renalcarematters.com/guides/crrt-continuous-renal-replacement-therapy
- Home HD in the Philippines: https://renalcarematters.com/guides/home-hemodialysis-philippines
- Find the canonical water-treatment, code blue, QAPI/CQI, HD prescription, vascular access, and other related guide URLs in the repository or public Guides index. Confirm targets before adding links.
- The originating Codex conversation was projectless. Its workspace is separate from the website repository and contains no site implementation to inherit.

Philippine curriculum and training sources:
- DOH AO 2012-0001, dialysis facility licensing: https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf
- DOH dialysis clinic assessment tool: https://hfsrb.doh.gov.ph/wp-content/uploads/2021/06/rev3-4132015-DOH-HDC-LTO-AT-frm-11282014.pdf
- Philippine Society of Nephrology 2024 HD guidance: https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf
- PRC CPDAS provider record with a Philippine 480-hour competency program example: https://cpdas.prc.gov.ph/public/providerInfo.aspx?id=4CWXH%2FLl%2BM9NTzh5uZdbXA%3D%3D

Verify the latest DOH/HFSRB issuances and relevant regional guidance before making claims about regulatory obligations. Attribute each requirement to the correct source. The DOH licensing materials describe renal dialysis nursing training from a competent provider. The PSN guidance reviewed in planning describes a structured program of three months or longer. The 480 hours are a proposed course design informed by a PRC-listed program example. Verify training-provider acceptance and current PRC CPD status before claiming either. Add a Philippine nursing scope reference from the relevant primary legal or PRC source.

International curriculum and clinical references:
- ANNA Core Curriculum, seventh edition page: https://old.annanurse.org/core-curriculum-nephrology-nursing
- ANNA announcement about the forthcoming eighth edition, September 2026: https://www.annanurse.org/september-2026-enews/
- EDTNA/ERCA post-basic nephrology nursing curriculum: https://edtnaerca.org/education/publications
- NNCC Certified Dialysis Nurse program and blueprint resources: https://www.nncc-exam.org/certification/cdn
- NNCC CDN preparation guide: https://www.nncc-exam.org/sites/default/files/prepguide/cdn.pdf
- KDIGO CKD evaluation and management: https://kdigo.org/guidelines/ckd-evaluation--and-management/
- KDIGO guideline library for AKI/AKD, anemia, CKD–mineral and bone disorder, and other relevant topics: https://kdigo.org/guidelines/
- KDOQI vascular access: https://www.kidney.org/professionals/kdoqi/guidelines-and-commentaries/vascular-access
- CDC dialysis bloodstream infection prevention: https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/
- ISPD PD guidelines and patient teaching resources: https://ispd.org/guidelines/
- KDIGO transplant candidate guideline: https://kdigo.org/guidelines/transplant-candidate/

Recheck ANNA edition status and the current NNCC blueprint when work begins. Use professional curricula to map scope, guidelines to support clinical claims, and applicable Philippine sources for local requirements. Confirm current primary sources for HD adequacy, resuscitation, and dialysis water quality. For technical limits, verify which standard and edition apply to the facility. A manufacturer manual or approved site procedure may be necessary for a machine-specific step. Keep examples distinguishable from prescribed targets and authoritative requirements.

Proposed provider-led course:
- 12 instructional weeks, scheduled over at least three calendar months if adopting the PSN duration recommendation. Proposed total 480 hours: 96 guided study, 48 skills lab/simulation, and 336 supervised clinical learning.
- Proposed completion: at least 80% on a separate written exam, passing case presentation, every safety-critical practical step demonstrated, and preceptor sign-off. Document observed care and simulation separately. Have the provider set encounter counts and validate competencies on its own equipment.
- HD clinical emphasis: full treatment encounters, water-system observation, and inpatient HD where available. Nephrology clinical emphasis: renal ward or CKD clinic, HD, and observational PD/transplant exposure where available.
- Optional educator blueprint for a future 60-item final. HD track: 30 chronic HD, 15 adult kidney disease, 9 AKI/acute HD, 6 water/dialysate. Nephrology track: 20 CKD/complications, 10 AKI, 12 HD, 10 PD/transplant, 8 conservative care/special populations/professional practice. These are proposed course weights. Map them separately from official examination weights.
- HD practical stations: prescription and machine checks, access and asepsis, intradialytic emergency, water-safety failure with handoff. Nephrology stations: CKD plan, AKI escalation, modality counseling, PD or transplant scenario. Capstone: fictional or de-identified renal case or a small quality audit, with a measurable follow-up outcome.

Module briefs. Each includes the initial quiz targets and the proposed primary visual for GPT production:

01. Kidney Function and Renal Assessment
    Teach filtration, tubular function, fluid/electrolyte and acid–base regulation, erythropoietin, vitamin D activation, and bedside assessment. Case: rapid weight gain and orthopnea. Quiz targets: erythropoietin; signs of possible fluid overload and immediate respiratory assessment; eGFR and urine ACR. Image: Filipino RN assessing an adult with a bedside scale and BP cuff. Keep the assessment sequence in accessible HTML. Alt-text intent: Nurse checks weight and blood pressure during a focused renal assessment.

02. CKD Identification, Staging, and Progression
    Teach cause, GFR, albuminuria, chronicity, comorbidities, referral clues, and medication reconciliation. Quiz targets: a single eGFR of 48 does not establish chronicity; eGFR 48 and urine ACR 180 mg/g persistent for four months correspond to G3a/A2; identify name, dose, and frequency of OTC pain relievers and flag NSAID exposure for review. Image: nurse reviewing serial laboratory results with a patient at an outpatient desk. Render the staging table and case values in HTML. Alt-text intent: Nurse reviews kidney function and urine albumin trends with a patient.

03. CKD Complications, Nutrition, and Medicines
    Teach anemia, iron indices, mineral and bone disorder, potassium, acid–base, volume, nutrition, and medication teaching. Quiz targets: ferritin and transferrin saturation; product-specific meal timing of a prescribed phosphate binder; assess unintentional weight loss and arrange dietitian review. Image: renal nurse and dietitian discussing a Filipino meal with an adult patient. Use food as context for individualized counseling. Alt-text intent: Nurse and dietitian review a meal during renal nutrition counseling.

04. AKI and Acute Kidney Support
    Teach hemodynamic, intrinsic and obstructive causes, monitoring, urgent escalation, and differences among intermittent, prolonged intermittent, and continuous kidney support. Quiz targets: creatinine 0.9 to 1.3 mg/dL in 36 hours meets the draft AKI criterion; oliguria with distended bladder can suggest obstruction; ECG changes with potassium 6.7 mmol/L require urgent escalation and a concise clinical handoff. Image: ICU nurse calling the clinical team while a colleague assesses the patient. Keep generated monitor values indistinct. Alt-text intent: Hospital nurses assess a patient and make an urgent clinical handoff.

05. Kidney Failure, Treatment Choices, and Conservative Care
    Teach HD, PD, transplant, comprehensive conservative kidney management, shared decisions, palliative and advance care planning, and travel or cost barriers. Quiz targets: four treatment pathways; a teach-back prompt; ask about barriers and coordinate a support referral. Image: Filipino patient, invited family member, and nurse at eye level in a private consultation. Alt-text intent: Patient and family discuss kidney failure treatment options with a nurse.

06. HD Principles, Prescription, and Adequacy
    Teach diffusion, ultrafiltration, convection, prescription verification, fluid accounting, delivered treatment time, Kt/V, and urea reduction ratio. Quiz targets: diffusion for conventional urea removal and ultrafiltration for water; 2.4 L over four hours equals 600 mL/hour before accounting for treatment inputs; common reasons for low delivered adequacy. Image: nurse verifying an order at an unconnected training machine. If using a membrane/circuit diagram, supply a clinician-approved vector layout with correct directionality and labels. Alt-text intent: Nurse compares the dialysis prescription with a training machine before treatment.

07. HD Vascular Access and Infection Prevention
    Teach fistulas, grafts, catheters, assessment, vessel preservation, asepsis, injection safety, station disinfection, and hepatitis B precautions. Quiz targets: withhold cannulation and promptly escalate a newly absent thrill/bruit; correct hub contamination before connection; keep needle sites and lines visible to detect bleeding or dislodgement. Image: close-up of a nurse palpating a bare forearm fistula before cannulation. Include no needles, active tubing, or staged catheter manipulation in the generated scene. Alt-text intent: Nurse palpates a forearm fistula to check for a thrill.

08. HD Equipment, Water, and Dialysate Safety
    Teach circuit checks, carbon treatment and reverse osmosis, chemical and microbial risks, documentation, conductivity, temperature, and release criteria. Link the site's water-treatment guide as reading. Quiz targets: carbon treatment reduces chlorine/chloramine; hold initiation on a supply that fails the facility's action threshold; conductivity and temperature do not verify all water hazards. Image: staff member checking a monitoring log in a dialysis water room. If adding a treatment-train diagram, use a clinician and technical reviewer to verify topology, sampling points, and the scope of the example. Alt-text intent: Dialysis staff member reviews the water-system monitoring log before treatment.

09. Complete HD Session and Complication Response
    Teach pre-, intra-, and post-treatment assessment, documentation, escalation, and unit-specific simulations for symptomatic hypotension, dislodgement, hemolysis, air alarm, reactions, and cardiac arrest. Quiz targets: immediate priorities in symptomatic hypotension; suspect blood loss from needle dislodgement or disconnection and act under protocol; report delivered treatment and patient status after interruption. Image: dialysis team responding in a simulation bay with a mannequin and a trainer. Avoid depicting specific emergency maneuvers in the generated image. Alt-text intent: Dialysis nurses rehearse an urgent response at a simulation station.

10. PD and Home Dialysis Nursing
    Teach CAPD and automated PD, fill/dwell/drain, exit-site surveillance, contamination, peritonitis recognition, home readiness, and caregiver return demonstration. Quiz targets: cloudy effluent with abdominal pain requires urgent PD-team assessment; dwell definition; observe a full return demonstration and assess response to warning signs. Image: patient and nurse reviewing unopened PD supplies on a clean surface in a Filipino home. Teach exchange technique with reviewed text and training materials. Alt-text intent: Nurse teaches a patient to prepare a clean space for home peritoneal dialysis.

11. Transplantation and Special Populations
    Teach referral, post-transplant assessment, immunosuppressant adherence, infection risk, delayed graft function, and considerations for pediatric, pregnant, frail, and medically complex patients. Quiz targets: urgently report early post-transplant oliguria and rising creatinine; follow medication-specific missed-dose instructions and consult the transplant team; identify two pediatric dialysis considerations. Image: transplant nurse reviewing an unlabeled medication schedule with a patient at follow-up. Alt-text intent: Transplant nurse reviews the medication schedule with a patient.

12. Philippine Practice, Quality Improvement, and Capstone
    Teach licensing context, scope, consent/privacy, infection surveillance, quality improvement, incident reporting, emergency transfer, and disruption planning for power, water, and transport. Quiz targets: compliant hub-disinfection events divided by observed eligible opportunities; intercept, verify, and report a dialysate-setting near miss; communicate interrupted treatment, patient condition, and disposition during a closure. Image: Philippine dialysis team reviewing a quality audit in a staff huddle. Keep generated charts indistinct and place real metrics in HTML. Alt-text intent: A dialysis team reviews a unit quality audit during a staff huddle.

4. Where we left off & next steps

Latest instruction from the user: “Go ahead and build a blueprint handoff for claude code. Instruct to improve upon the content based on validated sources and architect an image plan for each module for handoff to gpt for production.”

Execute in this order:

A. Inspect the repository.
- Read project instructions. Identify how guides, slugs, taxonomy, navigation, translations, search, sitemap, related content, images, and print styles are implemented.
- Identify the smallest set of changes that integrates a hub and module template with existing guide conventions. Reuse existing article layouts and quiz components where available.
- Verify canonical links to existing assigned readings. Record publication dependencies and site-specific decisions.

B. Validate and improve the content.
- Create a compact curriculum crosswalk mapping each module to Philippine program or practice sources, ANNA or EDTNA/ERCA domains, and the NNCC domains where relevant.
- Maintain a source register with publisher, title, year or edition, URL, relevant section/page, and review date. For quizzes, record the source or teaching objective supporting the keyed answer and rationale. Flag claims that depend on institutional policy, orders, manufacturer instructions, or a particular standard edition.
- Strengthen each lesson with an applied nursing case and teach-back or documentation task. Include what to assess, communicate, teach, and escalate. Review high-risk emergency sequencing, access, water thresholds, isolation, drugs, pediatric and transplant content with the appropriate subject reviewer before public release.
- Use original prose, cases, and questions. Use the draft targets as the minimum per-module scope. Three scored questions per module are enough for the first release. Favor case-based single-best-answer items with brief rationales for every option, plus a separate reflective prompt where useful. Keep clinically equivalent wording out of machine-graded free-text fields.
- Diagnostic and frequency thresholds, patient instructions, emergency actions, and medication timing need traceable source support. Clearly distinguish comparisons across jurisdictions and avoid unsupported accreditation or CPD claims.

C. Build the web experience.
- Implement a reusable module template with existing content conventions. Suggested module fields are title, slug, objectives, track emphasis, estimated reading time, lesson, case, quiz items and rationales, practice task, source list, review date, and optional image metadata.
- For the quiz, use grouped radio fields with visible labels and a Check answers button. Show score and rationale after submission, make feedback accessible to keyboard and screen-reader users, and allow a retry. Use wording such as “Self-assessment complete.” Any saved progress should be browser-local and optional if implemented.
- Integrate the hub and card with navigation and discoverability. Include print styling for the syllabus and preceptor checklist using existing conventions. Keep module content usable while assets are pending.
- Run the repository's build and relevant checks. Verify the hub, paths, quiz scoring and reset, mobile layout, keyboard and screen-reader behavior, source and previous/next links, search discoverability, and build output. If the repository or access is missing, report that concrete blocker and complete any independent planning that can be handed over.

D. Produce the GPT image handoff.
- Turn every module visual above into one copy-ready prompt. Include module ID, final filename, placement, the learning purpose, scene, framing and focal point, setting, people, clinically significant visual details, exclusions, and proposed alt text. A reusable art-direction preamble is fine if delivered with all prompts so the brief is self-contained.
- Use one coherent editorial visual style suited to Renal Care Matters. Recommended starting point: realistic documentary-style illustrations of Philippine renal care settings, consistent neutral color treatment, realistic staff attire, and no recognizable patients, provider logos, or personal records. Check current site assets before finalizing the style. Keep the visual's focal point usable in mobile crops.
- Separate editorial photos from instructional diagrams. GPT can produce the requested raster scenes from the image prompts. For an instructional diagram, provide a separate reviewed diagram brief, with real labels, data, and interactive or accessible explanations authored in site-native markup or independently verified graphics. Avoid asking image generation to render machine settings, numeric values, labels, or procedural steps.
- Propose a consistent naming convention such as renal-nursing-01-renal-assessment.webp through renal-nursing-12-quality-improvement.webp. Start with a 16:9 master and define responsive derivatives using the repository’s asset conventions. Specify any PNG/JPEG master and WebP/AVIF delivery formats based on the existing pipeline. Use concise meaningful alt text, or empty alt text if an image serves solely as decoration.
- Include a per-image review line for a renal nurse, nephrologist, or technical reviewer as appropriate. Where a generator introduces impossible anatomy, equipment, personal data, or a misleading workflow, revise or regenerate the visual before publication. Deliver the prompt sheet and image manifest to GPT for production. Image generation itself was not requested in this planning conversation.

5. Other key details

- Preserve a clear distinction between the public nurse education series and any provider-led training offering. A public self-study course can go live independently once its content has been reviewed. A provider-led launch depends on the provider confirming prerequisites, supervision, placement, clinical sign-off, and applicable recognition.
- Use Philippine scenarios and terminology where they help a reader apply the material. Include access constraints such as transport, scheduling, and localized disruption planning where relevant. Verify local details before presenting them as generally applicable.
- Suggested Guides card: “Nephrology Nursing & Hemodialysis. A study series for registered nurses, from kidney assessment and CKD to safe hemodialysis care. Each module includes a nursing case and a self-assessment with answer rationales.” CTA: “View the syllabus and start learning.”
- The proposed URL, phased launch, hours, sample module visual concepts, course exam weights, and English-first implementation are planning decisions. Repository findings and clinical review may warrant changes. Document consequential changes with the rationale.
- Expected handoff outputs from Claude Code: course integration and authored module content, source register and curriculum crosswalk, educator syllabus/checklist, working formative assessments, GPT-ready prompts and manifest for all 12 images, and verification notes listing any unresolved clinical or publication dependencies.