"""
Sutton Problem 3-9

Compute new exhaust velocity when exit area is reduced by 50% (nozzle cut off).
Report percent change in thrust and jet kinetic energy relative to the original nozzle.

Assumptions:
- Isentropic nozzle expansion
- Original nozzle is "optimally expanded": Pe_old = P_amb
- Choked throat; cutting Ae changes Ae/At, not At
"""

import numpy as np


## GIVEN
P_c = 2.068e6       # Pa, Chamber Pressure
T_c = 2222.0        # K, Chamber Temperature
mdot = 1.0          # kg/s, Mass Flow Rate
k = 1.30            # Specific Heat Ratio
R = 345.7           # J/(kg*K), Specific Gas Constant
g = 9.81            # m/s^2
P_a = 101.325e3     # Pa, Ambient Pressure


## FUNCTIONS
def area_ratio(M):
    """A/At as a function of Mach number (isentropic)."""
    term = (2/(k+1)) * (1 + (k-1)/2 * M**2)
    expo = (k+1) / (2*(k-1))
    return (1/M) * term**expo

def P_ratio(M):
    """P/Pc as a function of Mach number (isentropic)."""
    return (1 + (k-1)/2 * M**2) ** (-k/(k-1))

def v_from_Pe(Pe):
    """Exit velocity from Pc->Pe (isentropic)."""
    return np.sqrt(2*k/(k-1) * R*T_c * (1 - (Pe/P_c)**((k-1)/k)))


def bisect(f, lo, hi, target, iters=200, tol=1e-10):
    """Solve f(x)=target on [lo,hi] with bisection (assumes monotonic and bracketed)."""
    flo = f(lo) - target
    fhi = f(hi) - target
    if flo * fhi > 0:
        raise ValueError("Root not bracketed; adjust lo/hi.")

    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        fmid = f(mid) - target
        if abs(hi - lo) < tol:
            return mid
        if flo * fmid <= 0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    return 0.5 * (lo + hi)

## ANALYIS

# 1) OLD NOZZLE (optimal): Pe_old = Pamb
# Solve for Me_old from pressure ratio, then get Ae/At_old
Me_old = bisect(P_ratio, lo=1e-8, hi=50.0, target=P_a/P_c)   # unique solution for pressure ratio
AeAt_old = area_ratio(Me_old)
Pe_old = P_a
ve_old = v_from_Pe(Pe_old)

# Thrust: pressure term is zero by definition of optimal expansion
F_old = mdot * ve_old
KE_old = 0.5 * mdot * ve_old**2

# 2) NEW NOZZLE: Ae halved => (Ae/At) halved
# Solve for Me_new from Ae/At (supersonic branch), then compute Pe_new, ve_new, thrust
AeAt_new = 0.5 * AeAt_old

# For Ae/At > 1 there are two roots; we want the Supersonic branch => bracket [1, 50]
Me_new = bisect(area_ratio, lo=1.0 + 1e-8, hi=50.0, target=AeAt_new)

Pe_new = P_c * P_ratio(Me_new)
ve_new = v_from_Pe(Pe_new)

# Need Ae_new for pressure thrust. We can get At from mdot relation (choked).
mass_flux = P_c * np.sqrt(k/(R*T_c)) * (2/(k+1)) ** ((k+1)/(2*(k-1)))
At = mdot / mass_flux
Ae_new = AeAt_new * At

F_new = mdot * ve_new + (Pe_new - P_a) * Ae_new
KE_new = 0.5 * mdot * ve_new**2

# Percent Changes
F_change_pct = (F_new - F_old) / F_old * 100
KE_change_pct = (KE_new - KE_old) / KE_old * 100

## OUTPUT
print('SUTTON PROBLEM 3.9 RESULTS')
print(f"Old: Me={Me_old:.6f}, Ae/At={AeAt_old:.6f}, Pe={Pe_old:.3e} Pa, ve={ve_old:.3f} m/s, F={F_old:.3f} N, KE={KE_old:.3f}")
print(f"New: Me={Me_new:.6f}, Ae/At={AeAt_new:.6f}, Pe={Pe_new:.3e} Pa, ve={ve_new:.3f} m/s, F={F_new:.3f} N, KE={KE_new:.3f}")
print(f"\nPercent change in thrust: {F_change_pct:.3f} %")
print(f"Percent change in kinetic energy: {KE_change_pct:.3f} %")