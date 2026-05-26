""" Problem 3.17
 For an ideal rocket with a characteristic velocity c∗ of 1220 m/sec, a mass flow rate of
73.0 kg/sec, a thrust coefficient of 1.50, and a nozzle throat area of 0.0248 m2, compute
the effective exhaust velocity, 
the thrust, 
the chamber pressure, 
and the specific impulse.

"""
import numpy as np

## GIVEN/CONSTANTS
cstar = 1220    # Characteristic Velocity, m/s
mdot = 73.0     # Mass Flow Rate, kg/s
CF = 1.50       # Thrust Coefficient
At = 0.0248     # Nozzle Throat Area, m^2

## SOLUTION

c = cstar*CF        # Effective Exhaust Velocity, m/s
F = mdot*cstar*CF   # Thrust, N
Pc = F/(At*CF)      # Chamber Pressure, Pa
Isp = c/9.81        # Specific Impulse, s

## OUTPUT
print(f"Characteristic Velocity = {c} m/s")
print(f"Thrust = {F} N")
print(f"Chamber Pressure = {Pc} Pa")
print(f"Specific Impulse = {Isp} s")
