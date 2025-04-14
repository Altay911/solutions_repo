# Problem 2
# Escape Velocities and Cosmic Velocities

## Motivation

The concept of **escape velocity** is fundamental in understanding the conditions required to escape a celestial body's gravitational pull. Extending this concept, the **first, second, and third cosmic velocities** define the velocities required for different types of space missions:
- **First cosmic velocity**: The velocity needed to stay in orbit around a celestial body.
- **Second cosmic velocity**: The velocity needed to escape the gravitational influence of a celestial body.
- **Third cosmic velocity**: The velocity required to escape the gravitational influence of a star, enabling travel to another star system.

These velocities are pivotal in space exploration, from launching satellites to planning interplanetary and interstellar missions.

---

## 1. Theoretical Foundation

### Escape Velocity

The **escape velocity** is the minimum velocity an object must have to break free from the gravitational influence of a celestial body without further propulsion. The formula for escape velocity \( v_e \) is derived from the conservation of energy, considering both kinetic energy and gravitational potential energy:

\[
v_e = \sqrt{\frac{2 G M}{r}}
\]

Where:
- \( G \) is the gravitational constant (\(6.674 \times 10^{-11} \, \text{m}^3 \, \text{kg}^{-1} \, \text{s}^{-2}\))
- \( M \) is the mass of the celestial body (e.g., Earth, Mars, Jupiter)
- \( r \) is the radius of the celestial body

### First Cosmic Velocity (Orbital Velocity)

The **first cosmic velocity** is the velocity needed for a stable orbit around a celestial body. This is the velocity an object must have to stay in orbit without falling back to the surface. The formula for orbital velocity \( v_1 \) is:

\[
v_1 = \sqrt{\frac{G M}{r}}
\]

This velocity corresponds to the speed required to maintain a circular orbit at a specific radius.

### Second Cosmic Velocity (Escape Velocity)

The **second cosmic velocity** is the velocity needed to completely escape a celestial body’s gravitational pull. It is twice the value of the first cosmic velocity:

\[
v_2 = \sqrt{\frac{2 G M}{r}}
\]

This is the same as the formula for **escape velocity**, meaning it is the velocity required to leave the body’s gravitational influence.

### Third Cosmic Velocity (Escape from a Star System)

The **third cosmic velocity** is the velocity needed to escape the gravitational influence of the Sun (or any central star), which would enable an object to travel to another star system. This can be calculated as:

\[
v_3 = \sqrt{\frac{2 G M_{\text{star}}}{r_{\text{star}}} + \frac{2 G M_{\text{planet}}}{r_{\text{planet}}}}
\]

Where:
- \( M_{\text{star}} \) is the mass of the central star (e.g., the Sun)
- \( r_{\text{star}} \) is the distance from the star (in this case, the distance from the Sun to the planet, like Earth)
- \( M_{\text{planet}} \) and \( r_{\text{planet}} \) are the mass and radius of the planet from which the object is escaping.

---

## 2. Practical Applications

### Escape Velocities and Space Exploration

- **Launching Satellites**: The first cosmic velocity is essential for launching satellites into orbit. For example, satellites orbiting Earth need to reach the first cosmic velocity to avoid falling back to Earth.
  
- **Interplanetary Missions**: The second cosmic velocity is required for missions that escape Earth's gravity, such as spacecraft heading to other planets or the Moon.

- **Interstellar Travel**: The third cosmic velocity is theoretical for interstellar travel, as it involves escaping the gravitational pull of the Sun to reach another star system.

---

## 3. Implementation (Python Simulation)

Below is a Python script that calculates and visualizes the escape velocities and cosmic velocities for different celestial bodies, including Earth, Mars, and Jupiter.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)

# Celestial bodies: (Mass in kg, Radius in meters)
bodies = {
    "Earth": {"M": 5.972 * 10**24, "r": 6.371 * 10**6},
    "Mars": {"M": 0.64171 * 10**24, "r": 3.396 * 10**6},
    "Jupiter": {"M": 1.898 * 10**27, "r": 6.991 * 10**7}
}

# Function to calculate escape and cosmic velocities
def escape_velocity(M, r):
    return np.sqrt(2 * G * M / r)

def first_cosmic_velocity(M, r):
    return np.sqrt(G * M / r)

def third_cosmic_velocity(M_star, r_star, M_planet, r_planet):
    return np.sqrt((2 * G * M_star / r_star) + (2 * G * M_planet / r_planet))

# Calculate velocities
velocities = {}
for body, params in bodies.items():
    M = params["M"]
    r = params["r"]
    
    v1 = first_cosmic_velocity(M, r)
    v2 = escape_velocity(M, r)
    
    # Using the Sun's mass and Earth's distance for third cosmic velocity calculation
    if body == "Earth":
        v3 = third_cosmic_velocity(1.989 * 10**30, 1.496 * 10**11, M, r)  # Sun's mass and Earth's distance
    else:
        v3 = np.nan  # Not calculating third cosmic velocity for Mars and Jupiter here
    
    velocities[body] = {"v1": v1, "v2": v2, "v3": v3}

# Plotting the velocities
fig, ax = plt.subplots(figsize=(10, 6))
bodies_names = list(bodies.keys())
v1_values = [velocities[body]["v1"] for body in bodies_names]
v2_values = [velocities[body]["v2"] for body in bodies_names]
v3_values = [velocities[body]["v3"] if not np.isnan(velocities[body]["v3"]) else np.nan for body in bodies_names]

bar_width = 0.25
index = np.arange(len(bodies_names))

# Plot bars for each velocity type
ax.bar(index, v1_values, bar_width, label='First Cosmic Velocity (Orbital Velocity)')
ax.bar(index + bar_width, v2_values, bar_width, label='Second Cosmic Velocity (Escape Velocity)')
ax.bar(index + 2 * bar_width, v3_values, bar_width, label='Third Cosmic Velocity')

# Formatting the chart
ax.set_xlabel('Celestial Bodies')
ax.set_ylabel('Velocity (m/s)')
ax.set_title('Cosmic Velocities for Different Celestial Bodies')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(bodies_names)
ax.legend()

plt.show()
