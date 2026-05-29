print("""SUTTON PROBLEM 3-11
    Construction of a variable-area conventional axisymmetric nozzle has often been
considered to operate a rocket thrust chamber at the optimum expansion ratio at any
altitude. Because of the enormous difficulties of such a mechanical device, it has never
been successfully realized. However, assuming that such a mechanism could eventually
be constructed, what would have to be the variation of the area ratio with altitude
(plot up to 50 km) if such a rocket had a chamber pressure of 20 atm? 
Assume that k = 1.20.
""")

## IMPORT
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

## GIVEN/CONSTANTS
P_c = 20            # atm, Chamber Pressure
k = 1.20            # Specific Heat Ratio
P_sl = 101325       # Pa, Sea Level Pressure
# Taken from Appendix 2 Table 1, Sutton
P_amb_ratio = np.asarray([1, .887, .66919, .53313, .26151, 2.5158e-2, 7.8735e-4])
alt = np.asarray([0, 1e3, 3e3, 5e3, 10e3, 25e3, 50e3])              # m, Altitude

## FUNCTIONS
def pe_pc_from_mach(M, k):
    """Calculate the exit to chamber pressure ratio from Mach number using the isentropic flow relations."""
    return (1 + (k - 1) / 2 * M**2)**(-k / (k - 1)) # Returns Pe/Pc

def mach_from_pressure_ratio(pe_pc, k):
    f = lambda M: pe_pc_from_mach(M, k) - pe_pc
    return brentq(f, 1.0001, 20.0)  # Solve for Mach number given a pressure ratio, with bounds to ensure we find a supersonic solution

def area_mach(M, k):
    return (1.0 / M) * ((2.0 / (k + 1.0)) * (1.0 + (k - 1.0) / 2.0 * M**2))**((k + 1.0) / (2.0 * (k - 1.0)))

## ANALYSIS
P_c = 20 * P_sl               # Converts from atm to Pa
P_amb = P_sl * P_amb_ratio    # Pa, Ambient Pressure Array
PressRatio = P_c / P_amb      # Controlling Pressure Ratio Array

Me = np.asarray([mach_from_pressure_ratio(pr,k) for pr in 1 / PressRatio])
AreaRatio = area_mach(Me, k)


plt.figure()
plt.semilogx(AreaRatio, alt / 1000, marker="o")
plt.title('Optimum Nozzle Area Ratio vs Altitude')
plt.ylabel('Altitude, km')
plt.xlabel('Area Ratio, Ae/At')
plt.grid(True)
plt.show()