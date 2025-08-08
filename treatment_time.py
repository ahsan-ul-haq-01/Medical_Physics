#Treatment time calculation for radiotherapy
#Author: AHSAN UL HAQ

# Equalant field size calculation
X = float(input("Enter the X component of field size: "))
Y = float(input("Enter the Y component of field size: "))

result = 2*X*Y/(X+Y)
rounded_result = round(result)

print(rounded_result)

# Calculation of dose per field

total_dose = float(input("Enter the total dose (Gy): "))
no_of_fields = int(input("Enter the number of fields: "))
dose_per_field = (total_dose) / (no_of_fields)
print("The dose per field is:", dose_per_field, "Gy")

# Calcultaion of total dose per fraction

no_of_fractions = int(input("Enter the number of fractions: "))
dose_per_fraction = dose_per_field / (no_of_fractions)
print("The dose per fraction is:", dose_per_fraction, "Gy")

# Technique used 

# Ask user for the technique
technique = input("Enter the technique (SSD or SAD): ")

# Check the technique and ask for input accordingly
if technique == "SSD":
    distance = float(input("Enter the distance in cm: "))
    pdd = float(input("Enter the percentage depth dose (PDD): "))
    depth = float(input("Enter the depth in cm: "))
    incident_dose = (pdd/100) * ((distance + depth)**2) / (distance**2)
    print("The incident dose is:", incident_dose, "Gy")

elif technique == "SAD":
    distance = float(input("Enter the distance in cm: "))
    tar = float(input("Enter the tissue-air ratio (TAR): "))
    incident_dose = tar * (distance**2)
    print("The incident dose is:", float(incident_dose, "Gy"))

else:
    print("Invalid technique entered.")

# # what is the output of the machine
machine_output = float(input('Enter the output of the machine at SSD/SAD (Gy):'))

# # Calculation of treatment time per fraction
treatment_time_per_fraction = (incident_dose) / (machine_output)
print("Treatment time per field per fraction is :",treatment_time_per_fraction)