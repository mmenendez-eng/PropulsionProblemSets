print("""SUTTON PROBLEM 3-10
    What is the maximum velocity if the nozzle in Example 3-2 was designed to expand into
a vacuum? If the expansion area ratio was 2000?""")

## IMPORT
import numpy as np
from scipy.optimize import fsolve

## GIVEN/CONSTANTS
P_c = 2.068e6           # Pa, Chamber Pressure
T_c = 2222              # K, Chamber Temperature
mdot = 1.0              # kg/s, Mass Flow Rate
k = 1.30
R = 345.7               # J/kg.K, Specific Gas Constant
g0 = 9.81               # m/s^2, Standard Gravity
P_amb = 101.325e3       # Pascals, Ambient Pressure
ExpR = 2000             # Nozzle Expansion Ratio, Ae/At

## FUNCTIONS
def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 8)[0]  # Initial guess for supersonic flow
    return M_exit

def ideal_max_exhaust_velocity(k, R, Tc):
    return np.sqrt(2 * k * R * Tc / (k - 1))

def exhaust_velocity(k, Tc, R, P1, P2):
    """Calculates exhaust velocity based on pressure ratio and chamber conditions"""
    return np.sqrt(2 * k / (k - 1) * R * Tc * (1 - (P2 / P1)**((k - 1) / k)))


## ANALYSIS
# Maximum Exhaust Velocity:
# - at Vacuum (ExpR -> Inf)
v_max = ideal_max_exhaust_velocity(k, R, T_c) # m/s

# - at given Expansion Ratio (ExpR = 2000)
Me = calculate_exit_mach_number(ExpR, k)     # Exit Mach No.
T_e = T_c / (1 + (k - 1) / 2 * Me**2)               # Kelvin
v_max_real = Me * np.sqrt(k * R * T_e)            # m/s

## OUTPUT
print('\nRESULTS')
print(f'Maximum Exhaust Velocity at Vacuum       (ExpR -> Inf) = {v_max:.2f} m/s')
print(f'Maximum Exhaust Velocity at Design Point (ExpR = 2000) = {v_max_real:.2f} m/s')
