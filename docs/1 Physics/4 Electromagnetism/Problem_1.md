# Problem 1

# Simulating the Effects of the Lorentz Force

## Motivation

The Lorentz force is the force experienced by a charged particle moving in an electric and magnetic field. The force is given by:

\[
\mathbf{F} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B})
\]

Where:
- \( \mathbf{F} \) is the Lorentz force,
- \( q \) is the charge of the particle,
- \( \mathbf{E} \) is the electric field,
- \( \mathbf{v} \) is the velocity of the particle,
- \( \mathbf{B} \) is the magnetic field.

This force governs the motion of charged particles in fields and plays a key role in many physical systems, including particle accelerators, mass spectrometers, and plasma confinement devices. Simulations of the Lorentz force help visualize and explore the complex trajectories that arise due to these fields.

---

## 1. Exploration of Applications

### Key Systems Where Lorentz Force Plays a Role:
- **Particle Accelerators**: The Lorentz force is used to accelerate charged particles in cyclotrons and synchrotrons, where electric and magnetic fields are used to steer and accelerate particles to high velocities.
- **Mass Spectrometers**: In mass spectrometers, charged particles are deflected by magnetic fields, allowing for the determination of their mass-to-charge ratio.
- **Plasma Confinement**: Magnetic fields are used to confine hot plasma in fusion reactors (e.g., Tokamaks), where the motion of charged particles is controlled by Lorentz forces.

### Relevance of Electric and Magnetic Fields:
- **Electric Fields (\( \mathbf{E} \))**: Accelerate or decelerate charged particles along the direction of the field.
- **Magnetic Fields (\( \mathbf{B} \))**: Deflect charged particles, causing them to follow curved paths, depending on their velocity and charge.

---

## 2. Simulating Particle Motion

We will simulate the motion of a charged particle under the influence of different electric and magnetic field configurations. The basic equation of motion is:

\[
m \frac{d\mathbf{v}}{dt} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B})
\]

Where:
- \( m \) is the mass of the particle,
- \( \mathbf{v} \) is the velocity of the particle,
- \( \mathbf{E} \) and \( \mathbf{B} \) are the electric and magnetic fields.

### Steps to Implement:

1. **Uniform Magnetic Field**: Simulate the motion of a charged particle in a uniform magnetic field, which results in circular motion.
2. **Combined Electric and Magnetic Fields**: Simulate the motion in both electric and magnetic fields, leading to helical trajectories.
3. **Crossed Electric and Magnetic Fields**: Simulate the motion of the particle in crossed fields (electric and magnetic fields perpendicular to each other), resulting in drift motion.
4. **Parameter Exploration**: Vary the particle’s charge, mass, velocity, and field strengths to observe their influence on the trajectory.

---

## 3. Python Implementation

Below is a Python script to simulate the motion of a charged particle under various field configurations using the Lorentz force. We will use the **Runge-Kutta method** to solve the equations of motion numerically.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = np.array([0, 0, 1])  # Magnetic field (T) along the z-axis
E = np.array([0, 0, 0])  # Electric field (V/m), assuming no electric field for simplicity

# Initial conditions
v0 = np.array([1e6, 0, 0])  # Initial velocity (m/s)
r0 = np.array([0, 0, 0])  # Initial position (m)
t_max = 10e-6  # Maximum time (s)
dt = 1e-9  # Time step (s)

# Lorentz force calculation
def lorentz_force(v, r, q, m, E, B):
    # v: velocity, r: position, q: charge, m: mass, E: electric field, B: magnetic field
    return (q / m) * (E + np.cross(v, B))

# Runge-Kutta method for numerical integration
def runge_kutta(v, r, q, m, E, B, dt):
    k1v = lorentz_force(v, r, q, m, E, B)
    k1r = v
    
    k2v = lorentz_force(v + 0.5 * k1v * dt, r + 0.5 * k1r * dt, q, m, E, B)
    k2r = v + 0.5 * k1v * dt
    
    k3v = lorentz_force(v + 0.5 * k2v * dt, r + 0.5 * k2r * dt, q, m, E, B)
    k3r = v + 0.5 * k2v * dt
    
    k4v = lorentz_force(v + k3v * dt, r + k3r * dt, q, m, E, B)
    k4r = v + k3v * dt
    
    # Update velocity and position
    v_new = v + (k1v + 2*k2v + 2*k3v + k4v) * dt / 6
    r_new = r + (k1r + 2*k2r + 2*k3r + k4r) * dt / 6
    
    return v_new, r_new

# Simulate the motion
t = np.arange(0, t_max, dt)
r = np.zeros((len(t), 3))  # Position array
v = np.zeros((len(t), 3))  # Velocity array

r[0] = r0
v[0] = v0

# Integration loop
for i in range(1, len(t)):
    v[i], r[i] = runge_kutta(v[i-1], r[i-1], q, m, E, B, dt)

# Plot the trajectory
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[:, 0], r[:, 1], r[:, 2])
ax.set_title("Trajectory of the Charged Particle")
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
plt.show()
