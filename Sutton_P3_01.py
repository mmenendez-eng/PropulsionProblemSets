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

## GIVEN / CONSTANTS
k = 1.22                # Specific Heat Ratio
M_mol = 23.2            # kg/kg-mol, Molecular Weight: O2 + Gasoline (L)
R_u = 8314.3            # J/kg-mol-K, Universal Gas Constant

## ANALYSIS

R = R_u / M_mol         # J/kg-K , Specific Gas Constant

'''
From Ideal Gas Relations:
    Cp - Cv = R
    k = Cp / Cv
    Cp = k * R / (k - 1)
'''

# Calculate Heat Capacities
Cp = k * R / (k - 1)   # J/kg-K, Heat Capacity at Constant Pressure
Cv = Cp / k            # J/kg-K, Heat Capacity at Constant Volume

## OUTPUT
print('RESULTS')
print(f'Heat Capacity at Constant Pressure = {Cp:.2f} J/kg-K')
print(f'Heat Capacity at Constant Volume   = {Cv:.2f} J/kg-K')
