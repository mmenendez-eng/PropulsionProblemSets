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
AreaRatio = 2.3 # Ae/At, Nozzle Expansion Ratio
At = 5          # in^2, Nozzle Throat Area
k = 1.30        # Specific Heat Ratio
R_specific = 66 # ft-lbf/lbm*R, Specific Gas Constant
Pc = np.asarray([300,200,100])        # psia, Chamber Pressure
Tc = 5300       # deg. R, Chamber Temperature
Pa = 10        # psia, Atmospheric Temperature
g0 = 32.2

## FUNCTIONS
def exhaust_velocity(k,Tc,R,P1,P2,g):
    """Calculates exhaust velocity based on pressure ratio and chamber conditions"""
    return np.sqrt(2*k/(k-1)*R*Tc*g*(1-(P2/P1)**((k-1)/k)))

def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.0)[0]  # Initial guess for supersonic flow
    return M_exit


## ANALYSIS
# Pressure Ratio between Chamber and Atmosphere
PressRatio = Pc/Pa

# Exit Conditions
Me = calculate_exit_mach_number(AreaRatio, k) # Exit Mach No.
Pe = Pc/((1+0.5*(k-1)*Me**2)**(k/(k-1)))      # Exit Pressure, Pa
T_exit = Tc*(Pe/Pc)**((k-1)/k)                # Exit Temperature, deg R

# Ideal Exhaust Velocity for:
# - Optimum Area Ratio
v_exit_opt = exhaust_velocity(k,Tc,R_specific,Pc,Pa,g0) # ft/s

# - Actual Area Ratio
v_exit_actual = exhaust_velocity(k,Tc,R_specific,Pc,Pe,g0) # ft/s

# Propellant Flow
mdot = At*Pc*k*g0/np.sqrt(k*R_specific*Tc*g0)*np.sqrt((2/(k+1))**((k+1)/(k-1))) # kg/s

# Effective Exhaust Velocity
Ae = AreaRatio*At                       # in^2, Nozzle Exit Area
c = v_exit_actual + g0*(Pe-Pa)*Ae/mdot  # ft/s

# Thrust
F_thrust = mdot*c/g0    # N
# Specific Impulse
Isp = c/g0              # s

## OUTPUT
headers = (
    "Pc (psia)",
    "Pc/Pa",
    "c (ft/s)",
    "v_opt (ft/s)",
    "v_actual (ft/s)",
    "mdot (lbm/s)",
    "F (lbf)",
    "Isp (s)",
    "Pe (psia)",
    "Te (R)"
)

print("\nRESULTS")
print("-" * 118)
print(f"{headers[0]:>10} {headers[1]:>8} {headers[2]:>12} {headers[3]:>14} "
      f"{headers[4]:>16} {headers[5]:>14} {headers[6]:>10} "
      f"{headers[7]:>10} {headers[8]:>10} {headers[9]:>10}")
print("-" * 118)

for i in range(len(Pc)):
    print(f"{Pc[i]:10.0f} {PressRatio[i]:8.1f} {c[i]:12.0f} {v_exit_opt[i]:14.0f} "
          f"{v_exit_actual[i]:16.0f} {mdot[i]:14.2f} {F_thrust[i]:10.0f} "
          f"{Isp[i]:10.1f} {Pe[i]:10.1f} {T_exit[i]:10.0f}")
    

plt.figure()
plt.plot(Pc, PressRatio, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Pressure Ratio, Pc/Pa")
plt.title("Pressure Ratio vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, c, marker="o", label="Effective Exhaust Velocity")
plt.plot(Pc, v_exit_opt, marker="o", label="Ideal Velocity - Optimum")
plt.plot(Pc, v_exit_actual, marker="o", label="Ideal Velocity - Actual Area Ratio")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Velocity (ft/s)")
plt.title("Exhaust Velocity vs Chamber Pressure")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, mdot, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Propellant Flow Rate (lbm/s)")
plt.title("Propellant Flow Rate vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, F_thrust, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Thrust (lbf)")
plt.title("Thrust vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, Isp, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Specific Impulse (s)")
plt.title("Specific Impulse vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, Pe, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Exit Pressure, Pe (psia)")
plt.title("Exit Pressure vs Chamber Pressure")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(Pc, T_exit, marker="o")
plt.xlabel("Chamber Pressure, Pc (psia)")
plt.ylabel("Exit Temperature (R)")
plt.title("Exit Temperature vs Chamber Pressure")
plt.grid(True)
plt.show()