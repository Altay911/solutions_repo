# Gravity 1: Kepler's Third Law and Orbital Mechanics

## Problem 1: Orbital Period and Orbital Radius

### 1. Derivation of Kepler's Third Law for Circular Orbits

For a celestial body of mass \( m \) orbiting a much larger mass \( M \) (e.g., a planet around the Sun) in a circular orbit of radius \( r \), the gravitational force provides the centripetal force:

\[
\frac{GMm}{r^2} = \frac{mv^2}{r}
\]

Where:
- \( G \) is the gravitational constant,
- \( v \) is the orbital velocity.

The orbital velocity can be expressed in terms of the orbital period \( T \):

\[
v = \frac{2\pi r}{T}
\]

Substituting \( v \) into the force balance equation:

\[
\frac{GMm}{r^2} = \frac{m(2\pi r / T)^2}{r}
\]

Simplifying:

\[
\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}
\]

Rearranging to isolate \( T^2 \):

\[
T^2 = \frac{4\pi^2 r^3}{GM}
\]

This is Kepler's Third Law for circular orbits, showing that \( T^2 \propto r^3 \).

---

### 2. Implications for Astronomy

Kepler's Third Law is pivotal in astronomy for:
- **Calculating Planetary Masses:** By observing \( T \) and \( r \) for a moon orbiting a planet, we can solve for the planet's mass \( M \).
- **Determining Distances:** The law helps estimate the semi-major axis of exoplanets or binary star systems when \( T \) is known.
- **Understanding Dynamics:** It underpins models of galactic rotation curves and dark matter distributions.

---

### 3. Real-World Examples

- **Moon-Earth System:**  
  The Moon's orbital period (\( T \approx 27.3 \) days) and average distance (\( r \approx 384,400 \) km) align with Kepler's law when Earth's mass is plugged in.

- **Solar System Planets:**  
  For Earth, \( T^2 \approx 1 \) year\(^2\) and \( r^3 \approx 1 \) AU\(^3\), confirming the proportionality. Data for other planets (e.g., Mars, Jupiter) similarly fit.

---

### 4. Computational Model (Python Implementation)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# Constants (SI units)
M_sun = 1.989e30  # Mass of the Sun

def orbital_period(r, M=M_sun):
    """Calculate orbital period for circular orbit."""
    return np.sqrt(4 * np.pi**2 * r**3 / (G * M))

# Example: Earth's orbit (r = 1 AU in meters)
r_earth = 1.496e11  
T_earth = orbital_period(r_earth)
print(f"Earth's orbital period: {T_earth / (60*60*24):.2f} days")

# Plot T^2 vs. r^3 for varying radii
radii = np.linspace(1e10, 5e11, 100)  # 0.1 AU to 5 AU
periods = orbital_period(radii)
plt.figure(figsize=(8, 5))
plt.plot(radii**3, periods**2, 'b-')
plt.xlabel('Orbital Radius Cubed (r³) [m³]')
plt.ylabel('Orbital Period Squared (T²) [s²]')
plt.title("Kepler's Third Law: T² ∝ r³")
plt.grid(True)
plt.show()