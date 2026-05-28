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

## GIVEN/CONSTANTS
M_w = 24                        # kg/kg.mol, Molecular Mass
P_c = 2.533e6                   # Pa, Chamber Pressure
P_amb = 0.090e6                 # Pa, Ambient Pressure
T_c = 2900                      # K, Chamber Temperature
A_t = 0.00050                   # m^2, Nozzle Throat Area
k = 1.30                        # Specific Heat Ratio

g = 9.81                        # m/s^2, standard gravity
R_ = 8314.4                     # J/kg.K, universal gas constant

## Solution

# (A) Throat Velocity
R = R_/M_w                      # J/(kg.mol.K),  Specific gas constant
v_t = np.sqrt(2*k*R*T_c/(k+1))  #  m/s, Throat Velocity

# (B) Throat Specific Volume
T_t = 2*T_c/(k+1)               # K, Throat Temperature
P_t = P_c*(2/(k+1))**(k/(k-1))  # Pa, Throat Pressure
V_t = R*T_t/P_t                 # m^3/kg, Throat Specific Volume

# (C) Propellant Flow and Specific Impulse
mdot = A_t*v_t/V_t                                                                                  # kg/s, Mass Flow Rate
c = np.sqrt(2*k/(k-1)*R*T_c*(1-(P_amb/P_c)**((k-1)/k)))                                             # m/s, Effective Exhaust Velocity
AreaR_inv = ((k+1)/2)**(1/(k-1))*(P_amb/P_c)**(1/k)*np.sqrt((k+1)/(k-1)*(1-(P_amb/P_c)**((k-1)/k))) # At/Ae, Area Ratio Inverse
A_e = A_t/AreaR_inv                                                                                 # m^2, Nozzle Exit Area
CF = np.sqrt(2*k**2/(k-1)*(2/(k+1))**((k+1)/(k-1))*(1-(P_amb/P_c)**((k-1)/k)))                      # Thrust Coefficient
Isp = P_c*A_t*CF/(mdot*g)                                                                           # s, Specific Impulse              
I_sp = c/g

# (D) Thrust
F = A_t*CF*P_c                      # N, Thrust

# (E) Mach Number at Throat
M_t = v_t/np.sqrt(k*R*T_t)          # Mach No.


# Output
print(f'Throat Velocity         = {v_t:.2f} m/s')
print(f'Throat Specific Volume  = {V_t:.2f} m^3/kg')
print(f'Propellant Flow         = {mdot:.2f} kg/s')
print(f'Specific Impulse        = {Isp:.2f} s')
print(f'Thrust                  = {F:.2f} N')
print(f'Throat Mach Number      = {M_t:.2f}')