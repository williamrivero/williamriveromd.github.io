# -*- coding: utf-8 -*-
SIT = {"08": {"scenarios": [
    ("Waiting for the result", "A patient with peaked T waves and a missed session is connected while staff wait 45 minutes for the potassium.",
     "The ECG was not trusted until the laboratory confirmed it.", "Start the order set (calcium for ECG changes, insulin with glucose) and connect promptly; call the physician.",
     "ECG changes do not wait for the laboratory."),
    ("The 9 a.m. low sugar", "Two hours after insulin for hyperkalemia, a patient becomes sweaty and confused.",
     "Hypoglycemia from prolonged insulin effect.", "Check capillary glucose and treat per protocol; review the follow-on glucose order.",
     "Insulin lasts longer in kidney failure."),
    ("One line, two drugs", "During an arrest, calcium and bicarbonate are drawn up to go through the same line back to back.",
     "Risk of precipitation in the line.", "Use separate lines or flush well between them, per protocol.",
     "A blocked line in arrest wastes minutes."),
], "tips": ["Write which framework your unit follows for hyperkalemic arrest on the order set itself.", "Keep the hyperkalemia kit findable in seconds, not buried in the cart."]}}
