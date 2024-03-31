import numpy as np
import pandas as pd

p1 = 8.25  # pressure in bar
pressure_ratio = np.array([0.7030303,0.7030303,0.69090909,0.69090909,0.67878788,0.67878788,0.24242424,0.21818182,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818,0.18181818])
a = 3.297e-5  # area in m2
n = 1.13  # constant
v1 = 0.22604  # in m3/kg

# Calculate discharge
discharge = a * (((2 * n) / (n - 1)) * (p1 / v1) * ((pressure_ratio ** (2 / n) - pressure_ratio ** ((n + 1) / n)))) ** 0.5

# Create a DataFrame to store pressure_ratio and discharge values
data = {'Pressure Ratio': pressure_ratio, 'Discharge': discharge}
df = pd.DataFrame(data)

# Save to Excel file
file_name = 'pressure_discharge_data_2.xlsx'
df.to_excel(file_name, index=False)
print(f"Data saved to '{file_name}'")

