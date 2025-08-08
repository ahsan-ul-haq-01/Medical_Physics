from pylinac.calibration import tg51
from fpdf import FPDF

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except Exception:
            print("Please enter a valid floating point number.")

def get_tuple(prompt, count):
    while True:
        try:
            values = tuple(float(x) for x in input(prompt).split())
            if len(values) != count:
                raise ValueError
            return values
        except Exception:
            print(f"Please enter {count} floats separated by spaces.")

# User inputs
ENERGY = get_float("Enter photon energy (MV): ")
TEMP = get_float("Enter temperature (C): ")
press_type = input("Enter pressure units (mmHg/kPa): ").lower()
PRESS = get_float("Enter pressure value: ")
if press_type == 'mmhg':
    PRESS = tg51.mmHg2kPa(PRESS)
elif press_type != 'kpa':
    raise ValueError("Unknown pressure unit. Please use 'mmHg' or 'kPa'.")

CHAMBER = input("Enter chamber code (e.g. 30013): ")
P_ELEC = get_float("Enter P_elec: ")
ND_w = get_float("Enter NDw (Gy/nC): ")
MU = get_float("Enter number of MUs: ")

CLINICAL_PDD = get_float("Enter Clinical PDD at 10 cm (%): ")

# Calculations
pdd10x = tg51.pddx(pdd=CLINICAL_PDD, energy=ENERGY)
tpr = tg51.tpr2010_from_pdd2010(pdd2010=(38.0 / CLINICAL_PDD))
kq = tg51.kq_photon_tpr(chamber=CHAMBER, tpr=tpr)
p_tp = tg51.p_tp(temp=TEMP, press=PRESS)

m_reference = get_tuple("Enter 3 m_reference values separated by spaces: ", 3)
m_opposite = get_tuple("Enter 3 m_opposite values separated by spaces: ", 3)
p_pol = tg51.p_pol(m_reference=m_reference, m_opposite=m_opposite)

m_reduced = get_tuple("Enter 2 m_reduced values separated by spaces: ", 2)
p_ion = tg51.p_ion(voltage_reference=300, voltage_reduced=150,
                   m_reference=m_reference, m_reduced=m_reduced)

m_corr = tg51.m_corrected(
    p_ion=p_ion,
    p_tp=p_tp,
    p_elec=P_ELEC,
    p_pol=p_pol,
    m_reference=m_reference
)

dose_10 = m_corr * kq * ND_w
dose_10_per_mu = dose_10 / MU
dose_ddmax = dose_10_per_mu / CLINICAL_PDD

print("\n--- TG-51 Results ---")
print(f"Energy: {ENERGY} MV")
print(f"Temperature: {TEMP} °C")
print(f"Pressure: {PRESS:.2f} kPa")
print(f"Chamber: {CHAMBER}")
print(f"P_elec: {P_ELEC}")
print(f"ND_w: {ND_w} Gy/nC")
print(f"MU: {MU}")
print(f"Clinical PDD: {CLINICAL_PDD:.2f} %")
print(f"Corrected Measurement (m_corr): {m_corr:.6f}")
print(f"kQ: {kq:.6f}")
print(f"Dose/MU to water at dmax: {dose_ddmax:.6f}\n")

# --- Generate PDF report ---
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(0, 10, "TG-51 Calibration Report", ln=True, align="C")
pdf.ln(8)
pdf.set_font("Arial", size=11)
pdf.cell(0, 8, f"Energy: {ENERGY} MV", ln=True)
pdf.cell(0, 8, f"Temperature: {TEMP} °C", ln=True)
pdf.cell(0, 8, f"Pressure: {PRESS:.2f} kPa", ln=True)
pdf.cell(0, 8, f"Chamber: {CHAMBER}", ln=True)
pdf.cell(0, 8, f"P_elec: {P_ELEC}", ln=True)
pdf.cell(0, 8, f"ND_w: {ND_w} Gy/nC", ln=True)
pdf.cell(0, 8, f"MU: {MU}", ln=True)
pdf.cell(0, 8, f"Clinical PDD: {CLINICAL_PDD:.2f} %", ln=True)
pdf.cell(0, 8, f"m_reference: {m_reference}", ln=True)
pdf.cell(0, 8, f"m_opposite: {m_opposite}", ln=True)
pdf.cell(0, 8, f"m_reduced: {m_reduced}", ln=True)
pdf.cell(0, 8, f"Corrected Measurement (m_corr): {m_corr:.6f}", ln=True)
pdf.cell(0, 8, f"kQ: {kq:.6f}", ln=True)
pdf.cell(0, 8, f"Dose/MU to water at dmax: {dose_ddmax:.6f}", ln=True)

pdf.output("TG51_report.pdf")
print("PDF report generated as TG51_report.pdf")
