"""SUTTON EXTRA PROBLEM 3C: 

The thrust developed by a thermal rocket propulsion system is 900 lbf when the mass flow rate is 5.20 lbm/sec. The
nozzle has a minimum area of 1.0 in2 and a discharge area of 4.12 in2. Using the applicable thrust coefficient of 1.50
and a specific heat ratio of 1.30, find the corresponding ideal values of p1, p2, p3 in psia.

"""
import numpy as np
from scipy.optimize import fsolve

## GIVEN/CONSTANTS
F_thrust = 900 # Thrust, lbf
mdot = 5.20 # Mass Flow Rate, lbm/s
At = 1.0    # Nozzle Throat Area, in^2
Ae = 4.12   # Nozzle Exit Area, in^2
CF = 1.50   # Thrust Coefficient
k = 1.30    # Specific Heat Ratio
g0 = 32.2*12   # Standard Gravity, in/s^2

## FUNCTIONS
def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.5)[0]  # Initial guess for supersonic flow
    return M_exit

def calculate_pressure_ratio(M, k):
    """Calculate the chamber to Exit Pressure Ratio from Mach number using the isentropic flow relations."""
    Pc_Pe = (1 + (k - 1) / 2 * M**2)**(k / (k - 1))
    return Pc_Pe # Returns Pc/Pe

def thrust_coefficient(k, pe_pc, pa_pc, eps):
    momentum = np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - pe_pc**((k - 1) / k))
    )
    pressure = (pe_pc - pa_pc) * eps
    return momentum + pressure

## SOLVE
P1 = F_thrust/(CF*At)   # Nozzle Entry Pressure, psi
area_ratio = Ae/At  # Nozzle Area Ratio
exit_mach = calculate_exit_mach_number(area_ratio, k)       
pressure_ratio = calculate_pressure_ratio(exit_mach,k)      # Pressure Ratio, Pc/Pe

P2 = P1/pressure_ratio  # Nozzle Exit Pressure, psi

CF_pressure = CF - np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - (1/pressure_ratio)**((k - 1) / k)))

P3 = P2 - P1 * CF_pressure/area_ratio

print(f'Nozzle Entry Pressure = {P1:.2f} psi')
print(f'Nozzle Exit Pressure = {P2:.2f} psi')
print(f'Ambient Pressure = {P3:.2f} psi')