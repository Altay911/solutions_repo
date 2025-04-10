# Problem 2

# Forced Damped Pendulum Simulation

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants and Parameters
g = 9.81        # gravitational acceleration (m/s^2)
L = 1.0         # length of pendulum (m)
b = 0.5         # damping coefficient
A = 1.2         # driving force amplitude
omega_d = 2.0   # driving frequency (rad/s)

# Time span
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Initial conditions: [theta, omega]
y0 = [0.2, 0.0]

# Differential equation for the forced damped pendulum
def pendulum_ode(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -b * omega - (g / L) * np.sin(theta) + A * np.sin(omega_d * t)
    return [dtheta_dt, domega_dt]

# Solve ODE
sol = solve_ivp(pendulum_ode, t_span, y0, t_eval=t_eval, method='RK45')

# Plot theta vs time
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0])
plt.title('Forced Damped Pendulum: Angular Displacement vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.grid(True)
plt.show()

# Phase Portrait
plt.figure(figsize=(6, 6))
plt.plot(sol.y[0], sol.y[1], lw=0.5)
plt.title('Phase Portrait')
plt.xlabel('Theta (rad)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid(True)
plt.show()

# Poincaré Section (stroboscopic map)
t_poincare = np.arange(0, t_span[1], 2 * np.pi / omega_d)
poincare_indices = [np.argmin(np.abs(sol.t - tp)) for tp in t_poincare if tp <= sol.t[-1]]
theta_poincare = sol.y[0][poincare_indices]
omega_poincare = sol.y[1][poincare_indices]

plt.figure(figsize=(6, 6))
plt.scatter(theta_poincare, omegapoincare := omega_poincare, s=1)
plt.title('Poincaré Section')
plt.xlabel('Theta (rad)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid(True)
plt.show()

# Theory Section
"""
Theoretical Background:
The forced damped pendulum is governed by the second-order nonlinear differential equation:
    θ'' + bθ' + (g/L)sin(θ) = A sin(ω_d t)
Where:
- b is the damping coefficient
- A is the amplitude of the driving force
- ω_d is the driving frequency
- g is gravitational acceleration
- L is the length of the pendulum

For small-angle approximation (θ ≈ sin(θ)), the equation simplifies to a linear differential equation:
    θ'' + bθ' + (g/L)θ = A sin(ω_d t)

This equation resembles a driven harmonic oscillator and exhibits resonance when the driving frequency is near the system's natural frequency √(g/L).

As parameters like A, b, and ω_d vary, the system can show:
- Periodic behavior
- Quasiperiodic orbits
- Chaotic dynamics

Applications:
- Suspension bridges under oscillatory load
- Driven RLC electrical circuits
- Human biomechanical gait modeling

Limitations:
- No consideration for noise or complex driving functions
- Assumes point mass pendulum and ideal hinge

Extensions:
- Add noise terms or nonlinear damping
- Study bifurcation diagrams for chaos threshold
- Consider time-dependent damping or frequency
"""
