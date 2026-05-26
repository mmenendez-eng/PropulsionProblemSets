## Sutton Problem 3.4

print("""SUTTON PROBLEM 3.4
   Nitrogen at 500◦C (k = 1.38, molecular mass is 28.00) flows at a Mach number of
2.73. What are its actual and its acoustic velocity?
""")

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

# Given
k = 1.38                    # Heat Specific Ratio
T = 500                     # Gas Temp, Celsius
M_w = 28                    # Molecular Mass, kg/kg.mole
Mach = 2.73                 # Mach Number
R = 8314.4                  # J/kg.mole.K

# Analysis
R_ = R/M_w                   # J/kg.K
T = T + 273                 # Kelvin

def sonic_velocity(k,R,T):
    return np.sqrt(k*R*T)

a = sonic_velocity(k,R_,T)
v = Mach*a

# Output
print('Acoustic Velocity = ',a,' m/s')
print('Gas Velocity = ',v,' m/s')
