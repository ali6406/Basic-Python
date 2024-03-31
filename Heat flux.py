class HeatFluxCalculator:
    def __init__(self, conductivity, temperature_1=None, temperature_2=None, distance=None):
        self.conductivity = conductivity  # Thermal conductivity in W/(m*K)
        self.temperature_1 = temperature_1  # Temperature at state 1 in K
        self.temperature_2 = temperature_2  # Temperature at state 2 in K
        self.distance = distance  # Distance between the two states in meters

    def calculate_temperature_gradient(self):
        """
        Calculates the temperature gradient given two temperatures and distance.
        Formula: dT/dx = (T2 - T1) / distance
        where:
        dT/dx = Temperature gradient (K/m)
        T1 = Temperature at state 1 (K)
        T2 = Temperature at state 2 (K)
        distance = Distance between the two states (m)
        """
        if self.temperature_1 is None or self.temperature_2 is None or self.distance is None:
            raise ValueError("Temperature at one state or distance is missing.")

        temperature_gradient = (self.temperature_2 - self.temperature_1) / self.distance
        return temperature_gradient

    def calculate_heat_flux(self):
        """
        Calculates heat flux using Fourier's Law of Heat Conduction.
        Formula: Heat Flux (q) = -k * dT/dx
        where:
        q = Heat flux (W/m^2)
        k = Thermal conductivity (W/(m*K))
        dT/dx = Temperature gradient (K/m)
        """
        temperature_gradient = self.calculate_temperature_gradient()
        heat_flux = -self.conductivity * temperature_gradient
        return heat_flux

# Example usage:
if __name__ == "__main__":
    # Example data
    thermal_conductivity = 10  # W/(m*K)
    temperature_1 = 100  # K
    temperature_2 = 50  # K
    distance = 0.1  # m

    # Create an instance of HeatFluxCalculator
    heat_calculator = HeatFluxCalculator(thermal_conductivity, temperature_1, temperature_2, distance)

    # Calculate heat flux
    heat_flux = heat_calculator.calculate_heat_flux()

    print("Heat Flux:", heat_flux, "W/m^2")
