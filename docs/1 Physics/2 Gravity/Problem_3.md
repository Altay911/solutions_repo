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
# Kepler's Third Law Computational Model
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

def orbital_period(radius, central_mass):
    """Calculate orbital period for circular orbit using Kepler's Third Law"""
    return 2 * np.pi * np.sqrt(radius**3 / (G * central_mass))

# Constants for Earth
EARTH_MASS = 5.972e24  # kg
EARTH_RADIUS = 6.371e6  # meters

# Create range of orbital radii (from 160km to GEO)
altitudes = np.linspace(160e3, 42164e3 - EARTH_RADIUS, 100)  # in meters
radii = EARTH_RADIUS + altitudes  # actual orbital radii

# Calculate periods in seconds then convert to hours
periods_seconds = orbital_period(radii, EARTH_MASS)
periods_hours = periods_seconds / 3600

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(radii/1000, periods_hours, 'b-', linewidth=2)
plt.title("Orbital Period vs. Radius (Kepler's Third Law)", fontsize=14)
plt.xlabel('Orbital Radius (km)', fontsize=12)
plt.ylabel('Orbital Period (hours)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.tight_layout()

# Add some reference points
plt.plot(radii[0]/1000, periods_hours[0], 'ro', label='LEO (160km)')
plt.plot(radii[-1]/1000, periods_hours[-1], 'go', label='GEO (35,786km)')
plt.legend()

plt.show()

# Verification with known values
def print_verification(altitude_km):
    r = EARTH_RADIUS + altitude_km * 1000
    T = orbital_period(r, EARTH_MASS)/3600
    print(f"Altitude {altitude_km} km: Period = {T:.2f} hours")

print("\nVerification:")
print_verification(400)  # ISS orbit
print_verification(35786)  # GEO
print_verification(384400)  # Moon orbit (~27.3 days expected)