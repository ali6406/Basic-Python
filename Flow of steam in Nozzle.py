def isentropic_flow(a1, p1, t1, p2):
    # Constants
    gamma = 1.3  # Specific heat ratio for steam
    # Isentropic flow equations
    t2 = t1 * (p2 / p1) ** ((gamma - 1) / gamma)
    a2 = a1 * (p1 * t2) / (p2 * t1)
    return a2, t2
def nozzle_flow(a1, p1, t1, p_back):
    # Exit pressure for ideal expansion
    p_exit = p_back  # Assume exit pressure is equal to back pressure
    # Calculate nozzle parameters using isentropic flow equations
    a2, t2 = isentropic_flow(a1, p1, t1, p_exit)
    return a2, t2, p_exit
# Inputs (example values)
a_inlet = 0.05  # m^2 (inlet area of the nozzle)
p_inlet = 10.0  # bar (inlet pressure)
t_inlet = 400.0  # Celsius (inlet temperature)
p_back_pressure = 1.0  # bar (back pressure)
# Convert units
p_inlet *= 100  # Convert from bar to kPa
t_inlet += 273.15  # Convert Celsius to Kelvin
p_back_pressure *= 100  # Convert from bar to kPa
# Calculate nozzle parameters
exit_area, exit_temperature, exit_pressure = nozzle_flow(a_inlet, p_inlet, t_inlet, p_back_pressure)
# Display results
print(f"Exit Area: {exit_area:.4f} m^2")
print(f"Exit Temperature: {exit_temperature - 273.15:.2f} Celsius")
print(f"Exit Pressure: {exit_pressure / 100:.2f} bar")
