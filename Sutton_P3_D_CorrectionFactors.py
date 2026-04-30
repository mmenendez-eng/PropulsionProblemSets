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
actual_T1 = 6200 # deg. F
actual_T1 = actual_T1 + 459.67 # convert to deg. R
actual_P1 = 1000 # psia
k = 1.24
Mol = 23.3 # lbm/lb-mol
g0 = 32.2 # ft/s^2
R_universal = 1544 # universal gas constant, ft-lbf/lb-mol-R
actual_cstar = 1680*3.281  # experimental value, ft/s
zeta_CF = 0.94

## FUNCTIONS
def cstar(k,R,T):
    return np.sqrt(k*R*T)/(k*np.sqrt((2/(k+1))**((k+1)/(k-1))))

## ANALYSIS
# a) Calculate c*-efficiency
R_specific = R_universal/(Mol*g0)
ideal_cstar = cstar(k,R_specific,actual_T1) # m/s
zeta_cstar = actual_cstar/ideal_cstar
# b) Calculate effective exhuast velocity correction factor
zeta_velocity = zeta_cstar*zeta_CF

## OUTPUT
print(f'Ideal c*-efficiency = {ideal_cstar:.3f} ft/s')
print(f'Ideal c*-efficiency = {ideal_cstar/3.281:.3f} m/s')
print(f'Effective Exhaust Velocity Correction Factor = {zeta_velocity:.3f}')