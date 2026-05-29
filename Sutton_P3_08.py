print("""SUTTON PROBLEM 3-8
For an ideal rocket with:
- a characteristic velocity c* = 1500 m/sec
- a nozzle throat diameter of 20 cm
- a thrust coefficient of 1.38
- and a mass flow rate of 40 kg/sec
compute the chamber pressure, the thrust, and the specific impulse.
""")

## IMPORT
import numpy as np

## GIVEN/CONSTANTS
cstar = 1500                # m/s
Dt = 20/100                 # m
CF = 1.38           
mdot = 40                   # kg/s
g0 = 9.81                   # m/s^2

## ANALYSIS
# Chamber Pressure
At = np.pi/4*Dt**2          # m^2
Pc = mdot*cstar/At          # Pa

# Thrust
F_thrust = CF*At*Pc         # N

# Specific Impulse
Isp = F_thrust/(mdot*g0)    # s

## OUTPUT
print('RESULTS:')
print(f'Chamber Pressure = {Pc/(1e6):.2f} MPa')
print(f'Thrust = {F_thrust/(1e3):.2f} kN')
print(f'Specific Impulse = {Isp:.2f} s')