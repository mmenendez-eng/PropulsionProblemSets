""" Problem 3-9
For the rocket propulsion unit given in Example 3-2 
compute the new exhaust velocity
if the nozzle is cut off, decreasing the exit area by 50%. 
Estimate the losses in 
kinetic energy and 
thrust and 
express them as a percentage of the original kinetic energy and the
original thrust.
"""
## IMPORT
import numpy as np

## GIVEN
P_c = 2.068e6           # Pa
T_c = 2222              # K
mdot = 1.0              # kg/s
k = 1.30
R = 345.7               # J/kg.K
g = 9.81                # m/s^2
P_amb = 101.325e3       # Pascals

## SOLUTION

# Functions
def v_exit(k,R,T_c,P_c,P_exit):                 # Exhaust Velocity (m/s)
    v_exit = np.sqrt(2*k/(k-1)*R*T_c*(1-(P_exit/P_c)**((k-1)/k)))
    return v_exit

def V_exit(k,V_c,P_c,P_y):                      # Exit Specific Volume (m^3/kg)
    V_exit = V_c*(P_c/P_y)**(1/k)
    return V_exit

def T_exit(k,T_c,P_c,P_y):
    T_exit = T_c*(P_y/P_c)**((k-1)/k)           # Exit Temp.    (Kelvin)
    return T_exit

def A_exit(mdot,V_y,v_y):                       # Exit Area     (m^2)
    A_exit = mdot*V_y/v_y
    return A_exit

def M_exit(v_exit,k,R,T_exit):                  # Exit Mach No.
    M_exit = v_exit/np.sqrt(k*R*T_exit)
    return M_exit

# Analysis
# Nozzle Exit Area is 50% of optimal expansion -> expansion ratio is 50% of original
# P2 =/= P3
c = v_exit(k,R,T_c,P_c,P_amb)
Isp = F/(mdot*g)
PR = P_amb/P_c
V_c = R*T_c/P_c
P_y = np.linspace(P_c,P_amb)        
v_y = v_exit(k,R,T_c,P_c,P_y)
V_y = V_exit(k,V_c,P_c,P_y)
T_y = T_exit(k,T_c,P_c,P_y)
A_y = A_exit(mdot,V_y,v_y)
A_out = A_y[-1]
F_old = mdot*c+ (P_amb - P_amb)*A_out
A_new = A_out/2                             # Area nozzle approx 50%



T_t = 2*T_c/(k+1)
V_t = V_c*((k+1)/2)**(1/(k-1))              # correct
v_t = np.sqrt(T_t*R*k)
A_t = mdot*V_t/v_t
ExpR = A_new/A_t
print('Expansion Ratio =',ExpR)
PR_new = 5.5573                             # Per Anderson Appendix 1 Table 1.
P_exit = P_c/PR_new

v_2 = v_exit(k,R,T_c,P_c,P_exit)
V_2 = V_exit(k,V_c,P_c,P_exit)
T_2 = T_exit(k,T_c,P_c,P_exit)
A_2 = A_exit(mdot,V_2,v_2)

F_new = mdot*v_2 + (P_exit - P_amb)*A_new
KE_new = 0.5*mdot*(v_2**2)
KE_old = 0.5*mdot*(c**2)
print('Exhaust Velocity =',c)
print('Exhaust Velocity New =', v_2)
print('Thrust = ',F)
print('Thrust(new) = ',F_new)
print('Kinetic Energy Old',KE_old)
print('Kinetic Energy New',KE_new)

F_change = (F_new-F)/F*100
KE_change = (KE_new-KE_old)/KE_old*100

print('Percent Change in Thrust =',F_change)
print('Percent Change in Kinetic Energy =',KE_change)

## NOTES
'''
Values can be more accurate with an analytical method of obtaining the Pressure Ratio (as well as the Expansion Ratio, Nozzle Exit Area)
'''
