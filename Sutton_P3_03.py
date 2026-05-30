print("""SUTTON PROBLEM 3.3
    A certain nozzle expands a gas under isentropic conditions. Its chamber or nozzle
entry velocity equals 90 m/sec, its final velocity 1500 m/sec. What is the change in
enthalpy of the gas? What percentage of error is introduced if the initial velocity is
neglected?
""")
## IMPORT
import numpy as np

## GIVEN / CONSTANTS
v_i = 90                        # m/s, Initial Velocity
v_f = 1500                      # m/s, Final Velocity

## FUNCTIONS
def enth(h0,v):                             
    return h0 + (v**2)/2        # m^2/s^2, Enthalpy

## ANALYSIS

# Change in Enthalpy from Initial to Final State
dh = enth(0,v_f) - enth(0,v_i)  # m^2/s^2

# Percentage Error Neglecting Initial Velocity
dh_2 = enth(0,v_f)              # m^2/s^2
err = (dh - dh_2)/dh*100         # %

## OUTPUT
print('SUTTON PROBLEM 3-3 RESULTS:\n')
print(f'Change in enthalpy                      = {dh:.2f} m^2/s^2')
print(f'Change in enthalpy w/o initial velocity = {dh_2:.2f} m^2/s^2')
print(f'Percent Error                           = {err:.2f}%')
print('\nIn other words, this demonstrates that it is safe to assume that combustion chamber speeds are v=0')
print('prior to reaching nozzle entrance.')



