# Projection 3: Payload Trajectory Simulator

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Constants
G = 6.67430e-11  # Gravitational constant (N·m²/kg²)
M = 5.972e24     # Earth mass (kg)
R_earth = 6.371e6  # Earth radius (m)

# Initial conditions
altitude = 500e3  # 500 km above Earth
v0 = 7500        # Initial velocity (m/s). Try 7500 (orbit) or 11000 (escape)

# Set initial position (x, y) and velocity (vx, vy)
x0 = R_earth + altitude
y0 = 0
vx0 = 0
vy0 = v0

# Simulation parameters
dt = 1           # Time step (s)
t_max = 10000    # Total simulation time (s)
steps = int(t_max / dt)

# Arrays to store positions
x = np.zeros(steps)
y = np.zeros(steps)
x[0], y[0] = x0, y0
vx, vy = vx0, vy0

# Numerical integration (Euler method)
for i in range(1, steps):
    r = np.sqrt(x[i-1]**2 + y[i-1]**2)
    if r <= R_earth:
        break  # Stop if payload hits Earth
    ax = -G * M * x[i-1] / r**3
    ay = -G * M * y[i-1] / r**3
    vx += ax * dt
    vy += ay * dt
    x[i] = x[i-1] + vx * dt
    y[i] = y[i-1] + vy * dt

# Trim unused array elements
x = x[:i]
y = y[:i]

# Plot
plt.figure(figsize=(10, 10))
earth = Circle((0, 0), R_earth, color='blue', alpha=0.3, label='Earth')
plt.gca().add_patch(earth)
plt.plot(x, y, 'r-', label=f'Payload (v0 = {v0} m/s)')
plt.scatter(x0, y0, color='green', marker='*', s=100, label='Release Point')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Payload Trajectory Near Earth')
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()