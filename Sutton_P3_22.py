""" SUTTON Problem 3-22
The reason optimum thrust coefficient (as shown on Figs. 3-6 and 3-7) exists is
that as the nozzle area ratio increases with fixed p1/p3 and k, 
the pressure thrust in Eq. 3-30 changes sign at p2 = p3. 

Using k = 1.3 and p1/p3 = 50, show that as p2/p1 drops with increasing 𝜖, 
the term 1.964[1-(p2/p1)**0.231]
0.5 increases more slowly than
the (negative) term [1/50-p2/p1] 𝜖 increases (after the peak, where 𝜖 ≈ 7). 
(Hint: use Eq. 3-25.)
"""

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

## GIVEN/CONSTANTS
k = 1.3     # Specific Heat Ratio
p1_p3 = 50  # Pc/Pamb, Controlling Pressure Ratio
p3_p1 = 1/p1_p3 # Pamb/Pc, Ambient to Chamber Pressure Ratio

def momentum_CF(k,pe_pc):
    return np.sqrt(
        (2 * k**2 / (k - 1))
        * (2 / (k + 1))**((k + 1) / (k - 1))
        * (1 - pe_pc**((k - 1) / k))
    )

def pressure_CF(pe_pc,pa_pc,eps):
    return (pe_pc - pa_pc) * eps

def calculate_exit_mach_number(area_ratio, k):
    """Calculate the exit Mach number using the area-Mach relation."""

    def area_mach_relation(M):
        return (1 / M) * (((2 / (k + 1)) * (1 + ((k - 1) / 2) * M**2))**((k + 1) / (2 * (k - 1)))) - area_ratio

    M_exit = fsolve(area_mach_relation, 3.0)[0]  # Initial guess for supersonic flow
    return M_exit

def pe_pc_from_mach(M, k):
    """Calculate the exit to chamber pressure ratio from Mach number using the isentropic flow relations."""
    return (1 + (k - 1) / 2 * M**2)**(-k / (k - 1)) # Returns Pe/Pc
## SOLUTION

ExpR = np.arange(1.0,15.5,0.25)

Me = np.array([calculate_exit_mach_number(eps,k) for eps in ExpR])
P2_P1 = np.array([pe_pc_from_mach(M,k) for M in Me])

CF_momentum = momentum_CF(k,P2_P1)
CF_pressure = pressure_CF(P2_P1,p3_p1,ExpR)
CF_total = CF_momentum + CF_pressure

print(" eps      Me        p2/p1      C_F,mom    C_F,press   C_F,total")
for eps, M, p, cfm, cfp, cft in zip(ExpR, Me, P2_P1, CF_momentum, CF_pressure, CF_total):
    print(f"{eps:5.2f}    {M:7.4f}   {p:8.5f}    {cfm:8.5f}   {cfp:9.5f}   {cft:9.5f}")

imax = np.argmax(CF_total)
sign_change_idx = np.argmin(np.abs(P2_P1 - p3_p1))

print(f"p2 = p3 occurs at ε ≈ {ExpR[sign_change_idx]:.2f}")
print("\nPeak thrust coefficient occurs near:")
print(f"Optimal Expansion Ratio = {ExpR[imax]:.2f}, C_F = {CF_total[imax]:.5f}")
print(f"\nFor a fixed chamber-to-ambient pressure p2/p3 = {p1_p3} and k = {k}, the thrust coefficient reaches a maximum at around Ae/At ~= {ExpR[imax]:.2f}. "\
        "\nAs the expansion ratio increases further, p2/p1 continues to decrease."\
        "\nThe momentum term continues to increase, but gradually." \
        "\nThe pressure term becomes negative once p2/p1 < p3/p1 = 1/50 , which occurs when nozzle exit pressure becomes less than ambient." \
        "\nBeyond the optimum point, the magnitude of the negative pressure term's contribution increases faster than than the momentum term increases."\
        "\nTherefore, the total thrust coefficient decreases with further increases in nozzle expansion ratio."\
        "\nThis is why an optimum expansion ratio exists.")

plt.figure()
plt.plot(ExpR, P2_P1)
sign_change_idx = np.argmin(np.abs(P2_P1 - p3_p1))

plt.axvline(
    x=ExpR[sign_change_idx],
    linestyle=':',
    color='r',
    label='p₂ = p₃ (pressure term = 0)'
)
plt.axhline(
    y=p3_p1,
    linestyle='--',
    color='k',
    label=f'p3/p1 = {p3_p1:.3f}'
)
plt.xlabel('Expansion Ratio (Ae/At)')
plt.ylabel('p2/p1')
plt.title('Exit Pressure Ratio vs Expansion Ratio')
plt.legend()
plt.grid()
plt.show()

plt.figure()

plt.plot(ExpR, CF_total, label='C_F total')
plt.plot(ExpR, CF_momentum, label='C_F momentum')
plt.plot(ExpR, CF_pressure, label='C_F pressure')

plt.axvline(x=ExpR[imax], linestyle='--', color='k', label=f'Optimum ε ≈ {ExpR[imax]:.2f}')
plt.plot(ExpR[imax], CF_total[imax], 'ko')  # black dot
plt.annotate(
    f'CF(max)\nε ≈ {ExpR[imax]:.2f}\nC_F ≈ {CF_total[imax]:.3f}',
    xy=(ExpR[imax], CF_total[imax]),
    xytext=(ExpR[imax] + 1, CF_total[imax] - .35),
    arrowprops=dict(arrowstyle='->')
)
plt.xlabel('Expansion Ratio (Ae/At)')
plt.ylabel('Thrust Coefficient')
plt.title('Thrust Coefficient Components vs Expansion Ratio')
plt.legend()
plt.grid()
plt.show()
