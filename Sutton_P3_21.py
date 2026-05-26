""" Sutton Problem 3.21
A rocket nozzle has been designed with At = 19.2 in.2 and A2 = 267 in.2 to operate optimally at p3 = 4 psia and produce 18,100 lbf of ideal thrust with a chamber pressure of
570 psia. It will use the proven design of a previously built combustion chamber that operates at T1 = 6000 ∘R with k = 1.25 and R = 68.75 ft-lbf∕lbm∘R, with a c∗-efficiency of
95%. But test measurements on this thrust system, at the stated pressure conditions, yield
a thrust of only 16,300 lbf when the measured flow rate is 2.02 lbm/sec. Find the applicable correction factors (𝜁F, 𝜁d, 𝜁CF ) and the actual specific impulse assuming frozen flow
throughout.
"""
import numpy as np

## GIVEN/CONSTANTS
At = 19     # 
Pc = 570   # Chamber Pressure, psia
Pa = 4      # Ambient Pressure, psia
k = 1.25    # Specific Heat Ratio
Tc = 6000    # Chamber Temperature, deg. R
R = 68.75   # Specific Gas Constant, ft.lbf/lbm.R
cstar_eff = 0.95    # C-star Efficiency
g0 = 32.2   # ft/s^2
Fi = 18100  # Ideal Thrust, lbf
Fa = 16300  # Actual Thrust, lbf
mdota = 2.02 # Mass Flow Rate, lbm/s

## FUNCTIONS
def exhaust_velocity(k,R,T1, pe_pc): # [EQ.3-16]
    'Need to revise for US units'
    return np.sqrt(2*g0*k*R*T1/(k-1)*(1-pe_pc**((k-1)/k))) # m/s

## SOLUTION

# a) Thrust Correction Factor
corrF = Fa/Fi

# b) Discharge Correction Factor
c = exhaust_velocity(k,R,Tc,Pa/Pc)
mdoti = Fi/c
corrD = mdota/mdoti

# c) CF Efficiency
corrCF = corrF/(corrD*cstar_eff)

# d) Actual Specific Impulse
corrv = corrF/corrD
Isp_i = Fi/(mdoti*g0)
Isp_a = corrv*Isp_i
## OUTPUT
print(f'Thrust Corrector Factor = {corrF}')
print(f'Dicharge Correction Factor = {corrD}')
print(f'CF Efficiency = {corrCF}')
print(f'Actual Specific Impulse = {Isp_a} s')