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
cstar = 1500                # m/s, Characteristic Velocity
D_t = 20/100                # m, Nozzle Throat Diameter
CF = 1.38                   # Thrust Coefficient
mdot = 40                   # kg/s, Mass Flow Rate
g0 = 9.81                   # m/s^2, Standard Gravity

## ANALYSIS
# Chamber Pressure
A_t = np.pi / 4 * D_t**2    # m^2, Nozzle Throat Area
P_c = mdot * cstar / A_t    # Pa

# Thrust
F = CF * A_t * P_c          # N

# Specific Impulse
I_sp = F / (mdot * g0)      # s

## OUTPUT
print('SUTTON PROBLEM 3.8 RESULTS')
print(f'Chamber Pressure = {P_c/(1e6):.2f} MPa')
print(f'Thrust = {F/(1e3):.2f} kN')
print(f'Specific Impulse = {I_sp:.2f} s')