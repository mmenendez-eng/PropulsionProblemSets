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
## IMPORT
import numpy as np

## GIVEN / CONSTANTS
mdot = 3.7                      # kg/s, Mass Flow Rate
P_c = 2.1                       # MPa, Chamber Pressure
T_c = 2585.0                    # K, Chamber Temperature
M_mol = 18.0                    # kg/kg-mol, Molecular Mass
k = 1.30                        # Specific Heat Ratio
R_u = 8314.3                    # J/kg.K, Universal Gas Constant
P_a = .101325                   # MPa, Ambient Pressure

## FUNCTIONS
def exhaust_velocity(k: float, R: float, T_c: float, pe_pc: float) -> float:
    """Return ideal isentropic exhaust velocity [Eq. 3-16]"""
    return np.sqrt((2.0 * k / (k - 1.0)) * R * T_c * (1.0 - pe_pc ** ((k - 1.0) / k)))

def temperature_from_pressure_ratio(T_c: float, pe_pc: float, k: float) -> float:
    """Return exit static temperature from chamber temperature and p_e/p_c."""
    return T_c * pe_pc ** ((k - 1.0) / k)

def thrust_coefficient(k: float, pe_pc: float, pa_pc: float, area_ratio: float) -> float:
    """Return ideal thrust coefficient C_F.

    Uses the usual momentum term plus the pressure thrust term:
        C_F = momentum + (p_e/p_c - p_a/p_c) * A_e/A_t
    """
    momentum = np.sqrt(
        (2.0 * k**2 / (k - 1.0))
        * (2.0 / (k + 1.0)) ** ((k + 1.0) / (k - 1.0))
        * (1.0 - pe_pc ** ((k - 1.0) / k))
    )
    pressure = (pe_pc - pa_pc) * area_ratio
    return momentum + pressure

## ANALYSIS

# Exit Pressure = Ambient Pressure at Optimum Expansion
Pe_Pc = P_a/P_c

# Calculate Exit Conditions
v_e = exhaust_velocity(k, R_u, T_c, Pe_Pc)              # m/s
T_e = temperature_from_pressure_ratio(T_c, Pe_Pc, k)    # Kelvin

# Calculate Thrust Coefficient
CF = thrust_coefficient(k,Pe_Pc,Pe_Pc,1)

## OUTPUT
print('SUTTON PROBLEM 3-2 RESULTS:')
print(f'Controlling Pressure Ratio (Pc/Pe)  = {1/Pe_Pc:.2f}')
print(f'Exit Velocity                       = {v_e:.2f} m/s')
print(f'Exit Temperature                    = {T_e:.2f} Kelvin')
print(f'Thrust Coefficient                  = {CF:.2f}')
