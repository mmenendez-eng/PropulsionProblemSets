""" 
Sutton Problem 3.1 - Thermodynamics of Combustion Gases

Purpose:
Compute specific heats (Cp and Cv) for combustion products using ideal gas relations.

Significance:
    Specific heats are critical for:
- Nozzle flow calculations
- Exhaust velocity predictions
- Energy balance in propulsion systems

Assumptions:
- Ideal gas behavior
- Constant specific heat ratio (k)
"""

## GIVEN/CONSTANTS
k = 1.22            # Specific Heat Ratio
M_w = 23.2          # kg/kg-mol, Molecular Weight: O2 + Gasoline (L)
R_universal = 8314.3          # J/kg-mol-K, Universal Gas Constant

## ANALYSIS

# Calculate specific gas constant (R_specific)
R_specific = R_universal / M_w   # J/kg-K

'''
From Ideal Gas Relations:
    Cp - Cv = R_specific
    k = Cp / Cv
    Cp = k*R_specific / (k - 1)
'''

# Calculate Cp and Cv
Cp = k*R_specific / (k - 1)   # Heat Capacity at Constant Pressure, J/kg-K
Cv = Cp/k             # Heat Capacity at Constant Volume, J/kg-K

## OUTPUT
print(f'Cp = {Cp:.2f} J/kg-K')
print(f'Cv = {Cv:.2f} J/kg-K')
