# Projection 3: Trajectories of a Freely Released Payload Near Earth

## Theory
When a payload is released near Earth, its trajectory depends on its initial velocity and altitude. The possible trajectories are:
- **Elliptical**: Velocity below escape velocity.
- **Parabolic**: Velocity exactly at escape velocity (rare in practice).
- **Hyperbolic**: Velocity exceeds escape velocity (payload escapes Earth’s gravity).

The motion is governed by Newton’s law of gravitation:
\[
a = \frac{GM}{r^2}
\]
where \( G = 6.674 \times 10^{-11} \, \text{N·m}^2/\text{kg}^2 \), \( M = 5.972 \times 10^{24} \, \text{kg} \), and \( r = R_{\text{Earth}} + h \) (Earth’s radius \( R_{\text{Earth}} = 6.371 \times 10^6 \, \text{m} \)).

Escape velocity at altitude \( h \) is:
\[
v_{\text{escape}} = \sqrt{\frac{2GM}{R_{\text{Earth}} + h}}
\]

## Python Simulation
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # N·m²/kg²
M = 5.972e24    # Earth mass (kg)
R_earth = 6.371e6  # Earth radius (m)

# Initial conditions
h = 500e3  # Altitude (500 km)
v0 = 7600  # Initial velocity (m/s). Adjust to see different trajectories.

# Initial position and velocity (x-direction)
x0 = R_earth + h
y0 = 0
vx0 = 0
vy0 = v0

# Simulation parameters
dt = 10  # Time step (s)
t_max = 10000  # Total simulation time (s)
steps = int(t_max / dt)

# Arrays to store positions
x = np.zeros(steps)
y = np.zeros(steps)
x[0], y[0] = x0, y0
vx, vy = vx0, vy0

# Numerical integration (Euler method)
for i in range(1, steps):
    r = np.sqrt(x[i-1]**2 + y[i-1]**2)
    ax = -G * M * x[i-1] / r**3
    ay = -G * M * y[i-1] / r**3
    
    vx += ax * dt
    vy += ay * dt
    
    x[i] = x[i-1] + vx * dt
    y[i] = y[i-1] + vy * dt

# Plot trajectory
plt.figure(figsize=(8, 8))
earth = plt.Circle((0, 0), R_earth, color='blue', alpha=0.2)
plt.gca().add_patch(earth)
plt.plot(x, y, 'r--', label='Payload Trajectory')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Payload Trajectory Near Earth')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()