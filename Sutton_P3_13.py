""" Sutton P3.13:
The German World War II A-4 propulsion system had a sea-level thrust of 25,400 kg and
a chamber pressure of 1.5 Mpa. If the exit pressure is 0.084 MPa and the exit diameter
740 mm, what would be its thrust at 25,000 m?

"""

import numpy as np


## GIVEN/CONSTANTS
F_sl = 25400*9.81 # N, Thrust at sea level
P_sl = 101325 # Pa, Pressure at sea level
Pc = 1.5e6 # Pa, Chamber Pressure
Pe = 0.084e6 # Pa, Exit Pressure
De = 0.740 # m, Nozzle Exit Diameter
h = 25000 # m, operating altitude


## CALCULATIONS
P_atm1 = P_sl               # Sea level Atmospheric Pressure
P_atm2 = P_sl*0.025158      # Atmospheric Pressure at 25 km altitude

F_momentum = F_sl - (Pe - P_atm1)*np.pi/4*De**2  # Momentum Thrust at Sea Level

F_thrust = F_momentum + (Pe - P_atm2)*np.pi/4*De**2  # Thrust at 25 km altitude

print(f"Atmospheric pressure at {h} m: {P_atm2:.2f} Pa")
print(f"Thrust at sea level: {F_sl:.2f} N")
print(f"Momentum Thrust at sea level: {F_momentum:.2f} N")
print(f"Thrust at {h} m: {F_thrust:.2f} N")