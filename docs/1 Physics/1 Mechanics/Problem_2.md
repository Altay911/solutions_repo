# Investigating the Dynamics of a Forced Damped Pendulum

## Motivation

The **forced damped pendulum** is a beautiful mess of physics — simple at first glance, but wildly complex when you start adding damping and driving forces. Instead of a clean swing back and forth, you get a whole zoo of behavior: resonance, chaos, and quasi-periodic motion.

This system is a textbook example of how nonlinear dynamics emerge in real-world systems: from bridges vibrating in wind to circuits oscillating in sync with a signal. By tweaking a few knobs — like the damping factor, the amplitude of the driving force, or its frequency — the pendulum flips between elegant order and total chaos.

---

## 1. Theoretical Foundation

### Governing Equation

The motion of a forced damped pendulum is described by the nonlinear second-order differential equation:

\[
\frac{d^2\theta}{dt^2} + \gamma \frac{d\theta}{dt} + \omega_0^2 \sin(\theta) = A \cos(\omega t)
\]

Where:

- \( \theta(t) \): angular displacement
- \( \gamma \): damping coefficient
- \( \omega_0 \): natural frequency of the pendulum \( (\omega_0 = \sqrt{\frac{g}{L}}) \)
- \( A \): amplitude of the driving force
- \( \omega \): angular frequency of the driving force

### Small-Angle Approximation

For \( \theta \ll 1 \), we can approximate:

\[
\sin(\theta) \approx \theta
\]

This linearizes the equation:

\[
\frac{d^2\theta}{dt^2} + \gamma \frac{d\theta}{dt} + \omega_0^2 \theta = A \cos(\omega t)
\]

### Resonance

Resonance occurs when the driving frequency \( \omega \) approaches the natural frequency \( \omega_0 \). Under resonance, the amplitude of oscillation grows (limited only by damping).

---

## 2. Analysis of Dynamics

The behavior of the pendulum drastically changes with variations in:

- **Damping \( \gamma \)**: High damping smooths everything out; low damping allows buildup of energy.
- **Driving Amplitude \( A \)**: Stronger forcing leads to nonlinear and chaotic effects.
- **Driving Frequency \( \omega \)**: Dictates whether the system hits resonance or not.

### Chaos & Quasiperiodicity

When:
- Damping is moderate
- Forcing is strong
- Frequency is near resonance

...the pendulum can enter **chaotic regimes**, where tiny differences in initial conditions lead to wildly different outcomes.

---

## 3. Practical Applications

The forced damped pendulum isn’t just a classroom toy. It pops up in:

- **Energy harvesting** (piezoelectric oscillators)
- **Suspension bridges** (wind-induced vibrations)
- **AC circuits** (driven RLC circuits)
- **Biomechanics** (human walking modeled as forced oscillations)

---

## 4. Implementation (Python Simulation)

### Basic Simulation of the Forced Damped Pendulum

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
gamma = 0.5          # Damping coefficient
omega0 = 1.5         # Natural frequency
A = 1.2              # Driving force amplitude
omega_drive = 2/3    # Driving frequency
t_max = 100          # Duration
dt = 0.01            # Time step

# Differential equation
def pendulum(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -gamma * omega - omega0**2 * np.sin(theta) + A * np.cos(omega_drive * t)
    return [dtheta_dt, domega_dt]

# Initial conditions
y0 = [0.2, 0.0]  # [theta, omega]
t_eval = np.arange(0, t_max, dt)

# Solve
sol = solve_ivp(pendulum, [0, t_max], y0, t_eval=t_eval, method='RK45')

# Plot angular displacement
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='θ(t)')
plt.title("Forced Damped Pendulum Motion")
plt.xlabel("Time (s)")
plt.ylabel("Angular Displacement (rad)")
plt.grid(True)
plt.legend()
plt.show()
