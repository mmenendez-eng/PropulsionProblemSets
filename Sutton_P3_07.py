print(""" SUTTON PROBLEM 3-7
      A certain ideal rocket with: 
    - nozzle area ratio of 2.3 and 
    - throat area of 5 in^2 
    delivers gases at 
    - k = 1.30
    - R = 66ft-lbf/lbm-∘R 
    - chamber pressure of 300 psia and a constant
    - chamber temperature of 5300 ∘R against 
    - back atmospheric pressure of 10 psia.

    By means of an appropriate valve arrangement, it is possible to throttle the propellant flow
to the thrust chamber. 

Calculate and plot against pressure the following quantities for 
      300, 200, and 100 psia chamber pressure: 
      (a) pressure ratio between chamber and atmosphere;
      (b) effective exhaust velocity for area ratio involved; 
      (c) ideal exhaust velocity for optimum and actual area ratio; 
      (d) propellant flow; 
      (e) thrust; 
      (f) specific impulse; 
      (g) exit pressure; 
      (h) exit temperature.
""")

## IMPORT
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
## GIVEN/CONSTANTS
eps = 2.3       # Ae/At, Nozzle Expansion Ratio
A_t = 5         # in^2, Nozzle Throat Area
k = 1.30        # Specific Heat Ratio
R = 66          # ft-lbf/lbm*R, Specific Gas Constant
P_c = np.asarray([300,200,100])        # psia, Chamber Pressure
T_c = 5300       # deg. R, Chamber Temperature
P_a = 10        # psia, Atmospheric Pressure
g = 32.2

## FUNCTIONS, NOTE: Uses EE units
def exhaust_velocity(k, R, T_c, pe_pc, g):
    """Return ideal isentropic exhaust velocity in ft/s, Eq. 3-16 style."""
    return np.sqrt((2 * k / (k - 1)) * R * T_c * g * (1 - pe_pc ** ((k - 1) / k)))

def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.0)[0]  # Initial guess for supersonic flow
    return M_exit


## ANALYSIS
# Controlling Pressure Ratio between Chamber and Atmosphere
PressRatio = P_c/P_a

# Exit Conditions
M_e = calculate_exit_mach_number(eps, k) # Exit Mach No.
P_e = P_c / ((1 + (k - 1) / 2 * M_e**2)**(k / (k - 1)))      # Exit Pressure, psia
T_e = T_c * (P_e / P_c)**((k - 1) / k)                # Exit Temperature, deg R

# Ideal Exhaust Velocity for:
# - Optimum Area Ratio
v_e_opt = exhaust_velocity(k, R, T_c, P_a / P_c, g) # ft/s

# - Actual Area Ratio
v_e_actual = exhaust_velocity(k, R, T_c, P_e / P_c, g) # ft/s

# Propellant Flow
mdot = A_t * P_c * k * g / np.sqrt(k * R * T_c * g) * np.sqrt((2 / (k + 1))**((k + 1)/(k - 1))) # lbm/s

# Effective Exhaust Velocity
A_e = eps * A_t                       # in^2, Nozzle Exit Area
c = v_e_actual + g * (P_e - P_a) * A_e / mdot  # ft/s

# Thrust
F = mdot * c / g    # lbf
# Specific Impulse
I_sp = c / g              # s

## OUTPUT
headers = (
    "P_c (psia)",
    "P_c/P_a",
    "c (ft/s)",
    "v_opt (ft/s)",
    "v_actual (ft/s)",
    "mdot (lbm/s)",
    "F (lbf)",
    "I_sp (s)",
    "P_e (psia)",
    "T_e (R)"
)

print("\nRESULTS")
print("-" * 118)
print(f"{headers[0]:>10} {headers[1]:>8} {headers[2]:>12} {headers[3]:>14} "
      f"{headers[4]:>16} {headers[5]:>14} {headers[6]:>10} "
      f"{headers[7]:>10} {headers[8]:>10} {headers[9]:>10}")
print("-" * 118)

for i in range(len(P_c)):
    print(f"{P_c[i]:10.0f} {PressRatio[i]:8.1f} {c[i]:12.0f} {v_e_opt[i]:14.0f} "
          f"{v_e_actual[i]:16.0f} {mdot[i]:14.2f} {F[i]:10.0f} "
          f"{I_sp[i]:10.1f} {P_e[i]:10.1f} {T_e[i]:10.0f}")
    

plt.figure()
plt.plot(P_c, PressRatio, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Pressure Ratio, Pc/Pa")
plt.title("Pressure Ratio vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, c, marker="o", label="Effective Exhaust Velocity")
plt.plot(P_c, v_e_opt, marker="o", label="Ideal Velocity - Optimum")
plt.plot(P_c, v_e_actual, marker="o", label="Ideal Velocity - Actual Area Ratio")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Velocity (ft/s)")
plt.title("Exhaust Velocity vs Chamber Pressure")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, mdot, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Propellant Flow Rate (lbm/s)")
plt.title("Propellant Flow Rate vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, F, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Thrust (lbf)")
plt.title("Thrust vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, I_sp, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Specific Impulse (s)")
plt.title("Specific Impulse vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, P_e, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Exit Pressure, Pe (psia)")
plt.title("Exit Pressure vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(P_c, T_e, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Exit Temperature (R)")
plt.title("Exit Temperature vs Chamber Pressure")
plt.grid(True)
plt.show()