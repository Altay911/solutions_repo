# Problem 1

# Projectile Range as a Function of Angle of Projection

import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)

# Function to calculate range
def projectile_range(v0, theta_deg):
    theta_rad = np.radians(theta_deg)
    return (v0**2 * np.sin(2 * theta_rad)) / g

# Generate angle values
angles = np.linspace(0, 90, 500)

# Example initial velocities to compare
velocities = [10, 20, 30]  # m/s

plt.figure(figsize=(10, 6))
for v0 in velocities:
    ranges = projectile_range(v0, angles)
    plt.plot(angles, ranges, label=f"v0 = {v0} m/s")

plt.title("Projectile Range vs. Angle of Projection")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.legend()
plt.grid(True)
plt.show()

# Description of Theory
"""
Theoretical Foundation:
- Motion in 2D under gravity is governed by:
  Horizontal motion: x(t) = v0 * cos(theta) * t
  Vertical motion: y(t) = v0 * sin(theta) * t - (1/2) * g * t^2

- The range R is found by determining the time of flight T:
  At y(T) = 0:
    0 = v0 * sin(theta) * T - 0.5 * g * T^2
    => T = 2 * v0 * sin(theta) / g

- Substituting T into x(T):
    R = v0 * cos(theta) * (2 * v0 * sin(theta) / g)
    => R = (v0^2 * sin(2*theta)) / g

Observations:
- The range is maximum at 45 degrees for a flat surface.
- It is symmetric around 45 degrees (e.g., 30° and 60° give the same range).
"""

# Limitations and Extensions
"""
Limitations:
- Assumes no air resistance, flat ground, and launch/landing at same height.

Possible Improvements:
- Include air drag using numerical methods (e.g., Runge-Kutta).
- Model projectile motion from a height: affects time and thus range.
- Simulate wind or terrain changes by adjusting horizontal and vertical forces.

Real-World Applications:
- Sports (e.g., soccer, basketball shots)
- Engineering (ballistics, fireworks)
- Space science (launch trajectories)
"""
