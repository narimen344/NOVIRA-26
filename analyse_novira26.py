"""NOVIRA-26 | Reproduce the hospital report from cleaned fictional data.
Run: python analyse_novira26.py
No additional libraries are required.
"""

import csv
from pathlib import Path

# Read the patient file located beside this script.
file = Path(__file__).with_name("NOVIRA26_cleaned.csv")
with file.open(encoding="utf-8", newline="") as source:
    patients = list(csv.DictReader(source))

# 1 means hospitalized; 0 means not hospitalized.
def hospitalization_rate(group):
    if not group:
        return 0
    hospitalized = sum(patient["hospitalized"] == "1" for patient in group)
    return 100 * hospitalized / len(group)

print("NOVIRA-26 | Hospital Research Network")
print("Synthetic data — teaching demonstration only")
print("Patients analyzed:", len(patients))

print("\nHOSPITALIZATION RATE BY HOSPITAL")
for hospital in ["East Hospital", "North Hospital", "South Hospital", "West Hospital"]:
    group = [p for p in patients if p["hospital"] == hospital]
    print(f"{hospital}: {hospitalization_rate(group):.1f}% ({len(group)} patients)")

print("\nOVERALL HOSPITALIZATION RATE BY TREATMENT")
for treatment in ["AVX-7", "Standard care"]:
    group = [p for p in patients if p["treatment"] == treatment]
    high_risk = sum(p["baseline_risk"] == "High" for p in group) / len(group) * 100
    print(f"{treatment}: {hospitalization_rate(group):.1f}% hospitalized | {high_risk:.1f}% high-risk")

print("\nHOSPITALIZATION RATE WITHIN EACH BASELINE RISK GROUP")
for risk in ["Low", "Moderate", "High"]:
    print(risk)
    for treatment in ["AVX-7", "Standard care"]:
        group = [p for p in patients if p["baseline_risk"] == risk and p["treatment"] == treatment]
        print(f"  {treatment}: {hospitalization_rate(group):.1f}%")

print("\nReminder: observed associations do not prove a treatment is effective.")
