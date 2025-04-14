# Problem 3
# Trajectories of a Freely Released Payload Near Earth

## Motivation

When an object is released from a moving rocket near Earth, its trajectory is determined by initial conditions such as position, velocity, and altitude, along with gravitational forces. This problem blends principles of orbital mechanics and numerical methods. Understanding these trajectories is crucial for space missions, including payload deployment, orbital insertion, reentry, and escape scenarios.

---

## 1. Theoretical Foundation

The trajectory of a payload released near Earth is influenced by Earth's gravitational pull, which follows **Newton's Law of Gravitation**. The law states that the gravitational force between two objects is proportional to their masses and inversely proportional to the square of the distance between their centers:

\[
F = \frac{G M_1 M_2}{r^2}
\]

Where:
- \( F \) is the gravitational force
- \( G \) is the gravitational constant (\(6.674 \times 10^{-11} \, \text{m}^3 \, \text{kg}^{-1} \, \text{s}^{-2}\))
- \( M_1 \) and \( M_2 \) are the masses of the two objects (in this case, Earth and the payload)
- \( r \) is the distance between the centers of the two objects

The gravitational acceleration \( g \) near Earth's surface is approximately \(9.8 \, \text{m/s}^2\), but this changes with altitude. 

### Types of Trajectories

1. **Parabolic Trajectory**: If the velocity is less than the escape velocity but sufficient to overcome Earth's gravitational pull, the trajectory will be a parabola.

2. **Hyperbolic Trajectory**: If the object is released with a velocity greater than the escape velocity, the trajectory will be hyperbolic, indicating that the object is escaping Earth's gravitational influence.

3. **Elliptical Trajectory**: If the object's velocity is less than the escape velocity but greater than the orbital velocity, the trajectory will be elliptical, which is characteristic of orbital motion.

### Governing Equations

For a two-body system, the trajectory of the payload is governed by the following equations derived from Newton's second law and the gravitational force:

\[
\ddot{r} = -\frac{GM}{r^2}
\]

Where \( \ddot{r} \) is the acceleration of the payload, \( r \) is the distance from the center of Earth, and \( M \) is the mass of Earth.

In the absence of air resistance, the motion can be described in polar coordinates, where the position of the object is defined by radius \( r \) and angle \( \theta \).

---

## 2. Numerical Analysis

We will use numerical methods to simulate the trajectory of the payload, considering different initial conditions (position, velocity, and altitude). Specifically, we will use **Euler’s method** to solve the equations of motion iteratively.

### Initial Conditions

- Initial position \( r_0 \): Distance from the center of the Earth (radius of Earth + altitude)
- Initial velocity \( v_0 \): The speed of the payload at the moment of release
- Initial angle \( \theta_0 \): The direction of the velocity vector
- The direction of the velocity vector determines whether the trajectory is elliptical, parabolic, or hyperbolic.

---

## 3. Implementation (Python Simulation)

Below is a Python script to simulate and visualize the trajectory of a freely released payload near Earth. This code solves the equations of motion using a simple numerical integration method (Euler’s method) and plots the resulting trajectory.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972 * 10**24  # Mass of Earth (kg)
R_earth = 6.371 * 10**6  # Radius of Earth (m)

# Initial conditions
r_0 = R_earth + 500000  # Initial position (500 km altitude)
v_0 = 8000  # Initial velocity (m/s) - roughly 8 km/s
theta_0 = 0  # Angle of velocity vector (0 for horizontal)

# Time parameters
t_max = 10000  # Maximum time for the simulation (s)
dt = 10  # Time step (s)

# Convert to polar coordinates
r = r_0  # Distance from the center of Earth
theta = theta_0  # Angle in the plane of motion
v = v_0  # Velocity magnitude
vx = v * np.cos(theta)  # Velocity in x-direction
vy = v * np.sin(theta)  # Velocity in y-direction

# Arrays to store positions for plotting
times = np.arange(0, t_max, dt)
x_vals = []
y_vals = []

# Euler's method for numerical integration
for t in times:
    # Compute gravitational force
    F_gravity = G * M_earth / r**2  # Gravitational force (N)
    ax = -F_gravity * np.cos(theta)  # Acceleration in x-direction
    ay = -F_gravity * np.sin(theta)  # Acceleration in y-direction
    
    # Update velocity and position
    vx += ax * dt  # Update velocity in x-direction
    vy += ay * dt  # Update velocity in y-direction
    r = np.sqrt(x_vals[-1]**2 + y_vals[-1]**2)  # Update radius
    x_vals.append(x_vals[-1] + vx * dt)  # Update x position
    y_vals.append(y_vals[-1] + vy * dt)  # Update y position

# Plot the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Payload Trajectory')
plt.scatter(0, 0, color='r', label='Earth')  # Earth's position
plt.title('Trajectory of a Payload Released Near Earth')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.show()
