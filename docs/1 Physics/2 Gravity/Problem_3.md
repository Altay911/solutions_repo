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
# SIMPLE KEPLER'S LAW CALCULATOR (JUST COPY ALL BELOW)
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# Earth data
EARTH_MASS = 5.972e24  # kg
EARTH_RADIUS = 6371000  # meters

# Function to calculate period
def get_orbit_time(altitude_km):
    radius = EARTH_RADIUS + altitude_km*1000
    return 2*np.pi*np.sqrt(radius**3/(G*EARTH_MASS))/3600

# Make the plot
altitudes = np.linspace(160, 35786, 100)  # From 160km to GEO
periods = [get_orbit_time(alt) for alt in altitudes]

plt.figure(figsize=(10,5))
plt.plot(altitudes, periods, 'b-')
plt.title("Orbit Time vs Altitude")
plt.xlabel("Altitude (km)")
plt.ylabel("Orbit Time (hours)")
plt.grid(True)
plt.show()

# Check some real values
print("\nReal orbit checks:")
print(f"ISS (400km): {get_orbit_time(400):.2f} hours")
print(f"GPS (20,200km): {get_orbit_time(20200):.2f} hours")
print(f"GEO (35,786km): {get_orbit_time(35786):.2f} hours")
print(f"Moon (384,400km): {get_orbit_time(384400):.2f} hours")