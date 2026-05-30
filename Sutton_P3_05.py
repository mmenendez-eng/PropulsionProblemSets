print("""SUTTON PROBLEM 3.5
    The following data are given for an optimum rocket:
- Average molecular mass 24 kg/kg-mol
- Chamber pressure 2.533 Mpa
- External pressure 0.090 Mpa
- Chamber temperature 2900 K
- Throat area 0.00050 m2
- Specific heat ratio 1.30
    
    Determine: 
    (a) throat velocity; 
    (b) specific volume at throat; 
    (c) propellant flow and specific impulse; 
    (d) thrust; 
    (e) Mach number at throat.
    """)

## IMPORT
import numpy as np

## GIVEN / CONSTANTS
M_mol = 24                      # kg/kg.mol, Molecular Mass
P_c = 2.533e6                   # Pa, Chamber Pressure
P_a = 0.090e6                   # Pa, Ambient Pressure
T_c = 2900                      # K, Chamber Temperature
A_t = 0.00050                   # m^2, Nozzle Throat Area
k = 1.30                        # Specific Heat Ratio
g = 9.81                        # m/s^2, Standard Gravity
R_u = 8314.4                    # J/kg.K, Universal Gas Constant

## FUNCTIONS
def exhaust_velocity(k: float, R: float, T_c: float, pe_pc: float) -> float:
    """Return ideal isentropic exhaust velocity, Eq. 3-16 style."""
    return np.sqrt((2.0 * k / (k - 1.0)) * R * T_c * (1.0 - pe_pc ** ((k - 1.0) / k)))

## ANALYSIS

# (A) Throat Velocity
R = R_u / M_mol                             # J/(kg.mol.K),  Specific gas constant
v_t = np.sqrt(2 * k * R * T_c / (k + 1))    #  m/s, Throat Velocity

# (B) Throat Specific Volume
T_t = 2 * T_c / (k + 1)                     # K, Throat Temperature
P_t = P_c * (2 / (k + 1))**(k / (k - 1))    # Pa, Throat Pressure
V_t = R * T_t / P_t                         # m^3/kg, Throat Specific Volume

# (C) Propellant Flow and Specific Impulse
mdot = A_t * v_t / V_t                      # kg/s, Mass Flow Rate        
Pe_Pc = P_a / P_c                           # Optimal Conditions
c = exhaust_velocity(k, R, T_c, Pe_Pc)      # m/s, Exhaust Velocity
I_sp = c / g                                # s, Specific Impulse              

# (D) Thrust
F = mdot * c                              # N, Thrust

# (E) Mach Number at Throat
M_t = v_t / np.sqrt(k * R * T_t)          # Mach No.

## OUTPUT
print('SUTTON PROBLEM 3.5 RESULTS')
print(f'Throat Velocity         = {v_t:.2f} m/s')
print(f'Throat Specific Volume  = {V_t:.2f} m^3/kg')
print(f'Propellant Flow         = {mdot:.2f} kg/s')
print(f'Specific Impulse        = {I_sp:.2f} s')
print(f'Thrust                  = {F:.2f} N')
print(f'Throat Mach Number      = {M_t:.2f}')