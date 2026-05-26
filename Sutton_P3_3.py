## Sutton Problem 3.3

print("""SUTTON PROBLEM 3.3
    A certain nozzle expands a gas under isentropic conditions. Its chamber or nozzle
entry velocity equals 90 m/sec, its final velocity 1500 m/sec. What is the change in
enthalpy of the gas? What percentage of error is introduced if the initial velocity is
neglected?
""")
# Import Libraries/Modules
import numpy as np

# Given Constants
v_i = 90              # m/s
v_f = 1500            # m/s


# Change in Enthalpy
def enth(h0,v):                             # FUNCTION: ENTHALPY, m^2/s^2
    return h0 + (v**2)/2

h_i = enth(0,v_i)
h_f = enth(0,v_f)
dh = h_f - h_i

# Percentage Error Neglecting Initial Velocity
dh_2 = h_f

err= (dh - dh_2)/dh*100

# Output
print('OUTPUT:')
print('Change in enthalpy = ',dh,'m^2/s^2')
print('Change in enthalpy w/o v_i = ',dh_2,'m^2/s^2')
print('Error = ',err,'%')
print('In other words, this demonstrates that it is safe to assume that combustion chamber speeds are v=0')
print('prior to reaching nozzle entrance.')



