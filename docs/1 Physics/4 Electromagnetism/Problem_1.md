# Electromagnetism 1: Simulating Lorentz Force Effects

## Problem Statement
Simulate and analyze the motion of charged particles under various electromagnetic field configurations governed by the Lorentz force:
\[
\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B}
\]

## Physics Foundations

### Key Equations
1. **Lorentz Force**:
   \[
   \mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
   \]
2. **Equations of Motion**:
   \[
   \frac{d\mathbf{v}}{dt} = \frac{q}{m}(\mathbf{E} + \mathbf{v} \times \mathbf{B})
   \]
   \[
   \frac{d\mathbf{r}}{dt} = \mathbf{v}
   \]

### Characteristic Motions
| Field Configuration | Particle Trajectory | Physical Parameters |
|---------------------|---------------------|---------------------|
| Pure \(\mathbf{B}\) | Circular/Helical | Larmor radius \(r_L = \frac{mv_\perp}{|q|B}\) |
| \(\mathbf{E} + \mathbf{B}\) | Drift motion | \(\mathbf{v}_E = \frac{\mathbf{E} \times \mathbf{B}}{B^2}\) |
| Crossed fields | Cycloid | Drift velocity dependent on \(E/B\) ratio |

## Numerical Implementation

### Simulation Algorithm (Runge-Kutta 4th Order)
```python
# Pseudocode for RK4 implementation
def lorentz_force(q, m, E, B, v):
    return q*(E + np.cross(v,B)) / m

def rk4_step(r, v, dt, q, m, E, B):
    k1v = lorentz_force(q, m, E, B, v)
    k1r = v
    # ... complete RK4 steps ...
    return r_new, v_new