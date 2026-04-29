""" SUTTON EXTRA PROBLEM 3B

Using realistic correction factors, design a rocket nozzle to conform to the following  condiitions:

- Chamber pressure                  = 20.4 atm = 2.068 MPa
- Atmospheric pressure              = 1.0 atm
- Chamber temperature               = 2861 K
- Mean molecular mass of gases      = 21.87 kg/kg-mol
- Ideal specific impulse            = 230 sec (at operating conditions)
- Specific heat ratio               = 1.229
- Desired thrust                    = 1300 N

Determine the following: 
a) actual nozzle throat and exit areas, 
b) respective diameters, 
c) actual exhaust velocity, and 
d) actual specific impulse. 

Take ζF = 0.96 and ζv = 0.92. 

"""
import numpy as np
from scipy.optimize import brentq

## GIVEN/CONSTANTS
Pc = 2.068e6            # Chamber pressure, Pa
Pa = Pc/20.4            # Atmospheric pressure, Pa
Tc = 2861               # Chamber temperature, K   
Mol = 21.87             # Mean molecular mass, kg/kg-mol
Isp_ideal = 230         # Ideal specific impulse, sec
k = 1.229               # Specific heat ratio
F_actual = 1300         # Desired thrust, N
zeta_F = 0.96           # Thrust correction factor
zeta_v = 0.92           # Velocity correction factor
R_specific = 8314.5/Mol # Specific gas constant, J/kg-K
g0 = 9.81               # Standard gravity, m/s^2
## FUNCTIONS
def exhaust_velocity(k,R,T1, pe_pc): # [EQ.3-16]
    return np.sqrt(2*k*R*T1/(k-1)*(1-pe_pc**((k-1)/k))) # m/s

def pe_pc_from_mach(M, k):
    """Calculate the exit to chamber pressure ratio from Mach number using the isentropic flow relations."""
    return (1 + (k - 1) / 2 * M**2)**(-k / (k - 1)) # Returns Pe/Pc

def mach_from_pressure_ratio(pe_pc, k):
    f = lambda M: pe_pc_from_mach(M, k) - pe_pc
    return brentq(f, 1.0001, 20.0)  # Solve for Mach number given a pressure ratio, with bounds to ensure we find a supersonic solution

def area_mach(M, k):
    return (1/M)*((2/(k+1))*(1+(k-1)/2*M**2))**((k+1)/(2*(k-1)))

def thrust_coefficient(k, pe_pc, pa_pc, eps):
    momentum = np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - pe_pc**((k - 1) / k))
    )
    pressure = (pe_pc - pa_pc) * eps
    return momentum + pressure

## ANALYSIS
# Assume: optimal conditions (Pe = Pa)

# a) Calculate nozzle throat and exit areas

M_exit_actual = mach_from_pressure_ratio(Pa/Pc, k)  # Actual Exit Mach number
ExpR = area_mach(M_exit_actual, k)  # Area ratio (Ae/At)
CF_ideal = thrust_coefficient(k, Pa/Pc, Pa/Pc, ExpR)   # Ideal thrust coefficient at optimal expansion

At_actual = F_actual/(zeta_F*CF_ideal*Pc)*(1e4)   # Actual nozzle throat area, cm^2
Ae_actual = At_actual*ExpR    # Actual nozzle exit area, cm^2

# b) Calculate respective diameters
Dt, De = 2*np.sqrt(At_actual/np.pi), 2*np.sqrt(Ae_actual/np.pi) # cm


# c) Calculate actual exhaust velocity
v_ideal = Isp_ideal*g0  # m/s
v_actual = v_ideal*zeta_v # m/s
Isp_actual = Isp_ideal*zeta_v # sec


## OUTPUT
print(f'Actual Nozzle Throat Area: {At_actual:.6e} cm^2')
print(f'Actual Nozzle Throat Diameter: {Dt:.4f} cm')
print(f'Actual Nozzle Exit Area: {Ae_actual:.6e} cm^2')
print(f'Actual Nozzle Exit Diameter: {De:.4f} cm')
print(f'Actual Exhaust Velocity: {v_actual:.2f} m/s')
print(f'Actual Specific Impulse: {Isp_actual:.2f} sec')