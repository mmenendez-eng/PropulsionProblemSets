import matplotlib.pyplot as plt
import numpy as np

"""
The actual conditions for an optimum expansion nozzle operating at sea level are given
below. 
Calculate v2, T2, and CF . 
The mass flow m˙ = 3.7 kg/sec; 
p1 = 2.1 MPa; 
T1 = 2585 K;
M = 18.0 kg/kg-mol; 
and k = 1.30.
"""

# Given Constants
mdot = 3.7                      # kg/s
P_c = 2.1                        # MPa
T_c = 2585.0                       # K
M_w = 18.0                          # kg/kg-mol
k = 1.3
R = 8314.3                      # J/kg.k, universal
P_amb = 0.101                    # MPa


# Solve
PR = P_amb/P_c

v2 = np.sqrt(2*k/(k-1)*R*T_c/M_w*(1-(PR)**((k-1)/k)))

T2 = T_c*(PR**((k-1)/k))

print('Pressure Ratio = ',PR)
print('Exit Temperature =', T2, 'Kelvin')
print('Exit Velocity =', v2, 'm/s')


