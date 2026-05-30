print("""SUTTON PROBLEM 3.4
   Nitrogen at 500◦C (k = 1.38, molecular mass is 28.00) flows at a Mach number of
2.73. What are its actual and its acoustic velocity?
""")

## IMPORT
import numpy as np

## GIVEN / CONSTANTS
k = 1.38                    # Specific Heat Ratio
T = 500 + 273               # Celsius to Kelvin, Gas Temperature
M_mol = 28                  # Molecular Mass, kg/kg.mole
Mach = 2.73                 # Mach Number
R_u = 8314.4                # J/kg.mole.K, Universal Gas Constant

## ANALYSIS
R = R_u / M_mol             # J/kg.K, Specific Gas Constant
a = np.sqrt(k * R * T)      # m/s, Acoustic Velocity
v = Mach * a                # m/s, Gas Velocity

## OUTPUT
print('SUTTON PROBLEM 3.4 RESULTS:\n')
print(f'Acoustic Velocity = {a:.2f} m/s')
print(f'Gas Velocity = {v:.2f} m/s')
