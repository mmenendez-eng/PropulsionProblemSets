""" Problem 3-15
Assuming that the thrust correction factor is 0.985 and the discharge correction factor is
1.050 in Example 3–2, determine 
(a) the actual thrust; 
(b) the actual exhaust velocity;
(c) the actual specific impulse; 
(d) the velocity correction factor.
"""


import numpy as np

## GIVEN/CONSTANTS
corrF = 0.985   # Thrust Correction Factor
corrD = 1.050   # Discharge Correction Factor

Pc = 2.068e6    # Chamber Pressure, Pa
Tc = 2222       # Chamber Temperature, K
k = 1.30        # Specific Heat Ratio
R = 345.7       # Specific Gas Constant, J/kg.K
mdot = 1.0      # Mass Flow Rate, kg/s
g = 9.81        # grav. constant, m/s^2

# Assumptions (Optimal Conditions P2=P3)
Pe = 101325     # Exit Pressure, Pa

## Functions

def exhaust_velocity(k,R,T1, pe_pc): # [EQ.3-16]
    return np.sqrt(2*k*R*T1/(k-1)*(1-pe_pc**((k-1)/k))) # m/s


## Solution
Pe_Pc = Pe/Pc   # Pressure Expansion Ratio
c = exhaust_velocity(k,R,Tc,Pe_Pc)  # Ideal Nozzle Exit Velocity, m/s
F = mdot*c                          # Ideal Thrust, N

F_actual = F*corrF                  # Actual Thrust, N
mdot_actual = mdot*corrD            # Ideal Mass Flow Rate, kg/s
c_actual = F_actual/mdot_actual     # Actual Exit Velocity, m/s

corrv = F_actual/mdot_actual/c      # Exhaust Velocity Correction Factor

Isp = c/g                           # Ideal Specific Impulse, s
Isp_actual = Isp*corrv              # Actual Specific Impulse, s

## OUTPUT

print(f"Pressure Expansion Ratio (Pe/Pc) = {Pe_Pc}")
print(f"Ideal Effective Exhaust Velocity = {c} m/s")
print(f"Ideal Thrust = {F} N")
print(f"Ideal Specific Impulse = {Isp} s")
print(f"(a) Actual Thrust = {F_actual} N")
print(f"(b) actual exhaust velocity = {c_actual} m/s")
print(f"(c) actual specific impulse = {Isp_actual} s")
print(f"(d) velocity correction factor = {corrv} ")