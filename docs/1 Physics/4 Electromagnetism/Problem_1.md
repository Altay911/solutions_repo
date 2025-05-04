# Electromagnetism: Simulating the Lorentz Force

## Problem Statement
The Lorentz force, given by \(\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B}\), describes the motion of charged particles in electric (\(\mathbf{E}\)) and magnetic (\(\mathbf{B}\)) fields. This simulation explores the trajectories of charged particles under various field configurations to understand phenomena like circular motion, helical paths, and drift velocities.

---

## Objectives
1. **Explore Applications**: Investigate systems where the Lorentz force is critical (e.g., cyclotrons, mass spectrometers).  
2. **Simulate Particle Motion**: Visualize trajectories under:  
   - Uniform magnetic fields.  
   - Combined electric and magnetic fields.  
   - Crossed fields.  
3. **Parameter Exploration**: Study the effects of field strengths (\(E, B\)), initial velocity (\(v\)), and particle properties (\(q, m\)).  
4. **Visualization**: Generate 2D/3D plots highlighting key phenomena like the Larmor radius and drift velocity.  

---

## Python Simulation

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorentz_force(q, E, v, B):
    """Compute the Lorentz force on a charged particle."""
    return q * E + q * np.cross(v, B)

def simulate_trajectory(q, m, E, B, v0, dt=0.01, steps=1000):
    """Simulate particle trajectory using the Runge-Kutta method."""
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0], v[0] = np.array([0, 0, 0]), v0

    for i in range(1, steps):
        F = lorentz_force(q, E, v[i-1], B)
        a = F / m
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt

    return r

# Example: Uniform magnetic field (Bz) with initial velocity (vx, 0, 0)
q, m = 1.6e-19, 9.1e-31  # Charge of electron, mass of electron
E = np.array([0, 0, 0])
B = np.array([0, 0, 1e-3])  # 1 mT in z-direction
v0 = np.array([1e6, 0, 0])  # Initial velocity: 1e6 m/s along x

trajectory = simulate_trajectory(q, m, E, B, v0)

# Plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], label='Particle Path')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Particle Trajectory in Uniform Magnetic Field')
plt.legend()
plt.show()