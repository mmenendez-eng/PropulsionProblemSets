""" SUTTON PROBLEM 2.2

The following data are given for a certain rocket unit: 
- thrust = 8896 N 
- propellant consumption = 3.867 kg/sec 
- velocity of vehicle, 400 m/sec 
- energy content of propellant = 6.911 MJ/kg 

Assume 100% combustion efficiency.

Determine:
(a) the effective velocity; 
(b) the kinetic jet energy rate per unit flow of propellant;
(c) the internal efficiency; 
(d) the propulsive efficiency; 
(e) the overall efficiency;
(f) the specific impulse; 
(g) the specific propellant consumption.

"""

## GIVEN/CONSTANTS
thrust = 8896 # Thrust, N
mass_flow = 3.867 # Propellant Consumption/Mass Flow Rate, kg/s
vehicle_velocity = 400 # Vehicle Velocity, m/s
prop_specific_energy = 6.911e6 # Energy Content of Propellant, J/kg
comb_eff = 1    # Combustion Efficiency
g0 = 9.81 # Standard gravity, m/s^2

## ANALYSIS
# a) Effective Exhaust Velocity
c = thrust/mass_flow    # m/s

# b) Kinetic jet energy rate per unit flow of propellant
jet_power = 0.5*mass_flow*c**2              # J/s 
jet_specific_energy  = jet_power/mass_flow  # J/kg

# c) Internal Efficiency
chemical_power = mass_flow*prop_specific_energy # J/s 
internal_eff = jet_power/(comb_eff*chemical_power)

# d) Propulsive Efficiency
vehicle_power = thrust*vehicle_velocity # J/s
residual_jet_power = 0.5*mass_flow*(c - vehicle_velocity)**2    # J/s
prop_eff = vehicle_power/(vehicle_power + residual_jet_power)

# e) Overall Efficiency
overall_eff_product = comb_eff*internal_eff*prop_eff
overall_eff_direct = vehicle_power / chemical_power
# f) Specific Impulse
Isp = thrust/(mass_flow*g0)  # seconds

# g) Specific Propellant Consumption
SPC = 1/Isp             # 1/s

## OUTPUT
print(f"(a) Effective exhaust velocity: {c:.1f} m/s")
print(f"(b) Jet specific kinetic energy: {jet_specific_energy/1e6:.3f} MJ/kg")
print(f"(c) Internal efficiency: {internal_eff:.4f} = {internal_eff*100:.2f}%")
print(f"(d) Propulsive efficiency: {prop_eff:.4f} = {prop_eff*100:.2f}%")
print(f"(e) Overall efficiency, product method: {overall_eff_product:.4f} = {overall_eff_product*100:.2f}%")
print(f"(e) Overall efficiency, direct method: {overall_eff_direct:.4f} = {overall_eff_direct*100:.2f}%")
print(f"(f) Specific impulse: {Isp:.1f} s")
print(f"(g) Specific propellant consumption: {SPC:.5f} 1/s")