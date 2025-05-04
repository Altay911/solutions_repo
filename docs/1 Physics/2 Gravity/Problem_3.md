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
# Kepler's Third Law Explained

## The Fundamental Equation
For circular orbits, gravity provides the centripetal force:

\[
\frac{GMm}{r^2} = \frac{mv^2}{r}
\]

Where:
- \( G \) = 6.674×10⁻¹¹ N(m/kg)² (gravitational constant)
- \( M \) = mass of central body (kg)
- \( m \) = mass of orbiting body (kg)
- \( r \) = orbital radius (m)
- \( v \) = orbital velocity (m/s)

## Deriving the Law
1. Relate velocity to period:
   \[
   v = \frac{2\pi r}{T}
   \]
2. Substitute into the force equation:
   \[
   \frac{GM}{r^2} = \frac{4\pi^2 r}{T^2}
   \]
3. Rearrange to get Kepler's Third Law:
   \[
   T^2 = \frac{4\pi^2}{GM}r^3
   \]

## Live Python Calculator
```python
import numpy as np

G = 6.674e-11  # Gravitational constant

def orbital_period(M, r):
    """Calculate orbital period in seconds"""
    return 2 * np.pi * np.sqrt(r**3 / (G * M))

# Example: Earth's orbit around Sun
sun_mass = 1.989e30  # kg
earth_orbit_radius = 149.6e9  # meters

period = orbital_period(sun_mass, earth_orbit_radius)
print(f"Earth's orbital period: {period/86400:.2f} days")