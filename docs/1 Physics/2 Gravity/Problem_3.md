# Projection 3: Trajectories of a Freely Released Payload Near Earth

## Motivation
When a payload is released from a moving rocket near Earth, its trajectory is determined by initial conditions (position, velocity, altitude) and Earth's gravitational pull. Understanding these trajectories is crucial for applications like satellite deployment, space missions, and reentry scenarios. This project combines orbital mechanics and numerical methods to simulate and analyze payload motion.

---

## Task 1: Trajectory Analysis
Possible trajectories of a payload under Earth's gravity depend on its initial velocity \( v \):  
- **Elliptical Orbit:** \( v < v_{\text{escape}} \) (bound trajectory).  
- **Parabolic Trajectory:** \( v = v_{\text{escape}} \) (marginally unbound).  
- **Hyperbolic Trajectory:** \( v > v_{\text{escape}} \) (unbound, escape velocity).  

**Escape Velocity:**  
\[
v_{\text{escape}} = \sqrt{\frac{2GM_{\text{Earth}}}{r}}
\]  
Where \( r \) is the distance from Earth's center.

---

## Task 2: Numerical Analysis
The payload's motion is governed by Newton's law of gravitation:  
\[
\frac{d^2 \mathbf{r}}{dt^2} = -\frac{GM_{\text{Earth}}}{r^3} \mathbf{r}
\]  
We solve this ODE numerically using the **Runge-Kutta 4th-order (RK4)** method.

---

## Task 3: Trajectory Scenarios
- **Orbital Insertion:** Sub-escape velocity → elliptical orbit.  
- **Reentry:** Low velocity with atmospheric drag → decayed orbit.  
- **Escape:** Hyperbolic trajectory if \( v \geq v_{\text{escape}} \).

---

## Task 4: Computational Tool (Python Implementation)

### Code
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G
from scipy.integrate import solve_ivp

# Constants
M_earth = 5.972e24  # kg
R_earth = 6.371e6   # m

def equations_of_motion(t, y):
    """ODE system for payload motion: dy/dt = [velocity, acceleration]."""
    r = np.array(y[:3])       # First 3 elements are position (x,y,z)
    v = np.array(y[3:6])      # Next 3 elements are velocity (vx,vy,vz)
    r_norm = np.linalg.norm(r)
    a = -G * M_earth * r / r_norm**3
    return np.concatenate((v, a))  # Return [vx,vy,vz,ax,ay,az]

def simulate_trajectory(initial_pos, initial_vel, t_span=(0, 10000), dt=10):
    """Simulate payload trajectory using RK4."""
    sol = solve_ivp(
        equations_of_motion,
        t_span,
        np.concatenate((initial_pos, initial_vel)),
        t_eval=np.arange(t_span[0], t_span[1], dt),
        method='RK45'
    )
    return sol.y[:3, :]  # Return position vectors

# Example: Payload released at 500 km altitude
altitude = 500e3  # 500 km
initial_pos = np.array([R_earth + altitude, 0, 0])
initial_vel = np.array([0, 7.5e3, 0])  # 7.5 km/s (elliptical orbit)

trajectory = simulate_trajectory(initial_pos, initial_vel)

# Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[0], trajectory[1], trajectory[2], 'b-', label='Payload Trajectory')

# Draw Earth as a sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = R_earth * np.cos(u)*np.sin(v)
y = R_earth * np.sin(u)*np.sin(v)
z = R_earth * np.cos(v)
ax.plot_surface(x, y, z, color='green', alpha=0.5, label='Earth')

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')
ax.set_title('Payload Trajectory Near Earth')
ax.legend()
plt.tight_layout()
plt.show()