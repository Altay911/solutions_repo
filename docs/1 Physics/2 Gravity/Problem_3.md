# Kepler's Third Law: Orbital Period and Radius Relationship

## 1. Derivation of the Relationship

For a circular orbit, the centripetal force is provided by gravity:

\[
\frac{GMm}{r^2} = \frac{mv^2}{r}
\]

Where:
- \( G \) = gravitational constant
- \( M \) = mass of central body
- \( m \) = mass of orbiting body
- \( r \) = orbital radius
- \( v \) = orbital velocity

The orbital period \( T \) is related to velocity by:

\[
v = \frac{2\pi r}{T}
\]

Substituting and simplifying:

\[
\frac{GM}{r^2} = \frac{(2\pi r/T)^2}{r}
\]

\[
\frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}
\]

Rearranging gives Kepler's Third Law:

\[
T^2 = \frac{4\pi^2}{GM} r^3
\]

Thus, the square of the orbital period is proportional to the cube of the orbital radius.

## 2. Astronomical Implications

This relationship has profound implications:
- **Mass determination**: By measuring \( T \) and \( r \) of orbiting bodies, we can calculate the mass of the central object
- **Distance scaling**: Allows calculation of relative distances in planetary systems
- **Exoplanet studies**: Used to characterize planets around other stars
- **Satellite operations**: Essential for placing satellites in correct orbits

## 3. Real-World Examples

### Earth-Moon System:
- Orbital radius: 384,400 km
- Orbital period: 27.3 days
- Using Kepler's Law, we can verify these values are consistent

### Solar System Planets:
The following table shows how \( T^2 \) is proportional to \( r^3 \):

| Planet | Orbital Radius (AU) | Orbital Period (years) | \( r^3 \) | \( T^2 \) |
|--------|---------------------|------------------------|----------|----------|
| Mercury| 0.39                | 0.24                   | 0.059    | 0.058    |
| Venus  | 0.72                | 0.62                   | 0.373    | 0.384    |
| Earth  | 1.00                | 1.00                   | 1.000    | 1.000    |
| Mars   | 1.52                | 1.88                   | 3.512    | 3.534    |

## 4. Computational Model

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

def calculate_period(r, M):
    """Calculate orbital period for circular orbit"""
    return np.sqrt(4 * np.pi**2 * r**3 / (G * M))

# Earth parameters
M_earth = 5.972e24  # kg
earth_radius = 6.371e6  # m

# Generate orbital radii from LEO to GEO
radii = np.linspace(earth_radius + 160e3, 42164e3, 100)  # 160km to GEO

# Calculate periods
periods = calculate_period(radii, M_earth)

# Convert to hours for better readability
periods_hours = periods / 3600

# Plot
plt.figure(figsize=(10, 6))
plt.plot(radii/1000, periods_hours)
plt.title("Kepler's Third Law Verification")
plt.xlabel('Orbital Radius (km)')
plt.ylabel('Orbital Period (hours)')
plt.grid(True)
plt.show()

# Verify with known values
leo_radius = earth_radius + 400e3  # 400km altitude
geo_radius = 42164e3  # GEO altitude

leo_period = calculate_period(leo_radius, M_earth)/3600
geo_period = calculate_period(geo_radius, M_earth)/3600

print(f"LEO (400km) period: {leo_period:.2f} hours")
print(f"GEO period: {geo_period:.2f} hours (should be 24 hours)")