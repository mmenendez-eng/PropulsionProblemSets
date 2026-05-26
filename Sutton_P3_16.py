"""
An ideal rocket has the following characteristics:

Chamber pressure = 27.2 atm
Nozzle exit pressure = 3 psia
Specific heat ratio = 1.20
Average molecular mass = 21.0 lbm/lb-mol
Chamber temperature = 4200 ∘F

Determine the critical pressure ratio, the gas velocity at the throat, the expansion area ratio,
and the theoretical nozzle exit velocity.
"""
import numpy as np
from scipy.optimize import brentq

## GIVEN/CONSTANTS
Pc = 27.2   # Chamber Pressure, atm
Pe = 3      # Nozzle Exit Pressure, psia
Pe = Pe/14.696 # Nozzle Exit Pressure, atm
k = 1.20    # Specific Heat Ratio
Mol = 21.0  # Avg. Molecular Mass, lbm/lbf.mol
Tc = 4200   # Chamber Temperature, deg. F
Tc = Tc + 459.67    # Chamber Temperature, deg. R
R_ = 1545   # Universal Gas Constant, ft.lbf/lbm.mol.R
g0 = 32.2   # ft/s^2
## FUNCTIONS

def exhaust_velocity(k,R,T1, pe_pc): # [EQ.3-16]
    'Need to revise for US units'
    return np.sqrt(2*g0*k*R*T1/(k-1)*(1-pe_pc**((k-1)/k))) # m/s

def crit_pressure_ratio(k): # [EQ.3-20] Pt/P1
    return (2/(k+1))**(k/(k-1)) # Typical values between 0.53 and 0.57

def crit_velocity(k,R,T1): # [EQ.3-23]
    return np.sqrt(2*g0*k*R*T1/(k+1))

## SOLUTION
# a) Critical Pressure Ratio
'Assume Pe = Pamb, optimal conditions'
'Assume M = 1 at nozzle throat'
Pt_P1 = crit_pressure_ratio(k)
print(f'Critical Pressure Ratio = {Pt_P1}')

# b) Gas Velocity at Throat
R = R_/Mol  #
vt = crit_velocity(k,R,Tc)
print(f'Specific Gas Constant = {R} ')
print(f'Throat Velocity = {vt} ft/s')

# c) Expansion Area Ratio
def pe_pc_from_mach(M, k):
    """Calculate the exit to chamber pressure ratio from Mach number using the isentropic flow relations."""
    return (1 + (k - 1) / 2 * M**2)**(-k / (k - 1)) # Returns Pe/Pc

def mach_from_pressure_ratio(pe_pc, k):
    f = lambda M: pe_pc_from_mach(M, k) - pe_pc
    return brentq(f, 1.0001, 20.0)  # Solve for Mach number given a pressure ratio, with bounds to ensure we find a supersonic solution

M_exit = mach_from_pressure_ratio(Pe/Pc,k) # Note: Using Pe/Pc

def area_mach(M, k):
    return (1.0 / M) * ((2.0 / (k + 1.0)) * (1.0 + (k - 1.0) / 2.0 * M**2))**((k + 1.0) / (2.0 * (k - 1.0)))

ExpR = area_mach(M_exit,k)

print(f'Exit Mach = {M_exit}')
print(f'Expansion Area Ratio = {ExpR}')

# d) Nozzle Exit Velocity
c = exhaust_velocity(k,R,Tc,Pe/Pc)
print(f'Nozzle Exit Velocity = {c} ft/s')