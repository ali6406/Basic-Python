import numpy as np
import pandas as pd

p1 = 8  # pressure in bar
pressure_ratio = np.array([0.8875, 0.8875, 0.8875, 0.8875, 0.85, 0.65, 0.512, 0.425, 0.2875, 0.275, 0.275, 0.275, 0.275, 0.275, 0.275, 0.8875, 0.8875, 0.8625, 0.8875, 0.8625, 0.75, 0.625, 0.475, 0.2625, 0.275, 0.275, 0.275, 0.275, 0.275, 0.275])
a = 3.297e-5  # area in m2
n = 1.13  # constant
v1 = 0.22604  # specific volume in m3/kg

# Calculate discharge
discharge = a * (((2 * n) / (n - 1)) * (p1 / v1) * ((pressure_ratio ** (2 / n) - pressure_ratio ** ((n + 1) / n)))) ** 0.5

# Create a DataFrame to store pressure_ratio and discharge values
data = {'Pressure Ratio': pressure_ratio, 'Discharge': discharge}
df = pd.DataFrame(data)

# Save to Excel file
file_name = 'pressure_discharge_data.xlsx'
df.to_excel(file_name, index=False)
print(f"Data saved to '{file_name}'")