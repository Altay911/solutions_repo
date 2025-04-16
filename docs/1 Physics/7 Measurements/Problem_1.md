# Measuring Earth's Gravitational Acceleration with a Pendulum

## Motivation
The acceleration due to gravity, \( g \), is a fundamental constant that influences a wide range of physical phenomena. Measuring \( g \) accurately is crucial for understanding gravitational interactions, designing structures, and conducting experiments in various fields. One classic method for determining \( g \) is through the oscillations of a simple pendulum, where the period of oscillation depends on the local gravitational field.

## Task
Measure the acceleration \( g \) due to gravity using a pendulum and analyze the uncertainties in the measurements in detail. This exercise emphasizes rigorous measurement practices, uncertainty analysis, and their role in experimental physics.

## Procedure

### 1. Materials:
- A string (1 or 1.5 meters long)
- A small weight (e.g., bag of coins, bag of sugar, key chain) mounted on the string
- Stopwatch (or smartphone timer)
- Ruler or measuring tape

### 2. Setup:
- Attach the weight to the string and fix the other end to a sturdy support.
- Measure the length of the pendulum, \( L \), from the suspension point to the center of the weight using a ruler or measuring tape. Record the resolution of the measuring tool and calculate the uncertainty as half the resolution.

### 3. Data Collection:
- Displace the pendulum slightly (<15°) and release it.
- Measure the time for 10 full oscillations (\( T_{10} \)) and repeat this process 10 times. Record all 10 measurements.
- Calculate the mean time for 10 oscillations (\( \bar{T_{10}} \)) and the standard deviation (\( \sigma_{T_{10}} \)).
- Determine the uncertainty in the mean time as:
  \[
  \Delta T = \frac{\sigma_{T_{10}}}{\sqrt{10}}
  \]

### Calculations:
#### 1. Calculate the period:
\[
T = \frac{\bar{T_{10}}}{10}
\]
where \( T \) is the period of one oscillation.

#### 2. Determine \( g \):
Use the following formula for the period of a simple pendulum:
\[
T = 2\pi \sqrt{\frac{L}{g}}
\]
Rearrange to solve for \( g \):
\[
g = \frac{4\pi^2 L}{T^2}
\]

#### 3. Propagate uncertainties:
The uncertainty in \( g \) can be propagated using the formula:
\[
\Delta g = \left( \frac{4\pi^2}{T^4} \right) \sqrt{ \left( \Delta L \right)^2 + \left( \frac{2L}{T^2} \Delta T \right)^2 }
\]

## Analysis:

### 1. Compare your measured \( g \) with the standard value (\( g_{std} = 9.81 \, \text{m/s}^2 \)).

### 2. Discuss:
- The effect of measurement resolution on \( g \).
- Variability in timing and its impact on \( g \).
- Any assumptions or experimental limitations.

## Deliverables:
1. **Tabulated data in markdown**:
   - \( L \), \( T_{10} \) measurements, \( \bar{T_{10}} \), \( \Delta T \), \( g \).
   - Calculated \( g \) and its uncertainty \( \Delta g \).

2. **The discussion** on sources of uncertainty and their impact on the results.
