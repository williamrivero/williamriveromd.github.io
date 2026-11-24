# -*- coding: utf-8 -*-
"""Situations and tips for Physician on Duty, Module 06. Fictional and original.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters)."""

SITUATIONS = {"06": {
    "scenarios": [
        ("The chlorine test that was not done",
         "It is 6:10 a.m. in a unit in Quezon City. The first four patients are cannulated and waiting. The water log has no total chlorine entry for today. The technician on the night roster called in sick.",
         "No one knows whether the carbon beds are still removing chloramine. The test exists for exactly this moment.",
         "Ask the charge nurse to hold the start of treatment per the unit&rsquo;s water policy until a test is done by a trained staff member. Inform the Medical Director and the attending nephrologist, and follow the escalation list for a backup technician. Record the delay and the result.",
         "Chloramine breakthrough causes hemolysis in every patient on the loop at once. A missed test is a missing guard."),
        ("Itching in one room",
         "Two patients in the small back room of a unit in Pampanga develop sudden, severe itching and nausea an hour into the session. Patients in the main hall are well. The back room was recently connected to a separate water line.",
         "A water problem limited to one supply. Fluoride and other chemicals have caused exactly this pattern.",
         "Declare a possible cluster to the charge nurse. Assess both patients, and treat per protocol with an electrocardiogram (ECG) and a cardiac monitor if available. Hold new starts in that room per protocol. Ask the technician what supplies the back room and to test it. Call the Medical Director and the attending nephrologists.",
         "A room-by-room comparison is the fastest route to the cause. Fatal arrhythmia was part of the published fluoride outbreak."),
        ("Chills on the new jug",
         "Three patients develop shivering and a temperature of 38.4 &deg;C within forty minutes of starting. All three machines were connected to bicarbonate concentrate mixed the evening before and left uncovered.",
         "A pyrogenic reaction from bacteria or endotoxin in the bicarbonate concentrate is likely. Bloodstream infection must still be considered in each patient.",
         "Treat each patient per the fever protocol and Module 17, including blood cultures as the protocol directs. Ask that the containers be kept, not discarded, and that fresh concentrate be used per protocol. Call the Medical Director and the attending nephrologists.",
         "Discarding the jug destroys the evidence. Keeping it allows the cause to be confirmed and the mixing practice to be corrected."),
        ("The pink plasma",
         "A man is found to have a hemoglobin far lower than last month. His blood sample after dialysis is pink-tinged. Two other patients on the same shift report back pain during their sessions this week.",
         "Low-grade hemolysis in several patients, possibly from chloramine breakthrough, a tubing lot, or fluid temperature.",
         "Tell the charge nurse and the technician, and ask for the chlorine records and the disposables lot numbers. Call the Medical Director and the attending nephrologists. Follow the unit&rsquo;s protocol for any patient with active hemolysis on the machine, including not returning the blood.",
         "Hemolysis can be slow and spread over days. A falling hemoglobin in several patients at once is a cluster, even without drama."),
        ("The falling reverse osmosis trend",
         "Reading the log on a quiet Saturday, you see that the reverse osmosis salt rejection has fallen a little each day for two weeks. No patient is ill.",
         "The main barrier is losing efficiency. Dissolved chemicals, including metals, may be passing in increasing amounts.",
         "Ask the technician what is planned and by when. Inform the Medical Director in writing the same day. Note it in your shift record.",
         "Aluminum and other metals harm slowly and silently. A trend is the warning that comes before any symptom."),
    ],
    "tips": [
        "Read the chlorine entry in the water log before the first patient of your shift starts.",
        "When two patients have the same new complaint, ask what else they share: room, loop, machine, concentrate batch, or lot.",
        "Never let a concentrate jug, dialyzer, or blood line from a suspected cluster be thrown away.",
        "Ask after every water service or concentrate change whether a test was done before patients started.",
        "Keep the technician&rsquo;s and the Medical Director&rsquo;s numbers on your phone, not only on the wall.",
    ],
}}
