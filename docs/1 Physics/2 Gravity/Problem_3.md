# Problem 3: Trajectories of a Freely Released Payload Near Earth

## Analysis of Possible Trajectories

When a payload is released near Earth, its trajectory is determined by the balance between its initial velocity and Earth's gravitational pull. The possible trajectories are:

1. **Elliptical Orbit**: Occurs when the payload's velocity is below escape velocity but sufficient to maintain an orbit. The shape becomes more elongated as velocity increases toward escape velocity.

2. **Circular Orbit**: A special case of elliptical orbit where velocity is perfectly perpendicular to gravity with magnitude:
   \[
   v_{\text{circ}} = \sqrt{\frac{GM}{r}}
   \]

3. **Parabolic Trajectory**: Achieved exactly at escape velocity. The payload will theoretically never return.

4. **Hyperbolic Trajectory**: Occurs when velocity exceeds escape velocity. The payload will escape Earth's gravitational influence entirely.

5. **Suborbital/Reentry**: If velocity is insufficient for orbit, the payload follows a ballistic arc and reenters the atmosphere.

## Key Physics Principles

### Gravitational Force
\[
F = G \frac{m_1 m_2}{r^2}
\]
- \(G\): Gravitational constant
- \(m_1, m_2\): Masses of Earth and payload
- \(r\): Distance between centers

### Critical Velocities
- **Circular Orbit Velocity**:
  \[
  v_{\text{circ}} = \sqrt{\frac{GM}{r}}
  \]
- **Escape Velocity**:
  \[
  v_{\text{escape}} = \sqrt{\frac{2GM}{r}}
  \]

### Energy Considerations
Total orbital energy determines trajectory shape:
- Negative: Elliptical/Circular (bound orbit)
- Zero: Parabolic (escape)
- Positive: Hyperbolic (escape with excess energy)

## Numerical Approach (Conceptual)

### Equations of Motion
\[
\frac{d^2 \vec{r}}{dt^2} = -\frac{GM}{r^3} \vec{r}
\]
This second-order differential equation describes the payload's acceleration due to gravity.

### Implementation Steps

1. **Initial Conditions**:
   - Position: \(\vec{r}_0 = (R_E + h, 0)\)
   - Velocity: \(\vec{v}_0 = (v_0 \cos \theta, v_0 \sin \theta)\)

2. **Numerical Integration** (Euler method example):
   ```python
   # Pseudocode
   for each time step:
       a = -GM * r / norm(r)^3
       v += a * dt
       r += v * dt