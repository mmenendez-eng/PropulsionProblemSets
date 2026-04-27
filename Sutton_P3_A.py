"""Sutton Extra Problem 3A:
Some data for the MA-5A multiple liquid propellant engines are shown below. 

Calculate: 
the mass flow rate and
the nozzle area ratio for each for each component. 

Assume individual flow rates remain constant during rocket operation.
The last table entry represents a needed chemical thermodynamics input.

NOTE ON MASS FLOW RATE:

This script uses the physically consistent relation:
    mdot = F / (Isp * g0)

The Sutton Solutions Manual often reports mass flow using:
    mdot = F / Isp

This omits g0 and treats lbm and lbf interchangeably under EE-unit conventions.
As a result, manual values for mdot will be higher by a factor of ~32.2.

Despite this difference, the computed nozzle area ratios remain consistent with
the Sutton solutions because the same unit convention is embedded in the
tabulated P1/c* values, causing the discrepancy to cancel out.

All calculations here retain explicit g0 for dimensional consistency.
"""
import numpy as np

## GIVEN/CONSTANTS
F_thrust_sealevel = np.array([215e3, 60e3, 415])  # Thrust at sea level (lbf)
F_thrust_vacuum = np.array([240e3, 84e3, 500])  # Thrust in vacuum (lbf)
Isp_sealevel = np.array([264, 220, 240])  # Specific impulse at sea level (s)
Isp_vacuum = np.array([295, 309, 290])  # Specific impulse in vacuum (s)
P1_cstar = np.array([0.1287, 0.1287, 0.1005])  # P1/c* (lbf/in^2/ft/s)
g0 = 32.2  # Standard gravity (ft/s^2)
Psl = 14.7  # Standard sea level pressure (lbf/in^2)

## FUNCTIONS
def calculate_mdot(F_thrust, Isp):
    """Calculate mass flow rate (mdot) from thrust and specific impulse."""
    return F_thrust / (Isp * g0)  # Mass flow rate (lbm/s)

def calculate_nozzle_throat_area(P1_cstar, mdot):
    """Calculate nozzle throat area from P1/c* and mass flow rate."""
    return mdot/P1_cstar  # Nozzle throat area (in^2)

## ANALYSIS
# Calculate mass flow rate (mdot) for each engine component
mdot = calculate_mdot(F_thrust_vacuum, Isp_vacuum)  # Mass flow rate in vacuum (lbm/s)

# Calculate nozzle throat area for each engine component
At = calculate_nozzle_throat_area(P1_cstar, mdot)  # Nozzle throat area (in^2) 

# Calculate nozzle exit area
Ae = (F_thrust_vacuum - F_thrust_sealevel)/Psl  # in^2

# Calculate nozzle area ratio (Ae/At)
AreaRatio = Ae / At  # Nozzle area ratio
print("                           Booster      Sustainer      Vernier")
print("Mass Flow Rate (lbm/s) : ", mdot)
print("Area Ratio (Ae/At) :     ", AreaRatio)
