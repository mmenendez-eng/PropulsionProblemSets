# PropulsionProblemSets

Worked problems from *Rocket Propulsion Elements* by Sutton (9th Edition).

This repository contains propulsion calculations, nozzle analysis, performance studies, and supporting engineering scripts written in Python.

---

## Tools Used

- NumPy
- SciPy
- Matplotlib

---

## Completed Problems

### Sutton Problem 3-1 — Specific Heat Relations from Gas Properties
Computes the specific heat at constant pressure and constant volume for combustion gases using:

- Specific heat ratio (k)
- Molecular mass (M)
- Perfect gas relations

Key results:
- Calculates cp and cv
- Demonstrates relation between k, cp, and cv
- Reinforces thermodynamic gas property fundamentals

---

### Sutton Problem 3-2 — Optimum Expansion Nozzle Performance
Analyzes ideal nozzle expansion performance under sea-level optimum expansion conditions.

Key results:
- Calculates exit velocity
- Determines exit temperature
- Evaluates pressure ratio effects on nozzle performance
- Reinforces isentropic flow relations in rocket nozzles

---

### Sutton Problem 3-3 — Enthalpy Change in Isentropic Nozzle Flow
Computes enthalpy change for a nozzle flow undergoing isentropic expansion.

Key results:
- Calculates enthalpy change from velocity increase
- Quantifies error introduced by neglecting inlet velocity
- Demonstrates validity of assuming negligible chamber velocity

---

### Sutton Problem 3-4 — Acoustic and Gas Velocity at Mach 2.73
Computes acoustic velocity and actual gas velocity for nitrogen flow at elevated temperature.

Key results:
- Calculates local speed of sound
- Determines gas velocity from Mach number
- Reinforces compressible flow and Mach relations

---

### Sutton Problem 3-9 — Nozzle Area Change and Performance Impact
Analyzes how a reduction in nozzle area affects rocket motor performance.

Key results:
- Evaluates changes in nozzle flow conditions
- Determines impact on thrust/performance behavior
- Reinforces the sensitivity of nozzle operation to geometric changes
- Connects area variation to compressible flow behavior

---

### Sutton Problem 3-12 — Supersonic Nozzle Design at Altitude
Designs a supersonic rocket nozzle for operation at altitude using specified chamber and ambient conditions.

Key results:
- Calculates nozzle exit pressure and exit Mach number
- Determines exit velocity and thrust performance
- Evaluates nozzle behavior for a specified area ratio
- Reinforces isentropic nozzle design and altitude operation

---

### Sutton Problem 3-13 — Thrust Variation with Altitude
Computes the A-4 rocket thrust at altitude using pressure thrust correction.

Key results:
- Separates momentum thrust from pressure thrust
- Calculates atmospheric pressure effect at 25 km
- Demonstrates why thrust increases as ambient pressure decreases

---

### Sutton Problem 3-15 — Non-Ideal Thrust and Discharge Corrections
Applies thrust and discharge correction factors to determine actual rocket performance.

Key results:
- Calculates actual thrust
- Determines actual exhaust velocity
- Computes actual specific impulse
- Finds velocity correction factor

---

### Sutton Problem 3-16 — Ideal Rocket Nozzle Performance
Analyzes an ideal rocket nozzle using chamber, exit, and gas property conditions.

Key results:
- Calculates critical pressure ratio
- Determines throat velocity
- Computes expansion area ratio
- Finds theoretical nozzle exit velocity

---

### Sutton Problem 3-17 — Characteristic Velocity and Rocket Performance
Uses characteristic velocity and thrust coefficient to compute ideal rocket performance.

Key results:
- Calculates effective exhaust velocity
- Determines thrust
- Computes chamber pressure
- Calculates specific impulse

---

### Sutton Problem 3-19 — Upper Stage Nozzle Performance at Sea Level
Compares ideal upper-stage nozzle thrust at design altitude and sea-level test conditions.

Key results:
- Calculates ideal thrust at design ambient pressure
- Calculates ideal thrust at sea level
- Quantifies thrust loss from increased back pressure
- Identifies sea-level overexpansion/back pressure as the likely nonideal behavior source

---

### Sutton Problem 3-21 — Rocket Performance Correction Factors
Determines correction factors from measured thrust and mass flow data for a non-ideal rocket system.

Key results:
- Calculates thrust correction factor
- Determines discharge correction factor
- Computes thrust coefficient efficiency
- Calculates actual specific impulse

---

### Sutton Problem 3-22 — Thrust Coefficient vs Expansion Ratio
Analyzes thrust coefficient behavior as a function of nozzle expansion ratio for:

- k = 1.3
- p1/p3 = 50

Key results:
- Identifies optimum expansion ratio
- Shows pressure thrust sign change at p2 = p3
- Visualizes momentum vs pressure thrust contributions

---

### Sutton Extra Problem 3A — MA-5A Engine Performance Parameters
Analyzes propulsion performance data for the MA-5A liquid rocket engine system.

Key results:
- Calculates propellant mass flow rates
- Determines nozzle expansion ratios
- Examines relationships between thrust, specific impulse, and characteristic velocity
- Highlights dimensional consistency considerations in English Engineering units

---

### Sutton Extra Problem 3B — Rocket Nozzle Design with Correction Factors
Designs a rocket nozzle using realistic non-ideal correction factors for thrust and exhaust velocity.

Key results:
- Calculates throat and exit areas
- Determines nozzle diameters and expansion ratio
- Computes actual exhaust velocity and specific impulse
- Compares ideal and non-ideal nozzle performance
- Reinforces practical nozzle design methodology
