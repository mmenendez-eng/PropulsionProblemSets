"""Sutton Extra Problem 3D. 

Non-ideal behavior may be taken into account with a suitable efficiency (ηx) or equivalently with a correction factor (ζx). 
For a certain thermal thruster, the following information applies:

T1 = 6200 °F, 
p1 = 1000 psia, 
k = 1.24, and 
M = 23.3 lbm/lb-mol

If the experimental value for (c*)a (or (p1)a*(At)a /(mdot)a) is found to be 1680 m/sec, 
a) calculate the c*-efficiency for this thruster. 

Also, if ζCF = 0.94, 
b) calculate an "effective exhaust velocity correction factor" (ζc).
"""

## IMPORTS
import numpy as np

## GIVEN/CONSTANTS
actual_T1 = 6200    # Chamber temperature, deg. F
actual_P1 = 1000    # Chamber pressure, psia
k = 1.24            # Specific Heat Ratio
Mol = 23.3          # Molecular mass, kg/kmol
R_universal = 8314  # Universal gas constant, J/(kmol-K)
actual_cstar = 1680 # Experimental c*, m/s
zeta_CF = 0.94      # Thrust Coefficient correction factor

## FUNCTIONS
def cstar(k,R,T):
    return np.sqrt(k*R*T)/(k*np.sqrt((2/(k+1))**((k+1)/(k-1)))) # m/s

def fahrenheit_to_kelvin(T_F):
    return (T_F-32)*5/9 + 273.15

## ANALYSIS
# Convert temperature from deg. F to Kelvin
T1_K = fahrenheit_to_kelvin(actual_T1) # K

# a) Calculate c*-efficiency
R_specific = R_universal/(Mol)
ideal_cstar = cstar(k,R_specific,T1_K) # m/s
zeta_cstar = actual_cstar/ideal_cstar
# b) Calculate effective exhuast velocity correction factor
zeta_velocity = zeta_cstar*zeta_CF

## OUTPUT
print(f'Ideal c* = {ideal_cstar:.0f} m/s')
print(f'c*-efficiency = {zeta_cstar:.3f}')
print(f'Effective Exhaust Velocity Correction Factor = {zeta_velocity:.3f}')