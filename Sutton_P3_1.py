""" Sutton P3.1:
Certain experimental results indicate that the propellant gases of a liquid oxygen and
gasoline reaction have:

 - a mean molecular mass of 23.2 kg/kg-mol and 
 - a specific heat ratio of 1.22. 
 
Compute the specific heat at constant pressure and at constant volume,
assuming a perfect gas.
"""

## GIVEN/CONSTANTS
k = 1.22            # Specific Heat Ratio
M_w = 23.2          # kg/kg-mol, Molecular Weight: O2 + Gasoline (L)
R = 8314.3          # J/kg-mol-K, Universal Gas Constant

## ANALYSIS
C_p = k*R/((k-1)*M_w)   # Heat Capacity at Constant Pressure, J/kg-K
C_v = C_p/k             # Heat Capacity at Constant Volume, J/kg-K

## OUTPUT
print(f'C_p = {C_p:.2f} J/kg-K')
print(f'C_v = {C_v:.2f} J/kg-K')
