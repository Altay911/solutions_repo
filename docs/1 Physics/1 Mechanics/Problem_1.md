# PROBLEM 1 


## Motivation Investigating the Range as a Function of the Angle of Projection


Projectile motion, while seemingly simple, offers a rich playground for exploring fundamental principles of physics. The basic idea is straightforward: analyze how the **range** of a projectile depends on its **angle of projection**. Yet, beneath this simplicity lies a complex and versatile framework.

What makes this topic compelling is the number of **free parameters** involved—such as **initial velocity**, **gravitational acceleration**, and **launch height**. These parameters allow for a diverse set of solutions that describe phenomena ranging from the arc of a soccer ball to the trajectory of a rocket.

---

## 1. Theoretical Foundation

We start with the fundamental equations of motion under constant acceleration due to gravity, assuming no air resistance.

### Equations of Motion

Let:
- \( v_0 \): Initial velocity
- \( \theta \): Angle of projection
- \( g \): Acceleration due to gravity (typically \( 9.81 \, \text{m/s}^2 \))
- \( R \): Horizontal range

Decomposing the motion:

- Horizontal component:  
  \[
  v_{x} = v_0 \cos(\theta)
  \]
- Vertical component:  
  \[
  v_{y} = v_0 \sin(\theta)
  \]

Time of flight \( T \) (for level ground):

\[
T = \frac{2 v_0 \sin(\theta)}{g}
\]

**Range** is then:

\[
R(\theta) = v_{x} \cdot T = \frac{v_0^2 \sin(2\theta)}{g}
\]

---

## 2. Analysis of the Range

### Effect of Angle on Range

- The range is maximized when \( \sin(2\theta) \) is maximized.
- Max value of \( \sin(2\theta) \) is 1 when \( 2\theta = 90^\circ \) → \( \theta = 45^\circ \)

### Effect of Initial Velocity

- Range increases **quadratically** with \( v_0 \):  
  \[
  R \propto v_0^2
  \]

### Effect of Gravitational Acceleration

- Range is **inversely proportional** to \( g \):  
  \[
  R \propto \frac{1}{g}
  \]

---

## 3. Practical Applications

Real-world projectile motion often includes:

- Uneven terrain (non-zero launch and landing height)
- Air resistance (drag)
- Wind or spin (Magnus effect)

To account for these, we would need to:

- Modify the equations to include **drag force** proportional to velocity.
- Adjust for **initial and final height differences**.
- Use **numerical methods** to solve non-linear equations.

---

## 4. Implementation (Python Simulation)

Below is a Python script to visualize how the **range** varies with the **angle of projection**, for different initial velocities.

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
angles = np.linspace(0, 90, 100)  # degrees
radians = np.radians(angles)

# Initial velocities to compare
initial_velocities = [10, 20, 30]

plt.figure(figsize=(10, 6))

for v0 in initial_velocities:
    range_vals = (v0**2 * np.sin(2 * radians)) / g
    plt.plot(angles, range_vals, label=f'v₀ = {v0} m/s')

plt.title("Range vs Angle of Projection")
plt.xlabel("Angle (degrees)")
plt.ylabel("Range (meters)")
plt.legend()
plt.grid(True)
plt.show()


