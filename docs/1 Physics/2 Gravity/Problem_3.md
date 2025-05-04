# Problem 3: Trajectories of a Freely Released Payload Near Earth

## Analysis of Possible Trajectories

When a payload is released near Earth, its trajectory depends on initial velocity and position. The possible trajectories are:

1. **Elliptical Orbit**: Velocity below escape velocity but sufficient to orbit.
2. **Circular Orbit**: Perfectly balanced velocity for a circular path.
3. **Parabolic Trajectory**: Exactly at escape velocity.
4. **Hyperbolic Trajectory**: Velocity exceeds escape velocity.
5. **Suborbital/Reentry**: Velocity too low to maintain orbit.

## Key Physics Principles

- **Newton's Law of Gravitation**:
  \[
  F = G \frac{m_1 m_2}{r^2}
  \]

- **Escape Velocity**:
  \[
  v_{\text{escape}} = \sqrt{\frac{2GM}{r}}
  \]

- **Circular Orbit Velocity**:
  \[
  v_{\text{circ}} = \sqrt{\frac{GM}{r}}
  \]

## Numerical Approach (Conceptual)

1. **Equations of Motion**:
   \[
   \frac{d^2 \vec{r}}{dt^2} = -\frac{GM}{r^3} \vec{r}
   \]

2. **Initial Conditions**:
   - Altitude (\(h\))
   - Speed (\(v_0\))
   - Flight path angle (\(\theta\))

3. **Iterative Solution**:
   - Update velocity and position at each time step \(\Delta t\):
     \[
     \vec{v}_{n+1} = \vec{v}_n + \vec{a}_n \Delta t
     \]
     \[
     \vec{r}_{n+1} = \vec{r}_n + \vec{v}_n \Delta t
     \]

## Trajectory Scenarios

| Scenario          | Condition                          | Result               |
|-------------------|------------------------------------|----------------------|
| Stable Orbit      | \(v_0 \approx v_{\text{circ}}\)    | Elliptical/Circular  |
| Reentry           | \(v_0 \ll v_{\text{circ}}\)        | Suborbital           |
| Escape            | \(v_0 \geq v_{\text{escape}}\)     | Hyperbolic           |

## Deliverables

1. **Physics Explanation**:
   - Gravitational forces
   - Orbital mechanics

2. **Visualizations**:
   - Trajectory plots
   - Velocity vs. altitude

3. **Applications**:
   - Payload deployment
   - Reentry vehicles