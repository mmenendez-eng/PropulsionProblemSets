""" Sutton P3.12:
Design a supersonic nozzle to operate at 10 km altitude with an area ratio of 8.0. For the hot
gas take T0 = 3000 K, R = 378 J∕kg-K, and k = 1.3. 
Determine the 
exit Mach number, 
exit velocity, and 
exit temperature, as well as the 
chamber pressure. 

If this chamber pressure is doubled, what happens to the thrust and the exit velocity? 
Assume no change in gas properties. 
How close to optimum nozzle expansion is this nozzle?
"""

## Import
import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import brentq


## Given/Known
T0 = 3000  # Total temperature in K 
R = 378  # Gas constant in J/kg-K
k = 1.3  # Specific heat ratio
ExpR = 8.0  # Area ratio (Ae/At)
h = 10000  # Altitude in meters

## FUNCTIONS
def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.5)[0]  # Initial guess for supersonic flow
    return M_exit

def area_mach(M, k):
    return (1.0 / M) * ((2.0 / (k + 1.0)) * (1.0 + (k - 1.0) / 2.0 * M**2))**((k + 1.0) / (2.0 * (k - 1.0)))

def calculate_pressure_ratio(M, k):
    """Calculate the chamber to Exit Pressure Ratio from Mach number using the isentropic flow relations."""
    Pc_Pe = (1 + (k - 1) / 2 * M**2)**(k / (k - 1))
    return Pc_Pe # Returns Pc/Pe

def pe_pc_from_mach(M, k):
    """Calculate the exit to chamber pressure ratio from Mach number using the isentropic flow relations."""
    return (1 + (k - 1) / 2 * M**2)**(-k / (k - 1)) # Returns Pe/Pc

def mach_from_pressure_ratio(pe_pc, k):
    f = lambda M: pe_pc_from_mach(M, k) - pe_pc
    return brentq(f, 1.0001, 20.0)  # Solve for Mach number given a pressure ratio, with bounds to ensure we find a supersonic solution




def thrust_coefficient(k, pe_pc, pa_pc, eps):
    momentum = np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - pe_pc**((k - 1) / k))
    )
    pressure = (pe_pc - pa_pc) * eps
    return momentum + pressure

##--------------------------------------
## ANALYSIS
##--------------------------------------
#1) Case 1: Original Design Point
# Calculate Exit Conditions (Mach, Velocity, Temperature)
M_exit = calculate_exit_mach_number(ExpR, k) # Exit Mach number
T_exit = T0 / (1 + (k - 1) / 2 * M_exit**2)  # Exit temperature, K
V_exit = M_exit * np.sqrt(k * R * T_exit)  # Exit velocity, m/s

# Calculate Chamber Pressure
Pc_Pe = calculate_pressure_ratio(M_exit, k)  # Chamber-to-exit pressure ratio
Pe_Pc = 1/Pc_Pe                             # Exit Pressure Ratio
P_atm = 0.26151*101325  # Atmospheric pressure at 10 km altitude in Pa
P_chamber = Pc_Pe * P_atm  # Chamber pressure in Pa

#2) Case 2: New Design Point with Doubled Chamber Pressure
P_chamber2 = 2 * P_chamber  # New chamber pressure if doubled
P_e2 = 1/Pc_Pe * P_chamber2  # New exit pressure if chamber pressure is doubled
# Calculate Thrust Coefficients for Both Cases
CF1 = thrust_coefficient(k, Pe_Pc, P_atm/P_chamber, ExpR)  # Thrust coefficient at original chamber pressure
CF2 = thrust_coefficient(k, Pe_Pc, P_atm / P_chamber2, ExpR) # Thrust coefficient at doubled chamber pressure
# Calculate Percent Difference in Thrust if Chamber Pressure is Doubled
F2_F1 = CF2*P_chamber2/(CF1*P_chamber)  # Ratio of thrust at doubled chamber pressure to original thrust
F_dif = (F2_F1 - 1)*100  # Percent difference in thrust if chamber pressure is doubled

# -----------------------------
# Optimum area ratio for doubled chamber pressure
# -----------------------------
# For optimum expansion at doubled Pc, need Pe = P_atm
pe_pc_opt2 = P_atm / P_chamber2
M_opt2 = mach_from_pressure_ratio(pe_pc_opt2, k)
ExpR_opt2 = area_mach(M_opt2, k)

# Another solution for optimum area ratio at doubled chamber pressure using Eq. 3-25 (Area Ration as function of pressure ratios)
ExpR_inv = ((k+1)/2)**(1/(k-1))*(P_atm/P_chamber2)**(1/k)*np.sqrt((k+1)/(k-1)*(1-(P_atm/P_chamber2)**((k-1)/k)))  # Inverse of area ratio for doubled chamber pressure
ExpR_2 = 1/ExpR_inv  # Area ratio for doubled chamber pressure

## OUTPUT
print(f"Exit Mach number = {M_exit:.4f}")
print(f"Exit Temp. = {T_exit:.2f} K")
print(f"Exit Vel. = {V_exit:.2f} m/s")
print(f"Atmospheric Pressure = {P_atm:.4f} Pa")
print(f"Chamber Pressure = {P_chamber:.4f} Pa")
print(f"Pressure Ratio (Pc/Pe) = {Pc_Pe:.4f}")
print(f"New Chamber Pressure if Doubled = {P_chamber2:.4f} Pa")
print(f"New Exit Pressure = {P_e2:.4f} Pa")
print(f"Thrust Coefficient at Original Chamber Pressure = {CF1:.4f}")
print(f"Thrust Coefficient at Doubled Chamber Pressure = {CF2:.4f}")
print(f"Force Percent Difference = {F_dif:.2f} %")
print(f"Optimal Area Ratio for Doubled Chamber Pressure = {ExpR_2:.4f}")
print(f"Optimal Area Ratio for Doubled Chamber Pressure (from M_opt2) = {ExpR_opt2:.4f}")
print("-----------------------------------------------------------------------------------")
print("If the chamber pressure is doubled, the thrust increases by approximately {:.2f}%, " \
"The optimal area ratio for the new chamber pressure is {:.4f}, " \
"which indicates that the original nozzle design is not optimal for the doubled chamber pressure.".format(F_dif, ExpR_2))