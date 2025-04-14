# Problem 1
# Orbital Period and Orbital Radius

## Motivation

Kepler's Third Law of planetary motion relates the **square of the orbital period** of a planet to the **cube of its orbital radius**. This fundamental law allows us to calculate planetary motions and offers insights into the **gravitational interactions** governing the motion of celestial bodies. By analyzing this relationship, we can explore various phenomena, from satellite orbits to the structure of entire planetary systems.

---

## 1. Theoretical Foundation

### Deriving Kepler’s Third Law for Circular Orbits

We begin with the gravitational force that provides the centripetal force required for circular motion. According to Newton’s Law of Gravitation:

\[
F_{\text{gravity}} = \frac{G M m}{r^2}
\]

Where:
- \( G \) is the gravitational constant (\(6.674 \times 10^{-11} \, \text{m}^3 \, \text{kg}^{-1} \, \text{s}^{-2}\))
- \( M \) is the mass of the central body (e.g., Sun, Earth)
- \( m \) is the mass of the orbiting body (e.g., a planet, satellite)
- \( r \) is the orbital radius (distance from the center of the central body)

For circular motion, the **centripetal force** is given by:

\[
F_{\text{centripetal}} = \frac{m v^2}{r}
\]

Where:
- \( v \) is the orbital velocity of the satellite or planet.

Setting the gravitational force equal to the centripetal force:

\[
\frac{G M m}{r^2} = \frac{m v^2}{r}
\]

Solving for \( v \), the orbital velocity:

\[
v = \sqrt{\frac{G M}{r}}
\]

Now, the orbital period \( T \) is the time it takes for the planet or satellite to complete one revolution. The distance traveled in one orbit is the circumference of the circle \( 2\pi r \), so the period is:

\[
T = \frac{\text{circumference}}{\text{velocity}} = \frac{2\pi r}{v}
\]

Substituting \( v \) from earlier:

\[
T = 2\pi \sqrt{\frac{r^3}{G M}}
\]

Squaring both sides gives us the relationship:

\[
T^2 = \frac{4\pi^2 r^3}{G M}
\]

This is **Kepler’s Third Law**, which states that the **square of the orbital period** \( T^2 \) is **proportional to the cube of the orbital radius** \( r^3 \). This law is essential for understanding the motion of planets, satellites, and other celestial objects.

---

## 2. Implications for Astronomy

### Calculating Planetary Masses and Distances

Kepler's Third Law is incredibly useful for determining the mass of a central body (such as the Sun or Earth) when the orbital period and radius are known. For example, by observing the Moon’s orbital period and radius, we can estimate the mass of the Earth. Similarly, by studying the orbits of distant exoplanets, astronomers can infer the mass of the stars they orbit.

### Example: The Moon’s Orbit

The Moon orbits Earth with an orbital radius of approximately \( 3.84 \times 10^8 \) meters and an orbital period of about 27.3 days. Using Kepler’s Third Law, we can estimate the mass of the Earth if the orbital data of the Moon is known.

---

## 3. Real-World Examples

### Planets in the Solar System

In the Solar System, all planets follow an orbital path around the Sun. By using Kepler’s Third Law, we can compare the orbital periods and radii of planets to calculate their relative distances from the Sun. For instance:
- Earth has an orbital period of 365.25 days and an orbital radius of 1 AU (astronomical unit).
- Jupiter, with a much longer orbital period of about 11.86 Earth years, orbits the Sun at a much greater distance, roughly 5.2 AU.

### Satellites and Artificial Orbits

In modern times, satellites orbiting Earth also obey Kepler's Third Law. Understanding this law helps in the design of satellite orbits for communication, GPS systems, and space stations.

---

## 4. Implementation (Python Simulation)

Below is a Python script that simulates a circular orbit and verifies Kepler’s Third Law. The program calculates the orbital period based on different orbital radii for a given central mass (e.g., mass of Earth).

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972 * 10**24   # Mass of Earth (kg)

# Orbital radii (in meters)
radii = np.linspace(1e7, 1e9, 100)

# Orbital period (T) based on Kepler's third law: T^2 = (4π^2 r^3) / (GM)
periods = 2 * np.pi * np.sqrt(radii**3 / (G * M))

# Plotting the relationship between T^2 and r^3
plt.figure(figsize=(8, 6))
plt.plot(radii**3, periods**2, label="T^2 vs r^3")
plt.xlabel("r^3 (m^3)")
plt.ylabel("T^2 (s^2)")
plt.title("Kepler's Third Law: T^2 vs r^3")
plt.grid(True)
plt.legend()
plt.show()
