""" SUTTON PROBLEM 2.1

A jet of fluid hits a stationary flat plate perpendicularly.

(a) If there is 50 kg of fluid flowing per minute at an absolute velocity of 200 m/sec,
what will be the force on the plate?

(b) What will this force be when the plate moves in the direction of flow at u = 50
km/h? Explain the methodology.

"""
## GIVEN/CONSTANTS
mass_flow = 50/60                                       # Mass Flow Rate, kg/s
jet_velocity = 200                                      # Jet Velocity, m/s
plate_velocity = 50*1000/3600                           # Plate Velocity, m/s

## ANALYSIS
# Case 1: Stationary Plate
F1 = mass_flow*jet_velocity                             # Force at Plate, N

# Case 2: Moving Plate
# Since the plate is moving in the direction of flow, the mass flow rate with reference to the moving plate has now decreased.
rho_Area = mass_flow/jet_velocity                       # Density*Area, kg/m
relative_velocity = jet_velocity - plate_velocity       # Relative Jet Velocity, m/s
mass_flow_relative = rho_Area*(relative_velocity)       # Relative Mass Flow Rate (at plate), kg/s

F2 = mass_flow_relative*relative_velocity               # Force at Plate, N

## OUTPUT
print(f'Case 1 Force = {F1:.2f} N')
print(f'Jet Velocity = {jet_velocity:.2f} m/s')
print(f'Mass Flow Rate = {mass_flow:.2f} kg/s')
print(f'Case 2 Force = {F2:.2f} N')
print(f'Relative Velocity = {relative_velocity:.2f} m/s')
print(f'Relative Mass Flow Rate = {mass_flow_relative:.2f} kg/s')