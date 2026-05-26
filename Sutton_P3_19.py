""" Problem 3.19
 An upper stage of a launch vehicle propulsion unit fails to meet expectations during
sea-level testing. This unit consists of a chamber at 4.052 MPa feeding hot propellant to
a supersonic nozzle of area ratio 𝜖 = 20. The local atmospheric pressure at the design
condition is 20 kPa. The propellant has a k = 1.2 and the throat diameter of the nozzle
is 9 cm.
a. Calculate the ideal thrust at the design condition.
b. Calculate the ideal thrust at the sea-level condition.
c. State the most likely source of the observed nonideal behavior.
"""

import numpy as np
from scipy.optimize import fsolve


## GIVEN/CONSTANTS
P_c = 4.052e6  # Chamber pressure, Pa
P_a1 = 20e3  # Atmospheric pressure, Pa
ExpR = 20  # Area ratio
k = 1.2  # Specific heat ratio
D_throat = 0.09  # Throat diameter, m

## FUNCTIONS
def thrust(k, pe_pc, pa_pc, A_t, A_e, P_c):
    momentum = A_t*P_c*np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - pe_pc**((k - 1) / k))
    )
    pressure = (pe_pc - pa_pc) * A_e * P_c
    return momentum + pressure

def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.5)[0]  # Initial guess for supersonic flow
    return M_exit

## CALCULATIONS
# a. Calculate the ideal thrust at the design condition
# Calculate the throat area
A_t = np.pi * (D_throat / 2) ** 2
# Calculate the exit area using the area ratio
A_e = ExpR * A_t
# For the design condition, the exit pressure is equal to the atmospheric pressure
P_e1 = P_a1
# Calculate the thrust at the design condition  
thrust_design = thrust(k, P_a1 / P_c, P_e1 / P_c, A_t, A_e, P_c)
print(f"Ideal thrust at design condition: {thrust_design:.2f} N")

# b. Calculate the ideal thrust at the sea-level condition
# For the sea-level condition, ambient pressure is 101325 Pa
P_a2 = 101325  # Sea-level atmospheric pressure, Pa
# Calculate nozzle exit pressure using isentropic relations

# Calculate Exit Conditions (Mach, Velocity, Temperature)
M_exit = calculate_exit_mach_number(ExpR, k) # Exit Mach number
#T_exit = T0 / (1 + (k - 1) / 2 * M_exit**2)  # Exit temperature, K
#V_exit = M_exit * np.sqrt(k * R * T_exit)  # Exit velocity, m/s

def calculate_pressure_ratio(M, k):
    """Calculate the chamber to Exit Pressure Ratio from Mach number using the isentropic flow relations."""
    Pc_Pe = (1 + (k - 1) / 2 * M**2)**(k / (k - 1))
    return Pc_Pe # Returns Pc/Pe
Pc_Pe = calculate_pressure_ratio(M_exit, k)  # Chamber-to-exit pressure ratio
P_e2 = P_c / Pc_Pe  # Exit pressure at sea level
print(f"Exit pressure at sea level: {P_e2:.2f} Pa")
# Calculate the thrust at sea level
pe_pc2 = P_e2 / P_c
pa_pc2 = P_a2 / P_c
thrust_sea_level = thrust(k, pe_pc2, pa_pc2, A_t, A_e, P_c)
print(f"Ideal thrust at sea level: {thrust_sea_level:.2f} N")
print(f"Thrust loss from design to sea level: {thrust_design - thrust_sea_level:.2f} N")
print(f"Percentage thrust loss from design to sea level: {(thrust_design - thrust_sea_level) / thrust_design * 100:.2f}%")
# c. State the most likely source of the observed nonideal behavior.
print("The most likely source of the observed nonideal behavior is the increased back pressure at sea level, " \
"\nwhich reduces the effective expansion of the exhaust gases and thus decreases the thrust. " \
"\nAdditionally, flow separation in the nozzle due to the higher ambient pressure could also contribute to the nonideal performance.")