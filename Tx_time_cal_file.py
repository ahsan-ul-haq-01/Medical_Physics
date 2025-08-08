
# making an empty string to accumulate all values for single file
# Author: AHSAN UL HAQ
# Email: ahsanulhaqreshi@gmail.com

report = ""

# Equalant field size calculation
X = float(input("Enter the X component of field size: "))
Y = float(input("Enter the Y component of field size: "))

result = 2*X*Y/(X+Y)
rounded_result = round(result)
print(rounded_result)

report += f"""X component of field size: {X}
Y component of field size: {Y}
Equivalent field size (rounded): {rounded_result}
"""

# Calculation of dose per field
total_dose = float(input("Enter the total dose (Gy): "))
no_of_fields = int(input("Enter the number of fields: "))
dose_per_field = (total_dose) / (no_of_fields)
print("The dose per field is:", dose_per_field, "Gy")

report += f"""Total dose (Gy): {total_dose}
Number of fields: {no_of_fields}
Dose per field (Gy): {dose_per_field}
"""

# Calculation of total dose per fraction
no_of_fractions = int(input("Enter the number of fractions: "))
dose_per_fraction = dose_per_field / (no_of_fractions)
print("The dose per fraction is:", dose_per_fraction, "Gy")

report += f"""Number of fractions: {no_of_fractions}
Dose per fraction (Gy): {dose_per_fraction}
"""

# Technique used
technique = input("Enter the technique (SSD or SAD): ")
report += f"Technique: {technique}\n"

if technique == "SSD":
    distance = float(input("Enter the distance in cm: "))
    pdd = float(input("Enter the percentage depth dose (PDD): "))
    depth = float(input("Enter the depth in cm: "))
    incident_dose = (pdd/100) * ((distance + depth)**2) / (distance**2)
    print("The incident dose is:", incident_dose, "Gy")
    report += f"""Distance (cm): {distance}
Percentage depth dose (PDD): {pdd}
Depth (cm): {depth}
Incident dose (Gy): {incident_dose}
"""
elif technique == "SAD":
    distance = float(input("Enter the distance in cm: "))
    tar = float(input("Enter the tissue-air ratio (TAR): "))
    incident_dose = tar * (distance**2)
    print("The incident dose is:", incident_dose, "Gy")
    report += f"""Distance (cm): {distance}
Tissue-air ratio (TAR): {tar}
Incident dose (Gy): {incident_dose}
"""
else:
    print("Invalid technique entered.")
    report += "Invalid technique entered.\n"

machine_output = float(input('Enter the output of the machine at SSD/SAD (Gy):'))
treatment_time_per_fraction = (incident_dose) / (machine_output)
print("Treatment time per field per fraction is :",treatment_time_per_fraction)

report += f"""Machine output (Gy): {machine_output}
Treatment time per field per fraction: {treatment_time_per_fraction}
"""

# Save report to text file
with open("treatment_report.txt", "w") as f:
    f.write(report)
print("Report saved to treatment_report.txt")