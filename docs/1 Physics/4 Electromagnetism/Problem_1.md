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

FUNCTION lorentz_force(q, E, v, B):
    RETURN q * (E + cross_product(v, B))

FUNCTION simulate_trajectory(q, m, E, B, v0, dt, steps):
    INITIALIZE r[steps][3], v[steps][3]
    SET r[0] = [0, 0, 0], v[0] = v0

    FOR i FROM 1 TO steps:
        a = lorentz_force(q, E, v[i-1], B) / m
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt

    RETURN r